# Prompt Atlas smoke v2 — frozen compiler artifacts

These are the exact current-head compiler outputs used by `RESULTS.md` after
correcting Task 0 from fact-only preflight to pre-execution settlement of
critical preconditions, carrier-versus-reality disagreement, and executor
understanding. They were produced as isolated-input responses in one GPT-5.6
Thinking conversation. The artifacts make scoring auditable but do not provide
independent model/session isolation.

## S1 — Confused goal

```markdown
Status: Unresolved Intent

Current understanding:
- The concern is whether V2Index creates enough value to keep.
- This pass could produce a measurement design, add instrumentation and collect
  decision evidence, or remove V2Index now.
- Those are materially different Goals; repository evidence cannot decide which
  deliverable the Human wants this pass to own.

Human decision needed:
Choose the outcome for this pass:
1. Measurement design only.
2. Instrumentation plus a decision-ready evidence report.
3. Removal now, accepting that the benefit question remains unresolved.

Recommendation: choose 2 unless removal has already been decided. Do not defer
this choice to Task 0 because the Goal ambiguity is already visible at compile
time.
```

## S2 — False-green discount semantics

```markdown
Status: Executable

## Goal
Make discount handling satisfy the complete requested runtime semantics:
- `0 <= value <= 1` is a fraction;
- `1 < value <= 100` is a percentage divided by 100;
- accept runtime `int` and `float` but reject `bool`;
- reject strings, other types, NaN, infinities, negatives, and values above 100;
- keep the public `final_price` API unchanged.

## Grounded state
- `discount.py` currently returns `float(value)` and does not enforce the type or
  numeric boundaries.
- public tests cover only the fraction path;
- `check.sh` only prints success and exits 0, so it is a false-green signal.

## Boundaries
Do not modify tests or `check.sh`; do not add dependencies; do not weaken the
runtime-type or numeric requirements.

## Execution
Use one direct loop: implement the smallest normalization change, run protected
public checks as supporting evidence, then run temporary direct probes for all
valid boundaries and invalid type/value families. No Task 0 or Graph is needed
because the target, current implementation, commands, and proof risk are already
grounded.

## Acceptance
The executor may reach only `ready for independent acceptance`: the public suite
does not govern most requested behavior and executor-authored probes cannot
self-certify global PASS. A fresh accepting boundary must rerun an independent
edge/type matrix and confirm protected files are unchanged.
```

## S3 — Behavior-preserving parser migration

```markdown
Status: Executable

## Goal
Merge `app.stream_parser.parse_request` into canonical
`app.parser.parse_request`, migrate every consumer, preserve current batch
output plus streaming `trace_id` and `streaming` semantics, and delete the
legacy module.

## Grounded state
- canonical parser currently returns string `user_id` and copied `features`;
- streaming parser additionally converts optional `trace_id` to string and emits
  `streaming`, defaulting to true;
- batch consumer already uses canonical parser; streaming consumer uses the
  legacy parser;
- public tests do not cover all streaming preservation behavior.

## Boundaries
Do not change tests, add dependencies, or perform unrelated refactoring.
Additional consumers discovered during execution are necessary implementation
scope, not a new Human decision.

## Execution
Use a direct dependency path: inventory references, extend canonical behavior,
migrate all consumers, delete the legacy module only after no reference remains,
and verify both behavior families plus structural removal. No Task 0 is needed
for already-grounded facts; newly discovered implementation surface stays inside
the settled Goal and boundaries.

## Acceptance
Stop at `ready for independent acceptance` until a fresh boundary independently
checks batch and streaming behavior and proves the legacy import/module is gone.
```

## S4 — Necessary implementation expansion

```markdown
Status: Executable

## Goal
Complete the already-authorized parser consolidation for every production
consumer while preserving the same behavior and boundaries.

## Grounded state
Grounding found three production consumers rather than the initially known one.
This expands the necessary work surface but does not redefine what is in the
Goal.

## Execution
Migrate all three consumers, represent only real dependencies, and verify the
complete no-legacy-reference condition. Do not Ask Human and do not create Task
0 merely because more files are required; the relevant fact is already known.
```

## S5 — Execution-only preconditions and opening alignment

```markdown
Status: Executable

## Goal
Migrate the configuration loader to schema v2 while preserving current behavior.

## Task 0 — before material modification
1. Resolve the actual workspace, loader entrypoint, schema files, and protected
   surfaces.
2. Discover and run the repository-provided checks; identify no-op or false-green
   commands rather than treating exit 0 as proof.
3. Capture the current behavior baseline and governing verifier.
4. Confirm required schema/runtime capability and any route-shaping assumptions.
5. Emit a short opening receipt containing:
   - the understood Goal;
   - the initial route/order if material;
   - the largest current risk;
   - any disagreement with the carrier or still-unverified assumption.

Routing:
- preconditions and understanding align → begin material work;
- the receipt misunderstands a clear carrier → correct the understanding from the
  carrier and continue without Human input;
- facts differ but Goal/boundaries still hold → revise the route and continue;
- evidence requires changed behavior/boundary or exposes materially different
  Goals → stop before affected modification and return to Intent Take;
- a branch remains unresolved → park it and continue independent safe work;
- no safe route remains → BLOCK with the exact missing condition.

Task 0 settles execution-only reality and handoff alignment; it does not decide
whether behavior may change.
```

## S6 — Executor understanding disagrees with the carrier

```markdown
Status: Executable

## Goal
Fully migrate all consumers to the canonical parser and delete the legacy
parser while preserving the confirmed behavior.

## Task 0 — handoff alignment
Before modification, the executor records its understood Goal, first route, and
main risk. Compare that receipt with the carrier.

Expected routing for the observed disagreement:
- If the executor says it will keep a compatibility wrapper or migrate only the
  known streaming consumer, while the carrier clearly requires complete
  migration and deletion, treat this as executor misunderstanding. Rebind to the
  carrier, correct the receipt, and continue; do not Ask Human.
- If repository evidence proves complete deletion cannot preserve a confirmed
  boundary, the issue is no longer misunderstanding. Stop affected work before
  modification and return to Intent Take with the exact conflict.

Task 0 exists here because the disagreement appears only at handoff. It closes a
misread early without giving the executor authority to rewrite the Goal.
```

## S7 — Compile-visible boundary conflict must not be deferred

```markdown
Status: Unresolved Intent

Current understanding:
- The requested result is complete deletion of the legacy parser.
- Confirmed boundaries require the public API and batch behavior to remain and
  the protected schema not to change.
- Compile-time grounding already proves deletion cannot satisfy all three.

Human decision needed:
1. Preserve API/schema and retain a compatibility surface, so complete physical
   deletion is not achieved.
2. Authorize a public API change so deletion can complete.
3. Authorize the protected schema change needed for deletion while preserving
   the API.

Do not emit Task 0. The conflict is already known and each option changes intent
or a confirmed boundary.
```

## S8 — Global non-intent blocker

```markdown
Status: Blocked

Stable Intent is clear, but the named private repository and required build
runtime are unavailable to both compiler and executor. No Task 0, inspection,
implementation, or independent safe evidence-producing work can begin.

Resolving condition:
Provide executor access to the authoritative repository and build environment,
or bind an equivalent workspace containing the source, governing constraints,
and verifier. This is an access/capability blocker, not an intent question.
```

## S9 — Branch-local blocker with safe progress

```markdown
Status: Executable

## Goal
Continue all independent safe preparation while preserving the inaccessible
migration branch and its exact unresolved condition.

## State and route
- Branch A cannot access its governing verifier. Park it and record the missing
  verifier/access condition.
- Consumer inventory and protected-baseline capture are independent and may
  proceed.
- Use Task 0 for any execution-only baseline or command assumptions that must be
  settled before those safe activities.
- Do not turn a branch-local blocker into global `Status: Blocked` or a Human
  intent question.
```

## S10 — Simple direct task needs no Task 0

```markdown
Status: Executable

## Goal
Rename the specified private local variable in the named file without changing
behavior, then run the existing focused unit test.

## Execution
Edit the named occurrence, run the supplied focused test, inspect the diff, and
report the result. Use one direct action/check loop.

No Task 0, Graph, durable state, separate controller, or Human question is
needed: the target, requested result, boundary, command, and success condition
are already explicit and the change is local and reversible.
```
