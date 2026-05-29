# Architecture Diagram Queue

Use this file as the resumable queue register for proposed and generated architecture diagrams. Keep generated diagram content in the target artifact; keep only queue metadata, evidence, confidence, status, and next action or notes here.

Store high-level diagrams in `devspec/architecture/overview.md`, durable detailed diagrams in `devspec/architecture/diagrams/dia-NNN-<diagram-name>.md`, and temporary work-item diagrams in `devspec/work-items/<work-item-folder>/diagrams.md`.

## Diagram Queue Register

Add rows only when extraction or `/devspec.diagram` identifies real diagram candidates backed by evidence. Keep one row per diagram subject and update the existing row instead of creating duplicates.

| ID | Scope | Diagram type | Subject | Target location | Evidence | Confidence | Status | Tags | Next action or notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Queue Field Definitions

| Field | Guidance |
| --- | --- |
| ID | Use stable IDs such as `DIA-001`, preserving existing IDs and assigning the next available number for new rows. |
| Scope | Use `architecture`, `module`, `feature`, `workflow`, `user-journey`, or `work-item`. Prefer durable scopes over `work-item` unless the diagram is explicitly temporary or work-item-specific. |
| Diagram type | Use the Mermaid family only: `flowchart`, `sequenceDiagram`, `journey`, `stateDiagram`, or `classDiagram`. Do not include orientation here. |
| Subject | Use a specific lowercase kebab-case subject that can map to one diagram file or one overview section. For queued architecture diagrams, prefix the subject with the lowercase queue ID, such as `dia-001-order-fulfillment-flow`. |
| Target location | Use `devspec/architecture/overview.md#diagram-reference-index` for high-level overview diagrams, `devspec/architecture/diagrams/dia-NNN-<diagram-name>.md` for durable detailed diagrams, or `devspec/work-items/<work-item-folder>/diagrams.md#diagram-content` for temporary work-item diagrams. |
| Evidence | Name the source paths, docs, ADRs, queue request, or user-confirmed basis supporting the candidate. |
| Confidence | Use `observed` for direct evidence, `high-confidence` for inference from multiple local evidence points, or `low-confidence` when useful but incomplete evidence needs assumptions before generation. |
| Status | Use `devspec/glossary.md#artifact-status-values`; queue status belongs here, not in diagram indexes or generated diagram content. |
| Tags | Use comma-separated lowercase tags such as `process-flow`, `business-process`, `user-journey`, `lifecycle-flow`, or `hybrid-user-to-data-operational-flow` when they apply. Leave blank only when no durable selection tag is useful. |
| Next action or notes | Record duplicate-check result, suggested Mermaid declaration such as `flowchart LR` or `sequenceDiagram`, assumptions, blocker details, skip reason, or the next action needed. |
