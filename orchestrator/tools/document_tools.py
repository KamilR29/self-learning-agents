"""Narzędzia RAG nad korpusem dokumentów (konwencja LangChain ``@tool``).

Domyślnie działają na folderze ``nordvik-dataset`` w katalogu projektu. Ścieżkę
można nadpisać zmienną środowiskową ``NORDVIK_DOCS_DIR``.

Narzędzia:
    - list_documents()          — lista wszystkich dokumentów (ID + typ)
    - search_documents(query)   — wyszukiwanie po słowach kluczowych
    - read_document(doc_id)     — odczyt pełnej treści dokumentu po ID
"""

import os
import re
from functools import lru_cache
from pathlib import Path

from langchain.tools import tool

# Folder projektu: orchestrator/tools/document_tools.py -> parents[2] == korzeń repo
DEFAULT_DOCS_DIR = Path(__file__).resolve().parents[2] / "nordvik-dataset"


def _docs_dir() -> Path:
    return Path(os.environ.get("NORDVIK_DOCS_DIR", str(DEFAULT_DOCS_DIR))).resolve()


@lru_cache(maxsize=1)
def _index() -> list[dict]:
    """Zbuduj indeks dokumentów: [{id, typ, path, text}] z plików .md."""
    docs: list[dict] = []
    docs_dir = _docs_dir()
    for path in sorted(docs_dir.glob("*.md")):
        # Pomijamy pliki pomocnicze (np. mapa zbioru "00-MAPA-ZBIORU") — nazwy
        # zaczynające się od cyfry; identyfikatory dokumentów zaczynają się literą.
        if path.stem[:1].isdigit():
            continue
        text = path.read_text(encoding="utf-8")
        doc_id = _field(text, "ID") or path.stem
        typ = _field(text, "TYP") or "(nieznany typ)"
        docs.append({"id": doc_id, "typ": typ, "path": path, "text": text})
    return docs


def _field(text: str, name: str) -> str | None:
    m = re.search(rf"^{name}:\s*(.+)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def _lookup(doc_id: str) -> dict | None:
    key = doc_id.strip().lower().removesuffix(".md")
    for doc in _index():
        if doc["id"].lower() == key or doc["path"].stem.lower() == key:
            return doc
    return None


@tool
def list_documents() -> str:
    """List all available documents in the corpus (their IDs and types).

    Use this to see which documents exist before searching or reading.
    """
    docs = _index()
    if not docs:
        return f"Brak dokumentów w katalogu: {_docs_dir()}"
    lines = [f"Dostępne dokumenty ({len(docs)}):"]
    lines += [f"- {d['id']} — {d['typ']}" for d in docs]
    return "\n".join(lines)


@tool
def search_documents(query: str, limit: int = 5) -> str:
    """Search the document corpus for documents matching the query.

    Returns the most relevant documents (ID, type) with a short snippet around
    the match. Use it to find documents relevant to a question.

    Args:
        query: Search terms (e.g. "kredyt hipoteczny rata Kowalska" or "UM-7788").
        limit: Maximum number of documents to return.
    """
    terms = [t for t in re.split(r"\s+", query.lower().strip()) if t]
    if not terms:
        return "Puste zapytanie."
    scored = []
    for doc in _index():
        low = doc["text"].lower()
        score = sum(low.count(t) for t in terms)
        if score > 0:
            scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    if not scored:
        return f"Brak dokumentów pasujących do zapytania: {query!r}."

    out = [f"Znaleziono {len(scored)} dokument(ów). Najlepsze dopasowania:"]
    for score, doc in scored[:limit]:
        low = doc["text"].lower()
        pos = min((low.find(t) for t in terms if t in low), default=0)
        start = max(0, pos - 120)
        snippet = doc["text"][start:pos + 200].replace("\n", " ").strip()
        out.append(f"\n### {doc['id']} — {doc['typ']} (trafność: {score})\n…{snippet}…")
    return "\n".join(out)


@tool
def read_document(doc_id: str) -> str:
    """Read the full content of a document with the given identifier.

    Args:
        doc_id: Document identifier, e.g. "UM-7788", "DC-2201", "TO-2025-Q1".
            Case-insensitive.
    """
    doc = _lookup(doc_id)
    if doc is None:
        return (
            f"Nie znaleziono dokumentu o ID {doc_id!r}. "
            "Użyj list_documents() lub search_documents(), aby sprawdzić dostępne ID."
        )
    return doc["text"]
