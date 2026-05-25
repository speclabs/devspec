# Glossary

Use this file for shared devspec terms and status values.

## Run Status Values

| Status | Meaning |
| --- | --- |
| `active` | Work is in progress. |
| `waiting-for-user` | Work is paused until the user answers a recorded question. |
| `paused` | Work is intentionally paused and can resume from the recorded state. |
| `stopped` | Work stopped without an active resume path. |
| `blocked` | Required evidence, access, or context is missing. |
| `complete` | The stage or run is finished. |

## Work Item Status Values

| Status | Meaning |
| --- | --- |
| `intake` | Initial story capture is in progress. |
| `clarifying` | The item needs user or source clarification. |
| `finalized-not-ready` | Scope is captured but readiness gates are not met. |
| `finalized-ready` | Scope is ready for task planning. |
| `tasks-planned` | Implementation tasks are recorded. |
| `implementing` | Implementation is in progress. |
| `paused` | Work is paused and resumable. |
| `stopped` | Work stopped without an active resume path. |
| `blocked` | Work cannot proceed until a blocker is resolved. |
| `implemented` | Implementation is complete and awaiting review. |
| `reviewing` | Review is in progress. |
| `reviewed` | Review is complete. |

## Task Status Values

| Status | Meaning |
| --- | --- |
| `pending` | Not started. |
| `active` | In progress. |
| `paused` | Paused mid-task. |
| `blocked` | Cannot proceed until a blocker is resolved. |
| `complete` | Finished. |
| `skipped` | Intentionally not performed. |

## Review And Readiness Status Values

| Status | Meaning |
| --- | --- |
| `ready` | Meets readiness gates. |
| `not ready` | Missing required information or approval. |
| `approved` | Review found no required changes. |
| `approved-with-follow-ups` | Review passed with non-blocking follow-ups. |
| `changes-requested` | Review requires implementation changes. |

## Source Resolution Status Values

| Status | Meaning |
| --- | --- |
| `resolved` | External source was found and confirmed. |
| `manual` | User chose manual intake without external resolution. |
| `blocked` | Source resolution is required but unavailable or invalid. |

## Artifact Status Values

| Status | Meaning |
| --- | --- |
| `proposed` | Candidate identified from evidence. |
| `confirmed` | User approved generation. |
| `generated` | Artifact was added to the target path. |
| `skipped` | User declined generation. |
| `blocked` | Evidence or context is insufficient. |

## Access Requirement Values

| Value | Meaning |
| --- | --- |
| `reference-only` | Inspect for context only. |
| `edit` | Code or documentation changes are expected. |
| `edit-and-test` | Changes and validation are expected. |
| `validation-only` | Run validation only. |
| `release-coordination` | Track a delivery dependency; edits need separate confirmation. |
| `blocked` | Required repo is unavailable or inaccessible. |
