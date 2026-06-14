# Google Antigravity Adapter

Google Antigravity support is implemented through workspace rules under `.agents/rules/` and workspace skills under `.agents/skills/`.

## Invocation Model

| Devspec command | Antigravity skill |
| --- | --- |
| `/devspec.extract` | `/devspec-extract` |
| `/devspec.projectcontext` | `/devspec-projectcontext` |
| `/devspec.techstack` | `/devspec-techstack` |
| `/devspec.codebase-structure` | `/devspec-codebase-structure` |
| `/devspec.coding-standards` | `/devspec-coding-standards` |
| `/devspec.rules` | `/devspec-rules` |
| `/devspec.story` | `/devspec-story` |
| `/devspec.clarify` | `/devspec-clarify` |
| `/devspec.finalize` | `/devspec-finalize` |
| `/devspec.tasks` | `/devspec-tasks` |
| `/devspec.implement` | `/devspec-implement` |
| `/devspec.review` | `/devspec-review` |
| `/devspec.diagram` | `/devspec-diagram` |

## Adapter Rules

- `.agents/rules/devspec-workflow.md` provides always-on workspace guidance.
- `.agents/skills/devspec-*.md` provides command-like wrappers for each canonical command.
- Each skill references `devspec/adapters/command-registry.md` and the matching Copilot prompt and agent files.
- `/devspec.diagram` keeps Mermaid as the default output; pass `format=svg` for SVG-only output or `format=mermaid+svg` for both outputs without creating a separate Antigravity skill.
- Do not add Antigravity workflow files until the target workflow file location and format are confirmed for the team.
- Antigravity artifacts, task lists, and implementation plans are transient helpers; Git-tracked `devspec/` artifacts remain canonical.

## Enterprise Safety

| Area | Guidance |
| --- | --- |
| Rules | Workspace rules live under `.agents/rules/`; keep the devspec rule broad, short, and always on. |
| Skills | Workspace skills live under `.agents/skills/` and become slash-invokable command wrappers. |
| Permissions | Prefer Ask or Request Review for terminal commands, browser actions, MCP calls, non-workspace file access, and artifact application. |
| Strict mode | Use strict mode or equivalent review posture for regulated, security-sensitive, or unfamiliar repositories. |
| Sandboxing | Enable terminal sandboxing where available; deny network access unless the workflow requires it. |
| Project boundaries | Keep projects scoped to the repositories recorded in `devspec/foundation/codebase-structure.md`. |
| Artifact review | Treat Antigravity implementation plans and code diffs as review surfaces; canonical completion evidence still belongs in `devspec` artifacts. |
| Secrets | Keep credentials, tokens, local settings, and provider secrets outside rules, skills, prompts, and artifacts. |

## Known Gaps

- Exact `/devspec.*` slash parity is not assumed; Antigravity skills use `/devspec-story` style names.
- Antigravity workflows are intentionally not shipped until their workspace file contract is confirmed for the target environment.
- Permission, sandbox, project, and artifact-review behavior depends on the user's Antigravity project settings.

## Validation

Run the new repository, existing repository, story, and cross-tool recovery flows in `devspec/adapters/validation-flows.md` with Antigravity before treating the adapter as enterprise-ready.
