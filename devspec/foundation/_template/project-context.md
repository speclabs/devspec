# Project Context

Use this artifact for durable product facts that should shape future work items. Keep it concise and developer-facing. Omit optional rows or sections with no project content.

## Product Overview

| Field | Description | Source | Confidence |
| --- | --- | --- | --- |
| Purpose | <why the product exists> | <user-input-or-source> | confirmed |
| Problem | <user-or-business-problem-being-addressed> | <user-input-or-source> | confirmed |
| Target outcome | <intended-user-or-business-result> | <user-input-or-source> | confirmed |

## Audiences and Stakeholders

| Group | Category | Need or responsibility | Source | Confidence |
| --- | --- | --- | --- | --- |
| <primary-user-group> | user | <need-or-responsibility> | <user-input-or-source> | confirmed |
| <stakeholder-group> | stakeholder | <need-or-responsibility> | <user-input-or-source> | confirmed |

## Outcomes and Scope

Use this section for product goals, explicit scope exclusions, and measurable success signals. Keep operational rules and delivery gates in `rules.md`.

| Type | Outcome, boundary, or metric | Implementation implication | Source | Confidence |
| --- | --- | --- | --- | --- |
| goal | <desired-product-result> | <how-this-should-shape-implementation-decisions> | <user-input-or-source> | confirmed |
| scope exclusion | <explicit-exclusion> | <what-not-to-build-or-optimize-for> | <user-input-or-source> | confirmed |
| success metric | <target-or-signal> | <what to instrument, preserve, or optimize> | <user-input-or-source> | confirmed |

## Delivery Context

Use this section for product or business constraints and unresolved blockers that affect implementation planning. Keep repository location, access, ownership, and path facts in `codebase-structure.md`.

| Type | Context item | Scope | Required handling or next step | Source | Confidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| constraint | <product-or-business-constraint> | <affected-scope> | <required-action-or-limit> | <user-input-or-source> | confirmed | active |
| blocker | <unresolved-blocker-or-question> | <affected-scope> | <next-action-needed> | <user-input-or-source> | confirmed | open |
