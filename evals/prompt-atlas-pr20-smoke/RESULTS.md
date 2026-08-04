# Prompt Atlas PR #20 smoke results

## Verdict

`PASS`, limited to the six frozen compiler cases in `EVAL_SPEC.md`.

PR #20 preserves current compile-state and completion-trust behavior on the
covered cases while adding the intended execution-graph compilation behavior:

- simple and broad-linear work remains linear;
- a real fork/join is rendered as ordinary Tasks rather than Graph DSL;
- shared mutable surfaces have one owner;
- branches rejoin before complete-Goal acceptance;
- upstream interface change invalidates downstream evidence;
- one Goal remains one authoritative taskbook;
- branch-local blockers, Unresolved Intent, and independent-acceptance ceilings
  retain their prior semantics.

This is not execution evidence, statistical performance evidence, or broad
Leader parity.

## Deterministic smoke

Command:

```bash
python3 evals/prompt-atlas-pr20-smoke/check_artifacts.py
```

Observed output:

```text
PR20_SMOKE_PASS cases=6 executable=5 unresolved=1
```

The checker verifies:

- all five executable artifacts use the required seven-part contract order;
- S1, S3, and S6 do not expose parallel/Graph structure;
- S2 contains the required dependency, parallel, ownership, join, and evidence
  invalidation relationships;
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
| Concrete dependency compilation | PASS | S2 compiles canonical settlement → two consumer branches → legacy-removal join. |
| Ordinary Task rendering | PASS | S2 uses `depends on`, `may run in parallel`, and `after both ... pass`; no Graph-facing schema. |
| Ownership and integration safety | PASS | Canonical, batch, and streaming write surfaces are separated; the legacy deletion is gated on both branches. |
| Evidence invalidation | PASS | S2 explicitly reruns consumer evidence after a canonical interface/behavior change. |
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
   Prompt Atlas's one Goal → one taskbook boundary and was removed before this
   freeze.
2. The final compiler reference is 13 lines and remains conditional. It instructs
   Prompt Atlas to render ordinary Tasks and forbids fixed Agent topology and
   multi-taskbook compilation.

No additional trust-critical defect was found by the frozen smoke.

## Frozen hashes

- `EVAL_SPEC.md`: `8ff53ef3c83da5b938e6576643a0b4d85b2d94b7dda93e6a70cb09af1dde3ce1`
- `ARTIFACTS.md`: `8ae87d579532215fa8679f12ffb101c476bab3293a6e6fcdf59c98381f329f17`
- `check_artifacts.py`: `33227d687f730645207597175d47227feea0dff4a443bb423e6992e93c2ad023`

## Limitations

- one GPT-5.6 Thinking conversation produced and reviewed all artifacts;
- case isolation was instructional rather than independently enforced;
- no paired base-vs-PR compiler run was executed;
- no Executor, repository fixture, hidden oracle, or fresh-context Acceptor ran;
- six cases cannot establish broad behavior or cost impact;
- the repository exposes no PR CI workflow for this head.

The strongest defensible conclusion is:

> On the six frozen compiler cases, PR #20 adds concise compile-time dependency
> structure without over-graphing linear work or regressing the covered intent,
> blocker, one-taskbook, and completion-trust semantics.
