---
name: devspec-coding-standards
description: Run /devspec.coding-standards using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.coding-standards`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.coding-standards.prompt.md` and `.github/agents/devspec.coding-standards.agent.md` as the source of intent.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
