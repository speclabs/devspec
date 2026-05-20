---
name: exploration-recovery
description: Reuse known working exploration methods, apply discovery exclusions, and avoid repeating failed searches, scripts, provider lookups, validation probes, extraction attempts, or repair paths. Use when agents search, inspect, extract, resolve external references, map dependencies, discover code patterns, or run exploratory commands.
---

# Exploration Recovery

Reduce repeated token, CPU, and tool cost during repository or provider discovery.

## Workflow

1. Define the current scope and goal before probing.
   - Scope examples: repo path, provider name, work item, module, technology, source URL.
   - Goal examples: repository extraction, provider resolution, code pattern search, dependency mapping, implementation repair, version lookup, validation discovery.

2. Apply exclusions before broad search or helper scripts.
   - Read `devspec/foundation/discovery-exclusions.md` when present.
   - Exclude dependency, generated, cache, coverage, build-output, VCS, and tool-output paths.
   - For Node.js, Angular, React, Next, and Vite, use manifests, lockfiles, and framework config as dependency evidence instead of `node_modules/` or generated output.
   - Respect repo ignore files, but keep explicit exclusions for tools that may not honor them.
   - Inspect excluded folders only when the user asks or a project override marks them source-owned.

3. Check reusable exploration state before broad probing.
   - Read `devspec/foundation/exploration-state.md` when present.
   - Check session memory when available.
   - Match by both scope and goal. Do not apply a stale failure from a different context.

4. Use known working methods first.
   - Prefer recorded working methods when scope, goal, and environment assumptions still match.
   - Mention the fast path briefly when reporting results.

5. Skip known failed methods unless retry conditions are met.
   - Retry only when input, environment, credentials, dependencies, access, path, or command changed.
   - If unsure, prefer a different lower-cost path instead of replaying the failure.

6. Prefer cheap targeted discovery before expensive probing.
   - Use search, targeted file reads, manifests, devspec artifacts, and configured provider tools before generating broad helper scripts.
   - Limit each scope/goal to one new generated script, helper command, provider lookup path, or expensive search strategy before falling back to direct search and file reads.

7. Record meaningful results.
   - When a fallback succeeds after a failure, update `devspec/foundation/exploration-state.md`.
   - Record reusable discoveries only: scope, goal, failed method, failure reason, working method, last verified date, and retry condition.

## Exclusion Policy

Use this structure when `devspec/foundation/discovery-exclusions.md` is missing:

```md
# Discovery Exclusions

## Global

| Pattern | Reason | Retry or include only if |
| --- | --- | --- |
| `.git/` | VCS internals | User asks for Git internals |
| `dist/`, `build/`, `out/` | Generated output | Output is source-owned or explicitly requested |
| `coverage/` | Test output | User asks for coverage artifacts |

## Ecosystems

| Ecosystem or framework | Detect from | Exclude by default | Prefer as evidence |
| --- | --- | --- | --- |
| Node.js, Angular, React, Next, Vite | `package.json`, lockfiles, framework config | `node_modules/`, `.angular/`, `.next/`, `.turbo/`, `.vite/`, `dist/`, `build/`, `coverage/` | manifests, lockfiles, config |
```

## State Format

Use this structure when `devspec/foundation/exploration-state.md` is missing:

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

Mention skipped known failures only when relevant:

```md
Skipped known failed methods:
- Scope: <scope>; goal: <goal>; skipped: <method>; reason: <retry condition not met>.
```

Mention excluded paths only when they materially changed discovery, prevented a likely expensive scan, or the user asked for diagnostics.
