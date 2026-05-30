---
name: devspec-techstack
description: Run /devspec.techstack using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.techstack`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.techstack.prompt.md` and `.github/agents/devspec.techstack.agent.md` as the source of intent.
- Follow `AGENTS.md` for canonical workflow, recovery, no-intent-drift, and structured question rules.
- Treat unsupported Claude Code behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
