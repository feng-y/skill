---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered cross-turn hints into a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Do not substitute an intent brief for execution the user already requested.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground the context that matters, surface only decisions that genuinely belong to the user, and leave the next consumer a concise contract that does not require rediscovering requirement meaning.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, approval limits, and any user-owned priority needed to resolve competing constraints;
- **Immediate Task** — what should be completed now without prescribing the implementation;
- **Success / Stop** — the outcome and evidence that close the work, or what real blocker prevents closure; prefer achieved-result criteria over activity or work-volume criteria.

Keep these semantics distinct and recoverable, but do not turn them into a form unless the user asks. Prompt Atlas owns intent understanding, not architecture choice, implementation planning, execution, or a durable repo-identity harness.

Choose the output mode from the request:

- **Artifact mode** — return the completed Intent Contract or requested carrier.
- **Embedded mode** — establish the contract internally, then return control to the calling workflow instead of replacing the requested work with a prompt.

## Judgment rules

- **Typed authority:** the current user owns intent; current repo, config, tests, runtime, and other authoritative evidence own territory. Conversation and Memory may recover intent or suggest facts, but they do not override current evidence.
- **Intent before means:** recover the change a solution-shaped request is trying to cause. Treat a named approach as a suggestion unless the user makes it a boundary.
- **Reality before clarification:** investigate only unknowns whose answer could materially change Goal, Boundary, Immediate Task, Success / Stop, or the safe route. For engineering work, use `unknowns-first` when available instead of duplicating its territory / proof gate.
- **Judgment before grammar:** use the surrounding context and evidence to decide what matters. Do not classify, enumerate, or expose internal intake state when the same decision can be made directly and safely.
- **Progressive disclosure:** load detailed guidance only when needed. Use [chatgpt-memory.md](references/chatgpt-memory.md) when relevant Memory is actually available, and [completion-trust.md](references/completion-trust.md) when the contract needs a correctness or completion claim.

## Intent Take

### 1. Recover

Read the current request together with relevant corrections, prior decisions, examples, and context. Latest explicit corrections win over older compatible intent. Replace superseded meaning rather than accumulating it. Separate desired result, suggested means, and hard constraints. When current requirements compete, preserve any user-stated priority or tradeoff order needed for the next consumer to judge correctly; if that priority is material and genuinely user-owned but still missing, resolve it as a human decision rather than inventing one.

### 2. Ground

Close only material task-level uncertainty. Prefer the smallest authoritative check through code, config, tests, runtime, traces, references, or another appropriate capability. Capture a baseline when the requested change compares, preserves, migrates, regresses, counts, or claims performance. If evidence is unavailable, keep the uncertainty visible with its practical effect instead of inventing certainty.

For engineering work, let `unknowns-first` handle map-versus-territory discovery and proof escalation. Prompt Atlas consumes its conclusion; it does not mirror its state machine. Broader repo identity and implementation investigation remain downstream unless they are necessary to know what the user means.

### 3. Resolve human decisions

Ask only when the remaining material choice genuinely belongs to the user and available evidence cannot settle it. Gather already-visible related choices together rather than drip-feeding questions. Keep one clarification round to at most five questions. Before reaching that budget, ground further and combine decisions that share one judgment; use a reversible default only where it is independently safe. If more than five irreducible user-owned decisions still remain, narrow the current contract instead of transferring an oversized decision burden to the user or silently guessing the rest.

Render the smallest sufficient decision surface: what is established, what evidence cannot decide, why the judgment belongs to the user, and what materially changes between the viable choices. For a sharp decision, prefer 2–4 materially distinct options with their consequences; use an open question only when the choices cannot be bounded honestly. When evidence supports a preferred choice, include one concise recommendation with its basis and main tradeoff. Recommendations remain advisory until the user confirms them.

Do not silently make a direction-changing decision for the user. A reversible default is allowed only when it does not change Goal or a user-owned Boundary, the cost of being wrong is bounded and reversible, and the mismatch can be detected; mark it visibly as an unconfirmed Atlas default with its basis and consequence.

### 4. Compile and validate

Write one minimum-sufficient, self-contained Intent Contract in this order: desired change → current context → protected boundary → work now → success or stop. Prefer rich existing references—code, tests, traces, artifacts, schemas, rubrics—over replaying their contents. Keep the default artifact out of spec form: no phases, implementation sequence, ticket decomposition, command inventory, or execution-loop mechanics.

Preserve material uncertainty, recommendations, defaults, proof gaps, handoff obligations, and any material priority between competing user-owned constraints where a consumer can recover their owner, basis, and effect. Never present an Atlas recommendation or default as confirmed user intent.

Prompt Atlas is done when the next consumer can continue without re-deriving what the user means, reopening superseded intent, re-framing an already-visible user decision, or recreating an evidence-backed recommendation Atlas should already have surfaced.

When intake cannot compile yet, expose only the next useful outcome: a focused `probe`, a human `ask`, a bounded conditional/default, a named capability handoff, or the exact blocker. Do not emit the intake analysis.

For execution-oriented intent, completion requires trusted evidence and an achieved-result criterion rather than mere work performed; when independent acceptance is required, stop at `ready for independent acceptance`. Exploration-oriented intent may close on a bounded decision or finding with remaining uncertainty explicit.

If the user requests a fresh-session handoff, save the concise contract as Markdown in the operating system temporary directory, reference existing artifacts rather than copying them, redact sensitive context, add `Suggested skills`, and return the absolute path.

## Output

In Artifact mode, return one concise Intent Contract or requested carrier. For Chinese output, target roughly 100–200 characters and keep routine takes within 1,000 characters; exceed the budget only for material boundaries, evidence, decisions, or blockers. In Embedded mode, continue the caller's workflow after intake.