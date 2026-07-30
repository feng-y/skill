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

- [contract-anatomy.md](references/contract-anatomy.md) when intent authority or stability is unclear;
- [execution-compile.md](references/execution-compile.md) when graph shape, branch closure, AFK continuity, or Leader capability coverage needs judgment;
- [completion-trust.md](references/completion-trust.md) when completion can false-pass or needs an independent acceptance boundary.

## Stage 1 — Intent Take

Recover the current request from the user's latest authority, still-valid prior decisions, and relevant context. Preserve explicit requested outcomes unless the user supersedes them. Keep the **Why / design intent** when it will help a later executor choose correctly in situations the prompt cannot predict.

Ground only what can change intent meaning, feasibility inside settled boundaries, or success/proof semantics. Prefer the smallest authoritative check and rich existing references. Keep verified fact, inference, recommendation, and unknown distinct.

Ask the Human only for a material choice that evidence cannot settle and that changes user-owned outcome, accepted behavior, scope/priority, approval, or a protected proof rule. Implementation alternatives that preserve those semantics remain downstream judgment. A recommendation or reversible default never becomes Human authority through rewriting.

Intent is stable when Execution Compile no longer needs to rediscover the problem, complete outcome, authoritative choices/boundaries, material factual uncertainty, or what trusted success means. If it is not stable, return the current intent plus only the smallest decision, probe, conditional/default, or blocker needed to continue alignment.

When stable, treat the result as **Stable Intent IR** and continue to Stage 2.

## Stage 2 — Execution Compile

Execution Compile ends when it produces one executable carrier. It does not run the graph or own live execution state.

First ground enough execution reality to make the graph truthful: identify the actual target/workspace, work surfaces, governing specs or tests, material baselines, real dependencies, and critical commands/verifiers when accessible. Keep unavailable or unverified evidence explicit rather than turning plausibility into fact.

Close execution branches that would otherwise interrupt AFK work when different answers materially change task boundaries, dependencies, verification ownership/path, scope, architecture direction, or the Global Gate. Resolve them from Stable Intent, governing constraints, and evidence when possible. If materially different graphs remain equally valid, return `Status: Execution Decision`; local reversible How stays executor-owned. A visibly unconfirmed execution default is allowed only when the caller explicitly requires an executable carrier without another Human turn and the default preserves settled Goal/boundaries while being reversible or reliably mismatch-detectable.

Compile the **smallest useful graph**:

- Task / Issue nodes are bounded outcomes with only the context, real dependencies, applicable boundaries, and proof needed to judge them locally.
- Edges represent real dependency or evidence flow, not prose order.
- The Global Gate judges the complete Goal; local done is not global completion.
- Human gates exist only for newly exposed material branches that intent/evidence cannot close.

Add parallel ownership, partial-block behavior, continuity state, or separate verifier nodes only when the task actually needs them. Independent work may continue while another node is blocked. Trusted completed work survives replanning unless new evidence invalidates it.

The runtime progresses ready work through an evidence-driven loop: act, observe, evaluate, then continue, repair locally, or revise the remaining graph. A failed check is work-state, not automatically HITL. Completion requires the task-specific proof carried by the Global Gate; generic extra review or re-check steps are not a default requirement.

The executable carrier should make the following semantics recoverable without replaying the conversation: **Purpose, Goal, grounded State, closed Decisions, Graph, Boundaries, task-specific Verification, material Runtime/continuity semantics, and Delivery**. Keep the serialization task-shaped rather than filling empty sections.

For research or decision work, use evidence-bearing probe/source/synthesis nodes and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness rather than inventing code-style metrics.

## Output

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current best intent plus the smallest remaining alignment surface.
- **`Status: Execution Decision`** — Stable Intent exists, but a material execution branch still needs closure and no safe unconfirmed execution default applies.
- **`Status: Executable`** — one lowered executor-facing carrier.

For `Status: Executable`, do not prepend the Stable Intent IR or emit a second execution variant. Keep the artifact dense and readable; omit details that do not change executor judgment, but never compress away a requested outcome, authority distinction, material graph branch, or trusted proof obligation.