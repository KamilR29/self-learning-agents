"""Budowa agenta-orkiestratora RAG (Q&A nad dokumentami Nordvik) na bazie deepagents."""

from __future__ import annotations

import os

from deepagents import create_deep_agent

from orchestrator.prompts_loader import load_prompt
from orchestrator.subagents import subagents

# Model SUBAGENTÓW (retriever, answerer) — przypinany do każdego subagenta, żeby
# NIE dziedziczyli (droższego) modelu orkiestratora.
DEFAULT_MODEL = "openai:gpt-4o-mini"

# Model samego ORKIESTRATORA (planowanie/przepływ). Mocniejszy model tylko tutaj.
ORCHESTRATOR_MODEL = "openai:gpt-5-mini"


def build_orchestrator(
    subagent_model: str | None = None,
    orchestrator_model: str | None = None,
):
    """Zbuduj i skompiluj graf agenta-orkiestratora RAG.

    Orkiestrator odpowiada na pytania o dokumenty banku Nordvik, delegując
    wyszukiwanie/odczyt do subagenta ``retriever`` i syntezę do ``answerer``.
    Model orkiestratora jest niezależny od modelu subagentów.

    Args:
        subagent_model: model subagentów. Domyślnie env ``SUBAGENT_MODEL`` lub
            stała ``DEFAULT_MODEL``.
        orchestrator_model: model samego orkiestratora. Domyślnie env
            ``ORCHESTRATOR_MODEL`` lub stała ``ORCHESTRATOR_MODEL``.

    Returns:
        Skompilowany graf LangGraph gotowy do ``.invoke`` / ``.stream``.
    """
    orch_id = orchestrator_model or os.environ.get("ORCHESTRATOR_MODEL", ORCHESTRATOR_MODEL)
    sub_id = subagent_model or os.environ.get("SUBAGENT_MODEL", DEFAULT_MODEL)

    # Przypnij model subagentom, żeby NIE dziedziczyli modelu orkiestratora.
    subagents_pinned = [{**sa, "model": sub_id} for sa in subagents]

    return create_deep_agent(
        model=orch_id,
        system_prompt=load_prompt("orchestrator"),
        subagents=subagents_pinned,
        name="orchestrator",
    )
