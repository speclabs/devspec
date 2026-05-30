---
name: devspec-rules
description: Run /devspec.rules using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.rules`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.rules.prompt.md` and `.github/agents/devspec.rules.agent.md` as the source of intent.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
