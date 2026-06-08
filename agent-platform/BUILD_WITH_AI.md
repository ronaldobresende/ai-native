# Build With AI

## Purpose

This file defines how coding agents should create new multi-agent projects from natural language instructions.

This repository supports two creation modes:

1. Declarative mode:

   * a developer edits `agents.yaml`
   * then runs the scaffold command

2. Conversational mode:

   * a developer describes the desired system in natural language
   * the coding agent creates `agents.yaml`
   * then generates the project structure

---

# Required Context

Before creating a project, the coding agent must read:

* `AGENTS.md`
* `PROJECT_SPEC.md`
* `platform.yaml`
* `BUILD_WITH_AI.md`
* `WORKFLOW_ARCHITECT.md`

If available, also read:

* `templates/project_agents.yaml`
* `PROJECT_SCHEMA.md`

---

# Creation Protocol

When a user asks to create a new multi-agent project, follow this sequence:

1. Understand the requested system
2. Identify the project name
3. Identify the orchestration pattern
4. Identify all agents
5. Classify each agent type
6. Detect whether each agent needs:

   * tools
   * judge
   * prompt
   * external APIs
7. Generate or update `agents.yaml`
8. Generate the project structure
9. Generate initial agent specs
10. Generate initial prompts
11. Generate initial Pydantic models
12. Generate graph skeleton if orchestrator exists

---

# Agent Types

Supported agent types:

* `supervisor`
* `worker`
* `judge`
* `router`
* `planner`
* `executor`

---

# Default Project Structure

Generated projects should use:

```text
agents/
shared/
interfaces/
eval/
scripts/
```

---

# Default Worker Agent Structure

Each worker agent should contain:

```text
agent.py
prompt.md
models.py
judge.py
AGENT_SPEC.md
```

If the agent calls external APIs, also create:

```text
tools/
```

---

# Default Orchestrator Structure

Supervisor or orchestrator agents should contain:

```text
graph.py
state.py
routing.py
supervisor.py
AGENT_SPEC.md
nodes/
```

---

# Project YAML Rules

The coding agent must materialize the user's intent into `agents.yaml`.

The YAML must include:

* project name
* project description
* runtime stack
* interfaces
* agents
* agent names
* agent types
* optional capabilities

Example:

```yaml
version: 1

project:
  name: example-project
  description: >
    Example multi-agent project.

platform:
  starter: agent-platform

runtime:
  orchestration: langgraph
  llm_framework: langchain
  observability: langfuse
  evaluation: ragas
  optimization: dspy

interfaces:
  api: true
  streamlit: true

agents:
  - name: orchestrator
    type: supervisor

  - name: agent_a
    type: worker
    has_judge: true

  - name: critic
    type: judge
```

---

# Conversational Mode

If the user provides a natural language request, first convert it to `agents.yaml`.

Apply these decision rules when translating the request into a topology:

* If the user provides specific agents or topology, preserve it.
* If the user provides only a goal, use the Workflow Architect capability (see `WORKFLOW_ARCHITECT.md`) to infer the architecture.
* If the user provides a pattern but not agents, preserve the pattern and infer the missing agents.

Example user request:

```text
Create a supervisor-based multi-agent system with three agents:
Agent A summarizes documents.
Agent B retrieves company data.
Agent C validates the final answer.
```

Expected first action:

```text
Create or update agents.yaml.
```

Do not start writing Python code before the project topology is represented in YAML.

---

# Declarative Mode

If `agents.yaml` already exists, use it as the source of truth.

Do not infer agent structure from conversation if it conflicts with `agents.yaml`.

If there is conflict, ask for confirmation before modifying `agents.yaml`.

---

# Scaffold Execution

After `agents.yaml` is created or updated, generate the project structure.

Preferred command:

```bash
python scripts/scaffold.py --config agents.yaml --output .
```

If a `Makefile` exists, prefer:

```bash
make scaffold
```

---

# Coding Rules

Generated code must follow:

* async-first design
* Pydantic for structured inputs and outputs
* Markdown prompts
* LangGraph for orchestration
* Langfuse-ready tracing
* RAGAS-ready evaluation
* DSPy-ready optimization

---

# Safety Rules

Do not log sensitive data.

Do not invent business logic that was not requested.

Do not hardcode secrets.

Do not create cloud-specific infrastructure unless explicitly requested.

---

# Completion Criteria

A project creation task is complete only when:

* `agents.yaml` exists
* project folders exist
* each agent has required files
* orchestrator exists when required
* initial specs exist
* prompts exist
* Pydantic models exist
* README has basic usage instructions
