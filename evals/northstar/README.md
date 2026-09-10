# Northstar contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Northstar passes only when it:

1. owns canonical engineering Intent and materializes it as Drafted Issue when durable handoff is needed;
2. uses Problem / Draft / Constraints / Acceptance / Decisions / Evidence as needed, without manufacturing a separate Goal layer;
3. does not force Graph / Taskbook when a clear Issue can execute directly;
4. routes concrete-shape ambiguity to `$prototype`, long-term structural judgment to `$architecture-evolution`, territory facts to `$unknowns-first`;
5. defines Acceptance but leaves verifier choice / outcome judgment to `$replay`;
6. updates the same canonical Issue instead of creating parallel intent/spec/plan SOTs;
7. treats Issue as cohesive engineering outcome, not context-window-sized ticket;
8. only reopens Intent from Replay when verified reality invalidates Draft / Constraint / Acceptance or Human commitment.

## Scenario smoke

### N1 — Small direct Intent
A known parser behavior needs a local correction and acceptance oracle is already known.

PASS: compact Intent / Issue, no Goal, no Prototype/AE/Graph ceremony.

### N2 — Durable handoff
Conversation must be handed to a fresh agent / MultiCA.

PASS: Issue remains sufficient without original conversation; body contains current canonical intent and comments remain history/evidence.

### N3 — Concrete ambiguity
Two core paths both satisfy prose but differ materially in ownership.

PASS: call `$prototype`, fold correction back, do not ask AE unless long-term structure itself is undecided.

### N4 — Structural fork
Long-term responsibility / dependency direction is unresolved.

PASS: call `$architecture-evolution`; fold only durable structural decision into Intent.

### N5 — Territory unknown
Current producer may be A or B and answer changes intended path.

PASS: call `$unknowns-first`; do not guess.

### N6 — Complex dependency earns compile
Intent is settled but several material outcomes have real dependency that a fresh Executor would otherwise rediscover.

PASS: use `material-compile` to express coarse material relations; no file/helper/test tasklist and no verifier selection.

### N7 — Replay red, implementation defect
Acceptance remains valid but realized behavior is wrong.

PASS: keep Intent stable and route fix to PR / Executor; do not rewrite Issue merely because Replay is red.

### N8 — Replay disproves contract premise
Verified reality proves Acceptance or Draft is invalid.

PASS: reopen only affected Intent surface and update canonical Issue.

Contract smoke supports ownership/routing safety only; behavioral uplift requires real clean-session runs.
