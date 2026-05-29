# Architecture Diagrams

Use this folder for durable Mermaid diagrams that are more specific than the high-level architecture context in `devspec/architecture/overview.md`.

Store module, feature workflow, process-flow, user journey, sequence, state, class/domain, and cross-feature diagrams as one Markdown file per subject. Track proposed, generated, skipped, or blocked diagram work with evidence, confidence, and tags in `devspec/architecture/artifact-queue.md`.

Use Title Case for diagram display names and lowercase sequence-prefixed kebab-case for subject slugs and filenames. Queue ID `DIA-001` maps to subject and file prefix `dia-001-`; for example, `DIA-001 - Order Fulfillment Flow` uses `devspec/architecture/diagrams/dia-001-order-fulfillment-flow.md`. Existing `DIA-*` numbers and `dia-NNN-*` files must not be renumbered.

Keep default subjects language-neutral after the sequence prefix, such as `dia-NNN-system-context`, `dia-NNN-runtime-containers`, `dia-NNN-dependency-graph`, or `dia-NNN-authentication-authorization-flow`. Use `dia-NNN-hybrid-user-to-data-operational-flow` for the durable hybrid flow that connects user entry points, application boundaries, services, data stores, validations, operational states, and outcomes.

Queue `Diagram type` records the Mermaid family only. The generated diagram artifact records the full Mermaid declaration, such as `flowchart LR`, `flowchart TD`, `sequenceDiagram`, or `stateDiagram-v2`.
