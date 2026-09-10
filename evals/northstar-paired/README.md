# Northstar paired clean-session behavioral eval

Eval-only. This does not change Northstar runtime semantics.

## Scope

Compare a base skill revision with a candidate revision under isolated, otherwise identical sessions and measure whether **optional Northstar** preserves or produces a better executable handoff at lower cost without increasing speculative or over-specified behavior.

A validated handoff is not required to be a Taskbook. Depending on the case it may be:

- an already-sufficient Drafted Issue that Northstar correctly leaves un-recompiled;
- the same canonical Issue enriched with durable difficult-intent decisions / material relations;
- a separate execution contract / Taskbook when complexity or downstream access genuinely earns one.

This eval tests Northstar's bypass / difficult-intent / compile behavior. `evals/issue-shape/` separately owns conversation → Drafted Issue routing and artifact-shaping regressions.

Use the same target repo/ref, exact user prompt, Human response policy, model/reasoning configuration, tool permissions, and host configuration for both arms. Each arm starts from a fresh session with no conversation carry-over, memory, or artifacts from the other arm.

## Pair setup

For every case:

1. Freeze a real engineering task before either arm runs. Pin the target repo to an immutable commit SHA, record the exact user prompt, and store a SHA-256 of that prompt in every run record.
2. Freeze the Human intent behind the case and a response profile for clarification questions. The same Human/oracle answers both arms and does not volunteer arm-specific extra context.
3. Pin base and candidate skill revisions to immutable commit SHAs. Run them in separate clean sessions; randomize arm order when possible.
4. Keep model/config, tool permissions, and host configuration identical. Record stable IDs/strings so the scorer can reject mismatched pairs.
5. Preserve every candidate executable handoff with elapsed time, token counts, and tool-call count. Do not let the tested arm self-label it executable.
6. Give each handoff to a fresh Executor session with the same target repo/ref. Set `handoff_validated=true` only when the Executor can safely start material work without redoing Human intent judgment, materially redefining boundaries, or inventing completion proof.
7. If several handoff candidates appear in one session, the first executable handoff is the earliest candidate that independently validates. If none validates, set `handoff_validated=false`; handoff latency/token/tool fields may be `null` and are excluded from efficiency aggregates.
8. One pair per case is enough for smoke. A behavioral-uplift claim requires at least three independent clean-session repeats per arm for every case.

Use at least five real tasks spanning: clear small Issue / bypass, ambiguous intent, complex dependency Graph, contingent downstream work, and multiple valid implementation choices. The frozen set must also include at least one behavior-preserving migration/refactor with a reality conflict. Shapes may overlap.

### Clear-Issue bypass case

The handoff is valid when the incoming Drafted Issue already contains enough intended shape, boundary and Acceptance for a fresh Executor, and Northstar does **not** manufacture a new Goal / Taskbook / Graph merely because it was invoked. Record the existing material work in `compiled_work` for scoring; this field describes the handoff's material work, not necessarily new work invented by Northstar.

### Reality-conflict case

Freeze enough artifacts to distinguish causal attribution at the claim-relevant source, configuration, input, and runtime identities. A branch/ref named `main`, `clean`, `golden`, or `release` is a location, not evidence that its behavior is correct. Replay evidence applies only to the exact runner/config/input combination that produced it.

The independently judged handoff should:

- establish whether the claimed baseline is actually green before attributing a regression;
- when baseline is already red but an independent behavior oracle exists, keep semantic restoration and structural evolution as distinct outcomes and order them only by real dependency;
- preserve separate completion claims so recovery cannot masquerade as architecture improvement;
- avoid widening architecture merely to explain a failure whose causal owner has not been discriminated.

Unsupported baseline/candidate attribution makes the affected `compiled_work[].evidence_supported` false. A handoff that forces the Executor to rediscover the semantic baseline or materially redefine restoration vs evolution is not validated and sets `executor_reinterpretation=true`.

## Run record

Write one JSON object per session to JSONL:

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
    {"contract_changing": true}
  ],
  "compiled_work": [
    {"evidence_supported": true}
  ],
  "executor_reinterpretation": false,
  "total_input_tokens": 15000,
  "total_output_tokens": 2400,
  "total_tool_calls": 12
}
```

The scorer rejects a pair when target repo/ref, model configuration, prompt hash, Human response profile, tool profile, or host configuration differs across arms, and rejects a pair whose base/candidate `skill_ref` is identical.

`handoff_validated` is an independent executable-contract judgment. A true value means a fresh Executor can safely start from the handed-off canonical Issue / contract without recovering missing Human intent, materially redefining the work boundary, or inventing completion proof.

A failed session remains in the sample. If no handoff candidate exists, use `handoff_validated=false`, allow handoff-specific latency/token/tool fields to be `null`, set `compiled_work=[]`, and set `executor_reinterpretation=true`. If an invalid handoff attempt exists, keep its compiled work for quality adjudication even though its speed/cost is excluded from executable-handoff efficiency metrics.

`clarifications[].contract_changing` is judged against the final executable contract. A clarification is unnecessary when a different answer could not change accepted outcome, Human-owned choice, binding boundary, material-work judgment, or completion obligation.

`compiled_work[].evidence_supported` is false when a material work cut or dependency appears without current Evidence before it becomes real. A validated handoff must have non-empty `compiled_work`; for a bypass case this records the already-established material work carried by the Drafted Issue.

`executor_reinterpretation` is true when the fresh Executor must recover missing Human intent, materially redefine the work boundary, or invent completion proof before safely starting. Ordinary implementation discovery is not reinterpretation.

## Blind adjudication

Do not let either tested arm label its own quality metrics.

1. Preserve the raw session transcript, each candidate handoff, timing/token/tool counters, and target-reality Evidence.
2. Before judging quality, hide `arm`, `skill_ref`, and branch/revision markers that reveal which output is base or candidate.
3. Use the same independent judge/rubric for both arms; it must not prefer an implementation style absent from the contract.
4. `executor_reinterpretation` comes from the separate fresh Executor probe, not the original Northstar self-report.
5. Resolve reviewer disagreement before scoring and keep the adjudication note with the run artifacts.

## Metrics

- **Validated executable handoff rate**: validated sessions / all sessions. Higher is better.
- **First executable handoff latency**: median `first_handoff_latency_ms` over validated handoffs only.
- **Unnecessary clarification rate**: non-contract-changing clarification questions / all clarification questions; 0 when no clarification was asked.
- **Speculative task rate**: Evidence-unsupported material work / all `compiled_work`.
- **Executor reinterpretation rate**: sessions with `executor_reinterpretation=true` / all sessions.
- **Token / tool cost**: median input+output tokens and tool calls to the first validated executable handoff. Total-session fields are secondary context.

Run:

```bash
python3 evals/northstar-paired/score.py <results.jsonl>
```

## Behavioral claim readiness

The default sample gate requires at least five real cases and at least three clean-session repeats per arm for every case. Missing the gate is valid for scorer/schema smoke, but behavioral uplift remains `INCONCLUSIVE`.

Handoff validity is a measured quality signal, not a sample-size gate: a candidate can legitimately improve a weak base rather than making the whole pair unevaluable.

## Decision rule

Do not collapse the result into one opaque score. Default guardrails for a behavioral-uplift claim:

- validated executable handoff rate must not regress by more than 2 percentage points;
- unnecessary clarification rate, speculative task rate, and Executor reinterpretation rate must not regress by more than 2 percentage points;
- median first-handoff latency, tokens-to-handoff, and tool-calls-to-handoff must not regress by more than 10%;
- claim efficiency improvement only when at least one efficiency metric improves by at least 10% without violating quality guardrails.

If sample size is too small or paired results disagree materially across repeats, report measurements and mark the behavioral conclusion inconclusive.

## Smoke the scorer

`results.example.jsonl` is schema-only example data, not behavioral Evidence:

```bash
python3 evals/northstar-paired/score.py evals/northstar-paired/results.example.jsonl
```

The example should parse, pass the configured non-regression guardrails, and explicitly report the one-case sample as `INCONCLUSIVE` for behavioral-claim readiness.

## What this eval does not prove

It does not prove implementation quality after Executor execution, and it does not replace Issue Shape / Intent Shape contract regressions. It measures the behavioral effect of Northstar bypass, difficult-intent judgment, and material compile under controlled clean sessions.
