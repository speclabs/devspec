# Work-Item Intake

Use this artifact for detailed work-item intake. Keep identity, classification, source provenance, and routing summaries in `meta.md`; keep work-item decisions in `decisions.md`; keep implementation-ready scope in `finalize.md`.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | story |
| Current command | `/devspec.story` |
| Current agent | devspec.story |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.story` |
| Resume notes | |
| Updated | |

## Intake Source Record

| Field | Value |
| --- | --- |
| External reference | |
| Resolved summary shown | |
| Confirmation basis | `devspec/foundation/provider-integrations.md` |
| User confirmation | confirmed, rejected, pending |
| Manual intake used | yes, no |
| Manual description | |
| Manual acceptance criteria | |

## Work-Item Brief

Use this section for the durable work-item narrative. Keep it concise but specific enough for clarification and finalization.

| Field | Value |
| --- | --- |
| Problem | |
| Intended outcome | |
| User or customer impact | |
| Affected components | |
| Affected versions | |

## Work-Item Details

Use this table for facts that affect clarification, readiness, task planning, or validation. Keep repository paths and access requirements in `devspec/foundation/codebase-structure.md`; keep rule definitions in `devspec/foundation/rules.md`.

| Type | ID | Item | Source | Status |
| --- | --- | --- | --- | --- |
| Acceptance criterion | AC-001 |  | confirmed, provider, manual, user | pending |
| Assumption | ASM-001 |  | confirmed, inferred, user | open |
| Constraint | CON-001 |  | foundation, intake, user | open |
| Dependency | DEP-001 | <dependency-or-none> | intake, user, discovery | open |
| Multi-repo dependency | DEP-REPO-001 | yes, no; related repositories: <repository-names-only> | confirmed, user | open |
| Type-specific note | TS-001 | <bug-or-security-note>; rule source: `devspec/foundation/rules.md` | intake, user, rule | open |
| Risk | RISK-001 |  | intake, user, discovery | open |
| Blocker | BLK-001 |  | intake, user, discovery | open |
