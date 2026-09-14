# devspec.finalize

Produce a concise readiness brief and validation plan.

Invocation: `/devspec.finalize [work-item-id]`

<workflow command="devspec.finalize">
  <purpose>Produce a concise readiness brief and validation plan.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="security" />
  </protocols>
  <scope>Use to decide whether the current scope revision is buildable and to record its brief and validation plan. This command plans readiness only; devspec.refine owns requirements, devspec.tasks sequences the work, and devspec.implement changes code.</scope>
  <input>An optional work-item ID or a refined current draft.</input>
  <rules>
    <rule>Read only the current-revision story and decisions, the code areas story.md's Affected Areas table records and their direct interfaces, the current-revision task statuses when a correction is requested from the tasks stage, the finalization traces' direct sources in coding standards, codebase structure, rules, workflow rules, constitution, and the architecture queue or overview. Do not scan unrelated work items, code areas the Affected Areas table does not record, or historical revisions beyond the superseded sections of this work item. At a tasks-stage correction of a story that predates the Affected Areas table, read the areas the current brief names instead.</rule>
    <rule>devspec.refine owns every requirement question; ask none. At the finalization stage, check story.md's Open Requirement Gaps table before any other reading. Return the work item to devspec.refine when an entry is neither resolved nor explicitly skipped with its reason, or when the readiness check exposes a requirement gap: a missing behavior, criterion, edge case, compatibility requirement, or behavior-changing constraint, or an area the brief needs that the Affected Areas table does not record. Append each exposed gap to that table as raised by devspec.finalize before returning. This is a routing outcome, not a blocker: write no ready brief, leave `finalized_revision` unchanged, and record the open gap IDs in meta.md `last`.</rule>
    <rule>Check only material readiness gaps, judging buildability and verifiability rather than re-deriving requirements. Build on what devspec.refine recorded and own the design and the proof: for data and integration, the schemas, migrations, contracts, and rollout order; for validation, the plan and evidence for each acceptance criterion; handling for the edge cases story.md records, and only those; the rollout and compatibility plan for the compatibility story.md requires; and foundation trace entries for the recorded technical constraints. A missing refine-owned item is a requirement gap for devspec.refine, never a design decision this command makes silently. Security, compliance, and delivery constraints are this command's own, and the security protocol's gate applies here rather than in refinement.</rule>
    <rule>Run the ask protocol's discovery only across this command's own topics: security, compliance, and delivery constraints, the buildability of the recorded scope, and the confirmation the security protocol requires for each suspected false-positive or not-applicable finding. Ask them one at a time, resolve each answer into finalize.md or decisions.md, and record a material blocker for devspec.clarify only when the developer cannot answer yet.</rule>
    <rule>Mark ready only when no remaining gap can materially change implementation or validation. Record every gap judged immaterial in the brief's Assumptions and Open Items section with its basis, impact if wrong, and status, rather than discarding it. Reference a gap devspec.refine skipped by its Open Requirement Gaps ID instead of restating or re-judging it; when that skipped gap turns out to change buildability, append a new entry that cites it, raised by devspec.finalize, and return the work item to devspec.refine.</rule>
    <rule>Accept a correction request re-entered from the tasks stage only while `implemented_revision` is behind `scope_revision` and no task is in-progress or complete. Rewrite the brief in place at the same scope revision, set its Status to revised, record what changed and why in decisions.md, mark the superseded task list `superseded`, and reset `planned_revision` to none so devspec.tasks re-plans against the corrected brief. This is a correction, not a change request: reject a new or widened requirement and route it to devspec.changerequest, which increments the revision instead.</rule>
    <rule>Classify every accepted material decision as work-item-local or reusable. Promote a reusable business or validation decision to devspec/foundation/workflow-rules.md with a stable rule ID and source decision link; promote a reusable engineering constraint to devspec/foundation/rules.md. Record the resulting canonical rule link in decisions.md.</rule>
    <rule>Record one compact foundation trace for the relevant coding conventions, owned areas and boundaries, canonical rules, applicable active `CP-###` principles, and the OWASP categories the change touches. Record a separate architecture and diagram trace for relevant overview entries, completed diagrams, or queued candidates, including implementation and validation impact; no diagram is required.</rule>
    <rule>Write a concise implementation brief and validation plan, not implementation code. Write the brief under its template sections so a developer can review the plan section by section, recording a section as not applicable with its reason rather than omitting it, and name the concrete components, interfaces, contracts, schemas, and migrations the work will touch instead of describing them in general terms.</rule>
  </rules>
  <entry>Active work item at finalization with a current-revision story, or at tasks when the developer asks to correct the current-revision brief before implementation has begun; return a story whose Open Requirement Gaps table is not closed to devspec.refine, and reject stale finalization, blocked work, and a correction request once any task for the current revision is in-progress or complete.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/finalize.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/foundation/workflow-rules.md" />
    <artifact path="devspec/foundation/rules.md" />
  </outputs>
  <transitions>
    <transition outcome="ready" stage="tasks" run="active" next="devspec.tasks" />
    <transition outcome="requirement-gaps-open" stage="refinement" run="active" next="devspec.refine" />
    <transition outcome="material-blocker" stage="finalization" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Stamp the readiness brief with the current scope revision. Preserve earlier revision sections as superseded history.</closure>
</workflow>
