---
name: devspec-implement
description: Run /devspec.implement using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.implement`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.implement.prompt.md` and `.github/agents/devspec.implement-task.agent.md` as the source of intent.
- Follow `AGENTS.md` for canonical workflow, recovery, no-intent-drift, and structured question rules.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
