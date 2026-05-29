---
name: "devspec.extract"
description: "Create or refresh structured, evidence-backed devspec extraction state, constitution, architecture, foundation, and diagram queue artifacts from current root, repository URLs, local repository paths, or named multi-repo sources."
argument-hint: "Optional: leave blank for current root, paste one repository URL/path, or use Name - path pairs"
agent: "devspec.extract"
---

Create or refresh `devspec/foundation/extraction-state.md`, `devspec/constitution.md`, `devspec/architecture/overview.md`, relevant live `devspec/foundation/*.md` artifacts, and language-neutral diagram queue candidates from supported repository sources. Keep extracted output developer-facing, compact, evidence-backed, resumable, and structured.

Optional user input:
${input:extractSources:Optional: leave blank for current root, paste one repository URL/path, or use Name - path pairs}
