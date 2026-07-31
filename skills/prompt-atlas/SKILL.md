---
name: prompt-atlas
description: Two-stage compiler for turning a raw or evolving request into an executable agent handoff. Intent Take converges on Stable Intent without inventing Human authority. Execution Compile lowers that intent into the smallest truthful carrier with grounded reality, clear Human boundaries, execution freedom, continuity only when needed, and trusted acceptance. Use for requirement clarification, prompt/task preparation, handoff, or when another workflow needs stable intent or an executable task carrier.
---

# Prompt Atlas

Prompt Atlas has two stages:

1. **Intent Take** — establish what should be achieved, why it matters, what is authoritative, and what would count as success.
2. **Execution Compile** — lower Stable Intent into one small, grounded carrier that a capable runtime can execute without using Human interaction as ordinary orchestration.

Stable Intent is source semantics, not the first half of the final taskbook. Execution Compile transforms it into an executor-facing representation; it does not append execution prose to an Intent Contract or reinterpret settled intent.

Trust a capable frontier model with routine implementation How, local self-correction, and ordinary verification. Encode what is costly or unsafe to reconstruct: intent, authority, material reality, real dependencies, interruption-sensitive state, and task-specific proof obligations.

Use progressive disclosure:

- [contract-anatomy.md](references/contract-anatomy.md) when intent authority, Goal closure, or stability is unclear;
- [execution-compile.md](references/execution-compile.md) when execution shape, branch closure, Task 0, continuity, or acceptance needs judgment;
- [completion-trust.md](references/completion-trust.md) when completion can false-pass or needs an independent acceptance boundary.

## Stage 1 — Intent Take

Recover the current request from the user's latest authority, still-valid prior decisions, and relevant context. Preserve explicit requested outcomes unless the user supersedes them. Keep the **Why / design intent** when it will help a later executor choose correctly in situations the prompt cannot predict.

Distinguish missing reality from an unclosed or confused Goal. Evidence can resolve facts; it cannot choose between materially different outcomes the Human may want. When the prompt is still a concern, hypothesis, comparison, or active deliberation, ground only enough context to make the real choice clear, then ask the smallest useful question.

Ask Human only when one of these boundaries is reached:

- **change intent** — proceeding would change the requested outcome, accepted behavior, or a design direction the Human made part of the result;
- **change boundary** — proceeding would cross or relax confirmed scope, constraints, approval, protected proof, or require an irreversible/high-risk authorization;
- **confused intent** — materially different Goal interpretations remain plausible after accessible grounding.

Do not ask for facts evidence can settle, necessary implementation expansion inside settled boundaries, architecture How, task decomposition, or ordinary execution choices. Treat unknown as a routing signal: investigate factual unknowns, leave local How to execution, let Execution Compile make safe visible defaults, and Ask Human only at the boundaries above.

A safe delegated default must preserve the current intent and boundaries, have a reasonable evidence- or convention-backed choice, and be reversible or reliably mismatch-detectable. Keep it visibly unconfirmed with its basis, consequence if wrong, and rollback or replan route. It may close execution orchestration; it may not silently change what the Human asked for.

When the Human defines a scope or classification rule but is unsure which concrete entities satisfy it, preserve the rule as authority and derive membership from evidence. Ask again only when the residual classification depends on Human meaning rather than observable reality.

Treat Intent Take as a convergence loop across turns: recover the candidate Goal, confirmed authority, still-valid evidence, and remaining decision surface; reconcile each new Human message or authoritative fact rather than restarting discovery. Rewriting alone cannot promote inference into authority.

Intent is stable when Execution Compile no longer needs to rediscover the problem, complete outcome, confirmed boundaries, or trusted success semantics, and none of the three Ask Human conditions remains. If it is not stable, perform accessible focused grounding first, then return the current understanding plus only the smallest unresolved decision, unavailable probe, or blocker.

When stable, treat the result as **Stable Intent IR** and continue to Stage 2.

## Stage 2 — Execution Compile

Execution Compile ends when it produces one executable carrier or a truthful non-intent blocker and stops. Use two coupled lenses:

- **Authority** — what remains Human-owned, what the compiler may decide visibly, what execution may adapt, and what boundary judges completion when separation is required.
- **Control protocol** — the minimum action loop, dependencies, evidence routes, continuity, and acceptance needed for this task.

Ground enough execution reality to identify the actual workspace, governing specs/tests, material baselines, dependencies, and critical verifiers. If a carrier-shaping fact cannot be checked during compile but can be checked safely before modification, make it **Task 0** rather than asking Human or pretending it is true. If required evidence, access, or capability is unavailable and no safe Task 0 or independent work route exists, return `Status: Blocked` with the exact missing condition.

If grounding or a future Task 0 result would require changing intent, changing a confirmed boundary, or resolving confused intent, return `Status: Unresolved Intent`. Otherwise keep factual mismatch, implementation discovery, and execution-theory changes inside execution through probe, repair, replan, or truthful blocking.

Close ordinary pre-run choices with evidence, execution freedom, or a safe visible delegated default. A choice that remains uncertain inside stable intent stays executor-owned; it does not create another Human gate.

Compile the smallest useful carrier:

- preserve Purpose, Goal, settled Decisions, visible delegated defaults, and authority boundaries;
- keep a simple task as one current action when that is enough;
- add Task/Issue nodes and dependency/evidence edges only when they improve execution judgment;
- keep routine act / observe / evaluate / repair work inside the execution runtime;
- let execution revise remaining work while intent, confirmed boundaries, and proof obligations remain unchanged;
- park a blocked branch and continue independent safe work;
- require recoverable semantic state only when work may outlive one context or span independent actors;
- judge the complete Goal at a Global Gate; local done is not global completion.

For long-running or cross-context repository work, the carrier may require the downstream runtime to maintain project-local continuity under `.scratch/<project>/IMPLEMENTATION_NOTES.md`. Prompt Atlas compiles the requirement; the runtime creates and updates the file.

`Status: Executable` means the Goal is clear, no foreseeable Ask Human boundary or hard blocker remains open, delegated defaults are explicit and safe for the handoff mode, and every ordinary execution uncertainty has a non-Human route such as Task 0, probe, repair, branch parking, replan, retry, or truthful blocking.

The carrier should make the following recoverable without replaying the conversation: **Purpose, Goal, grounded State, settled and delegated Decisions, Authority, minimum execution structure, Boundaries, Verification, Continuity, Acceptance, and Delivery**. Keep the serialization task-shaped rather than filling empty sections.

For research or decision work, use evidence-bearing probe/source/synthesis work and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness rather than inventing code-style metrics.

## Output and handoff

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current understanding plus the smallest probe or Human decision needed because intent would change, a confirmed boundary would change, or intent remains confused.
- **`Status: Blocked`** — Stable Intent is clear, but required evidence, access, capability, or another non-intent prerequisite is unavailable and no safe execution route remains; include the exact blocker and resolving condition.
- **`Status: Executable`** — one lowered executor-facing carrier that satisfies the readiness condition above. Execution-time facts and ordinary choices remain routed inside the carrier rather than creating another compile-time Human decision state.

Default to **artifact-only** unless the caller explicitly requests or owns execution continuation. An executable task alone does not authorize automatic execution. In artifact-only mode, delegated defaults remain visibly reviewable and become execution input only when the caller accepts, edits, or forwards the carrier. For a **compile-and-run** caller with an available execution runtime, `Status: Executable` is the handoff boundary: Prompt Atlas stops, the caller binds the carrier as the execution source, and execution continues without another Human “start” turn.

When independent acceptance is required, the carrier must state the accepting boundary and private-proof requirement. Before execution begins, the caller/runtime must either bind or reserve that boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter cannot claim an equivalent PASS.

For `Status: Executable`, do not prepend the Stable Intent IR or emit a second execution variant. Omit details that do not change downstream judgment, but never compress away a requested outcome, authority distinction, material dependency, delegated default, Task 0, recovery requirement, handoff requirement, or trusted proof obligation.
