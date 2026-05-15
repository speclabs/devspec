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
- If required details remain missing or ambiguous, ask exactly one clarification or confirmation question at a time using clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's answer before asking the next question.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Write or update `devspec/foundation/project-context.md`.
- Keep the artifact concise, structured, and durable for later stages.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, questions resolved, remaining blockers if any, and the recommended next step or prompt to run.
