"""Bazowy system RAG: agentowe wyszukiwanie w dokumentach (deepagents).

Orkiestrator deleguje wyszukiwanie i odczyt dokumentów do subagenta ``retriever``,
a syntezę końcowej odpowiedzi do ``answerer``.
"""

from simple_agents.agent import build_orchestrator

__all__ = ["build_orchestrator"]
