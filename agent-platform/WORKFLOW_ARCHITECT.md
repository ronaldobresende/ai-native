# Workflow Architect

## Purpose

This document defines the **Workflow Architect** capability for `ai-native`.

Workflow Architect is a design-time capability used by coding agents when translating a user prompt into a multi-agent project specification.

It exists to support three practical architecture modes:

1. The user explicitly describes the architecture.
2. The user partially describes the architecture, such as by naming a pattern, workflow style or architectural constraint.
3. The user describes only the goal, and the coding agent infers the architecture.

In both cases, the result must be recorded in `agents.yaml` before the deterministic scaffold runs.

Workflow Architect does not make the scaffold non-deterministic.

Workflow Architect does not execute runtime workflows.

Workflow Architect does not call an LLM from `scaffold.py`.

---

## 1. Mental model

The core `ai-native` flow remains:

```text
Prompt
→ agents.yaml
→ deterministic scaffold
→ generated project
→ refinement by coding agent
```

Workflow Architect operates between the prompt and `agents.yaml`.

It helps coding agents decide whether to preserve an explicit architecture or infer one from a higher-level goal.

The scaffold remains deterministic and only materializes what is declared in `agents.yaml`.

---

## 2. Architecture modes

Workflow Architect defines three practical architecture modes.

---

### 2.1 Explicit Architecture Mode

Use this mode when the user prompt explicitly provides one or more of:

* agents;
* roles;
* tools;
* workflow steps;
* topology;
* orchestration style;
* architecture pattern.

In this mode, the coding agent acts as a direct translator.

Behavior:

* Preserve the user's explicit design.
* Convert the provided architecture into `agents.yaml`.
* Do not invent a different topology.
* Do not replace the user's agent design with a preferred pattern.
* Add only missing implementation details that are required to make the specification coherent.
* Keep additions minimal and explainable.

Example:

```text
Create a system with a supervisor agent, a document reader agent, a policy checker agent, a synthesizer and a critic.
```

Expected behavior:

```text
Preserve the requested agents and topology.
Generate agents.yaml from the explicit architecture.
Do not replace it with another pattern.
```

---

### 2.2 Partially Explicit Architecture Mode

Use this mode when the user provides a pattern, workflow style, or architectural constraint, but does not list all agents or roles.

In this mode, the coding agent preserves the explicit part and infers only the missing parts.

Behavior:

* Preserve the user-provided pattern or architectural constraint.
* Infer only the missing agents, roles, tools, contracts or topology details.
* Record the completed architecture in `agents.yaml`.
* Do not override the chosen pattern unless it is inconsistent, impossible, or conflicts with explicit platform boundaries.
* If the pattern requires supporting agents, generate them as static, versioned project artifacts.

Example:

```text
Create a system using fan-out-and-synthesize to analyze several information sources and produce a final recommendation.
```

Expected behavior:

```text
Preserve fan-out-and-synthesize as the selected pattern.
Infer the necessary executor agents, synthesizer and critic.
Record the expanded architecture in agents.yaml.
Run the deterministic scaffold after agents.yaml exists.
```

---

### 2.3 Inferred Architecture Mode

Use this mode when the user prompt provides only a high-level goal, business problem, or desired outcome without specifying the multi-agent topology.

In this mode, the coding agent acts as the Workflow Architect.

Behavior:

* Analyze the goal.
* Select an appropriate architecture pattern from the Pattern Catalog.
* Propose the necessary agents, roles, tools and topology.
* Generate an expanded, fully specified `agents.yaml`.
* Make the architecture explicit before scaffold execution.
* Proceed to deterministic scaffold generation only after `agents.yaml` is complete.

Example:

```text
Create a system that analyzes complex documents and produces an auditable recommendation.
```

Expected behavior:

```text
Infer the architecture.
Choose a pattern.
Propose agents and topology.
Generate agents.yaml.
Run scaffold deterministically.
```

---

## 3. Decision rule

Use this rule before generating or modifying `agents.yaml`:

```text
If the prompt explicitly provides agents or architecture, preserve it.

If the prompt provides a pattern but not agents, preserve the pattern and infer the missing agents.

If the prompt provides only a goal, infer the architecture using Workflow Architect.
```

The coding agent must not reinterpret an explicit architecture as an inferred one.

The coding agent must not create a business-specific project unless the user explicitly asks for one.

---

## 4. Source of truth

`agents.yaml` remains the source of truth for generated projects.

Workflow Architect decisions must be materialized in `agents.yaml` before scaffold execution.

The scaffold should not make architectural decisions that were not represented in `agents.yaml`.

The scaffold should not call an LLM.

The scaffold should not infer agent roles from free text.

The scaffold should only read the project specification and generate files deterministically.

---

## 5. Static and dynamic boundaries

Generated agent roles, prompts, contracts and orchestration files become static, versioned artifacts in the repository.

The current model does not create new agent roles dynamically at runtime.

Future runtime fan-out may dynamically create work items or parallel executions, but those executions should run through predefined, versioned agent roles or graph nodes.

This distinction is important:

```text
Design-time inference:
  Decides architecture, agents, topology and contracts before scaffold.

Runtime fan-out:
  May execute predefined nodes multiple times based on runtime work items.
```

Workflow Architect is design-time.

Runtime fan-out is future work unless explicitly implemented in a later platform capability.

---

## 6. Pattern Catalog

When operating in Inferred Architecture Mode, the Workflow Architect selects from the Pattern Catalog.

The catalog is not a list of business domains.

The catalog is a set of reusable architecture patterns and building blocks.

Not every pattern requires scaffold templates immediately.

Some patterns are already aligned with the current `ai-native` vocabulary.

Others are future-oriented patterns inspired by recent dynamic workflow approaches.

---

## 7. Current ai-native patterns and building blocks

These are current `ai-native` architectural patterns or building blocks that coding agents may use when generating `agents.yaml`.

### supervisor-orchestrator

A central supervisor or orchestrator coordinates the workflow, manages state, delegates to worker agents and determines the next step.

Use when:

* the workflow has multiple specialized agents;
* execution order depends on state;
* there is a need for coordination and routing;
* one agent should own the overall process.

### worker-agents

Single-purpose agents focused on a specific task, transformation, analysis or decision support function.

Use when:

* responsibilities can be separated clearly;
* each agent has a stable role;
* the system benefits from semantic locality.

### tool-using-agents

Agents equipped with external tools such as APIs, databases, search, retrieval, calculators or enterprise systems.

Use when:

* the agent must act outside the LLM context;
* the agent needs fresh or structured data;
* the agent must call deterministic functions;
* tool boundaries should be explicit and testable.

### judge-or-critic

An agent responsible for evaluating, criticizing or validating the output of another agent.

Use when:

* output quality matters;
* there are safety, compliance or consistency requirements;
* the system needs review before producing a final answer;
* evaluation criteria can be represented as a rubric.

### rag-oriented-agent

An agent optimized for retrieval-augmented generation.

Use when:

* the system depends on documents or knowledge bases;
* retrieval quality matters;
* source grounding is required;
* context must be assembled before generation.

### evaluator-oriented-agent

An agent or component dedicated to offline or continuous evaluation.

Use when:

* prompts, models or agents must be compared;
* golden datasets are available;
* metrics such as faithfulness, relevance, accuracy or cost need to be measured;
* tools such as RAGAS, LLM-as-a-judge or custom evaluators are part of the project.

---

## 8. Claude-inspired dynamic workflow patterns

These patterns are inspired by recent dynamic workflow ideas such as planning, fan-out, synthesis and verification.

In `ai-native`, they should be treated as reusable architecture patterns that can be materialized into `agents.yaml`, templates and static project files.

They should not be treated as direct copies of any vendor-specific runtime.

---

### classify-and-act

An initial classifier or router determines the type of task and selects the appropriate execution path.

Use when:

* requests fall into distinct categories;
* each category requires a different agent or workflow;
* routing logic should be explicit and testable.

Typical shape:

```text
input
→ classifier/router
→ selected path
→ result
```

---

### fan-out-and-synthesize

A planner decomposes the task into multiple workstreams, executors process them, and a synthesizer merges the results.

Use when:

* the task can be decomposed into independent parts;
* multiple sources or perspectives should be analyzed;
* parallel or semi-parallel execution is useful;
* a final consolidated answer is required.

Typical design-time shape:

```text
goal
→ Workflow Architect
→ selected fan-out pattern
→ generated executor agents
→ synthesizer
→ optional critic
→ agents.yaml
→ scaffold
```

Typical runtime shape, if later implemented:

```text
input
→ planner
→ work items
→ executor runs
→ synthesizer
→ critic
→ final output
```

This is the first intended dynamic workflow pattern to receive scaffold support in a future implementation task.

---

### adversarial-verification

One or more agents produce an answer, and another agent challenges, verifies or attempts to find flaws.

Use when:

* correctness matters;
* hallucination risk must be reduced;
* claims must be checked;
* the system benefits from adversarial review.

Typical shape:

```text
producer
→ verifier / critic
→ revised or approved output
```

---

### generate-and-filter

One agent or workflow generates multiple candidate solutions, and another agent filters, ranks or deduplicates them.

Use when:

* creativity or solution diversity matters;
* several alternatives should be compared;
* a rubric can select the best outputs.

Typical shape:

```text
generator
→ candidates
→ filter/ranker
→ selected outputs
```

---

### tournament

Multiple agents attempt the same task, and a judge selects the strongest result.

Use when:

* independent attempts improve quality;
* there are multiple viable strategies;
* the best answer can be selected by a rubric.

Typical shape:

```text
agent A
agent B
agent C
→ judge
→ winner / merged answer
```

---

### loop-until-done

An agent iterates with a critic or verifier until a stopping condition is met.

Use when:

* the output can be improved iteratively;
* completion criteria are explicit;
* the system needs repeated refinement;
* there is a bounded loop or retry policy.

Typical shape:

```text
executor
→ critic
→ revise
→ critic
→ done
```

---

## 9. Workflow Architect output

When architecture is inferred, the coding agent should produce or update `agents.yaml` with:

* selected architecture mode;
* selected pattern;
* agents;
* agent roles;
* tools;
* prompts;
* graph or topology information;
* judges or critics when needed;
* interfaces;
* evaluation hooks;
* notes for scaffold/refinement.

A future proposed schema may look like:

```yaml
generation:
  architecture_mode: inferred
  workflow_architect:
    enabled: true
    selected_pattern: fan-out-and-synthesize
    pattern_catalog:
      - ai_native_default
      - claude_dynamic_workflows
```

This is a proposed schema shape until scaffold support is explicitly implemented.

---

## 10. Non-goals

Workflow Architect does not:

* execute runtime workflows;
* dynamically create undefined agent roles during runtime;
* replace `agents.yaml`;
* replace deterministic scaffold generation;
* call LLMs from `scaffold.py`;
* create business projects automatically;
* create cloud infrastructure;
* deploy agents;
* add vendor-specific runtime behavior by default.

---

## 11. Summary

Workflow Architect allows `ai-native` to support both explicit and inferred architecture creation.

The important distinction is:

```text
Explicit architecture:
  The user provides agents or topology.
  The coding agent preserves it.

Partially explicit architecture:
  The user provides a pattern or constraint.
  The coding agent preserves it and infers missing details.

Inferred architecture:
  The user provides only a goal.
  The coding agent chooses a pattern, proposes agents and generates agents.yaml.
```

In all cases:

```text
agents.yaml remains the source of truth.
scaffold remains deterministic.
generated projects remain versioned and reviewable.
coding agents refine behavior after scaffold generation.
```
