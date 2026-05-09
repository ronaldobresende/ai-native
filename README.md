# AI-Native Agent 

Plataforma AI-native para engenharia de sistemas multi-agentes.

Este repositório fornece uma plataforma para construir, gerar, evoluir e operar sistemas multi-agentes utilizando coding agents como:

* Codex
* Claude Code
* Devin
* Gemini
* GitHub Copilot

A plataforma foi desenhada com foco em:

* engenharia declarativa via YAML
* arquitetura AI-operable
* scaffolding orientado a topologia
* semantic locality
* geração baseada em templates
* orquestração com LangGraph
* contratos estruturados com Pydantic
* observabilidade com Langfuse
* avaliação de sistemas multi-agentes com RAGAS
* validação e debugging via Streamlit
* integração simplificada com APIs e providers corporativos
* abstração de providers de LLM


---

# Filosofia

Plataformas tradicionais são desenhadas principalmente para humanos.

Esta plataforma foi desenhada para:

* humanos
* coding agents
* workflows autônomos de engenharia

A estrutura do repositório, os templates, os prompts e a arquitetura foram organizados propositalmente para que agentes de IA consigam:

* entender a plataforma
* gerar projetos
* evoluir sistemas
* validar arquiteturas
* criar agentes
* manter limites semânticos
* operar autonomamente

---

# Conceitos Fundamentais

## AI-Native

A plataforma assume que agentes de IA são engenheiros de software de primeira classe.

O repositório foi estruturado para que coding agents consigam:

* ler instruções
* entender topologias
* gerar código
* refinar prompts
* criar grafos de orquestração
* manter contratos
* operar de forma autônoma

---

# Conceitos de Sistemas Multi-Agentes

Sistemas multi-agentes são arquiteturas compostas por múltiplos agentes especializados que colaboram para resolver tarefas complexas.

Em vez de utilizar um único agente extremamente genérico responsável por todas as tarefas, sistemas multi-agentes dividem responsabilidades em agentes menores, especializados e com objetivos mais claros.

Exemplo conceitual:

```text id="1f5w5k"
Agente A → busca informações
Agente B → resume conteúdo
Agente C → valida consistência
Agente D → toma decisão final
```

Essa abordagem melhora:

* separação de responsabilidades
* previsibilidade
* manutenção
* escalabilidade
* observabilidade
* governança
* reutilização
* avaliação de qualidade
* evolução incremental do sistema

Além disso, sistemas multi-agentes permitem combinar diferentes capacidades de modelos e agentes em um mesmo workflow.

Exemplo:

* um agente especializado em retrieval
* outro em sumarização
* outro em validação
* outro em tomada de decisão

---

# Tipos de Agentes

A plataforma utiliza tipos arquiteturais para representar o papel de cada agente dentro do workflow.

O objetivo não é representar domínio de negócio, mas sim responsabilidade arquitetural.

Exemplo:

```yaml id="y7yy33"
- name: credit_summary
  type: worker
```

Neste caso:

* `credit_summary` representa o domínio
* `worker` representa o papel arquitetural

---

## `worker`

Agente especializado em executar uma tarefa específica.

Exemplos:

* resumo
* classificação
* análise
* extração
* pesquisa
* transformação de dados

Normalmente workers recebem contexto, executam uma responsabilidade clara e retornam um resultado estruturado.

---

## `supervisor`

Agente responsável por coordenar outros agentes.

Funções comuns:

* controlar fluxo
* decidir ordem de execução
* consolidar resultados
* controlar estado do workflow
* encerrar processos

Arquiteturas supervisor são atualmente uma das formas mais comuns de sistemas multi-agentes corporativos.

---

## `judge`

Agente responsável por validar outputs de outros agentes.

Funções comuns:

* detectar inconsistências
* revisar respostas
* validar coerência
* reduzir alucinações
* validar contratos estruturados

O padrão "LLM-as-a-Judge" vem sendo amplamente utilizado em sistemas modernos de IA generativa.

---

## `router`

Agente responsável por decidir para qual agente ou workflow uma tarefa deve ser enviada.

Exemplo conceitual:

```text id="5y8j8m"
entrada financeira → financial_agent
entrada jurídica → legal_agent
```

---

## `planner`

Agente responsável por decompor problemas complexos em etapas menores.

Exemplo conceitual:

```text id="i0py0o"
1. buscar informações
2. analisar contexto
3. consolidar riscos
4. gerar recomendação
```

---

## `executor`

Agente responsável por executar ações concretas.

Exemplos:

* chamadas de APIs
* execução de SQL
* integrações externas
* automações
* operações em arquivos

---

# Arquiteturas Multi-Agentes

A plataforma foi desenhada para suportar diferentes topologias multi-agentes.

Exemplos:

* supervisor
* planner/executor
* router-based
* collaborative
* hierarchical
* swarm

Atualmente a topologia mais madura na plataforma é:

```text id="w5t7k0"
supervisor
```

---

# Referências

## Anthropic — Building Effective Agents

https://www.anthropic.com/engineering/building-effective-agents

Discussão moderna sobre:

* agentes especializados
* workflows explícitos
* orquestração
* sistemas multi-agentes determinísticos

---

## LangGraph — Multi-Agent Architectures

https://langchain-ai.github.io/langgraph/concepts/multi_agent/

Conceitos sobre:

* orchestration
* routing
* state management
* arquiteturas multi-agentes

---

## Microsoft AutoGen

https://microsoft.github.io/autogen/

Framework focado em:

* colaboração entre agentes
* workflows autônomos
* conversação multi-agente

---

## Martin Fowler — Context Engineering for Coding Agents

https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html

Discussão sobre:

* context engineering
* coding agents
* workflows assistidos por IA
* arquitetura AI-operable

---

# Engenharia Declarativa via YAML

Os projetos são declarados utilizando:

```text id="vls63z"
agents.yaml
```

Esse arquivo é a fonte de verdade do sistema gerado.

O fluxo esperado é:

```text id="37r5ji"
Prompt
→ agents.yaml
→ scaffold
→ projeto gerado
→ refinamento
```

Em vez de:

```text id="h4v91u"
Prompt
→ geração descontrolada de código
```

---

# Semantic Locality

Arquivos relacionados permanecem próximos.

Exemplo:

```text id="r39yr6"
agents/company/

  agent.py
  prompt.md
  models.py
  judge.py
  tools/
```

Isso melhora drasticamente:

* manutenção
* entendimento pela IA
* modificações autônomas
* recuperação de contexto
* qualidade da geração de código

---

# Arquitetura Orientada a Topologia

A plataforma suporta arquiteturas multi-agentes como:

* supervisor
* planner/executor
* router
* judge
* collaborative
* hierarchical
* swarm

Atualmente o suporte mais forte é para:

```text id="4z2u7n"
supervisor
```

mas a arquitetura foi desenhada para expansão futura.

---

# Estrutura do Repositório

```text id="t4q5pc"
.
├── AGENTS.md
├── .github/
│
├── agent-platform/
│   ├── AGENTS.md
│   ├── BUILD_WITH_AI.md
│   ├── PROJECT_SCHEMA.md
│   ├── PROJECT_SPEC.md
│   ├── platform.yaml
│   ├── Makefile
│   │
│   ├── scripts/
│   │   └── scaffold.py
│   │
│   └── templates/
│       ├── worker_agent/
│       ├── orchestrator/
│       ├── shared/
│       ├── interfaces/
│       └── eval/
│
└── projects/
```

---

# Arquivos Importantes

## `/AGENTS.md`

Arquivo principal de instruções descoberto automaticamente por coding agents como o Codex.

Ele redireciona os agentes para os arquivos da plataforma.

---

# `.github/`

Contém instruções operacionais para agentes de IA.

---

## `.github/CLAUDE.md`

Instruções otimizadas para Claude Code.

---

## `.github/PLAYBOOK.md`

Playbook operacional para coding agents autônomos como Devin.

Define:

* workflow esperado
* regras de geração
* checklist de validação
* regras de segurança
* ciclo de vida de geração dos projetos

---

## `.github/copilot-instructions.md`

Instruções compactas otimizadas para GitHub Copilot.

---

# `agent-platform/`

A plataforma propriamente dita.

Este diretório contém:

* convenções
* regras arquiteturais
* templates
* engine de scaffold
* contratos de geração

Projetos gerados NÃO devem modificar arquivos da plataforma, exceto quando o objetivo for evoluir a própria plataforma.

---

# Arquivos da Plataforma

## `PROJECT_SPEC.md`

Define a filosofia arquitetural.

Explica:

* topologias
* orquestração
* semantic locality
* convenções AI-native
* limites da plataforma

---

## `PROJECT_SCHEMA.md`

Documenta a estrutura esperada do:

```text id="o0n0m0"
agents.yaml
```

---

## `BUILD_WITH_AI.md`

Instruções para coding agents operarem a plataforma.

---

## `platform.yaml`

Define metadados e defaults da plataforma.

---

# Engine de Scaffold

## `scripts/scaffold.py`

Engine principal de geração de projetos.

Responsável por:

* ler o `agents.yaml`
* carregar templates
* renderizar arquivos
* criar estrutura do projeto
* gerar agentes
* gerar orquestração
* gerar estrutura de avaliação

O scaffold evita sobrescrever arquivos existentes sempre que possível.

---

# Templates

## `templates/worker_agent/`

Define a estrutura de agentes worker.

Arquivos gerados:

```text id="lmm3a7"
agent.py
prompt.md
models.py
judge.py
AGENT_SPEC.md
```

---

## `templates/orchestrator/`

Define a topologia supervisor/orquestração.

Arquivos gerados:

```text id="09rlhk"
graph.py
routing.py
state.py
supervisor.py
```

---

## `templates/shared/`

Componentes compartilhados da plataforma/runtime.

Exemplos:

```text id="9ahm49"
llm.py
settings.py
tracing.py
```

---

## `templates/interfaces/`

Interfaces de debug e interação.

Exemplos:

```text id="2uxf0y"
api.py
streamlit.py
```

---

## `templates/eval/`

Estrutura de avaliação.

Exemplos:

```text id="r3n9qm"
ragas.py
metrics.py
golden_set/
```

---

# Projetos Gerados

Os sistemas gerados são criados dentro de:

```text id="jv99ul"
projects/
```

Exemplo:

```text id="dft5x0"
projects/garantia-imovel-test/
```

Cada projeto gerado é isolado da plataforma.

---

# Como os Coding Agents Utilizam a Plataforma

Quando um coding agent recebe um pedido como:

```text id="j9b4nm"
"Crie um sistema multi-agente..."
```

o ciclo esperado é:

1. Ler instruções do repositório
2. Ler AGENTS.md
3. Ler specs da plataforma
4. Criar `agents.yaml`
5. Executar scaffold
6. Gerar projeto
7. Refinar prompts/contratos/tools
8. Validar topologia
9. Executar validações locais

---

# Exemplo de Uso Conversacional

Exemplo de prompt para Codex / Claude / Devin:

```text id="gjmjhu"
Leia:
- AGENTS.md
- .github/PLAYBOOK.md
- agent-platform/AGENTS.md
- agent-platform/PROJECT_SPEC.md
- agent-platform/BUILD_WITH_AI.md
- agent-platform/PROJECT_SCHEMA.md
- agent-platform/platform.yaml

Depois crie um sistema multi-agente.

Requisitos:
- arquitetura supervisor
- um planner
- um researcher
- um writer
- um critic

Use:
- LangGraph
- LangChain
- Langfuse
- RAGAS
- Streamlit

Primeiro gere o agents.yaml.

Depois execute o scaffold.

Depois gere o projeto em:
projects/research-assistant/
```

---

# Exemplo de Uso Declarativo

Crie:

```text id="9tb7mg"
agents.yaml
```

Exemplo:

```yaml id="8zjvf6"
project:
  name: research-assistant

interfaces:
  api: true
  streamlit: true

agents:
  - name: orchestrator
    type: supervisor

  - name: researcher
    type: worker
    has_tools: true

  - name: writer
    type: worker

  - name: critic
    type: judge
    has_judge: true
```

Execute:

```bash id="xv8nbi"
python agent-platform/scripts/scaffold.py \
  --config agents.yaml \
  --output projects
```

---

# Exemplo de Estrutura Gerada

```text id="qv64v0"
projects/research-assistant/

  agents/
    orchestrator/
    researcher/
    writer/
    critic/

  shared/
  interfaces/
  eval/

  README.md
  pyproject.toml
  agents.yaml
```

---

# Tecnologias

A plataforma foi desenhada para trabalhar com:

* LangGraph
* LangChain
* Pydantic
* Langfuse
* RAGAS
* DSPy
* Streamlit
* FastAPI

A abstração de provider é suportada.

Exemplos:

* OpenAI
* Azure OpenAI
* Bedrock
* Anthropic
* SDKs corporativos internos
* IARA

---

# Estado Atual da Plataforma

Atualmente a plataforma fornece:

* scaffold determinístico
* suporte forte para supervisor
* geração de worker agents
* geração de orquestração
* estrutura de avaliação
* semantic locality
* estrutura AI-operable

Evoluções futuras podem incluir:

* templates planner
* templates router
* topologia swarm
* geração automática de grafos
* engine Jinja2
* plugins de topologia
* otimização DSPy
* loops autônomos de avaliação

---

# Princípios de Design

## Explícito acima de mágico

A plataforma favorece estruturas explícitas.

---

## Geração determinística

O scaffold deve permanecer previsível e auditável.

---

## AI-operability

O repositório deve ser compreensível para coding agents.

---

## Baixo nível de nesting

Evitar arquiteturas excessivamente profundas.

---

## Isolamento de domínio

Lógica de negócio pertence apenas aos projetos gerados.

Nunca dentro de:

```text id="r3k8r2"
agent-platform/
```

---

## Referências Arquiteturais

Esta plataforma foi influenciada por discussões modernas sobre:
- sistemas multi-agentes
- coding agents
- context engineering
- workflows determinísticos
- governança de código gerado por IA

### Anthropic — Building Effective Agents
https://www.anthropic.com/engineering/building-effective-agents

Estratégias para construção de agentes especializados e workflows multi-agentes previsíveis.

### Martin Fowler — Structured Prompt-Driven Development (SPDD)
https://martinfowler.com/articles/structured-prompt-driven/

Abordagem estruturada para geração, governança e evolução de software assistido por IA.

### Martin Fowler — Context Engineering for Coding Agents
https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html

Princípios para compartilhamento de contexto e operação eficiente de coding agents.

# Licença

MIT License.

Este projeto é livre para uso, modificação e distribuição.
