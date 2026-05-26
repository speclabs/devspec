# Meta

Use this artifact as the work-item control record. Keep only identity, triage, workflow status, resume state, intake provenance, ownership, dates, and links. Put detailed story content in `story.md`, implementation readiness in `finalize.md`, and execution state in `tasks.md` or `implement.md`.

## Work Item Identity

| Field | Value |
| --- | --- |
| Title | |
| Folder name | |
| Naming status | valid, needs-confirmation, legacy |

## Classification

| Field | Value |
| --- | --- |
| Type | feature, bug, security-vulnerability |
| Severity | low, medium, high, critical, n/a for feature |
| Priority | record for features when available |
| Disclosure status | internal, coordinated, public, n/a |

## Triage Index

Use this section for routing and lookup only. Keep narrative impact, acceptance criteria, and dependency details in `story.md`.

| Field | Value |
| --- | --- |
| Customer impact summary | |
| Affected scope | |
| Affected versions | |
| Multi-repo dependency | yes, no |
| Related repos | repo names only |
| Detail source | `story.md` |

## Workflow Status

| Field | Value |
| --- | --- |
| Work item status | See `devspec/glossary.md#work-item-status-values` |
| Readiness status | See `devspec/glossary.md#review-and-readiness-status-values` |
| Review status | See `devspec/glossary.md#review-and-readiness-status-values` |

## Resume State

| Field | Value |
| --- | --- |
| Current stage | |
| Current command | |
| Current agent | |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | |
| Resume notes | |
| Updated | |

## Intake Provenance

| Field | Value |
| --- | --- |
| Source resolution status | See `devspec/glossary.md#source-resolution-status-values` |
| Source system | |
| Identifier | |
| URL | |
| Confirmation status | confirmed, rejected, pending, n/a |
| Resolution notes | |

## Ownership And Dates

| Field | Value |
| --- | --- |
| Owner | |
| Reviewer | |
| Created | |
| Updated | |

## Related Links

| Type | Link |
| --- | --- |
| Parent work item | |
| Related ADRs | |
| Related PRs or commits | |
