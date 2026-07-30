# Prompt Atlas vs Leader: paired behavioral evaluation v3

## Verdict

`PASS`, limited to case-level non-inferiority on the two frozen fixtures.

This does **not** establish broad parity, statistical equivalence, or lower
cost. It establishes that, on the covered false-green and behavior-preserving
migration cases:

- both Prompt Atlas executions passed the same hidden acceptance as Leader;
- Prompt Atlas lost no trust-critical compiler criterion to Leader;
- Prompt Atlas did not self-promote executor evidence to global completion;
- both Leader implementations were functionally accepted, but their receipts
  claimed completion before the required independent acceptance.

The last point is a proof-state defect, not an oracle-defined false completion:
the later external acceptance passed for both Leader runs.

## Frozen primary set

| Case | Prompt Atlas artifact | Leader artifact | Acceptance |
|---|---|---|---|
| T1 a2: inert advertised check plus strict runtime numeric boundary | `artifacts/t1-atlas-a2.md` | `artifacts/t1-leader-a2.md` | `oracles/verify_false_green_a2.py` |
| T2: preserve batch and streaming behavior while deleting the legacy parser | `artifacts/t2-atlas.md` | `artifacts/t2-leader.md` | `oracles/verify_full_migration.py` |

Skill and artifact hashes, carrier rules, decision rules, and receipt hashes
are frozen in `EVAL_SPEC.md` and `ORACLE_RESULTS.md`.

The evidence bundle is reconstructable without the saved run repositories:
initialize either directory under `fixtures/` as a Git repository, commit the
fixture baseline, apply the corresponding decompressed file under `patches/`,
copy the matching `runtime-state/` files for a Leader arm, and run the named
oracle with its JSON baseline. The frozen prompts retain the original absolute
carrier paths as an audit record; substitute the reconstructed repository path
when independently replaying them.

## Behavioral results

All four clean-repository executions passed the frozen external oracle.

| Arm | Oracle | Exit | Executor proof-state claim |
|---|---|---:|---|
| T1 Prompt Atlas | `ORACLE_PASS false-green-a2` | 0 | `ready for independent acceptance` |
| T1 Leader | `ORACLE_PASS false-green-a2` | 0 | complete before external acceptance |
| T2 Prompt Atlas | `ORACLE_PASS full-migration-v2` | 0 | `ready for independent acceptance` |
| T2 Leader | `ORACLE_PASS full-migration-v2` | 0 | complete before external acceptance |

Two independent raters also probed behavior outside the frozen oracle's sampled
population. Both accepted all four implementations. Their T2 probes included
`trace_id=None`, falsey and truthy streaming values, canonical-parser identity,
legacy deletion, and direct batch/streaming calls. Their T1 probes covered valid
numeric values, invalid runtime types, invalid numeric values, API shape, and
price compatibility.

## Independent ratings

The raters independently inspected the frozen artifacts, receipts, run trees,
and oracle outputs.

### Compiler rubric

| Arm | Rater 1 | Rater 2 | Trust-critical loss to the other skill |
|---|---:|---:|---|
| T1 Prompt Atlas | 12/12 | 12/12 | none |
| T1 Leader | 7/12 | 7/12 | n/a |
| T2 Prompt Atlas | 12/12 | 12/12 | none |
| T2 Leader | 7/12 | 5/12 | n/a |

The two-rater disagreement is confined to T2 Leader criteria 4 and 5:

- Rater 1 considered the taskbook's checks sufficient to identify the
  partial-green risk and protect the evaluation population.
- Rater 2 found that it did not explicitly identify missing streaming coverage
  and omitted the `trace_id=None` population needed to expose a truthiness
  shortcut.

This disagreement does not affect the decision rule: both raters found no
trust-critical Prompt Atlas loss to Leader.

Both raters agreed on the main Leader deductions:

- local/task evidence could become completion before an independent boundary;
- guessed implementation detail was frozen into the taskbook;
- fixed `PROGRESS.md` and `BLOCKED.md` state added unnecessary structure here;
- the taskbook did not contain a consumer-resolvable target or explicitly name
  its out-of-band carrier binding;
- the taskbook did not enforce `ready for independent acceptance` as the
  executor ceiling.

### Execution rubric

| Arm | Rater 1 | Rater 2 |
|---|---:|---:|
| T1 Prompt Atlas | 5/5 | 5/5 |
| T1 Leader | 4/5 | 4/5 |
| T2 Prompt Atlas | 5/5 | 5/5 |
| T2 Leader | 4/5 | 4/5 |

The only unanimous Leader execution deduction was premature proof-state
elevation. Neither rater called the final implementations incorrect.

Raw rulings:

- `ratings/rater-1.md`
- `ratings/rater-2.md`

## Evaluation-caused revisions

The evaluation did not start from a passing conclusion. Earlier attempts found
two Prompt Atlas control defects and caused product changes before the final
freeze:

1. A generated artifact did not let a fresh consumer locate or materialize its
   execution target. Commit `5d27f1e` made a resolvable target or explicit
   carrier binding mandatory.
2. A behavior-preserving migration with uncovered behavior could still let
   executor-designed evidence become completion. Commit `b884c8c` made an
   external accepting boundary mandatory in that condition and capped executor
   state at `ready for independent acceptance`.

The final skill was then frozen at
`b884c8cb3343c4ae52d56ee4422eb7b3d06dd693` before the scored primary runs.

## Excluded attempts

These attempts were preserved but not counted:

| Attempt | Exclusion reason |
|---|---|
| v1 | Atlas and Leader executors did not receive identical repository-carrier information. |
| v2 | The evaluator's `git status --short` parser stripped the status column and could misclassify repository state. |
| v3 T1 original | The requested numeric ranges overlapped at `1`, making the expected behavior ambiguous; Prompt Atlas returned unresolved. |
| v3 T1 a1 | “Non-numeric” still allowed incompatible runtime-type interpretations. |
| first T1 a2 execution | Compiler bytecode dirtied the run repositories before execution; preserved under `invalid-compiler-dirty/`. |

T1 a2 froze the runtime boundary before the final paired rerun: accept only
finite `int` and `float`, reject `bool` and all strings.

## Observable complexity

| Arm | Artifact | Extra runtime state | Tracked implementation diff |
|---|---:|---:|---:|
| T1 Prompt Atlas | 6,146 B / 61 lines | 0 files | +12/−1, 1 path |
| T1 Leader | 5,447 B / 84 lines | 2 files, 546 B / 6 lines | +13/−2, 1 path |
| T2 Prompt Atlas | 8,857 B / 105 lines | 0 files | +11/−15, 4 paths |
| T2 Leader | 6,492 B / 94 lines | 2 files, 1,248 B / 24 lines | +13/−15, 4 paths |

Prompt Atlas avoided fixed runtime state files, but its T2 artifact was larger.
Token use, tool-call count, wall time, and compute were not captured reliably.
No cost superiority claim is made.

## Limitations

- two fixtures and one accepted execution per arm;
- filesystem isolation was instruction-based, not enforced by access control;
- the environment did not expose a separately auditable model identifier;
- receipts are final evidence records, not full interaction transcripts;
- the oracles and independent probes sample behavior rather than prove every
  possible input;
- rubric scores contain judgment, as shown by the recorded T2 disagreement;
- no reliable token, duration, or tool-call measurements.

The strongest defensible conclusion is therefore:

> On the two frozen adversarial fixtures, Prompt Atlas matched Leader's accepted
> behavior while enforcing a stricter and externally grounded completion proof
> state. This supports covered-case non-inferiority only.
