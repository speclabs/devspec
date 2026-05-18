# Architecture Artifact Queue

Use this file as resumable extraction state for architecture visuals and related generated artifacts. Keep final generated Mermaid diagrams and user journeys in `devspec/architecture/overview.md`.

## Queue

| ID | Type | Subject | Evidence source | Status | Output section | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Add rows only when extraction identifies real architecture-diagram or user-journey candidates.

## Status Rules

- `proposed`: candidate identified from evidence, waiting for user confirmation.
- `confirmed`: user approved generation, not yet generated.
- `generated`: artifact was added to `overview.md`.
- `skipped`: user declined generation.
- `blocked`: evidence or context is insufficient.
