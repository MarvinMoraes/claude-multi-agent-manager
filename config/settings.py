"""Configurações globais carregadas do arquivo .env."""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-opus-4-5")
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "8192"))
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "60"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    def validate(self):
        if not self.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY não configurada. Verifique o arquivo .env")


settings = Settings()
