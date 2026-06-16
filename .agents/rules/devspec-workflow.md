---
description: Always-on devspec workflow, artifact, and no-intent-drift rules for Google Antigravity.
alwaysApply: true
---

# Devspec Workflow Rules

When the user invokes or references a `/devspec.*` workflow, treat it as command intent from `devspec/adapters/command-registry.md`.

Follow these rules:

- Read `devspec/adapters/command-registry.md` before acting on a `devspec` command.
- Preserve the original intent of the canonical Copilot prompt and agent files named in the registry.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history, Antigravity artifacts, memory, or task lists.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Preserve structured question behavior from `.github/prompts/PATTERNS.md#interactive-question-pattern`; if clickable options are unavailable, render the same option labels as text and preserve the recommended option.
- Use `devspec/glossary.md` for status values.
- Use `devspec/foundation/codebase-structure.md` for repository access requirements.
- Keep product context in `devspec/foundation/project-context.md`, durable principles in `devspec/constitution.md`, and operational governance, compliance rules, enforcement details, and delivery gates in `devspec/foundation/rules.md`.
- Use `devspec/adapters/validation-flows.md` for enterprise acceptance checks.
- For `/devspec.diagram`, keep Mermaid as the default output and treat `format=svg` or `format=mermaid+svg` as canonical command input, not a separate workflow.
- Keep provider credentials, tokens, user settings, and secrets outside prompt, rule, skill, and artifact files.
- Record unsupported Antigravity behavior as a limitation instead of changing workflow semantics.

Do not recommend unregistered commands such as `/devspec.plan`, `/devspec.architecture`, `/devspec.provider-integrations`, `/devspec.queue`, or `/devspec.decisions`.

For Antigravity execution, prefer strict or review-requesting permission posture for commands, non-workspace file access, browser actions, MCP calls, and artifact application unless the project has explicitly approved broader access.
