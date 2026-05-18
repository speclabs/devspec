---
name: "devspec.coding-standards"
description: "Create or update devspec foundation coding standards from required user-provided language-specific or framework-specific standards, engineering practices, or links to existing standards."
argument-hint: "Describe the standards by language or framework, or provide links to existing coding standards"
agent: "devspec.coding-standards"
---

Create or update `devspec/foundation/coding-standards.md`.

Required user input:
${input:codingStandardsInput:Describe the standards by language or framework, or provide links to existing coding standards}

Execution:
- Pass the required input to `devspec.coding-standards`; the agent owns validation, artifact updates, clarification, standards-source handling, and handoff behavior.
