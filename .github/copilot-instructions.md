# Copilot Instructions

This repository is an AI-native agent platform.

Primary source files:

- `agent-platform/AGENTS.md`
- `agent-platform/PROJECT_SPEC.md`
- `agent-platform/BUILD_WITH_AI.md`
- `agent-platform/PROJECT_SCHEMA.md`

Rules:

- Keep platform code generic.
- Do not add business-specific logic to `agent-platform/`.
- Generated projects must be driven by `agents.yaml`.
- Use Pydantic for structured contracts.
- Use LangGraph for orchestration.
- Use Markdown prompt files.
- Keep related files close together.
- Prefer templates over hardcoded scaffold content.