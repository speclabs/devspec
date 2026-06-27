# Architecture Diagram Queue

Use this file as the resumable queue register for proposed and generated architecture diagrams. Keep generated diagram content in the target artifact; keep only queue metadata, evidence, confidence, status, output-format guidance, and next action or notes here.

Store high-level diagram references in `devspec/architecture/overview.md`, durable SVG images in `devspec/architecture/images/dia-NNN-<diagram-name>.svg` by default, optional Mermaid Markdown artifacts in `devspec/architecture/diagrams/dia-NNN-<diagram-name>.md`, optional HTML diagram artifacts in `devspec/architecture/html/dia-NNN-<diagram-name>.html`, and temporary work-item diagrams under `devspec/work-items/<work-item-folder>/images/` with optional Mermaid `diagrams.md` or `html/*.html` companions.

## Diagram Queue Register

Add rows only when extraction or `/devspec.diagram` identifies real diagram candidates backed by evidence. Keep one row per diagram subject and update the existing row instead of creating duplicates.

| ID | Scope | Diagram type | Subject | Target location | Evidence | Confidence | Status | Tags | Next action or notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Queue Field Definitions

| Field | Guidance |
| --- | --- |
| ID | Use stable IDs such as `DIA-001`, preserving existing IDs and assigning the next available number for new rows. |
| Scope | Use `architecture`, `module`, `feature`, `workflow`, `user-journey`, or `work-item`. Prefer durable scopes over `work-item` unless the diagram is explicitly temporary or work-item-specific. |
| Diagram type | Use the logical diagram family only: `flowchart`, `sequenceDiagram`, `journey`, `stateDiagram`, `classDiagram`, `erDiagram`, `gantt`, `quadrantChart`, `mindmap`, or `timeline`. Do not include orientation or output format here. |
| Subject | Use a specific lowercase kebab-case subject that can map to one diagram file or one overview section. For queued architecture diagrams, prefix the subject with the lowercase queue ID, such as `dia-001-order-fulfillment-flow`. |
| Target location | Use `devspec/architecture/images/dia-NNN-<diagram-name>.svg` for default durable SVG output, `devspec/architecture/overview.md#diagram-reference-index` for high-level overview references, `devspec/architecture/diagrams/dia-NNN-<diagram-name>.md` for optional Mermaid Markdown artifacts, `devspec/architecture/html/dia-NNN-<diagram-name>.html` for optional HTML artifacts, or work-item `images/`, `diagrams.md#diagram-content`, and `html/` targets for temporary work-item diagrams. Record companion targets in `Next action or notes`. |
| Evidence | Name the source paths, docs, ADRs, queue request, or user-confirmed basis supporting the candidate. |
| Confidence | Use `observed` for direct evidence, `high-confidence` for inference from multiple local evidence points, or `low-confidence` when useful but incomplete evidence needs assumptions before generation. |
| Status | Use `devspec/glossary.md#artifact-status-values`; queue status belongs here, not in diagram indexes or generated diagram content. |
| Tags | Use comma-separated lowercase tags such as `process-flow`, `business-process`, `user-journey`, `lifecycle-flow`, or `hybrid-user-to-data-operational-flow` when they apply. Leave blank only when no durable selection tag is useful. |
| Next action or notes | Record duplicate-check result, output format as one or more of `svg`, `html`, and `mermaid` joined with `+`. Examples: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`. Include suggested Mermaid declaration such as `flowchart LR` or `sequenceDiagram` when the output set includes `mermaid`, SVG target, optional Mermaid or HTML targets, assumptions, blocker details, skip reason, or the next action needed. |
