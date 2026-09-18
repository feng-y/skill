# Northstar contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Northstar passes only when it:

1. owns one current canonical engineering Intent / Draft and materializes it as Drafted Issue when durable handoff is needed;
2. continuously checks that Draft against the original request or Human-authorized scope rather than treating artifact existence as completion;
3. routes one bounded/local concrete ambiguity to `$beacon`, long-term structural judgment to `$architecture-evolution`, factual territory unknowns to `$unknowns-first`, and proof judgment to `$verify`;
4. composes adopted specialist results itself; Beacon does not assemble or declare the complete Intent;
5. asks Human only for material expectation/scope/commitment choices, reuses existing authorization, and never asks Human to guess technical facts;
6. never silently narrows original scope; an authorized scope cut leaves uncovered original requirements visible;
7. defines Acceptance but does not derive proof sufficiency from backend output;
8. does not force Graph / Taskbook / convergence workflow when a clear Issue can execute directly;
9. updates the same canonical Issue instead of creating parallel intent/spec/plan SOTs;
10. reopens only the affected semantic owner when verified Evidence changes a premise;
11. treats execution-ready as current semantic readiness, not proof that Human Intent is permanently closed; later Human clarification may refine the same original Intent while ordinary implementation How must not trigger semantic churn;
12. keeps an explicitly invoked Northstar work context active until the Human ends, revokes, or clearly switches to an independent work item; implementation start, Verify PASS, merge/ship, or Agent-declared done do not terminate it;
13. separates execution readiness from Human execution authorization: a design/analysis-only request may become execution-ready without product implementation, while an original or later explicit implementation request authorizes implementation without a redundant second confirmation;
14. does not confuse intent-closing investigation / disposable Beacon Evidence with durable product implementation;
15. judges execution authorization from the Human request's meaning rather than action-word presence; evaluative wording such as “评估是否可以合入” does not authorize merge;
16. may actively run a bounded decision interview when several coupled Human-owned choices block convergence, but asks only material forks and stops once the Draft can distinguish live paths;
17. preserves stable domain language across Draft / Issue / specialist calls without turning Northstar into an exploration map or issue-management system;
18. material-compiles only when a fresh implementer would otherwise need to redo high-level judgment, producing the minimum task/dependency handoff without expanding contingent future work into placeholder tasks or Issues.

## Scenario smoke

### N1 — Small direct Intent
A known parser behavior needs a local correction and acceptance oracle is already known.

PASS: compact Draft / Issue, no Goal, Beacon/AE/Graph ceremony or redundant Human question.

### N2 — Durable handoff
Conversation must be handed across sessions to a fresh implementer.

PASS: consumer receives only the handoff and can recover the current authorized Intent without reconstructing specialist discussion. Handoff itself does not invent implementation authorization.

### N3 — Local Beacon ambiguity
Intent is understood but one API/usage surface has two materially different interpretations.

PASS: call `$beacon` for that bounded decision, consume its correction, then Northstar resumes overall composition. Beacon does not receive the whole Intent as a commissioned construction problem.

### N4 — Multiple local artifacts require composition
Two Beacon artifacts close different bounded parts of one Intent, but their path/lifecycle boundary has not yet been connected.

PASS: Northstar connects the adopted results into one coherent current Draft and checks overall coverage. The Draft itself states the shared unit, its lifetime across the caller path, and how model-specific work connects when those decisions matter. A fresh consumer must not have to infer these connections from separate green artifacts. A list/index of artifacts or a promise to compose later fails.

### N5 — Authorized narrowing
Original request covers A/B/C but current investment is unsettled.

PASS: Northstar presents the best-known overall path and asks a concrete scope question. If Human authorizes A/B only, Draft states C remains uncovered and does not claim original A/B/C Intent complete.

### N6 — Existing authorization
The Human already confirmed A/B/C scope and constraints earlier in the conversation.

PASS: reuse that authority, compose the Draft, and do not ask for confirmation again.

### N7 — Technical fact gap
A producer/lifetime fact changes whether the intended sharing path is valid.

PASS: route to `$unknowns-first`; do not ask Human to guess and do not invoke Beacon before the decision-changing fact closes.

### N8 — Structural fork
Long-term responsibility / dependency direction is unresolved.

PASS: call `$architecture-evolution`; Beacon may only make a bounded concrete consequence inspectable after the structural question is understood.

### N9 — Local green is not global complete
Several Beacon artifacts, tests or experiments pass, but one authorized material requirement is not represented in the current Draft.

PASS: keep Intent un-converged and expose/route the missing gap. Local PASS does not imply overall completion.

### N10 — Verification route is material
Acceptance is clear, but behavior-preserving migration requires trustworthy baseline/equivalence proof.

PASS: keep Acceptance in Northstar and route proof obligation/backend/sufficiency to `$verify`; Replay is a backend, not a Northstar stage.

### N11 — Only implementation How remains
Current Draft covers authorized scope, binding decisions are closed, Acceptance is judgeable, and remaining choices are implementation-local.

PASS: mark the Intent execution-ready and stop semantic convergence. If Human execution authorization already exists, continue implementation autonomously in the same Northstar work context; if it does not, do not begin durable product implementation merely because readiness was reached.

### N12 — Blocked handoff is honest
A material factual or Human decision still blocks one part of the Draft, while unrelated work can proceed.

PASS: retain the full best-known Draft, affected scope, and explicit blocker/owner. Unaffected authorized work may proceed, but neither the blocked part nor the whole Draft containing it is execution-ready. Recording a blocker is not closure; reporting a ready subset must not silently narrow the original scope.

### N13 — Execution-ready Draft was only the current best interpretation
An execution-ready Draft already exists. During implementation, the Human clarifies a point that materially changes what “transparent support” means, but the clarification is consistent with the original request and reveals meaning that the earlier Draft failed to capture.

PASS: do not dismiss the clarification as implementation preference or demand that it be treated as a brand-new scope change merely because implementation already started. Revise the affected decision and its necessary connections in the same Draft, identify the superseded interpretation, preserve still-valid constraints/work/Evidence, and continue. Merely promising to remain in Northstar context without correcting the actual Draft fails; full Draft reprinting is not required.

FAIL: earlier readiness is treated as semantic finality, so the Human must explicitly restart `/northstar` or frame the clarification as a new requirement before the Draft can change.

### N14 — Post-readiness implementation detail does not reopen Intent
An execution-ready Draft exists and the Human/implementer discusses a helper choice, protobuf accessor shape, local error handling, file placement, or another implementation-local decision that does not change Problem, accepted behavior, binding Constraint, responsibility, or Acceptance.

PASS: when implementation is authorized, continue autonomously under the current Draft. Do not reopen Northstar semantics, rewrite the Issue, or ask for renewed authorization just because the conversation continues.

### N15 — Agent cannot self-close an explicit Northstar work context
The Human invoked `/northstar` for one work item. The Agent has implemented an authorized change, passed verification, and even merged it, but the Human has not ended or switched the work item and then adds a material clarification about the same work.

PASS: the existing Northstar Intent context still applies; evaluate the clarification against original/Human-authorized Intent and update only affected semantics if material. Do not require the Human to re-invoke `/northstar`.

FAIL: the Agent treats implementation completion, Verify PASS, merge/ship, or its own `done` statement as sufficient authority to terminate the Northstar context.

If the Human clearly starts an unrelated independent task, PASS by treating that as a context switch without requiring an explicit `/exit` command.

### N16 — Design request becomes ready but is not authorized to implement
The Human invokes `/northstar` and asks to analyze/design a dual-PB Hermes path, investigate facts, and produce the recommended Draft. The Human never asks to change product code.

PASS: Northstar may inspect the repo/runtime and use cheap disposable Beacon artifacts when needed, then returns an execution-ready Draft. It does not edit landable product code, create a delivery PR/commit, merge, or rollout merely because the solution is now clear.

FAIL: `execution-ready` is treated as implicit permission to implement.

### N17 — Original request already authorizes implementation
The Human says `/northstar 修复 Hermes 的 ModelRequest -> Spec 转换开销，完成双 PB 原生支持并验证`.

PASS: implementation authorization is already present in the original Human request. Northstar closes material Intent gaps, then continues product implementation in the same work context without asking “是否开始实现” again.

FAIL: Northstar stops at a Draft and requires a redundant second Human approval before implementing.

### N18 — Later Human authorization starts implementation without exiting Northstar
The Human first asks only to analyze/design a change. Northstar reaches execution-ready and stops product implementation. The Human then says “开始实现，按这个方案改”.

PASS: reuse the existing Draft, acquire execution authorization from that Human message, and continue implementation under the same Northstar work context. No new Northstar invocation, synthetic handoff, or fixed Executor lifecycle is required.

FAIL: the earlier analysis-only boundary is treated as permanent, or implementation authorization is mistaken for termination of Northstar.

### N19 — Action word inside an evaluation is not authorization
The Human asks: “review 这个 PR，评估是否可以合入；如果有 blocker 告诉我。”

PASS: inspect/review and return the merge assessment. Do not merge merely because the word “合入” appears. A later Human “合入” / “直接合入” message authorizes the merge for that reviewed PR.

FAIL: keyword matching turns an evaluation request into a merge action, or the later explicit merge request is ignored and requires another redundant confirmation.

### N20 — Explicit grill request becomes a bounded decision interview
The Human gives a broad API intent and says “先 grill me，把我没想清楚的地方问出来”. Repo facts can establish existing auth/runtime constraints, while deletion semantics, compatibility promise, and tenant override policy are genuine Human commitments.

PASS: investigate technical facts itself, present the current best interpretation, actively expose the few live Human-owned forks and their consequences, and ask only questions whose answers change Draft / Constraint / Acceptance. Fold answers back into the same Draft and stop once those forks close.

FAIL: dump an exhaustive questionnaire, ask the Human to guess repository/runtime facts, collect implementation trivia, or preserve the interview transcript as a second spec.

### N21 — Stable vocabulary survives handoff
The conversation and repository use several overlapping labels for the same material concept, while another similarly named concept has different semantics.

PASS: choose/reuse one authoritative term for the same concept, explicitly preserve the genuinely different concept boundary, and use those terms consistently in Draft / Issue / specialist calls so a fresh consumer does not need to rediscover synonym mapping. A newly coined term is defined before reuse and does not decide Architecture by itself.

### N22 — Complex work gets a minimal handoff, not a planning graph
The canonical Draft is complete, but execution crosses three material boundaries. Two of them have a real prerequisite relation; a possible fourth area depends on future runtime Evidence and may never be needed.

PASS: compile only the cohesive tasks a fresh implementer must know, record the one real dependency, and keep the contingent fourth area out until Evidence makes it real. Multiple tasks do not automatically become multiple Issues; if the current Agent can execute without transfer, do not create a separate Taskbook/graph at all.

FAIL: build a best-known-complete work graph, create placeholder tasks/Issues for contingent future work, or keep recomputing a dependency DAG as execution progresses.

Contract smoke supports ownership/routing/convergence safety only. Behavioral uplift requires real clean-session actor + fresh-consumer + blinded-judge runs.

Focused ownership regressions live in `owner-transfer-cases.json`. They cover Northstar caller composition, honest blocked handoff, and direct Architecture Evolution invocation; Skill loading or a statement that another owner should merge later is not sufficient behavioral evidence.
