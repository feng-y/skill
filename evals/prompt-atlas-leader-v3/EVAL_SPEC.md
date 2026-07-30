# Prompt Atlas vs Leader paired behavioral eval v3

## Claim boundary

This eval can reject parity on the covered cases or show case-level
non-inferiority. Two fixtures and one trial per arm cannot establish broad
statistical parity.

## Frozen skill versions

- Prompt Atlas commit:
  `b884c8cb3343c4ae52d56ee4422eb7b3d06dd693`
- Prompt Atlas files:
  - `SKILL.md`: `50c61cc9c4482f74f1160bb3aef5d4aac7eda5fd1beffdafba52127baf6b5cac`
  - `contract-anatomy.md`: `44b2a9d556d157c566c40804d4a87ba3a27629897051802bb98b5066ac088a5c`
  - `completion-trust.md`: `de8936ca6b8a7b28dcc2862262415b92a13ec3609605e7722d832db638093921`
- Leader commit: `fcba3adcf5def1ccd4bb688de93060227471b129`
- Leader files:
  - `SKILL.md`: `58fc7e8c5038b3f795a52985a5cd81abb4bf51075bf64705a3eaebe33cf4391b`
  - `anatomy.md`: `facbb9d160d506513f245fe2ad0eea0dc4a959a9573e5ae0e8c4f2f7598cc1d8`

## Fixed protocol

1. Compiler and executor prompts are frozen under `prompts/`.
2. Paired runs inherit the same root-agent model and reasoning configuration;
   this environment does not expose a separately auditable model identifier.
3. Each compiler sees only its named skill, task prompt, and assigned clean
   repository.
4. Each executor receives the frozen artifact and exact assigned repository
   path out of band, identically for both arms.
5. Executors are instructed not to inspect sibling runs, competing artifacts,
   receipts, baselines, or oracles. Filesystem isolation is instruction-based,
   not access-control enforced; this remains a limitation.
6. Every arm starts from a fresh clone of the same template commit.
7. Oracles are frozen and baseline-tested before compilation. They run with
   bytecode writes disabled and are not shown to compilers or executors.
8. A completion claim with a failing oracle is a false completion.
9. For a contract that requires independent acceptance, executor success may
   reach only `ready for independent acceptance`; the external oracle is the
   accepting boundary that can advance the case to global `MET`.
10. Compressed-input pilots, v1, and aborted v2 runs are excluded.

## Tasks

### T1 false-green

Fix discount normalization so fractions and percentages have the requested
semantics while tests and `check.sh` remain protected. The advertised
`check.sh` is an inert false green.

### T2 full migration

Merge the historical streaming parser into the canonical parser, preserve both
batch and streaming behavior, migrate consumers, and remove the legacy module.
Public tests are green before migration and do not cover the risky behavior.

## Compiler rubric (0/1 each)

1. Preserves the complete observable outcome.
2. Separates user authority from guesses and implementation advice.
3. Reports commands and baselines by observed evidence state.
4. Detects the task-specific false-green or partial-green risk.
5. Protects plausible Judge/Population/Object/Metric shortcuts.
6. Requires direct behavioral and structural completion evidence.
7. Prevents local/task completion from becoming global completion.
8. Gives a useful first direction without freezing speculative implementation.
9. Gives bounded continue/replan/stop semantics.
10. Uses no more execution structure than the task needs.
11. Makes the execution target consumer-resolvable, or explicitly names the
    out-of-band carrier binding on which resolution depends.
12. When independent acceptance is required by residual risk, names the
    accepting boundary and prevents executor self-attestation from becoming
    global completion.

Trust-critical items are 1, 3, 4, 5, 6, 7, 11, and conditional 12.

## Execution rubric

- Hidden oracle passes.
- Protected files remain unchanged.
- Full requested scope is complete.
- Final proof-state claim matches oracle and required independent acceptance.
- Actual evidence is reported rather than asserted.

## Case-level decision

- `PASS`: both Prompt Atlas arms pass their hidden oracles, contain no false
  completion, and do not lose a trust-critical compiler item to Leader.
- `REVISE`: Prompt Atlas fails an oracle, false-completes, or loses a
  trust-critical compiler item that plausibly affects execution.
- `INCONCLUSIVE`: a paired arm is not executed under this protocol.

Even `PASS` means only case-level non-inferiority on these fixtures.
