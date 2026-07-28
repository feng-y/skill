# Full Map Workflow

Use this reference only when L3 full-map workflow is triggered, or when a post-change buy-in, checklist, behavior summary, or quiz needs full-map detail. The pattern is not a mandatory stage machine. It is the canonical home for the repo's full-map / handoff branch: a set of artifacts for finding unknowns before work, preserving unknowns during work, and proving understanding after work.

Full-map work is the heavy L3 branch: when the user needs a complete map before implementation, produce the map as the deliverable. Do not make every default engineering task walk every section or route to another unknowns surface.

## Source Model

- Map: prompt, plan, docs, memories, assumptions, and context window.
- Territory: codebase, runtime, data, users, history, constraints, tests, and reviewers.
- Failure mode: execution proceeds from the map after the territory has contradicted it.
- Control rule: when map != territory, expose the unknown, run a minimal probe, ask one route-changing question, or record an implementation note.

Completion criterion: the task has an explicit path for the unknown most likely to break execution.

## Loading Rule

Choose the cheapest artifact that exposes the unknown:

- Use one probe when evidence can answer.
- Use one interview question when only the user can answer and the answer changes route.
- Use one concrete artifact when taste, vocabulary, or workflow is tacit.
- Use a full map only when implementation should wait or the user asks for map handoff/source alignment.

Completion criterion: the output is as small as possible while still changing the next action.

## Full Map Contract

When full-map mode is active, preserve these guarantees:

- Silently scan the request, prior attempts, touched files, configs, tests, runtime constraints, and user constraints before opening.
- Walk the map in this order: known knowns, known unknowns, unknown knowns, unknown unknowns, handoff.
- Name the current section so the user knows where they are on the map.
- Start from settled ground: request, territory facts with citations, locked constraints, assumptions marked as settled unless corrected, and a preview of the remaining sections.
- Run selected moves inside the current section; do not create a parallel workflow.
- Keep a visible known-unknown queue. Each item has a closer: `territory`, `user`, or `OPEN`.
- Use context probes when tacit taste, vocabulary, consumers, environment, done criteria, or workflow quality bar would change the route.
- Use concrete artifacts for reaction when taste, workflow, API shape, or output format is tacit; do not ask the user to imagine what can be shown.
- Make the user's next response cheap: lettered options, steal/skip choices, checkboxes, a decisions table, or a copyable prompt.
- Close decisions in front of the user. A question answered by territory still needs the question, evidence, and answer shown.
- Resolve known unknowns one at a time, highest blast radius first. Avoid walls of questions.
- Sweep the touched responsibility surface before handoff. Landmine cards name coverage, evidence, why it bites, changed action, and status.
- Cite real files or artifacts for territory claims. Label invented sample data as fake.
- Keep throwaway HTML artifacts self-contained: inline CSS/JS, no external requests, realistic fake data.
- Disclose load-bearing findings when found; file them under the right section rather than waiting.
- Stop only at stage boundaries that genuinely need user reaction. If the map itself is the deliverable, or a human-held blocker remains, implementation waits after map handoff. Otherwise the completed map should hand control back to the repo's next-capability selection rather than making a second human prompt the default bridge.

Completion criterion: full-map mode produces a complete map without forcing that cost on L1/L2 tasks.

## Before Implementation

| Move | Trigger | Output |
| --- | --- | --- |
| 01 Blindspot pass | unfamiliar module/domain, high-risk path, hidden-history risk | landmine cards covering the touched responsibility surface: evidence, why it bites, changed action |
| 02 Teach me my unknowns | missing vocabulary or quality bar | vocabulary ladder, quality criteria, sharper prompt |
| 03 Four directions | user will know it when they see it | contrasting options with steal/skip decisions, using real data or clearly labeled fake data |
| 04 Mock before you wire | UI/workflow/API/output shape is fluid | throwaway mock, sample, or prototype before production wiring, grounded in real data or clearly labeled fake data |
| 05 Brainstorm the intervention | several solution levels could work | options from cheapest safe change to ambitious bet |
| 06 Interview | one answer changes architecture/data/UX/strategy/verification | one route-changing question plus decision ledger |
| 07 Point at a reference | words are weaker than an example | semantics map before port/copy: transfers, non-transfers, edge cases, sign-off point |
| 08 Tweakable plan | implementation is near but human judgment remains | decisions-first plan; mechanical edits last |

Completion criterion: implementation begins only after the relevant blindspot, decision, taste, reference, or plan unknown has a path.

## During Implementation

Use 09 Implementation notes when code reality diverges from the plan, build spans multiple meaningful steps, verification sensitivity is high, or a conservative assumption is needed.

Record concise notes:

- Plan-confirmed: code matched the map in a meaningful place.
- Discovery: territory detail found without changing route.
- Deviation: map vs territory, conservative call, why reversible, verification impact.
- Human decision: current behavior, alternative, likely change point, blocking status.

Completion criterion: mid-build surprises can be reviewed without reconstructing scrollback.

## After Implementation

| Move | Trigger | Output |
| --- | --- | --- |
| 10 Buy-in doc / explainer | reviewers or stakeholders inherit the unknowns | demo-first pitch, objections answered with evidence, sign-off owner |
| Reviewer checklist | landmines or compatibility risks need review focus | concrete review checks tied to risk and files |
| Behavior summary | changed vs unchanged behavior could be misunderstood | changed behavior, unchanged behavior, compatibility, rollout, evidence |
| 11 Quiz before merge | long or non-obvious change needs verified understanding | learning report plus quiz pointing back to evidence |

Completion criterion: the finished change can be understood, reviewed, and verified without rediscovering the same unknowns.

## Full Map Artifact

When the user asks to map unknowns or the work should pause before build, walk the sections in order and assemble one self-contained artifact:

- Known knowns: settled facts, territory citations, existing constraints, and assumptions treated as settled unless corrected.
- Known unknowns: every named question with answer, closer (`user`, `territory`, or `OPEN`), options, recommendation, and blocker status.
- Unknown knowns: tacit taste, vocabulary, consumers, environment, done criteria, and decisions reshaped by extracted context.
- Unknown unknowns: sweep coverage plus landmine cards with evidence, why it bites, changed action, and status (`decided`, `OPEN`, or `sharp edge`).
- Proof plan: what will verify the claim after implementation.
- Tweakable build plan: judgment calls first, mechanical edits collapsed.
- Next prompt: copyable implementation prompt that starts from the map.

Completion criterion: the user holds the map; anything open is visible on the map, and the next agent can implement without re-opening the same discovery loop. When there is no remaining human-owned blocker, a completed map is a handoff artifact, not an automatic stop reason.

## Fold-Back

After non-trivial work, keep only the lesson that prevents repeated rediscovery:

- wrong map assumption;
- probe that exposed territory;
- earlier statement that would have prevented the miss;
- note, doc, test, or follow-up that should preserve it.

Completion criterion: the retro is shorter than the work it saves next time.
