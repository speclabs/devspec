# Shared Prompt Patterns

Keep repeated workflow behavior here instead of duplicating it in every prompt or agent.

## Interactive Question Pattern

- Ask exactly one user question at a time.
- Before asking, follow the [Question Basis Pattern](#question-basis-pattern).
- Use a structured multiple-choice question whenever a finite decision can be offered; use free-form wording only when meaningful options cannot be provided.
- Use clickable multiple-choice options whenever the platform supports them. When clickable options are unavailable, render the same option labels as text and ask the user to reply with one label or `Custom Answer`.
- Every structured question must include question intent, prompt text, option labels, exactly one recommended option with a short reason, fallback rendering, and the recorded state required by the Question Basis Pattern.
- Always include a `Custom Answer` option for user-facing choices.
- Use stage-specific option sets only when the stage defines them in a pattern, agent, or artifact policy; otherwise use the standard option set for the question intent.
- Wait for the user's answer before asking another question.
- If several confirmations are discovered, present only the highest-priority one and defer the rest.

| Question intent | Use when | Standard options |
| --- | --- | --- |
| `clarification` | Required facts are missing or ambiguous, including provider identity, target work item, folder name, or blocked readiness facts. | Meaningful stage-specific choices plus `Custom Answer`; use free-form only when meaningful options cannot be offered. |
| `confirmation` | A resolved fact, provider item, constitution change, repository access value, generated artifact, or risky scope change needs explicit approval. | `Yes`, `No`, `Custom Answer` unless a stage-specific confirmation set is defined. |
| `selection` | The user must choose among sources, repositories, work items, diagram types, target locations, or other finite values. | The finite candidate values plus `Custom Answer`. |
| `continuation` | A workflow, queue item, task, or handoff can continue or stop at the current checkpoint. | `Proceed`, `Skip`, `Custom Answer`. |
| `resume` | A run is resuming from `stopped` or ambiguous state. | `Continue`, `Pause`, `Skip`, `Custom Answer`. |
| `approval` | Queue item generation, diagram generation, overwrite behavior, process-flow batch work, or similar gated action needs approval. | `Proceed`, `Skip`, `Custom Answer` unless the stage defines a narrower approval set. |
| `retry` | Failed lookup, failed validation, repeated implementation attempts, blocked discovery, or another retryable failure needs direction. | `Proceed`, `Skip`, `Custom Answer`, with the retry condition or changed method named in the prompt. |

Standard stage-specific option sets:

- Binary confirmations use `Yes`, `No`, and `Custom Answer`.
- Source selection for `/devspec.extract` uses `Use current project root`, `Enter repo paths`, `Cancel extraction`, and `Custom Answer`.
- Provider resolution uses `Confirm and continue`, `Reject and retry input`, `Switch to manual intake`, `Cancel`, and `Custom Answer`.
- Repository access confirmation uses the values in `devspec/glossary.md#access-requirement-values` plus `Custom Answer`.
- Workflow continuation, queue processing, task continuation, generated artifact approval, and retry decisions use `Proceed`, `Skip`, and `Custom Answer` unless a narrower stage-specific set applies.
- Resume from `stopped` or ambiguous state uses `Continue`, `Pause`, `Skip`, and `Custom Answer`.

## Question Basis Pattern

- Use this pattern to justify and record any structured user or developer question.
- Ask only when durable artifacts, configured sources, or repository evidence cannot resolve the issue and the answer would materially change intake, readiness, task planning, validation, repository access, compliance handling, delivery risk, or handoff.
- Identify the source artifact, source section, source row or ID, user input, provider evidence, repository evidence, or failed lookup that created the question.
- Name the missing, ambiguous, conflicting, or unconfirmed fact and the material impact of leaving it unresolved.
- Ask only the highest-priority unresolved question; defer lower-impact questions until the active one is answered or withdrawn.
- Use the [Interactive Question Pattern](#interactive-question-pattern) for option labels, recommended option, `Custom Answer`, and fallback rendering.
- Before waiting for the answer, record question intent, question source, blocking gap, material impact, option labels, recommended option and reason, impacted artifacts, continuation condition, and next required action in the current `Resume State`, queue row, blocker row, or clarification log, using the stage artifact fields available for that command.
- Do not ask about low-impact preferences, implementation tactics better handled by `/devspec.tasks`, or facts already captured in upstream artifacts.

## Next Action Selection Pattern

- Recommend one next step.
- Do not output multiple next prompts, command lists, or peer next-action bullets while a clarification, confirmation, queue item, handoff, retry, or fallback decision is pending.
- When several next actions are possible, pick the highest-priority unresolved action and ask one structured question using the [Interactive Question Pattern](#interactive-question-pattern).
- If no confirmation or selection is pending, provide exactly one registered slash command, handoff, file update, or structured question.
- For queues, select the next unresolved item by queue order and status unless the stage defines stricter priority.
- A final response may summarize completed work, but it must close with one next action or one structured question.

## Registered Command Recommendation Pattern

- Use `.github/prompts/README.md#registered-slash-commands` as the command registry.
- Recommend only registered slash commands; do not invent commands from workflow names, artifact names, queue names, or agent names.
- Do not recommend unregistered commands such as `/devspec.plan`, `/devspec.architecture`, `/devspec.provider-integrations`, `/devspec.queue`, or `/devspec.decisions`.
- Before recommending a slash command, verify it is registered and the matching `.github/prompts/devspec.<command>.prompt.md` file exists.
- If no registered command fits, recommend a concrete file update, configured handoff, or structured question.
- Map common workflow labels to registered commands when appropriate: planning -> `/devspec.tasks`, implementation -> `/devspec.implement`, review -> `/devspec.review`, diagram generation -> `/devspec.diagram`, and provider integration changes -> manual updates in `devspec/foundation/provider-integrations.md`.

## Prerequisite Validation Pattern

- Validate required user input and upstream artifacts before producing output.
- If a prerequisite is missing, invalid, ambiguous, or not ready, stop, explain the blocker, and direct the user to the recovery step.
- Record unresolved blockers only when the user declines to answer or evidence remains unavailable.
- Treat optional user input as additive guidance unless the stage explicitly requires it.

## Session Recovery Pattern

- Treat Git-tracked `devspec` artifacts as canonical; chat history and session memory are supporting context only.
- At the start of each applicable command, read the target artifact and durable state files, then reconcile `Resume State`.
- Use work-item folders as the orchestration boundary. Use tasks, target repositories, target areas, and attempts as checkpoints.
- For monorepos, record the target repository once and distinguish tasks by module, layer, or area. For multi-repo work, every executable task must name target repository and required access.
- Keep `Run status` values limited to the values in `devspec/glossary.md#run-status-values`.
- Use `paused` when the user expects to continue from the same task or question.
- Use `stopped` when the run intentionally ended and should ask one structured `resume` question before resuming.
- Use `blocked` only when evidence, access, or prerequisites are insufficient; record the blocker and continuation condition.
- Before any blocking question, handoff, retry-loop stop, or run end, update `Resume State` with stage, item, last completed step, resume command, and the applicable fields required by the [Question Basis Pattern](#question-basis-pattern).
- On rerun, resume a `paused` item directly when prerequisites still hold; for `stopped` or ambiguous state, ask one structured `resume` question first.
- Retry only when the recorded retry condition is met, the user gives custom direction, or the method materially changed. Do not replay recorded failed methods just because the session changed.
- When stage tasks or queue items are complete, mark the stage `complete` and hand off to the next registered command or configured agent.

## Output Closure Pattern

- Follow the [Next Action Selection Pattern](#next-action-selection-pattern).
- Follow the [Registered Command Recommendation Pattern](#registered-command-recommendation-pattern) before recommending any slash command.
- End with exactly one registered command, handoff, file update, or structured question.
- If the next step requires clarification, confirmation, selection, approval, retry direction, queue approval, resume, or continuation, ask one structured question with explicit options following the Interactive Question Pattern.
- Summarize only the artifact or work-item path updated, key outcome, blockers or open questions, and single next action.

## Extraction State Pattern

- Use this pattern for `/devspec.extract` only.
- Create or update `devspec/foundation/extraction-state.md` from `devspec/foundation/_template/extraction-state.md` when extraction starts and is not canceled.
- Use `extraction-state.md` only for the extraction queue, resume state, blockers, and confirmations.
- Keep exactly one extraction queue row `active`. Use existing task status values from `devspec/glossary.md#task-status-values`.
- Process extraction queue rows in ID order unless a blocker, confirmation, or explicit user direction changes the next action.
- Before asking a question, blocking, pausing, or handing off, update `Resume State`, the active extraction queue row, and `Blockers and Confirmations` with the applicable fields required by the [Question Basis Pattern](#question-basis-pattern).
- Do not store extracted facts in `extraction-state.md`; write them to the target artifact named by the active queue row.
- Do not store reusable discovery methods in `extraction-state.md`; use `devspec/foundation/exploration-state.md`.
- Do not store diagram queue state in `extraction-state.md`; use `devspec/architecture/artifact-queue.md`.

## Token Stewardship Pattern

- Prefer canonical references over restating policy, templates, or provider rules.
- Keep stage artifacts concise: record decisions, evidence, blockers, validation, and handoffs; omit narrative filler.
- Do not duplicate content already captured in another devspec artifact. Link or name the source instead.
- Preserve user-authored content with targeted edits instead of whole-file rewrites.

## Minimum Necessary Implementation Pattern

- Before planning or changing code, confirm whether the current task requires a repository code change or can be satisfied by artifact updates, configuration already present, documentation, validation, or no action.
- Prefer existing repository patterns, language or platform capabilities, and already-installed dependencies before introducing new abstractions, helper layers, generated code, or dependencies.
- Choose the smallest change that satisfies `finalize.md`, `tasks.md`, applicable validation, and `devspec/foundation/rules.md`; do not add speculative flexibility, cleanup, refactors, or future work unless the finalized brief requires it.
- Never reduce repository access checks, readiness gates, validation, error handling, security, privacy, accessibility, compliance handling, or required recovery state to save tokens or lines.
- Record the selected implementation path, evidence, blockers, validation, and material tradeoffs; omit rejected alternatives unless they explain a risk, blocker, retry, or review finding.

## Task Quality Gate Pattern

- Use this pattern across `/devspec.tasks`, `/devspec.implement`, and `/devspec.review` to keep task planning, execution, and review aligned with the finalized brief.
- Keep sequencing, dependency, and traceability information in task rows.
- During `/devspec.tasks`, record a compact `Task Quality Review` before `Implementation Tasks` covering scope/source coverage, validation coverage, dependency order, granularity, blockers, ambiguity, and implementation-risk gaps.
- Every executable task must include `Source refs` pointing to the finalized acceptance criteria, implementation brief rows, validation plan rows, risks, or follow-ups that justify the task.
- Keep tasks actionable, independently verifiable where practical, and sized for one meaningful checkpoint. Split tasks that are too broad to validate safely; merge tasks that are too small to produce useful implementation or review evidence.
- Sequence task rows so dependencies appear before dependents. Use the `Depends on` column for required predecessors, and use `none` only when the task can start without another task's output.
- Treat missing coverage, impossible sequencing, vague done criteria, missing validation, ambiguous target areas, unresolved access, and external blockers as task-planning blockers when they would materially change implementation or review.
- During `/devspec.implement`, before each task attempt, confirm the task is still actionable, within finalized scope, unblocked, specific enough to implement, and ordered after its dependencies. If implementation reveals task ambiguity, a blocking dependency, or oversized scope, update `implement.md`, update the task checkpoint or status when applicable, and stop for the required structured question instead of silently expanding scope.
- During `/devspec.review`, compare `finalize.md`, `tasks.md`, `implement.md`, and changed code or artifacts. Flag missing source coverage, incomplete or skipped tasks without rationale, blocked tasks treated as done, missing validation evidence, source-ref drift, and implementation beyond task scope as review findings when they affect correctness, delivery risk, or readiness to close.

## Artifact Content Pattern

- Write artifacts for developers who need to plan, implement, review, or recover work. Every captured item should make clear what is true, where it applies, what evidence or source supports it, and what a developer should do with it.
- Prefer Markdown tables for matrix data, including stack details, source evidence, repository configuration, work-area boundaries, integration contracts, rules, readiness, tasks, validations, and comparison-style decisions.
- Prefer bullets for direct facts, rules, assumptions, blockers, and concise developer guidance.
- Prefer ordered lists only for workflows, procedures, reproduction steps, migration steps, or task sequences where order changes the result.
- Avoid theory, generic explanations, restated prompt policy, and broad background that does not change a developer's next action.
- Do not keep optional sections only to satisfy a template. Omit sections, tables, or rows that have no real project content, unless the empty section is required for resume state or a command contract.
- Use source labels consistently: `confirmed` for user-provided or approved facts, `observed` for direct repository evidence, `inferred` for reasoned conclusions from evidence, and `blocked` for unresolved gaps.
- Preserve useful existing content, but replace stale, vague, or duplicative prose with compact structured records.

## Constitution Amendment Pattern

- Use `devspec/constitution.md` only for rare, durable principles that apply across work items and agents.
- Do not overwrite the full constitution or replace existing principles unless the user explicitly confirms the replacement or removal.
- Do not infer settled principle changes from repository evidence alone. Treat extracted or observed principles as candidates until the user confirms them.
- Route operational gates, compliance procedures, enforcement details, and evolving governance requirements to `devspec/foundation/rules.md`; route product purpose, audiences, outcomes, scope, and metrics to `devspec/foundation/project-context.md`.
- Before writing a confirmed constitution change, check affected prompts, agents, templates, adapter guidance, validation docs, `devspec/foundation/project-context.md`, and `devspec/foundation/rules.md` for conflicts with the changed principle.
- Do not leave unexplained template placeholders or bracketed tokens in live constitution content.
- Record unresolved amendment follow-ups explicitly in the affected artifact using `TODO(<FIELD_NAME>): <next action>` instead of hidden prose.

## Readiness Gap Scan Pattern

- Use this pattern during `/devspec.finalize` before marking a work item `ready`; other stages may record obvious blockers, but they must not run a broad readiness audit unless their command contract says so.
- Scan the upstream work-item artifacts, accepted decisions, applicable foundation artifacts, `devspec/constitution.md`, `devspec/architecture/overview.md`, relevant `devspec/architecture/decisions/*.md`, and available repository evidence for gaps in scope boundaries, acceptance criteria, actors or personas, domain and data rules, lifecycle or state behavior, UX/error/empty/loading states, non-functional needs, integrations and external dependencies, security/privacy/compliance, validation testability, terminology consistency, TODO markers, ambiguous placeholders, and conflicts with durable principles, foundation constraints, delivery gates, or architecture decisions.
- Treat a gap as blocking only when resolving it would materially change implementation scope, task decomposition, validation design, repository readiness, delivery risk, compliance handling, or type-specific rule handling.
- Do not ask about low-impact preferences, purely stylistic choices, implementation tactics better left to `/devspec.tasks`, or facts already captured in upstream artifacts.
- When one or more blocking gaps remain, prioritize by highest implementation impact and uncertainty, then surface only the top unresolved blocking clarification through the current stage's single-question or handoff flow.
- Record scan outcomes through existing readiness gates, implementation brief rows, validation plan rows, blockers, or handoff state. Do not create a separate speculative audit artifact or invent coverage/status values outside `devspec/glossary.md`.

## Discovery Exclusion Pattern

- Before repository search, extraction, code-pattern discovery, layout mapping, validation-surface discovery, or generated helper scripts, read `devspec/foundation/discovery-exclusions.md` when present.
- Apply `Baseline Exclusions` for dependency installs, generated output, caches, coverage output, VCS internals, local tool metadata, and temporary output. Do not infer project conventions from installed dependency or generated output source.
- Use manifests, lockfiles, and framework config files for dependencies and tooling; inspect dependency folders only when the user asks or a project override permits it.
- Respect repository ignore files as a baseline, while still applying this pattern.
- Apply `Ecosystem Discovery Rules` from `devspec/foundation/discovery-exclusions.md`; initialize it from `devspec/foundation/_template/discovery-exclusions.md` when missing.
- Keep source discovery focused on owned source roots, tests, scripts, config, infrastructure, docs, manifests, and routing-critical files.
- Record project-specific include or exclude exceptions in `devspec/foundation/discovery-exclusions.md`, not individual stage artifacts.

## Diagram Extraction Consistency Pattern

- Use this pattern when extraction proposes diagram candidates or `/devspec.diagram` generates or updates a diagram.
- Queue only candidates backed by concrete repository evidence from owned routes, modules, workflows, state transitions, services, integrations, ADRs, docs, infrastructure, runtime config, or manifests.
- Each queued candidate must include ID, scope, diagram type, subject, target location, evidence, confidence, status, tags, and next action or notes. Record the equivalent-diagram check result in `Next action or notes`.
- Diagram output format defaults to `svg`. Accept `format=` values made from one or more unique output types from `svg`, `html`, and `mermaid`, joined with `+`. Example: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`. Reject duplicated or unknown output types, such as `format=svg+svg`, `format=png`, or `format=pdf`, with one structured `clarification` question before writing output.
- Format examples:
  - `/devspec.diagram runtime architecture` -> generate SVG only.
  - `/devspec.diagram format=html runtime architecture` -> generate HTML only.
  - `/devspec.diagram format=mermaid runtime architecture` -> generate Mermaid only, stored in the Markdown artifact.
  - `/devspec.diagram format=svg+html runtime architecture` -> generate SVG and HTML only.
  - `/devspec.diagram format=svg+mermaid runtime architecture` -> generate SVG and Mermaid only.
  - `/devspec.diagram format=html+mermaid runtime architecture` -> generate HTML and Mermaid only; do not generate SVG.
  - `/devspec.diagram format=svg+html+mermaid runtime architecture` -> generate all three output types.
- Use stable IDs such as `DIA-001`, `DIA-002`, preserving existing IDs and assigning the next available number for new rows.
- Keep subjects specific enough to become one diagram file. Use Title Case for display names and lowercase kebab-case for subject slugs.
- For durable architecture diagram queue rows, use the queue ID as the sequence anchor: `DIA-001` maps to subject `dia-001-<diagram-name>`, default SVG target `devspec/architecture/images/dia-001-<diagram-name>.svg`, optional Mermaid Markdown target `devspec/architecture/diagrams/dia-001-<diagram-name>.md`, optional HTML target `devspec/architecture/html/dia-001-<diagram-name>.html`, and display title `DIA-001 - <Title Case Diagram Name>`.
- Never renumber existing `DIA-*` rows, generated `dia-NNN-*` diagram files, or generated `dia-NNN-*` SVG files. New diagrams get the next available `DIA-*` ID and matching lowercase `dia-NNN-*` subject prefix.
- Avoid language, framework, vendor, or platform names in default diagram subjects. Use language-specific evidence only as supporting evidence unless the user explicitly requests a specialized diagram.
- Prefer reusable architecture, module, feature, workflow, sequence, state, or user-journey diagrams over temporary work-item diagrams. Use work-item `images/<diagram-name>.svg` by default, optional work-item `diagrams.md`, and optional `html/<diagram-name>.html` only for explicit or clearly temporary work-item-specific diagram content, and keep diagram status in `devspec/architecture/artifact-queue.md`.
- Use queue `Tags` for durable selection and batch processing. Process-flow rows must include `process-flow`; add narrower tags such as `business-process`, `user-journey`, `lifecycle-flow`, or `hybrid-user-to-data-operational-flow` when they apply.
- Use queue `Diagram type` for the logical diagram family only: `flowchart`, `sequenceDiagram`, `journey`, `stateDiagram`, `classDiagram`, `erDiagram`, `gantt`, `quadrantChart`, `mindmap`, or `timeline`. Record orientation such as `LR`, `TD`, or `BT` and output format in `Next action or notes` when useful. Examples: `format=svg`, `format=html`, `format=mermaid`, `format=svg+html`, `format=svg+mermaid`, `format=svg+html+mermaid`, `format=html+mermaid`. Write the full Mermaid declaration in the optional Mermaid Markdown artifact when Mermaid output is selected.
- Use `flowchart LR` for relationship maps, dependency graphs, event flows, and pipelines. Use `flowchart TD` for context, topology, hierarchy, data movement, and risk grouping. Use `flowchart BT` only for optional layer dependency views where lower layers should appear as foundations.
- Use `sequenceDiagram` for actor, service, workflow, or security interactions over time; `journey` for user-facing paths; `stateDiagram-v2` for lifecycle or status transitions; `classDiagram` for stable domain or structural relationships; and `erDiagram` for entity relationship models.
- Use confidence values consistently: `observed` for directly supported code, docs, config, or ADR evidence; `high-confidence` for inference from multiple local evidence points; `low-confidence` only when useful but incomplete evidence must be recorded as an assumption.
- Do not queue vague subjects, candidates without source evidence, duplicate or equivalent existing diagrams, or temporary work-item diagrams without an explicit request.
- Use `blocked` when a diagram idea is useful but evidence is insufficient; use `skipped` only after the user declines generation.
- Before queueing or writing, check `devspec/architecture/artifact-queue.md`, `devspec/architecture/overview.md`, `devspec/architecture/images/*.svg`, `devspec/architecture/diagrams/*.md`, `devspec/architecture/html/*.html`, and relevant work-item `images/*.svg`, `diagrams.md`, and `html/*.html` files for equivalent subject, scope, diagram type, or target location.
- Avoid duplicate overview diagrams unless `devspec/architecture/overview.md` lacks a confirmed architecture context or diagram reference entry.
- During `/devspec.extract`, seed candidates in `devspec/architecture/artifact-queue.md` and ask only about the next unresolved candidate after higher-priority confirmations. Generate diagrams later through `/devspec.diagram` unless the user explicitly continues through the confirmed queue.
- During `/devspec.extract`, honor requested diagram output formats as generation preferences only after explicit approval; extraction may generate at most one approved diagram artifact set before stopping or asking for continuation.
- During `/devspec.diagram`, reuse matching queue metadata instead of reclassifying the same subject from scratch. Generate exactly one evidence-backed diagram artifact set per run unless the user requests process-flow batch generation.

## Architecture Diagram Intake Pattern

- Use this pattern when `/devspec.diagram` receives structured architecture-diagram input with fields such as `Application/System`, `Architecture style`, `Primary goal of diagram`, `Audience`, `Users/Actors`, `Core components`, `External systems`, `Data stores`, `Key flows`, `Boundaries`, `Design rules`, or `Output format`.
- Treat structured architecture-diagram input as approved input for one `/devspec.diagram` artifact set. Continue to follow the [Diagram Extraction Consistency Pattern](#diagram-extraction-consistency-pattern), [SVG Output Pattern](#svg-output-pattern), [Mermaid Internal Naming and Readability Pattern](#mermaid-internal-naming-and-readability-pattern), [Mermaid Visual Quality Pattern](#mermaid-visual-quality-pattern), and duplicate checks before writing.
- Preserve SVG as the default output. Treat editable SVG, SVG-only output, real SVG text, "Generate as SVG", "Generate this as SVG", or "not as a raster image" as `format=svg` unless the user explicitly requests an output combination that includes `html` or `mermaid`.
- Map `Application/System` to diagram subject and title unless a matching queue row already supplies a durable subject. Map `Architecture style`, `Primary goal of diagram`, and `Audience` into diagram metadata, queue notes, source evidence or assumptions, and maintenance notes when they affect generation.
- Map `Users/Actors`, `Core components`, `External systems`, `Data stores`, and `Boundaries` to visible diagram content only when supported by user-confirmed input, existing `devspec/` artifacts, or repository evidence. Keep `Core components` as components with short labels; put responsibilities in evidence or assumptions unless a label can remain 1-4 words.
- Map `Key flows` to numbered arrows when SVG output is selected. For Mermaid output, keep edge labels short and omit visible step numbers unless the user explicitly requests numbered flows and the diagram remains readable.
- Map `Design rules` into layout guidance only when they do not conflict with canonical devspec rules. Preserve 16:9 landscape, clear left-to-right or top-to-bottom flow, grouped components, dashed boundaries, short labels, low connector crossings, and a legend for SVG output.
- If the input says `Do not add any components not listed above`, `Do not add components`, or equivalent, treat the listed components and systems as authoritative. Do not add inferred visible nodes; record missing but relevant repository evidence as assumptions, blockers, or maintenance notes instead.
- If structured input conflicts with confirmed architecture artifacts, ADRs, foundation rules, or repository evidence, record the conflict and ask one structured question only when choosing either source would materially change the diagram scope, security/compliance meaning, or target artifact. Otherwise prefer confirmed durable artifacts and record the user input as an assumption or note.
- Keep SVG architecture diagrams presentation-ready: 16:9 canvas, standalone XML, real `<text>` elements, numbered flow markers, dashed boundary boxes, short labels, and a legend. Never embed rasterized text.

Compact neutral example:

```text
/devspec.diagram

Application/System:
Customer Portal

Architecture style:
cloud-native

Primary goal of diagram:
Explain runtime flow and data movement.

Audience:
Developers and architects.

Users/Actors:
- Customer
- Support agent

Core components:
- Web app: user entry point
- API service: business operations
- Worker: asynchronous processing

External systems:
- Identity provider: authentication
- Payment gateway: payments

Data stores:
- Customer database: profiles and orders

Key flows:
1. User signs in through the identity provider.
2. Web app calls the API service.
3. API service reads and writes customer data.
4. Worker processes asynchronous jobs.
5. API service sends payment requests to the gateway.

Boundaries:
- Client boundary
- Application boundary
- External services boundary

Design rules:
- Use a 16:9 landscape layout
- Use numbered arrows
- Use dashed boxes for boundaries
- Include a legend

Output format:
Editable SVG.
```

## Diagram Family Intake Pattern

- Use this pattern when `/devspec.diagram` receives structured non-architecture input for `sequenceDiagram`, `stateDiagram`, `classDiagram`, `erDiagram`, `journey`, `timeline`, `gantt`, `quadrantChart`, or `mindmap` content.
- Treat structured family-specific input as approved input for one `/devspec.diagram` artifact set. Continue to follow the [Diagram Extraction Consistency Pattern](#diagram-extraction-consistency-pattern), [SVG Output Pattern](#svg-output-pattern), [Mermaid Internal Naming and Readability Pattern](#mermaid-internal-naming-and-readability-pattern), [Mermaid Visual Quality Pattern](#mermaid-visual-quality-pattern), and duplicate checks before writing.
- Preserve SVG as the default output. Treat editable SVG, SVG-only output, real SVG text, "Generate as SVG", "Generate this as SVG", or "not as a raster image" as `format=svg` unless the user explicitly requests an output combination that includes `html` or `mermaid`.
- Map shared fields such as `Subject`, `Title`, `Purpose`, `Audience`, `Scope`, `Evidence`, `Source`, `Output format`, `Design rules`, and `Exclusions` into diagram metadata, queue notes, source evidence or assumptions, maintenance notes, and generated content when they affect generation.
- If structured input says `Do not add items`, `Use only listed items`, `Do not infer additional nodes`, or equivalent, treat the listed participants, states, entities, stages, milestones, plotted items, or topics as the complete visible set. Do not add inferred visible elements; record missing but relevant repository evidence as assumptions, blockers, or maintenance notes instead.
- If structured input conflicts with confirmed architecture artifacts, ADRs, foundation rules, or repository evidence, record the conflict and ask one structured question only when choosing either source would materially change the diagram scope, security/compliance meaning, lifecycle/state meaning, data/domain meaning, timeline meaning, scoring meaning, or target artifact. Otherwise prefer confirmed durable artifacts and record the user input as an assumption or note.
- Keep family-specific labels short and evidence-backed. Put long explanations in source evidence, assumptions, or maintenance notes rather than visible nodes, messages, states, cards, milestones, plotted labels, or branch labels.
- Use family-specific mappings only for fields that materially change visible diagram content:

| Diagram family | Structured input fields to map |
| --- | --- |
| `sequenceDiagram` | `Participants`, `Actors`, `Systems`, `Messages`, `Steps`, `Happy path`, `Error path`, `Method labels`, `Collapsed intermediaries`, `Notes` |
| `stateDiagram` / lifecycle | `States`, `Start state`, `End state`, `Terminal states`, `Transitions`, `Events`, `Guards`, `Exception states`, `Rework states`, `State groups` |
| `classDiagram` / `erDiagram` / domain model | `Entities`, `Classes`, `Fields`, `Methods`, `Relationships`, `Cardinality`, `Aggregate boundaries`, `External entities`, `Ownership` |
| `journey` | `Actor`, `Persona`, `Stages`, `Actor touchpoints`, `System touchpoints`, `Decisions`, `Outcomes`, `Pain points`, `Status signals` |
| `timeline` / `gantt` | `Phases`, `Milestones`, `Dates`, `Periods`, `Dependencies`, `Gates`, `Risks`, `Owners`, `Release markers` |
| `quadrantChart` | `X axis`, `Y axis`, `Quadrant labels`, `Plotted items`, `Scores`, `Scoring meaning`, `Thresholds`, `Priority notes` |
| `mindmap` | `Central topic`, `Branch groups`, `Child topics`, `Relationships`, `Priority branches`, `Open questions`, `Notes` |

## SVG Output Pattern

- Use this pattern when `/devspec.diagram` or approved `/devspec.extract` continuation generates SVG, Mermaid, or HTML output.
- SVG is the default output. `format=svg` generates the SVG visual output plus required queue or overview metadata. Any accepted combination generates exactly the requested output types: `svg` for the SVG visual output, `mermaid` for the optional Markdown/Mermaid artifact, and `html` for the optional standalone HTML artifact.
- Store durable SVG files under `devspec/architecture/images/dia-NNN-<diagram-name>.svg`, optional Mermaid files under `devspec/architecture/diagrams/dia-NNN-<diagram-name>.md`, and optional HTML files under `devspec/architecture/html/dia-NNN-<diagram-name>.html`. Store temporary work-item SVG files under `devspec/work-items/<work-item-folder>/images/<diagram-name>.svg`, optional Mermaid content in `devspec/work-items/<work-item-folder>/diagrams.md`, and optional HTML files under `devspec/work-items/<work-item-folder>/html/<diagram-name>.html`.
- For SVG-only output, do not create a Markdown diagram artifact unless requested. Preserve resumability and evidence through `devspec/architecture/artifact-queue.md`, `devspec/architecture/overview.md` diagram references, SVG metadata elements, and queue notes.
- Select the SVG template deterministically from the matrix below. Use the most specific matching row by queue tags, explicit user request, or diagram family before falling back to `architecture-diagram.svg`; do not invent ad hoc SVG layouts when a matching template exists.

| Diagram request, family, or tags | SVG template |
| --- | --- |
| Architecture, component, topology, dependency graph, API surface, event/message map, data ownership flow, deployment topology, configuration/secrets flow, risk/hotspot map, generic workflow map | `devspec/architecture/_template/architecture-diagram.svg` |
| `process-flow`, `business-process`, process-flow rows tagged `user-journey` or `lifecycle-flow`, `hybrid-user-to-data-operational-flow`, explicit process-flow SVG | `devspec/architecture/_template/process-flow-diagram.svg` |
| `sequenceDiagram`, interaction sequence, authentication/authorization sequence, critical workflow sequence | `devspec/architecture/_template/sequence-diagram.svg` |
| `stateDiagram`, `stateDiagram-v2`, lifecycle, status transition | `devspec/architecture/_template/state-lifecycle-diagram.svg` |
| `classDiagram`, `erDiagram`, domain model, domain structure, entity relationship | `devspec/architecture/_template/domain-model-diagram.svg` |
| `journey`, explicit user journey that is not a process-flow row | `devspec/architecture/_template/journey-map-diagram.svg` |
| `timeline`, `gantt`, release timeline, migration timeline, sprint or release plan | `devspec/architecture/_template/timeline-plan-diagram.svg` |
| `quadrantChart`, risk quadrant, priority quadrant, 2D scoring | `devspec/architecture/_template/quadrant-analysis-diagram.svg` |
| `mindmap`, domain capability mindmap, explicit brainstorming map | `devspec/architecture/_template/mindmap-diagram.svg` |

- Generated SVG files must be standalone XML with `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 WIDTH HEIGHT" role="img" aria-labelledby="title desc">`, inline `<defs>` and `<style>`, and no external assets.
- Generated SVG and HTML visual output must follow the shared devspec dark visual contract unless the user explicitly requests a light or custom theme: dark slate page background `#020617`, framed surface `#0f172a`, subtle grid or divider lines `#1e293b`, primary text `#f8fafc`, secondary text `#cbd5e1` or `#94a3b8`, Apache-2.0-distribution-safe monospace font stack `"JetBrains Mono", "Cascadia Code", monospace`, and the semantic role palette used by the Mermaid Visual Quality Pattern. Do not name proprietary system font fallbacks in generated SVG or HTML, and do not bundle, embed, or fetch font files unless their open-font license and required notices are included with the distribution.
- Do not generate white-background, default-renderer, or simple unstylized SVG/HTML diagrams for `/devspec.diagram`. If a renderer or diagram family cannot honor the dark visual contract, prefer generating the SVG companion as the canonical visual output and record the limitation in the Mermaid or HTML artifact notes.
- Use a 16:9 landscape SVG canvas by default, preferably `viewBox="0 0 1600 900"` for durable diagrams. Smaller custom SVGs are allowed only when documented constraints require them, and they must still keep the same dark chrome, monospace typography, role colors, line treatment, real `<text>` labels, and compact legend style.
- Keep process-flow, journey, state, sequence companion, domain, workflow, and architecture SVGs visually related: same dark background, grid, framed surface, title treatment, footer treatment, semantic role colors, and legend treatment. Preserve family-specific semantics such as process lanes, decisions, exceptions, loop-backs, actors, stores, and boundaries inside that shared style.
- Do not include `<script>`, `<iframe>`, `<foreignObject>`, remote images, remote fonts, external stylesheets, secrets, tokens, credentials, internal-only URLs, or visible placeholder tokens in generated SVG output.
- Keep visible SVG text short: noun labels for nodes, protocol or action labels for arrows, and no paragraphs. Use semantic colors consistently with the Mermaid visual palette.
- Draw arrows behind nodes, keep labels clear of connectors, keep the legend outside major boundaries, and ensure the diagram remains readable at README width and when exported to PNG or PDF.
- Before reporting success, validate the generated SVG as XML and check required root attributes, forbidden elements, unresolved placeholders, obvious text overlap, and evidence-backed content.
- For `format=html`, create a standalone `.html` file with escaped text, inline CSS, no scripts, no iframes, no remote assets, no remote fonts, no secrets, and no unresolved placeholders. Render the same evidence-backed diagram content as static HTML using the same dark visual contract as the SVG output.
- For `format=mermaid`, use `devspec/architecture/_template/diagram.md` for durable diagrams or `devspec/work-items/_template/diagrams.md` for temporary work-item diagrams, and include Mermaid content.

## Mermaid Internal Naming and Readability Pattern

- Use this pattern when `/devspec.diagram` generates or updates Mermaid content, and when `/devspec.extract` records generation guidance for queued diagram candidates.
- Keep durable diagram file naming separate from Mermaid internal naming. `DIA-*` IDs and `dia-NNN-*` subjects name queue rows and files; Mermaid node IDs, node labels, edge labels, classes, methods, and layout must stay simple and readable.
- Choose the best Mermaid family for the evidence: `flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram`, `journey`, `erDiagram`, `gantt`, `quadrantChart`, `mindmap`, or `timeline`. Use `flowchart TD` for hierarchy, topology, data movement, and risk grouping. Use `flowchart LR` for interactions, relationship maps, process flows, event flows, and pipelines. Use `stateDiagram-v2` as the generated declaration for state diagrams. Use `gantt` for sprint plans, release schedules, and task-duration timelines; `timeline` for historical milestones and event sequences; `quadrantChart` for 2D priority or risk scoring matrices; and `mindmap` for exploratory domain or capability brainstorming only when formal flowchart evidence is not yet available.
- For flowcharts, use short alphanumeric node IDs with no spaces or punctuation, such as `AuthCtrl`, `ProviderSvc`, `OrderDb`, or `JobRunner`.
- Wrap every human-readable flowchart node label in double quotes and keep it to 1-4 words, such as `AuthCtrl["Authentication Controller"]` or `ProviderSvc["Provider Service"]`.
- Do not use `\n` or `<br>` line breaks inside node labels or edge labels under any circumstance. If a label needs a line break, it violates the 1-4 word node label rule or 2-3 word edge label rule.
- Flowchart nodes must be nouns such as components, classes, services, actors, or data stores, not paragraphs of responsibilities or actions.
- Put interaction context on edge labels, not inside node labels. Use 2-3 word action phrases such as `-->|"API Calls"|`, `-->|"Loads App"|`, or `-->|"Validates Session"|`.
- Keep each diagram focused on one primary business domain or architectural concern. Do not create overloaded graphs that mix orthogonal concerns such as authentication, session validation, master data CRUD, reporting, and deployment in the same flowchart.
- Prefer macro structure over micro logic in architectural `flowchart` or `graph` diagrams. Map components such as services, controllers, repositories, applications, data stores, and external systems, not internal logic inside those components.
- Do not use decision diamonds such as `Node{"Is Valid?"}` or map `if/else` execution paths, validation loops, error handling branches, or error-handling UI states unless the user explicitly requests an algorithm or activity flowchart.
- Do not map UI micro-interactions such as opening modals, hiding editors, clicking buttons, showing failure modals, or user input correction. Treat a client application as one cohesive boundary or a small set of high-level pages.
- Keep architectural flowcharts and graphs structurally unidirectional and strictly adjacent by layer. Map dependency or invocation direction, such as UI -> API -> service -> repository -> database, and do not draw cross-layer arrows that skip layers.
- Treat return paths as implied by downward invocation arrows; do not map response data, domain data, HTTP status codes, validation exceptions, database errors, or other return paths flowing back up the stack.
- Use `sequenceDiagram` when the requested view requires exact step-by-step request and response behavior. Do not force complex bidirectional request or response cycles into a `flowchart` or `graph`.
- In sequence diagrams, map messages only between distinct participants, such as UI -> controller -> service -> repository. Do not use self-referential arrows to show internal variable processing or local component logic.
- Default sequence diagrams to the successful happy path unless the user explicitly asks for an error scenario. Omit `alt` or `opt` blocks for local form validation failures, 400 Bad Requests, or generic exception handling.
- Collapse pass-through API client helpers in sequence diagrams. If a UI component uses an API client service only to forward a request to an API controller, map the message directly from the UI component to the API controller.
- Prefer actual method names for sequence message labels, such as `AuthenticateAsync(req)`, instead of descriptive paragraphs or implementation steps such as trimming fields or hashing values.
- Keep runtime and compile-time concerns in separate diagrams. Do not mix runtime communication such as HTTP calls or database queries with compile-time structural dependencies such as project references. Default to runtime or logical data flow unless the user explicitly asks for a project dependency graph.
- Exclude meta-actors and SDLC processes from logical architecture diagrams. Do not include developers, maintainers, source control, Git, CI/CD, deployment pipelines, or build processes unless the user explicitly requests an SDLC, build, or deployment diagram.
- Exclude build artifacts from runtime diagrams. Do not include database projects, `.csproj` files, generated artifacts, package outputs, or other source-code project files unless the diagram is explicitly a static code dependency or project dependency graph.
- Enforce C4-style system boundaries for runtime diagrams. Group runtime components inside sensible system boundaries, and place databases or stores owned and exclusively used by the application inside the application system boundary.
- Use `PascalCase` for classes, interfaces, and entities. Use `camelCase()` for methods or functions only when a method-level diagram is explicitly requested or the selected diagram type requires methods.
- Avoid API and Swagger bloat in Mermaid content. Do not put HTTP verbs, route templates, status codes, DTO names, payload model names, or endpoint specs in flowchart nodes.
- Avoid tech stack and version bloat in Mermaid content. Do not put framework versions, target frameworks such as `net10.0`, specific library names such as `Dapper` or `MediatR`, or hosting models in node labels unless the user explicitly requests a physical deployment diagram.
- Omit standard framework wiring such as controller registration, middleware setup, dependency injection setup, CORS, logging, SQL connection factories, or configuration plumbing unless the requested diagram is specifically about startup, request-pipeline, or infrastructure-layer behavior.
- Prefer domain, capability, service, component, actor, and data-store names over file names, route names, package names, and implementation noise.
- Keep generated Mermaid valid inside a fenced `mermaid` block. If a user asks for "only Mermaid", apply that restriction to the Mermaid content itself while preserving required devspec artifact metadata outside the diagram block.
- Apply the [Mermaid Visual Quality Pattern](#mermaid-visual-quality-pattern) for semantic color coding, node shapes, subgraph boundaries, and complexity guardrails in every generated diagram.

## Mermaid Visual Quality Pattern

- Use this pattern when `/devspec.diagram` generates or updates any Mermaid diagram. Apply the full pattern (theme init, `classDef` palette, shapes, subgraphs, guardrails) to `flowchart` and `stateDiagram-v2`. Apply complexity guardrails only to `sequenceDiagram`, `classDiagram`, `erDiagram`, `gantt`, `quadrantChart`, `mindmap`, and `timeline`.
- Apply semantic `classDef` color coding, dark theme initialization, role-appropriate node shapes, and `subgraph` boundaries to produce clean, information-dense diagrams free of visual noise.
- This pattern complements the [Mermaid Internal Naming and Readability Pattern](#mermaid-internal-naming-and-readability-pattern); visual quality rules add color, shape, and layout structure without overriding naming or anti-bloat constraints.
- Every generated flowchart must: (1) open with the theme init block, (2) declare only the `classDef` classes whose roles appear in the diagram, (3) use role-appropriate node shapes, (4) wrap boundaries of 3+ nodes in a named `subgraph`, (5) assign `classDef` classes in a batch block at the end, and (6) stay within complexity guardrails.

### Theme Initialization

- Open every `flowchart` block with the dark theme init directive so renderers that support it (VS Code, Mermaid Live Editor, Cursor, most AI chat surfaces) apply consistent dark theming. GitHub and GitLab silently ignore `%%{init:...}%%` and render with their default theme; `classDef` colors are the portable styling fallback that works on both.
- Use this exact init block unless the user requests a light or custom theme:

```
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#64748b', 'clusterBkg': '#0f172a', 'clusterBorder': '#334155'}}}%%
```

- Do not add `%%{init:...}%%` to `sequenceDiagram`, `journey`, `classDiagram`, `erDiagram`, `gantt`, `quadrantChart`, `mindmap`, or `timeline` blocks; those diagram families rely on renderer-managed defaults.
- For `stateDiagram-v2`, include the init block only when the rendering context is confirmed to support it; omit it otherwise.
- Mermaid output is not the canonical visual target when renderer support conflicts with the shared dark visual contract. When a Mermaid family or host renderer cannot reliably enforce dark styling, keep the Mermaid syntactically portable, record the renderer limitation in notes, and use SVG or HTML output for the consistent architecture-style visual.

### Semantic `classDef` Palette

- Assign each node a semantic class based on its architectural role using this fixed Mermaid-adapted palette, which mirrors Cocoon-AI's component-type color vocabulary:

| Role | Class name | Fill | Stroke |
| --- | --- | --- | --- |
| Frontend / UI | `ui` | `#083344` | `#22d3ee` |
| Backend / Service | `svc` | `#064e3b` | `#34d399` |
| Database / Store | `db` | `#4c1d95` | `#a78bfa` |
| Cloud / External | `ext` | `#78350f` | `#fbbf24` |
| Security / Auth | `sec` | `#881337` | `#fb7185` |
| Events / Messages | `evt` | `#7c2d12` | `#fb923c` |
| Actor / User | `actor` | `#1e293b` | `#94a3b8` |
| Generic / Unknown | `gen` | `#1e293b` | `#64748b` |

- Write the `classDef` block immediately after the `%%{init:...}%%` line and before any node or `subgraph` definitions. Include only declarations for roles that actually appear in the diagram; omit unused class names.
- Use the fixed class names (`ui`, `svc`, `db`, `ext`, `sec`, `evt`, `actor`, `gen`) across all diagrams so color meaning is consistent and predictable.
- Assign classes at the end of the diagram using batch syntax on a single line per class: `class Node1,Node2 svc`. Place all class assignments after the last node, edge, and `end` keyword.
- For `classDiagram` and `erDiagram`, skip `classDef` and use `style` directives only when the user explicitly requests semantic color coding; structural defaults are acceptable for those families.

### Node Shape Vocabulary

- Select node shape based on architectural role so shape carries meaning independent of color:

| Architectural role | Mermaid shape | Example |
| --- | --- | --- |
| Service / Component | Rectangle | `Svc["&nbsp;Auth Service&nbsp;"]` |
| User / Actor | Stadium | `User(["&nbsp;User&nbsp;"])` |
| Database / Store | Cylinder | `Db[("&nbsp;User DB&nbsp;")]` |
| Start / End terminal | Circle | `Start(((" ")))` |
| Event / Message | Hexagon | `Evt{{"&nbsp;Order Placed&nbsp;"}}` |
| Background Job / Worker | Subroutine | `Job[["&nbsp;Report Job&nbsp;"]]` |
| Decision gate | Diamond | `Dec{"&nbsp;Approved?&nbsp;"}` - only when explicitly requested |
| External API / SaaS | Asymmetric flag | `Ext>["&nbsp;Stripe API&nbsp;"]` |

- Never use diamond shapes for any purpose other than an explicit user-requested decision gate.
- Use rectangle as the default shape when no role-specific shape clearly applies.
- Do not mix shape meanings; once a shape carries a role in a diagram, every node of that shape must share the same role.
- Pad every node label and every edge label with a single `&nbsp;` on each side so text has visible breathing room inside its shape and along its connector: `Svc["&nbsp;Auth Service&nbsp;"]`, `-->|"&nbsp;Validates Session&nbsp;"|`. This applies to all node shapes (rectangle, stadium, cylinder, hexagon, subroutine) and to every Mermaid diagram family where `&nbsp;` is supported. Subgraph title labels follow the same rule: `subgraph BE["&nbsp;Backend Services&nbsp;"]`.

### Subgraph Structuring Rules

- Use `subgraph` to group nodes by system boundary, architectural layer, service ownership zone, or deployment region - the Mermaid equivalent of Cocoon-AI's dashed region and security-group boundaries.
- Wrap any logical boundary containing 3 or more nodes in a named `subgraph`. Use 1-3 word boundary labels with `&nbsp;` padding: `subgraph FE["&nbsp;Frontend Layer&nbsp;"]`, `subgraph BE["&nbsp;Backend Services&nbsp;"]`, `subgraph Cloud["&nbsp;Cloud Services&nbsp;"]`.
- Limit subgraph nesting to one outer boundary and one inner cluster at most; never nest more than 2 levels deep.
- Draw all cross-subgraph arrows after all `subgraph...end` blocks so edge lines render clearly over boundary boxes rather than being obscured by them.
- Do not use `subgraph` to cluster unrelated nodes for aesthetic grouping; every subgraph must represent a real architectural boundary, ownership group, or deployment zone.
- For diagrams with fewer than 3 nodes total, omit `subgraph`; flat structure is cleaner at that scale.

### Complexity Guardrails

- Cap flowchart node count at 15. Beyond 15 nodes, split at the clearest responsibility boundary into two diagrams and cross-link them via the `devspec/architecture/overview.md` Diagram Reference Index.
- Cap `sequenceDiagram` participant count at 6. Beyond 6, collapse pass-through intermediary components per the Mermaid Internal Naming and Readability Pattern.
- Cap `stateDiagram-v2` state count at 12. Beyond 12, extract sub-state regions into a child diagram and reference them from the parent.
- These are hard limits, not guidelines. If evidence demands more nodes, narrow the diagram scope: a focused diagram always delivers more value than an overloaded one.
- When splitting a diagram, record both halves as separate queue rows with cross-reference notes in `Next action or notes`.

## Process Flow Extraction Pattern

- Use this pattern during the `/devspec.extract` `process-flows` queue row and for `/devspec.diagram` process-flow generation.
- Treat process flows as business-centric end-to-end workflows first: user or actor initiation, system or service handoffs, business decisions, state changes, integrations, data touchpoints, success outcomes, and major failure or exception paths.
- Include user journeys, lifecycle flows, cross-service process sequences, and hybrid user-to-data operational flows when they explain an end-to-end business process.
- Do not treat pure structural maps, generic CRUD paths, deployment pipelines, CI/CD, authentication or configuration flows, or one-off work-item diagrams as process flows unless the user explicitly requests them.
- Discover process-flow evidence from owned routes, controllers, service methods, state transitions, jobs, event handlers, tests, docs, ADRs, integration boundaries, domain terms, user-facing actions, data stores, validations, and business outcomes.
- Queue one row per distinct durable process flow, with `process-flow` in `Tags`, a `dia-NNN-<diagram-name>` subject, a default SVG target under `devspec/architecture/images/`, and notes that name the actor or trigger, business outcome, major decisions or state changes, data touchpoints, integrations, duplicate-check result, requested output format, process-flow SVG template guidance, and suggested Mermaid declaration when the output set includes `mermaid`.
- Queue the default hybrid candidate when evidence can connect user entry points to application boundaries, services, integrations, data stores, validations, operational states, and outcomes:
  `Hybrid User-to-Data Operational Flow`, subject `dia-NNN-hybrid-user-to-data-operational-flow`, scope `workflow`, diagram type `flowchart`, declaration `flowchart TD`, tags `process-flow, business-process, hybrid-user-to-data-operational-flow`.
- Use `observed` only when source evidence directly supports the process flow. Use `high-confidence` when multiple local evidence points support the flow. Use `low-confidence` for useful but incomplete process-flow candidates and leave them queued rather than generating them in batch mode.
- When `/devspec.diagram` receives a process-flow batch request, process eligible rows in `DIA-*` order. Eligible rows must include `process-flow`, have status `proposed` or `confirmed`, confidence `observed` or `high-confidence`, a target matching `devspec/architecture/images/dia-NNN-<diagram-name>.svg` unless a non-SVG output set is explicitly requested, a valid output format when specified, and a passing duplicate check.
- When SVG output is selected for a process flow, use `devspec/architecture/_template/process-flow-diagram.svg`. Keep the happy path visually obvious, use distinct visual roles for start/end, manual, automated, integration, decision, exception, and artifact steps, draw exception paths as labeled dashed rose arrows, label loop-backs or rework paths, and ensure every branch ends at a step, state, or loop-back.

### Default Diagram Candidate Catalog

Use this language-neutral priority catalog for extraction. Queue a candidate only when concrete evidence exists and duplicate checks pass.

| Priority | Display name | Subject slug | Scope | Diagram type | Mermaid declaration | Default SVG target |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | System Context | `dia-NNN-system-context` | architecture | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-system-context.svg` |
| 2 | Domain and Capability Map | `dia-NNN-domain-capability-map` | architecture | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-domain-capability-map.svg` |
| 3 | Repository and Ownership Map | `dia-NNN-repository-ownership-map` | architecture | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-repository-ownership-map.svg` |
| 4 | Runtime Containers | `dia-NNN-runtime-containers` | architecture | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-runtime-containers.svg` |
| 5 | Dependency Graph | `dia-NNN-dependency-graph` | architecture | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-dependency-graph.svg` |
| 6 | Component Interaction Map | `dia-NNN-component-interaction-map` | architecture | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-component-interaction-map.svg` |
| 7 | API Surface Map | `dia-NNN-api-surface-map` | module | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-api-surface-map.svg` |
| 8 | Event and Message Flow | `dia-NNN-event-message-flow` | workflow | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-event-message-flow.svg` |
| 9 | Data Ownership and Flow | `dia-NNN-data-ownership-flow` | architecture | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-data-ownership-flow.svg` |
| 10 | Critical Workflow Sequence | `dia-NNN-<workflow-slug>-sequence` | workflow | `sequenceDiagram` | `sequenceDiagram` | `devspec/architecture/images/dia-NNN-<workflow-slug>-sequence.svg` |
| 11 | Authentication and Authorization Flow | `dia-NNN-authentication-authorization-flow` | workflow | `sequenceDiagram` | `sequenceDiagram` | `devspec/architecture/images/dia-NNN-authentication-authorization-flow.svg` |
| 12 | Deployment Topology | `dia-NNN-deployment-topology` | architecture | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-deployment-topology.svg` |
| 13 | CI/CD Pipeline | `dia-NNN-cicd-pipeline` | workflow | `flowchart` | `flowchart LR` | `devspec/architecture/images/dia-NNN-cicd-pipeline.svg` |
| 14 | Configuration and Secrets Flow | `dia-NNN-configuration-secrets-flow` | architecture | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-configuration-secrets-flow.svg` |
| 15 | Risk and Hotspot Map | `dia-NNN-risk-hotspot-map` | architecture | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-risk-hotspot-map.svg` |
| 16 | Hybrid User-to-Data Operational Flow | `dia-NNN-hybrid-user-to-data-operational-flow` | workflow | `flowchart` | `flowchart TD` | `devspec/architecture/images/dia-NNN-hybrid-user-to-data-operational-flow.svg` |
| 17 | Release or Migration Timeline | `dia-NNN-release-migration-timeline` | architecture | `timeline` | `timeline` | `devspec/architecture/images/dia-NNN-release-migration-timeline.svg` |
| 18 | Sprint and Release Gantt | `dia-NNN-sprint-release-gantt` | workflow | `gantt` | `gantt` | `devspec/architecture/images/dia-NNN-sprint-release-gantt.svg` |
| 19 | Risk and Priority Quadrant | `dia-NNN-risk-priority-quadrant` | architecture | `quadrantChart` | `quadrantChart` | `devspec/architecture/images/dia-NNN-risk-priority-quadrant.svg` |
| 20 | Domain Capability Mindmap | `dia-NNN-domain-capability-mindmap` | architecture | `mindmap` | `mindmap` | `devspec/architecture/images/dia-NNN-domain-capability-mindmap.svg` |

Optional evidence-specific diagrams may include `layered-architecture`, `<entity-slug>-lifecycle`, `<domain-slug>-domain-structure`, `background-jobs-schedulers`, or `<feature-slug>-workflow` when the user asks or repository evidence makes the specialized diagram more useful than a default catalog item. Catalog rows 17-20 are optional: queue them only when evidence shows a release plan, sprint timeline, 2D scoring need, or domain brainstorming gap that a core flowchart catalog item (rows 1-16) cannot adequately serve.

### Excluded Diagram Families

Do not use the following Mermaid families regardless of the requested subject. For each, use the stated portable alternative instead.

| Family | Reason excluded | Use instead |
| --- | --- | --- |
| `architecture-beta` | Requires Mermaid v11.1.0+; GitHub and GitLab render at v10.x and will silently fail or error. Still officially beta (`-beta` suffix, experimental). Icon system requires `iconify.design` registration - not portable across environments. Layout has known node-collision bugs (mermaid issue #6120). `flowchart` with `subgraph` blocks covers all the same layouts portably. | `flowchart TD` or `flowchart LR` with named `subgraph` blocks and the semantic `classDef` palette |
| `block` | Experimental, non-standard layout model, no `classDef` support, poor renderer coverage outside Mermaid Live. | `flowchart` |
| `kanban` | Experimental, project-management board - not an architecture artifact. | Work-item task list in `tasks.md` |
| `radar` | Experimental, data-chart family - not structural or flow-based. | `quadrantChart` for 2D scoring, or a plain markdown table |
| `sankey` | Experimental, data-flow volume chart - not a software architecture diagram. | `flowchart LR` for directional flows |
| `venn` | Experimental, limited renderer support, no devspec architecture use case. | `flowchart` with overlapping `subgraph` boundaries |
| `packet` | Experimental, network packet format - not a general architecture diagram. | `sequenceDiagram` for protocol interactions |
| `zenuml` | Non-standard sequence syntax, poor coverage outside Mermaid Live. | `sequenceDiagram` |
| `gitGraph` | SDLC artifact - branch and commit history, not architecture. | Source-control docs or a plain markdown table |
| `pie` | Data-chart family - not architectural. | Markdown table or `quadrantChart` |
| `xychart-beta` | Experimental, data-chart family - not architectural. | Markdown table |

## Exploration Recovery Pattern

- When `.github/skills/exploration-recovery/SKILL.md` is available, use it as the operational procedure.
- Before broad search, generated scripts, helper commands, provider lookup, or repeated discovery, follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern), then check `devspec/foundation/exploration-state.md#method-ledger` when present and session memory for reusable methods in the same scope.
- Use `working` methods first when scope and goal match.
- Skip `failed` methods unless input, environment, credentials, dependencies, access, path, or command changed.
- Prefer built-in repository search, targeted reads, manifest inspection, and configured provider tools before generating broad helper scripts.
- Limit probing to one new generated script, helper command, provider lookup path, or expensive search strategy per source or goal before falling back to direct search/read evidence gathering.
- When a reusable method outcome should be preserved, create or update `devspec/foundation/exploration-state.md` from `devspec/foundation/_template/exploration-state.md` and record method ledger rows with scope, goal, method, outcome, evidence or failure reason, retry or reuse condition, and last verified date. Optionally mirror a concise transient summary in `/memories/session/<stage>.md`.
- On rerun, use the recorded working method first and mention skipped known failures in the output.

## Foundation Update Pattern

- Required user input is mandatory.
- Ask one structured `clarification` question at a time when required details are missing or ambiguous, following the Interactive Question Pattern.
- Follow the [Artifact Content Pattern](#artifact-content-pattern).
- Follow the [Constitution Amendment Pattern](#constitution-amendment-pattern) when user input or repository evidence proposes durable principle changes.
- Use the matching `devspec/foundation/_template/*.md` or `devspec/architecture/_template/*.md` file as the section contract when one exists.
- Treat live `devspec/foundation/*.md` and `devspec/architecture/*.md` files as project-owned; update them in place and never replace them wholesale from templates.
- If a live foundation or architecture artifact is missing, initialize it from the matching `_template` file before applying user-provided or extracted content.
- Keep output durable, structured, concise, and useful to later work-item stages.

## Work-Item Target Pattern

- Use the current work item when clear; otherwise ask one structured `selection` question, following the Interactive Question Pattern.
- Work-item folders must follow the [Work-Item Folder Naming Pattern](#work-item-folder-naming-pattern) when created by `/devspec.story`.
- Follow the [Artifact Content Pattern](#artifact-content-pattern) when updating work-item artifacts.
- Treat optional user input as additive guidance only.
- Update the target work-item artifact in place. Stay within current stage scope and, after finalization, within finalized scope.

## Work-Item Folder Naming Pattern

- New work-item folders must use `<provider-prefix-optional>-<work-item-number>-<kebab-case-title>`.
- Validate new folder names with `^(?:[A-Z]{3,5}-)?[0-9]+-[a-z0-9]+(?:-[a-z0-9]+)*$`.
- Provider prefix is optional. When present, it must be 3-5 uppercase letters. Use known mappings where available: GitHub -> `GHUB`, Azure DevOps -> `ADO`, Jira -> `JIRA`.
- Work-item number must be numeric and should come from the resolved provider item, issue number, work item ID, or manually supplied external reference.
- Title slug must be lowercase kebab-case from the resolved provider title or manually supplied title.
- Remove punctuation, replace separators with hyphens, collapse repeated hyphens, and trim leading or trailing hyphens.
- If provider prefix, numeric work-item number, or title slug is missing or ambiguous, ask exactly one structured `clarification` or `selection` question before creating the folder.
- Do not create or rename a work-item folder until the generated folder name is valid or the user confirms a custom valid name.
- Do not automatically rename existing work-item folders; treat non-matching existing folders as legacy and continue using them unless the user explicitly asks to rename.

## Multi-Repo Validation Pattern

- `devspec/foundation/codebase-structure.md` is the source of truth for multi-repo configuration.
- Validate repository role, local path, current workspace availability, and access requirement there before planning or implementation depends on a repository.
- Treat repository location, workspace membership, and access requirement as separate facts; do not classify a repository outside the current repository folder or workspace as `reference-only` based on location.
- Do not infer, default, or backfill missing access requirements. In particular, do not assume `reference-only`.
- For each repository with a missing or ambiguous access requirement, ask exactly one repository-specific structured `confirmation` question before writing or relying on that configuration.
- Access requirement confirmation options must be limited to the values in `devspec/glossary.md#access-requirement-values` plus `Custom Answer`.
- Respect access requirements: do not edit repositories marked `reference-only`, `validation-only`, `release-coordination`, or `unavailable` unless the user explicitly confirms a scope change.
- Do not run validation in repositories marked `reference-only`, `release-coordination`, or `unavailable` unless the user explicitly confirms a scope change.
- For multi-repo work, stop and surface a blocker instead of guessing when required repository configuration is missing, outdated, or inaccessible.
- For single-repo work, do not require multi-repo configuration.

## Explore and Memory Pattern

- Follow the [Discovery Exclusion Pattern](#discovery-exclusion-pattern) before repository discovery, code search, or Explore runs.
- Use `Explore` when repository discovery, analogous implementations, impacted areas, or likely blockers cannot be resolved cheaply from current artifact context.
- Persist only transient working-state summaries to `/memories/session/<stage>.md`; do not treat session memory as canonical.
- Keep session memory concise and structured with objective, findings, open questions, decisions, and next recommended step.
- Update session memory only after meaningful discovery or scope changes, not after every minor step.
- If clarification changes scope or invalidates findings, rerun discovery as needed and replace stale memory sections instead of appending conflicts.
- Write final user-visible results and durable workflow state to the stage artifact, not only to session memory.
