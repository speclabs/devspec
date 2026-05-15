---
name: "devspec.codebase-structure"
description: "Create or update devspec foundation codebase structure from required user-provided repository layout, module boundaries, ownership seams, and integration boundaries."
argument-hint: "Describe the repository layout, module boundaries, ownership seams, and integration boundaries"
agent: "devspec.codebase-structure"
---

Create or update `devspec/foundation/codebase-structure.md`.

Required user input:
${input:codebaseStructureInput:Describe the repository layout, module boundaries, ownership seams, and integration boundaries}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Write or update `devspec/foundation/codebase-structure.md`.
- Focus on repo and module structure, not broad system architecture.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, open questions, and the recommended next step or prompt to run.