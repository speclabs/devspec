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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/rules.md`.
- Keep this artifact focused on project-operational hard constraints, not enduring principles that belong in `devspec/constitution.md`.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
