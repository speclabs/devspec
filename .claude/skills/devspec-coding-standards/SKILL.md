---
name: devspec-coding-standards
description: Run /devspec.coding-standards using the canonical devspec command registry. Supports mono-repo and multi-repo workspaces. Works across GitHub Copilot, Claude Code, OpenAI Codex, Cursor, and other AI agents.
---

Execute canonical command `/devspec.coding-standards`.

1. Read `AGENTS.md` for canonical workflow, no-intent-drift, cross-tool recovery, and structured question rules.
2. Read `devspec/adapters/command-registry.md` for this command's required input, outputs, mutation level, and next handoff.
3. Read `.github/prompts/devspec.coding-standards.prompt.md` and `.github/agents/devspec.coding-standards.agent.md` as the authoritative source of command intent and behavior.
4. Apply `.github/prompts/PATTERNS.md` for shared behavior: interactive questions, prerequisite validation, session recovery, discovery exclusions, and output closure.
5. Honor multi-repo boundaries: when `devspec/foundation/codebase-structure.md` records multiple repositories, every task, artifact, and access requirement must name the target repository.

Command input comes from the user's current message.

Platform note: Claude Code may not register `/devspec.coding-standards` as a native slash command. Treat the command name as workflow intent and use this skill as the invocation mechanism. Record any unsupported behavior in `devspec/adapters/compatibility-matrix.md`.
