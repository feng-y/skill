# Northstar paired clean-session behavioral eval

Eval-only. This does not change Northstar runtime semantics.

## Scope

Compare a base Northstar revision with a candidate revision under isolated, otherwise identical sessions. Measure whether the candidate produces a better **resumable Northstar package** at lower cost without increasing missing intent, speculative work, unnecessary clarification, or handoff duplication. For material cross-session work, that package is the canonical Taskbook plus a delta-only session handoff.

Northstar does not own proof sufficiency judgment; `$verify` is evaluated separately. This harness stops at the first independently validated resumable Taskbook + handoff package.

## Valid handoff

A resumable package is valid when a fresh worker can read the canonical Taskbook, apply the short session delta, and safely start the next material task without recovering missing Human intent, materially redefining Problem / Draft / Constraints / Acceptance, or inventing completion criteria.

For material cross-session work:

- Taskbook carries the complete durable Intent / Draft, binding decisions, Acceptance, material work/status, and next owner;
- session handoff carries only resume delta: Taskbook pointer, last/current task, live blocker/decision, next task/owner, and return-to-Northstar judgment point;
- Drafted Issue may track/reference the canonical Taskbook, but must not duplicate it as a second plan.

The package is not required to contain Goal, explicit Graph, proof commands, backend configuration, or a replay of the original conversation. A long handoff that repeats Taskbook content is a failure, not a more complete handoff.

## Pair setup

For every case:

1. pin the target repo to an immutable commit and freeze the exact user prompt;
2. use the same Human response policy, model/reasoning config, tool permissions and host config for both arms;
3. start each arm in a fresh session with no carry-over;
4. preserve candidate Taskbook + handoff packages plus timing/token/tool counters;
5. give each package to a separate fresh worker probe; only the independent probe may set `handoff_validated=true`;
6. one pair per case is smoke; behavioral claims require at least 5 real cases and 3 clean-session repeats per arm per case.

The frozen set should cover at least: clear direct Intent, bounded/local concrete-shape ambiguity, territory unknown, architecture pressure, complex material dependency, delta-only cross-session handoff, and a case where Acceptance is clear but verification should be delegated to Verify rather than embedded in Intent.

Execution orchestration / control-plane behavior is outside this eval. Verification backend choice, including DaVinci Replay, is also outside Northstar handoff quality unless Northstar incorrectly hardcodes it into Intent.

## Existing JSONL schema

The existing scorer schema is retained for continuity.

`compiled_work` means **material work represented by the canonical Taskbook**, not necessarily work newly compiled by Northstar. `evidence_supported=false` means the Taskbook invents a material cut / dependency without current decision-relevant support. The field name is retained for scorer compatibility; it does not mean the session handoff should contain the work plan.

`executor_reinterpretation=true` when the fresh worker cannot recover the intended change from Taskbook + handoff without materially redefining the boundary or inventing completion criteria. Ordinary implementation discovery is not reinterpretation.

`clarifications[].contract_changing=false` marks a question whose answer could not change Problem, Draft, binding Constraint, Acceptance, material work judgment, or Human commitment.

Use the existing `results.example.jsonl` only as schema smoke data, not behavioral Evidence.

## Metrics

The scorer reports:

- validated resumable-package rate;
- first resumable-package latency;
- unnecessary clarification rate;
- speculative task rate;
- Executor reinterpretation rate;
- token/tool cost to first validated handoff.

Run:

```bash
python3 evals/northstar-paired/score.py <results.jsonl>
```

## Decision rule

Keep the existing non-regression guardrails: quality rates must not regress materially, and latency/token/tool cost must stay within configured tolerance. Claim efficiency improvement only when at least one efficiency metric improves without violating quality guardrails.

If sample size is insufficient or repeated runs disagree materially, report measurements and keep the behavioral conclusion `INCONCLUSIVE`.

## What this eval does not prove

It does not prove implementation quality after execution, Verify quality, Architecture Evolution quality, or low-level orchestration quality. It measures whether Northstar produces a canonical Taskbook plus non-duplicative resume handoff that a fresh worker can safely continue from.
