# Claude Code Adapter

Claude Code support is implemented through project skills under `.claude/skills/devspec-*/SKILL.md`.

## Invocation Model

| Devspec command | Claude skill |
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

- Each skill is a thin wrapper around the canonical command registry.
- Each skill references the matching Copilot prompt and agent files instead of redefining command behavior.
- Dotted command names are preserved as canonical `devspec` vocabulary even when Claude invokes hyphenated skill names.
- Platform limitations belong in `devspec/adapters/compatibility-matrix.md`.

## Validation

Run the new repository, existing repository, story, and cross-tool recovery flows in `devspec/adapters/validation-flows.md` with Claude Code after installing or copying the project skills.
