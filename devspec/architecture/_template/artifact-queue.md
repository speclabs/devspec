# Architecture Artifact Queue

One row per diagram candidate. `Duplicate check` records what was compared and the result, so a later run does not regenerate an existing diagram. `Next` is the one action left for that row, or `none` when it is complete.

| ID | Scope | Type | Subject | Output | Evidence | Duplicate check | Status | Next |
|---|---|---|---|---|---|---|---|---|
