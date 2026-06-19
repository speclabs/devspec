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

Use one row per blocker and at most one `open` row. Open blockers must preserve the question basis: source artifact or evidence, blocking gap, material impact, question intent, option labels including `Custom Answer`, recommended option with reason, impacted artifacts, continuation condition, and next action. When no blocker is active, set `Pending user question` to `none` and put the handoff in `Next required action`.

| ID | Status | Source artifact or evidence | Blocking gap | Material impact | Question | Options | Recommended option and reason | User answer | Impacted artifacts | Continuation condition or next action | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLAR-001 | open, resolved, superseded, withdrawn | `story.md`, `finalize.md`, user input, provider evidence, repository evidence, or other source |  |  |  | intent; option labels including `Custom Answer` |  |  |  |  |  |
