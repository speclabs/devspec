---
name: "devspec.extract"
description: "Create or refresh devspec constitution, architecture, and foundation artifacts from one or more GitHub, Azure DevOps, or GitLab repository URLs, or from local repository folder paths."
argument-hint: "Paste one or more supported repo URLs or local repo folder paths"
agent: "devspec.extract"
---

Create or refresh `devspec/constitution.md`, `devspec/architecture/overview.md`, and the relevant `devspec/foundation/*.md` artifacts from supported repository sources.

Required user input:
${input:extractSources:Paste one or more supported repo URLs or local repo folder paths}

Execution:
- Pass the required repository sources to `devspec.extract`; the agent owns source validation, evidence extraction, artifact updates, confirmations, artifact-queue resumption, and handoff behavior.
