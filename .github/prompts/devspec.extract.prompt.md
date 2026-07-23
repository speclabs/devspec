---
name: "devspec.extract"
description: "Create or refresh structured, evidence-backed devspec extraction state, constitution, architecture, foundation, process-flow, and diagram queue artifacts from current root, repository URLs, local repository paths, or named multi-repo sources."
argument-hint: "Optional: leave blank for current root, paste one repository URL/path, use Name - path pairs, or include diagram format=svg / format=html / format=mermaid / format=svg+html / format=svg+mermaid / format=svg+html+mermaid / format=html+mermaid"
agent: "devspec.extract"
---

Create or refresh `devspec/foundation/extraction-state.md`, `devspec/constitution.md`, `devspec/architecture/overview.md`, relevant live `devspec/foundation/*.md` artifacts, business-centric process-flow candidates, and language-neutral diagram queue candidates from supported repository sources. SVG is the default diagram output; optional Markdown and HTML format tokens are preserved as diagram generation preferences and honored only after explicit generation approval. Keep extracted output developer-facing, compact, evidence-backed, resumable, and structured. Treat constitution changes as confirmation-gated candidates and route operational gates, compliance procedures, enforcement details, and evolving governance requirements to `devspec/foundation/rules.md`.

Optional user input:

<runtime_input>
${input:extractSources:Optional: leave blank for current root, paste one repository URL/path, use Name - path pairs, or include diagram format=svg / format=html / format=mermaid / format=svg+html / format=svg+mermaid / format=svg+html+mermaid / format=html+mermaid}
</runtime_input>
