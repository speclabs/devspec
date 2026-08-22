# Devspec Gemini Instructions

Use this file as Gemini CLI and Gemini-backed agent context for this repository.

@./AGENTS.md

## Gemini Adapter Rules

- Treat `AGENTS.md` as the shared cross-agent baseline.
- Treat `devspec/adapters/command-registry.md` as the canonical command registry.
- Treat `.github/prompts/*.prompt.md` and `.github/agents/*.agent.md` as the protected reference implementation.
- Preserve canonical `/devspec.*` command vocabulary even when Gemini CLI invokes native commands such as `/devspec:story`.
- Recover from Git-tracked `devspec/` artifacts before relying on Gemini session memory.
- Preserve structured question behavior from `.github/prompts/PATTERNS.md#interactive-question-pattern`: show interactive multiple-choice options when Gemini can render them, otherwise render the identical options as text; include an example for every option and `Custom Answer`; ask one question at a time; and preserve the recommendation with its justification.
- Do not store credentials, API keys, tokens, personal settings, or provider secrets in Gemini context, commands, or artifacts.

## Native Gemini Commands

Gemini CLI project commands live under `.gemini/commands/devspec/`.

| Canonical command | Gemini CLI command |
| --- | --- |
| `/devspec.extract` | `/devspec:extract` |
| `/devspec.projectcontext` | `/devspec:projectcontext` |
| `/devspec.techstack` | `/devspec:techstack` |
| `/devspec.codebase-structure` | `/devspec:codebase-structure` |
| `/devspec.coding-standards` | `/devspec:coding-standards` |
| `/devspec.rules` | `/devspec:rules` |
| `/devspec.story` | `/devspec:story` |
| `/devspec.clarify` | `/devspec:clarify` |
| `/devspec.finalize` | `/devspec:finalize` |
| `/devspec.tasks` | `/devspec:tasks` |
| `/devspec.implement` | `/devspec:implement` |
| `/devspec.review` | `/devspec:review` |
| `/devspec.diagram` | `/devspec:diagram` |
