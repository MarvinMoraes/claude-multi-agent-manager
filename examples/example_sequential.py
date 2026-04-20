"""Exemplo de pipeline sequencial: Pesquisador → Redator."""

from agents.base_agent import BaseAgent
from orchestrator.orchestrator import Orchestrator
from config.settings import settings

settings.validate()

# Agente 1: Pesquisador
researcher = BaseAgent(
    name="Pesquisador",
    role="Você coleta e organiza informações sobre um tema de forma detalhada e estruturada.",
)

# Agente 2: Redator
writer = BaseAgent(
    name="Redator",
    role="Você transforma informações brutas em textos claros, envolventes e bem estruturados.",
)

# Orquestrador
orchestrator = Orchestrator(agents=[researcher, writer])

# Executar pipeline
task = "Explique o que são modelos de linguagem de grande escala (LLMs) e como eles funcionam."
result = orchestrator.run(task=task, mode="sequential")

print("=" * 60)
print("RESULTADO FINAL:")
print("=" * 60)
print(result)
