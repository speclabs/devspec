# Architecture Artifact Queue

Use this file as resumable state for architecture visuals, module diagrams, feature workflows, user journeys, and related generated artifacts.

Keep high-level system diagrams in `devspec/architecture/overview.md` and detailed architecture, module, feature workflow, user journey, sequence, and state diagrams in `devspec/architecture/diagrams/<subject-slug>.md`.

Use `devspec/work-items/<work-item-folder>/diagrams.md` only for explicit or clearly temporary work-item diagrams, such as a one-off bug reproduction flow, migration path, security incident or threat flow, temporary implementation plan, or experiment.

## Queue

| ID | Scope | Type | Subject | Target path | Evidence source | Status | Output section | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Add rows only when extraction or `/devspec.diagram` identifies real diagram candidates.

## Scope Rules

- `architecture`: stable system-level structure or cross-system flow.
- `module`: durable module or bounded-context behavior.
- `feature`: reusable feature-level behavior not tied to a single work item.
- `workflow`: process flow across modules, services, or users.
- `user-journey`: user-facing path through product behavior.
- `work-item`: explicit or clearly temporary diagram specific to one story, bug, or security issue.

## Type Rules

- `flowchart`: feature, module, or process workflow.
- `sequenceDiagram`: service, actor, or system interaction over time.
- `journey`: user-facing experience flow.
- `stateDiagram`: lifecycle, status, or transition behavior.
- `classDiagram`: stable domain or structural relationships when useful.

## Status Rules

- `proposed`: candidate identified from evidence, waiting for user confirmation.
- `confirmed`: user approved generation, not yet generated.
- `generated`: artifact was added to the target path.
- `skipped`: user declined generation.
- `blocked`: evidence or context is insufficient.
