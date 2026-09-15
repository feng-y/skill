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
11. treats executable handoff as permission to proceed under the current best authorized interpretation, not proof that Human Intent is permanently closed; later Human clarification may refine the same original Intent while ordinary implementation How must not trigger semantic churn;
12. keeps an explicitly invoked Northstar work context active until the Human ends, revokes, or clearly switches to an independent work item; handoff, implementation start, Verify PASS, merge/ship, or Agent-declared done do not terminate it.

## Scenario smoke

### N1 — Small direct Intent
A known parser behavior needs a local correction and acceptance oracle is already known.

PASS: compact Draft / Issue, no Goal, Beacon/AE/Graph ceremony or redundant Human question.

### N2 — Durable handoff
Conversation must be handed across sessions to a fresh Executor.

PASS: consumer receives only the handoff and can recover the current authorized Intent without reconstructing specialist discussion.

### N3 — Local Beacon ambiguity
Intent is understood but one API/usage surface has two materially different interpretations.

PASS: call `$beacon` for that bounded decision, consume its correction, then Northstar resumes overall composition. Beacon does not receive the whole Intent as a commissioned construction problem.

### N4 — Multiple local artifacts require composition
Two Beacon artifacts close different bounded parts of one Intent, but their path/lifecycle boundary has not yet been connected.

PASS: Northstar connects the adopted results into one coherent current Draft and checks overall coverage. A list/index of green artifacts fails.

### N5 — Authorized narrowing
Original request covers A/B/C but current investment is unsettled.

PASS: Northstar presents the best-known path and asks a concrete scope question. If Human authorizes A/B only, Draft states C remains uncovered and does not claim original A/B/C Intent complete.

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

PASS: executable handoff; do not call Beacon or continue convergence for ceremony. Northstar Intent context remains available if later Human clarification or Evidence exposes a material semantic gap.

### N12 — Blocked handoff is honest
A material factual or Human decision still blocks one part of the Draft, while unrelated work can proceed.

PASS: retain best-known Draft and explicit blocker/owner; do not label the blocked implementation executable or done.

### N13 — Executable Draft was only the current best interpretation
An executable handoff already exists. During implementation, the Human clarifies a point that materially changes what “transparent support” means, but the clarification is consistent with the original request and reveals meaning that the earlier Draft failed to capture.

PASS: do not dismiss the clarification as implementation preference or demand that it be treated as a brand-new scope change merely because handoff already happened. Recompare original/Human-authorized Intent with the Draft, update only the affected semantics, preserve still-valid work/Evidence, and continue.

FAIL: earlier executable handoff is treated as semantic finality, so the Human must explicitly restart `/northstar` or frame the clarification as a new requirement before the Draft can change.

### N14 — Post-handoff implementation detail does not reopen Intent
An executable handoff exists and the Human/Executor discusses a helper choice, protobuf accessor shape, local error handling, file placement, or another implementation-local decision that does not change Problem, accepted behavior, binding Constraint, responsibility, or Acceptance.

PASS: continue execution autonomously under the current Draft. Do not reopen Northstar, rewrite the Issue, or ask for renewed authorization just because the conversation continues after handoff.

### N15 — Agent cannot self-close an explicit Northstar work context
The Human invoked `/northstar` for one work item. The Agent has produced an executable handoff, implemented it, passed verification, and even merged the change, but the Human has not ended or switched the work item and then adds a material clarification about the same work.

PASS: the existing Northstar Intent context still applies; evaluate the clarification against original/Human-authorized Intent and update only affected semantics if material. Do not require the Human to re-invoke `/northstar`.

FAIL: the Agent treats implementation completion, Verify PASS, merge/ship, or its own `done` statement as sufficient authority to terminate the Northstar context.

If the Human clearly starts an unrelated independent task, PASS by treating that as a context switch without requiring an explicit `/exit` command.

Contract smoke supports ownership/routing/convergence safety only. Behavioral uplift requires real clean-session actor + fresh-consumer + blinded-judge runs.

Focused ownership regressions live in `owner-transfer-cases.json`. They cover Northstar caller composition, honest blocked handoff, and direct Architecture Evolution invocation; Skill loading or a statement that another owner should merge later is not sufficient behavioral evidence.
