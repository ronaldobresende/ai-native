# AI Native Context

This file is the canonical repository context for coding agents working on `ai-native`.

Read this file before changing code, templates, schemas, examples or documentation.

It defines the identity, boundaries and operating model of the `ai-native` platform.

---

## 1. What is ai-native?

`ai-native` is an AI-native platform for generating multi-agent systems with the help of coding agents.

It is a platform for creating structured AI-agent projects from prompts.

It is not a business application.

It is not a single-agent implementation.

It is not a cloud-specific framework.

It is not an AWS-only, Azure-only, LangGraph-only or vendor-locked product.

It is not a collection of hardcoded business workflows.

The platform exists to transform a natural language prompt into a structured multi-agent project through a deterministic scaffold and later refinement by coding agents.

The intended flow is:

```text
Prompt
→ agents.yaml
→ deterministic scaffold
→ generated project
→ refinement by coding agent
```

This flow is the core philosophy of the repository.

Preserve it in every change.

---

## 2. Core philosophy

The `ai-native` platform separates four concerns:

1. Platform capabilities
2. Project scaffolding
3. Generated project structure
4. Business-specific refinement

The platform provides reusable primitives, templates, schemas, conventions and generation rules.

The scaffold creates the initial structure deterministically.

Generated projects contain concrete agents, prompts, tools, models, workflows, interfaces and evaluation assets.

Coding agents refine generated projects after the scaffold has created the initial project skeleton.

The scaffold is not expected to fully implement the final business behavior.

The scaffold is expected to create a strong project structure that is easy for coding agents to continue.

---

## 3. Deterministic scaffold first

The scaffold must be deterministic.

Given the same `agents.yaml`, it should generate the same structure.

The deterministic scaffold phase should create:

* folders
* files
* contracts
* agent boundaries
* workflow boundaries
* orchestration skeletons
* Pydantic model skeletons
* prompt files
* tool placeholders
* evaluation placeholders
* interface placeholders
* documentation placeholders

The deterministic scaffold phase should not try to solve the full business problem.

The refinement phase belongs to coding agents.

---

## 4. Minimal templates are intentional

Minimal templates are acceptable.

Placeholders are acceptable.

`NotImplementedError` is acceptable.

Explicit TODOs are acceptable.

A generated file does not need to be production-ready immediately after scaffold generation.

A placeholder is good when it:

* marks a clear contract;
* identifies the refinement point;
* avoids fake business logic;
* preserves semantic locality;
* makes the next coding-agent step obvious.

A placeholder is bad when it:

* hides missing behavior;
* pretends to implement production logic;
* returns fake business values;
* introduces domain assumptions not requested by the user;
* makes the generated project look more complete than it is.

Do not remove placeholders simply because they are placeholders.

Only replace them when the user explicitly asks for refinement or implementation.

---

## 5. Platform vs generated project

When the user asks to evolve `ai-native`, the default assumption is:

```text
Evolve the platform.
Do not create a business project.
```

Only create a new generated project when the user explicitly asks for one.

Only add business-specific logic when the user explicitly asks for it.

If the request is about capabilities such as:

* new agent types;
* new workflow topologies;
* new scaffold behavior;
* new templates;
* new schema sections;
* new deployment targets;
* new observability hooks;
* new evaluation patterns;
* new coding-agent instructions;

then implement them as generic platform capabilities.

Do not invent a business domain.

---

## 6. What belongs in agent-platform?

The `agent-platform/` directory is the reusable platform core.

It may contain:

* scaffold scripts;
* reusable templates;
* platform-level schemas;
* project-generation conventions;
* generic agent patterns;
* generic workflow topologies;
* generic deployment adapters;
* validation helpers;
* documentation for coding agents.

It must not contain:

* bank-specific rules;
* credit-renegotiation rules;
* legal decision rules;
* real-estate decision rules;
* customer-specific integrations;
* hardcoded domain prompts;
* real credentials;
* real cloud infrastructure;
* real deployment configuration;
* real ARNs;
* real account IDs;
* production endpoints;
* customer data;
* PII examples.

The platform core should remain reusable.

---

## 7. What belongs in generated projects?

Generated projects are created from `agents.yaml`.

A generated project may contain:

* concrete agents;
* concrete prompts;
* concrete tools;
* concrete Pydantic models;
* concrete graph definitions;
* concrete interfaces;
* concrete evaluators;
* domain-specific behavior, only when explicitly requested.

Generated projects are expected to be refined by coding agents after scaffold generation.

Generated projects may start with incomplete implementations if the contracts, boundaries and refinement points are clear.

---

## 8. What is agents.yaml?

`agents.yaml` is the source of truth for a generated project.

It should describe the intended project structure before implementation begins.

It may include:

* project metadata;
* runtime choices;
* interfaces;
* agents;
* agent types;
* agent capabilities;
* tools;
* models;
* prompts;
* orchestration topology;
* workflow pattern;
* observability settings;
* evaluation settings;
* optional deployment targets.

Coding agents should not start implementing Python behavior before the intended topology is represented in `agents.yaml`.

When evolving the platform, prefer extending `agents.yaml` support declaratively instead of hardcoding one-off behavior in Python templates.

---

## 9. Existing example

The repository contains an example generated project:

```text
example/garantia-imovel-test/
```

The prompt used to generate that example is:

```text
example/garantia-imovel-test/prompt.txt
```

This example demonstrates how the platform can generate a project from a prompt.

The example is not the platform core.

Do not modify the example unless explicitly requested.

Do not infer that future platform work should become a legal, guarantee, real-estate, banking or credit project.

Examples are references.

They are not the architectural center of the repository.

---

## 10. Coding-agent operating model

When working on this repository, coding agents should follow this sequence:

1. Read `AI_NATIVE_CONTEXT.md`.
2. Read `AGENTS.md`.
3. Read `.github/PLAYBOOK.md`.
4. Read `.github/CLAUDE.md` when using Claude-based agents.
5. Read `.github/copilot-instructions.md` when using Copilot.
6. Read `agent-platform/AGENTS.md`.
7. Read `agent-platform/PROJECT_SPEC.md`.
8. Read `agent-platform/PROJECT_SCHEMA.md`.
9. Read `agent-platform/BUILD_WITH_AI.md`.
10. Read `agent-platform/WORKFLOW_ARCHITECT.md`.
11. Read `agent-platform/platform.yaml`.
12. Inspect `agent-platform/scripts/scaffold.py`.
13. Inspect the relevant templates.

Then classify the user request as one of:

* platform evolution;
* documentation update;
* generated-project creation;
* generated-project refinement;
* schema evolution;
* scaffold evolution;
* template evolution;
* deployment-adapter evolution;
* workflow-pattern evolution;
* business-specific implementation.

If the user did not explicitly ask for a business project, do not create one.

---

## 11. How to evolve the platform

Platform evolution should be:

* generic;
* reusable;
* declarative when possible;
* compatible with `agents.yaml`;
* scaffold-driven;
* deterministic;
* friendly to coding agents;
* low in accidental complexity;
* explicit in generated structure;
* easy to inspect.

Prefer:

* extending schema documentation;
* adding reusable templates;
* updating scaffold generation rules;
* adding optional capabilities;
* adding generic adapters;
* adding generic workflow patterns;
* adding validation helpers;
* improving coding-agent instructions.

Avoid:

* hardcoding one-off project behavior;
* mixing business rules into platform code;
* creating cloud resources;
* making deployment mandatory;
* coupling the core to one vendor;
* hiding behavior inside overly complex generation logic;
* making the generated project look complete when it still requires refinement.

---

## 12. Scaffold design principles

The scaffold should remain simple and predictable.

Good scaffold behavior:

* reads `agents.yaml`;
* creates deterministic files and folders;
* respects existing files when appropriate;
* generates clear placeholders;
* keeps related files close together;
* preserves semantic locality;
* avoids unnecessary abstraction;
* avoids hidden behavior;
* produces projects that coding agents can easily continue.

Bad scaffold behavior:

* creates business logic not declared in `agents.yaml`;
* creates infrastructure without explicit request;
* silently overwrites user work;
* injects real credentials or real cloud identifiers;
* generates opaque code that coding agents cannot easily refine;
* introduces complex framework behavior before the project requires it.

---

## 13. Template design principles

Templates should express structure and contracts.

Templates do not need to complete final behavior.

A good template:

* has a clear responsibility;
* is easy to read;
* has explicit placeholders;
* uses consistent naming;
* avoids domain assumptions;
* provides a refinement path for coding agents;
* keeps generated code inspectable.

A bad template:

* mixes unrelated concerns;
* includes fake production behavior;
* hides incomplete logic;
* assumes a business domain;
* hardcodes cloud provider behavior;
* creates coupling that the schema did not request.

---

## 14. Semantic locality

Generated projects should be easy for coding agents to navigate.

Related files should stay close together.

Agent-specific files should live near the agent.

Workflow-specific files should live near the workflow or orchestrator.

Evaluation files should be discoverable.

Prompt files should be easy to find and edit.

Avoid deeply nested structures unless they materially improve clarity.

A coding agent should be able to understand where to refine behavior without searching the entire repository.

---

## 15. Deployment targets

Deployment targets are optional adapters.

A deployment target must not redefine the platform core.

For example, an AWS AgentCore integration should be modeled as an optional deployment adapter.

It should not transform `ai-native` into an AWS-only framework.

It should not create real infrastructure unless explicitly requested.

It should not require credentials.

It should not be enabled by default.

It should be generated only when declared in `agents.yaml`.

A deployment adapter may include:

* placeholder entrypoints;
* example configuration files;
* optional requirements files;
* README instructions;
* TODOs for later refinement.

A deployment adapter must not include:

* real credentials;
* real account IDs;
* real ARNs;
* production endpoints;
* automatic deploy workflows;
* Terraform, CDK or CloudFormation unless explicitly requested.

---

## 16. Workflow patterns

Workflow patterns should be generic platform capabilities.

They should not be implemented as business processes.

For example, a dynamic workflow pattern such as:

```text
planner
→ fanout executors
→ synthesizer
→ critic
```

is a reusable topology.

It is not a credit workflow.

It is not a legal workflow.

It is not a banking workflow.

It is not a real-estate workflow.

It should be scaffolded as a generic orchestration pattern that future generated projects can refine.

Workflow templates may contain placeholders and `NotImplementedError` when behavior depends on project-specific refinement.

The important part is the contract:

1. planner decomposes the original task;
2. executors process planned work items;
3. synthesizer consolidates executor results;
4. critic reviews the synthesized result;
5. final output exposes the plan, executor results, synthesis, critique and status.

---

## 17. Agent types

Agent types should be treated as platform-level concepts.

Examples of generic agent roles include:

* supervisor;
* planner;
* executor;
* worker;
* synthesizer;
* critic;
* judge;
* tool-using agent;
* evaluator.

Do not create domain-specific agent roles in the platform core unless they are examples or explicitly requested.

Domain-specific agents belong in generated projects.

---

## 18. Observability and evaluation

Observability and evaluation are platform capabilities.

They should be scaffolded as generic hooks, placeholders or optional integrations.

Examples:

* Langfuse tracing placeholders;
* RAGAS evaluation placeholders;
* LLM-as-a-judge templates;
* local evaluation runners;
* prompt/version metadata.

Do not make a specific observability or evaluation provider mandatory unless the platform schema explicitly declares it as required.

Prefer optional, replaceable, well-documented integration points.

---

## 19. Cloud and vendor boundaries

The platform may support cloud-specific adapters.

The platform must not become cloud-specific by accident.

If adding support for AWS, Azure, GCP or any other provider:

* keep it optional;
* keep it adapter-based;
* keep it disabled by default;
* avoid real infrastructure;
* avoid credentials;
* avoid production identifiers;
* document the boundary clearly.

The core should remain portable.

---

## 20. Documentation expectations

Documentation should help both humans and coding agents.

Good documentation:

* states the purpose of the repository;
* distinguishes platform from generated projects;
* explains scaffold behavior;
* explains placeholder policy;
* explains where to make changes;
* explains what not to do;
* provides small examples;
* avoids overfitting to one business domain.

When adding a platform capability, update relevant documentation:

* `AI_NATIVE_CONTEXT.md` if the operating model changes;
* `PROJECT_SPEC.md` if the platform scope changes;
* `PROJECT_SCHEMA.md` if `agents.yaml` changes;
* `BUILD_WITH_AI.md` if coding-agent workflow changes;
* `platform.yaml` if capabilities change;
* `AGENTS.md` or `.github/*` instructions if coding-agent behavior changes.

---

## 21. Safety and repository boundaries

Never add:

* secrets;
* credentials;
* account IDs;
* real ARNs;
* production endpoints;
* customer data;
* personal data;
* PII examples;
* internal company data;
* domain rules not requested by the user;
* real deployment automation without explicit request.

Never create a business project unless the user explicitly asks for one.

Never treat an example as the platform core.

Never remove intentional placeholders only because they are incomplete.

Never convert a generic platform capability into a domain-specific implementation.

---

## 22. Decision checklist for coding agents

Before changing files, answer these questions:

1. Is the user asking to evolve the platform or create/refine a generated project?
2. Is a business domain explicitly requested?
3. Should this change be represented in `agents.yaml`?
4. Does this belong in `agent-platform/` or in a generated project?
5. Is this a reusable capability or one-off behavior?
6. Will the scaffold remain deterministic?
7. Are placeholders acceptable for this stage?
8. Does this change preserve semantic locality?
9. Does this introduce hidden cloud/vendor coupling?
10. Does this require documentation updates?

If the answer is unclear, prefer the smaller generic platform change.

---

## 23. Correct mental model

The correct mental model for `ai-native` is:

```text
The user describes the desired multi-agent system in natural language.

A coding agent converts that intent into agents.yaml.

The deterministic scaffold creates the project structure.

The generated project contains explicit contracts, placeholders and boundaries.

A coding agent refines the generated project into working behavior.
```

The platform exists to make this process repeatable, structured and safe.

---

## 24. Workflow Architect

The Workflow Architect is a design-time capability used by coding agents when translating user intent into `agents.yaml`.

It supports three architecture modes:

* **Explicit architecture:** the user provides agents, roles, tools, workflow or topology. The coding agent must preserve the explicit architecture.
* **Partially explicit architecture:** the user provides a pattern or architectural constraint, but not all agents. The coding agent must preserve the explicit pattern and infer only the missing agents, roles or topology details.
* **Inferred architecture:** the user provides only a high-level goal. The coding agent selects a pattern, proposes agents/topology, and generates an expanded `agents.yaml`.

In all modes:

* `agents.yaml` remains the source of truth.
* The scaffold remains deterministic and does not call an LLM.
* Architecture inference happens before scaffold execution.
* Generated agents, prompts, contracts and topology become versioned artifacts.

For detailed rules, read `agent-platform/WORKFLOW_ARCHITECT.md`.

---

## 25. Summary

`ai-native` is a platform for generating AI-native multi-agent systems.

Its core flow is:

```text
Prompt
→ agents.yaml
→ deterministic scaffold
→ generated project
→ coding agent refinement
```

Preserve this model.

When in doubt:

* evolve the platform generically;
* keep the scaffold deterministic;
* keep templates explicit;
* keep placeholders honest;
* avoid business logic unless requested;
* avoid real infrastructure unless requested;
* make the next coding-agent step obvious.
