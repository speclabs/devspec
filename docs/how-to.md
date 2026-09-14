# How to use devspec

This guide uses real developer situations to show which agent command to run, when to run it, and what happens next. Install the framework by either setup route, then invoke the listed `devspec.*` command from your configured agent host. The CLI is one route, not a prerequisite.

Git-tracked `devspec/` artifacts are the project record. Do not skip a command because the answer is present in chat: record the evidence or decision in the matching artifact.

> Commands validate their entry state. If a command says the work is blocked, use `devspec.clarify`; do not force the next route.

## Choose the scaffold and confirm source scope

The `devspec/` scaffold may live in the code repository or in a separate Git repository that records a multi-repository change. The directory open in the agent host is the scaffold location, not automatic permission to inspect source. Before every `devspec.*` command, confirm single-repository or multi-repository scope when current evidence is absent. The agent collects each repository path, then asks one access-requirement question per repository, as `devspec/protocols/repo-access.xml` defines. A new repository may explicitly confirm that no source exists yet. Current canonical evidence may replace a repeated confirmation only when it records the same facts.

Use the [beginner command examples](command-examples.md) to choose a scaffold layout, confirm one or more repository boundaries, and copy a safe first prompt for every command.

For provider-backed story intake, pass one GitHub, Azure DevOps, Jira, GitLab, or other provider work-item URL or identifier to `/devspec.story` only when an authenticated MCP connector is available. Intake reads the item, shows a summary, and asks for explicit structured confirmation before creating the work item; it never writes back to the provider. See [MCP provider intake](command-examples.md#intake-from-mcp-providers).

## Choose the first command

| Developer situation | Run | Then |
|---|---|---|
| `devspec/foundation/repository-state.md` says `existing` | `devspec.extract` | Start a work item after the baseline is ready. |
| `devspec/foundation/repository-state.md` says `new` | `devspec.projectcontext` | Continue the new-foundation route. |
| New feature, API contract, migration, security change, or multiple concerns | `devspec.story` | Refine, then finalize, plan, implement, and review. |
| One local, low-risk correction | `devspec.quickfix` | Complete directly, clarify a blocker, or route to a story. |
| A recorded material decision blocks current work | `devspec.clarify` | Resume the exact saved command. |
| A related requirement arrives after finalization | `devspec.changerequest` | Refine and re-finalize the new scope revision. |
| One evidence-backed architecture or workflow visual is needed | `devspec.diagram` | Return to the caller's workflow, or clarify an evidence blocker. |
| A known foundation artifact needs a narrow update | Its matching foundation command | Return to the caller, or clarify an evidence blocker. |

## Continue current work without an ID

Say `continue` or run the next work-item command without an ID. devspec resolves private per-worktree context, reads the selected `meta.md` next action, and resumes only that action. If context is missing or multiple active stories exist, it asks you to select one; use an ID only to switch stories explicitly.

## 1. Map an existing service before changing it

**Scenario.** You inherit an orders API and need to add an export, but its integrations, conventions, and security controls are not documented.

1. Initialize the repository as `existing` if it is not initialized yet.

```powershell
uvx devspec init --target . --profile all --repo-state existing
uvx devspec doctor --target . --profile all
```

2. Confirm source scope: enter the repository path, then choose one of the six named access requirements. For ordinary delivery work that is `edit-and-test`; a repository you only read as evidence is `reference-only`. The [beginner command examples](command-examples.md#confirm-repository-scope-before-every-command) walk through both questions.
3. In your agent host, run a scoped request such as `/devspec.extract Source scope confirmed: orders API at D:\Code\orders-api (primary, `edit-and-test`).`
4. It inspects only the confirmed source, tests, configuration, and documentation, then creates the evidence-backed foundation and prepares a list of applicable diagrams.
5. At extraction closure, it shows the list and asks: **“Do you want me to generate all the possible diagrams?”** Choose **Yes** to generate every listed diagram, **No** to leave the list prepared, or enter selected IDs or subjects. For example, enter `DIA-001, DIA-004` to generate only those two.
6. Any prepared diagram can be generated later with `/devspec.diagram <DIA-ID-or-subject>`, for example `/devspec.diagram DIA-002`. Static SVG is the default. Use `/devspec.diagram DIA-002 motion=explain` only when the confirmed sequence, flow, or state transition benefits from explanatory motion.
7. If material evidence or source scope is unavailable, answer the recorded question through `/devspec.clarify`. Otherwise, begin the requested change with `/devspec.story Add customer export`.

**What to expect.** `extract` is the existing-system baseline command. It prepares diagrams before generating them, so a developer can keep the list only, generate all, choose a subset, or later run `/devspec.diagram DIA-002` for one queued diagram. Do not rerun individual foundation commands just to recreate its baseline.

### Add explanatory motion to a diagram

1. Select one queued ID or provide one evidence-backed subject.
2. Run `/devspec.diagram DIA-002 motion=explain`. A plain request for an animated diagram selects the same mode; `motion=none` is the default.
3. Request `format=html` separately only when an HTML presentation shell is also needed. The inline SVG keeps the same animation and reduced-motion behavior.
4. Check the queue records `svg; motion=explain`, then open the completed output from the architecture overview.

**What to expect.** The SVG reveals only the confirmed order or transition, runs once, and finishes with the complete diagram visible. Labels, arrows, and state distinctions remain meaningful without animation. A reduced-motion preference disables the animation and shows the complete final frame immediately.

- Next command when ready: `/devspec.story <request>`.

## 2. Establish a new repository before the first feature

**Scenario.** Your team has created an empty service repository and wants a durable engineering baseline before accepting feature work.

1. Initialize it with `--repo-state new`.
2. Confirm the repository scope before the first command, for example: `Scope confirmed: scaffold and planned source at D:\Code\inventory; no source exists yet; `edit-and-test`.`
3. Run these agent commands in order:

```text
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

4. Use `/devspec.coding-standards` to add a team-defined standard at any time as a targeted update. Include a concise example that future implementations should follow; the artifact distinguishes it from an observed source convention.
5. Use `/devspec.diagram <subject>` only when a specific evidence-backed visual is needed during this route. Add `motion=explain` only for a confirmed sequence, flow, or state transition; otherwise keep the static default.

**What to expect.** Each command records its artifact and advances to the next command, or records an evidence blocker and routes to `/devspec.clarify`. After `devspec.rules`, the foundation is ready for `/devspec.story`.

## 3. Deliver a feature from request to accepted review

**Scenario.** Product asks for a customer-export API with authorization, audit evidence, and automated validation.

1. Start one work item: `/devspec.story Add customer export API with authorization`.
2. Run `/devspec.refine`. Every work item goes through it after intake: intake records only what the source supplied, lists the rest as open requirement gaps, and never reads the code. When the source was already complete, refinement records the affected areas and closes without questions.
3. Run `/devspec.finalize`. It asks its own security, compliance, and delivery questions in the same run. If it finds an open or new requirement gap, it returns the work item to `/devspec.refine` without recording a blocker; run `/devspec.refine` again. After finalization reports `ready`, run the delivery route:

```text
/devspec.tasks
/devspec.implement
/devspec.review
```

4. Follow the review outcome exactly:

   - `accepted`: the work item is complete; no next command is required.
   - `rework-required`: run `/devspec.implement`. Review has already set the tasks its findings name back to `rework`; the rest stay complete.
   - `blocked`: run `/devspec.clarify`, then resume the saved command.

**What to expect.** Finalization, tasks, implementation, and review are stamped with the same scope revision. Review checks the recorded changed-work baseline and the validation evidence, not just the code diff.

## 4. Work across an API and a web application repository

**Scenario.** A checkout-flow change needs an API in `D:\Code\orders-api` and a web application in `D:\Code\orders-web`.

1. Choose one Git-tracked scaffold location for the change record: either the primary code repository or a dedicated devspec repository. Keep the work-item artifacts in that one location.
2. Initialize the scaffold location with the appropriate profile and repository state. When it is a dedicated scaffold repository, open that directory in the agent host; do not assume it grants access to the code repositories.
3. Start the story from the primary repository and state the repository roles, local paths, and read, edit, and validation permissions in the request. For example:

```text
/devspec.story Add checkout address validation. Primary: orders-api at D:\Code\orders-api (`edit-and-test`). Dependent UI: orders-web at D:\Code\orders-web (`edit-and-test`).
```

4. When a command needs the second repository, it uses the `repo-access` protocol before reading, editing, or validating it. Record a repository as reference-only or validation-only when that is its real boundary.
5. Run `/devspec.extract` instead of the individual foundation commands when you need an evidence-backed baseline for an explicitly scoped multi-repository existing system.

**What to expect.** There is no separate multi-repository configuration command. The approved roles, paths, and access permissions are the configuration, recorded in canonical devspec artifacts. Never infer access from a path. Honor exactly the recorded requirement: never inspect a `release-coordination` or `unavailable` repository; never edit a `reference-only`, `validation-only`, `release-coordination`, or `unavailable` one; and never validate a `reference-only`, `edit`, `release-coordination`, or `unavailable` one. `devspec/protocols/repo-access.xml` is the authority.

- Next command for a new change: `/devspec.story <one request with repository scope>`.

## 5. Handle the common exceptions

### Correct one low-risk UI defect

**Scenario.** The Orders page has an incorrect empty-state label and no contract, data, security, or cross-cutting behavior changes are involved.

1. Run `/devspec.quickfix Fix Orders empty-state text` and select `UI` as the primary scope.
2. Record the changed area and focused validation in the generated quickfix record.

**What to expect.** A quickfix completes directly only when the risk stays local. If investigation exposes authentication, a public API, a migration, unresolved risk, or unrelated work, it routes to `/devspec.story` without editing code.

### Add a related requirement after implementation started

**Scenario.** After export implementation begins, product asks for a new JSON format in the same feature.

1. Run `/devspec.changerequest Add JSON export`.
2. Follow the route back through `/devspec.refine`, `/devspec.finalize`, `/devspec.tasks`, implementation, and review.

**What to expect.** This is the post-finalization route: the command increments `scope_revision`, retains previous records as superseded history, and prevents implementation against stale tasks.

### Resolve a material question without guessing

**Scenario.** Finalization asked for the required data-retention period, and no one can confirm it yet, so the work item is blocked.

1. Run `/devspec.clarify` and answer the one recorded decision.

**What to expect.** Clarification resumes the exact saved stage and next command. It does not add new scope or bypass a required review.
