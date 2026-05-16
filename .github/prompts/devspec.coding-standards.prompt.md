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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md#prerequisite-validation-pattern); required user input is mandatory for this stage.
- Accept direct standards content, links to existing standards, repository-relative paths to standards docs, or a mix of those inputs.
- Follow the [Interactive Question Pattern](PATTERNS.md#interactive-question-pattern) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/coding-standards.md`.
- Organize the artifact by language or framework when applicable, then capture cross-cutting standards that apply across the codebase.
- Record standards source links or document paths when the user provides them.
- Capture language-specific details such as file naming, indentation, regions, formatting, linting, testing, framework conventions, and database or SQL indentation patterns when they are provided or confirmed.
- Keep at least one short example for each language or framework section when the user provides one or confirms one.
- Keep the artifact actionable for later `finalize`, `tasks`, and `implement` stages.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md#output-closure-pattern).
