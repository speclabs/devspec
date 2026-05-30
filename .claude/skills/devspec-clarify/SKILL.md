---
name: devspec-clarify
description: Run /devspec.clarify using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.clarify`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.clarify.prompt.md` and `.github/agents/devspec.clarify.agent.md` as the source of intent.
- Follow `AGENTS.md` for canonical workflow, recovery, no-intent-drift, and structured question rules.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
