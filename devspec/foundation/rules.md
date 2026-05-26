# Operational Rules

Use this artifact for project-operational rules that affect planning, implementation, review, or release. Keep enduring principles in `devspec/constitution.md`; keep product goals and scope boundaries in `project-context.md`.

## Rule Governance

| Boundary | Guidance |
| --- | --- |
| Purpose | Record operational constraints, governance requirements, delivery gates, and evolving project rules. |
| Exclusions | Do not duplicate durable principles from `devspec/constitution.md` or product intent from `project-context.md`. |
| Record quality | Write actionable records with scope, enforcement point, source, and confidence. |
| Optional content | Omit rows or sections that have no project-specific content. |

## Operational Rule Catalog

Use this section for hard constraints, compliance requirements, and forbidden patterns. Use `Type` to distinguish the rule kind instead of creating separate overlapping sections.

| Type | Rule | Scope | Requirement or prohibition | Enforcement point | Evidence, rationale, or preferred alternative | Source | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

## Delivery Gate Catalog

| Gate | Applies to | Required evidence | Blocking condition | Source | Confidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Work-Item Handling Rules

Use this section for rules that vary by work-item type or workflow stage. These defaults apply unless a stricter project-specific rule or delivery gate supersedes them.

| Work-item type | Stage | Requirement |
| --- | --- | --- |
| bug | Intake and readiness | Capture expected behavior, actual behavior, reproduction steps, impact, and regression context unless blocked. |
| bug | Planning | Include reproduce, fix, and regression-validation work when practical. |
| bug | Implementation | Record regression validation and useful before-and-after snippets for code fixes. |
| bug | Review | Review bugs with meaningful regression risk before closure. |
| security-vulnerability | Intake and readiness | Capture severity, affected scope, attack surface, exploitability, disclosure status, and containment or remediation plan. |
| security-vulnerability | Shared artifacts | Minimize or redact sensitive exploit details when full disclosure is unsafe. |
| security-vulnerability | Planning | Include impact confirmation, remediation, supported-version verification, and follow-up needs when applicable. |
| security-vulnerability | Implementation | Verify remediation across affected supported versions and record backport, release, or advisory follow-up. |
| security-vulnerability | Review | Review security vulnerabilities before closure. |
| all | Review | Check scope adherence, bugs, regressions, missing validation, and rule violations against the finalized brief. |
| all | Changes requested | Route the work item back to implementation before marking it complete. |

## Exceptions and Waivers

Include this section only when exception handling differs from the normal rules or gates.

| Exception | Affected rule or gate | Approval or handling process | Status | Source |
| --- | --- | --- | --- | --- |
|  |  |  | open |  |
