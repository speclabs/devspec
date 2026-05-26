---
name: exploration-recovery
description: Reuse known working exploration methods, apply discovery exclusions, and avoid repeating failed discovery or repair paths. Use for discovery-heavy, repeated, or failure-prone work such as repository extraction, provider lookup, dependency or code-pattern mapping, validation discovery, implementation repair, and review investigation.
---

# Exploration Recovery

Use this skill to keep repository and provider discovery focused, cheap, and recoverable. Treat `.github/prompts/PATTERNS.md` as the policy source; this skill is the runtime checklist.

## Checklist

1. Define the current scope and goal before probing.
   - Scope examples: repo path, provider, work item, module, technology, or source URL.
   - Goal examples: repository extraction, provider resolution, dependency mapping, code-pattern search, validation discovery, implementation repair, or review investigation.

2. Apply discovery exclusions before broad search, Explore runs, generated scripts, or helper commands.
   - Read `devspec/foundation/discovery-exclusions.md` when present.
   - If it is missing, use `devspec/foundation/_template/discovery-exclusions.md` as the section contract before creating or updating the live artifact.
   - Apply baseline exclusions and ecosystem discovery rules unless the user asks or a project override includes a normally excluded path.
   - Prefer manifests, lockfiles, framework config, scripts, docs, tests, and owned source roots as evidence.

3. Check reusable exploration state before new probing.
   - Read `devspec/foundation/exploration-state.md` when present.
   - If it is missing, continue without it unless this run produces a reusable method outcome worth preserving.
   - Use `devspec/foundation/_template/exploration-state.md` as the section contract before creating the live artifact.
   - Check session memory only as transient context; Git-tracked devspec artifacts remain canonical.
   - Use `Method Ledger` rows matched by both scope and goal, and ignore stale entries from different contexts.

4. Prefer known working and low-cost methods.
   - Use rows with `working` outcome first when the scope, goal, and environment assumptions still match.
   - Skip rows with `failed` outcome unless the retry condition is met or the user gives new direction.
   - Ignore rows with `superseded` outcome when a newer matching method exists.
   - Prefer targeted search, targeted reads, manifests, devspec artifacts, and configured provider tools before generated scripts or broad scans.
   - Limit each scope and goal to one new generated script, helper command, provider lookup path, or expensive search strategy before falling back to direct search and file reads.

5. Record only reusable results.
   - Update `devspec/foundation/exploration-state.md` only for reusable discoveries, skipped failures that changed the path, or successful fallback paths after a failure.
   - Record scope, goal, method, outcome, evidence or failure reason, retry or reuse condition, last verified date, and brief notes.
   - Do not record every search, one-off read, or expected empty result.

## Reporting

- Mention skipped known failures only when they materially changed the path taken.
- Mention excluded paths only when they prevented a likely expensive scan, changed the evidence gathered, or the user asked for diagnostics.
- Keep final output aligned with the active agent's Output Format and the shared Output Closure Pattern.
