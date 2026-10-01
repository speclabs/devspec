# devspec.changerequest

Append one related post-finalization requirement without rewriting history.

Invocation: `/devspec.changerequest [work-item-id] Add JSON export`

<workflow command="devspec.changerequest">
  <purpose>Append one related post-finalization requirement without rewriting history.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
  </protocols>
  <scope>Use only for a requirement related to a work item that is already finalized. Use devspec.story for independent scope, and edit the story directly while it is still before finalization.</scope>
  <input>An optional work-item ID and one related missing requirement.</input>
  <rules>
    <rule>Append the next CR-### entry and CR-scoped criteria; never rewrite baseline evidence.</rule>
    <rule>List every requirement gap the change leaves open in story.md's Open Requirement Gaps table, raised by its CR-### ID, and ask none of them; devspec.refine owns those questions.</rule>
    <rule>Mark the earlier finalization, task, implementation, and review sections superseded when the revision increments, preserving their recorded evidence unchanged.</rule>
    <rule>Ask one material classification question when it is unclear whether the request is related or a new linked work item. Until the request is classified related, leave the work item's stage and next action unchanged: route an independent request to devspec.story as a linked work item, and when the developer cannot answer yet, stop with the question unanswered in decisions.md.</rule>
  </rules>
  <entry>Related requirement for a finalized-or-later work item with an active current scope revision; reject independent, blocked, or pre-finalization requests.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/finalize.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/implement.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/review.md" />
  </outputs>
  <transitions>
    <transition outcome="related-change-accepted" stage="refinement" run="active" next="devspec.refine" />  </transitions>
  <closure>Append the CR and record the classification that justified it.</closure>
</workflow>
