# Work-Item Diagrams

Use this file only for explicit or clearly temporary work-item diagrams, such as a one-off bug reproduction flow, migration path, security incident or threat flow, temporary implementation plan, or experiment.

Reusable process flows, feature workflows, module workflows, user journeys, sequences, and state diagrams should live under `devspec/architecture/diagrams/` and be referenced from the work item.

Do not keep a separate diagram index or status here. `devspec/architecture/artifact-queue.md` owns diagram status from `devspec/glossary.md#artifact-status-values`. This file owns only temporary work-item-specific diagram content and the resume state needed to continue the diagram command.

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

## Diagram Content

### DIA-001 - <subject>

| Field | Value |
| --- | --- |
| Type | |
| Subject | |
| Queue source | `devspec/architecture/artifact-queue.md` |
| Evidence sources | |
| Confidence | observed, high-confidence, low-confidence |
| Assumptions | none or listed below |
| Notes | |

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#64748b', 'clusterBkg': '#0f172a', 'clusterBorder': '#334155'}}}%%
flowchart TD
    %% classDef palette — include only roles present in this diagram
    classDef ui fill:#083344,stroke:#22d3ee,color:#e2e8f0
    classDef svc fill:#064e3b,stroke:#34d399,color:#e2e8f0
    classDef db fill:#4c1d95,stroke:#a78bfa,color:#e2e8f0
    classDef ext fill:#78350f,stroke:#fbbf24,color:#e2e8f0
    classDef sec fill:#881337,stroke:#fb7185,color:#e2e8f0
    classDef evt fill:#7c2d12,stroke:#fb923c,color:#e2e8f0
    classDef actor fill:#1e293b,stroke:#94a3b8,color:#e2e8f0
    classDef gen fill:#1e293b,stroke:#64748b,color:#e2e8f0

    %% Pad all node labels and edge labels with &nbsp; on each side for readability
    %% e.g.  Svc["&nbsp;Auth Service&nbsp;"]   -->|"&nbsp;Validates&nbsp;"|
    %% nodes and subgraphs here
    %% cross-subgraph arrows after all subgraph...end blocks
    %% class assignments at the end: class Node1,Node2 className
```
