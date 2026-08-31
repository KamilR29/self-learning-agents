"""Narzędzia grafu wiedzy (GraphRAG na Neo4j) dla subagenta grafowego.

Budowa, przeszukiwanie i aktualizacja grafu z dokumentów Nordvik przez
neo4j-graphrag. Ontologia grafu jest jawna i edytowalna (plik JSON) — jawny
schemat omija automatyczną walidację, która przerywała budowę, a agent może go
rozszerzać. Bez konfiguracji Neo4j narzędzia zwracają komunikat o niedostępności.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path

from langchain.tools import tool

INDEX_NAME = "nordvik_chunks"
CHUNK_LABEL = "Chunk"
EMBEDDING_PROPERTY = "embedding"
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMS = 1536


SCHEMA_PATH = Path(
    os.environ.get("SLA_GRAPH_SCHEMA", str(Path(__file__).resolve().parents[2] / "agent-memory" / "graph_schema.json"))
).resolve()


_SEED_SCHEMA: dict = {
    "node_types": [
        {"label": "Client", "description": "Klient banku (osoba lub firma)"},
        {"label": "Application", "description": "Wniosek kredytowy/produktowy (WN-...)"},
        {"label": "Decision", "description": "Decyzja kredytowa (DC-...)"},
        {"label": "Contract", "description": "Umowa / umowa kredytu/leasingu (UM-...)"},
        {"label": "RepaymentSchedule", "description": "Harmonogram spłat (HS-...)"},
        {"label": "Regulation", "description": "Regulamin produktu (REG-...)"},
        {"label": "Policy", "description": "Polityka wewnętrzna (POL-...)"},
        {"label": "RateTable", "description": "Tabela oprocentowania (TO-...)"},
        {"label": "FeeTable", "description": "Tabela opłat i prowizji (TOP-...)"},
        {"label": "SAR", "description": "Zgłoszenie transakcji podejrzanej (SAR-...)"},
        {"label": "RiskReport", "description": "Raport ryzyka klienta (RR-...)"},
        {"label": "IncomeCertificate", "description": "Zaświadczenie o dochodach (ZD-...)"},
        {"label": "TransactionHistory", "description": "Historia transakcji (HT-...)"},
        {"label": "Account", "description": "Rachunek bankowy / IBAN"},
        {"label": "Property", "description": "Nieruchomość lub przedmiot zabezpieczenia"},
    ],
    "relationship_types": [
        "CONCERNS_CLIENT", "DECISION_FOR", "REALIZES", "ATTACHED_TO",
        "APPLIES_POLICY", "GOVERNED_BY", "USES_RATE_TABLE", "USES_FEE_TABLE",
        "HAS_SCHEDULE", "FILED_FOR", "AGGREGATES", "UPDATES_RISK",
        "SECURED_BY", "HAS_ACCOUNT", "REFERENCES",
    ],
    "additional_node_types": True,
    "additional_relationship_types": True,
}

RETRIEVAL_QUERY = """
WITH node AS chunk, score
OPTIONAL MATCH (chunk)<-[:FROM_CHUNK]-(entity)
OPTIONAL MATCH (entity)-[rel]-(nb)
WHERE type(rel) <> 'FROM_CHUNK'
WITH chunk, score,
     collect(DISTINCT entity.name) AS entities,
     collect(DISTINCT coalesce(startNode(rel).name, '?') + ' -[' + type(rel) + ']-> ' + coalesce(endNode(rel).name, '?')) AS relationships
RETURN chunk.text AS text, entities, relationships, score
"""


def is_configured() -> bool:
    return all(os.environ.get(k) for k in ("NEO4J_URI", "NEO4J_USERNAME", "NEO4J_PASSWORD"))


def _not_configured_msg(tool_name: str) -> str:
    return (
        f"{tool_name} niedostępne: brak konfiguracji Neo4j (ustaw NEO4J_URI, "
        "NEO4J_USERNAME, NEO4J_PASSWORD). Skorzystaj z narzędzi plikowych zamiast zmyślać."
    )


def _load_schema() -> dict:
    if not SCHEMA_PATH.exists():
        SCHEMA_PATH.parent.mkdir(parents=True, exist_ok=True)
        SCHEMA_PATH.write_text(json.dumps(_SEED_SCHEMA, ensure_ascii=False, indent=2), encoding="utf-8")
        return dict(_SEED_SCHEMA)
    data = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    data.setdefault("additional_node_types", True)
    data.setdefault("additional_relationship_types", True)
    return data


def _save_schema(schema: dict) -> None:
    SCHEMA_PATH.parent.mkdir(parents=True, exist_ok=True)
    SCHEMA_PATH.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")


def _run_async(coro):
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor(1) as ex:
        return ex.submit(lambda: asyncio.run(coro)).result()


@lru_cache(maxsize=1)
def get_driver():
    import neo4j
    return neo4j.GraphDatabase.driver(
        os.environ["NEO4J_URI"],
        auth=(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]),
    )


@lru_cache(maxsize=1)
def _embedder():
    from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)


def count_learned_nodes() -> int:
    """Liczba węzłów wiedzy dopisanych przez agenta (:LearnedFact + :Learning).

    Mierzy aktualizacje pamięci grafowej wprost z bazy — zapisy subagentów nie
    wypływają na strumień orkiestratora. Zwraca -1, gdy Neo4j jest niedostępny.
    """
    if not is_configured():
        return -1
    try:
        records, _, _ = get_driver().execute_query(
            "MATCH (n) WHERE n:LearnedFact OR n:Learning RETURN count(n) AS c"
        )
        return int(records[0]["c"]) if records else 0
    except Exception:
        return -1


@lru_cache(maxsize=1)
def _answer_llm():
    from neo4j_graphrag.llm import OpenAILLM
    return OpenAILLM(model_name="gpt-4o-mini", model_params={"temperature": 0.0})


@lru_cache(maxsize=1)
def _extraction_llm():
    from neo4j_graphrag.llm import OpenAILLM
    return OpenAILLM(
        model_name="gpt-4o-mini",
        model_params={"response_format": {"type": "json_object"}, "temperature": 0.0},
    )


@lru_cache(maxsize=1)
def _graph_rag():
    from neo4j_graphrag.generation import GraphRAG, RagTemplate
    from neo4j_graphrag.retrievers import VectorCypherRetriever

    retriever = VectorCypherRetriever(
        get_driver(), index_name=INDEX_NAME, embedder=_embedder(),
        retrieval_query=RETRIEVAL_QUERY,
    )
    template = RagTemplate(
        template=(
            "Odpowiedz na PYTANIE wyłącznie na podstawie KONTEKSTU (fragmenty i "
            "relacje z grafu wiedzy). Nie dodawaj informacji spoza kontekstu. "
            "Podaj konkretną odpowiedź.\n\n# PYTANIE:\n{query_text}\n\n"
            "# KONTEKST:\n{context}\n\n# ODPOWIEDŹ:\n"
        ),
        expected_inputs=["query_text", "context"],
    )
    return GraphRAG(llm=_answer_llm(), retriever=retriever, prompt_template=template)


async def _build_graph(limit: int | None) -> str:
    from neo4j_graphrag.experimental.components.text_splitters.fixed_size_splitter import (
        FixedSizeSplitter,
    )
    from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline
    from neo4j_graphrag.indexes import create_vector_index
    from self_learning_agents.tools.document_tools import _index


    pipeline = SimpleKGPipeline(
        llm=_extraction_llm(),
        driver=get_driver(),
        embedder=_embedder(),
        schema=_load_schema(),
        text_splitter=FixedSizeSplitter(chunk_size=800, chunk_overlap=150),
        from_pdf=False,
        perform_entity_resolution=True,
        on_error="IGNORE",
    )
    docs = _index()
    if limit:
        docs = docs[:limit]
    total = len(docs)
    ok, failed = 0, []
    for i, doc in enumerate(docs, 1):
        print(f"      [graf] ({i}/{total}) ekstrakcja: {doc['id']} ...", flush=True)
        try:
            await pipeline.run_async(text=f"[DOKUMENT {doc['id']}]\n{doc['text']}")
            ok += 1
        except Exception as exc:  # jeden dokument nie przerywa całości
            failed.append(doc["id"])
            print(f"      [graf] pominięto {doc['id']}: {exc!r}", flush=True)


    try:
        create_vector_index(
            get_driver(), name=INDEX_NAME, label=CHUNK_LABEL,
            embedding_property=EMBEDDING_PROPERTY, dimensions=EMBEDDING_DIMS,
            similarity_fn="cosine",
        )
    except Exception:
        pass
    msg = f"Zbudowano graf: {ok}/{total} dokumentów; indeks '{INDEX_NAME}' gotowy."
    if failed:
        msg += f" Pominięto {len(failed)}: {', '.join(failed)}."
    return msg


@tool
def graph_build(limit: int = 0) -> str:
    """Zbuduj/odśwież graf wiedzy Neo4j z dokumentów Nordvik.

    Korzysta z edytowalnej ontologii (schema_show / schema_add_*) jako jawnego
    schematu; LLM może też dodawać nowe typy w locie. Zapisuje fragmenty +
    embeddingi i tworzy indeks wektorowy. Dokument, którego ekstrakcja się nie
    powiedzie, jest pomijany — to nie przerywa całości.

    Args:
        limit: Ile dokumentów wczytać (0 = wszystkie). Mała wartość na potrzeby testu.
    """
    if not is_configured():
        return _not_configured_msg("graph_build")
    try:
        return _run_async(_build_graph(limit or None))
    except Exception as exc:
        hint = " UWAGA: brak wtyczki APOC w Neo4j." if "apoc" in repr(exc).lower() else ""
        return f"graph_build błąd: {exc!r}.{hint}"


@tool
def graph_search(query: str, top_k: int = 8) -> str:
    """Przeszukaj graf wiedzy Neo4j (GraphRAG) zbudowany z dokumentów Nordvik.

    Wyszukiwanie wektorowe po fragmentach plus przejście po wydobytych encjach
    i relacjach. Najlepsze do pytań o powiązania / wielostopniowych.

    Args:
        query: Pytanie w języku naturalnym.
        top_k: Ile fragmentów pobrać jako kontekst.
    """
    if not is_configured():
        return _not_configured_msg("graph_search")
    try:
        result = _graph_rag().search(query, retriever_config={"top_k": top_k})
        return result.answer or "(graf nie zwrócił odpowiedzi)"
    except Exception as exc:
        return (
            f"graph_search błąd: {exc!r}. Czy graf został zbudowany (graph_build)? "
            "Sprawdź też połączenie z Neo4j."
        )


@tool
def graph_update(cypher: str) -> str:
    """Zaktualizuj graf wiedzy zapytaniem zapisującym w Cypher (MERGE/SET/DELETE).

    Używaj MERGE zamiast CREATE, aby unikać duplikatów.

    Args:
        cypher: Zapytanie zapisujące w języku Cypher.
    """
    if not is_configured():
        return _not_configured_msg("graph_update")
    try:
        _, summary, _ = get_driver().execute_query(cypher)
        c = summary.counters
        return (
            "OK. Zmiany: "
            f"węzły +{c.nodes_created}/-{c.nodes_deleted}, "
            f"relacje +{c.relationships_created}/-{c.relationships_deleted}, "
            f"właściwości ustawione: {c.properties_set}."
        )
    except Exception as exc:
        return f"graph_update błąd: {exc!r}. Sprawdź składnię Cypher i połączenie z Neo4j."


@tool
def graph_status() -> str:
    """Zwróć stan grafu wiedzy (liczba węzłów/relacji, indeks wektorowy)."""
    if not is_configured():
        return _not_configured_msg("graph_status")
    try:
        driver = get_driver()
        nodes, _, _ = driver.execute_query("MATCH (n) RETURN count(n) AS c")
        rels, _, _ = driver.execute_query("MATCH ()-[r]->() RETURN count(r) AS c")
        idx, _, _ = driver.execute_query(
            "SHOW INDEXES YIELD name WHERE name=$n RETURN count(*) AS c", n=INDEX_NAME
        )
        return (
            f"Graf: {nodes[0]['c']} węzłów, {rels[0]['c']} relacji; "
            f"indeks '{INDEX_NAME}' {'istnieje' if idx[0]['c'] else 'NIE istnieje'}."
        )
    except Exception as exc:
        return f"graph_status błąd: {exc!r}. Sprawdź połączenie z Neo4j."


@tool
def graph_add_learned_fact(question: str, answer: str, sources: str = "") -> str:
    """Zapisz w grafie nauczony fakt (pytanie–odpowiedź), by graph_search go znalazł.

    Zapisywany jako węzeł :Chunk:LearnedFact z embeddingiem, więc trafia do
    indeksu wektorowego i jest odnajdywany następnym razem — graf faktycznie się uczy.

    Args:
        question: Pytanie, na które udzielono odpowiedzi.
        answer: Zweryfikowana odpowiedź.
        sources: ID dokumentów źródłowych po przecinku (opcjonalnie).
    """
    if not is_configured():
        return _not_configured_msg("graph_add_learned_fact")
    try:
        text = f"Nauczony fakt — Pytanie: {question}\nOdpowiedź: {answer}\nŹródła: {sources}"
        emb = _embedder().embed_query(text)
        fid = "learned::" + hashlib.sha1(question.lower().encode("utf-8")).hexdigest()[:16]
        get_driver().execute_query(
            "MERGE (f:Chunk:LearnedFact {id:$id}) "
            "SET f.text=$text, f.embedding=$emb, f.sources=$src, f.learned_at=datetime()",
            id=fid, text=text, emb=emb, src=sources,
        )
        return f"Zapisano nauczony fakt do grafu (id {fid})."
    except Exception as exc:
        return f"graph_add_learned_fact błąd: {exc!r}."


@tool
def graph_add_learning(question: str, critique: str, entity_ids: str = "") -> str:
    """Dopisz do grafu jakościową wskazówkę/krytykę, powiązaną z właściwymi węzłami.

    Zapisuje węzeł :Chunk:Learning (z embeddingiem, więc wyszukiwalny) i łączy go
    z węzłami encji wskazanymi w pytaniu (np. WN-4501) relacjami :HINT_FOR / :FROM_CHUNK.
    Stosuj do feedbacku typu „załącznik dobrze, ale dochód netto źle; brakuje DC-2201” —
    BEZ podawania konkretnych poprawnych wartości.

    Args:
        question: Pytanie, którego dotyczy wskazówka (do embeddingu wyszukiwania).
        critique: Jakościowa uwaga (co było źle / co spróbować), bez konkretnych wartości.
        entity_ids: ID dokumentów/encji do powiązania po przecinku (np. "WN-4501, DC-2201").
    """
    if not is_configured():
        return _not_configured_msg("graph_add_learning")
    try:
        driver = get_driver()
        emb = _embedder().embed_query(f"{question}\n{critique}")
        lid = "learning::" + hashlib.sha1(question.lower().encode("utf-8")).hexdigest()[:16]
        driver.execute_query(
            "MERGE (l:Chunk:Learning {id:$id}) "
            "SET l.text=$text, l.embedding=$emb, l.kind='critique', l.updated_at=datetime()",
            id=lid, text=critique, emb=emb,
        )
        ids = [x.strip() for x in entity_ids.split(",") if x.strip()]
        linked = 0
        if ids:
            recs, _, _ = driver.execute_query(
                "MATCH (l:Learning {id:$id}) UNWIND $ids AS eid "
                "MATCH (e) WHERE (e.name CONTAINS eid OR e.id CONTAINS eid) AND NOT e:Learning AND NOT e:Chunk "
                "MERGE (l)-[:HINT_FOR]->(e) MERGE (e)-[:FROM_CHUNK]->(l) "
                "RETURN count(DISTINCT e) AS c",
                id=lid, ids=ids,
            )
            linked = recs[0]["c"] if recs else 0
        return f"Zapisano wskazówkę do grafu (id {lid}); powiązano z {linked} węzłami."
    except Exception as exc:
        return f"graph_add_learning błąd: {exc!r}."


@tool
def schema_show() -> str:
    """Pokaż bieżącą ontologię grafu (typy węzłów i relacji).

    Ontologia steruje graph_build; możesz ją rozszerzyć narzędziami
    schema_add_node_type i schema_add_relationship_type.
    """
    s = _load_schema()
    nodes = ", ".join(
        f"{n['label']}" if isinstance(n, dict) else str(n) for n in s.get("node_types", [])
    )
    rels = ", ".join(s.get("relationship_types", []))
    return (
        f"Ontologia grafu (plik: {SCHEMA_PATH.name}):\n"
        f"- typy węzłów: {nodes or '(brak)'}\n"
        f"- typy relacji: {rels or '(brak)'}\n"
        f"- LLM może dodawać własne typy: {s.get('additional_node_types', True)}"
    )


@tool
def schema_add_node_type(label: str, description: str = "") -> str:
    """Dodaj typ węzła (etykietę) do edytowalnej ontologii grafu.

    Args:
        label: Nowa etykieta węzła, np. "Guarantor".
        description: Krótki opis, co reprezentuje ten typ encji.
    """
    s = _load_schema()
    labels = {(n["label"] if isinstance(n, dict) else n) for n in s.get("node_types", [])}
    if label in labels:
        return f"Typ węzła '{label}' już istnieje w ontologii."
    s.setdefault("node_types", []).append({"label": label, "description": description})
    _save_schema(s)
    return f"Dodano typ węzła '{label}' do ontologii. Zadziała przy kolejnym graph_build."


@tool
def schema_add_relationship_type(rel_type: str) -> str:
    """Dodaj typ relacji do edytowalnej ontologii grafu.

    Args:
        rel_type: Nowy typ relacji, np. "GUARANTEES" (UPPER_SNAKE_CASE).
    """
    s = _load_schema()
    rt = rel_type.strip().upper().replace(" ", "_")
    if rt in s.get("relationship_types", []):
        return f"Typ relacji '{rt}' już istnieje w ontologii."
    s.setdefault("relationship_types", []).append(rt)
    _save_schema(s)
    return f"Dodano typ relacji '{rt}' do ontologii. Zadziała przy kolejnym graph_build."
