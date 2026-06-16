---
name: devspec-extract
description: Run /devspec.extract using the canonical devspec command registry. Backfills foundation and architecture artifacts from local paths, GitHub, Azure DevOps, GitLab, or named multi-repo sources. Works across GitHub Copilot, Claude Code, OpenAI Codex, Cursor, and other AI agents.
---

Execute canonical command `/devspec.extract`.

1. Read `AGENTS.md` for canonical workflow, no-intent-drift, cross-tool recovery, and structured question rules.
2. Read `devspec/adapters/command-registry.md` for this command's required input, outputs, mutation level, and next handoff.
3. Read `.github/prompts/devspec.extract.prompt.md` and `.github/agents/devspec.extract.agent.md` as the authoritative source of command intent and behavior.
4. Apply `.github/prompts/PATTERNS.md` for shared behavior: interactive questions, prerequisite validation, session recovery, output closure, and specifically `PATTERNS.md#discovery-exclusion-pattern`, `PATTERNS.md#diagram-extraction-consistency-pattern`, `PATTERNS.md#svg-output-pattern`, and `PATTERNS.md#process-flow-extraction-pattern`. Do not queue diagram families listed in `PATTERNS.md#excluded-diagram-families` (such as `architecture-beta`) when seeding `devspec/architecture/artifact-queue.md`; use the documented portable alternative instead.
5. Preserve `format=svg` and `format=mermaid+svg` as diagram generation preferences in queue notes. Extraction remains queue-first and may generate at most one approved diagram artifact set only after the canonical approval gate.
6. For multi-repo extraction: process each repository source in sequence, apply discovery exclusions from `devspec/foundation/discovery-exclusions.md`, record per-repo evidence and status in `devspec/foundation/extraction-state.md`, and seed diagram candidates per-repo in `devspec/architecture/artifact-queue.md`.

Command input comes from the user's current message.

Platform note: Claude Code may not register `/devspec.extract` as a native slash command. Treat the command name as workflow intent and use this skill as the invocation mechanism. Record any unsupported behavior in `devspec/adapters/compatibility-matrix.md`.
