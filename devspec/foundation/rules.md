# Rules

This file holds project-operational constraints, governance rules, and delivery gates.

## Scope Reminder

- Use this file for operational constraints, delivery gates, and evolving project rules.
- Do not duplicate enduring principles that belong in `devspec/constitution.md`.

## Hard Constraints

- Constraint 1:

## Compliance Requirements

- Requirement 1:

## Forbidden Patterns

- Pattern 1:

## Delivery Gates

- Gate 1:

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

| Exception | Process | Status |
| --- | --- | --- |
|  |  | open |
