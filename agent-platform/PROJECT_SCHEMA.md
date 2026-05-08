# Project YAML Schema

## Purpose

This document defines the official structure of `agents.yaml`.

All generated projects must follow this schema.

Coding agents should validate project definitions against this specification before scaffolding projects.

---

# Root Structure

```yaml
version:
project:
platform:
runtime:
interfaces:
agents:
```

---

# version

Required.

Example:

```yaml
version: 1
```

---

# project

Required.

Defines the generated project metadata.

Example:

```yaml
project:
  name: credit-analysis
  description: >
    Multi-agent credit analysis system.
```

Rules:

* `name` is required
* `description` is optional but recommended

---

# platform

Required.

Defines which platform generated the project.

Example:

```yaml
platform:
  starter: agent-platform
```

Rules:

* `starter` is required

---

# runtime

Required.

Defines the runtime stack.

Example:

```yaml
runtime:
  orchestration: langgraph
  llm_framework: langchain
  observability: langfuse
  evaluation: ragas
  optimization: dspy
```

Rules:

* all fields optional
* defaults may be inferred by the platform

---

# interfaces

Optional.

Defines external interfaces.

Example:

```yaml
interfaces:
  api: true
  streamlit: true
```

Defaults:

```yaml
api: true
streamlit: true
```

---

# agents

Required.

Defines all agents in the system.

Example:

```yaml
agents:

  - name: orchestrator
    type: supervisor

  - name: summarizer
    type: worker
    has_judge: true

  - name: critic
    type: judge
```

---

# Agent Fields

## name

Required.

Example:

```yaml
name: summarizer
```

Rules:

* lowercase recommended
* snake_case recommended
* must be unique

---

## type

Required.

Supported values:

* supervisor
* worker
* judge
* planner
* executor
* router

Example:

```yaml
type: worker
```

---

## description

Optional.

Example:

```yaml
description: >
  Summarizes proposal histories.
```

---

## has_tools

Optional.

Boolean.

If true, generate:

```text
tools/
```

inside the agent directory.

Example:

```yaml
has_tools: true
```

---

## has_judge

Optional.

Boolean.

If true, generate:

```text
judge.py
```

for the agent.

Example:

```yaml
has_judge: true
```

---

# Orchestrator Rules

Supervisor agents should generate:

```text
graph.py
state.py
routing.py
supervisor.py
nodes/
```

Worker agents should generate:

```text
agent.py
prompt.md
models.py
AGENT_SPEC.md
```

---

# Prompt Rules

Prompts must be Markdown files.

Example:

```text
prompt.md
```

Prompt variables should use:

```text
{variable}
```

syntax.

---

# Structured Output Rules

All agent outputs should use Pydantic models.

Avoid raw string outputs.

---

# Evaluation Rules

Projects should support:

* RAGAS
* Golden Sets
* LLM-as-a-Judge

Evaluation belongs in:

```text
eval/
```

---

# Observability Rules

Projects should support:

* Langfuse tracing
* metadata tracking
* latency tracking
* execution path tracking

Sensitive data must not be logged.

---

# Philosophy

This schema exists to:

* reduce ambiguity
* standardize generated systems
* improve coding-agent consistency
* enable deterministic scaffolding
* improve maintainability
