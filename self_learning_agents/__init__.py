"""Ogólny agent-orkiestrator zbudowany na bibliotece deepagents (LangGraph).

Główny agent (orkiestrator) planuje pracę i deleguje pod-zadania do
wyspecjalizowanych subagentów przez wbudowane narzędzie ``task``.
"""

from self_learning_agents.agent import build_orchestrator

__all__ = ["build_orchestrator"]
