# Northstar paired clean-session behavioral eval

Eval-only. This does not change Northstar / Prompt Atlas runtime semantics.

## Goal

Compare a base skill revision with a candidate revision under isolated, otherwise identical sessions and measure whether Intent take + Intent compile produces a better executable handoff at lower cost without increasing speculative or over-specified behavior.

Use the same target repo/ref, user prompt, model, reasoning effort, tool permissions, and host configuration for both arms. Each arm starts from a fresh session with no conversation carry-over, memory, or artifacts from the other arm.

## Pair setup

For every case:

1. Freeze a real engineering task before either arm runs. Record the target repo/ref and exact user prompt.
2. Run `base` and `candidate` in separate clean sessions. Randomize arm order when possible.
3. Keep model/config/tool permissions identical. Do not reveal the other arm's output to either session.
4. Capture the first executable handoff, not merely the first answer. A handoff is executable only when a fresh Executor can start material work without redoing Human intent judgment, redefining material boundaries, or inventing completion proof.
5. After handoff, give the Taskbook to a fresh Executor session with the same target repo/ref. Record whether the Executor must reinterpret Human intent, material boundaries, or completion proof before safe start.
6. For a smoke comparison, one pair per case is enough. For a behavioral-uplift claim, use at least three independent clean-session repeats per arm for each case.

Use at least five real tasks spanning these shapes: clear small task, ambiguous intent, complex dependency Graph, contingent downstream work, and a task with multiple valid implementation choices. Freeze the case set before running either arm.

## Run record

Write one JSON object per session to a JSONL file. Required fields:

```json
{
  "case_id": "real-task-01",
  "repeat": 1,
  "arm": "base",
  "skill_ref": "main@<sha>",
  "target_repo": "owner/repo",
  "target_ref": "<sha-or-branch>",
  "model": "<model/config>",
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

`clarifications[].contract_changing` is judged against the final executable contract. A clarification is unnecessary when a different answer could not change Goal, Human-owned choice, binding boundary, material-work judgment, or completion obligation.

`compiled_work[].evidence_supported` is false when a material work cut or dependency was compiled without current Evidence and before it became real. Implementation detail does not count as a material work cut.

`executor_reinterpretation` is true when a fresh Executor must recover missing Human intent, materially redefine the work boundary, or invent the completion proof before it can safely start. Ordinary implementation discovery is not reinterpretation.

## Metrics

All metrics are lower-is-better.

- **First executable handoff latency**: median `first_handoff_latency_ms`.
- **Unnecessary clarification rate**: non-contract-changing clarification questions / all clarification questions. If no clarification was asked, the rate is 0.
- **Speculative task rate**: Evidence-unsupported compiled material work / all compiled material work. If no material work was compiled, the record is invalid for this metric.
- **Executor reinterpretation rate**: sessions with `executor_reinterpretation=true` / all sessions.
- **Token / tool cost**: median input+output tokens to first executable handoff and median tool calls to first executable handoff. Total-session token/tool fields are reported as secondary context.

Run `python3 evals/northstar-paired/score.py <results.jsonl>` to print base/candidate aggregates and deltas.

## Decision rule

Do not collapse the result into one opaque score.

Default guardrails for a behavioral-uplift claim:

- unnecessary clarification rate, speculative task rate, and Executor reinterpretation rate must not regress by more than 2 percentage points;
- median first-handoff latency, tokens-to-handoff, and tool-calls-to-handoff must not regress by more than 10%;
- claim an efficiency improvement only when at least one of those three efficiency metrics improves by at least 10% without violating the quality guardrails.

If sample size is too small or paired results disagree materially across repeats, report the measurements and mark the behavioral conclusion inconclusive rather than converting noise into a PASS.

## What this eval does not prove

It does not prove implementation quality after Executor execution, and it does not replace Taskbook contract/scenario regression. It measures the behavioral effect of Northstar / Prompt Atlas shaping and compilation under controlled clean sessions.