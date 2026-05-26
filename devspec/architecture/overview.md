# Architecture Overview

Use this artifact for confirmed high-level architecture context, durable diagram references, architecture decision references, and unresolved architecture gaps. Keep detailed repository layout in `devspec/foundation/codebase-structure.md`, integration contracts in `devspec/foundation/codebase-structure.md#integration-contracts`, proposed diagram lifecycle in `devspec/architecture/artifact-queue.md`, and full ADR content in `devspec/architecture/decisions/`.

## Architecture Context

Use this section for confirmed architecture facts that affect system understanding across major components, integration relationships, runtime boundaries, and important data movement. Keep implementation file placement in `devspec/foundation/codebase-structure.md#work-areas-and-boundaries` and detailed contracts in `devspec/foundation/codebase-structure.md#integration-contracts`.

| Context type | Subject | Summary | Source | Confidence | Developer relevance |
| --- | --- | --- | --- | --- | --- |
| component |  |  |  |  |  |
| integration |  |  |  |  |  |
| data-flow |  |  |  |  |  |

## Diagram Reference Index

Use this section for confirmed high-level diagrams in this file and links to durable detailed diagrams. Do not mirror lifecycle status here; track proposed, pending, generated, skipped, or blocked diagram work in `devspec/architecture/artifact-queue.md`.

| ID | Scope | Diagram type | Subject | Link or section | Notes |
| --- | --- | --- | --- | --- | --- |
|  | architecture, module, feature, workflow, user-journey | flowchart, sequenceDiagram, journey, stateDiagram, classDiagram |  | `devspec/architecture/diagrams/<subject-slug>.md` or section anchor |  |

## Decision Reference Index

Use this section only for pointers to durable ADRs or confirmed architecture decisions. Keep decision status, context, and consequences in the ADR file.

| Decision | Reference | Notes |
| --- | --- | --- |
|  | `devspec/architecture/decisions/<adr-file>.md` |  |

## Architecture Gaps and Blockers

Use this section only for missing or conflicting architecture facts that prevent reliable planning, diagram generation, or architecture decision recording. Keep implementation blockers in work-item artifacts.

| Gap or blocker | Impact | Required resolution | State |
| --- | --- | --- | --- |
|  |  |  | open |
