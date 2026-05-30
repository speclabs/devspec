# Architecture Diagram

Use this artifact for one durable architecture, module, feature, workflow, process-flow, user journey, sequence, state, or domain diagram. Keep diagram status in `devspec/architecture/artifact-queue.md`; keep only generated content, supporting evidence, assumptions, and maintenance notes here.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | diagram |
| Current command | `/devspec.diagram` |
| Current agent | devspec.diagram |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | |
| Recommended option | |
| Resume command | `/devspec.diagram` |
| Resume notes | |
| Updated | |

## Diagram Metadata

| Field | Value |
| --- | --- |
| ID | |
| Display title | `DIA-NNN - <Title Case Diagram Name>` |
| Scope | architecture, module, feature, workflow, user-journey |
| Diagram type | flowchart, sequenceDiagram, journey, stateDiagram, classDiagram, erDiagram |
| Mermaid declaration | flowchart TD, flowchart LR, flowchart BT, sequenceDiagram, journey, stateDiagram-v2, classDiagram, erDiagram |
| Subject | `dia-NNN-<diagram-name>` |
| Confidence | observed, high-confidence, low-confidence |
| Tags | |
| Queue row | `devspec/architecture/artifact-queue.md#diagram-queue-register` |

## Mermaid Diagram

Use simple Mermaid internal naming. Keep durable `DIA-*` IDs and `dia-NNN-*` subjects in metadata and filenames only. In Mermaid content, use short alphanumeric node IDs, double-quoted node labels of 1-4 words, and short edge labels for interaction context. Do not put HTTP verbs, routes, status codes, DTO names, payload names, Swagger details, or framework boilerplate in flowchart nodes unless the diagram is specifically about a startup or request pipeline.

```mermaid
flowchart TD
```

## Source Evidence and Assumptions

Use `evidence` for directly supported code, docs, config, ADRs, or user-confirmed facts. Use `assumption` only when the diagram depends on an inference that is not fully confirmed.

| Type | Source or assumption | Diagram impact | Resolution |
| --- | --- | --- | --- |
| evidence |  |  | confirmed |
| assumption |  |  | open |

## Maintenance Notes

| Note | Action or owner | Resolution state |
| --- | --- | --- |
|  |  | open |
