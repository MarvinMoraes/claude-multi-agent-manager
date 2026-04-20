# 🤖 Claude Multi-Agent Manager

Framework para **gestão e orquestração de múltiplos agentes de IA** usando a [API da Anthropic (Claude)](https://www.anthropic.com).

---

## 📋 Visão Geral

Este repositório fornece uma estrutura para criar, configurar e coordenar múltiplos agentes baseados no modelo Claude. Com ele, você pode:

- **Criar agentes especializados** com papéis e ferramentas específicas
- **Orquestrar fluxos de trabalho** com comunicação entre agentes
- **Gerenciar contexto e memória** de cada agente de forma independente
- **Monitorar e registrar** a execução de cada agente

---

## 🏗️ Estrutura do Projeto

```
claude-multi-agent-manager/
├── agents/              # Definições e configurações dos agentes
│   ├── base_agent.py    # Classe base para todos os agentes
│   └── examples/        # Exemplos de agentes especializados
├── orchestrator/        # Lógica de orquestração e coordenação
│   └── orchestrator.py  # Orquestrador principal
├── tools/               # Ferramentas disponíveis para os agentes
│   └── base_tool.py     # Interface base para ferramentas
├── memory/              # Gerenciamento de memória e contexto
│   └── context_manager.py
├── config/              # Arquivos de configuração
│   └── settings.py
├── examples/            # Exemplos de uso completos
├── tests/               # Testes unitários e de integração
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MarvinMoraes/claude-multi-agent-manager.git
cd claude-multi-agent-manager
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
# Edite o .env com sua chave de API da Anthropic
```

---

## ⚙️ Configuração

Edite o arquivo `.env` com suas credenciais:

```env
ANTHROPIC_API_KEY=sua-chave-aqui
CLAUDE_MODEL=claude-opus-4-5
MAX_TOKENS=8192
LOG_LEVEL=INFO
```

---

## 📖 Uso Básico

```python
from agents.base_agent import BaseAgent
from orchestrator.orchestrator import Orchestrator

# Criar agentes especializados
researcher = BaseAgent(
    name="Pesquisador",
    role="Especialista em pesquisa e coleta de informações",
    tools=["web_search", "document_reader"]
)

writer = BaseAgent(
    name="Redator",
    role="Especialista em redação e síntese de conteúdo",
    tools=["text_formatter"]
)

# Criar orquestrador
orchestrator = Orchestrator(agents=[researcher, writer])

# Executar tarefa
result = orchestrator.run(
    task="Pesquise sobre IA generativa e escreva um resumo"
)

print(result)
```

---

## 🛠️ Arquitetura de Agentes

### Tipos de Agentes

| Tipo | Descrição |
|------|------------|
| **Orquestrador** | Coordena os demais agentes e gerencia o fluxo de tarefas |
| **Especialista** | Agente com papel e ferramentas específicas |
| **Revisor** | Valida e critica as saídas de outros agentes |
| **Executor** | Executa ações concretas (código, APIs, etc.) |

### Padrões de Comunicação

- **Sequencial**: Agentes executam em cadeia, cada um recebe a saída do anterior
- **Paralelo**: Múltiplos agentes executam simultaneamente
- **Hierárquico**: Um agente mestre delega para sub-agentes
- **Debate**: Agentes discutem para chegar a uma conclusão

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia o [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir um pull request.

1. Faça um fork do projeto
2. Crie sua branch: `git checkout -b feature/minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: adiciona minha feature'`
4. Push para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🔗 Recursos

- [Documentação da API Anthropic](https://docs.anthropic.com)
- [Claude Models](https://docs.anthropic.com/en/docs/about-claude/models)
- [Tool Use com Claude](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Multi-agent workflows](https://docs.anthropic.com/en/docs/build-with-claude/agents)
