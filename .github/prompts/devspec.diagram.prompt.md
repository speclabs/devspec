---
name: "devspec.diagram"
description: "Generate or update one evidence-backed diagram, defaulting to Mermaid with opt-in SVG output, or batch-generate queued process-flow diagrams."
argument-hint: "Describe the diagram subject, scope, diagram type, related work item, all process-flow diagrams, or optional format=svg / format=mermaid+svg"
agent: "devspec.diagram"
---

Generate or update one diagram for the requested subject, or batch-generate eligible queued process-flow diagrams when explicitly requested, using canonical naming, sequence-prefixed subject slugs, and diagram output guidance.

Mermaid is the default output. Use `format=svg` for SVG-only output and `format=mermaid+svg` for both Mermaid and SVG.

Required user input:
${input:diagramInput:Describe the diagram subject, scope, diagram type, related work item, all process-flow diagrams, or optional format=svg / format=mermaid+svg}
