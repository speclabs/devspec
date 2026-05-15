---
name: "devspec.techstack"
description: "Create or update devspec foundation tech stack from required user-provided languages, frameworks, services, tooling, hosting, and delivery constraints."
argument-hint: "Describe the languages, frameworks, services, tooling, hosting, and delivery constraints"
agent: "devspec.techstack"
---

Create or update `devspec/foundation/tech-stack.md`.

Required user input:
${input:techStackInput:Describe the languages, frameworks, services, tooling, hosting, and delivery constraints}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- If required details remain missing or ambiguous, ask exactly one clarification or confirmation question at a time using clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's answer before asking the next question.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Write or update `devspec/foundation/tech-stack.md`.
- Capture versions, platform constraints, tooling, and operational assumptions when known.
- Organize the artifact by project or repo, using one heading per project.
- Keep tech stack details in Markdown tables.
- Include both the version used in the project and the current market version when that information is available.
- Use web lookup when practical to identify current market versions.
- If the current market version cannot be verified, record that clearly instead of guessing.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, projects covered, key table changes, questions resolved, remaining blockers if any, and the recommended next step or prompt to run.
