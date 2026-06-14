---
name: devspec-diagram
description: Run /devspec.diagram using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.diagram`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.diagram.prompt.md` and `.github/agents/devspec.diagram.agent.md` as the source of intent.
- Preserve Mermaid as the default output, pass through `format=svg` for SVG-only output, and pass through `format=mermaid+svg` for both Mermaid and SVG.
- For SVG output, use `devspec/architecture/_template/diagram.svg`, durable targets under `devspec/architecture/images/`, and the SVG validation rules from `.github/prompts/PATTERNS.md#svg-output-pattern`.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
