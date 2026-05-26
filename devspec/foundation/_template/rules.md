# Rules

This file holds project-operational constraints, governance rules, and delivery gates.

## Scope Reminder

- Use this file for operational constraints, delivery gates, and evolving project rules.
- Do not duplicate enduring principles that belong in `devspec/constitution.md`.
- Write rules as actionable records with scope, enforcement point, source, and confidence.
- Omit optional sections that have no project-specific content.

## Hard Constraints

| Rule | Scope | Requirement | Enforcement point | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
| <rule-name> | <system-or-work-scope> | <must-do-or-must-not-do> | <planning-implementation-review-release> | <source-or-user-input> | confirmed |

## Compliance Requirements

Include this section only when compliance requirements exist.

| Requirement | Applies to | Required action | Evidence or policy source | Confidence |
| --- | --- | --- | --- | --- |
| <requirement> | <data-system-or-work-type> | <action-required> | <source-or-user-input> | confirmed |

## Forbidden Patterns

Include this section only when forbidden patterns exist.

| Pattern | Scope | Why forbidden | Preferred alternative | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
| <pattern> | <scope> | <risk-or-policy-reason> | <alternative> | <source-or-user-input> | confirmed |

## Delivery Gates

| Gate | Applies to | Required evidence | Blocking condition | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
| <gate-name> | <work-type-or-release-stage> | <validation-or-approval-required> | <what blocks completion> | <source-or-user-input> | confirmed |

## Bug Handling Rules

| Stage | Requirement |
| --- | --- |
| Intake and readiness | Capture expected behavior, actual behavior, reproduction steps, impact, and regression context unless blocked. |
| Planning | Include reproduce, fix, and regression-validation work when practical. |
| Implementation | Record regression validation and useful before-and-after snippets for code fixes. |
| Review | Review bugs with meaningful regression risk before closure. |

## Security Vulnerability Rules

| Stage | Requirement |
| --- | --- |
| Intake and readiness | Capture severity, affected scope, attack surface, exploitability, disclosure status, and containment or remediation plan. |
| Shared artifacts | Minimize or redact sensitive exploit details when full disclosure is unsafe. |
| Planning | Include impact confirmation, remediation, supported-version verification, and follow-up needs when applicable. |
| Implementation | Verify remediation across affected supported versions and record backport, release, or advisory follow-up. |
| Review | Review security vulnerabilities before closure. |

## Review Rules

| Rule | Requirement |
| --- | --- |
| Review focus | Check scope adherence, bugs, regressions, missing validation, and rule violations against the finalized brief. |
| Changes requested | Route the work item back to implementation before marking it complete. |

## Exceptions

Include this section only when exception handling differs from the normal gates.

| Exception | Process | Status |
| --- | --- | --- |
|  |  | open |
