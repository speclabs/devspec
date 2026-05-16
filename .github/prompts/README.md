# Devspec Prompt Workflow

This document defines the proposed end-to-end prompt workflow for project development.

## Workflow Shape

Use the prompts in this order:

1. `devspec.extract.prompt.md`
2. `devspec.projectcontext.prompt.md`
3. `devspec.techstack.prompt.md`
4. `devspec.codebase-structure.prompt.md`
5. `devspec.coding-standards.prompt.md`
6. `devspec.rules.prompt.md`
7. `devspec.story.prompt.md`
8. `devspec.clarify.prompt.md`
9. `devspec.finalize.prompt.md`
10. `devspec.tasks.prompt.md`
11. `devspec.implement.prompt.md`
12. `devspec.review.prompt.md`

The extract prompt is the repo-ingestion entry point for backfilling existing projects. The next five prompts define stable project context. The last six prompts process one work item inside that context.

## Prompt Groups

### Foundation Prompts

These are project-level prompts and should be created or refreshed when the project changes.

| Prompt | Purpose | Output |
| --- | --- | --- |
| `extract` | Extract candidate constitution, architecture, and foundation content from supported repositories or local paths. | Evidence-backed project draft |
| `projectcontext` | Define business goals, users, domain terms, constraints, and success measures. | Project brief |
| `techstack` | Record languages, frameworks, services, tooling, hosting, and delivery constraints. | Stack matrix |
| `codebase-structure` | Define repository layout, module boundaries, and ownership seams for implementation placement. | Structure blueprint |
| `coding-standards` | Define preferred implementation practices, testing expectations, and quality rules. | Engineering standards |
| `rules` | Define non-negotiable constraints, forbidden choices, governance, and release gates. | Hard ruleset |

### Execution Prompts

These are work-item-level prompts and should run for each story, issue, bug, task, or PBI.

| Prompt | Purpose | Output |
| --- | --- | --- |
| `story` | Normalize an external work item into an internal development story. | Draft story |
| `clarify` | Resolve blocking ambiguity only. | Clarified story |
| `finalize` | Freeze the implementation-ready contract for the work item. | Final story brief |
| `tasks` | Decompose a finalized story into ordered implementation work. | Execution task plan |
| `implement` | Execute the approved work against the finalized brief. | Change summary and validation evidence |
| `review` | Review implemented work for defects, scope drift, and validation gaps. | Review findings and approval status |

## Shared Contract

Every prompt should produce predictable sections so the next prompt can consume the result without reinterpreting freeform chat.

Every prompt should also accept user input.

Use this input policy across the workflow:

- Foundation prompts must require user input.
- Execution prompts must accept user input.
- `story` must require user input.
- `clarify`, `finalize`, `tasks`, `implement`, and `review` may accept optional user input for adjustments, constraints, reviewer notes, or operator guidance.
- Optional user input after `story` is additive only. It may add guidance or context, but it must not silently override approved scope or prior decisions.
- If optional user input changes scope or invalidates an approved brief, send the workflow back to the appropriate earlier stage instead of mutating the current stage in place.
- Resolve missing information by asking exactly one clarification or confirmation question at a time with clickable options whenever reasonable, plus `Custom Answer`, one recommended option, and a short justification.
- Wait for the user's answer before asking the next question.
- Only record unresolved blockers when the user declines to answer or the evidence remains unavailable.
- Every prompt response should end with a recommended next step or prompt to run so users can follow the workflow without guessing.
- Each prompt file should expose that input through frontmatter and prompt-body placeholders such as `argument-hint` and `${input:...}`.

Use this closing pattern consistently:

```markdown
Recommended next step or prompt to run
- `devspec.<next-stage>.prompt.md` because {short justification}
```

Use this common structure where applicable:

```markdown
# Title
## Metadata
## Context
## Assumptions
## Constraints
## Dependencies
## Decisions
## Acceptance Criteria
## Risks
## Blockers
## Next Step
```

Not every prompt needs every section, but section names should stay stable across prompts.

## Prompt Contracts

### `devspec.extract.prompt.md`

**Goal**
Backfill devspec artifacts from one or more existing repositories.

**Inputs**
- Required user input
- One or more GitHub, Azure DevOps, or GitLab repository URLs
- Or one or more local repository folder paths
- Optional branch, tag, or commit guidance when the default branch is not correct

**Must produce**
- Source validation results
- Evidence-backed candidate updates for constitution, architecture, and foundation artifacts
- Clear separation between observed facts, high-confidence inference, and unresolved blockers only when they cannot be resolved during questioning
- Explicit confirmation step before constitution changes are written
- Updated architecture and foundation files when evidence is sufficient

**Rules**
- Accept repository URLs only, not issues, pull requests, merge requests, work items, wiki pages, releases, or pipelines.
- Reject unsupported providers.
- Preserve human-authored content when updating existing artifacts.
- Do not synthesize ADRs without explicit user direction and strong evidence.
- Treat principle-level content as confirm-before-write.
- End with a recommended next step or prompt to run, usually `devspec.projectcontext.prompt.md` after extraction succeeds.

**Handoff**
Feeds the foundation prompts and can reduce the manual input needed for them.

**User input**
Mandatory.

### `devspec.projectcontext.prompt.md`

**Goal**
Create the canonical project brief.

**Inputs**
- Required user input
- Product vision
- Problem domain
- User types
- Business goals
- Delivery constraints

**Must produce**
- Project summary
- Primary users and stakeholders
- Core domain vocabulary
- Business goals and non-goals
- Success metrics
- High-level constraints

**Handoff**
Used by all later prompts.

**Recommended next prompt**
`devspec.techstack.prompt.md`

**User input**
Mandatory.

### `devspec.techstack.prompt.md`

**Goal**
Capture the actual technology and delivery environment.

**Inputs**
- Required user input
- Existing repository or platform details
- Runtime and deployment targets
- Tooling preferences

**Must produce**
- One heading per project or repo
- Tech stack tables for languages and runtimes, frameworks and libraries, services and infrastructure, tooling, and hosting or delivery constraints
- Versions used in the project
- Current market versions when available
- CI/CD and hosting model
- Local development and testing tools
- Operational constraints

**Handoff**
Constrains architecture and implementation choices.

**Recommended next prompt**
`devspec.codebase-structure.prompt.md`

**User input**
Mandatory.

### `devspec.codebase-structure.prompt.md`

**Goal**
Define how the codebase is organized.

**Inputs**
- Required user input
- Project context
- Tech stack
- Existing repository structure if present

**Must produce**
- One tree node repository layout per repo under a dedicated repo heading
- Service or module boundaries
- Naming conventions
- Ownership seams
- Integration boundaries
- Cross-cutting concerns placement

**Handoff**
Used by `story`, `finalize`, and `implement` to place changes correctly.

**Recommended next prompt**
`devspec.coding-standards.prompt.md`

**User input**
Mandatory.

### `devspec.coding-standards.prompt.md`

**Goal**
Define preferred engineering practices.

**Inputs**
- Required user input
- Tech stack
- Team standards
- Existing code patterns

**Must produce**
- Style and naming expectations
- Testing expectations
- Error handling patterns
- Logging and observability expectations
- Documentation expectations
- Code review expectations

**Handoff**
Guides code quality during `finalize` and `implement`.

**Recommended next prompt**
`devspec.rules.prompt.md`

**User input**
Mandatory.

### `devspec.rules.prompt.md`

**Goal**
Define hard constraints that cannot be violated.

**Inputs**
- Required user input
- Security requirements
- Compliance rules
- Platform restrictions
- Organizational guardrails

**Must produce**
- Required controls
- Forbidden libraries or patterns
- Data handling requirements
- Performance or reliability floors
- Release or approval gates

**Handoff**
Applied as a hard filter to every work item and implementation plan.

**Recommended next prompt**
`devspec.story.prompt.md`

**User input**
Mandatory.

### `devspec.story.prompt.md`

**Goal**
Turn a work tracking reference into a normalized internal story.

**Inputs**
- Required user input
- Story number, Jira number, bug number, issue number, task number, or PBI number
- Or a full GitHub, Azure DevOps, or Jira URL
- Work-item type classification when it can be inferred or clarified

**Must produce**
- Source system and source reference
- Canonical source link when available
- Source resolution status and provider details
- Resolved item confirmation status
- Resolved summary shown to the user
- Work-item type and type-appropriate urgency, using priority for features and severity for bugs or security vulnerabilities
- Multi-repo dependency status for features and the related repos when applicable
- Problem summary
- Intended user outcome
- Impact summary and affected scope
- In-scope and out-of-scope items
- Draft acceptance criteria
- Bug reproduction details when the item is a bug
- Security impact details when the item is a security vulnerability
- Known dependencies and risks
- Unresolved blockers after questioning and confirmation attempts

**Rules**
- Do not guess the source system for ambiguous bare numbers.
- Validate the input against supported provider formats before treating it as resolved.
- If the input cannot be resolved confidently, ask for clarification.
- If the input format is invalid, fail fast and ask the user to correct it or choose manual intake.
- If provider lookup is unavailable or resolution fails, record the outcome and offer manual intake only as an explicit fallback.
- If provider resolution succeeds, show at least provider, identifier, title, type when available, current external status when available, canonical link, and a short summary, then require explicit user confirmation before creating or updating the work item.
- Offer only these confirmation actions after successful resolution: confirm and continue, reject and retry input, switch to manual intake, or cancel.
- Manual intake requires a user-provided external reference, manual description, and manual acceptance criteria.
- If the work-item type is unclear, ask for clarification instead of assuming feature, bug, or security-vulnerability.
- Bugs should capture expected behavior, actual behavior, reproduction steps, regression context, and user impact.
- Features should capture priority instead of severity.
- Features should confirm whether the work has multi-repo dependencies.
- If a feature depends on multiple repos, capture all related repos in the story artifacts.
- Security vulnerabilities should capture severity, affected scope, attack surface, exploitability, disclosure status, and containment or remediation notes.
- Minimize sensitive exploit detail in shared artifacts unless it is necessary for remediation.
- Normalize the work item into a consistent internal story format.

**Handoff**
Feeds `clarify`.

**Recommended next prompt**
`devspec.clarify.prompt.md`

**User input**
Mandatory.

### `devspec.clarify.prompt.md`

**Goal**
Ask only the minimum questions required to unblock implementation.

**Inputs**
- Optional user input
- Draft story
- Foundation prompt outputs

**Must produce**
- Blocking questions only
- Impact of each unresolved item
- Updated assumptions after answers are provided
- Revised acceptance criteria if needed

**Rules**
- Do not reopen settled project-wide decisions.
- Do not ask optional or low-value questions.
- Treat optional user input as additive guidance. If the new input changes scope, route back to `story` or `finalize` instead of rewriting the current stage silently.
- Ask exactly one blocking question at a time.
- Present the question with clickable multiple-choice options whenever reasonable.
- Include a `Custom Answer` option.
- Include one recommended option with a short justification.
- Wait for the user's selection or input before asking the next question.

**Handoff**
Feeds `finalize`.

**Recommended next prompt**
`devspec.finalize.prompt.md`

**User input**
Optional.

### `devspec.finalize.prompt.md`

**Goal**
Freeze a story into an implementation-ready brief.

**Inputs**
- Optional user input
- Clarified story
- Foundation prompt outputs

**Must produce**
- Work-item type and severity or priority as applicable
- Final scope
- Confirmed acceptance criteria
- Assumptions
- Dependencies
- Risks and mitigations
- Validation approach
- Type-specific readiness gates
- Release, backport, or advisory needs when applicable
- Ready status: `ready` or `not ready`

**Rules**
- If blocking ambiguity remains, mark the brief as `not ready`.
- Do not silently invent missing requirements.
- Bugs are not ready if reproducible behavior, user impact, or regression expectations remain unclear.
- Security vulnerabilities are not ready if severity, affected scope, containment or remediation plan, or validation and backport expectations are missing.
- Treat optional user input as additive only. If it changes approved scope or decisions, move back to `clarify` before producing a new finalized brief.

**Handoff**
Feeds `tasks`.

**Recommended next prompt**
`devspec.tasks.prompt.md`

**User input**
Optional.

### `devspec.tasks.prompt.md`

**Goal**
Break a finalized story into ordered implementation tasks without changing scope.

**Inputs**
- Optional user input
- Final story brief with `ready` status
- Foundation prompt outputs
- Current codebase structure

**Must produce**
- Ordered task list
- Task dependencies
- Components, modules, or files likely to change
- Validation step for each task or task group
- Bug reproduction and regression tasks when applicable
- Security verification, backport, or disclosure tasks when applicable
- Definition of done for the implementation effort

**Rules**
- Do not change or expand the finalized scope.
- Do not invent new requirements.
- If execution blockers remain, surface them explicitly.
- Keep tasks implementation-oriented and small enough to execute or review.
- Bugs should usually include reproduce, fix, and regression-validation tasks.
- Security vulnerabilities should usually include impact confirmation, remediation, verification across affected supported versions, and backport, release, or advisory tasks when applicable.
- Treat optional user input as additive guidance only. Do not use it to redefine the finalized brief.

**Handoff**
Feeds `implement`.

**Recommended next prompt**
`devspec.implement.prompt.md`

**User input**
Optional.

### `devspec.implement.prompt.md`

**Goal**
Implement one approved task at a time for the current work item according to the finalized brief.

**Inputs**
- Optional user input
- Final story brief with `ready` status
- Execution task plan when available
- Foundation prompt outputs
- Current repository state

**Must produce**
- Direct code changes for the single task executed in the current run
- Task implemented in the current run
- Task execution log entry in `implement.md`
- Next-task handoff
- Type-specific handling notes when the work item is a bug or security vulnerability
- Files likely to change
- Validation steps
- Completion summary
- Residual risks or follow-up work

**Rules**
- Respect codebase structure, coding standards, and hard rules.
- Do not widen scope beyond the finalized brief.
- Follow the execution task plan one task at a time unless a blocker requires deviation.
- Select the next pending task using `tasks.md` and any prior handoff recorded in `implement.md`.
- If no pending task remains, notify the user that all planned tasks are already implemented and record that completed state in `implement.md`.
- Record each implementation pass as a dated task-level log entry in `implement.md`.
- After each task, leave a clear handoff for the next task instead of silently continuing through the task list.
- For bugs, confirm regression validation as part of implementation evidence.
- For security vulnerabilities, avoid exposing sensitive exploit detail unnecessarily and record remediation, verification, and backport or advisory status when applicable.
- Report validation evidence, not just intent.
- Treat optional user input as additive guidance only. If it changes scope, send the work back to `finalize` or `tasks` rather than overriding the current brief.

**Handoff**
Feeds `review`.

**Recommended next prompt**
`devspec.review.prompt.md`

**User input**
Optional.

### `devspec.review.prompt.md`

**Goal**
Review the implemented work item against the finalized brief and record approval or required changes.

**Inputs**
- Optional user input
- Final story brief with `ready` status
- Execution task plan when available
- Implementation log and changed code
- Foundation prompt outputs

**Must produce**
- Review status: `approved`, `approved-with-follow-ups`, or `changes-requested`
- Findings ordered by severity
- Scope compliance assessment
- Validation gaps
- Type-specific review notes when the work item is a bug or security vulnerability
- Next step or handoff

**Rules**
- Review should focus on bugs, regressions, security risks, validation gaps, missing tests, and scope drift.
- Do not silently reopen planning or rewrite the finalized brief during review.
- Bugs with meaningful regression risk should receive review before closure.
- Security vulnerabilities must receive review before closure.
- If blocking findings exist, mark the review as `changes-requested` and route the work back to `implement`.
- Treat optional user input as additive guidance only. If it changes scope, route back to `finalize` instead of mutating the review stage.

**Handoff**
Feeds `implement` when changes are required, or delivery when approved.

**Recommended next prompt**
`devspec.implement.prompt.md` when changes are requested, otherwise stop the workflow or hand off to delivery.

**User input**
Optional.

## Design Recommendations

- Keep prompt descriptions explicit about when to use each prompt. Discovery in chat depends heavily on the `description` field.
- Keep foundation prompts reusable and project-wide. They should not mention a specific work item.
- Keep execution prompts narrow. Each should solve one stage of work-item processing.
- Keep `tasks` separate from `implement` for medium and large work items. Planning and execution are different activities and benefit from an explicit handoff.
- Keep `review` separate from `implement`. Execution and review are different responsibilities and should leave separate artifacts.
- Make user input handling explicit in every prompt. Foundation prompts should refuse to proceed without required user input, while execution prompts after `story` should treat user input as additive rather than required.
- Favor stable headings over creative formatting. Prompt chaining works better when downstream prompts can rely on exact section names.
- Require `story` and `finalize` to fail safely when inputs are incomplete or ambiguous. This prevents low-quality implementation work from starting.

## Cross-Agent Repository Layout

If the repository needs to support multiple agent ecosystems, use a canonical-devspec-plus-adapters model.

- Shared devspec artifacts are the source of truth.
- Agent-specific files are adapters that point to the shared devspec artifacts instead of duplicating them.
- Each work item keeps its own decision log so later stages can trace why something changed.

Use a refined version of the proposed structure:

```text
repo/
|-- README.md                         # Human-readable repo entry point
|-- AGENTS.md                         # Generic agent adapter entry point
|-- CLAUDE.md                         # Claude-specific adapter file
|-- GEMINI.md                         # Gemini-specific adapter file
|-- .github/
|   `-- copilot-instructions.md       # Copilot-specific adapter file
|-- .cursor/
|   `-- rules/
|       `-- project.mdc               # Cursor adapter rules, keep thin
|-- .windsurfrules                    # Windsurf adapter rules, keep thin
|
|-- devspec/
|   |-- constitution.md               # Project principles and non-negotiable engineering guardrails
|   |-- foundation/
|   |   |-- project-context.md        # Output of the projectcontext stage
|   |   |-- tech-stack.md             # Output of the techstack stage
|   |   |-- codebase-structure.md     # Repo and module structure for implementation placement
|   |   |-- coding-standards.md       # Output of the coding-standards stage
|   |   |-- provider-integrations.md  # Provider input formats, MCP integration guidance, and resolution policy
|   |   `-- rules.md                  # Project-operational hard constraints and delivery gates
|   |-- architecture/
|   |   |-- overview.md               # Broader system architecture beyond repo layout
|   |   |-- decisions/
|   |   |   `-- ADR-0001-example.md   # Long-lived architecture decisions
|   |   `-- diagrams/                 # Optional diagrams and visuals
|   |-- work-items/
|   |   |-- _template/
|   |   |   |-- meta.md               # Source reference, owner, status, dates, and related links
|   |   |   |-- story.md              # Output of the story stage
|   |   |   |-- clarify.md            # Output of the clarify stage
|   |   |   |-- finalize.md           # Output of the finalize stage
|   |   |   |-- tasks.md              # Output of the tasks stage
|   |   |   |-- implement.md          # Output of the implement stage
|   |   |   |-- review.md             # Output of the review stage
|   |   |   |-- decisions.md          # Work-item-level decisions and rationale
|   |   |   `-- notes.md              # Optional supporting notes
|   |   `-- <feature-name>/
|   |       |-- meta.md               # Work item metadata, source reference, and related links
|   |       |-- story.md              # Story-normalized work item
|   |       |-- clarify.md            # Clarifications and answers
|   |       |-- finalize.md           # Implementation-ready brief
|   |       |-- tasks.md              # Task breakdown used by implement stage
|   |       |-- implement.md          # Implementation outcome and validation summary
|   |       |-- review.md             # Review findings and approval status
|   |       |-- decisions.md          # Local decision history for this work item
|   |       `-- notes.md              # Optional scratchpad or review notes
|   `-- glossary.md                   # Shared domain vocabulary when needed
|
|-- src/
|-- tests/
|-- scripts/
`-- package.json / pyproject.toml / pom.xml / etc.
```

Sub-folders intentionally removed from the recommended baseline:

- `.cursor/rules/testing.mdc` because testing guidance should stay canonical in `devspec/foundation/coding-standards.md` unless Cursor truly needs a separate adapter.
- `.specify/` because it is only useful if that toolchain is actively used; otherwise it becomes dead structure.
- `.kiro/` because it duplicates project context, tech, and structure guidance that already belongs in canonical devspec artifacts.

Add those folders only when the corresponding agent or tool is actually adopted.

### Canonical Versus Adapter Files

Treat these as canonical project artifacts:

- `devspec/constitution.md`
- `devspec/foundation/*`
- `devspec/architecture/*`
- `devspec/work-items/*`
- `devspec/glossary.md`

Treat these as agent adapters:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/*`
- `.windsurfrules`

Adapter files should be thin. They should tell each agent how to use the canonical devspec artifacts instead of restating the same rules in multiple places.

### Decision Tracking Model

Use two levels of decision storage:

- Project-wide principles and policy decisions in `devspec/constitution.md`.
- Architecture decisions in `devspec/architecture/decisions/` as ADRs.
- Feature or work-item decisions in `devspec/work-items/<feature-name>/decisions.md`.

This split keeps durable cross-project decisions separate from local delivery decisions.

### Constitution

Keep a single `devspec/constitution.md` file for the project's durable principles.

Use it for:

- engineering principles
- delivery guardrails
- testing expectations
- security and compliance defaults
- rules that apply across all features and all agents

Do not repeat the same content in agent adapter files. Agent-specific files should point back to `devspec/constitution.md`.

Keep the split explicit:

- `devspec/constitution.md` holds enduring principles that rarely change.
- `devspec/foundation/rules.md` holds project-operational hard constraints, governance rules, and delivery gates that may evolve over time.

### Structure Versus Architecture

Keep the split explicit:

- `devspec/foundation/codebase-structure.md` defines repository layout, module boundaries, ownership seams, and implementation placement.
- `devspec/architecture/overview.md` defines the broader system view, major components, integration boundaries, and shared diagrams.

### Provider Integrations

Keep provider access guidance in `devspec/foundation/provider-integrations.md`.

- The `story` stage should stay provider-agnostic.
- Provider-specific resolution should happen through MCP servers or equivalent integration tools.
- The workflow should prefer exact URLs first, provider-qualified identifiers second, and ambiguous identifiers only after clarification.
- Invalid input should fail fast.
- Missing or unavailable provider integration should offer manual intake explicitly instead of guessing.
- Successful provider resolution should still require explicit user confirmation after showing the resolved details.
- The resolved confirmation view should at minimum show provider, identifier, title, type when available, current external status when available, canonical link, and a short summary.
- The confirmation step should allow only confirm and continue, reject and retry input, switch to manual intake, or cancel.
- Manual fallback should require an external reference, description, and acceptance criteria before intake can proceed.

### Spec Folder Naming

Keep folder names simple and developer-friendly:

- `user-export`
- `login-flow`
- `payment-timeout`

Do not overload the folder name with tracker ids or system names unless the team truly needs that in the path.

Create the work-item folder at the `story` stage and do not rename it later. If the story title evolves, keep the refined title inside `story.md` and `meta.md` instead of changing the folder path.

Keep external references inside `meta.md`, for example:

- GitHub issue number or URL
- Azure DevOps work item id or URL
- Jira issue key or URL
- Owner, status, and timestamps

`meta.md` should at minimum include:

- source reference
- source resolution status
- source confirmation status
- owner
- status
- review status
- created date
- updated date
- related links

### Simple Naming Recommendations

If the goal is ease of use for developers and alignment with the devspec workflow, prefer these names:

- `project-context.md` for project-wide context
- `tech-stack.md` for stack constraints and choices
- `codebase-structure.md` for codebase layout and boundaries
- `coding-standards.md` for engineering expectations
- `provider-integrations.md` for provider input formats and MCP integration guidance
- `rules.md` for hard constraints
- `story.md` for work-item intake
- `clarify.md` for follow-up questions and answers
- `finalize.md` for the implementation-ready brief
- `tasks.md` for implementation work
- `implement.md` for implementation outcome and validation summary
- `review.md` for review findings and approval status
- `decisions.md` for decision history
- `notes.md` for optional scratch notes
- `meta.md` for lightweight metadata and external references

This keeps file names short, stage-aligned, and easy to scan in editors and pull requests.

### Why This Layout Works

- It supports multiple agent ecosystems without making any one agent the source of truth.
- It gives the project one clear constitutional source for principles that all prompts, specs, and agents can follow.
- It keeps prompt outcomes and work-item artifacts durable and diffable in Git.
- It gives each work item a local history of story intake, clarifications, finalization, tasks, implementation, review, and decisions.
- It lets agent-specific instruction files stay small and easier to maintain.

## Recommended Next Step

Run the workflow on one sample feature, one bug, and one security-vulnerability work item to validate the new typed intake, one-task-at-a-time implementation, and review-stage handoff behavior before broader adoption.