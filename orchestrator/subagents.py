"""Subagenci RAG do odpowiadania na pytania o dokumenty banku Nordvik.

Format zgodny z dokumentacją deepagents (słowniki SubAgent). Prompty ładowane
z plików ``prompts/<nazwa>.md``.
"""

from orchestrator.prompts_loader import load_prompt
from orchestrator.tools import list_documents, read_document, search_documents

retriever_subagent = {
    "name": "retriever",
    "description": (
        "Wyszukuje i czyta dokumenty banku Nordvik. Deleguj tu odnajdywanie "
        "właściwych dokumentów, odczyt ich treści oraz śledzenie powiązań między "
        "dokumentami po ID (multi-hop). Przekaż konkretne pytanie lub listę ID."
    ),
    "system_prompt": load_prompt("retriever"),
    "tools": [search_documents, read_document, list_documents],
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

subagents = [retriever_subagent, answerer_subagent]
