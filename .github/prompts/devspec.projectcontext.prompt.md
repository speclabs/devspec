---
name: "devspec.projectcontext"
description: "Create or update devspec foundation project context from required user-provided product vision, users, goals, non-goals, and business constraints."
argument-hint: "Describe the product vision, users, goals, non-goals, and business constraints"
agent: "devspec.projectcontext"
---

Create or update `devspec/foundation/project-context.md`.

Required user input:
${input:projectContextInput:Describe the product vision, users, goals, non-goals, and business constraints}

Execution:
- Pass the required input to `devspec.projectcontext`; the agent owns validation, artifact updates, clarification, and handoff behavior.
