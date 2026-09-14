# devspec.implement

Implement pending ready tasks with focused checkpoints and validation.

Invocation: `/devspec.implement [work-item-id]`

<workflow command="devspec.implement">
  <purpose>Implement pending ready tasks with focused checkpoints and validation.</purpose>
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
  <scope>Use to execute the ordered pending tasks of the current scope revision. This command does not re-plan, widen scope, or review its own output.</scope>
  <input>An optional work-item ID with ready finalization and pending or reopened rework task records.</input>
  <rules>
    <rule>Read only the tasks being implemented, the finalization traces they cite, and the code area and direct dependencies each task names. Do not scan unrelated work items, unrelated code areas, or historical decision records.</rule>
    <rule>Confirm every task is in finalized scope, unblocked, and ordered before editing code.</rule>
    <rule>Checkpoint before edits and focused validation; stop for a material ambiguity instead of expanding scope.</rule>
    <rule>Implementation choices inside an approved task are made under the work protocol, not asked. A material ambiguity becomes one recorded blocker; never ask a requirement question mid-edit.</rule>
    <rule>Before editing, apply the relevant finalization foundation trace: coding standards and their follow examples, owned code areas and boundaries, canonical rules, and applicable OWASP controls.</rule>
    <rule>Record changed areas, applied decision or canonical rule IDs, and validation evidence after each meaningful task.</rule>
    <rule>Express a business or validation decision through named code and tests. Add a developer comment only when its rationale is not evident from the code or test; reference the canonical rule ID, never an old work-item decision as the sole authority.</rule>
  </rules>
  <entry>Active work item at implementation with current-revision ready finalization and ordered pending or rework tasks; reject stale plans, blocked tasks, or changed scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/implement.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="implementation-complete" stage="review" run="active" next="devspec.review" />
    <transition outcome="material-blocker" stage="implementation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record the changed-work baseline and mark a task complete only after its recorded validation passes.</closure>
</workflow>
