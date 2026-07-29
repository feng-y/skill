---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered, evolving cross-turn hints into a concise, consumer-ready Intent Contract or requested prompt/carrier covering goal, current context, boundary, immediate task, and success or stop conditions. Support human-driven iterative intent alignment across separate invocations by preserving settled semantics, incorporating new user authority, and refreshing territory grounding from authoritative evidence. When intent is stable, include a concise non-executable handoff hint for Direct Execute or Wayfinder. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Explicit /prompt-atlas use returns the compiled artifact as the terminal result of this invocation.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground the context that matters, resolve only decisions that genuinely belong to the user, and leave the next consumer a concise artifact that does not require rediscovering requirement meaning.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, approval limits, protected evaluation or proof rules when material, and any user-owned priority needed to resolve competing constraints;
- **Immediate Task** — what should be completed now without prescribing the implementation;
- **Success / Stop** — the outcome and evidence that close the work, or what real blocker prevents closure; prefer achieved-result criteria over activity or work-volume criteria.

Keep these semantics distinct and recoverable, but do not turn them into a form unless the user asks. Prompt Atlas owns intent understanding and carrier compilation, and supports cross-turn alignment by preserving settled semantics, incorporating new user authority, and refreshing territory grounding from authoritative evidence. New user authority may revise user-owned intent; evidence may revise territory facts, feasibility, proof state, or route without silently rewriting that intent. Prompt Atlas does not own whether alignment continues, and repeated self-refinement on the same information is quality review, not new intent. It also does not own architecture choice, implementation planning, execution, or a durable repo-identity harness. Each Intent Take invocation terminates after delivering either a stable artifact with its handoff hint or the smallest useful unresolved decision/probe/blocker. A handoff hint is non-executable routing guidance, not a transition into downstream work.

Choose the output mode from the invocation:

- **Artifact mode** — the default for explicit `/prompt-atlas` use and direct requests to clarify, consolidate, prepare, hand off, or rewrite a requirement. When a stable artifact is ready, return the completed Intent Contract or requested carrier with one concise handoff hint selecting Direct Execute or Wayfinder, then stop this invocation. When stable compilation is not yet possible, return only the smallest necessary decision surface, probe, bounded conditional/default, or blocker and stop.
- **Embedded mode** — only when another capability or workflow explicitly invokes Prompt Atlas as an intake sub-capability. Return the compiled artifact or decision surface to that caller and stop the Prompt Atlas invocation. Do not infer Embedded mode merely because the user's ultimate task could later be planned or executed; let the caller own downstream routing unless it asks for a handoff judgment.

Use detailed guidance only when it becomes relevant: [contract-anatomy.md](references/contract-anatomy.md) for intent-artifact goal attainment and stability, and [completion-trust.md](references/completion-trust.md) for correctness or completion claims.

## Intent Take

### 1. Recover

Recover from the current request, relevant corrections, prior decisions, and examples. When a prior Atlas artifact is available, use its still-valid settled semantics as the baseline rather than restarting from raw history. The current user owns intent; current authoritative evidence owns territory. Latest explicit corrections supersede older meaning. Only new user authority may change Goal, user-owned priorities, confirmed decisions, or user-owned boundaries. Better territory evidence may update Current Context, feasibility, proof obligations, or route without silently rewriting those user-owned semantics. Recover the desired change separately from suggested means and hard boundaries.

### 2. Ground

Investigate only unknowns whose answers could materially change Goal, Boundary, Immediate Task, Success / Stop, or the safe route. Prefer the smallest authoritative check and rich existing references. For repo-scoped work, include governing repo-local constraints or acceptance rules when they can materially change Boundary, Success / Stop, proof obligation, or route; these are contract facts rather than downstream implementation detail. For engineering work, let `unknowns-first` own map-versus-territory discovery and proof escalation when available; otherwise apply the same reality-first judgment at lightweight scope. Capture a sourced baseline whenever the requested change is judged relative to current behavior or measurement, and keep its evidence state and mismatch consequence explicit. Preserve material uncertainty instead of inventing certainty or asking the user for facts the environment can settle. Broader repo identity and implementation investigation remain downstream unless needed to know what the user means.

### 3. Resolve human decisions

Resolve only material decisions that available evidence cannot settle and that genuinely belong to the user. As the normal interaction budget, aim for one compact round with no more than five questions; for each question, prefer 2–4 materially distinct options and one concise recommendation with its basis. Include only the context needed to choose well. If the budget would materially reduce goal attainment or stability, exceed it rather than omit a necessary user decision; exceeding it is not itself a failure. Do not silently choose a direction or present a recommendation or default as confirmed user intent. Use a reversible default only when it leaves Goal and user-owned Boundary unchanged, the cost of being wrong is bounded and reversible, and mismatch is detectable; mark it visibly as unconfirmed with its basis and consequence. When a user decision is required, expose the smallest useful decision surface and stop; do not manufacture another internal round by answering it on the user's behalf.

### 4. Compile and validate

For each invocation, compile the best current intent into one minimum-sufficient, self-contained artifact when the five semantics are stable enough for the next consumer. If a target consumer or carrier is named, adapt organization, density, and context packaging for that consumer while preserving intent authority, material uncertainty, boundaries, and proof obligations. Carrier adaptation must not import the consumer's architecture, planning, execution, or verification procedure into Prompt Atlas. Prefer rich existing references—code, tests, traces, artifacts, schemas, rubrics—over replaying their contents.

For a stable Artifact-mode result, append one concise **Handoff Hint** based on the remaining uncertainty:

- **Direct Execute** — choose this when the remaining uncertainty is implementation-level and can be resolved during execution without making a material architecture or solution choice that could change responsibility boundaries, structure, interfaces, migration strategy, Goal, Boundary, or proof obligation. The hint should say that the artifact can be used directly as execution input and briefly state why no design pass is needed.
- **Wayfinder** — choose this when intent and protected boundaries are stable but a material architecture or solution choice still remains. The hint should say that the artifact should be used as Wayfinder design input to resolve How without reopening settled What.

Do not use task size alone to choose between these routes. Do not expose Leader as a separate top-level route; if unattended execution is desired, Leader may consume a Direct Execute artifact as an execution carrier. The Handoff Hint may explain this only when it is directly useful. It never starts the next capability.

For repo-changing work, make write scope explicit when implicit scope is unsafe. Prompt Atlas is done when the next consumer can continue without re-deriving what the user means. Downstream work may enrich implementation knowledge and current evidence, but settled user intent changes only with new user authority; contradictory territory evidence may reopen assumptions, feasibility, proof state, or route, not user-owned intent. A proof gap cannot become completion through handoff.

When material uncertainty still prevents stable compilation, expose only the next useful alignment outcome: a focused `probe`, a human `ask`, a bounded conditional or default, or the exact blocker, then stop this invocation. Do not append a downstream Handoff Hint while user-owned intent or required grounding is still unresolved. Further intent convergence requires a later invocation with new user authority. A later invocation may also refine territory grounding from new authoritative evidence without changing user-owned intent. Without either new signal, additional self-review may improve consistency or expression but must not promote an inference, recommendation, default, or uncertainty into settled intent. Exploration-oriented intent may close on a bounded decision or finding with remaining uncertainty explicit; correctness or completion claims must carry the trust obligations selected by `completion-trust`.

If the user requests a fresh-session handoff, save the concise artifact as Markdown in the operating system temporary directory, reference existing artifacts rather than copying them, redact sensitive context, add `Suggested skills`, and return the absolute path.

## Output

In Artifact mode, return one concise Intent Contract, requested carrier, or smallest necessary unresolved outcome. Stable artifacts end with a brief Handoff Hint choosing Direct Execute or Wayfinder; normally keep the hint to 1–3 sentences. For Chinese output, target roughly 100–200 characters and keep routine artifacts within 1,000 characters. Treat these as normal output budgets, not completion gates: exceed them when fitting the budget would materially reduce goal attainment or stability. In Embedded mode, return the compiled artifact or decision surface to the caller. In both modes, delivery ends the Prompt Atlas invocation.