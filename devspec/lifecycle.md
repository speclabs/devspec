# devspec Lifecycle

Canonical contracts in `devspec/contracts/` own command behavior. This document owns the legal route graph those contracts use. The shared state vocabulary — run states, stages, task statuses, evidence labels, the changed-work baseline, and resume semantics — lives in `devspec/protocols/state.xml`, and `devspec/protocols/run.xml` owns where each state record lives and which fields it holds.

## State records

- A diagram records queue status and returns to its invoking workflow without changing that workflow's state.
- The selected current work item is private convenience state, never workflow evidence and never committed. `devspec/protocols/current-work-item.xml` owns where it is stored and how it is selected, validated, and cleared.

## Work-item stages

| Stage | Required next command or terminal outcome |
|---|---|
| `intake` | `devspec.story` or `devspec.clarify` |
| `refinement` | `devspec.refine` or `devspec.clarify` |
| `finalization` | `devspec.finalize` or `devspec.clarify` |
| `tasks` | `devspec.tasks`, `devspec.clarify`, or `devspec.finalize` to correct the current-revision brief before implementation begins |
| `implementation` | `devspec.implement` or `devspec.clarify` |
| `review` | `devspec.review` or `devspec.clarify` |
| `complete` | terminal (`next: none`) |

A work-item stage that records a material blocker routes to `devspec.clarify` and nowhere else. The foundation, caller, and quickfix triage stages do the same; the quickfix `routed` stage is non-terminal and routes only to `devspec.story`. `devspec/protocols/revision.xml` owns which revision each stage may read and write.

## Route graph

- Existing repository: `devspec.extract → devspec.story`.
- New repository: `devspec.projectcontext → devspec.techstack → devspec.codebase-structure → devspec.coding-standards → devspec.rules → devspec.story`. A targeted foundation update returns to its caller after completing its declared artifact.
- Work item: `devspec.story → devspec.refine → devspec.finalize → devspec.tasks → devspec.implement → devspec.review`. From `finalization`, `devspec.finalize` returns a story with an open or newly exposed requirement gap to `devspec.refine` as an active route, not a blocker. From `tasks`, `devspec.finalize` may re-run once to correct its own brief at the same scope revision while no task is in-progress or complete; it resets `planned_revision` so `devspec.tasks` re-plans. A new or widened requirement is not a correction and goes to `devspec.changerequest`. Review results are `accepted → complete`, `rework-required → devspec.implement`, or `blocked → devspec.clarify`.
- Work-item IDs are optional selectors for switching or resolving ambiguity. Without one, the current-work-item protocol resolves which work item a command acts on.
- `devspec.clarify` resolves one decision and resumes its saved originating command. `devspec.changerequest` is allowed only after finalization and always routes to `devspec.refine` with a new revision before `devspec.finalize` runs again. `devspec.quickfix` ends complete, blocks to `devspec.clarify`, or routes to `devspec.story`. `devspec.diagram` returns to its caller, ends terminal when it was requested directly, or blocks to `devspec.clarify`.
