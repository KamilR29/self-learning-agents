"""Subagenci RAG do odpowiadania na pytania o dokumenty banku Nordvik.

Format zgodny z dokumentacją deepagents (słowniki SubAgent). Prompty ładowane
z plików ``prompts/<nazwa>.md``.

Subagenci:
  - retriever       — wyszukiwanie i odczyt dokumentów z plików,
  - graph-retriever  — pamięć grafowa (GraphRAG na Neo4j) do pytań o relacje,
  - answerer        — synteza końcowej odpowiedzi ze źródłami.
"""

from self_learning_agents.prompts_loader import load_prompt
from self_learning_agents.tools import (
    graph_add_learned_fact,
    graph_add_learning,
    graph_build,
    graph_search,
    graph_status,
    graph_update,
    list_documents,
    read_document,
    schema_add_node_type,
    schema_add_relationship_type,
    schema_show,
    search_documents,
)

retriever_subagent = {
    "name": "retriever",
    "description": (
        "Wyszukuje i czyta dokumenty banku Nordvik z plików. Deleguj tu "
        "odnajdywanie właściwych dokumentów, odczyt ich treści oraz śledzenie "
        "powiązań między dokumentami po ID (multi-hop). Przekaż konkretne pytanie "
        "lub listę ID."
    ),
    "system_prompt": load_prompt("retriever"),
    "tools": [search_documents, read_document, list_documents],
}

graph_retriever_subagent = {
    "name": "graph-retriever",
    "description": (
        "Zarządza pamięcią grafową (GraphRAG na Neo4j) zbudowaną z dokumentów "
        "Nordvik. Potrafi ją PRZESZUKIWAĆ (graph_search), BUDOWAĆ (graph_build), "
        "sprawdzać stan (graph_status) oraz AKTUALIZOWAĆ: zapisać zweryfikowany "
        "fakt (graph_add_learned_fact), zapisać jakościową wskazówkę/krytykę "
        "dowiązaną do encji (graph_add_learning) lub wykonać zapytanie Cypher "
        "(graph_update). Deleguj tu pytania o RELACJE oraz zadania zapisu wiedzy "
        "i wskazówek do grafu."
    ),
    "system_prompt": load_prompt("graph-retriever"),
    "tools": [
        graph_search, graph_build, graph_status, graph_update,
        graph_add_learned_fact, graph_add_learning,
        schema_show, schema_add_node_type, schema_add_relationship_type,
    ],
}

answerer_subagent = {
    "name": "answerer",
    "description": (
        "Przetwarza zebrane informacje z dokumentów i formułuje KONKRETNĄ, "
        "końcową odpowiedź na pytanie (z cytowaniem źródeł po ID). Deleguj tu na "
        "końcu — przekaż treść pytania oraz zebrane fakty/fragmenty dokumentów."
    ),
    "system_prompt": load_prompt("answerer"),
    "tools": [read_document],
}

verifier_subagent = {
    "name": "verifier",
    "description": (
        "Weryfikator (fact-checker): sprawdza w dokumentach, czy PROPONOWANA "
        "ODPOWIEDŹ jest prawdziwa. Deleguj tu przed zwróceniem odpowiedzi — przekaż "
        "pytanie i proponowaną odpowiedź. Zwraca werdykt (POTWIERDZONA / CZĘŚCIOWO / "
        "NIEPOTWIERDZONA) oraz listę niezgodności z poprawnymi wartościami i ID źródeł."
    ),
    "system_prompt": load_prompt("verifier"),
    "tools": [search_documents, read_document],
}

subagents = [
    retriever_subagent,
    graph_retriever_subagent,
    answerer_subagent,
    verifier_subagent,
]
