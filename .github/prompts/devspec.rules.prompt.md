---
name: "devspec.rules"
description: "Create or update devspec foundation rules from required user-provided hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates."
argument-hint: "Describe the hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates"
agent: "devspec.rules"
---

Create or update `devspec/foundation/rules.md`.

Required user input:
${input:rulesInput:Describe the hard constraints, compliance requirements, forbidden patterns, governance rules, and delivery gates}

Execution:
- Pass the required input to `devspec.rules`; the agent owns validation, artifact updates, clarification, rules scoping, and handoff behavior.
