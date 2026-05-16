---
name: "devspec.coding-standards"
description: "Create or update devspec foundation coding standards from required user-provided language-specific or framework-specific standards, engineering practices, or links to existing standards."
argument-hint: "Describe the standards by language or framework, or provide links to existing coding standards"
agent: "devspec.coding-standards"
---

Create or update `devspec/foundation/coding-standards.md`.

Required user input:
${input:codingStandardsInput:Describe the standards by language or framework, or provide links to existing coding standards}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- Accept direct standards content, links to existing standards, repository-relative paths to standards docs, or a mix of those inputs.
- If required details remain missing or ambiguous, ask exactly one clarification or confirmation question at a time using clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's answer before asking the next question.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Write or update `devspec/foundation/coding-standards.md`.
- Organize the artifact by language or framework when applicable, then capture cross-cutting standards that apply across the codebase.
- Record standards source links or document paths when the user provides them.
- Capture language-specific details such as file naming, indentation, regions, formatting, linting, testing, and framework conventions when they are provided or confirmed.
- Keep the artifact actionable for later `finalize`, `tasks`, and `implement` stages.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, questions resolved, remaining blockers if any, and the recommended next step or prompt to run.
