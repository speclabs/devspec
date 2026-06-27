# Work-Item Diagrams

Use this optional Markdown file only for explicit or clearly temporary work-item diagrams when the selected output set includes `mermaid`.

Reusable default SVG diagrams live under `devspec/architecture/images/`; optional durable Mermaid Markdown diagrams live under `devspec/architecture/diagrams/`; optional durable HTML diagrams live under `devspec/architecture/html/`. `devspec/architecture/artifact-queue.md` owns diagram status. Temporary SVGs for this work item belong under `devspec/work-items/<work-item-folder>/images/`; temporary HTML files belong under `devspec/work-items/<work-item-folder>/html/`.

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
| Output format | mermaid, svg+mermaid, html+mermaid, or svg+html+mermaid |
| Subject | |
| SVG target | `devspec/work-items/<work-item-folder>/images/<diagram-name>.svg` when output format includes svg |
| HTML target | `devspec/work-items/<work-item-folder>/html/<diagram-name>.html` when output format includes html |
| Queue source | `devspec/architecture/artifact-queue.md` |
| Evidence sources | |
| Confidence | observed, high-confidence, low-confidence |
| Assumptions | none or listed below |
| Notes | |

Follow `.github/prompts/PATTERNS.md#diagram-extraction-consistency-pattern`, `#mermaid-internal-naming-and-readability-pattern`, `#mermaid-visual-quality-pattern`, and `#svg-output-pattern` when generating content. Mermaid flowcharts must use the dark init block and semantic role palette; when a Mermaid renderer ignores theme settings, use SVG or HTML output as the canonical architecture-style visual and record the limitation in `Notes`.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#64748b', 'clusterBkg': '#0f172a', 'clusterBorder': '#334155'}}}%%
flowchart TD
    classDef gen fill:#1e293b,stroke:#64748b,color:#e2e8f0

    Placeholder["&nbsp;<diagram content>&nbsp;"]

    class Placeholder gen
```

Create this Markdown file only when the selected output set includes `mermaid`. For SVG-only or HTML-only output, store targets in the queue row and generated files instead.
