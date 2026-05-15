---
name: "devspec.coding-standards"
description: "Create or update devspec foundation coding standards from required user-provided engineering practices, testing expectations, logging, documentation, and review standards."
argument-hint: "Describe the engineering practices, testing expectations, logging, documentation, and review standards"
agent: "devspec.coding-standards"
---

Create or update `devspec/foundation/coding-standards.md`.

Required user input:
${input:codingStandardsInput:Describe the engineering practices, testing expectations, logging, documentation, and review standards}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Write or update `devspec/foundation/coding-standards.md`.
- Keep the artifact actionable for later `finalize`, `tasks`, and `implement` stages.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, open questions, and the recommended next step or prompt to run.
