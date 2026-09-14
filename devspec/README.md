# devspec

New repository foundation: `projectcontext → techstack → codebase-structure → coding-standards → rules`. Existing repository baseline: `extract` completes the foundation, prepares the applicable diagram list, and asks whether to generate all or selected diagrams. Rare durable cross-work-item principles live in `constitution.md` with stable `CP-###` IDs. `extract` records candidates from evidence; `projectcontext` promotes or retires them only on explicit input.

Work item: `story → refine → finalize → tasks → implement → review`. Every work item goes through refinement after intake, even when the source carried acceptance criteria. Story intake accepts one manual request or, when an authenticated MCP connector is available, one read-only provider work-item reference.
After `story` selects a work item, use the normal work-item commands without repeating its ID. Per-worktree private context resolves the selected story and its recorded `next` action; use an ID only to switch or disambiguate stories.

Use `clarify` only for an active blocker and `quickfix` only for localized, low-risk changes. See `lifecycle.md` for all command transitions.

Each contract in `contracts/` states its own intent, scope, rules, and transitions, and loads the shared behavior it needs from `protocols/`: `state` for the run-state and evidence vocabulary, `run` for preflight and checkpoints, `work` for scope and change discipline, `ask` for material questions, `current-work-item` for ID-free continuation, `revision` for scope revisions, `repo-access` for repository boundaries, and `security` for the OWASP baseline. A rule belongs in a protocol when more than one command needs it.

`diagram` creates static SVG by default. Use `motion=explain` only for an evidence-backed sequence, flow, or state transition; animated output must retain complete static and reduced-motion meaning.
