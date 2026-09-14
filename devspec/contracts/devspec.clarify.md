# devspec.clarify

Resolve one active blocker and resume its originating stage.

Invocation: `/devspec.clarify [work-item-id]`

<workflow command="devspec.clarify">
  <purpose>Resolve one active blocker and resume its originating stage.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
  </protocols>
  <scope>Use only to resolve one recorded material blocker and resume the command that recorded it. This command never advances a stage, changes scope, or answers a question its originating command has not recorded.</scope>
  <input>An optional work-item ID, or one foundation or quickfix record, with one active material blocker question.</input>
  <rules>
    <rule>Resolve the one question the originating command recorded as its active material blocker, never another queued question and never a question the originating command did not record, and append its answer to decisions.md. When the originating command keeps a wider queue, leave the remaining questions to that command's own re-discovery on resume. For a work item, append the origin command, question, resolution, evidence, and exact resume command to clarify.md.</rule>
    <rule>Do not accept scope changes after finalization; route them to changerequest.</rule>
    <rule>Return to the saved stage and next action after resolution.</rule>
  </rules>
  <entry>Exactly one active material blocker in a foundation, work-item, or quickfix decision record with a saved originating command; reject unblocked or ambiguous records.</entry>
  <outputs>
    <artifact path="devspec/foundation/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/clarify.md" />
    <artifact path="devspec/quickfixes/QF-&lt;number&gt;-&lt;slug&gt;.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="decision-resolved" stage="origin" run="active" next="resume-origin" />
  </transitions>
  <closure>Append the resolution, restore the exact saved stage and next command, and do not change scope while resolving a blocker.</closure>
</workflow>
