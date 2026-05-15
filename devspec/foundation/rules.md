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

- Bugs must record expected behavior, actual behavior, reproduction steps, user or customer impact, and regression status before being marked ready unless a documented blocker prevents it.
- Bug fixes must include regression validation appropriate to the affected area.

## Security Vulnerability Rules

- Security vulnerabilities must record severity, affected scope, attack surface, exploitability, and a containment or remediation plan before being marked ready.
- Sensitive exploit details should be minimized or redacted in shared artifacts when broader repository visibility makes full disclosure unsafe.
- Security fixes must verify remediation across affected supported versions and record backport, release, or advisory follow-up when applicable.

## Review Rules

- Code review should check scope adherence, bugs, regressions, missing validation, and rule violations against the finalized brief.
- Bugs with meaningful regression risk should receive review before closure.
- Security vulnerabilities must receive review before closure.
- Review findings marked `changes-requested` must route the work item back to implementation before the item is considered complete.

## Exceptions

- Exception process:
