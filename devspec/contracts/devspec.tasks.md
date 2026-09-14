# devspec.tasks

Create ordered, independently verifiable implementation tasks.

Invocation: `/devspec.tasks [work-item-id]`

<workflow command="devspec.tasks">
  <purpose>Create ordered, independently verifiable implementation tasks.</purpose>
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
  <scope>Use to turn a ready finalization into an ordered, independently verifiable plan. This command plans only; devspec.implement makes the changes.</scope>
  <input>An optional work-item ID with a ready current finalization brief.</input>
  <rules>
    <rule>Read only the current finalization brief, the story's current-revision criteria, and the foundation or architecture entries that brief already cites. Do not re-derive the traces from source or re-read unrelated foundation artifacts.</rule>
    <rule>Each task names scope, dependency, source justification, applicable decision or canonical rule IDs, validation, and done condition. Cite the finalization foundation and architecture traces for coding standards, codebase boundaries, diagrams, and OWASP controls instead of duplicating them per task.</rule>
    <rule>Order dependencies before dependents and split only work too broad to validate safely.</rule>
    <rule>Sequencing, splitting, and validation choices are this command's own judgment, recorded as source justification rather than asked. Record a blocker only when the brief cannot become an ordered, independently verifiable plan without a decision it does not contain.</rule>
  </rules>
  <entry>Active work item at tasks with a ready finalization matching the current scope revision; reject blocked readiness evidence.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="tasks-planned" stage="implementation" run="active" next="devspec.implement" />
    <transition outcome="material-blocker" stage="tasks" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Plan only the active revision. Each task has source justification, validation, done condition, and a controlled initial status.</closure>
</workflow>
