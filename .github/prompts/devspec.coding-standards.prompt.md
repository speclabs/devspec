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
- Follow the [Foundation Update Pattern](PATTERNS.md#foundation-update-pattern).
- Accept direct standards content, links to existing standards, repository-relative paths to standards docs, or a mix of those inputs.
- Organize the artifact by language or framework when applicable, then capture cross-cutting standards that apply across the codebase.
- Record standards source links or document paths when the user provides them.
- Capture file naming, indentation, grouping, formatting, linting, testing, framework, database/SQL, XML-doc, and developer-comment rules when provided, detected, or confirmed.
- Keep at least one short example for each language or framework section when the user provides one or confirms one.
- Follow the [Token Stewardship Pattern](PATTERNS.md#token-stewardship-pattern).
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
