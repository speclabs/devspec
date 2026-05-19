---
name: exploration-recovery
description: Reuse known working exploration methods, apply repository discovery exclusions, and avoid repeated failed searches, generated scripts, helper commands, provider lookups, validation discovery, extraction attempts, or repair probes. Use when agents need to search, explore, extract, inspect, resolve external references, discover code patterns, map dependencies, or run exploratory commands in a repository or multi-repo workspace.
---

# Exploration Recovery

Use this skill to reduce repeated token, CPU, and tool cost during discovery.

## Workflow

1. Define the current scope and goal before probing.
   - Scope examples: repo path, provider name, work item, module, technology, source URL.
   - Goal examples: repository extraction, provider resolution, code pattern search, dependency mapping, implementation repair, version lookup, validation discovery.

2. Apply discovery exclusions before broad search or helper scripts.
   - Read `devspec/foundation/discovery-exclusions.md` when it exists.
   - Exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output paths by default.
   - For Node.js, Angular, React, Next, and Vite, exclude `node_modules/`, `.angular/`, `.next/`, `.turbo/`, `.vite/`, `dist/`, `build/`, and `coverage/`.
   - Use manifests, lockfiles, and framework config files as dependency evidence instead of installed dependency folders.
   - Respect repository ignore files as a baseline, but still apply explicit exclusions when search or script tools may not honor them.
   - Inspect excluded folders only when the user explicitly asks or a project override records that the path is source-owned.

3. Check durable and transient state before running broad exploration.
   - Read `devspec/foundation/exploration-state.md` when it exists.
   - Check session memory when available.
   - Match by both scope and goal; do not over-apply a stale failure from a different context.

4. Use known working methods first.
   - Prefer the recorded working method when scope, goal, and environment assumptions still match.
   - Mention the fast path briefly when reporting results.

5. Skip known failed methods unless retry conditions are met.
   - Retry only when the input changed, environment changed, credentials changed, dependencies were installed, network/access was restored, the path was corrected, or the command was updated.
   - If unsure, prefer a different lower-cost path instead of replaying the failure.

6. Prefer cheap targeted discovery before expensive probing.
   - Use repository search, targeted file reads, manifests, existing devspec artifacts, and configured provider tools before generating broad helper scripts.
   - Limit each scope/goal to one new generated script, helper command, provider lookup path, or expensive search strategy before falling back to direct search/read evidence gathering.

7. Record meaningful results.
   - When a fallback succeeds after a failure, update `devspec/foundation/exploration-state.md`.
   - Record only reusable discoveries, not every small search.
   - Include scope, goal, failed method, failure reason, working method, last verified date, and retry condition.

## Exclusion Policy

Use this structure when the project has no existing discovery-exclusions file:

```md
# Discovery Exclusions

## Global Exclusions

| Pattern | Reason | Retry or include only if |
| --- | --- | --- |
| `.git/` | VCS internals | User asks for Git internals |
| `dist/`, `build/`, `out/` | Generated output | Output is source-owned |
| `coverage/` | Test output | User asks for coverage artifacts |

## Ecosystem Exclusions

| Ecosystem or framework | Detect from | Exclude by default | Prefer as evidence |
| --- | --- | --- | --- |
| Node.js, Angular, React, Next, Vite | `package.json`, lockfiles, framework config | `node_modules/`, `.angular/`, `.next/`, `.turbo/`, `.vite/`, `dist/`, `build/`, `coverage/` | manifests, lockfiles, config |
```

## State Format

Use this structure when the project has no existing exploration-state file:

```md
# Exploration State

## Known Working Methods

| Scope | Goal | Working method | Last verified | Notes |
| --- | --- | --- | --- | --- |

## Known Failed Methods

| Scope | Goal | Failed method | Failure reason | Retry only if |
| --- | --- | --- | --- | --- |
```

## Reporting

Include skipped known failures in the final result when relevant. Keep it short:

```md
Skipped known failed methods:
- Scope: <scope>; goal: <goal>; skipped: <method>; reason: <retry condition not met>.
```

Mention excluded paths only when they materially changed discovery, prevented a likely expensive scan, or the user asked for diagnostics.
