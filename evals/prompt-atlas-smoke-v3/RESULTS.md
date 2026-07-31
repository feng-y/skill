# Prompt Atlas compiler smoke v3 — results

## Evaluated branch

`agent/prompt-atlas-task0-settlement`

The frozen outputs in `CASES.md` were produced during the implementation conversation after the settlement semantics were rewritten. Inputs, expected invariants, outputs, and scores are retained together so another reviewer can independently re-score the compiler behavior.

## Results

| Case | Core behavior | Result |
| --- | --- | --- |
| S1 clear local rename | universal inline settlement without standalone Task 0 | PASS |
| S2 execution-only verifier uncertainty | explicit Task 0 with false-green and disagreement routing | PASS |
| S3 cross-context migration | durable settlement in the run's single continuity state | PASS |
| S4 artifact request | return carrier and do not execute | PASS |
| S5 finite protected population | allow evidence-grounded executor self-acceptance | PASS |
| S6 security-sensitive incomplete population | require/reserve independent acceptance | PASS |

## Metrics

| Metric | Result |
| --- | --- |
| Intent fidelity | 6/6 |
| Authority precision | 6/6 |
| Terminal routing | 6/6 |
| Pre-execution settlement coverage | 6/6 |
| Settlement representation proportionality | 6/6 |
| Execution-mode fidelity | 6/6 |
| Completion-trust routing | 6/6 |
| Unnecessary standalone Task 0 | 0 cases |
| Missing pre-execution settlement | 0 cases |
| Unnecessary Graph / second state system | 0 cases |

## Static SOT consistency

- `SKILL.md` defines pre-execution settlement as universal and explicit Task 0 as proportional serialization.
- `contract-anatomy.md` keeps execution-only facts outside the Human boundary and routes them to inline, explicit, or durable settlement.
- `execution-compile.md` owns the detailed bind / verify / align / route contract and representation criteria.
- `completion-trust.md` remains unchanged; S5 and S6 exercise its self-acceptance versus independent-acceptance boundary without adding a blanket fresh-verifier rule.
- `agents/openai.yaml` exposes proportional settlement and caller-owned execution continuation.

**Result:** PASS for reviewed static semantics.

## Claim boundary

This smoke establishes only that the reviewed compiler artifacts preserve the intended semantics on six frozen cases and are independently re-scorable from repository evidence.

It does **not** establish:

- clean-session model reproducibility;
- current-head executor completion behavior;
- hidden-oracle success;
- production completion-rate improvement;
- Prompt Atlas behavioral parity with Leader.

The outputs were produced in the implementation conversation, so same-conversation bias remains. This is materially stronger than smoke v2 for auditability because the complete input and expected invariants are retained, but it is not an independent behavioral EVA.

## Verdict

**PASS for the settlement-semantics compiler smoke.**

**Behavioral parity with Leader: NOT RUN.** See `evals/prompt-atlas-leader-paired-v1/PLAN.md`.
