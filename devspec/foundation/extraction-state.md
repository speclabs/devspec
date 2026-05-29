# Extraction State

Use this file for the `/devspec.extract` queue and resume state. Keep extracted facts in target artifacts, reusable discovery methods in `devspec/foundation/exploration-state.md`, and diagram lifecycle in `devspec/architecture/artifact-queue.md`.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | extract |
| Current command | `/devspec.extract` |
| Current agent | devspec.extract |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current task | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.extract` |
| Resume notes | |
| Updated | |

## Extraction Queue

| ID | Stage | Target artifact | Evidence focus | Status | Next action | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| EXT-001 | source-and-access | `devspec/foundation/extraction-state.md` | source input, source labels, source validation, access requirements | pending | Validate sources and required access. | |
| EXT-002 | discovery-preparation | `devspec/foundation/discovery-exclusions.md` | exclusions, ignore files, reusable discovery methods | pending | Apply discovery rules before broad search. | |
| EXT-003 | project-context | `devspec/foundation/project-context.md` | documentation, README files, product signals, user-facing behavior | pending | Extract evidence-backed project context. | |
| EXT-004 | technology-stack | `devspec/foundation/tech-stack.md` | manifests, lockfiles, runtime configuration, tooling, CI/CD | pending | Extract stack and version evidence. | |
| EXT-005 | codebase-structure | `devspec/foundation/codebase-structure.md` | layout, modules, work areas, boundaries, integration contracts, multi-repository configuration | pending | Extract placement and boundary guidance. | |
| EXT-006 | coding-standards | `devspec/foundation/coding-standards.md` | style guides, observed patterns, tests, examples | pending | Extract standards and anti-patterns. | |
| EXT-007 | rules-and-constraints | `devspec/foundation/rules.md` | compliance, security, delivery gates, operational constraints | pending | Extract actionable rules only. | |
| EXT-008 | architecture-overview | `devspec/architecture/overview.md` | components, integrations, runtime boundaries, data movement | pending | Extract high-level architecture context. | |
| EXT-009 | diagram-candidates | `devspec/architecture/artifact-queue.md` | evidence-backed diagram candidates and duplicate checks | pending | Queue eligible diagram candidates. | |
| EXT-010 | constitution-candidates | `devspec/constitution.md` | durable principle candidates requiring confirmation | pending | Ask before writing principle changes. | |
| EXT-011 | closure | `devspec/foundation/extraction-state.md` | updated artifacts, blockers, confirmations, next action | pending | Summarize extraction and select one next action. | |

## Blockers and Confirmations

| ID | Kind | Related task | Subject | Required action | Resolution | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  | blocker, confirmation |  |  |  |  |  |
