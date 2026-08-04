# Prompt Atlas PR #20 smoke results

## Verdict

`PASS`, limited to the six frozen compiler cases in `EVAL_SPEC.md` and the
current-source contract checks in `check_artifacts.py`.

PR #20 preserves current compile-state and completion-trust behavior on the
covered cases while adding the intended execution-graph compilation behavior:

- simple and broad-linear work remains linear;
- a real fork/join is rendered as ordinary Tasks rather than Graph DSL;
- direct edges are limited to result consumption, safe-execution prerequisites,
  and downstream evidence invalidation;
- shared mutable surfaces have one owner;
- branches rejoin before complete-Goal acceptance;
- one Goal remains one authoritative taskbook;
- branch-local blockers, Unresolved Intent, and independent-acceptance ceilings
  retain their prior semantics;
- taskbook compilation omits inactive detail and runtime control mechanisms;
- authority boundaries cover dependency, permission, external-write, destructive,
  and irreversible operations when file scope alone is insufficient;
- a required Task 0 exposes Executor misunderstanding before material change.

This is not execution evidence, statistical performance evidence, or broad
Leader parity.

## Deterministic smoke

Frozen artifact smoke previously produced:

```text
PR20_SMOKE_PASS cases=6 executable=5 unresolved=1
```

The six artifacts and their shape checks did not change in the final alignment.
The new current-source assertions were executed separately and produced:

```text
PR20_CURRENT_SOURCE_CONTRACT_PASS checks=9
```

The current branch could not be cloned directly in the local runner because DNS
access to GitHub was unavailable. Current source files were read through the
GitHub connector. The final two changes were source-contract refinements; no
artifact was regenerated or claimed as independent model evidence.

The checked-in checker verifies:

- direct-edge and no-transitive-edge rules;
- compilation frugality and an initial ready root;
- authority-sensitive operation boundaries;
- Task 0 opening alignment and clear-misread correction;
- runtime control remains outside the taskbook;
- all five executable artifacts use the required seven-part contract order and
  contain executable Tasks;
- S1, S3, and S6 do not expose parallel/Graph structure;
- S2 contains dependency, parallel, ownership, join, and evidence invalidation;
- no artifact exposes TaskGroup, node schema, Graph DSL, fixed Agent identities,
  or multiple taskbooks;
- S4 parks a branch-local blocker and keeps safe work executable;
- S5 remains `Unresolved Intent` and emits no executable contract;
- S6 stops at `ready for independent acceptance` and does not reveal reserved
  private-check contents.

## Manual rubric

| Criterion | Result | Evidence |
|---|---|---|
| Fixed taskbook order | PASS | S1–S4 and S6 use Contract Header through Completion and Acceptance in exact order. |
| Proportional linear default | PASS | S1 and S6 use one Task; S3 stays one aggregate linear migration despite twenty files. |
| Direct edge formation | PASS | S2 edges follow canonical-result consumption and evidence invalidation; no transitive or merely sequential edge is rendered. |
| Concrete dependency compilation | PASS | S2 compiles canonical settlement → two consumer branches → legacy-removal join. |
| Ordinary Task rendering | PASS | S2 uses `depends on`, `may run in parallel`, and `after both ... pass`; no Graph-facing schema. |
| Ownership and integration safety | PASS | Canonical, batch, and streaming write surfaces are separated; legacy deletion is gated on both branches. |
| Evidence invalidation | PASS | S2 reruns consumer evidence after a canonical interface or behavior change. |
| Initial ready work | PASS | Every Executable artifact has a Task that can begin directly or after its stated Task 0. |
| Compilation frugality | PASS | Linear cases remain compact; global facts are not repeated per Task; no scheduler, lease, or fixed Agent topology is emitted. |
| Authority-sensitive boundaries | PASS | Current contract bounds dependency changes, permissions, external writes, destructive actions, and irreversible side effects when file scope is insufficient. |
| Task 0 opening alignment | PASS | Current contract requires Goal/route/risk/disagreement receipt and corrects a clear taskbook misread without escalating to Human. |
| One-taskbook boundary | PASS | No case emits fixed Agent topology or multi-taskbook fan-out. |
| PR #19 trust/routing regression | PASS | S4 remains partial executable, S5 remains unresolved, and S6 preserves the independent-acceptance ceiling and private-check boundary. |

## Case results

| Case | Expected | Result |
|---|---|---|
| S1 simple local edit | Linear, no Task 0 ceremony or Graph | PASS |
| S2 real fork and join | Minimal dependency structure as ordinary Tasks | PASS |
| S3 broad but linear | No graph merely because scope is large | PASS |
| S4 branch-local blocker | Park branch; continue safe work | PASS |
| S5 confused architecture request | `Unresolved Intent` | PASS |
| S6 false-green acceptance | Linear; `ready for independent acceptance` | PASS |

## Review findings and repairs

The Graph enhancement was not accepted on first wording:

1. The first reference draft allowed a multiple-taskbook exception. That violated
   Prompt Atlas's one Goal → one taskbook boundary and was removed before freeze.
2. The graph reference remains short and conditional. It renders ordinary Tasks
   and forbids fixed Agent topology and multi-taskbook compilation.
3. Leader cross-review found three narrow compiler residuals: edge formation was
   implicit, compilation frugality was unstated, and no pre-Handoff invariant
   required ready work. These were repaired without adding a section or schema.
4. A second Leader hard-logic review found two execution-safety residuals:
   file-only boundaries did not explicitly cover authority-sensitive side effects,
   and Task 0 no longer required an opening alignment receipt. Both were restored
   in `execution-compile.md` without importing fixed files, `/goal`, multi-taskbook
   management, or runtime scheduling.

No additional trust-critical defect was found in the covered contract surface.

## Frozen Git blobs

- `EVAL_SPEC.md`: `e62f6276d37f68fbfd36089c73448bbabcbfc9f9`
- `ARTIFACTS.md`: `48bfc47c88a53395401f51712e78a084886a1677`
- `check_artifacts.py`: `7d67aa8ad24334a864154b2b7b3c489642fb3d2c`

## Limitations

- one GPT-5.6 Thinking conversation produced and reviewed all artifacts;
- case isolation was instructional rather than independently enforced;
- the final source-contract refinement was checked against unchanged frozen
  artifacts rather than through an independently isolated recompilation;
- the final combined checked-in command was not rerun from a fresh clone after the
  last source-only assertions because GitHub DNS access was unavailable;
- no paired base-vs-PR compiler run was executed;
- no Executor, repository fixture, hidden oracle, or fresh-context Acceptor ran;
- six cases cannot establish broad behavior or cost impact;
- the repository exposes no PR CI workflow for this head.

The strongest defensible conclusion is:

> On the six frozen compiler cases and current-source contract checks, PR #20 adds
> concise dependency structure, compilation economy, authority-sensitive
> boundaries, and pre-change alignment without over-graphing linear work or
> regressing the covered intent, blocker, one-taskbook, and completion-trust
> semantics.
