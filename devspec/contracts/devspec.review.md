# devspec.review

Review changed work against readiness, tasks, and validation evidence.

Invocation: `/devspec.review [work-item-id]`

<workflow command="devspec.review">
  <purpose>Review changed work against readiness, tasks, and validation evidence.</purpose>
  <protocols>
    <protocol ref="ask" queue="single-blocker" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
    <protocol ref="security" />
  </protocols>
  <scope>Use to judge completed implementation against the current scope revision's approved scope and recorded evidence. This command records findings; devspec.implement applies them.</scope>
  <input>An optional work-item ID with finalization, tasks, implementation record, and changed work.</input>
  <rules>
    <rule>Read only the changed-work baseline's changed paths and their direct callers, the current-revision finalization, tasks, and implementation records, and the canonical rules those records cite. Do not re-review unchanged code or unrelated work items.</rule>
    <rule>Compare changed work to approved scope, task source coverage, finalization foundation and architecture traces, validation evidence, and every applicable accepted material decision or canonical rule.</rule>
    <rule>Verify the work against every protocol this work item loaded, and report a violation as a finding: evidence labels and changed-work baseline from state, revision currency from revision, scope and change discipline from work, access boundaries from repo-access, and the security gate from security.</rule>
    <rule>Check changed source against the shared work protocol for duplicated capabilities, unjustified dependencies, speculative abstractions, and unused configuration. Evaluate the choices against approved requirements, project conventions, and any recorded justification.</rule>
    <rule>Record actionable complexity findings in the existing Findings table with the location, supporting evidence, and a suitable simpler alternative or removal that preserves required behavior and safeguards.</rule>
    <rule>Require rework for demonstrated violations of approved scope or the shared implementation rule. Do not block acceptance solely because a different stylistic implementation is shorter.</rule>
    <rule>Record each decision or rule verification as implemented-as-decided, intentionally-superseded with a recorded replacement, or not-verified. Treat an unrecorded contradiction as rework-required. A not-verified entry blocks acceptance: record it as a finding with what evidence is missing, and return rework-required, or blocked when the missing evidence needs a developer decision.</rule>
    <rule>A judgment this command cannot make from the recorded evidence becomes a finding or one blocker, never an interactive question to the developer.</rule>
    <rule>Write findings only; do not silently edit implementation code. On rework-required, set only the tasks a finding names to `rework` in tasks.md and leave every other task complete; name those task IDs in the review record.</rule>
    <rule>Record exactly one outcome: accepted, rework-required, or blocked; record exactly one next action.</rule>
  </rules>
  <entry>Active work item at review with complete implementation and matching finalization and task records for the current scope revision; reject an unknown changed-work baseline.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/review.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="accepted" stage="complete" run="complete" next="none" />
    <transition outcome="rework-required" stage="implementation" run="active" next="devspec.implement" />
    <transition outcome="blocked" stage="review" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Verify the recorded changed-work baseline. Accepted is terminal and clears current-work-item context; rework returns only affected tasks to implementation and blocked work preserves context.</closure>
</workflow>
