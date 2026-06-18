# Clarification Record

Use this artifact only for blocking ambiguity resolution. Keep state in `Resume State`; keep active and resolved blockers in `Clarification Log`.

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
| Recommended option | active blocker option and reason or none |
| Resume command | `/devspec.clarify` |
| Resume notes | |
| Updated | |

## Clarification Log

Use one row per blocker and at most one `open` row. Open blockers must preserve question intent, option labels including `Custom Answer`, and the recommended option with reason. When no blocker is active, set `Pending user question` to `none` and put the handoff in `Next required action`.

| ID | Status | Source artifact | Blocking gap | Question | Options | Recommended option and reason | User answer | Impacted artifacts | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLAR-001 | open, resolved, superseded, withdrawn | `story.md`, `finalize.md`, user input, or other source |  |  | intent; option labels including `Custom Answer` |  |  |  |  |
