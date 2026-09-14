# Command Registry

Purpose and next route are the contract's own `<purpose>` and `<transition next>` values. Change the contract, not this table.

| Command | Purpose | Next route |
|---|---|---|
| `devspec.extract` | Inspect the approved existing system end-to-end, produce its technical, business, workflow, and rule baseline, and prepare an evidence-backed diagram candidate list for explicit generation approval. | `devspec.story`, `devspec.clarify` |
| `devspec.projectcontext` | Capture product purpose, users, outcomes, and scope boundaries. | `devspec.techstack`, `return-to-caller`, `devspec.clarify` |
| `devspec.techstack` | Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints. | `devspec.codebase-structure`, `return-to-caller`, `devspec.clarify` |
| `devspec.codebase-structure` | Capture or customize owned source roots, repository layouts, module boundaries, integrations, and repository access. | `devspec.coding-standards`, `return-to-caller`, `devspec.clarify` |
| `devspec.coding-standards` | Capture concise, reusable coding conventions, followable examples, and anti-patterns from source evidence or developer-defined standards. | `devspec.rules`, `return-to-caller`, `devspec.clarify` |
| `devspec.rules` | Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules. | `devspec.story`, `return-to-caller`, `devspec.clarify` |
| `devspec.story` | Create one concise work-item intake from a request or provider reference. | `devspec.refine`, `devspec.clarify` |
| `devspec.refine` | Make one draft story buildable through scoped review and material questions. | `devspec.finalize`, `devspec.clarify` |
| `devspec.clarify` | Resolve one active blocker and resume its originating stage. | `resume-origin` |
| `devspec.changerequest` | Append one related post-finalization requirement without rewriting history. | `devspec.refine` |
| `devspec.finalize` | Produce a concise readiness brief and validation plan. | `devspec.tasks`, `devspec.refine`, `devspec.clarify` |
| `devspec.tasks` | Create ordered, independently verifiable implementation tasks. | `devspec.implement`, `devspec.clarify` |
| `devspec.implement` | Implement pending ready tasks with focused checkpoints and validation. | `devspec.review`, `devspec.clarify` |
| `devspec.review` | Review changed work against readiness, tasks, and validation evidence. | `none`, `devspec.implement`, `devspec.clarify` |
| `devspec.diagram` | Create one evidence-backed diagram with duplicate checks and durable queue state. | `return-to-caller`, `devspec.clarify`, `none` |
| `devspec.quickfix` | Implement and validate one localized, low-risk enhancement or bug fix. | `none`, `devspec.clarify`, `devspec.story` |

Work-item IDs are optional for `refine`, `finalize`, `tasks`, `implement`, `review`, `clarify`, and `changerequest`. Without an ID, resolve the private per-worktree current context and run only the work item's recorded `next` action. Use an explicit ID to switch stories; when several eligible work items exist, ask the developer to choose.
