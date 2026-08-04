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
- Task 0 remains conditional and, when required, exposes Executor misunderstanding
  before material change.

This is not execution evidence, statistical performance evidence, or broad
Leader parity.

## Deterministic smoke

The current GitHub blobs were reconstructed locally because the runner could not
resolve `github.com` for a direct clone. The checked-in command was then run with
system Python:

```bash
/usr/bin/python3 evals/prompt-atlas-pr20-smoke/check_artifacts.py
```

Observed output:

```text
PR20_SMOKE_PASS cases=6 executable=5 unresolved=1
```

Reverse validation intentionally replaced the conditional rule with the old
unconditional sentence `Task 0 runs before material change.`. The checker exited
non-zero (`rc=1`), proving this regression is now detected.

The checker verifies:

- direct-edge and no-transitive-edge rules;
- compilation frugality and an initial ready root;
- authority-sensitive operation boundaries;
- conditional Task 0, opening alignment, and clear-misread correction;
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
| Conditional Task 0 | PASS | S1 remains free of Task 0 ceremony; required Task 0 retains Goal/route/risk/disagreement alignment. |
| Task 0 reverse validation | PASS | Reintroducing the unconditional sentence makes the checker fail. |
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

1. The first Graph reference draft allowed a multiple-taskbook exception. That
   violated Prompt Atlas's one Goal → one taskbook boundary and was removed.
2. Leader compiler cross-review found three narrow residuals: edge formation was
   implicit, compilation frugality was unstated, and no pre-Handoff invariant
   required ready work. These were repaired without adding a section or schema.
3. Leader hard-logic review found two execution-safety residuals: file-only
   boundaries did not explicitly cover authority-sensitive side effects, and
   Task 0 no longer required an opening alignment receipt. Both were restored.
4. Final cross-file review found the restored Task 0 sentence had accidentally
   become unconditional, contradicting S1, `SKILL.md`, and the declared PR boundary.
   It was narrowed to `When Task 0 is required...`, and the checker now rejects
   recurrence of the unconditional wording.

No additional trust-critical defect was found in the covered contract surface.

## Frozen Git blobs

- `EVAL_SPEC.md`: `aa66fa2cfc06ab87e6b19b79818b10bbe1b44ca9`
- `ARTIFACTS.md`: `48bfc47c88a53395401f51712e78a084886a1677`
- `check_artifacts.py`: `cd9e989ea92e595e3b1af5dcac8343b034ba2c37`

## Limitations

- one GPT-5.6 Thinking conversation produced and reviewed all artifacts;
- case isolation was instructional rather than independently enforced;
- the final contract refinement was checked against unchanged frozen artifacts
  rather than through an independently isolated recompilation;
- the current GitHub blobs were reconstructed through the connector rather than
  cloned because DNS access to GitHub was unavailable;
- no paired base-vs-PR compiler run was executed;
- no Executor, repository fixture, hidden oracle, or fresh-context Acceptor ran;
- six cases cannot establish broad behavior or cost impact;
- the repository exposes no PR CI workflow for this head.

The strongest defensible conclusion is:

> On the six frozen compiler cases and current-source contract checks, PR #20 adds
> concise dependency structure, compilation economy, authority-sensitive
> boundaries, and conditional pre-change alignment without over-graphing linear
> work or regressing the covered intent, blocker, one-taskbook, and
> completion-trust semantics.
