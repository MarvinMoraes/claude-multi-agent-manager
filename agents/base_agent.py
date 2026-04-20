"""Classe base para todos os agentes Claude."""

from typing import Any, Optional
import anthropic
from loguru import logger
from config.settings import settings


class BaseAgent:
    """Agente base que encapsula a comunicação com a API do Claude."""

    def __init__(
        self,
        name: str,
        role: str,
        tools: Optional[list] = None,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None,
    ):
        self.name = name
        self.role = role
        self.tools = tools or []
        self.model = model or settings.CLAUDE_MODEL
        self.max_tokens = max_tokens or settings.MAX_TOKENS
        self.system_prompt = system_prompt or self._default_system_prompt()
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.conversation_history: list[dict] = []
        logger.info(f"Agente '{self.name}' inicializado com papel: {self.role}")

    def _default_system_prompt(self) -> str:
        return f"""Você é {self.name}, um agente especializado em IA.
Seu papel: {self.role}
Responda sempre em português brasileiro, seja preciso e objetivo."""

    def run(self, task: str, context: Optional[str] = None) -> str:
        """Executa uma tarefa e retorna o resultado."""
        user_message = task
        if context:
            user_message = f"Contexto:\n{context}\n\nTarefa:\n{task}"

        self.conversation_history.append({"role": "user", "content": user_message})

        logger.debug(f"[{self.name}] Executando tarefa: {task[:100]}...")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.conversation_history,
        )

        result = response.content[0].text
        self.conversation_history.append({"role": "assistant", "content": result})

        logger.debug(f"[{self.name}] Tarefa concluída.")
        return result

    def reset_history(self):
        """Limpa o histórico de conversa do agente."""
        self.conversation_history = []
        logger.info(f"[{self.name}] Histórico de conversa resetado.")

    def __repr__(self) -> str:
        return f"BaseAgent(name='{self.name}', role='{self.role}', model='{self.model}')"
