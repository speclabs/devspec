---
name: "devspec.extract"
description: "Create or refresh devspec constitution, architecture, and foundation artifacts from GitHub, Azure DevOps, GitLab, or local repo paths."
argument-hint: "Paste supported repo URLs or local repo paths"
agent: "devspec.extract"
---

Create or refresh `devspec/constitution.md`, `devspec/architecture/overview.md`, and relevant live `devspec/foundation/*.md` artifacts from supported repository sources.

Required user input:
${input:extractSources:Paste supported repo URLs or local repo paths}
