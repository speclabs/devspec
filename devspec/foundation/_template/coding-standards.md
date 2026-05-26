# Coding Standards

Use this artifact as a compact, evidence-backed catalog for how developers should write, test, document, and review code. Prefer source references and short rules over copied prose. Omit optional rows or sections with no real standards or evidence.

## Standards Evidence Sources

Use this section only for source documents, configuration files, or representative code that support one or more catalog rows. Do not infer coding standards from paths excluded by `devspec/foundation/discovery-exclusions.md`, such as installed dependencies or generated output.

| Source | Source type | Applies to | Confidence | Notes |
| --- | --- | --- | --- | --- |
| <path-or-link> | formatter, linter, standards-doc, config, source-sample, user-input | <language-framework-layer-or-area> | confirmed, observed, inferred, blocked | <why-this-source-matters> |

## Standards Catalog

Use this as the single place for language, framework, testing, error-handling, logging, documentation, review, observed-pattern, and anti-pattern guidance. Add a row only when the rule changes how developers should write or review code. Keep examples as references to `Examples`, not long snippets in this table.

Use `Type` values as follows:
- `rule`: explicit standard from a project source, user instruction, or config.
- `observed-pattern`: recurring style or structure found in source evidence.
- `anti-pattern`: forbidden or discouraged pattern with the preferred replacement in `Developer guidance`.
- `expectation`: cross-cutting review or quality expectation that applies across multiple areas.

| ID | Scope | Category | Type | Developer guidance | Evidence | Confidence | Example |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CS-001 | <language-framework-layer-or-area> | file-naming, formatting, sql-layout, comments, member-ordering, linting, testing, framework, error-handling, logging, documentation, review | rule, observed-pattern, anti-pattern, expectation | <what-to-do-or-avoid-and-preferred-pattern> | <source-id-path-or-link> | confirmed, observed, inferred, blocked | EX-001 or n/a |

## Examples

Include this section only when a short snippet clarifies a style, indentation, naming, grouping, SQL layout, testing pattern, or framework pattern better than a catalog row alone. Keep examples minimal and canonical, usually 5-20 lines. Link each example to one or more catalog row IDs.

### EX-001: <example-name>

Applies to: CS-001
Source: `<source-path>`

```text
<short representative snippet>
```

## Standards Blockers and Conflicts

Use this section only when standards evidence conflicts, required source evidence is missing, or a project decision is needed before agents can apply a standard.

| Topic | Affected catalog row | Conflict or gap | Evidence | Resolution needed | Status |
| --- | --- | --- | --- | --- | --- |
| <topic> | CS-001 or new | <conflict-or-gap> | <source-paths-or-input> | <question-or-decision> | open |
