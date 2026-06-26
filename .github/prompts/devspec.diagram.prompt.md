---
name: "devspec.diagram"
description: "Generate or update one evidence-backed diagram, defaulting to SVG with optional Mermaid and HTML output, or batch-generate queued process-flow diagrams."
argument-hint: "Describe the diagram subject, scope, diagram type, related work item, all process-flow diagrams, or optional format=svg / format=html / format=mermaid / format=svg+html / format=svg+mermaid / format=svg+html+mermaid / format=html+mermaid"
agent: "devspec.diagram"
---

Generate or update one diagram for the requested subject, or batch-generate eligible queued process-flow diagrams when explicitly requested, using canonical naming, sequence-prefixed subject slugs, and diagram output guidance.

SVG is the default output. Use `format=` with one or more of `svg`, `html`, and `mermaid` joined by `+`. Example: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`.

Required user input:
${input:diagramInput:Describe the diagram subject, scope, diagram type, related work item, all process-flow diagrams, or optional format=svg / format=html / format=mermaid / format=svg+html / format=svg+mermaid / format=svg+html+mermaid / format=html+mermaid}
