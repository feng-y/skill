# Completion Trust

Use this reference only when the Goal or governing repo contract makes correctness/completion proof material. It is not a generic instruction to add another reviewer, verifier, or independent agent to every task.

Intent Take preserves **what must be proven**. Execution Compile places that obligation in the fixed taskbook graph as local proof, an explicit verification node when needed, and the complete-Goal Global Gate. The Executor runs visible proof but cannot weaken its semantics or self-certify evidence that requires an independent boundary.

## Proof semantics

Preserve the minimum proof properties needed for the claim:

1. **Directness** — prefer evidence that demonstrates the intended behavior or result. Existing authoritative acceptance paths outrank convenient proxies such as build, lint, or coverage when those proxies do not prove the target property.
2. **Failure sensitivity** — when a new or changed gate could false-pass, require evidence that it can distinguish right from wrong.
3. **Integrity boundary** — when a cheaper false pass is plausible, freeze the material **Judge, Population, Object, and Metric** so downstream work cannot silently weaken assertions, shrink coverage, substitute a narrower or mocked object, alter thresholds, bypass failure propagation, or reduce a protected baseline.
4. **Independent acceptance** — when Executor self-attestation remains gameable or incomplete, final completion belongs to a fresh or independent accepting boundary.

Intent Take need not choose exact commands, retry patterns, or verifier implementation when those are execution How.

## Lower into the fixed graph

Every taskbook has an execution graph and every material node has proof. The minimal topology is:

```text
Task 0 → Execute with local proof → Global Gate
```

Expand it to an explicit verification node only when proof spans multiple results, must run after integration, or genuinely needs fresh or independent judgment:

```text
Task 0 → Implement → Verify → Global Gate
```

Execution Compile attaches proof where it matters:

- local proof belongs to the node whose outcome it establishes;
- an explicit `Verify` node exists only for cross-node, integration, fresh-context, hidden, or independent proof;
- the complete-Goal Global Gate remains distinct from all local completion;
- protected Judge / Population / Object / Metric and non-regression semantics stay binding;
- Executor-owned evidence stops at `ready for independent acceptance` when another boundary owns final judgment.

The graph is fixed as a required execution structure; the proof topology inside it follows the property being proven rather than forcing a separate verifier for every task.

## Frozen proof envelope and adaptable execution

The compiler freezes:

- the property that must be proven;
- protected judging surfaces and baselines;
- complete-Goal acceptance obligations;
- required freshness, isolation, or independence;
- the completion ceiling and handoff mode.

The Executor may adapt implementation How and the remaining work graph inside that envelope. A replan may change where or how proof is collected, but it may not weaken the property, narrow the protected population, substitute a different object, lower the metric, or remove required independence.

## Acceptance binding

When independent acceptance is required, the taskbook must identify:

- the property and complete-Goal gate owned by the independent boundary;
- the required freshness, isolation, or separation;
- where private or hidden proof is retained outside Executor-visible state;
- the latest point by which an actual Acceptor or equivalent runtime boundary must be bound.

Before execution begins, the caller/runtime must either bind or reserve the required independent boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter may still produce visible evidence, but it cannot substitute Executor self-attestation or claim an equivalent PASS.

## Visible-contract boundary

A hidden oracle, manager-side spot check, fresh-context challenge, or other mechanism whose strength depends on Executor independence stays outside the Executor-visible taskbook. Prompt Atlas may state the property and accepting boundary; it must not expose hidden cases or let the Executor author the decisive oracle and then certify itself.

If the runtime or harness cannot provide a required independent boundary, execution may end at `ready for independent acceptance`; it must not claim equivalent proof.

## Runtime truth

Insufficient, compromised, narrowed, skipped, fabricated, or stale proof is `UNMET`. A local PASS can unlock dependent work without proving the whole Goal. Failed proof returns to evidence-producing work or a materially different replan while safe work remains. Environment unavailability stays explicit. Upstream changes invalidate downstream evidence when the change affects what that evidence proved.
