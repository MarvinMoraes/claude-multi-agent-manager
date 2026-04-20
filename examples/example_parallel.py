"""Exemplo de execução paralela: múltiplos agentes com perspectivas diferentes."""

from agents.base_agent import BaseAgent
from orchestrator.orchestrator import Orchestrator
from config.settings import settings

settings.validate()

# Criar agentes com perspectivas distintas
optimist = BaseAgent(
    name="Otimista",
    role="Você analisa temas destacando oportunidades, benefícios e aspectos positivos.",
)

critic = BaseAgent(
    name="Crítico",
    role="Você analisa temas identificando riscos, desafios e pontos de atenção.",
)

neutral = BaseAgent(
    name="Analista",
    role="Você analisa temas de forma equilibrada, apresentando fatos e dados objetivos.",
)

# Orquestrador
orchestrator = Orchestrator(agents=[optimist, critic, neutral])

# Executar em paralelo
task = "Analise o impacto da IA generativa no mercado de trabalho nos próximos 5 anos."
results = orchestrator.run(task=task, mode="parallel")

print("=" * 60)
print("ANÁLISES PARALELAS:")
print("=" * 60)
for agent_name, result in results.items():
    print(f"\n[{agent_name.upper()}]")
    print(result)
    print("-" * 40)
