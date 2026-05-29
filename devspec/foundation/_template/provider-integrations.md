# Provider Integrations

Use this policy for external work-item resolution during `devspec.story`. Keep provider-specific access behind MCP servers or equivalent integration tools, and allow manual intake only as an explicit fallback when provider resolution is unavailable or intentionally skipped.

## Resolution Policy

| Policy area | Requirement |
| --- | --- |
| Workflow boundary | Keep the work-item intake workflow provider-agnostic; provider-specific lookup belongs in integration tools. |
| Resolution preference | Prefer exact provider URLs or provider-qualified identifiers over inferred matches. |
| Ambiguity handling | Ask one clarification question before resolving an ambiguous provider or identifier. |
| Manual fallback | Use manual intake only when external resolution is unavailable and the user explicitly chooses to proceed. |
| Work-item creation gate | Do not create or update the work-item folder from provider input until the resolved item is shown and explicitly confirmed. |
| Secret handling | Keep provider authentication, credentials, and secrets outside prompt artifacts. |

## Supported Provider Inputs

| Provider | Preferred input | Accepted shorthand | Validation guardrail |
| --- | --- | --- | --- |
| GitHub | Full issue URL or supported pull request URL | `owner/repo#123` | Reject bare numbers unless repository context is configured. |
| Jira | Full issue URL | Issue key such as `ABC-123` | Reject malformed keys or keys outside configured project patterns. |
| Azure DevOps | Full work item URL | Numeric ID only with configured organization and project context | Reject numeric IDs when organization or project context is missing. |

## Resolution Flow and Outcomes

Resolve inputs in this order:

| Order | Input path | Required handling |
| --- | --- | --- |
| 1 | Full provider URL | Validate format, resolve through the configured provider tool, and request confirmation on success. |
| 2 | Provider-qualified identifier | Validate provider context, resolve through the configured provider tool, and request confirmation on success. |
| 3 | Ambiguous identifier | Ask for provider clarification before lookup. |
| 4 | Manual intake | Continue only after the user explicitly chooses manual intake and supplies required manual fields. |

Handle outcomes as follows:

| Condition | Required handling |
| --- | --- |
| Invalid input format | Stop intake and explain why the input is invalid. |
| Ambiguous provider | Ask one clarification question to identify the provider. |
| Known provider cannot resolve item | Stop intake and classify the failure as not found, access denied, or integration unavailable when possible. |
| Integration unavailable | Offer manual intake as an explicit fallback. |
| Provider resolution succeeds | Show the confirmation summary and require explicit user confirmation before creating or updating the work-item folder. |
| Unverified provider input | Do not create a normal resolved work item. |

## Confirmation Requirements

Show this minimum summary when provider resolution succeeds:

| Field | Required |
| --- | --- |
| Provider | yes |
| Identifier | yes |
| Title | yes |
| Type | when available |
| Current external status | when available |
| Canonical link | yes |
| Short summary | yes |

Offer only these confirmation actions:

| Action | Result |
| --- | --- |
| Confirm and continue | Continue normal resolved intake. |
| Reject and retry input | Ask for a corrected source. |
| Switch to manual intake | Continue only with manual intake requirements. |
| Cancel | Stop intake. |
| Custom Answer | Route to clarification; do not create or update the work-item folder until resolved. |

## Integration Tooling and Access

| Area | Requirement |
| --- | --- |
| Tooling model | Use one MCP server per provider or one internal MCP server that wraps multiple providers. |
| Lookup tools | Validate and fetch work items by URL or provider-specific identifier. |
| Returned data | Include title, description, status, labels or type, links, and relevant metadata. |
| Failure detail | Distinguish not found, unauthorized, malformed input, and transient provider failures. |
| Authentication configuration | Keep provider authentication outside prompt artifacts. |
| Privilege model | Use least-privilege tokens or service identities. |
| Access mode | Prefer read-only access for intake and review unless write-back is required. |

## Work-Item Intake Recording Requirements

| Recording area | Requirement |
| --- | --- |
| Source resolution status | Record a value from `devspec/glossary.md#source-resolution-status-values` in `meta.md`. |
| Lookup attempt | Record provider and resolution notes. |
| Manual status | Use only when the user explicitly chooses to continue without external resolution. |
| Manual intake | Require external reference, manual description, and manual acceptance criteria. |
| Resolved items | Require explicit user confirmation after showing resolved details. |
| Blocked status | Use when input is invalid or required resolution failed. |
| Confirmation result | Record it in `meta.md` and record the shown summary in `story.md`. |
| Provider policy ownership | Keep provider-specific details here instead of duplicating them across prompt files. |
| Maintenance trigger | Update this file when provider formats, supported tools, authentication expectations, or fallback policy changes. |
