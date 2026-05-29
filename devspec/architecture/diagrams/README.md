# Architecture Diagrams

Use this folder for durable Mermaid diagrams that are more specific than the high-level architecture context in `devspec/architecture/overview.md`.

Store module, feature workflow, user journey, sequence, state, class/domain, and cross-feature diagrams as one Markdown file per subject. Track proposed, generated, skipped, or blocked diagram work with evidence and confidence in `devspec/architecture/artifact-queue.md`.

Use Title Case for diagram display names and lowercase kebab-case for subject slugs and filenames. Keep default subjects language-neutral, such as `system-context`, `runtime-containers`, `dependency-graph`, or `authentication-authorization-flow`.

Queue `Diagram type` records the Mermaid family only. The generated diagram artifact records the full Mermaid declaration, such as `flowchart LR`, `flowchart TD`, `sequenceDiagram`, or `stateDiagram-v2`.
