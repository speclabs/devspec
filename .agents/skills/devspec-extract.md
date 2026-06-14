---
name: devspec-extract
description: Run /devspec.extract using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.extract`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.extract.prompt.md` and `.github/agents/devspec.extract.agent.md` as the source of intent.
- Preserve `format=svg` and `format=mermaid+svg` as diagram generation preferences in queue notes; extraction remains queue-first and may generate at most one approved diagram artifact set only after the canonical approval gate.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
