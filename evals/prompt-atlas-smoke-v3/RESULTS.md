# Prompt Atlas compiler smoke v3 — results

## Evaluated branch and semantic snapshot

`agent/prompt-atlas-task0-settlement`

- `skills/prompt-atlas/SKILL.md` blob: `352013cfc4279bd8288ee146957620ae4c8fabb9`
- `skills/prompt-atlas/references/contract-anatomy.md` blob: `5d846bed6fbcd43022fb64e7109ff9bc180d742e`
- `skills/prompt-atlas/references/execution-compile.md` blob: `aa447041707378dc2b5c209daf3f4f93b98a33f8`
- `skills/prompt-atlas/references/completion-trust.md` blob: `b2af67ae34bdbbc011a1bed742be4ba0fc545fa5`
- `skills/prompt-atlas/agents/openai.yaml` blob: `2e794ace901c6e575416838821cf222037665c47`

## Frozen evaluation artifacts

- `README.md` blob: `99a9a8486756cfac1e33150309e1bdc483fab75f`
- `CASES.md` index blob: `73f67a238ab77e6b999106970aed7e90d835e385`
- `cases/S1-inline-settlement.md` blob: `9cc52ce36813e3b31653c9b151a8ae00c45a8dcd`
- `cases/S2-explicit-task0.md` blob: `64d64a1c44be68b82a578703fe9b347bf4d42716`
- `cases/S3-durable-settlement.md` blob: `4d434be5ea898d25e70726eefd7d22632f0295aa`
- `cases/S4-artifact-only.md` blob: `b6ec41eb5ded229ef60ec2fe9d4a6b4e2a6422e4`
- `cases/S5-self-acceptance.md` blob: `d563ed4a013860acfc124aa528aee24a65761ae6`
- `cases/S6-independent-acceptance.md` blob: `3bd25111e74ee0e35f111be096097504ee82888d`

## Runner and rater metadata

- Date: `2026-07-31`
- Compiler runner: `GPT-5.6 Thinking`
- Rater: `GPT-5.6 Thinking`
- Generation mode: same implementation conversation; each case input was treated as isolated by instruction, but model/session isolation was not independently enforceable.
- Rating mode: same conversation after artifact generation, followed by a separate PR-diff review pass that found and repaired the original S5 false-green.
- Sampling/API parameters: not exposed or recorded in this ChatGPT runtime.
- Repository execution: not performed; this is compiler-output evaluation only.

The artifacts are independently re-scorable from the frozen inputs, invariants, outputs, and blobs. They are not independently reproducible model runs because a clean runner session, exact sampling parameters, and a second isolated rater were not used.

## Results

| Case | Core behavior | Result |
| --- | --- | --- |
| S1 clear local rename | inline settlement, grounding reuse, no standalone Task 0 | PASS |
| S2 execution-only verifier uncertainty | explicit Task 0 with false-green and disagreement routing | PASS |
| S3 cross-context migration | durable settlement in the run's single continuity state | PASS |
| S4 artifact request | return carrier and do not execute | PASS |
| S5 protected structural proof | self-acceptance closes universal rejection without sample extrapolation | PASS |
| S6 security-sensitive incomplete population | require/reserve independent acceptance | PASS |

## Metrics

| Metric | Result |
| --- | --- |
| Intent fidelity | 6/6 |
| Authority precision | 6/6 |
| Terminal routing | 6/6 |
| Pre-execution settlement coverage | 6/6 |
| Settlement representation proportionality | 6/6 |
| Grounding reuse | 6/6 |
| Execution-mode fidelity | 6/6 |
| Completion-trust routing | 6/6 |
| Unnecessary standalone Task 0 | 0 cases |
| Missing pre-execution settlement | 0 cases |
| Unnecessary Graph / second state system | 0 cases |
| Universal claim closed by sampled negatives alone | 0 cases |

## Static SOT consistency

- `SKILL.md` defines pre-execution settlement as universal, proportional, and a validation of still-fresh grounded state rather than a second discovery pass.
- `contract-anatomy.md` keeps execution-only facts outside the Human boundary and routes them to proportional settlement.
- `execution-compile.md` owns bind / verify / align / route, explicit Task 0 criteria, grounding reuse, and representation proportionality.
- `completion-trust.md` remains unchanged; S5 now uses protected structural proof to close the universal claim, while S6 preserves independent acceptance for an incomplete/manipulable population.
- `agents/openai.yaml` exposes proportional settlement and caller-owned execution continuation.

**Result:** PASS for reviewed static semantics.

## Claim boundary

This smoke establishes only that the frozen compiler artifacts preserve the intended semantics on six reviewed cases and can be independently re-scored from repository evidence.

It does **not** establish:

- clean-session compiler reproducibility;
- current-head executor completion behavior;
- hidden-oracle success;
- production completion-rate improvement;
- Prompt Atlas behavioral parity with Leader.

## Verdict

**PASS for the settlement-semantics compiler smoke.**

**Behavioral parity with Leader: NOT RUN.** See `evals/prompt-atlas-leader-paired-v1/PLAN.md` and preregistered `FIXTURES.md`.
