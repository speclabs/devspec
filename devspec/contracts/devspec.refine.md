# devspec.refine

Make one draft story buildable through scoped review and material questions.

Invocation: `/devspec.refine [work-item-id]`

<workflow command="devspec.refine">
  <purpose>Make one draft story buildable through scoped review and material questions.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use to make a draft story, or the requirement a change request added, buildable through scoped analysis and material questions; this is the only route out of intake and out of an accepted change request, because neither devspec.story nor devspec.changerequest reads the code, compatibility, or risk evidence readiness depends on. devspec.finalize returns work here when a requirement gap is open.</scope>
  <input>An optional work-item ID or clear current draft.</input>
  <rules>
    <rule>Read only the draft, workflow rules, codebase structure to locate the code area, the foundation rules that constrain behavior such as accessibility and compliance rules, the selected code area, and its direct dependencies. Do not read coding standards: they shape how code is written rather than what it does, and devspec.finalize applies them. Do not scan unrelated historical work-item decisions.</rule>
    <rule>Run the ask protocol's discovery across every refinement dimension before advancing: behavior, acceptance criteria, scope boundaries, technical constraints, edge cases, dependencies, compatibility risks, data and integration impact, and validation gaps. Queue every open entry in story.md's Open Requirement Gaps table, whether devspec.story, devspec.changerequest, or devspec.finalize raised it, add every gap the scoped reading exposes, and re-run discovery after each answer. When the source already carried confirmed acceptance criteria and no entry is open, still run discovery across the code-area dimensions, and close with no questions when none apply. This command owns every requirement question.</rule>
    <rule>Record what the work must do, never how it is designed. For data and integration, record which data and integrations the behavior touches and what consumers must keep working; for validation, make every acceptance criterion observable and testable; record edge cases as criteria, compatibility as who must not break, and only the technical constraints that change behavior or scope. Schemas, migrations, contracts, rollout, edge-case handling, and the validation plan are devspec.finalize's design. Security, compliance, and delivery constraints are devspec.finalize's; raise one only when it materially changes the behavior being refined.</rule>
    <rule>Record every code area, module, interface, and data store the criteria touch in story.md's Affected Areas table with the criteria it serves and its evidence label. devspec.finalize reads only these areas, so an area missing here comes back as a requirement gap.</rule>
    <rule>Close story.md's Open Requirement Gaps table before advancing: set every entry resolved with the criteria or constraint it produced, or skipped with its reason. devspec.finalize returns the work item here while an entry is neither.</rule>
    <rule>Do not re-ask intake identity questions. The work-item number, provider reference, and type are settled in story.md and meta.md; correct type in meta.md from better evidence without asking.</rule>
    <rule>Improve behavior, acceptance criteria, scope, technical constraints, edge cases, dependencies, compatibility risks, and blockers in place, and resolve each answered question into the artifact it affects rather than leaving it only in decisions.md.</rule>
    <rule>At a scope revision above 1, limit discovery to the current revision's CR-### criteria, their open gaps, and the areas they touch. Never edit criteria or gaps a finalized revision recorded; route a new requirement after finalization to changerequest.</rule>
  </rules>
  <entry>Active work item at refinement for the current scope revision, whether routed from intake or a change request, or returned by devspec.finalize with an open requirement gap; reject a finalized revision, blocked, stale, or unrelated scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="ready-for-finalization" stage="finalization" run="active" next="devspec.finalize" />
    <transition outcome="material-blocker" stage="refinement" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Do not advance while any applicable material question remains unanswered or explicitly skipped with its reason, and do not treat an empty queue as completeness without re-running discovery. Record the one blocker and resume reference.</closure>
</workflow>
