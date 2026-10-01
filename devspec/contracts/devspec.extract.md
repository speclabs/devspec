# devspec.extract

Inspect the approved existing system end-to-end, produce its technical, business, workflow, and rule baseline, and prepare an evidence-backed diagram candidate list for explicit generation approval.

Invocation: `/devspec.extract`

<workflow command="devspec.extract">
  <purpose>Inspect the approved existing system end-to-end, produce its technical, business, workflow, and rule baseline, and prepare an evidence-backed diagram candidate list for explicit generation approval.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
    <protocol ref="security" />
  </protocols>
  <scope>Use for the existing-system baseline of an approved source scope. This command completes the whole foundation chain in one run; do not also run the individual foundation commands for the same repository. It prepares diagram candidates and offers generation once; devspec.diagram owns every later diagram.</scope>
  <input>Explicitly confirmed source repository scope, or current canonical evidence that names each repository's role, local path, and allowed access.</input>
  <rules>
    <rule>Complete repo-access before inspecting source, then record the accepted source scope in `devspec/foundation/codebase-structure.md`. Later commands may use that record as scope evidence.</rule>
    <rule>Inspect owned source, tests, manifests, configuration, infrastructure, scripts, and docs; exclude dependencies, caches, generated output, and repositories outside approved scope.</rule>
    <rule>For every approved repository, record an observed repository layout in `devspec/foundation/codebase-structure.md`: a readable `text` tree rooted at its confirmed local path that includes solution or manifest files, owned source and test roots, meaningful modules, configuration, and integration or migration locations. Keep the tree representative rather than exhaustive; exclude dependencies, caches, generated output, and secrets.</rule>
    <rule>Do not invent roles, workflows, business rules, validation rules, integrations, or diagrams; record an absent fact as blocked instead.</rule>
    <rule>Initialize and complete every listed foundation artifact from its template when missing: project context, technology stack, codebase structure, coding standards with followable local examples, rules, technical baseline, roles, workflows, workflow rules, extraction state, exploration state, and coverage. Record rare cross-work-item principle candidates in `devspec/constitution.md` with stable `CP-###` IDs, evidence, and candidate state; do not promote inferred candidates.</rule>
    <rule>For each observed coding convention that changes implementation or review behavior, assign a stable `CS-###` ID and capture one or more concise, concrete local code or test snippets as `EX-###` entries under `## Standards Examples`. Each entry names the applicable standard IDs, source location, and fenced language-appropriate code; one example may apply to multiple standards. Record a relevant anti-pattern when repository evidence supports one.</rule>
    <rule>Populate the OWASP baseline in rules.md from observed code, dependency, configuration, deployment, and access evidence.</rule>
    <rule>For every confirmed business workflow, record its business area, participating roles, trigger, outcome, business rules, validation rules, evidence, and applicable exceptions.</rule>
    <rule>Identify applicable evidence-backed diagram candidates: system architecture, application landscape, infrastructure topology, integration sequence or context, and a journey or process-flow diagram for every confirmed workflow. Add domain-model or state-lifecycle candidates only when evidence supports them. Record each in the diagram queue with its stable ID, type, subject, evidence, output format, duplicate-check result, status, and next action, and do not generate an SVG or add an overview entry before the developer answers the question below.</rule>
    <rule>After all foundation extraction outputs are complete, show the developer the complete candidate list. When one or more candidates exist, ask exactly one interactive confirmation, "Do you want me to generate all the possible diagrams?", offering `Yes — generate all listed diagrams`, `No — prepare the list only`, `Choose diagrams — enter the IDs or subjects to generate`, and `Custom Answer`, each with a concise example, and recommend `No — prepare the list only` when no generation preference is already confirmed. Whenever the list is shown, say that any listed diagram can be generated later with `/devspec.diagram &lt;DIA-ID-or-subject&gt;`, for example `/devspec.diagram DIA-002`.</rule>
    <rule>Generate exactly what the answer selects — every listed non-duplicate candidate, none, or only the entered IDs or subjects — validate each SVG XML file, update its queue status, and index completed durable output in the overview. Leave every ungenerated candidate listed in the queue, and keep the overview limited to completed diagram links.</rule>
    <rule>Record every path deliberately left out of inspection in `devspec/foundation/discovery-exclusions.md` with its reason, so a later run does not re-explore it or mistake the gap for missing evidence.</rule>
    <rule>Keep one extraction coverage item active and write discovered facts to their destination artifact, not queue state. Reuse recorded discovery methods and do not repeat a failed method unless its condition changed.</rule>
  </rules>
  <entry>Existing system with confirmed source scope and no active incompatible extraction run; reject new-repository foundation authoring or an assumed workspace target.</entry>
  <outputs>
    <artifact path="devspec/constitution.md" />
    <artifact path="devspec/foundation/project-context.md" />
    <artifact path="devspec/foundation/tech-stack.md" />
    <artifact path="devspec/foundation/codebase-structure.md" />
    <artifact path="devspec/foundation/coding-standards.md" />
    <artifact path="devspec/foundation/rules.md" />
    <artifact path="devspec/foundation/technical-baseline.md" />
    <artifact path="devspec/foundation/roles.md" />
    <artifact path="devspec/foundation/workflows.md" />
    <artifact path="devspec/foundation/workflow-rules.md" />
    <artifact path="devspec/foundation/extraction-state.md" />
    <artifact path="devspec/foundation/exploration-state.md" />
    <artifact path="devspec/foundation/extraction-coverage.md" />
    <artifact path="devspec/foundation/discovery-exclusions.md" />
    <artifact path="devspec/architecture/artifact-queue.md" />
    <artifact path="devspec/architecture/overview.md" />
    <artifact path="devspec/foundation/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-ready" stage="foundation" run="active" next="devspec.story" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Complete the listed baseline outputs and present the diagram candidate list before routing to story. Record every material evidence gap as blocked with a continuation condition, and preserve ungenerated candidates for `/devspec.diagram`.</closure>
</workflow>
