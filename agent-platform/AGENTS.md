# AI-Native Agent Platform Guidelines

## Purpose

This repository is an AI-native platform accelerator for building multi-agent systems.

It provides:

* repository conventions
* scaffolding scripts
* reusable templates
* orchestration patterns
* evaluation patterns
* observability patterns

The platform is domain-agnostic.

Domain-specific projects must be created as implementations of this platform.

---

# Core Stack

| Capability           | Technology |
| -------------------- | ---------- |
| Orchestration        | LangGraph  |
| Runtime Abstractions | LangChain  |
| Structured Contracts | Pydantic   |
| Observability        | Langfuse   |
| Evaluation           | RAGAS      |
| Prompt Optimization  | DSPy       |

---

# Architecture Principles

## Platform vs Project

The platform must remain generic.

Domain-specific logic must not be added to the platform core.

Examples of domain-specific logic:

* credit analysis rules
* company-specific business logic
* proposal-specific prompts
* regulatory domain prompts

Those belong inside generated projects.

---

# AI-Native Repository Design

This repository is optimized for:

* coding agents
* semantic locality
* low cognitive overhead
* deterministic scaffolding
* explicit contracts
* minimal navigation cost

Prefer:

* feature-based organization
* short files
* clear filenames
* local context close to code

Avoid:

* deep directory nesting
* giant shared utility folders
* excessive abstractions
* framework magic

---

# Generated Project Rules

Generated projects should follow this structure:

```text
agents/
shared/
interfaces/
eval/
scripts/
```

Each generated agent should contain:

```text
agent.py
prompt.md
models.py
judge.py
AGENT_SPEC.md
```

The orchestrator should contain:

```text
graph.py
state.py
routing.py
supervisor.py
AGENT_SPEC.md
```

---

# Pydantic Rules

All structured inputs and outputs must use Pydantic models.

Avoid raw dictionaries for agent input/output contracts.

Validation must happen before LLM execution.

---

# LangGraph Rules

LangGraph is the official orchestration framework.

Generated projects must place graph orchestration inside:

```text
agents/orchestrator/
```

The orchestrator owns:

* graph construction
* routing
* retries
* conditional edges
* supervisor behavior

Business agents must not orchestrate other agents directly.

---

# Prompt Rules

Prompts must be stored as Markdown files.

Avoid inline prompts inside Python code.

Prompt files may contain template variables such as:

```text
{input}
{context}
{cnpj}
```

---

# Tooling Rules

External APIs should be represented as tools.

Agent-specific tools should live inside:

```text
agents/<agent-name>/tools/
```

Shared clients should only be used for truly cross-agent integrations.

---

# Observability Rules

Langfuse is the standard observability platform.

Generated projects should support:

* trace metadata
* latency tracking
* model metadata
* execution path metadata
* optional evaluation metadata

Sensitive data must not be logged.

---

# Evaluation Rules

Evaluation should support:

* Golden Sets
* RAGAS
* LLM-as-a-Judge
* regression testing

Offline evaluation belongs in:

```text
eval/
```

Runtime validation belongs in:

* judge.py
* critic/judge agents

---

# DSPy Rules

DSPy should be used for:

* prompt optimization
* reasoning program optimization
* controlled experimentation

DSPy must not be coupled directly to LangGraph orchestration.

---

# Repository Philosophy

This platform favors:

* conventions over custom architecture
* explicit contracts over implicit behavior
* scaffolding over manual setup
* AI-agent compatibility over enterprise over-segmentation

Favor clarity over abstraction.
