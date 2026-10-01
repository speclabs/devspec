# Glossary

Run states, work-item and quickfix stages, task statuses, evidence labels, the changed-work baseline, and resume semantics are defined once in `devspec/protocols/state.xml`. `devspec/lifecycle.md` owns the route graph. This file covers the remaining terms.

- Scope revision: a monotonic work-item number identifying which generation of approved scope a record belongs to. `devspec/protocols/revision.xml` owns its rules.
- Current work-item context: a private, per-worktree Git-metadata selection used to resolve an omitted work-item ID. It is never a Git-tracked artifact and never replaces `meta.md` as canonical state.
- Material question: a question whose answer can change implementation, validation, or scope. Only material questions enter the ask queue; anything else is decided without asking.
- Material decision: the recorded answer to a material question, held in the command's decision record.
- Material blocker: a material question that must be answered before the command can continue. It sets run state `blocked` and makes `devspec.clarify` the next command. Exactly one may be active at a time.
- Developer: the person the agent asks. Every interactive question in this framework is addressed to the developer; the agent never answers its own material question.
- Registered next action: the single next command recorded in the state record. A command reports exactly one, and `none` is a valid registered next action for terminal work.
- OWASP exception: a reviewer-confirmed false-positive or not-applicable finding supported by enforceable evidence; it is distinct from an unresolved vulnerability. `devspec/protocols/security.xml` owns its confirmation rules.

## Repository access requirements

| Value | Meaning |
|---|---|
| `reference-only` | Read repository content as evidence only; do not edit or validate it. |
| `edit` | Read and edit approved repository files; do not run validation there. |
| `edit-and-test` | Read and edit approved repository files and run approved validations. |
| `validation-only` | Read required files and run approved validations; do not edit repository files. |
| `release-coordination` | Coordinate release information only; do not inspect, edit, or validate repository contents. |
| `unavailable` | The repository cannot currently be accessed; record the impact as a blocker. |

These lowercase values are the recorded form. `devspec/protocols/repo-access.xml` owns how they are collected, recommended, recorded, and enforced.
