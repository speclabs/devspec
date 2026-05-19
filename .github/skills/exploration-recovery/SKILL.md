---
name: exploration-recovery
description: Reuse known working exploration methods and avoid repeated failed searches, generated scripts, helper commands, provider lookups, validation discovery, extraction attempts, or repair probes. Use when agents need to search, explore, extract, inspect, resolve external references, discover code patterns, map dependencies, or run exploratory commands in a repository or multi-repo workspace.
---

# Exploration Recovery

Use this skill to reduce repeated token, CPU, and tool cost during discovery.

## Workflow

1. Define the current scope and goal before probing.
   - Scope examples: repo path, provider name, work item, module, technology, source URL.
   - Goal examples: repository extraction, provider resolution, code pattern search, dependency mapping, implementation repair, version lookup, validation discovery.

2. Check durable and transient state before running broad exploration.
   - Read `devspec/foundation/exploration-state.md` when it exists.
   - Check session memory when available.
   - Match by both scope and goal; do not over-apply a stale failure from a different context.

3. Use known working methods first.
   - Prefer the recorded working method when scope, goal, and environment assumptions still match.
   - Mention the fast path briefly when reporting results.

4. Skip known failed methods unless retry conditions are met.
   - Retry only when the input changed, environment changed, credentials changed, dependencies were installed, network/access was restored, the path was corrected, or the command was updated.
   - If unsure, prefer a different lower-cost path instead of replaying the failure.

5. Prefer cheap targeted discovery before expensive probing.
   - Use repository search, targeted file reads, manifests, existing devspec artifacts, and configured provider tools before generating broad helper scripts.
   - Limit each scope/goal to one new generated script, helper command, provider lookup path, or expensive search strategy before falling back to direct search/read evidence gathering.

6. Record meaningful results.
   - When a fallback succeeds after a failure, update `devspec/foundation/exploration-state.md`.
   - Record only reusable discoveries, not every small search.
   - Include scope, goal, failed method, failure reason, working method, last verified date, and retry condition.

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
