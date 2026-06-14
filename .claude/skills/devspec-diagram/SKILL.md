---
name: devspec-diagram
description: Run /devspec.diagram using the canonical devspec command registry. Generates evidence-backed Mermaid diagrams for architecture, workflows, journeys, sequences, states, timelines, and planning views. Supports mono-repo and multi-repo workspaces. Works across GitHub Copilot, Claude Code, OpenAI Codex, Cursor, and other AI agents.
---

Execute canonical command `/devspec.diagram`.

1. Read `AGENTS.md` for canonical workflow, no-intent-drift, cross-tool recovery, and structured question rules.
2. Read `devspec/adapters/command-registry.md` for this command's required input, outputs, mutation level, and next handoff.
3. Read `.github/prompts/devspec.diagram.prompt.md` and `.github/agents/devspec.diagram.agent.md` as the authoritative source of command intent and behavior.
4. Apply `.github/prompts/PATTERNS.md` for shared behavior: interactive questions, prerequisite validation, session recovery, discovery exclusions, and output closure — including `PATTERNS.md#diagram-extraction-consistency-pattern`, `PATTERNS.md#mermaid-internal-naming-and-readability-pattern`, `PATTERNS.md#mermaid-visual-quality-pattern`, `PATTERNS.md#process-flow-extraction-pattern`, and `PATTERNS.md#excluded-diagram-families`.
5. For every generated `flowchart` or `stateDiagram-v2`: open with the dark theme init block, declare the semantic `classDef` palette for roles present, use role-appropriate node shapes, wrap boundaries of 3+ nodes in named `subgraph` blocks, draw cross-subgraph arrows after all `end` keywords, assign `classDef` classes in a batch block at the end, and verify node count stays within complexity guardrails. Never use an excluded family such as `architecture-beta`; substitute the documented portable alternative.
6. Honor multi-repo boundaries: when `devspec/foundation/codebase-structure.md` records multiple repositories, scope diagram evidence to the correct repository boundary.

Command input comes from the user's current message.

Platform note: Claude Code may not register `/devspec.diagram` as a native slash command. Treat the command name as workflow intent and use this skill as the invocation mechanism. Record any unsupported behavior in `devspec/adapters/compatibility-matrix.md`.
