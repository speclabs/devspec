---
name: "devspec.solution-structure"
description: "Create or update devspec foundation solution structure from required user-provided repository layout, module boundaries, ownership seams, and integration boundaries."
argument-hint: "Describe the repository layout, module boundaries, ownership seams, and integration boundaries"
agent: "devspec.solution-structure"
---

Create or update `devspec/foundation/solution-structure.md`.

Required user input:
${input:solutionStructureInput:Describe the repository layout, module boundaries, ownership seams, and integration boundaries}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Write or update `devspec/foundation/solution-structure.md`.
- Focus on repo and module structure, not broad system architecture.
- Update the file in place if it already exists.
- Summarize the file updated, key changes, and open questions.
