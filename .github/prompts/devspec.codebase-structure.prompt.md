---
name: "devspec.codebase-structure"
description: "Create or update devspec foundation codebase structure from required user-provided repository layout, module boundaries, ownership seams, integration boundaries, and multi-repo configuration when applicable."
argument-hint: "Describe the repository layout, module boundaries, ownership seams, integration boundaries, and multi-repo configuration when applicable"
agent: "devspec.codebase-structure"
---

Create or update `devspec/foundation/codebase-structure.md`.

Required user input:
${input:codebaseStructureInput:Describe the repository layout, module boundaries, ownership seams, and integration boundaries}

Execution:
- Pass the required input to `devspec.codebase-structure`; the agent owns validation, artifact updates, clarification, multi-repo handling, and handoff behavior.
