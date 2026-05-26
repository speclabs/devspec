# Exploration State

Use this file to avoid repeating failed searches, generated scripts, helper commands, provider lookups, validation discovery paths, and repair probes. Record only reusable exploration results, not every search or one-off file read.

Apply `devspec/foundation/discovery-exclusions.md` before recording or reusing exploration methods.

Keep entries concise and evidence-based. Scope must be specific enough to prevent false matches, such as a repo path, provider name, work item, module, technology, or source URL. Goal must describe the exploration task, such as repository extraction, provider resolution, dependency mapping, implementation repair, version lookup, or validation discovery. Remove or update stale entries when the environment changes.

## Method Ledger

Use this as the single recovery view for reusable exploration methods. Prefer `working` methods first when scope, goal, and assumptions still match. Skip `failed` methods unless the retry condition is met, the user gives new direction, or the method materially changes. Use `superseded` when a better working method replaces an older entry.

| Scope | Goal | Method | Outcome | Evidence or failure reason | Retry or reuse condition | Last verified | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <repo-provider-work-item-module-or-technology> | <repository-extraction-provider-resolution-dependency-mapping-repair-version-lookup-or-validation-discovery> | <search-command-provider-tool-or-process> | working, failed, superseded | <why-it-worked-or-failed> | <when-to-reuse-or-retry> | <date-or-unknown> | <brief-context> |
