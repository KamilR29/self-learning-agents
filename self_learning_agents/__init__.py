"""System Q&A z pamięcią długoterminową i grafem wiedzy (deepagents + Neo4j).

Orkiestrator prowadzi przepływ i deleguje zadania do subagentów, korzystając z
pamięci grafowej (GraphRAG) i ucząc się między kolejnymi uruchomieniami.
"""

from self_learning_agents.agent import build_orchestrator

__all__ = ["build_orchestrator"]
