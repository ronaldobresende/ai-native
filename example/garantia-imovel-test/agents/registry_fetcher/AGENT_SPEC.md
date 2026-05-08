# registry_fetcher Agent Specification

## Purpose

Consulta uma API ficticia de matriculas de imoveis por identificador do imovel ou numero da matricula e retorna dados estruturados.

## Project-Specific Contract

Uses `MockRegistryClient` in `tools/registry_client.py`.

Inputs are `RegistryFetchInput`. Outputs are `RegistryFetchOutput`.

No real API call is allowed in this test project.

---

# Agent Type

worker

---

# Responsibilities

This agent is responsible only for its own domain task.

The agent must:

* execute a single responsibility
* use structured outputs
* follow its prompt strictly
* avoid unrelated reasoning
* avoid orchestration responsibilities

---

# Input Contract

Input models must be defined in:

* models.py

Inputs should use Pydantic models.

Avoid raw dictionaries whenever possible.

---

# Output Contract

Outputs must be defined in:

* models.py

Outputs should:

* be structured
* deterministic when possible
* validated before returning

---

# Prompt

Main prompt file:

* prompt.md

Prompts must:

* remain domain-local
* avoid infrastructure concerns
* avoid orchestration logic
* use explicit instructions

---

# Judge

If enabled, local validation is implemented in:

* judge.py

The judge may validate:

* consistency
* completeness
* hallucinations
* formatting
* reasoning quality

---

# Tools

If the agent uses external integrations, tools should live inside:

* tools/

Tools should contain:

* API calls
* external integrations
* lightweight transformations

Tools must not contain:

* orchestration logic
* business orchestration
* graph routing

---

# Rules

* Use Pydantic for structured data.
* Do not invent information.
* Use only provided context.
* Keep business logic local to this agent.
* Avoid cross-agent orchestration.
* Keep prompts isolated from infrastructure concerns.

---

# Observability

Agent execution should support:

* tracing
* latency measurement
* metadata collection
* optional evaluation metadata

Sensitive data must not be logged.

---

# Evaluation

The agent may support:

* local judge evaluation
* RAGAS evaluation
* regression evaluation
* Golden Set validation

Offline evaluation belongs in:

* eval/

---

# Philosophy

This agent should remain:

* focused
* isolated
* deterministic
* semantically cohesive
* easy for coding agents to understand
