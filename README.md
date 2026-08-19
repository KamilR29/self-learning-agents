# Agent-orkiestrator RAG (deepagents)

System Q&A (prosty **RAG**) nad zbiorem dokumentów fikcyjnego banku
**Nordvik Finanse S.A.** ([`nordvik-dataset/`](nordvik-dataset)), zbudowany na
bibliotece [`deepagents`](https://github.com/langchain-ai/deepagents) (LangGraph).

Główny agent (**orkiestrator**) nie odpowiada sam — **planuje** i **deleguje**
pod-zadania do subagentów przez wbudowane narzędzie `task`. Odpowiedzi powstają
**wyłącznie** na podstawie treści dokumentów (agenci mają narzędzia do ich
czytania), z podaniem **źródeł** (ID dokumentów).

## Architektura

```
                        ┌─────────────────────────┐
   pytanie ───────────► │      ORKIESTRATOR        │
   użytkownika          │  plan + delegowanie +    │
                        │  odpowiedź ze źródłami   │
                        └──────┬──────────────┬────┘
                          task │              │ task
                               ▼              ▼
                  ┌────────────────────┐  ┌────────────────────┐
                  │     retriever      │  │      answerer      │
                  │ search_documents   │  │ read_document      │
                  │ read_document      │  │ (synteza odpowiedzi│
                  │ list_documents     │  │  ze źródłami)      │
                  └──────────┬─────────┘  └─────────┬──────────┘
                             ▼                      ▼
                              nordvik-dataset/
                              (50 dokumentów .md)
```

- **retriever** — wyszukuje i czyta dokumenty, śledzi powiązania po ID (multi-hop).
- **answerer** — przetwarza zebrane informacje i formułuje konkretną odpowiedź ze źródłami.

Narzędzia RAG czytają pliki `.md` bezpośrednio z folderu `nordvik-dataset`
(plik pomocniczy `00-MAPA-ZBIORU.md` jest wykluczony z korpusu). Orkiestrator
dostaje od `deepagents` również `task` (delegacja) i `write_todos` (planowanie).

## Struktura projektu

| Plik | Rola |
|------|------|
| `orchestrator/agent.py` | `build_orchestrator()` — składa graf przez `create_deep_agent` |
| `orchestrator/subagents.py` | subagent `retriever` (format `SubAgent`) |
| `orchestrator/tools/` | pakiet narzędzi RAG (`@tool`): `list_documents`, `search_documents`, `read_document` |
| `orchestrator/prompts/*.md` | prompty: `orchestrator`, `retriever` |
| `main.py` | CLI (tryb jednorazowy i interaktywny) |

## Instalacja

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install -r requirements.txt
```

Skonfiguruj klucz (skopiuj `.env.example` do `.env`):

```bash
OPENAI_API_KEY=sk-...             # wymagane (dostawca modelu: OpenAI)
```

## Uruchomienie

```bash
python main.py "Ile wynosi rata kredytu hipotecznego Anny Kowalskiej i z czego wynika?"
```

albo tryb interaktywny:

```bash
python main.py
```

Przykładowe pytania (patrz też gotowe zestawy w [`nordvik-pytania/`](nordvik-pytania)):
- „Jaka jest kwota kredytu w umowie UM-7788?” (jeden dokument)
- „Dlaczego odrzucono wniosek WN-4508 mimo wystarczającej zdolności?” (multi-hop)
- „Prześledź łańcuch kredytu hipotecznego Anny Kowalskiej i zweryfikuj spójność liczb.” (złożone)

## Użycie z kodu

```python
from orchestrator import build_orchestrator

agent = build_orchestrator()                      # lub build_orchestrator("openai:gpt-4o-mini")
result = agent.invoke({"messages": [
    {"role": "user", "content": "Ile wynosi rata w harmonogramie HS-7788?"}
]})
print(result["messages"][-1].content)
```

## Konfiguracja korpusu

Domyślnie agent czyta dokumenty z `./nordvik-dataset`. Inny folder wskażesz
zmienną `NORDVIK_DOCS_DIR`. Dokumenty to pliki `.md`, których nazwa odpowiada
identyfikatorowi dokumentu (np. `UM-7788.md`), a treść zaczyna się od nagłówka z
polami `ID:` i `TYP:`.

## Wariant `self_learning_agents` (pamięć długoterminowa + GraphRAG)

Klon pakietu `orchestrator` rozszerzony o dwa rodzaje **dodatkowej pamięci**:

1. **Pamięć plikowa (długoterminowa, agent-scoped)** — `CompositeBackend` kieruje
   route `/memories/` do `FilesystemBackend` (`agent-memory/AGENTS.md` na dysku).
   Agent wczytuje pamięć do promptu i aktualizuje ją narzędziem `edit_file` — uczy
   się między rozmowami. Folder zmienisz zmienną `SLA_MEMORY_DIR`.
2. **Pamięć grafowa (GraphRAG na Neo4j)** — knowledge graph z dokumentów Nordvik
   (encje + relacje + embeddingi). Obsługuje ją **osobny subagent `graph-retriever`**
   (własny prompt), który sam **buduje, przeszukuje i aktualizuje** graf swoimi
   narzędziami — nie ma osobnego skryptu ingestu:
   - `graph_status()` — stan grafu (węzły/relacje, indeks),
   - `graph_build(limit)` — budowa/odświeżenie grafu (ekstrakcja schema-free),
   - `graph_search(query)` — przeszukiwanie (retrieval wektorowy + relacje),
   - `graph_update(cypher)` — aktualizacja grafu (MERGE/SET/DELETE).
   Bez konfiguracji Neo4j narzędzia zgłaszają niedostępność, a agent działa dalej
   na plikach (`retriever`).

Subagenci wariantu: `retriever` (pliki), `graph-retriever` (GraphRAG/Neo4j),
`answerer` (synteza odpowiedzi), `verifier` (fact-check w dokumentach).

**Pętla samo-uczenia i weryfikacji** (sterowana promptem orkiestratora):
1. najpierw pamięć + `graph-retriever`;
2. gdy brak odpowiedzi → `retriever` (dokumenty), a zdobyty trwały fakt orkiestrator
   dopisuje do pamięci (`edit_file` na `/memories/AGENTS.md`);
3. `answerer` formułuje odpowiedź;
4. `verifier` sprawdza ją w dokumentach — jeśli NIEPOTWIERDZONA, pętla szukania
   rusza ponownie z uwagami weryfikatora (maks. 3 rundy).

Uruchomienie wariantu z pamięcią:

```bash
AGENT_PACKAGE=self_learning_agents python main.py "Twoje pytanie..."
```

Włączenie GraphRAG (Neo4j):

```
# 1) w .env: NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD (+ OPENAI_API_KEY)
# 2) uruchom agenta (jak wyżej) i poproś o zbudowanie grafu, np.:
#    "Zbuduj graf wiedzy z dokumentów, a potem odpowiedz: jak SAR-y wpłynęły na DC-2250?"
# graph-retriever sam wywoła graph_build, a następnie graph_search.
```

Graf buduje, przeszukuje i aktualizuje **subagent `graph-retriever`** swoimi
narzędziami (`graph_build`, `graph_search`, `graph_update`, `graph_status`) —
nie ma osobnego skryptu ingestu.

Pliki wariantu: `self_learning_agents/agent.py` (backend pamięci plikowej),
`self_learning_agents/tools/graph_tools.py` (narzędzia grafowe: build/search/update/status).

## Rozbudowa

- **Nowe narzędzie RAG** (np. filtrowanie po typie dokumentu) — dodaj funkcję w
  `orchestrator/rag_tools.py` i wpisz ją do `tools` odpowiedniego subagenta.
- **Nowy subagent** — dodaj słownik w `orchestrator/subagents.py` (pola:
  `name`, `description`, `system_prompt`, opcjonalnie `tools`/`model`) i dopisz go
  do listy `subagents`; prompt umieść w `orchestrator/prompts/<name>.md`. Kluczowe
  jest dobre pole `description` — po nim orkiestrator decyduje, kiedy delegować.

## Uwaga o modelu

Domyślny model to `openai:gpt-4o-mini` (tani i szybki). Zmienisz go zmienną `ORCHESTRATOR_MODEL`
(format LangChain `provider:model`) albo argumentem `build_orchestrator(model=...)`.
Aby użyć Anthropic, ustaw `ORCHESTRATOR_MODEL=anthropic:claude-sonnet-4-5` i
`ANTHROPIC_API_KEY` (pakiet `langchain-anthropic` jest już w zależnościach `deepagents`).
