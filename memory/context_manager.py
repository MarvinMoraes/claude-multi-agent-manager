"""Gerenciador de contexto e memória para os agentes."""

from typing import Any, Optional
from loguru import logger


class ContextManager:
    """Gerencia o contexto compartilhado entre agentes."""

    def __init__(self):
        self._context: dict[str, Any] = {}
        self._history: list[dict] = []

    def set(self, key: str, value: Any):
        """Define um valor no contexto compartilhado."""
        self._context[key] = value
        logger.debug(f"Contexto atualizado: {key}")

    def get(self, key: str, default: Any = None) -> Any:
        """Recupera um valor do contexto."""
        return self._context.get(key, default)

    def add_to_history(self, agent_name: str, task: str, result: str):
        """Registra a execução de um agente no histórico."""
        entry = {"agent": agent_name, "task": task, "result": result}
        self._history.append(entry)

    def get_history(self) -> list[dict]:
        """Retorna o histórico completo de execuções."""
        return self._history.copy()

    def clear(self):
        """Limpa o contexto e o histórico."""
        self._context.clear()
        self._history.clear()
        logger.info("Contexto e histórico limpos.")

    def summary(self) -> str:
        """Retorna um resumo do histórico como texto."""
        if not self._history:
            return "Nenhuma execução registrada."
        lines = []
        for i, entry in enumerate(self._history, 1):
            lines.append(f"{i}. [{entry['agent']}] {entry['task'][:60]}...")
        return "\n".join(lines)
