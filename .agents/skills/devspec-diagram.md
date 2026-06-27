---
name: devspec-diagram
description: Run /devspec.diagram using the canonical devspec command registry and Copilot reference contract.
---

Execute canonical command `/devspec.diagram`.

- Read `devspec/adapters/command-registry.md` for the command contract.
- Read `.github/prompts/devspec.diagram.prompt.md` and `.github/agents/devspec.diagram.agent.md` as the source of intent.
- Preserve SVG as the default output. Pass through any non-duplicated `format=` combination of `svg`, `html`, and `mermaid`; examples include `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, and `format=html+mermaid`.
- For SVG output, select the matching template from `.github/prompts/PATTERNS.md#svg-output-pattern`, including architecture, process-flow, sequence, state/lifecycle, domain-model, journey-map, timeline-plan, quadrant-analysis, and mindmap templates. Durable targets stay under `devspec/architecture/images/`, and validation follows `.github/prompts/PATTERNS.md#svg-output-pattern`.
- Keep every generated SVG and HTML diagram on the shared dark architecture-style visual contract from `.github/prompts/PATTERNS.md#svg-output-pattern`, including custom smaller SVGs. Do not produce white/default/simple diagram styling unless the user explicitly requests a light or custom theme.
- Preserve required inputs, output artifacts, status values, gates, handoff order, and recovery behavior.
- Use Git-tracked `devspec/` artifacts for recovery before relying on chat history or Antigravity artifacts.
- Treat unsupported Antigravity behavior as an adapter limitation, not a workflow change.

Command input comes from the user's current message.
