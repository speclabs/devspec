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
- Write or update `devspec/foundation/rules.md`.
- Keep this artifact focused on project-operational hard constraints, not enduring principles that belong in `devspec/constitution.md`.
- Update the file in place if it already exists.
- End the response with a recommended next step or next prompt to run.
- Summarize the file updated, key changes, open questions, and the recommended next step or prompt to run.
