---
name: "devspec.diagram"
description: "Generate or update one evidence-backed Mermaid diagram, or batch-generate queued process-flow diagrams, using canonical naming and Mermaid declaration guidance."
argument-hint: "Describe the diagram subject, scope, diagram type, related work item, or all process-flow diagrams"
agent: "devspec.diagram"
---

Generate or update one diagram for the requested subject, or batch-generate eligible queued process-flow diagrams when explicitly requested, using canonical naming, sequence-prefixed subject slugs, and Mermaid declaration guidance.

Required user input:
${input:diagramInput:Describe the diagram subject, scope, diagram type, related work item, or all process-flow diagrams}
