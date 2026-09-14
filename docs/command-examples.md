# Beginner command examples

Use these examples from the agent host that has the devspec wrapper installed. Single-repository or multi-repository scope evidence is a prerequisite for every command. They are starting prompts, not commands to run in a fixed order: each command validates its own entry state and reports the one permitted next action.

## Confirm repository scope before every command

No `devspec.*` command treats the agent's current workspace as proof of its repository boundary. Before every command, provide either an explicit confirmation or current canonical evidence that identifies the scaffold, source repositories, and permissions. A brand-new repository can confirm that it has no source yet.

When evidence is absent, collect scope in this order for every command:

1. Ask one free-form repository path question. The text input should say, “Which repository is in scope? Enter its local path or name.” Show examples such as `D:\Code\orders-api` and `D:\Code\orders-web`, and let the developer type another value. Do not ask about access yet.
2. After the path is confirmed, ask: **What access requirement applies to `D:\Code\orders-api`?** Always show these choices: **Reference-only** — inspect source, configuration, and tests as evidence; do not edit or run validations. **Edit** — update approved repository files; do not run validations. **Edit-and-test** — make approved changes and run focused validations, including tests. Recommended for ordinary delivery work; for a repository outside the change, recommend the least privilege that still satisfies the command. **Validation-only** — run approved validations without editing. **Release-coordination** — coordinate release information without inspecting the repository. **Unavailable** — record a blocker because the repository cannot be accessed. **Custom Answer** — describe another boundary, for example edit only one approved folder. `Edit-and-test` grants normal delivery capability; the active command still controls whether source is changed.
3. Repeat the path question and then the access question for each additional repository. Record the scaffold path, repository role, and the separate read, edit, and validation permissions before continuing.

For a new project, the path answer may say `D:\Code\inventory — no source exists yet`; access is still confirmed after the path.

Current canonical evidence may be used only when it already names the repository path, role, and permissions in `foundation/codebase-structure.md` or another current foundation record, and still reflects the requested work. If neither confirmation nor evidence exists, complete the path question and then the access question for every repository before the agent inspects any source.

## Choose where the scaffold lives

| Layout | Use it when | What to do |
|---|---|---|
| In the project repository | One repository owns both code and devspec records. | Run `init --target .` from that repository. Commit `devspec/` and the selected agent wrapper with the code. |
| Dedicated scaffold repository | Several repositories share one change record, or the team keeps specifications separately. | Create a Git repository such as `D:\Code\orders-spec`, run `init --target D:\Code\orders-spec`, and open that directory in the agent host. State every source repository's path, role, and permissions in the request. Commit the devspec artifacts to the scaffold repository. |

The scaffold location is not a source-access grant. When it is outside the code repository, source code remains outside the scaffold until the developer explicitly confirms the repository boundary. Keep only one authoritative work-item record for a change: in the owning project repository or in the dedicated scaffold repository.

## Work with multiple repositories

Name a primary repository that owns the change record, then list every dependent repository. For each one, state a local path plus one named access requirement (`reference-only`, `edit`, `edit-and-test`, `validation-only`, `release-coordination`, or `unavailable`). For example, a documentation repository might be `edit-and-test`; a production-infrastructure repository may be `reference-only`. The agent must not infer missing permissions. It honors exactly the recorded requirement, as `devspec/protocols/repo-access.xml` defines: an `edit` repository is never validated, and a `release-coordination` one is never even inspected.

## Intake from MCP providers

Use the same `/devspec.story` command for GitHub Issues, Azure DevOps work items, Jira issues, GitLab issues, or another provider. A provider connector is optional: manual text intake continues to work without one. When a connector is available and authenticated, devspec resolves exactly one named URL or identifier with an approved read method, normalizes its reference, and stores a concise redacted snapshot in `story.md`.

The intake command is read-only. It never changes state, fields, assignees, labels, comments, links, or provider records, and a provider write requires a separate explicit request and an approved integration workflow.

On success it shows the provider, identifier, title, type and status when available, canonical link, and short summary, then asks one confirmation question: Confirm and continue, Reject and retry input, Switch to manual intake, Cancel, or Custom Answer — each with an example, and exactly one recommended choice with its justification. After confirmation it asks for the work-item number, offering the date-based value, the resolved provider identifier, and the next value above the highest existing number, each shown as the full proposed folder name. Only then is the folder created.

Intake asks nothing else: it records what the source supplies, lists the remaining requirement gaps in `story.md`, and leaves those questions to `/devspec.refine`. If the reference is ambiguous or unavailable, it asks one clarification or offers explicit manual intake instead of searching broadly or inventing content.

```text
/devspec.story https://github.com/acme/orders/issues/42

/devspec.story JIRA-123

/devspec.story https://dev.azure.com/acme/commerce/_workitems/edit/12345
```

Before enabling an organization connector, record its approved read and write boundaries in `foundation/provider-integrations.md`; never put credentials or tokens in devspec artifacts.

## Command examples

| Command | Use it when | Beginner example |
|---|---|---|
| `devspec.extract` | An existing system needs its first evidence-backed baseline and diagram candidate list. | `/devspec.extract Source scope confirmed: catalog API at D:\Code\catalog-api (primary, read/edit/validate).` After the list is shown, answer `Yes`, `No`, or enter IDs such as `DIA-001, DIA-003`. |
| `devspec.projectcontext` | A new repository needs its product purpose and boundaries. | `/devspec.projectcontext We are creating an internal inventory service for warehouse staff.` |
| `devspec.techstack` | Project context is complete and the team must record its intended stack. | `/devspec.techstack Use .NET 10, PostgreSQL, Docker, and GitHub Actions; no source exists yet.` |
| `devspec.codebase-structure` | The project needs owned areas, integration boundaries, or a custom per-repository layout tree. | `/devspec.codebase-structure Add a Developer-defined layout for the database repository: solution → sqlproj → dbo/Tables, Stored Procedures, and MigrationScripts.` |
| `devspec.coding-standards` | The structure is known and implementation conventions or a numbered example need recording. | `/devspec.coding-standards Add developer-defined CS-018 with EX-007: validate command inputs at the boundary; source: user directive, 2026-09-03; show `ArgumentNullException.ThrowIfNull(input)` before accessing input members.` |
| `devspec.rules` | The new foundation needs enforceable engineering and security rules. | `/devspec.rules Require pull-request review, secret scanning, and OWASP controls with test evidence.` |
| `devspec.story` | One feature, bug, migration, security request, or accessible provider work item needs intake. | `/devspec.story https://github.com/acme/warehouse/issues/42` or `/devspec.story Add CSV export for warehouse stock with manager authorization.` |
| `devspec.refine` | The next step after intake or a change request: the draft needs its behavior, acceptance-criteria, code-area, compatibility, and risk questions asked and answered. | `/devspec.refine Analyze export limits, authorization behavior, and CSV compatibility.` |
| `devspec.finalize` | The active story is complete enough for a readiness and validation plan, or its brief needs correcting before implementation begins. | `/devspec.finalize` |
| `devspec.tasks` | Finalization is ready and implementation work needs ordered tasks. | `/devspec.tasks` |
| `devspec.implement` | Current-revision tasks are ready to change code. | `/devspec.implement` |
| `devspec.review` | Implementation and its recorded validation are complete. | `/devspec.review` |
| `devspec.clarify` | One active material blocker has a recorded question. | `/devspec.clarify The retention period is seven years.` |
| `devspec.changerequest` | A related requirement arrives after finalization. | `/devspec.changerequest Also support JSON export for the same authorized managers.` |
| `devspec.diagram` | A specific architecture or workflow visual needs evidence, including one previously prepared candidate. | `/devspec.diagram DIA-002` for static SVG, or `/devspec.diagram DIA-002 motion=explain` for an evidence-backed animated sequence. |
| `devspec.quickfix` | One localized, low-risk correction has one primary scope. | `/devspec.quickfix Fix the misspelled Orders empty-state label; scope: UI.` |

For `refine`, `finalize`, `tasks`, `implement`, `review`, `clarify`, and `changerequest`, omit an ID only when the current per-worktree context selects the right active work item. Give an explicit ID to switch stories; when several eligible stories exist, select one instead of guessing.

Diagram motion accepts `motion=none|explain` and defaults to `none`. A plain request for an animated diagram maps to `motion=explain`. Animated output remains SVG, is recorded as `svg; motion=explain` in the queue, and must retain complete static and reduced-motion meaning. Add `format=html` separately when a presentation shell is required.
