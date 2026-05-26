# Architecture Diagram Queue

Use this file as resumable lifecycle state for proposed and generated architecture diagram artifacts. Keep generated diagram content in the target artifact; keep only queue metadata, evidence, confidence, status, and next action or notes here.

Store high-level diagrams in `devspec/architecture/overview.md`, durable detailed diagrams in `devspec/architecture/diagrams/<subject-slug>.md`, and temporary work-item diagrams in `devspec/work-items/<work-item-folder>/diagrams.md`.

## Diagram Queue Register

Add rows only when extraction or `/devspec.diagram` identifies real diagram candidates backed by evidence. Keep one row per diagram subject and update the existing row instead of creating duplicates.

| ID | Scope | Diagram type | Subject | Target location | Evidence | Confidence | Status | Next action or notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Queue Field Definitions

| Field | Guidance |
| --- | --- |
| ID | Use stable IDs such as `DIA-001`, preserving existing IDs and assigning the next available number for new rows. |
| Scope | Use `architecture`, `module`, `feature`, `workflow`, `user-journey`, or `work-item`. Prefer durable scopes over `work-item` unless the diagram is explicitly temporary or work-item-specific. |
| Diagram type | Use Mermaid types: `flowchart`, `sequenceDiagram`, `journey`, `stateDiagram`, or `classDiagram`. |
| Subject | Use a specific subject that can map to one diagram file or one overview section. |
| Target location | Use `devspec/architecture/overview.md#diagram-reference-index` for high-level overview diagrams, `devspec/architecture/diagrams/<subject-slug>.md` for durable detailed diagrams, or `devspec/work-items/<work-item-folder>/diagrams.md#work-item-diagrams` for temporary work-item diagrams. |
| Evidence | Name the source paths, docs, ADRs, queue request, or user-confirmed basis supporting the candidate. |
| Confidence | Use `observed` for direct evidence, `high-confidence` for inference from multiple local evidence points, or `low-confidence` when useful but incomplete evidence needs assumptions before generation. |
| Status | Use `devspec/glossary.md#artifact-status-values`; queue status belongs here, not in diagram indexes or generated diagram content. |
| Next action or notes | Record duplicate-check result, assumptions, blocker details, skip reason, or the next action needed. |
