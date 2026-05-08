# Orchestrator Specification

## Purpose

Coordinates graph orchestration, routing, retries, and multi-agent supervision.

---

# Agent Type

supervisor

---

# Responsibilities

The orchestrator is responsible for:

* graph construction
* graph execution
* routing decisions
* retry decisions
* workflow supervision
* conditional transitions
* execution coordination

The orchestrator must not contain:

* business-specific reasoning
* domain-specific prompts
* unrelated API integrations

---

# Graph

Graph construction should live in:

* graph.py

The graph should:

* remain explicit
* remain readable
* avoid hidden abstractions
* avoid excessive indirection

---

# State

Global graph state should remain:

* minimal
* explicit
* typed
* deterministic

State definitions belong in:

* state.py

---

# Routing

Routing logic belongs in:

* routing.py

Routing should support:

* conditional execution
* retries
* critic loops
* workflow branching

---

# Supervisor

Supervisor reasoning belongs in:

* supervisor.py

The supervisor may:

* retry agents
* stop execution
* trigger critics
* trigger recovery paths
* validate workflow coherence

---

# Nodes

Reusable graph nodes may live inside:

* nodes/

Nodes should remain:

* isolated
* reusable
* deterministic

---

# Rules

* Keep orchestration explicit.
* Keep graph topology readable.
* Avoid hidden runtime magic.
* Avoid embedding business logic in orchestration.
* Avoid giant shared mutable state.

---

# Observability

The orchestrator should support:

* execution tracing
* node-level metadata
* routing metadata
* retry metadata
* execution timing

Sensitive data must not be logged.

---

# Philosophy

The orchestrator should remain:

* explicit
* deterministic
* topology-aware
* semantically clear
* easy for coding agents to modify
