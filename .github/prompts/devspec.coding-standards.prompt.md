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
- Follow the [Prerequisite Validation Pattern](PATTERNS.md); required user input is mandatory for this stage.
- Accept direct standards content, links to existing standards, repository-relative paths to standards docs, or a mix of those inputs.
- Follow the [Interactive Question Pattern](PATTERNS.md) when required details remain missing or ambiguous.
- Write or update `devspec/foundation/coding-standards.md`.
- Organize the artifact by language or framework when applicable, then capture cross-cutting standards that apply across the codebase.
- Record standards source links or document paths when the user provides them.
- Capture language-specific details such as file naming, indentation, regions, member grouping and ordering, formatting, linting, testing, framework conventions, database or SQL indentation patterns, and XML or developer comment expectations when they are provided or confirmed.
- Always record a documentation-comment rule that requires XML documentation comments where the language supports them and concise developer comments for non-obvious implementation details elsewhere.
- Always record a member-ordering rule that uses separate regions for each member type, such as properties, methods, and events, then sorts members within each region by access specifier and by name.
- Keep at least one short example for each language or framework section when the user provides one or confirms one.
- Keep the artifact actionable for later `finalize`, `tasks`, and `implement` stages.
- Update the file in place if it already exists.
- Follow the [Output Closure Pattern](PATTERNS.md).
