---
name: devspec-clarify
description: Run /devspec.clarify using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.clarify`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.clarify.prompt.md` and `.github/agents/devspec.clarify.agent.md` as the source of intent.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
