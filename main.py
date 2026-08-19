"""Interaktywny CLI dla agenta-orkiestratora RAG.

Użycie:
    python main.py "Twoje pytanie..."        # jednorazowe
    python main.py                            # tryb interaktywny (pętla)

Wybór pakietu agenta zmienną AGENT_PACKAGE (domyślnie "orchestrator"):
    AGENT_PACKAGE=self_learning_agents python main.py "..."   # wersja z pamięcią

Wymaga ustawionego OPENAI_API_KEY. Zmienne można umieścić w pliku .env.
"""

from __future__ import annotations

import importlib
import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage

_PACKAGE = os.environ.get("AGENT_PACKAGE", "orchestrator")
build_orchestrator = importlib.import_module(_PACKAGE).build_orchestrator


def _print_new_messages(chunk: dict) -> None:
    """Wypisz nowe wiadomości pojawiające się w strumieniu grafu."""
    for value in chunk.values():
        if not isinstance(value, dict):
            continue
        for msg in value.get("messages", []) or []:
            if not isinstance(msg, BaseMessage):
                continue
            name = getattr(msg, "name", None) or msg.type
            # Wywołania narzędzi (delegacje do subagentów, planowanie itd.)
            for call in getattr(msg, "tool_calls", None) or []:
                target = (call.get("args") or {}).get("subagent_type")
                suffix = f" → {target}" if target else ""
                print(f"  ↳ [{name}] wywołuje narzędzie: {call['name']}{suffix}")
            text = _extract_text(msg.content)
            if text:
                print(f"[{name}] {text}")


def _extract_text(content) -> str:
    """Wyciągnij czytelny tekst z treści wiadomości.

    Treść modeli 'reasoning' (np. OpenAI) to lista bloków — interesują nas tylko
    bloki tekstowe; reasoning i wywołania narzędzi pomijamy.
    """
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = [
            block["text"]
            for block in content
            if isinstance(block, dict) and block.get("type") == "text" and block.get("text")
        ]
        return "\n".join(parts).strip()
    return ""


def run_once(agent, prompt: str) -> None:
    print(f"\n=== Polecenie: {prompt} ===\n")
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": prompt}]},
        stream_mode="updates",
        config={"recursion_limit": 100},
    ):
        _print_new_messages(chunk)
    print("\n=== Gotowe ===\n")


def main() -> None:
    load_dotenv()
    agent = build_orchestrator()

    if len(sys.argv) > 1:
        run_once(agent, " ".join(sys.argv[1:]))
        return

    print("Agent-orkiestrator. Wpisz polecenie (lub 'exit', aby zakończyć).")
    while True:
        try:
            prompt = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if prompt.lower() in {"exit", "quit", "q"}:
            break
        if prompt:
            run_once(agent, prompt)


if __name__ == "__main__":
    main()
