# Re-entrant Review: judge an existing Taskbook independently

Use only when the Human explicitly asks to review / validate / judge an **already-existing authoritative Taskbook**. This is a new Prompt Atlas invocation, not an extension of Compile, and it adds no Acceptance layer, manager lifecycle, or persistent session requirement.

## Authority

Review depends only on reconstructible inputs, not on keeping the old conversation alive:

1. **authoritative Taskbook** — original Goal, decision priority, allowed/forbidden boundary, must-preserve, required Verification, Evidence requirements, Completion Hook, and the durable execution-state carrier selected at Compile;
2. **current repo/workspace reality** — current revision, diff, binding/config, and runnable providers;
3. **durable execution state** — the Taskbook-selected single carrier plus raw/stable Evidence artifacts left by the Executor. If an older Taskbook names no carrier, resolve one existing carrier in this order: Human/repo authority or existing repo convention, existing runtime-provided carrier, then `implement-notes` fallback. Do not create a second protocol;
4. prior-session memory may help locate things, but cannot replace those sources of truth.

If the Human explicitly changed Goal / boundary / Verification / priority / authorization after the Taskbook, do not silently synthesize a new contract. Report that the original Taskbook has been superseded and must be recompiled before Review.

## Review judgment

- Read the Taskbook first; never reconstruct the task from conversation.
- Apply the original Completion Hook using only **Goal / constraints + triggered required Verification + current valid Evidence**.
- Executor narration, self-declared `PASS`, and conclusions in the durable carrier are not Evidence by default.
- When the authoritative environment is accessible, directly reacquire final-judgment-critical Evidence when the cost is reasonable. When it is unavailable, require reviewable provenance/artifacts rather than guessing.
- Premise changes stale only affected Evidence; unrelated Evidence remains reusable.
- Green produced by weakening the judge through skip/todo, weaker assertions, deleting live tests, mocking away the subject, threshold changes, swallowed failures, `|| true`, or equivalent tactics is invalid.
- **Review judges; it does not implement or repair**: do not mutate the target workspace, patch the Goal, rewrite the Taskbook, or launch an Executor. On failure, return the smallest executable gap for a later Executor invocation.

## Verdict

- **`Verdict: PASS`** — trustworthy Evidence satisfies the original Completion Hook;
- **`Verdict: NON-PASS`** — a concrete, still-actionable completion gap remains; report the smallest gap and the Evidence supporting it, without designing the repair patch;
- **`Verdict: BLOCKED`** — required authority/environment/Evidence is unavailable, or a Human-owned contract change superseded the Taskbook; state the exact resume condition.

Keep Review output short: Verdict, critical Evidence, and only the necessary gap / resume condition. Do not restate the whole Taskbook.

## Fresh-session Review Prompt

This thin launcher can be pasted into any fresh Prompt Atlas session. Replace `<TASKBOOK_PATH>` with the Taskbook file outside the repo/workspace, or attach the Taskbook body directly:

```text
Read <TASKBOOK_PATH> as the authoritative execution contract. Review the current workspace and still-valid Evidence against its Goal, decision priority, boundaries, must-preserve constraints, triggered required Verification, and Completion Hook.

Use current authoritative repo/runtime reality and the Taskbook-selected durable execution-state carrier only as evidence/provenance inputs; if the Taskbook predates carrier selection, resolve one existing carrier from Human/repo authority or repo/runtime convention before falling back to implement-notes. Do not reconstruct the task from conversation and do not create a second state protocol. Re-acquire final-judgment-critical Evidence directly when the authoritative environment is accessible. Reuse Evidence whose premises remain valid and stale only affected Evidence when premises changed. Executor narration or self-declared PASS is not proof, and any green obtained by weakening the judge is invalid.

Do not implement or repair the Goal, modify the target workspace, rewrite the Taskbook, or launch an Executor during review. Return Verdict: PASS only when the original Completion Hook is satisfied. Otherwise return Verdict: NON-PASS or BLOCKED with the smallest concrete gap, the Evidence supporting that judgment, and the exact resume condition for a separate Executor invocation.
```

Same-session review is allowed as a convenience, but correctness must be identical when the same Taskbook + repo reality + durable Evidence are supplied in a fresh session.