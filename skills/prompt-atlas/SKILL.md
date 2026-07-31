---
name: prompt-atlas
description: Two-stage compiler for turning a raw or evolving request into an executable agent handoff. Intent Take converges on Stable Intent without inventing Human authority. Execution Compile lowers that intent into the smallest truthful carrier with explicit authority boundaries, a grounded execution graph, local convergence loops, recovery needs, and trusted acceptance. Use for requirement clarification, prompt/task preparation, handoff, or when another workflow needs stable intent or an executable task carrier.
---

# Prompt Atlas

Prompt Atlas has two stages:

1. **Intent Take** — establish what should be achieved, why it matters, what is authoritative, and what would count as success.
2. **Execution Compile** — lower Stable Intent into one small, grounded carrier that a capable runtime can execute without using Human interaction as ordinary orchestration.

Stable Intent is source semantics, not the first half of the final taskbook. Execution Compile transforms it into an executor-facing representation; it does not append execution prose to an Intent Contract or reinterpret settled intent.

Trust a capable frontier model with routine implementation How, local self-correction, and ordinary verification. Encode what is costly or unsafe to reconstruct: intent, authority, material reality, real dependencies, interruption-sensitive state, and task-specific proof obligations.

Use progressive disclosure:

- [contract-anatomy.md](references/contract-anatomy.md) when intent authority, Goal closure, or stability is unclear;
- [execution-compile.md](references/execution-compile.md) when authority boundaries, graph shape, loop boundaries, branch closure, continuity, or acceptance needs judgment;
- [completion-trust.md](references/completion-trust.md) when completion can false-pass or needs an independent acceptance boundary.

## Stage 1 — Intent Take

Recover the current request from the user's latest authority, still-valid prior decisions, and relevant context. Preserve explicit requested outcomes unless the user supersedes them. Keep the **Why / design intent** when it will help a later executor choose correctly in situations the prompt cannot predict.

Distinguish missing reality from an unclosed Goal. Evidence can resolve context unknowns; it cannot decide what outcome the Human wants. When the prompt expresses a concern, hypothesis, competing questions, or active deliberation without establishing one authoritative outcome, do not turn that thinking surface into execution scope. First resolve only the decision-relevant context that is accessible and needed to make the choice meaningful. Then form the smallest coherent candidate Goal or options and ask the Human to confirm, select, or correct them. A model-proposed Goal remains inference until a subsequent Human message closes it. If the required evidence cannot be obtained in this turn, return only the smallest focused probe or blocker needed to continue convergence.

Do not over-apply this gate. If existing Human authority already establishes a complete minimum outcome, broader questions, future decisions, and implementation unknowns do not make that Goal unclosed; preserve the minimum Goal and keep the rest separate.

Ground only what can change intent meaning, feasibility inside settled boundaries, Goal closure, or success/proof semantics. Prefer the smallest authoritative check and rich existing references. Keep verified fact, inference, recommendation, and unknown distinct.

Treat unknown as a routing signal, not a stop condition and not a reason to suppress a necessary question: resolve factual unknowns from evidence, leave reversible implementation How to execution, and ask only when the remaining material uncertainty belongs to Human authority.

Before declaring intent stable, scan for unresolved Human-owned choices. Resolve reality/context unknowns from authoritative evidence when possible and use that grounding to reduce the decision surface. Do not ask about unknowns evidence can settle or local implementation How. If a remaining material choice changes user-owned outcome, accepted behavior, scope/priority, approval, or a protected proof rule, surface the smallest useful decision set with materially distinct options, consequences, and a concise recommendation. Do not erase such a choice through inference, recommendation, or an implicit default.

When the Human defines a scope or classification rule but expresses tentative beliefs about which concrete entities satisfy it, preserve the rule and explicit inclusions/exclusions as authority; treat the membership claim as a territory hypothesis. Derive the concrete member set from evidence at the first stage where it affects judgment—Intent Take when it changes Goal closure or a Human decision, otherwise Execution Compile when it determines concrete work—and ask again only for residual cases whose classification depends on Human-owned semantics rather than repository facts.

Treat Intent Take as a convergence loop across turns: recover the current candidate Goal, confirmed authority, still-valid evidence, and remaining decision surface; reconcile each new Human message or authoritative fact against that state rather than restarting discovery. Rewriting alone cannot promote inference into authority.

Intent is stable when Execution Compile no longer needs to rediscover the problem, complete outcome, authoritative choices/boundaries, any material factual uncertainty that changes those source semantics, or what trusted success means, and no material Human-owned choice remains unresolved. If it is not stable, perform accessible focused grounding first, then return the current understanding plus only the smallest unresolved decision, candidate Goal, unavailable probe, or blocker. When Goal closure or another Human-owned decision remains, ask it explicitly rather than hiding it behind a passive unresolved state.

When stable, treat the result as **Stable Intent IR** and continue to Stage 2.

## Stage 2 — Execution Compile

Execution Compile ends when it produces one executable carrier and stops. Use two coupled lenses while compiling:

- **Authority** — what remains Human-owned, what the execution runtime may adapt inside Stable Intent, and what boundary judges completion when separation is required.
- **Control protocol** — how the smallest useful Graph, node-local Loops, evidence routes, continuity, and Global Gate keep execution moving truthfully.

First ground enough execution reality to identify the actual workspace, work surfaces, governing specs/tests, material baselines, real dependencies, and critical verifiers when accessible. Keep unavailable or unverified evidence explicit.

If grounding shows that Stable Intent cannot be preserved inside confirmed boundaries, or exposes a new Human-owned choice, return `Status: Unresolved Intent`. If Stable Intent remains valid but materially different carriers remain equally acceptable, return `Status: Execution Decision`. Local reversible How stays executor-owned.

Compile the smallest useful carrier:

- preserve Purpose, Goal, settled Decisions, and authority boundaries;
- use bounded outcome nodes and real dependency/evidence edges only when they improve execution judgment; a simple task may remain one current action;
- keep routine act / observe / evaluate / repair work inside the execution runtime or node-local Loops;
- let the execution runtime revise the remaining plan or Graph from evidence while Stable Intent, protected boundaries, and proof obligations remain unchanged;
- route Intent conflict or required authority expansion back to Intent Take;
- allow independent ready work to continue when one branch blocks;
- require recoverable semantic state only when work may outlive one context or span independent actors;
- judge the complete Goal at a Global Gate; local done is not global completion.

For long-running or cross-context repository work, the carrier may require the downstream runtime to maintain project-local continuity under `.scratch/<project>/IMPLEMENTATION_NOTES.md`. Prompt Atlas compiles the requirement; the runtime creates and updates the file.

`Status: Executable` means every foreseeable material Human-owned decision exposed by current intent and evidence is closed, and each ordinary execution uncertainty has a non-Human route such as probe, local repair, branch parking, evidence-driven replanning, retry, or truthful blocking. New runtime evidence may still expose a genuinely new authority boundary.

The carrier should make the following recoverable without replaying the conversation: **Purpose, Goal, grounded State, closed Decisions, Authority, the minimum execution structure, Boundaries, Verification, Continuity, Acceptance, and Delivery**. Keep the serialization task-shaped rather than filling empty sections.

For research or decision work, use evidence-bearing probe/source/synthesis work and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness rather than inventing code-style metrics.

## Output and handoff

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current understanding plus the smallest unavailable probe or explicit Human decision needed to close the Goal or repair another material intent boundary.
- **`Status: Execution Decision`** — Stable Intent remains valid, but a material execution branch still needs closure and no safe unconfirmed default applies.
- **`Status: Executable`** — one lowered executor-facing carrier that satisfies the readiness condition above.

For an **artifact-only** caller, return the terminal artifact. For a **compile-and-run** caller with an available execution runtime, `Status: Executable` is the handoff boundary: Prompt Atlas stops, the caller binds the carrier as the execution source, and execution continues without another Human “start” turn. The same physical agent may continue, but it must switch from compile judgment to the carrier's authority boundaries and execution semantics.

When independent acceptance is required, the carrier must state the accepting boundary and private-proof requirement. Before execution begins, the caller/runtime must either bind or reserve that boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter cannot claim an equivalent PASS.

For `Status: Executable`, do not prepend the Stable Intent IR or emit a second execution variant. Omit details that do not change downstream judgment, but never compress away a requested outcome, authority distinction, material dependency or branch, recovery requirement, handoff requirement, or trusted proof obligation.
