# Northstar paired clean-session behavioral eval

Eval-only. This does not change Northstar / Prompt Atlas runtime semantics.

## Goal

Compare a base skill revision with a candidate revision under isolated, otherwise identical sessions and measure whether Intent take + Intent compile produces a better executable handoff at lower cost without increasing speculative or over-specified behavior.

Use the same target repo/ref, exact user prompt, Human response policy, model/reasoning configuration, tool permissions, and host configuration for both arms. Each arm starts from a fresh session with no conversation carry-over, memory, or artifacts from the other arm.

## Pair setup

For every case:

1. Freeze a real engineering task before either arm runs. Pin the target repo to an immutable commit SHA, record the exact user prompt, and store a SHA-256 of that prompt in every run record.
2. Freeze the Human intent behind the case and a response profile for clarification questions. The same Human/oracle answers both arms from that profile and does not volunteer arm-specific extra context.
3. Pin base and candidate skill revisions to immutable commit SHAs. Run `base` and `candidate` in separate clean sessions. Randomize arm order when possible.
4. Keep model/config, tool permissions, and host configuration identical. Record these as stable IDs/strings so the scorer can reject mismatched pairs. Do not reveal the other arm's output to either session.
5. Preserve every candidate Taskbook handoff with its elapsed time, token counts, and tool-call count. Do not call it executable yet.
6. Give each candidate Taskbook to a fresh Executor session with the same target repo/ref. Independently judge whether the Executor can safely start material work without redoing Human intent judgment, redefining material boundaries, or inventing completion proof. Set `handoff_validated=true` only for a handoff that passes this gate.
7. When several handoff candidates exist in one session, the first executable handoff is the earliest candidate that independently validates. Record latency/token/tool fields to that validated handoff. If no candidate validates, set `handoff_validated=false`; the handoff latency/token/tool fields may be `null` and are excluded from efficiency aggregates.
8. For a smoke comparison, one pair per case is enough. For a behavioral-uplift claim, use at least three independent clean-session repeats per arm for each case.

Use at least five real tasks spanning these shapes: clear small task, ambiguous intent, complex dependency Graph, contingent downstream work, and a task with multiple valid implementation choices. The frozen set must also include at least one behavior-preserving migration/refactor with a reality conflict: the named clean/base ref, a replay or comparison oracle, and current runtime behavior are not assumed to agree. Shapes may overlap in one case. Freeze the case set before running either arm.

### Reality-conflict case

For the required reality-conflict case, freeze enough artifacts to distinguish causal attribution at the claim-relevant source, configuration, input, and runtime identities. A branch/ref called `main`, `master`, `clean`, `golden`, or `release` is a location, not evidence that its behavior is correct. A passing or failing replay is evidence only for the exact runner/config/input combination that produced it.

The independently judged handoff should:

- establish whether the claimed baseline is actually green before attributing a regression to the candidate change;
- when the baseline is already red but an independently supported behavior oracle exists, keep semantic restoration and structural evolution as distinct material outcomes and order them only by their real dependency;
- preserve separate completion claims so behavior recovery cannot masquerade as architecture improvement, and architecture checks cannot substitute for behavior parity;
- avoid widening the proposed architecture merely to explain a failure whose causal owner has not been discriminated.

Use the existing adjudication fields rather than adding incident-specific score fields. An unsupported baseline/candidate attribution makes the affected `compiled_work[].evidence_supported` false. A handoff that forces the Executor to rediscover the semantic baseline, materially separate restoration from evolution, or invent their completion proof is not validated and sets `executor_reinterpretation=true`.

## Run record

Write one JSON object per session to a JSONL file. Required fields:

```json
{
  "case_id": "real-task-01",
  "repeat": 1,
  "arm": "base",
  "skill_ref": "main@<immutable-sha>",
  "target_repo": "owner/repo",
  "target_ref": "<immutable-sha>",
  "model": "<model + reasoning config>",
  "prompt_sha256": "<sha256 of exact user prompt>",
  "human_response_profile": "<stable response-profile id>",
  "tool_profile": "<stable tool-permission profile>",
  "host_config": "<stable host/runtime profile>",
  "handoff_validated": true,
  "first_handoff_latency_ms": 42000,
  "input_tokens_to_handoff": 12000,
  "output_tokens_to_handoff": 1800,
  "tool_calls_to_handoff": 9,
  "clarifications": [
    {"contract_changing": true},
    {"contract_changing": false}
  ],
  "compiled_work": [
    {"evidence_supported": true},
    {"evidence_supported": false}
  ],
  "executor_reinterpretation": false,
  "total_input_tokens": 15000,
  "total_output_tokens": 2400,
  "total_tool_calls": 12
}
```

The scorer rejects a pair when target repo/ref, model configuration, prompt hash, Human response profile, tool profile, or host configuration differs across arms, and rejects a pair whose base/candidate `skill_ref` is identical.

`handoff_validated` is an independent executable-contract judgment, not the tested arm's self-report. A true value means a fresh Executor can safely start from that Taskbook without recovering missing Human intent, materially redefining the work boundary, or inventing completion proof. Handoff-specific latency/token/tool metrics are calculated only from records with `handoff_validated=true`.

A failed session remains in the sample. If no handoff candidate exists, use `handoff_validated=false`, allow the handoff-specific latency/token/tool fields to be `null`, set `compiled_work=[]`, and set `executor_reinterpretation=true` because a fresh Executor cannot safely start from the missing contract. If an invalid handoff attempt exists, keep its compiled work for quality adjudication even though its speed/cost is excluded from executable-handoff efficiency metrics.

`clarifications[].contract_changing` is judged against the final executable contract. A clarification is unnecessary when a different answer could not change Goal, Human-owned choice, binding boundary, material-work judgment, or completion obligation.

`compiled_work[].evidence_supported` is false when a material work cut or dependency was compiled without current Evidence and before it became real. Implementation detail does not count as a material work cut. A validated handoff must have non-empty `compiled_work`; empty work is allowed only for a failed no-handoff session and contributes no speculative-work denominator.

`executor_reinterpretation` is true when the fresh Executor must recover missing Human intent, materially redefine the work boundary, or invent the completion proof before it can safely start. Ordinary implementation discovery is not reinterpretation.

## Blind adjudication

Do not let either tested arm label its own quality metrics.

1. Preserve the raw session transcript, each candidate Taskbook, timing/token/tool counters, and target-reality Evidence.
2. Before judging `handoff_validated`, `contract_changing`, or `evidence_supported`, hide `arm`, `skill_ref`, and any branch/revision marker that reveals which output is base or candidate.
3. Use the same independent judge/rubric for both arms. The judge validates executable handoffs, classifies each clarification, and classifies each material work cut against the frozen Human intent and target repo/runtime reality; it must not prefer an implementation style absent from the contract.
4. `executor_reinterpretation` comes from the separate fresh Executor probe, not from the original Northstar / Prompt Atlas session self-report.
5. If two reviewers are used and disagree on a classification, resolve the disagreement before scoring and keep the adjudication note with the run artifacts.

This keeps the measured quality and handoff-validity signals independent from the skill revision being tested.

## Metrics

- **Validated executable handoff rate**: validated sessions / all sessions. Higher is better. Failed handoffs stay visible here instead of disappearing as fast observations.
- **First executable handoff latency**: median `first_handoff_latency_ms` over validated handoffs only.
- **Unnecessary clarification rate**: non-contract-changing clarification questions / all clarification questions. If no clarification was asked, the rate is 0.
- **Speculative task rate**: Evidence-unsupported compiled material work / all compiled material work.
- **Executor reinterpretation rate**: sessions with `executor_reinterpretation=true` / all sessions.
- **Token / tool cost**: median input+output tokens and tool calls to the first validated executable handoff. Total-session token/tool fields are reported as secondary context across all runs.

Run:

```bash
python3 evals/northstar-paired/score.py <results.jsonl>
```

The scorer prints base/candidate aggregates, percentage-point deltas for quality rates, relative deltas for efficiency metrics, non-regression guardrails, and an explicit behavioral-claim readiness section.

## Behavioral claim readiness

The sample-size readiness gate is explicit:

```text
Behavioral claim readiness:
READY FOR SCORING
- cases: 5/5
- min repeats/case: 3/3
- validated handoffs: base 14/15, candidate 15/15
```

or:

```text
Behavioral claim readiness:
INCONCLUSIVE
- cases: 1/5
- min repeats/case: 1/3
```

The default sample gate requires at least five real cases and at least three clean-session repeats per arm for every case. Handoff validity is not a sample-size gate: it is measured as a first-class quality signal so a candidate can legitimately improve a weak base rather than making the whole comparison unevaluable.

A sample that misses the cases/repeats gate may still be used as scorer/schema smoke or exploratory measurement, but it cannot support a behavioral-uplift claim.

## Decision rule

Do not collapse the result into one opaque score.

Default guardrails for a behavioral-uplift claim:

- validated executable handoff rate must not regress by more than 2 percentage points;
- unnecessary clarification rate, speculative task rate, and Executor reinterpretation rate must not regress by more than 2 percentage points;
- median first-handoff latency, tokens-to-handoff, and tool-calls-to-handoff must not regress by more than 10%;
- claim an efficiency improvement only when at least one of those three efficiency metrics improves by at least 10% without violating the quality guardrails.

Invalid handoffs are never used to reward speed or handoff token/tool cost. If an arm has no validated handoff, its handoff-efficiency metrics are `n/a` and the corresponding comparison is `INCONCLUSIVE`; the validation-rate metric still records the failure.

If sample size is too small or paired results disagree materially across repeats, report the measurements and mark the behavioral conclusion inconclusive rather than converting noise into a PASS.

## Smoke the scorer

`results.example.jsonl` is schema-only example data, not behavioral Evidence. It can be used to confirm that the scorer accepts a valid pair and explicitly reports the one-case sample as `INCONCLUSIVE` for behavioral-claim readiness:

```bash
python3 evals/northstar-paired/score.py evals/northstar-paired/results.example.jsonl
```

## What this eval does not prove

It does not prove implementation quality after Executor execution, and it does not replace Taskbook contract/scenario regression. It measures the behavioral effect of Northstar / Prompt Atlas shaping and compilation under controlled clean sessions.
