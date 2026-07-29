---
name: prompt-atlas
description: Adaptively converge a one-sentence goal or scattered, evolving cross-turn hints into a stable, consumer-ready Intent Contract or requested prompt/carrier covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Explicit /prompt-atlas use returns the compiled artifact as the terminal result of this invocation.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground the context that matters, resolve only decisions that genuinely belong to the user, and leave the next consumer a concise artifact that does not require rediscovering requirement meaning.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, approval limits, protected evaluation or proof rules when material, and any user-owned priority needed to resolve competing constraints;
- **Immediate Task** — what should be completed now without prescribing the implementation;
- **Success / Stop** — the outcome and evidence that close the work, or what real blocker prevents closure; prefer achieved-result criteria over activity or work-volume criteria.

Keep these semantics distinct and recoverable, but do not turn them into a form unless the user asks. Prompt Atlas owns intent understanding, convergence across alignment turns, and carrier compilation—not architecture choice, implementation planning, execution, or a durable repo-identity harness. Each Intent Take invocation terminates at artifact delivery; a next-capability hint is non-executable routing metadata, not a transition into downstream work.

Choose the output mode from the invocation:

- **Artifact mode** — the default for explicit `/prompt-atlas` use and direct requests to clarify, consolidate, prepare, hand off, or rewrite a requirement. Return the completed Intent Contract or requested carrier and stop this invocation. Optionally include one concise next-capability hint when useful.
- **Embedded mode** — only when another capability or workflow explicitly invokes Prompt Atlas as an intake sub-capability. Return the compiled artifact to that caller and stop the Prompt Atlas invocation. Do not infer Embedded mode merely because the user's ultimate task could later be planned or executed.

Use detailed guidance only when it becomes relevant: [contract-anatomy.md](references/contract-anatomy.md) for intent-artifact goal attainment and stability, and [completion-trust.md](references/completion-trust.md) for correctness or completion claims.

## Intent Take

### 1. Recover

Recover from the current request, relevant corrections, prior decisions, and examples. When a prior Atlas contract or alignment result is available, use its still-valid settled semantics as the baseline rather than restarting from raw history. The current user owns intent; current authoritative evidence owns territory. Latest explicit corrections supersede older meaning. Recover the desired change separately from suggested means and hard boundaries, including any user-stated priority needed to judge competing constraints.

### 2. Ground

Investigate only unknowns whose answers could materially change Goal, Boundary, Immediate Task, Success / Stop, or the safe route. Prefer the smallest authoritative check and rich existing references. For repo-scoped work, include governing repo-local constraints or acceptance rules when they can materially change Boundary, Success / Stop, proof obligation, or route; these are contract facts rather than downstream implementation detail. For engineering work, let `unknowns-first` own map-versus-territory discovery and proof escalation when available; otherwise apply the same reality-first judgment at lightweight scope. Capture a sourced baseline whenever the requested change is judged relative to current behavior or measurement, and keep its evidence state and mismatch consequence explicit. Preserve material uncertainty instead of inventing certainty or asking the user for facts the environment can settle. Broader repo identity and implementation investigation remain downstream unless needed to know what the user means.

### 3. Resolve human decisions

Resolve only material decisions that available evidence cannot settle and that genuinely belong to the user. As the normal interaction budget, aim for one compact round with no more than five questions; for each question, prefer 2–4 materially distinct options and one concise recommendation with its basis. Include only the context needed to choose well. If the budget would materially reduce goal attainment or stability, exceed it rather than omit a necessary user decision; exceeding it is not itself a failure. Do not silently choose a direction or present a recommendation or default as confirmed user intent. Use a reversible default only when it leaves Goal and user-owned Boundary unchanged, the cost of being wrong is bounded and reversible, and mismatch is detectable; mark it visibly as unconfirmed with its basis and consequence.

### 4. Compile and validate

Once remaining uncertainty would not materially change Goal, Boundary, Immediate Task, Success / Stop, or downstream route, compile one minimum-sufficient, self-contained artifact from the five semantics. If a target consumer or carrier is named, adapt organization, density, and context packaging for that consumer while preserving intent authority, material uncertainty, boundaries, and proof obligations. Carrier adaptation must not import the consumer's architecture, planning, execution, or verification procedure into Prompt Atlas. Prefer rich existing references—code, tests, traces, artifacts, schemas, rubrics—over replaying their contents. A next-capability hint may identify where the artifact should go next, but it does not trigger that capability within this invocation.

For repo-changing work, make write scope explicit when implicit scope is unsafe. Prompt Atlas is done when the next consumer can continue without re-deriving what the user means. Downstream work may enrich implementation knowledge and current evidence, but settled user intent changes only with new user authority; contradictory territory evidence may reopen assumptions, feasibility, or route, not user intent. A proof gap cannot become completion through handoff.

When material intent uncertainty still prevents stable compilation, expose only the next useful alignment outcome: a focused `probe`, a human `ask`, a bounded conditional or default, a named capability handoff, or the exact blocker. Do not emit the intake analysis. Exploration-oriented intent may close on a bounded decision or finding with remaining uncertainty explicit; correctness or completion claims must carry the trust obligations selected by `completion-trust`.

If the user requests a fresh-session handoff, save the concise artifact as Markdown in the operating system temporary directory, reference existing artifacts rather than copying them, redact sensitive context, add `Suggested skills`, and return the absolute path.

## Output

In Artifact mode, return one concise Intent Contract or requested carrier. For Chinese output, target roughly 100–200 characters and keep routine artifacts within 1,000 characters. Treat these as normal output budgets, not completion gates: exceed them when fitting the budget would materially reduce goal attainment or stability. In Embedded mode, return the compiled artifact to the caller. In both modes, artifact delivery ends the Prompt Atlas invocation.