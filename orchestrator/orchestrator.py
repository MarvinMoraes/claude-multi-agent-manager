"""Orquestrador principal para coordenar múltiplos agentes."""

from typing import Optional
from loguru import logger
from agents.base_agent import BaseAgent


class Orchestrator:
    """Coordena múltiplos agentes para resolver tarefas complexas."""

    def __init__(self, agents: list[BaseAgent]):
        self.agents = {agent.name: agent for agent in agents}
        logger.info(f"Orquestrador iniciado com {len(agents)} agente(s): {list(self.agents.keys())}")

    def run_sequential(self, task: str) -> str:
        """Executa agentes em sequência, passando a saída de um para o próximo."""
        logger.info(f"Iniciando execução sequencial para tarefa: {task[:80]}...")
        result = task
        for name, agent in self.agents.items():
            logger.info(f"→ Agente ativo: {name}")
            result = agent.run(task=task, context=result if result != task else None)
        return result

    def run_parallel(self, task: str) -> dict[str, str]:
        """Executa todos os agentes em paralelo (sequencialmente, sem concorrência)."""
        logger.info(f"Iniciando execução paralela para tarefa: {task[:80]}...")
        results = {}
        for name, agent in self.agents.items():
            logger.info(f"→ Executando agente: {name}")
            results[name] = agent.run(task=task)
        return results

    def run(self, task: str, mode: str = "sequential") -> str | dict:
        """Executa a tarefa no modo especificado."""
        if mode == "sequential":
            return self.run_sequential(task)
        elif mode == "parallel":
            return self.run_parallel(task)
        else:
            raise ValueError(f"Modo desconhecido: {mode}. Use 'sequential' ou 'parallel'.")

    def add_agent(self, agent: BaseAgent):
        """Adiciona um novo agente ao orquestrador."""
        self.agents[agent.name] = agent
        logger.info(f"Agente '{agent.name}' adicionado ao orquestrador.")

    def remove_agent(self, name: str):
        """Remove um agente pelo nome."""
        if name in self.agents:
            del self.agents[name]
            logger.info(f"Agente '{name}' removido do orquestrador.")
        else:
            logger.warning(f"Agente '{name}' não encontrado.")

    def __repr__(self) -> str:
        return f"Orchestrator(agents={list(self.agents.keys())})"
