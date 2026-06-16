---
name: devspec-rules
description: Run /devspec.rules using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.rules`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.rules.prompt.md` and `.github/agents/devspec.rules.agent.md` as the source of intent.
- Keep this command focused on operational rules, compliance requirements, enforcement details, delivery gates, exceptions, and evolving governance; do not duplicate durable principles from `devspec/constitution.md` or product intent from `devspec/foundation/project-context.md`.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
