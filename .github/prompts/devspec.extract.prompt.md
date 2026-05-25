---
name: "devspec.extract"
description: "Create or refresh devspec constitution, architecture, and foundation artifacts from current root, repo URLs, local repo paths, or named multi-repo sources."
argument-hint: "Optional: leave blank for current root, paste one repo URL/path, or use Name - path pairs"
agent: "devspec.extract"
---

Create or refresh `devspec/constitution.md`, `devspec/architecture/overview.md`, and relevant live `devspec/foundation/*.md` artifacts from supported repository sources.

Optional user input:
${input:extractSources:Optional: leave blank for current root, paste one repo URL/path, or use Name - path pairs}
