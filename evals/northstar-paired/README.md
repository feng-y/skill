# Northstar paired clean-session behavioral eval

Eval-only. This does not change Northstar runtime semantics.

## Scope

Compare a base Northstar revision with a candidate revision under isolated, otherwise identical sessions. Measure whether the candidate produces a better **canonical Intent / Drafted Issue handoff** at lower cost without increasing missing intent, speculative work, or unnecessary clarification.

Northstar no longer owns verification/outcome judgment; `$replay` is evaluated separately. This harness stops at the first independently validated executable Intent handoff.

## Valid handoff

A handoff is valid when a fresh Executor can safely start material work without recovering missing Human intent, materially redefining Problem / Draft / Constraints / Acceptance, or inventing completion criteria.

A valid handoff may be:

- a compact Drafted Issue for a clear small/medium change;
- the same Issue enriched by `$prototype`, `$architecture-evolution`, or `$unknowns-first` results;
- an earned material execution contract when complex dependency genuinely requires compile.

It is not required to contain Goal, Taskbook, or explicit Graph.

## Pair setup

For every case:

1. pin the target repo to an immutable commit and freeze the exact user prompt;
2. use the same Human response policy, model/reasoning config, tool permissions and host config for both arms;
3. start each arm in a fresh session with no carry-over;
4. preserve candidate handoffs plus timing/token/tool counters;
5. give each handoff to a separate fresh Executor probe; only the independent probe may set `handoff_validated=true`;
6. one pair per case is smoke; behavioral claims require at least 5 real cases and 3 clean-session repeats per arm per case.

The frozen set should cover at least: clear direct Intent, concrete-shape ambiguity, territory unknown, architecture pressure, and complex material dependency. A durable cross-session Issue handoff case is strongly preferred.

Execution orchestration / control-plane behavior is outside this eval. The handoff must remain valid regardless of which system starts, routes, pauses, resumes, or retries execution.

## Existing JSONL schema

The existing scorer schema is retained for continuity.

`compiled_work` means **material work represented by the handoff**, not necessarily work newly compiled by Northstar. For a direct Issue, record its already-established material work. `evidence_supported=false` means the handoff invents a material cut / dependency without current decision-relevant support.

`executor_reinterpretation=true` when the fresh Executor must recover missing Human intent, materially redefine the intended change/boundary, or invent completion criteria before safely starting. Ordinary implementation discovery is not reinterpretation.

`clarifications[].contract_changing=false` marks a question whose answer could not change Problem, Draft, binding Constraint, Acceptance, material work judgment, or Human commitment.

Use the existing `results.example.jsonl` only as schema smoke data, not behavioral Evidence.

## Metrics

The scorer reports:

- validated executable handoff rate;
- first executable handoff latency;
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

It does not prove implementation quality after execution, Replay verification quality, Architecture Evolution quality, or orchestration/control-plane quality. It measures Northstar Intent handoff behavior only.
