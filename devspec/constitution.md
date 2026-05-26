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

## Amendment Policy

| Rule | Requirement |
| --- | --- |
| Change threshold | Update this file only for durable principles that rarely change. |
| Confirmation | Principle-level changes require explicit confirmation before writing. |
| Operational rules | Put operational delivery gates and evolving compliance rules in `devspec/foundation/rules.md`. |
