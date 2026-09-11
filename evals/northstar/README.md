# Northstar contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Northstar passes only when it:

1. owns canonical engineering Intent and materializes it as Drafted Issue when durable handoff is needed;
2. uses Problem / Draft / Constraints / Acceptance / Decisions / Evidence as needed, without manufacturing a separate Goal layer;
3. does not force Graph / Taskbook when a clear Issue can execute directly;
4. routes concrete-shape ambiguity to `$prototype`, long-term structural judgment to `$architecture-evolution`, factual territory unknowns to `$unknowns-first`;
5. defines Acceptance but does not derive proof sufficiency from backend output; material verification design/judgment routes to `$verify`;
6. never treats availability of Replay/test/build as a reason to rewrite Intent or embed backend commands in the canonical contract;
7. updates the same canonical Issue instead of creating parallel intent/spec/plan SOTs;
8. treats Issue as cohesive engineering outcome, not context-window-sized ticket;
9. accepts verified Evidence feedback from research / execution / review / verification backends and reopens only the affected semantic owner;
10. when complex material Graph exists, verified Evidence may recompile only the affected dependency cone without turning Northstar into progress manager.

## Scenario smoke

### N1 — Small direct Intent
A known parser behavior needs a local correction and acceptance oracle is already known.

PASS: compact Intent / Issue, no Goal, no Prototype/AE/Graph ceremony; Acceptance states observable outcome. A local test may later prove it without Northstar choosing the command.

### N2 — Durable handoff
Conversation must be handed across sessions to a fresh Executor.

PASS: Issue remains sufficient without original conversation; body contains current canonical intent and comments remain history/evidence. Control-plane choice is irrelevant.

### N3 — Concrete ambiguity
Two core paths both satisfy prose but differ materially in ownership.

PASS: call `$prototype`, fold correction back, do not ask AE unless long-term structure itself is undecided.

### N4 — Structural fork
Long-term responsibility / dependency direction is unresolved.

PASS: call `$architecture-evolution`; fold only durable structural decision into Intent.

### N5 — Territory unknown
Current producer may be A or B and answer changes intended path.

PASS: call `$unknowns-first`; do not guess and do not let Unknowns First redesign Intent.

### N6 — Complex dependency earns compile
Intent is settled but several material outcomes have real dependency that a fresh Executor would otherwise rediscover.

PASS: use `material-compile` to express coarse material relations; no file/helper/test tasklist and no backend selection.

### N7 — Verification route is material
Acceptance is clear, but behavior-preserving migration requires trustworthy baseline/equivalence proof.

PASS: keep Acceptance in Northstar and route proof obligation/backend/sufficiency to `$verify`. Do not make Replay a Northstar stage.

### N8 — Execution Evidence changes material graph
Intent remains valid, but verified implementation/review Evidence proves one contingent branch is now real and another dependency does not exist.

PASS: recompile only the affected material dependency cone; unrelated work/Evidence stay valid; control plane does not own Graph semantics.

### N9 — Backend red, implementation defect
Acceptance remains valid and Verify establishes realized behavior is wrong using a test/Replay/runtime backend.

PASS: keep Intent stable and route fix to PR / Executor; do not rewrite Issue merely because a verifier is red.

### N10 — Verify disproves contract premise
Verified reality proves Acceptance or Draft itself is invalid.

PASS: reopen only affected Intent surface and update canonical Issue.

Contract smoke supports ownership/routing safety only; behavioral uplift requires real clean-session runs.
