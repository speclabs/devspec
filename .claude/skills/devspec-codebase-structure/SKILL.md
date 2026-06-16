---
name: devspec-codebase-structure
description: Run /devspec.codebase-structure using the canonical devspec command registry. Supports mono-repo and multi-repo workspaces. Works across GitHub Copilot, Claude Code, OpenAI Codex, Cursor, and other AI agents.
---

Execute canonical command `/devspec.codebase-structure`.

1. Read `AGENTS.md` for canonical workflow, no-intent-drift, cross-tool recovery, and structured question rules.
2. Read `devspec/adapters/command-registry.md` for this command's required input, outputs, mutation level, and next handoff.
3. Read `.github/prompts/devspec.codebase-structure.prompt.md` and `.github/agents/devspec.codebase-structure.agent.md` as the authoritative source of command intent and behavior.
4. Apply `.github/prompts/PATTERNS.md` for shared behavior: interactive questions, prerequisite validation, session recovery, discovery exclusions, and output closure.
5. Honor multi-repo boundaries: when recording multiple repositories, capture per-repo work areas, boundaries, integration contracts, and access requirements as separate entries in `devspec/foundation/codebase-structure.md`.

Command input comes from the user's current message.

Platform note: Claude Code may not register `/devspec.codebase-structure` as a native slash command. Treat the command name as workflow intent and use this skill as the invocation mechanism. Record any unsupported behavior in `devspec/adapters/compatibility-matrix.md`.
