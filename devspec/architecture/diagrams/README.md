# Architecture Diagrams

Use this folder for durable Markdown diagram artifacts that are more specific than the high-level architecture context in `devspec/architecture/overview.md`. Mermaid is the default generated diagram content; SVG output is opt-in with `format=svg` or `format=mermaid+svg`.

Store module, feature workflow, process-flow, user journey, sequence, state, class/domain, and cross-feature diagrams as one Markdown file per subject. Store durable SVG images under `devspec/architecture/images/dia-NNN-<diagram-name>.svg` when requested. Track proposed, generated, skipped, or blocked diagram work with evidence, confidence, output format, and tags in `devspec/architecture/artifact-queue.md`.

## File and Queue Naming

Use Title Case for diagram display names and lowercase sequence-prefixed kebab-case for subject slugs and filenames. Queue ID `DIA-001` maps to subject and file prefix `dia-001-`; for example, `DIA-001 - Order Fulfillment Flow` uses `devspec/architecture/diagrams/dia-001-order-fulfillment-flow.md`. Existing `DIA-*` numbers and `dia-NNN-*` files must not be renumbered.

Keep default subjects language-neutral after the sequence prefix, such as `dia-NNN-system-context`, `dia-NNN-runtime-containers`, `dia-NNN-dependency-graph`, or `dia-NNN-authentication-authorization-flow`. Use `dia-NNN-hybrid-user-to-data-operational-flow` for the durable hybrid flow that connects user entry points, application boundaries, services, data stores, validations, operational states, and outcomes.

Queue `Diagram type` records the logical diagram family only. The generated diagram artifact records the output format, and records the full Mermaid declaration such as `flowchart LR`, `flowchart TD`, `sequenceDiagram`, `stateDiagram-v2`, or `erDiagram` when Mermaid output is selected.

`DIA-*` IDs, `dia-NNN-*` subjects, and `dia-NNN-*` filenames are durable diagram file and diagram queue naming conventions. They must not leak into Mermaid internal naming or SVG visible labels unless they are part of metadata outside the diagram content.

## SVG Output

- `/devspec.diagram <subject>` generates Mermaid by default.
- `/devspec.diagram format=svg <subject>` generates SVG-only visual output plus the required Markdown metadata artifact.
- `/devspec.diagram format=mermaid+svg <subject>` generates both the Mermaid block and the SVG companion file.
- For SVG-only output, keep the Markdown artifact for resume state, metadata, evidence, assumptions, queue linkage, and SVG target reference.
- Use `devspec/architecture/_template/diagram.svg` as the starting point for durable SVG output and validate generated SVG as XML before reporting success.

## Mermaid Readability

- Use simple internal names: short alphanumeric node IDs such as `AuthCtrl` or `ProviderSvc`, double-quoted node labels of 1-4 words such as `AuthCtrl["Authentication Controller"]`, and 2-3 word edge labels such as `-->|"API Calls"|`.
- Put interaction context on edge labels, not inside node labels.
- Do not use `\n` or `<br>` line breaks inside node labels or edge labels.

## Flowchart Scope

- Keep architectural flowcharts and graphs structurally unidirectional and adjacent by layer.
- Map dependency or invocation direction, such as UI -> API -> service -> repository -> database.
- Avoid cross-layer arrows that skip layers.
- Treat return paths as implied by downward invocation arrows.
- Keep each architectural flowchart focused on one primary business domain at macro level, not overloaded graphs or component internals.
- Do not use decision diamonds, if/else paths, validation loops, error branches, UI micro-interactions, HTTP return codes, validation exceptions, or database error returns unless the user explicitly requests an algorithm or activity flowchart.

## Sequence and Boundary Guidance

- Use `sequenceDiagram` when exact step-by-step request and response behavior is required.
- Show messages between distinct participants only.
- Default to the happy path, omit generic error `alt` or `opt` blocks unless requested, collapse pass-through API client helpers, and use method names such as `AuthenticateAsync(req)` for message labels.
- Keep runtime communication and compile-time project dependencies in separate diagrams; default to runtime or logical data flow unless the user explicitly requests a project dependency graph.
- Logical architecture diagrams must include only actual end users, client applications, runtime components, data stores, and external systems that interact with the live application.
- Exclude developers, maintainers, Git, CI/CD, deployment pipelines, build artifacts, and source-code project files unless the diagram is specifically about SDLC, build, deployment, or static project dependencies.
- Place databases owned and exclusively used by the application inside the system boundary.

## Detail to Avoid

Avoid API, tech stack, and framework bloat in generated Mermaid content. Do not put HTTP verbs, route templates, status codes, DTO or payload names, Swagger details, framework versions, specific library names, hosting models, or standard framework wiring into flowchart nodes unless the requested diagram is specifically about startup, request-pipeline, infrastructure-layer, or physical deployment behavior.
