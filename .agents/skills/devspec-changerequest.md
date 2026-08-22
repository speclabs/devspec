---
name: devspec-changerequest
description: Run /devspec.changerequest using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.changerequest`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.changerequest.prompt.md` and `.github/agents/devspec.changerequest.agent.md` as the source of intent.
- Preserve required inputs, artifact outputs, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Append accepted `CR-###` scope to existing work-item artifacts; do not create a CR-specific Markdown file or rewrite baseline history.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.
