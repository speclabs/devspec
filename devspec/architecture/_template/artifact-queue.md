# Architecture Artifact Queue

Use this file as resumable state for proposed and generated architecture visuals.

Store high-level diagrams in `devspec/architecture/overview.md`, durable detailed diagrams in `devspec/architecture/diagrams/<subject-slug>.md`, and temporary work-item diagrams in `devspec/work-items/<work-item-folder>/diagrams.md`.

## Queue

| ID | Scope | Type | Subject | Target path | Evidence source | Confidence | Status | Output section | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Add rows only when extraction or `/devspec.diagram` identifies real diagram candidates.

## Scope Values

| Scope | Meaning |
| --- | --- |
| `architecture` | Stable system-level structure or cross-system flow. |
| `module` | Durable module or bounded-context behavior. |
| `feature` | Reusable feature-level behavior not tied to a single work item. |
| `workflow` | Process flow across modules, services, or users. |
| `user-journey` | User-facing path through product behavior. |
| `work-item` | Explicit or temporary diagram specific to one story, bug, or security issue. |

## Diagram Type Values

| Type | Meaning |
| --- | --- |
| `flowchart` | Feature, module, or process workflow. |
| `sequenceDiagram` | Service, actor, or system interaction over time. |
| `journey` | User-facing experience flow. |
| `stateDiagram` | Lifecycle, status, or transition behavior. |
| `classDiagram` | Stable domain or structural relationships when useful. |

## Confidence Values

| Confidence | Meaning |
| --- | --- |
| `observed` | Directly supported by code, docs, config, or ADR evidence. |
| `high-confidence` | Inferred from multiple local evidence points. |
| `low-confidence` | Useful but incomplete evidence; record assumptions before generation. |

## Status Values

Use `devspec/glossary.md#artifact-status-values` for queue status values.
