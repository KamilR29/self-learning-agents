"""Narzędzia pamięci grafowej (GraphRAG na Neo4j) dla subagenta grafowego.

Subagent BUDUJE, PRZESZUKUJE i AKTUALIZUJE graf wiedzy z dokumentów Nordvik
(biblioteka ``neo4j-graphrag``), a także zarządza EDYTOWALNĄ ONTOLOGIĄ (schematem)
grafu — jawny schemat unika automatycznej walidacji, która przerywała budowę,
a jednocześnie agent może go rozszerzać (`additional_*` pozwala LLM dodawać typy).

Narzędzia:
  - graph_build(limit)                     — budowa/odświeżenie grafu (schema z pliku),
  - graph_search(query)                    — przeszukiwanie (retrieval + relacje),
  - graph_update(cypher)                   — aktualizacja grafu (Cypher),
  - graph_status()                         — stan grafu,
  - schema_show()                          — pokaż ontologię (typy węzłów i relacji),
  - schema_add_node_type(label, desc)      — dodaj typ węzła do ontologii,
  - schema_add_relationship_type(rtype)    — dodaj typ relacji do ontologii.

Bezpieczna degradacja: bez konfiguracji Neo4j narzędzia zgłaszają niedostępność.
Wymaga pakietów ``neo4j`` i ``neo4j-graphrag`` oraz OPENAI_API_KEY.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path

from langchain.tools import tool

# --------------------------------------------------------------------------- #
# Konfiguracja                                                                  #
# --------------------------------------------------------------------------- #
INDEX_NAME = "nordvik_chunks"
CHUNK_LABEL = "Chunk"
EMBEDDING_PROPERTY = "embedding"
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMS = 1536

# Ścieżka edytowalnej ontologii (część pamięci agenta).
SCHEMA_PATH = Path(
    os.environ.get("SLA_GRAPH_SCHEMA", str(Path(__file__).resolve().parents[2] / "agent-memory" / "graph_schema.json"))
).resolve()

# Ontologia bazowa (seed) — dopasowana do dokumentów Nordvik. Agent może ją
# rozszerzać (schema_add_*), a LLM dodawać typy w locie (additional_*=True).
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


# --------------------------------------------------------------------------- #
# Edytowalna ontologia (schemat) — plik JSON                                    #
# --------------------------------------------------------------------------- #
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


# --------------------------------------------------------------------------- #
# Leniwe zasoby                                                                 #
# --------------------------------------------------------------------------- #
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
    """Liczba węzłów WIEDZY dopisanych przez agenta (:LearnedFact + :Learning).

    Służy do POMIARU aktualizacji pamięci grafowej z samej bazy (niezależnie od
    strumienia agenta — subagenci są uruchamiani przez ``.invoke``, więc ich
    zapisy do grafu nie wypływają na strumień orkiestratora). Zwraca ``-1``, gdy
    Neo4j nie jest skonfigurowany lub odczyt się nie powiódł.
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

    # JAWNY schemat (z pliku) — pomija automatyczną walidację schematu, która
    # przerywała build; additional_*=True pozwala LLM dodawać własne typy.
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
        except Exception as exc:  # pojedynczy dokument nie przerywa całości
            failed.append(doc["id"])
            print(f"      [graf] pominięto {doc['id']}: {exc!r}", flush=True)

    # Indeks wektorowy tworzymy ZAWSZE na końcu (nawet po pominięciach).
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


# --------------------------------------------------------------------------- #
# Narzędzia: budowa / przeszukiwanie / aktualizacja / stan                      #
# --------------------------------------------------------------------------- #
@tool
def graph_build(limit: int = 0) -> str:
    """Build/refresh the Neo4j knowledge graph from the Nordvik documents.

    Uses the editable ontology (schema_show / schema_add_*) as an explicit schema;
    the LLM may also add new types on the fly. Stores chunks + embeddings and
    creates the vector index. A document that fails extraction is skipped, not fatal.

    Args:
        limit: How many documents to ingest (0 = all). Use a small number to test.
    """
    if not is_configured():
        return _not_configured_msg("graph_build")
    try:
        return _run_async(_build_graph(limit or None))
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        hint = " UWAGA: brak wtyczki APOC w Neo4j." if "apoc" in repr(exc).lower() else ""
        return f"graph_build błąd: {exc!r}.{hint}"


@tool
def graph_search(query: str, top_k: int = 8) -> str:
    """Search the Neo4j knowledge graph (GraphRAG) built from the Nordvik documents.

    Vector retrieval over chunks plus traversal over extracted entities/relationships.
    Best for relational / multi-hop questions.

    Args:
        query: The question in natural language.
        top_k: How many chunks to retrieve as context (default 5).
    """
    if not is_configured():
        return _not_configured_msg("graph_search")
    try:
        result = _graph_rag().search(query, retriever_config={"top_k": top_k})
        return result.answer or "(graf nie zwrócił odpowiedzi)"
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        return (
            f"graph_search błąd: {exc!r}. Czy graf został zbudowany (graph_build)? "
            "Sprawdź też połączenie z Neo4j."
        )


@tool
def graph_update(cypher: str) -> str:
    """Update the knowledge graph by running a write Cypher query (MERGE/SET/DELETE).

    Prefer MERGE over CREATE to avoid duplicates.

    Args:
        cypher: A write Cypher statement.
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
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        return f"graph_update błąd: {exc!r}. Sprawdź składnię Cypher i połączenie z Neo4j."


@tool
def graph_status() -> str:
    """Report the state of the knowledge graph (node/relationship counts, index)."""
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
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        return f"graph_status błąd: {exc!r}. Sprawdź połączenie z Neo4j."


# --------------------------------------------------------------------------- #
# Narzędzia: EDYTOWALNA ONTOLOGIA (schemat)                                     #
# --------------------------------------------------------------------------- #
@tool
def graph_add_learned_fact(question: str, answer: str, sources: str = "") -> str:
    """Persist a learned Q&A fact into the graph so future graph_search finds it.

    Stores it as a :Chunk:LearnedFact node with an embedding, so it enters the
    vector index and is retrieved next time — the graph literally learns.

    Args:
        question: The question that was answered.
        answer: The verified answer.
        sources: Comma-separated source document IDs (optional).
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
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        return f"graph_add_learned_fact błąd: {exc!r}."


@tool
def graph_add_learning(question: str, critique: str, entity_ids: str = "") -> str:
    """Attach a qualitative learning/critique to the graph, linked to relevant nodes.

    Stores a :Chunk:Learning node (with embedding, so it is retrievable) and links it
    to the entity nodes named in the question (e.g. WN-4501) via :HINT_FOR / :FROM_CHUNK.
    Use for feedback like „attachment right, but net income wrong; missing DC-2201” —
    WITHOUT the concrete correct values.

    Args:
        question: The question this learning is about (used for retrieval embedding).
        critique: Qualitative feedback (what was wrong / to try), no concrete answer values.
        entity_ids: Comma-separated document/entity IDs to link (e.g. "WN-4501, DC-2201").
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
    except Exception as exc:  # pragma: no cover - zależne od Neo4j
        return f"graph_add_learning błąd: {exc!r}."


@tool
def schema_show() -> str:
    """Show the current graph ontology (node types and relationship types).

    The ontology guides graph_build; you can extend it with schema_add_node_type
    and schema_add_relationship_type.
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
    """Add a node type (label) to the editable graph ontology.

    Args:
        label: New node label, e.g. "Guarantor".
        description: Short description of what this entity type represents.
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
    """Add a relationship type to the editable graph ontology.

    Args:
        rel_type: New relationship type, e.g. "GUARANTEES" (UPPER_SNAKE_CASE).
    """
    s = _load_schema()
    rt = rel_type.strip().upper().replace(" ", "_")
    if rt in s.get("relationship_types", []):
        return f"Typ relacji '{rt}' już istnieje w ontologii."
    s.setdefault("relationship_types", []).append(rt)
    _save_schema(s)
    return f"Dodano typ relacji '{rt}' do ontologii. Zadziała przy kolejnym graph_build."
