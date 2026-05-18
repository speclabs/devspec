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
- Follow the [Foundation Update Pattern](PATTERNS.md#foundation-update-pattern).
- Keep this artifact focused on project-operational hard constraints, not enduring principles that belong in `devspec/constitution.md`.
- Capture compliance requirements, forbidden patterns, delivery gates, review rules, and exception process when known.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
