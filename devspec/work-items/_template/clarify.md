# Clarify

Use this artifact only for blocking ambiguity resolution. Keep resumability, handoff, and next action in `Resume State`. Keep active and resolved blockers in `Clarifications`. Do not duplicate story or finalize details; reference the impacted artifact and section instead.

## Resume State

| Field | Value |
| --- | --- |
| Current stage | clarify |
| Current command | `/devspec.clarify` |
| Current agent | devspec.clarify |
| Run status | See `devspec/glossary.md#run-status-values` |
| Current item | |
| Last completed step | |
| Next required action | |
| Pending user question | active blocker ID or none |
| Recommended option | active blocker option or none |
| Resume command | `/devspec.clarify` |
| Resume notes | |
| Updated | |

## Clarifications

Use one row per blocker. Keep at most one row with `open` status; resolved, superseded, and withdrawn rows are the history. When no blocker is active, set `Pending user question` in `Resume State` to `none` and use `Next required action` for the handoff target.

| ID | Status | Source artifact | Blocking gap | Question | Options | Recommended option and reason | User answer | Impacted artifacts | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLAR-001 | open, resolved, superseded, withdrawn | `story.md`, `finalize.md`, user input, or other source |  |  | include `Custom Answer` |  |  |  |  |
