# Devspec Prompt Workflow

This document defines the proposed end-to-end prompt workflow for project development.

## Workflow Shape

Use the prompts in this order:

1. `devspec.projectcontext.prompt.md`
2. `devspec.techstack.prompt.md`
3. `devspec.solution-structure.prompt.md`
4. `devspec.coding-standards.prompt.md`
5. `devspec.rules.prompt.md`
6. `devspec.story.prompt.md`
7. `devspec.clarify.prompt.md`
8. `devspec.finalize.prompt.md`
9. `devspec.tasks.prompt.md`
10. `devspec.implement.prompt.md`

The first five prompts define stable project context. The last four prompts process one work item inside that context.

## Prompt Groups

### Foundation Prompts

These are project-level prompts and should be created or refreshed when the project changes.

| Prompt | Purpose | Output |
| --- | --- | --- |
| `projectcontext` | Define business goals, users, domain terms, constraints, and success measures. | Project brief |
| `techstack` | Record languages, frameworks, services, tooling, hosting, and delivery constraints. | Stack matrix |
| `solution-structure` | Define architecture, repository layout, module boundaries, and ownership seams. | Structure blueprint |
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

## Shared Contract

Every prompt should produce predictable sections so the next prompt can consume the result without reinterpreting freeform chat.

Every prompt should also accept user input.

Use this input policy across the workflow:

- Foundation prompts must require user input.
- Execution prompts must accept user input.
- `story` must require user input.
- `clarify`, `finalize`, `tasks`, and `implement` may accept optional user input for adjustments, constraints, reviewer notes, or operator guidance.
- Each prompt file should expose that input through frontmatter and prompt-body placeholders such as `argument-hint` and `${input:...}`.

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
## Open Questions
## Next Step
```

Not every prompt needs every section, but section names should stay stable across prompts.

## Prompt Contracts

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
- Languages and versions
- Frameworks and libraries
- Data stores and messaging
- CI/CD and hosting model
- Local development and testing tools
- Operational constraints

**Handoff**
Constrains architecture and implementation choices.

**User input**
Mandatory.

### `devspec.solution-structure.prompt.md`

**Goal**
Define how the solution is organized.

**Inputs**
- Required user input
- Project context
- Tech stack
- Existing repository structure if present

**Must produce**
- Top-level repository layout
- Service or module boundaries
- Naming conventions
- Ownership seams
- Integration boundaries
- Cross-cutting concerns placement

**Handoff**
Used by `story`, `finalize`, and `implement` to place changes correctly.

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

**User input**
Mandatory.

### `devspec.story.prompt.md`

**Goal**
Turn a work tracking reference into a normalized internal story.

**Inputs**
- Required user input
- Story number, Jira number, bug number, issue number, task number, or PBI number
- Or a full GitHub, Azure DevOps, or Jira URL

**Must produce**
- Source system and source reference
- Canonical source link when available
- Problem summary
- Intended user outcome
- In-scope and out-of-scope items
- Draft acceptance criteria
- Known dependencies and risks
- Open questions blocking implementation

**Rules**
- Do not guess the source system for ambiguous bare numbers.
- If the input cannot be resolved confidently, ask for clarification.
- Normalize the work item into a consistent internal story format.

**Handoff**
Feeds `clarify`.

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

**Handoff**
Feeds `finalize`.

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
- Final scope
- Confirmed acceptance criteria
- Assumptions
- Dependencies
- Risks and mitigations
- Validation approach
- Ready status: `ready` or `not ready`

**Rules**
- If blocking ambiguity remains, mark the brief as `not ready`.
- Do not silently invent missing requirements.

**Handoff**
Feeds `tasks`.

**User input**
Optional.

### `devspec.tasks.prompt.md`

**Goal**
Break a finalized story into ordered implementation tasks without changing scope.

**Inputs**
- Optional user input
- Final story brief with `ready` status
- Foundation prompt outputs
- Current solution structure

**Must produce**
- Ordered task list
- Task dependencies
- Components, modules, or files likely to change
- Validation step for each task or task group
- Definition of done for the implementation effort

**Rules**
- Do not change or expand the finalized scope.
- Do not invent new requirements.
- If execution blockers remain, surface them explicitly.
- Keep tasks implementation-oriented and small enough to execute or review.

**Handoff**
Feeds `implement`.

**User input**
Optional.

### `devspec.implement.prompt.md`

**Goal**
Implement the approved work item according to the finalized brief.

**Inputs**
- Optional user input
- Final story brief with `ready` status
- Execution task plan when available
- Foundation prompt outputs
- Current repository state

**Must produce**
- Implementation plan or direct code changes
- Files likely to change
- Validation steps
- Completion summary
- Residual risks or follow-up work

**Rules**
- Respect solution structure, coding standards, and hard rules.
- Do not widen scope beyond the finalized brief.
- Follow the execution task plan unless a blocker requires deviation.
- Report validation evidence, not just intent.

**Handoff**
Feeds review, testing, or delivery workflows.

**User input**
Optional.

## Design Recommendations

- Keep prompt descriptions explicit about when to use each prompt. Discovery in chat depends heavily on the `description` field.
- Keep foundation prompts reusable and project-wide. They should not mention a specific work item.
- Keep execution prompts narrow. Each should solve one stage of work-item processing.
- Keep `tasks` separate from `implement` for medium and large work items. Planning and execution are different activities and benefit from an explicit handoff.
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
|   |   |-- solution-structure.md     # Output of the solution-structure stage
|   |   |-- coding-standards.md       # Output of the coding-standards stage
|   |   `-- rules.md                  # Output of the rules stage
|   |-- architecture/
|   |   |-- overview.md               # Shared architecture summary when needed
|   |   |-- decisions/
|   |   |   `-- ADR-0001-example.md   # Long-lived architecture decisions
|   |   `-- diagrams/                 # Optional diagrams and visuals
|   |-- work-items/
|   |   |-- _template/
|   |   |   |-- meta.md               # Source id, owner, status, timestamps
|   |   |   |-- story.md              # Output of the story stage
|   |   |   |-- clarify.md            # Output of the clarify stage
|   |   |   |-- finalize.md           # Output of the finalize stage
|   |   |   |-- tasks.md              # Output of the tasks stage
|   |   |   |-- implement.md          # Output of the implement stage
|   |   |   |-- decisions.md          # Work-item-level decisions and rationale
|   |   |   `-- notes.md              # Optional supporting notes
|   |   `-- <feature-name>/
|   |       |-- meta.md               # Work item metadata and source traceability
|   |       |-- story.md              # Story-normalized work item
|   |       |-- clarify.md            # Clarifications and answers
|   |       |-- finalize.md           # Implementation-ready brief
|   |       |-- tasks.md              # Task breakdown used by implement stage
|   |       |-- implement.md          # Implementation outcome and validation summary
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

### Spec Folder Naming

Keep folder names simple and developer-friendly:

- `user-export`
- `login-flow`
- `payment-timeout`

Do not overload the folder name with tracker ids or system names unless the team truly needs that in the path.

Keep external references inside `meta.md`, for example:

- GitHub issue number or URL
- Azure DevOps work item id or URL
- Jira issue key or URL
- Owner, status, and timestamps

### Simple Naming Recommendations

If the goal is ease of use for developers and alignment with the devspec workflow, prefer these names:

- `project-context.md` for project-wide context
- `tech-stack.md` for stack constraints and choices
- `solution-structure.md` for architecture and boundaries
- `coding-standards.md` for engineering expectations
- `rules.md` for hard constraints
- `story.md` for work-item intake
- `clarify.md` for follow-up questions and answers
- `finalize.md` for the implementation-ready brief
- `tasks.md` for implementation work
- `implement.md` for implementation outcome and validation summary
- `decisions.md` for decision history
- `notes.md` for optional scratch notes
- `meta.md` for lightweight metadata and external references

This keeps file names short, stage-aligned, and easy to scan in editors and pull requests.

### Why This Layout Works

- It supports multiple agent ecosystems without making any one agent the source of truth.
- It gives the project one clear constitutional source for principles that all prompts, specs, and agents can follow.
- It keeps prompt outcomes and work-item artifacts durable and diffable in Git.
- It gives each work item a local history of story intake, clarifications, finalization, tasks, implementation, and decisions.
- It lets agent-specific instruction files stay small and easier to maintain.

## Recommended Next Step

Create the missing prompt files using this contract, align the existing `devspec.story.prompt.md` with the `story` contract above, add `devspec.tasks.prompt.md`, and decide whether the repository should adopt the cross-agent layout described above.