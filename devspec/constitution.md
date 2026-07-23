# Constitution

This file holds enduring principles that apply across work items and agents. Use it for rare, durable guidance; put operational delivery gates, evolving compliance rules, and enforcement details in `devspec/foundation/rules.md`.

## Durable Principles

| Area | Principle |
| --- | --- |
| Engineering | Prefer simple solutions over speculative abstractions. |
| Engineering | Favor readable, maintainable code over cleverness. |
| Delivery | Keep requirements, implementation, and validation aligned. |
| Delivery | Changes must stay within approved scope. |
| Delivery | Significant scope changes must return to an earlier devspec stage. |
| Validation | Validation is required before work is considered complete. |
| Validation | New behavior should have corresponding validation. |
| Validation | Regressions should be captured in tests when practical. |
| Security and compliance | Do not weaken security controls without explicit approval. |
| Security and compliance | Handle sensitive data according to project and organizational rules. |
| Security and compliance | Validate untrusted input at the first trusted execution boundary; caller or UI validation does not replace authoritative validation. |
| Security and compliance | Enforce authorization at the boundary for protected actions and resources. |
| Security and compliance | Do not expose internal exceptions, secrets, paths, queries, stack traces, or sensitive diagnostics through public errors. |
| Security and compliance | Do not log secrets or sensitive payloads; use safe metadata and correlation identifiers. |
| Reliability | Require evidence-backed resource bounds where variable or untrusted workloads could exhaust storage, memory, compute, or execution time. |

## Amendment Policy

| Rule | Requirement |
| --- | --- |
| Change threshold | Update this file only for durable principles that rarely change. |
| Confirmation | Principle-level changes require explicit confirmation before writing. |
| Operational rules | Put operational delivery gates and evolving compliance rules in `devspec/foundation/rules.md`. |

## Amendment Review

Use this checklist before finalizing any confirmed principle-level change. Keep unresolved follow-ups explicit instead of hiding them in prose.

| Review item | Requirement |
| --- | --- |
| Explicit confirmation | Record the user's confirmation for the specific principle addition, removal, or wording change before writing. |
| Artifact routing | Move operational rules, delivery gates, compliance procedures, enforcement details, and evolving governance requirements to `devspec/foundation/rules.md`. |
| Consistency check | Check affected prompts, agents, templates, adapter guidance, and validation docs for conflicts with the changed principle. |
| Placeholder check | Do not leave unexplained template placeholders or bracketed tokens in live constitution content. |
| Preservation | Preserve existing principles unless the user explicitly confirms replacement or removal. |
| Follow-ups | Record unresolved amendment follow-ups as `TODO(<FIELD_NAME>): <next action>` rows or notes in the affected artifact. |
