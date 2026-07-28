---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered cross-turn hints into a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Do not substitute an intent brief for execution the user already requested.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is trying to change, why it matters now, what is already true, what must not drift, what work should happen now, and what outcome, handoff, or blocker closes the current step.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, frozen evaluation rules, acceptable differences, scope, and approval limits;
- **Immediate Task** — what the consumer should complete now without prescribing the implementation;
- **Success / Stop** — the completion rule and proportional evidence that fulfill the work or expose a real blocker.

Keep the five semantics distinct, ordered, and recoverable as one contiguous segment each. Visible headings are optional; prose style is secondary to semantic stability. Prompt Atlas must work standalone. It may inspect current repo evidence for this task, but it does not build a durable repo-identity harness, select an architectural evolution path, write a spec, plan implementation, or execute the work.

Choose the output mode from the user's request:

- **Artifact mode** — when the user asks for an intent brief, prompt, goal carrier, or handoff, return the completed Intent Contract.
- **Embedded mode** — when a broader workflow invokes intake before doing the requested work, establish the contract internally and return control to that workflow; do not replace the requested implementation, review, or decision with a prompt.

Prompt Atlas succeeds when Intent Take is stable enough that the next consumer does not need to rediscover what the user means. That may enable direct execution, but it also includes reliable handoff into planning consumers such as wayfinder: once Intent Take is achieved, a planning workflow should be able to continue from the contract without reopening requirement meaning.

At the demand-understanding layer, Prompt Atlas should cover at least the high-value intake abilities that a strong Leader-style system demonstrates before execution begins: recovering the real requested change, separating intent from suggested means and hard constraint, closing route-changing clarification in the smallest sufficient set, respecting typed authority, and refusing to compile a false execution-ready target. It builds this layer on top of `unknowns-first` and related territory / proof gates, then compiles the result into a shared Intent Contract. It does not absorb execution-carrier mechanics such as task-zero protocols, command inventories, anti-cheat enforcement, rollback, or continuity files.

## Intent Take loop

1. **Capture**
   - Start equally well from a one-sentence goal or scattered hints across turns.
   - Resolve user-held intent in this order: latest explicit correction or rejection → current explicit requirements → compatible earlier decisions and constraints → examples and repeated hints → Memory. Replace superseded meaning instead of accumulating it.
   - For a solution-shaped request, recover the change it is meant to cause. Keep the named means open when suggested; preserve it in Immediate Task or Boundary when the user explicitly requires it.
   - Separate desired result, suggested means, and hard constraint.
   - Use conversation, project context, and available Memory as intent evidence, never as proof of current repo state. No remembered or hinted repo fact becomes territory without current evidence. When relevant ChatGPT context is already available, read [chatgpt-memory.md](references/chatgpt-memory.md).

2. **Enrich**
   - List candidate material gaps. A gap is material only when changing or removing it would alter one of the five semantics, the current-step outcome, or an execution-protection choice.
   - Describe each material item on separate axes rather than one exclusive list: role (`current fact`, `baseline`, or `verification dependency`), evidence state (`verified`, `inferred`, or `unmeasured`), and closure effect (`informational`, `required precondition`, or `proof gap`). Only combine compatible values; do not force these axes into one exclusive classification.
   - When multiple user-owned material choices are already sharp and no territory probe should come first, Atlas may harvest them in one compact clarification set instead of serial single questions. Include only choices whose answers would change Goal, Boundary, proof or closure, write boundary, or capability handoff. Do not use this to gather implementation sequence, command inventory, stop-loss, or other execution-carrier detail.
   - For engineering work, use `unknowns-first` when available. Otherwise apply its light gate directly: Target / Territory / first route-changing Unknown / minimum Proof. Atlas must strengthen that base with demand-understanding work that `unknowns-first` does not own on its own: supersession, intent-vs-means separation, compact clarification harvest, slot ownership, and consumer routing.
   - Close only material task-level unknowns. Use the smallest sufficient chain through code, config, tests, runtime, traces, or another authoritative source.
   - Verify current facts whose falsity would change the contract. Capture a baseline when success compares, preserves, migrates, regresses, counts, or claims performance, and preserve its subject, source, evidence state, and what a mismatch blocks; if it cannot be measured safely now, carry it forward as a required precondition or proof gap and state what a mismatch blocks.
   - Keep broader repo identity work and implementation choices out of intake. Fold supported conclusions, not investigation transcripts, into the contract.

3. **Resolve**
   - Choose the first material gap deterministically:
     1. a user-owned contradiction or missing choice that would change Goal or Boundary;
     2. a territory-owned fact whose falsity would change route, scope, write boundary, or preserved behavior;
     3. a proof or baseline gap whose falsity would change Success / Stop, self-attestation, or closure;
     4. a consumer or handoff gap that would force downstream reinterpretation.
   - Tie-break within a class by earliest affected slot in fixed order: Goal → Current Context → Boundary → Immediate Task → Success / Stop. If still tied, choose the cheapest single closer that can decide it.
   - Pick exactly one closer class: `user`, `territory`, `capability`, `reversible-default`, or `none`.
   - A `user` closer may be one direction-changing question or one compact clarification harvest when several already-sharp user-owned choices together determine a single contract shape. Ask only after territory evidence is exhausted for those choices; do not drip-feed questions that were already jointly visible.
   - When `unknowns-first` is active, total-map its terminals: `continue → compile`, `probe → probe`, `ask → ask`, `note → bounded conditional`, `must-verify-in-repo → bounded conditional` when route and safe action remain clear but a named verifier must run before closure otherwise `→ blocker`, and `full-map → handoff` when a named next capability is available and the settled contract can transfer without reopening intake otherwise `→ blocker`.
   - Emit exactly one current-step outcome: `compile`, `probe`, `ask`, `bounded conditional`, `handoff`, or `blocker`.
   - After a probe, return to Enrich with the evidence and reclassify. When no material gap remains, compile.
   - Atlas may apply a reversible default only when it changes neither Goal nor a user-owned Boundary, safe progress remains clear without branching the contract into variants, the wrong-cost is bounded and reversible, and the contract names where a mismatch would surface. Never default a user-owned direction change.

4. **Compile**
   - Compile only after authority ownership, the first material gap, the closer class, and slot ownership are fixed. The same raw input and evidence state must yield the same authority winner, first material gap, current-step outcome, slot placement, and execution-protection choice. Equivalent one-sentence goals and scattered hints that resolve to the same authority-owned intent and evidence state must yield equivalent contracts. Wording may vary.
   - Render in this fixed order: desired change → current facts and bounded uncertainty → protected boundary → work to complete now → completion rule or blocker. These are semantic slots, not required headings.
   - Keep every slot distinct and contiguous. Give each material fact one home. Do not merge slots, silently omit a material slot, or return competing variants.
   - Write the result as minimum-sufficient, self-contained engineer-to-engineer prose. Keep decisions and real invariants, express intent instead of imitating examples, and reference rich artifacts instead of replaying them.
   - Keep the default artifact out of spec form: no phases, implementation sequence, ticket decomposition, command inventory, or full acceptance checklist.
   - Any surviving user-owned choice, territory-owned uncertainty, reversible default, or consumer-owned follow-through must stay visible in its owning slot with recoverable owner, state, basis, and effect.
   - Slot ownership defaults:
     - **Goal** — settled desired change only; unresolved user-owned direction changes force `ask` or `blocker`.
     - **Current Context** — verified facts, inferred facts, contradictions, baseline subject, source, and evidence state, verifier strength, and the basis for a default or proof gap.
     - **Boundary** — invariants, acceptable differences, write boundary, safe-action fences, and any frozen Judge / Population / Object / Metric dimensions.
     - **Immediate Task** — the next question, clarification set, check, verification precondition, consumer follow-through, or named capability handoff.
     - **Success / Stop** — the closure consequence, completion threshold, mismatch rule, and, when a contract is emitted, the current closure state.
   - Normalize contract closure to `complete`, `ready for independent acceptance`, or `bounded decision / finding`. `blocker` is a current-step outcome, not a closure state. Execution-oriented requests close on trusted proof; exploration-oriented requests close on a bounded answer or decision with remaining uncertainty explicit.
   - For repo-changing work, carry an explicit write boundary when multiple edit surfaces, shared state, unrelated user changes, or likely scope drift make implicit scope unsafe. Prefer verified writable paths or ownership over a blacklist.
   - When the requested result needs a correctness or completion claim, read [completion-trust.md](references/completion-trust.md). Compile only the material Proof obligation, Integrity boundary, and self-attestation policy into their owning slots rather than adding another section.
   - When the outcome is `handoff`, return one consumer-ready contract. Name the next capability and next work in Immediate Task, and keep open proof, uncertainty, and boundary obligations in their owning slots so the next capability continues from the contract instead of re-running intake.
   - If the user requests a fresh-session handoff, save the concise contract as Markdown in the operating system's temporary directory—not the workspace—reference existing artifacts, redact sensitive context, add `Suggested skills`, and return the absolute path.

5. **Validate**
   - Confirm the artifact maps back to all five semantics in order, each slot remains recoverable as one contiguous segment, every material fact appears once, territory claims have evidence, and remaining uncertainty has bounded effect.
   - For every applicable surviving non-settled item, a downstream consumer must be able to recover its owner, evidence state, basis, and effect from the contract itself.
   - When the visible outcome is `ask`, every question in that outcome must already be sharp, user-owned, and route-changing for this contract, and the set must be no larger than needed to avoid a second clarification round on already-known decisions.
   - When material to this contract, a downstream consumer must also be able to tell which facts are verified versus inferred, whether a baseline exists, its source, and what a mismatch blocks, what proof is still missing, whether next work belongs to the user, direct execution, a planning consumer such as wayfinder, or another named capability, and which closure state currently applies if a contract is emitted.
   - At minimum, a planning consumer should be able to continue from the contract without re-deriving requirement meaning, reopening superseded intent, or asking for route-defining context that Atlas should already have settled.
   - At the demand-understanding layer, Atlas is incomplete if a strong Leader-style intake would still have to redo the real-change recovery, intent-vs-means split, typed-authority judgment, or already-sharp route-changing clarification before downstream work can proceed.
   - Return to Enrich only when a consumer would otherwise have to rediscover requirement meaning; downstream implementation investigation is allowed.
   - Remove any sentence or mechanism whose absence would not change intent, protected boundaries, evidence, ownership, or completion behavior.
   - Finish the current pass in exactly one visible outcome: `probe`, `ask`, `bounded conditional`, `handoff`, or exact `blocker`; otherwise emit one compiled contract whose closure is `complete`, `ready for independent acceptance`, or `bounded decision / finding`. Do not emit the intake analysis.

## Output

In Artifact mode, return one concise Intent Contract or the requested carrier. For Chinese output, target roughly 100–200 characters and keep routine takes within 1,000 characters; exceed the budget only for material boundaries, evidence, or blockers. In Embedded mode, continue the caller's workflow after intake.

Apply typed authority: the current user statement owns intent; current repo, config, tests, and runtime evidence own territory. Preserve existing behavior and repo invariants unless the request changes them. Execution intent closes on an achieved result with trusted evidence; when self-attestation is forbidden, the executor closes only at `ready for independent acceptance` until external judgment passes. Exploration intent closes on a bounded decision or finding with remaining uncertainty explicit. Keep solution uncertainty open after requirement meaning is settled. Downstream consumers may enrich or execute the contract, but they must not reopen superseded intent without contradictory evidence, relocate a hard boundary into a suggestion, or turn a proof gap into silent completion.
