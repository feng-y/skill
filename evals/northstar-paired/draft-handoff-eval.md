# Primary-Draft / routing paired eval

Eval-only. This is an evidence-checked **scoring sidecar**, not an agent launcher or an automatic semantic judge. Normal runtime must not read this directory.

## Cases and claim boundary

`draft-cases.json` freezes eight cases: connected Hermes sharing change; blocked factual premise; adopted corrections scattered across comments; clear local change; independent AE caller; independent Verify caller; verification-source identity gap; two independent Intents.

D1 reconstructs a user-reported Hermes failure. The original session and production sources are not available. Its concrete sharing/lifetime facts are deliberately supplied **fixture context**, not claims about the real Hermes implementation. D2–D8 are constructed counterexamples. Repeating them does not create a corpus of real observed tasks.

The primary comparison is base `acc09e5040b808b46cc8f9aea17bbac988d639ab` versus this change's pinned head. This measures the new correction, not separate causal uplift from #93 versus #94.

## Candidate setup

1. Freeze both Skill revisions, one target/fixture snapshot per case, exact model including reasoning configuration, tool permissions, host/global instructions and Human-response policy. Keep them equal within pairs and across each case's repeats. Alternate/randomize arm order.
2. Use an external temporary workspace. Expose the target task and only the arm's installed runtime Skills through the same discovery mechanism. Exclude this repository's evals, plan, validation report, change history and judge rubric. Do not include this conversation or prior run state.
3. Export only organic prompts with the command below. Start a **fresh actual agent session** for every case/arm/repeat. No prompt names a required Skill chain or supplies a grading instruction. Do not count self-reported invocations: retain actual Skill loads/calls and resulting artifacts in the trace.
4. For Intent cases, give the resulting handoff to a separate fresh consumer with the frozen task/territory authority, but without the author's conversation, reasoning or evaluation rubric. Record whether it must reconstruct a binding decision, connected intended path or acceptance before work. For D2 it should recognize the explicit blocker, not invent a solution.
5. A blinded judge receives sanitized trace, result and probe, with arm/revision identity removed. Grade actual behavior and artifact content before the coordinator restores pair metadata. Required evidence must cite real line spans. One judge may score multiple outputs, but cannot be a candidate or consumer session.

```bash
python3 evals/northstar-paired/draft_eval.py export-prompts /tmp/draft-actor-input
```

The output directory must be new. It contains only `01.txt` … `08.txt`, in manifest order. Do not place the private case manifest or this rubric in an actor's workspace.

One pair per case is smoke; the full focused set is **8 cases × 2 arms × 3 repeats = 48 actual sessions**, plus fresh consumer probes for Intent cases. The existing broader uplift threshold remains at least five real cases and three clean repeats per arm. This constructed set alone cannot establish that broad claim.

## Judge checks

| Check | Observable criterion |
| --- | --- |
| `single_primary_draft` | One current intended-change authority **per Intent**, not one file/view/session; candidate sketches are not parallel accepted Drafts. |
| `draft_sufficiency` | The connected material shape is sufficient for the declared scope. For executable cases, a fresh consumer need not recover intent. D2 instead requires an honest best-known blocked Draft, not an executable handoff. |
| `integration` | Adopted corrections appear coherently in the current primary Draft, preserving unaffected commitments. Merely forwarding fragments fails. |
| `routing` | The actual next unresolved question reaches the appropriate semantic owner; do not grade literal Skill names alone. |
| `owner_retention` | Specialist returns to its original decision owner; necessary premise-driven re-entry is not erroneous takeover. Independent AE/Verify do not acquire a synthetic Northstar stage. |
| `factual_discipline` | No invented territory, lifetime, immutability, performance number, accepted choice or proof. |
| `prototype_discipline` | A call has a material shape reason and sufficient bounded scope; no call for already-concrete/How-only work, no shaping through decision-changing unknown facts. Inline sufficient shaping is allowed. |

A correct invocation with an incomplete primary Draft is a failure. A correct short Draft with no Prototype call can pass. Neither the number of headings nor the number of calls proves quality.

`executable_handoff` is separately recorded and checked against the case. D2 passing blocked-handoff checks never counts as executable implementation readiness. Independent AE/Verify/factual cases have no Intent-Draft grades and use `executable_handoff=null`.

## Observation record

Write one JSON object per run to an external `observations.jsonl` **after blinded judging**. Reuse the existing paired identity fields: `case_id`, `repeat`, `arm`, `skill_ref`, `target_repo`, `target_ref`, `model`, `prompt_sha256`, `human_response_profile`, `tool_profile`, `host_config`. `skill_ref` must be a full commit SHA; prompt hash covers the exported UTF-8 bytes including their trailing newline. Pin actual target identity rather than using branch names.

Additional fields:

- `session_id`, `judge_session_id`, and `probe_session_id` for Intent cases; actor and probe sessions must be distinct and fresh;
- `evidence_kind`: `clean_session` for actual executions, `synthetic_smoke` only for scorer tests; `clean_session` and `blind_judge` booleans;
- `prototype_invocations`: observed integer count; `facts_closed_before_prototype`: trace-supported boolean;
- `executable_handoff`: independent consumer assessment, or null for non-Intent cases;
- `artifacts`: `trace`, `result`, plus `probe` for Intent cases. Each has a relative `path` under the evidence root and a SHA-256 `sha256`;
- `checks`: exactly the case's check names. Each contains `ok` (true/false/null) and `evidence`, a list of `{ "artifact": "result", "lines": [start, end] }` spans, 1-based and inclusive. Null means unmeasured, not pass.

Routing/owner/Prototype grades require trace evidence; sufficiency requires probe evidence; other measured grades require result evidence. The scorer checks file identities and line bounds, not the semantic truth of a grade. Session-isolation and blinding metadata are declarations requiring coordinator audit, not cryptographic proof. Never manufacture artifacts to satisfy these fields.

```bash
python3 evals/northstar-paired/draft_eval.py score /tmp/run/observations.jsonl \
  --evidence-root /tmp/run
python3 -m unittest discover -s evals/northstar-paired -p 'test_draft_eval.py' -v
```

`test_draft_eval.py` provides synthetic schema examples and failure-injection tests. Its fabricated fixture text is explicitly marked and never counts as an agent transcript.

## Results and decision

The sidecar reuses the original scorer's pair validation. It reports per-check numerators/denominators, unknowns, every candidate failure, per-pair regression and improvement. Derived over-trigger/handoff contradictions override a superficially green grade; failures cannot hide behind an average. A missing grade, incomplete suite, unclean run or missing evidence cannot become a positive gate.

Exit codes: `0` focused non-regression after complete clean-session records; `1` measured candidate failure/regression; `2` invalid input or artifact identity; `3` inconclusive or synthetic-only evidence. Even exit 0 is not a claim of broad behavioral uplift, production performance, code quality or efficiency.

Keep using the unmodified `score.py` for actual Northstar handoff/clarification/speculation/reinterpretation and token/tool/latency records in its existing schema, joined by case/repeat/arm. Do not put independent AE/Verify cases into Northstar handoff-rate denominators. Do not invent timing/counters when the host cannot expose them. Both the Draft sidecar and applicable original quality/cost guardrails matter to merge interpretation.

Skill Doctor is not currently installed in this repository: explicit cleanup `c13842d` removed it before #93. This sidecar does not restore it, read local conversation history or upload transcripts. A future real-corpus assessment can apply its evidence-first attribution approach; no grade is fabricated here.
