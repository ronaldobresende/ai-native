# Claude Instructions

This repository contains an AI-native agent platform.

Before making changes, read:

- `agent-platform/AGENTS.md`
- `agent-platform/PROJECT_SPEC.md`
- `agent-platform/BUILD_WITH_AI.md`
- `agent-platform/PROJECT_SCHEMA.md`
- `agent-platform/platform.yaml`

## Operating Rules

- Treat `agent-platform/` as the platform core.
- Do not add domain-specific business logic to the platform.
- Use `agents.yaml` as the source of truth for generated projects.
- Prefer editing templates over hardcoding generated code in scripts.
- Keep generated projects AI-native, feature-based, and low-nesting.
- Use Pydantic for all structured inputs and outputs.
- Use LangGraph for orchestration.
- Use Langfuse-ready tracing.
- Keep prompts in Markdown files.