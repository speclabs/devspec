# Clarify

Use this artifact only for blocking ambiguity resolution. Keep resumability in `Resume State`, the single unresolved question in `Active Blocker`, answered or superseded questions in `Resolution Log`, and the handoff result in `Clarification Outcome`. Do not duplicate story or finalize details; reference the impacted artifact and section instead.

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
| Recommended option | see `Active Blocker` or none |
| Resume command | `/devspec.clarify` |
| Resume notes | |
| Updated | |

## Active Blocker

Use this section only for the one unresolved blocking question. Set `Status` to `none` when no blocker is active.

| Field | Value |
| --- | --- |
| ID | |
| Source artifact | `story.md`, `finalize.md`, user input, or other source |
| Blocking gap | |
| Question | |
| Options | include `Custom Answer` |
| Recommended option | |
| Recommendation reason | |
| Asked | |
| Status | open, none |

## Resolution Log

Record only answered, superseded, or withdrawn blockers here. Keep the active open blocker in `Active Blocker` until it is resolved.

| ID | Date | Source artifact | Question | User answer | Impacted artifacts | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | resolved, superseded, withdrawn |

## Clarification Outcome

| Field | Value |
| --- | --- |
| Blocking status | blocked, unblocked |
| Open blocker ID | |
| Handoff target | `/devspec.clarify` while blocked; `/devspec.finalize` when unblocked |
| Outcome notes | |
