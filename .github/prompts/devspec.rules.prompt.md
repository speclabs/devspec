---
name: "devspec.rules"
description: "Create or update devspec foundation rules from required user-provided hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates."
argument-hint: "Describe the hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates"
agent: "devspec.rules"
---

Create or update `devspec/foundation/rules.md`.

Required user input:
${input:rulesInput:Describe the hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates}

Requirements:
- Treat the user input as required. If it is missing, stop and ask for it.
- If required details remain missing or ambiguous, ask exactly one clarification or confirmation question at a time using clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's answer before asking the next question.
- Resolve those questions before writing the artifact whenever practical.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Write or update `devspec/foundation/rules.md`.
- Keep this artifact focused on project-operational hard constraints, not enduring principles that belong in `devspec/constitution.md`.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, questions resolved, remaining blockers if any, and the recommended next step or prompt to run.
