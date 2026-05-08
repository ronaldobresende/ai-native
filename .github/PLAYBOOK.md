# Devin Playbook

## Mission

Use this repository as an AI-native agent platform accelerator.

Your goal is to create, modify, or validate multi-agent projects using the platform conventions.

---

# Required Reading

Before starting any task, read:

1. `agent-platform/AGENTS.md`
2. `agent-platform/PROJECT_SPEC.md`
3. `agent-platform/BUILD_WITH_AI.md`
4. `agent-platform/PROJECT_SCHEMA.md`
5. `agent-platform/platform.yaml`

---

# Golden Rule

Do not create project code directly from natural language first.

Always materialize intent into an `agents.yaml` file before generating code.

---

# Workflow: Create a New Project

1. Understand the user's requested system.
2. Identify:

   * project name
   * orchestration pattern
   * agents
   * agent types
   * tools
   * judges
   * interfaces
3. Create or update an `agents.yaml`.
4. Validate the YAML against `PROJECT_SCHEMA.md`.
5. Run the scaffold command.
6. Inspect generated files.
7. Fill initial agent specs and prompts.
8. Add minimal Pydantic models.
9. Do not implement domain logic unless explicitly requested.
10. Report created files and next steps.

---

# Preferred Command

From repository root:

```bash
python agent-platform/scripts/scaffold.py --config agents.yaml --output projects
```

If a Makefile target exists, prefer it.

---

# Project Creation Output

Generated projects should live under:

```text
projects/<project-name>/
```

Do not generate projects inside `agent-platform/`.

---

# Editing Rules

When modifying the platform:

* edit templates in `agent-platform/templates/`
* avoid hardcoding generated content in `scaffold.py`
* keep scaffold deterministic
* keep platform domain-agnostic

When modifying generated projects:

* keep agent files close together
* prompts stay in `prompt.md`
* schemas stay in `models.py`
* local judge logic stays in `judge.py`
* external APIs stay in `tools/`

---

# Validation Checklist

Before completing a task, verify:

* `agents.yaml` exists
* project was generated in `projects/`
* each worker agent has:

  * `agent.py`
  * `prompt.md`
  * `models.py`
  * `AGENT_SPEC.md`
* agents with `has_judge: true` have `judge.py`
* agents with `has_tools: true` have `tools/`
* supervisor has:

  * `graph.py`
  * `state.py`
  * `routing.py`
  * `supervisor.py`
* no domain-specific code was added to `agent-platform/`
* no secrets were committed

---

# Safety Rules

* Do not log sensitive data.
* Do not hardcode credentials.
* Do not add cloud-specific infrastructure unless requested.
* Do not invent business rules.
* Ask for confirmation if project requirements conflict with `agents.yaml`.

---

# Completion Report

At the end, report:

* what was created
* where it was created
* commands executed
* assumptions made
* recommended next steps
