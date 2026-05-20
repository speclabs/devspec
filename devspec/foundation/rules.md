# Rules

This file holds project-operational hard constraints, governance rules, and delivery gates.

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

- Intake and readiness must capture expected behavior, actual behavior, reproduction steps, user or customer impact, and regression context unless a documented blocker prevents it.
- Planning should usually include reproduce, fix, and regression-validation work.
- Implementation must record regression validation appropriate to the affected area.
- When bug fixes change code, implementation records should include focused before-and-after snippets when useful for review or audit.
- Bugs with meaningful regression risk should receive review before closure.

## Security Vulnerability Rules

- Intake and readiness must capture severity, affected scope, attack surface, exploitability, disclosure status, and a containment or remediation plan before the item is marked ready.
- Sensitive exploit details should be minimized or redacted in shared artifacts when broader repository visibility makes full disclosure unsafe.
- Planning should include impact confirmation, remediation, verification across affected supported versions, and backport, release, or advisory follow-up when applicable.
- Implementation must verify remediation across affected supported versions and record backport, release, or advisory follow-up when applicable.
- Security vulnerabilities must receive review before closure.

## Review Rules

- Code review should check scope adherence, bugs, regressions, missing validation, and rule violations against the finalized brief.
- Review findings marked `changes-requested` must route the work item back to implementation before the item is considered complete.

## Exceptions

- Exception process:
