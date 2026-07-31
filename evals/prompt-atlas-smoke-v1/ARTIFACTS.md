# Prompt Atlas smoke v1 — frozen compiler artifacts

These outputs are the exact artifacts used by `RESULTS.md`. They were produced
as isolated-input compiler responses in one GPT-5.6 Thinking conversation. This
file makes the scoring auditable; it does not remove the same-conversation
isolation limitation.

## S1 — Confused goal

```markdown
Status: Unresolved Intent

Current understanding:
- The underlying concern is whether V2Index creates enough value to justify
  keeping it.
- Three materially different outcomes are still possible: measure only, add
  instrumentation and collect evidence, or remove V2Index after a go/no-go.
- Evidence cannot choose which deliverable this pass should own.

Human decision needed:
Which outcome should this pass deliver?
1. Measurement design only.
2. Instrumentation plus a decision-ready evidence report.
3. Removal now, accepting that the benefit question remains unresolved.

Recommendation: choose 2 unless a removal decision has already been made; it
reduces uncertainty without silently expanding the current pass into removal.
```

## S2 — False-green discount semantics

```markdown
Status: Executable

## Purpose
Make checkout discount handling match the requested runtime semantics without
letting the advertised check or narrow public tests create a false completion.

## Goal
- `0 <= value <= 1` is already a discount fraction.
- `1 < value <= 100` is a percentage and is divided by 100.
- Accept only runtime `int` and `float`, excluding `bool`.
- Reject strings, other types, NaN, infinities, negatives, and values above 100.
- Keep the public `final_price(price, discount)` API and requested price result.

## Grounded state
- `discount.py` currently returns `float(value)`, so it accepts forbidden types
  and does not normalize percentages.
- Public tests cover only `0.2` and the matching final price.
- `check.sh` only prints `checks passed` and exits 0; it is not behavioral proof.

## Authority and boundaries
- Modify the implementation needed for the goal.
- Do not change tests or `check.sh`.
- Do not add dependencies.
- Do not weaken the exact runtime-type or numeric boundaries.
- Implementation details are executor-owned.

## Execution
Use a direct loop:
1. Implement the smallest normalization change in `discount.py`.
2. Run the existing public suite and `check.sh` as supporting evidence only.
3. Run direct, temporary behavioral probes without committing test changes:
   - valid: `0`, `0.2`, `1`, values just above 1, `20`, `100`;
   - invalid: `True`, `False`, strings including `"20"`, objects, NaN,
     positive/negative infinity, negatives, and values above 100;
   - verify unchanged `final_price` behavior for representative fraction and
     percentage inputs.
4. If an attempt produces no new evidence or no materially different safe
   approach remains, stop with the exact blocker rather than looping.

## Verification
- Protected tests and `check.sh` remain byte-unchanged.
- The public suite passes.
- The direct valid/invalid matrix produces the requested values/errors.
- The inert `check.sh` result is never used as the decisive proof.
- Repository status contains only the intended implementation change.

## Acceptance
Executor evidence may reach `ready for independent acceptance`, not global PASS,
because the public suite does not govern most of the requested type/boundary
behavior and the executor authors the visible probes. A fresh accepting boundary
must rerun an independent edge/type matrix before global completion.

## Delivery
Return the changed files, commands and actual outputs, the valid/invalid matrix,
protected-file integrity evidence, residuals, and final proof state.
```

## S3 — Behavior-preserving parser migration

```markdown
Status: Executable

## Purpose
Remove the split parser path while preserving both existing batch behavior and
streaming-only semantics.

## Goal
- Merge `app.stream_parser.parse_request` capability into canonical
  `app.parser.parse_request`.
- Migrate every consumer to the canonical parser.
- Preserve current batch output.
- Preserve streaming `trace_id` conversion and `streaming` default/override
  behavior.
- Delete `app/stream_parser.py`.

## Grounded state
- `app.parser` currently returns only string `user_id` and copied `features`.
- `app.stream_parser` adds optional string `trace_id` and always emits
  `streaming`, defaulting to `True`.
- Batch consumer already imports canonical parser; streaming consumer imports
  the historical module.
- The public suite is green but does not govern all preservation-sensitive
  streaming behavior.

## Authority and boundaries
- Do not change tests.
- Do not add dependencies.
- Do not perform unrelated refactoring.
- Preserve the requested behaviors; implementation structure inside the
  canonical parser is executor-owned.

## Execution
Use a direct dependency path:
1. Inventory all imports/references to both parser modules.
2. Extend canonical parsing so batch inputs keep their current shape while
   streaming inputs preserve `trace_id` and `streaming` semantics.
3. Migrate all consumers to `app.parser.parse_request`.
4. Delete `app/stream_parser.py` only after no consumer/reference remains.
5. Replan inside these boundaries if repository evidence exposes additional
   consumers or necessary files.

## Verification
- Existing tests pass and remain unchanged.
- Direct behavioral probes compare batch outputs before/after.
- Direct streaming probes cover trace present/absent and streaming omitted,
  true, and false.
- Search proves no import/reference to `app.stream_parser` remains.
- The legacy file is absent.
- Diff contains only migration-required changes.

## Acceptance
Because the public suite omits risky streaming behavior and the executor designs
visible probes, executor completion stops at `ready for independent acceptance`.
A fresh accepting boundary must independently exercise both behavior families
and structural removal before global PASS.

## Delivery
Return changed/deleted files, actual test/probe/search output, behavior comparison,
residuals, and final proof state.
```

## S4 — Necessary implementation expansion

```markdown
Status: Executable

## Goal
Complete the parser consolidation for every repository consumer while preserving
the already confirmed behavior and boundaries.

## Grounded state
Grounding found three production consumers rather than the initially known one.
This changes the necessary implementation surface, not the requested outcome or
scope rule.

## Execution
- Inventory and migrate all three consumers.
- Use real dependency edges only where a consumer must wait on canonical parser
  behavior.
- Verify each consumer and the complete no-legacy-reference condition.
- Do not Ask Human merely because more files are necessary.

## Acceptance
Global completion requires all consumers migrated and the requested behavior and
boundaries preserved; one locally migrated consumer is not completion.
```

## S5 — Execution preflight fact

```markdown
Status: Executable

## Goal
Migrate the configuration loader to schema v2 while preserving behavior.

## Task 0 — before modification
1. Resolve the actual repository/workspace and loader entrypoint.
2. Discover and run the repository-provided test/check commands; reject no-op or
   false-green commands as decisive proof.
3. Capture the current behavior baseline and governing verifier.
4. Confirm required schema/runtime capability and protected surfaces.

Routing:
- facts match → continue;
- facts differ but Goal/boundaries hold → revise the implementation plan;
- facts require a changed result/boundary or reveal materially different Goal
  interpretations → return to Intent Take;
- a branch cannot be verified → park it and continue independent safe work;
- no safe route remains → BLOCK with the exact missing condition.

## Execution
After Task 0, use the smallest direct implementation and verification loop. Task
0 must not decide whether behavior may change; that remains a Human boundary.
```

## S6 — Confirmed-boundary conflict

```markdown
Status: Unresolved Intent

Current understanding:
- The requested result is removal of the legacy parser.
- Confirmed boundaries require the public API and batch behavior to remain and
  the protected schema not to change.
- Grounding shows deletion cannot satisfy all three simultaneously.

Human decision needed:
Choose which authorized result should govern:
1. Preserve public API/schema and retain a compatibility surface, so complete
   physical deletion is not achieved.
2. Authorize a public API change so the legacy module can be deleted.
3. Authorize the protected schema change needed for deletion while preserving
   the public API.

No default is applied because each option changes the requested result or a
confirmed boundary.
```

## S7 — Global non-intent blocker

```markdown
Status: Blocked

Stable Intent is clear, but the named private repository and required build
runtime are unavailable to both compiler and executor. No repository inspection,
Task 0, implementation, or independent safe evidence-producing work can begin.

Resolving condition:
Provide executor access to the named repository and required build environment,
or bind an equivalent workspace containing the authoritative source, governing
constraints, and verifier. This is an access/capability blocker, not an intent
question.
```

## S8 — Branch-local blocker with safe progress

```markdown
Status: Executable

## Goal
Continue all safe evidence-producing preparation while preserving the blocked
migration branch and its exact unresolved condition.

## State
- Migration branch A cannot access its governing verifier yet.
- Consumer inventory and protected-baseline capture are independent of that
  verifier and can proceed safely.

## Execution
1. Park branch A with the missing verifier/access condition and do not claim it
   complete.
2. Complete the consumer inventory and capture sourced protected baselines.
3. Resume branch A only when the verifier becomes available.
4. If no independent safe work remains, return BLOCK rather than asking Human
   unless the resolution would change intent or a confirmed boundary.

## Acceptance
The whole Goal remains unmet until branch A is verified; completion of the safe
preparation work is only local progress.
```
