"""Budowa agenta-orkiestratora RAG z PAMIĘCIĄ długoterminową (deepagents).

Pamięć jest agent-scoped i oparta o pliki: route ``/memories/`` jest kierowany do
``FilesystemBackend`` (zapis na prawdziwy dysk, utrwalanie między rozmowami),
a pozostały filesystem działa na ``StateBackend`` (w pamięci, per rozmowa).

Agent wczytuje plik pamięci ``AGENTS.md`` do promptu na starcie i może go
aktualizować narzędziem ``edit_file`` (uczy się z interakcji między rozmowami).
"""

from __future__ import annotations

import os
from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

from self_learning_agents.prompts_loader import load_prompt
from self_learning_agents.subagents import subagents


DEFAULT_MODEL = "openai:gpt-4.1-mini"

ORCHESTRATOR_MODEL = "openai:gpt-5-mini"

MEMORY_DIR = Path(
    os.environ.get("SLA_MEMORY_DIR", str(Path(__file__).resolve().parents[1] / "agent-memory"))
).resolve()
MEMORY_FILE = "AGENTS.md"

_SEED_MEMORY = """\
# Pamięć agenta — PLAYBOOK (strategie, nie fakty)

To jest pamięć PROCEDURALNA. Fakty (np. kwoty, PESEL) trafiają do grafu wiedzy.
Tutaj zapisujesz WSKAZÓWKI, JAK skuteczniej odpowiadać, aby kolejne pytania szły
lepiej: od czego zaczynać dla danego typu pytania, co zadziałało, co nie,
które podejście/wywołania pomagają, na co uważać.

## O systemie
- Odpowiadam na pytania o dokumenty fikcyjnego banku Nordvik Finanse.
- Fakty opieram na dokumentach/grafie i cytuję ID źródeł.

## Wskazówki (uczą się z każdą interakcją)
(pusto — dopisywane automatycznie po każdym pytaniu; przykłady: „Pytania o łańcuch
hipoteczny: śledź KYC→WN→ZD→DC→UM→HS; HS-7794 to repricing HS-7788, nie sprzeczność”)
"""


def _ensure_memory_seed() -> None:
    """Utwórz folder i plik pamięci z treścią początkową, jeśli nie istnieją."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    memory_path = MEMORY_DIR / MEMORY_FILE
    if not memory_path.exists():
        memory_path.write_text(_SEED_MEMORY, encoding="utf-8")


def build_orchestrator(
    subagent_model: str | None = None,
    orchestrator_model: str | None = None,
):
    """Zbuduj graf agenta-orkiestratora RAG z pamięcią długoterminową.

    Model ORKIESTRATORA (planowanie/przepływ) jest niezależny od modelu SUBAGENTÓW,
    dzięki czemu orkiestrator dostaje mocniejszy model (lepiej trzyma się
    obowiązkowych kroków), a subagenci zostają na tańszym.

    Args:
        subagent_model: model subagentów. Domyślnie env ``SUBAGENT_MODEL`` lub
            stała ``DEFAULT_MODEL``.
        orchestrator_model: model samego orkiestratora. Domyślnie env
            ``ORCHESTRATOR_MODEL`` lub stała ``ORCHESTRATOR_MODEL``.
    """
    from langchain.chat_models import init_chat_model

    orch_id = orchestrator_model or os.environ.get("ORCHESTRATOR_MODEL", ORCHESTRATOR_MODEL)
    sub_id = subagent_model or os.environ.get("SUBAGENT_MODEL", DEFAULT_MODEL)
    _ensure_memory_seed()

    orch_chat = init_chat_model(orch_id, max_retries=8)
    sub_chat = init_chat_model(sub_id, max_retries=8)

    subagents_pinned = [{**sa, "model": sub_chat} for sa in subagents]

    backend = CompositeBackend(
        default=StateBackend(),
        routes={"/memories/": FilesystemBackend(root_dir=MEMORY_DIR, virtual_mode=True)},
    )

    return create_deep_agent(
        model=orch_chat,
        system_prompt=load_prompt("orchestrator"),
        subagents=subagents_pinned,
        memory=[f"/memories/{MEMORY_FILE}"],
        backend=backend,
        name="orchestrator",
    )
