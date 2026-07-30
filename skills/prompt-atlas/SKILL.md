---
name: prompt-atlas
description: Two-stage compiler for turning a raw or evolving request into an executable agent handoff. Intent Take converges on Stable Intent without inventing Human authority. Execution Compile lowers that intent into the smallest truthful execution graph that can run with minimal Human orchestration. Use for requirement clarification, prompt/task preparation, handoff, or when another workflow needs stable intent or an executable task carrier.
---

# Prompt Atlas

Prompt Atlas has two stages:

1. **Intent Take** — establish what should be achieved, why it matters, what is authoritative, and what would count as success.
2. **Execution Compile** — lower Stable Intent into a small, grounded execution graph with the decisions, dependencies, proof boundaries, and runtime semantics needed for AFK execution.

Stable Intent is source semantics, not the first half of the final taskbook. Execution Compile transforms it into an executor-facing representation; it does not append execution prose to an Intent Contract or reinterpret settled intent.

Trust a capable frontier model with routine implementation How, local self-correction, and ordinary verification. Encode what is costly or unsafe to reconstruct: intent, authority, material reality, real orchestration structure, and task-specific proof obligations.

Use progressive disclosure:

- [contract-anatomy.md](references/contract-anatomy.md) when intent authority, goal closure, or stability is unclear;
- [execution-compile.md](references/execution-compile.md) when graph shape, branch closure, AFK continuity, or Leader capability coverage needs judgment;
- [completion-trust.md](references/completion-trust.md) when completion can false-pass or needs an independent acceptance boundary.

## Stage 1 — Intent Take

Recover the current request from the user's latest authority, still-valid prior decisions, and relevant context. Preserve explicit requested outcomes unless the user supersedes them. Keep the **Why / design intent** when it will help a later executor choose correctly in situations the prompt cannot predict.

Distinguish missing reality from an unclosed Goal. Evidence can resolve context unknowns; it cannot decide what outcome the Human wants. When the prompt expresses a concern, hypothesis, competing questions, or active deliberation without establishing one authoritative outcome, do not turn that thinking surface into execution scope. First resolve only the decision-relevant context that is accessible and needed to make the choice meaningful. Then form the smallest coherent candidate Goal or options and ask the Human to confirm, select, or correct them. A model-proposed Goal remains inference until a subsequent Human message closes it. If the required evidence cannot be obtained in this turn, return only the smallest focused probe or blocker needed to continue convergence.

Do not over-apply this gate. If existing Human authority already establishes a complete minimum outcome, broader questions, future decisions, and implementation unknowns do not make that Goal unclosed; preserve the minimum Goal and keep the rest separate.

Ground only what can change intent meaning, feasibility inside settled boundaries, Goal closure, or success/proof semantics. Prefer the smallest authoritative check and rich existing references. Keep verified fact, inference, recommendation, and unknown distinct.

Before declaring intent stable, actively scan for unresolved Human-owned choices. Resolve reality/context unknowns from authoritative evidence when possible and use that grounding to reduce the decision surface. Do not ask about unknowns evidence can settle or local implementation How. But if a remaining material choice changes user-owned outcome, accepted behavior, scope/priority, approval, or a protected proof rule, surface the smallest useful decision set to the Human with materially distinct options, consequences, and a concise recommendation. Do not erase such a choice through inference, recommendation, or an implicit default.

When the Human defines a scope or classification rule but expresses tentative beliefs about which concrete entities satisfy it, preserve the rule and explicit inclusions/exclusions as authority; treat the membership claim as a territory hypothesis. Derive the concrete member set from evidence at the first stage where it affects judgment, and ask again only for residual cases whose classification depends on Human-owned semantics rather than repository facts.

Intent is stable when Execution Compile no longer needs to rediscover the problem, complete outcome, authoritative choices/boundaries, any material factual uncertainty that changes those source semantics, or what trusted success means, and no material Human-owned choice remains unresolved. If it is not stable, perform any accessible focused grounding first, then return the current understanding plus only the smallest unresolved decision, candidate Goal, unavailable probe, or blocker. When Goal closure or another Human-owned decision remains, ask it explicitly rather than hiding it behind a passive unresolved state.

When stable, treat the result as **Stable Intent IR** and continue to Stage 2.

## Stage 2 — Execution Compile

Execution Compile ends when it produces one executable carrier. It does not run the graph or own live execution state.

First ground enough execution reality to make the graph truthful: identify the actual target/workspace, work surfaces, governing specs or tests, material baselines, real dependencies, and critical commands/verifiers when accessible. Keep unavailable or unverified evidence explicit rather than turning plausibility into fact.

If execution grounding shows that Stable Intent cannot be preserved inside its confirmed boundaries, or exposes a new Human-owned choice about Goal, accepted behavior, scope/priority, approval, or protected proof, return `Status: Unresolved Intent` with the conflict, evidence, and smallest decision surface, then re-enter Intent Take. Do not misclassify an intent change as an execution branch.

Close execution branches that would otherwise interrupt AFK work when different answers materially change task boundaries, dependencies, verification ownership/path, scope, architecture direction, or the Global Gate while preserving Stable Intent. Resolve them from Stable Intent, governing constraints, and evidence when possible. If materially different graphs remain equally valid, return `Status: Execution Decision`; local reversible How stays executor-owned. A visibly unconfirmed execution default is allowed only when the caller explicitly requires an executable carrier without another Human turn and the default preserves settled Goal/boundaries while being reversible or reliably mismatch-detectable.

Compile the **smallest useful graph**:

- Task / Issue nodes are bounded outcomes with only the context, real dependencies, applicable boundaries, and proof needed to judge them locally.
- Edges represent real dependency or evidence flow, not prose order.
- The Global Gate judges the complete Goal; local done is not global completion.
- Human gates exist only for newly exposed material execution branches that intent/evidence cannot close without changing Stable Intent.

Add parallel ownership, partial-block behavior, continuity state, or separate verifier nodes only when the task actually needs them. Independent work may continue while another node is blocked. Trusted completed work survives replanning unless new evidence invalidates it.

The runtime progresses ready work through an evidence-driven loop: act, observe, evaluate, then continue, repair locally, or revise the remaining graph. A failed check is work-state, not automatically HITL. Completion requires the task-specific proof carried by the Global Gate; generic extra review or re-check steps are not a default requirement.

The executable carrier should make the following semantics recoverable without replaying the conversation: **Purpose, Goal, grounded State, closed Decisions, Graph, Boundaries, task-specific Verification, material Runtime/continuity semantics, and Delivery**. Keep the serialization task-shaped rather than filling empty sections.

For research or decision work, use evidence-bearing probe/source/synthesis nodes and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness rather than inventing code-style metrics.

## Output

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current understanding plus the smallest unavailable probe or explicit Human decision needed to close the Goal or repair another material intent boundary.
- **`Status: Execution Decision`** — Stable Intent remains valid, but a material execution branch still needs closure and no safe unconfirmed execution default applies.
- **`Status: Executable`** — one lowered executor-facing carrier.

For `Status: Executable`, do not prepend the Stable Intent IR or emit a second execution variant. Keep the artifact dense and readable; omit details that do not change executor judgment, but never compress away a requested outcome, authority distinction, material graph branch, or trusted proof obligation.