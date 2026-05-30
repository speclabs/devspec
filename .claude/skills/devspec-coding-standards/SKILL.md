---
name: devspec-coding-standards
description: Run /devspec.coding-standards using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.coding-standards`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.coding-standards.prompt.md` and `.github/agents/devspec.coding-standards.agent.md` as the source of intent.
- Follow `AGENTS.md` for canonical workflow, recovery, no-intent-drift, and structured question rules.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
