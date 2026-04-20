"""Testes básicos para o BaseAgent (sem chamadas reais à API)."""

import pytest
from unittest.mock import patch, MagicMock
from agents.base_agent import BaseAgent


@pytest.fixture
def mock_agent():
    with patch("agents.base_agent.anthropic.Anthropic"):
        agent = BaseAgent(
            name="TestAgent",
            role="Agente de teste",
        )
    return agent


def test_agent_creation(mock_agent):
    assert mock_agent.name == "TestAgent"
    assert mock_agent.role == "Agente de teste"
    assert mock_agent.conversation_history == []


def test_agent_reset_history(mock_agent):
    mock_agent.conversation_history = [{"role": "user", "content": "hello"}]
    mock_agent.reset_history()
    assert mock_agent.conversation_history == []


def test_agent_repr(mock_agent):
    repr_str = repr(mock_agent)
    assert "TestAgent" in repr_str
    assert "Agente de teste" in repr_str
