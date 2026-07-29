---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered cross-turn hints into a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Do not substitute an intent brief for execution the user already requested.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground the context that matters, resolve only decisions that genuinely belong to the user, and leave the next consumer a concise contract that does not require rediscovering requirement meaning.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, approval limits, protected evaluation or proof rules when material, and any user-owned priority needed to resolve competing constraints;
- **Immediate Task** — what should be completed now without prescribing the implementation;
- **Success / Stop** — the outcome and evidence that close the work, or what real blocker prevents closure; prefer achieved-result criteria over activity or work-volume criteria.

Keep these semantics distinct and recoverable, but do not turn them into a form unless the user asks. Prompt Atlas owns intent understanding, not architecture choice, implementation planning, execution, or a durable repo-identity harness.

Choose the output mode from the request:

- **Artifact mode** — return the completed Intent Contract or requested carrier.
- **Embedded mode** — establish the contract internally, then return control to the calling workflow instead of replacing the requested work with a prompt.

Use detailed guidance only when it becomes relevant: [contract-anatomy.md](references/contract-anatomy.md) for contract completeness, stability, goal attainment, and downstream readiness; [completion-trust.md](references/completion-trust.md) for correctness or completion claims; and [chatgpt-memory.md](references/chatgpt-memory.md) when relevant Memory is available.

## Intent Take

### 1. Recover

Read the current request with relevant corrections, prior decisions, examples, conversation context, and available Memory. The current user owns intent; current authoritative evidence owns territory. Conversation and Memory may recover intent or suggest facts but do not override current evidence. Latest explicit corrections supersede older meaning rather than accumulating beside it. Recover the desired change separately from suggested means and hard boundaries, including any user-stated priority needed to judge competing constraints.

### 2. Ground

Investigate only unknowns whose answers could materially change Goal, Boundary, Immediate Task, Success / Stop, or the safe route. Prefer the smallest authoritative check and rich existing references. For engineering work, let `unknowns-first` own map-versus-territory discovery and proof escalation when available and consume its conclusion rather than mirroring its state machine; when unavailable, apply the same reality-first judgment directly at lightweight scope. Capture a sourced baseline whenever the requested change is judged relative to current behavior or measurement, and keep its evidence state and the consequence of mismatch explicit. Preserve material uncertainty instead of inventing certainty or asking the user for facts the environment can settle. Broader repo identity and implementation investigation remain downstream unless they are necessary to know what the user means.

### 3. Resolve human decisions

Resolve only material decisions that available evidence cannot settle and that genuinely belong to the user. As the normal interaction budget, aim for one compact round with no more than five questions; for each question, prefer 2–4 materially distinct options and one concise recommendation with its basis. Include only the context needed to make the choice well. If staying within that budget would materially reduce Intent Take correctness, completeness, or goal attainment, exceed it rather than omit a necessary user decision; exceeding the budget is not itself a failure. Do not silently choose a direction or present an Atlas recommendation or default as confirmed user intent. Use a reversible default only when it leaves Goal and user-owned Boundary unchanged, the cost of being wrong is bounded and reversible, and a mismatch is detectable; mark it visibly as unconfirmed with its basis and consequence.

### 4. Compile and validate

Write one minimum-sufficient, self-contained Intent Contract in this order: desired change → current context → protected boundary → work now → success or stop. Prefer rich existing references—code, tests, traces, artifacts, schemas, rubrics—over replaying their contents. Keep it an intent contract rather than a downstream spec or execution plan.

Preserve material uncertainty, recommendations, defaults, proof gaps, handoff obligations, and any material priority between competing user-owned constraints where a consumer can recover their owner, basis, and effect. For repo-changing work, make write scope explicit when multiple edit surfaces, shared state, unrelated user changes, or likely scope drift make implicit scope unsafe.

Prompt Atlas is done when the next consumer can continue without re-deriving what the user means, reopening superseded intent, re-framing an already-visible user decision, or recreating an evidence-backed recommendation Atlas should already have surfaced. Downstream work may enrich implementation knowledge, but without contradictory evidence it must not reopen settled intent, demote a hard boundary into a suggestion, or turn an unresolved proof gap into completion.

When intake cannot compile yet, expose only the next useful outcome: a focused `probe`, a human `ask`, a bounded conditional or default, a named capability handoff, or the exact blocker. Do not emit the intake analysis. Exploration-oriented intent may close on a bounded decision or finding with remaining uncertainty explicit; correctness or completion claims must carry the trust obligations selected by `completion-trust`.

If the user requests a fresh-session handoff, save the concise contract as Markdown in the operating system temporary directory, reference existing artifacts rather than copying them, redact sensitive context, add `Suggested skills`, and return the absolute path.

## Output

In Artifact mode, return one concise Intent Contract or requested carrier. For Chinese output, target roughly 100–200 characters and keep routine contracts within 1,000 characters. Treat these as normal output budgets, not completion gates: if staying within them would materially reduce Intent Take correctness, completeness, or goal attainment, exceed them rather than compress away what the next consumer needs. In Embedded mode, continue the caller's workflow after intake.
