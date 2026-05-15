---
name: "devspec.projectcontext"
description: "Create or update devspec foundation project context from required user-provided product vision, users, goals, non-goals, and business constraints."
argument-hint: "Describe the product vision, users, goals, non-goals, and business constraints"
agent: "devspec.projectcontext"
---

Create or update `devspec/foundation/project-context.md`.

Required user input:
${input:projectContextInput:Describe the product vision, users, goals, non-goals, and business constraints}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Write or update `devspec/foundation/project-context.md`.
- Keep the artifact concise, structured, and durable for later stages.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, open questions, and the recommended next step or prompt to run.
