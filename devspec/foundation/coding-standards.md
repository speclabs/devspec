# Coding Standards

## Standards Sources

| Source | Type | Applies to | Confidence | Notes |
| --- | --- | --- | --- | --- |
| <path-or-link> | formatter | <language-or-framework> | confirmed | |

## Language And Framework Standards

### Language Or Framework: <name>

| Category | Rule | Evidence | Confidence | Example |
| --- | --- | --- | --- | --- |
| File naming | <rule> | <path-or-config> | confirmed | |
| Formatting and indentation | <indent-size-line-length-brace-style> | <config-or-source-path> | observed | CS-001 |
| Database or SQL layout | <keyword-case-join-indent-query-layout> | <path-or-query-file> | observed | CS-002 |
| Documentation comments | <xml-doc-jsdoc-docstring-rule> | <path-or-docs> | inferred | |
| Developer comments | <when-comments-are-required> | <path-or-docs> | confirmed | |
| Member grouping and ordering | <fields-constructors-public-private-order> | <source-path> | observed | CS-003 |
| Formatting or linting | <tool-and-command> | <config-path> | confirmed | |
| Testing conventions | <test-naming-structure-assertions> | <test-path> | observed | |
| Framework-specific conventions | <framework-pattern> | <source-path> | observed | |

## Observed Patterns

Use this as a compact pattern catalog. Prefer source references plus short examples over long copied code.

| Pattern ID | Pattern | Applies to | Rule | Evidence | Confidence | Example |
| --- | --- | --- | --- | --- | --- | --- |
| CS-001 | <pattern-name> | <language-framework-or-layer> | <rule-to-follow> | <source-path> | observed | CS-001 |

## Formatting Examples

Keep examples minimal and canonical. Use 5-20 lines when possible, enough to show indentation, grouping, naming, or layout.

### CS-001: <formatting-or-pattern-name>

Source: `<source-path>`

```text
<short representative snippet>
```

## Anti-Patterns

| Pattern | Avoid | Evidence | Preferred pattern | Confidence |
| --- | --- | --- | --- | --- |
| <anti-pattern-name> | <what-not-to-do> | <source-or-rule-path> | <preferred-pattern-id-or-rule> | observed |

## Cross-Cutting Expectations

| Area | Expectation | Evidence | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Style and naming | <expectation> | <path-or-rule> | confirmed | |
| Testing | <expectation> | <path-or-rule> | confirmed | |
| Error handling | <expectation> | <path-or-rule> | observed | |
| Logging and observability | <expectation> | <path-or-rule> | observed | |
| Documentation | <expectation> | <path-or-rule> | confirmed | |
| Review | <expectation> | <path-or-rule> | confirmed | |

## Blockers Or Conflicts

| Topic | Conflict or gap | Evidence | Resolution needed |
| --- | --- | --- | --- |
| <topic> | <conflict-or-gap> | <source-paths> | <question-or-decision> |
