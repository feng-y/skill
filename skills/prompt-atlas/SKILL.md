---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered cross-turn hints into a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Do not substitute an intent brief for execution the user already requested.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is trying to change, why it matters now, what is already true, what must not drift, what work should happen now, and what outcome or blocker closes the request.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, frozen evaluation rules, acceptable differences, scope, and approval limits;
- **Immediate Task** — what the consumer should complete now without prescribing the implementation;
- **Success / Stop** — the outcome and proportional evidence that fulfill the work, stop expansion, or expose a real blocker.

Keep the five semantics distinct and ordered. Visible headings are optional; prose style is secondary to semantic stability. Prompt Atlas must work standalone. It may inspect current repo evidence for this task, but it does not build a durable repo-identity harness, select an architectural evolution path, write a spec, plan implementation, or execute the work.

Choose the output mode from the user's request:

- **Artifact mode** — when the user asks for an intent brief, prompt, goal carrier, or handoff, return the completed Intent Contract.
- **Embedded mode** — when a broader workflow invokes intake before doing the requested work, establish the contract internally and return control to that workflow; do not replace the requested implementation, review, or decision with a prompt.

## Intent Take loop

1. **Capture**
   - Start equally well from a one-sentence goal or scattered hints across turns.
   - Resolve user-held intent in this order: latest explicit correction or rejection → current explicit requirements → compatible earlier decisions and constraints → examples and repeated hints → Memory. Replace superseded meaning instead of accumulating it.
   - For a solution-shaped request, recover the change it is meant to cause. Keep the named means open when suggested; preserve it in Immediate Task or Boundary when the user explicitly requires it.
   - Separate desired result, suggested means, and hard constraint.
   - Use conversation, project context, and available Memory as intent evidence, never as proof of current repo state. When relevant ChatGPT context is already available, read [chatgpt-memory.md](references/chatgpt-memory.md).

2. **Enrich**
   - Classify the first material gap by its closer: user-held intent, inspectable territory, or another domain capability.
   - For engineering work, use `unknowns-first` when available. Otherwise apply its light gate directly: Target / Territory / first route-changing Unknown / minimum Proof.
   - Treat a hint or unknown as material only when changing or removing it would alter one of the five semantics, the closure state, or an execution-protection choice.
   - Close only material task-level unknowns. Use the smallest sufficient chain through code, config, tests, runtime, traces, or another authoritative source.
   - Verify current facts whose falsity would change the contract. Capture a baseline when success compares, preserves, migrates, regresses, counts, or claims performance; if it cannot be measured safely now, make the check an execution precondition and state what a mismatch blocks.
   - Keep broader repo identity work and implementation choices out of intake. Fold supported conclusions, not investigation transcripts, into the contract.

3. **Resolve**
   - Choose exactly one terminal for the current intake step: `probe` when one territory check can decide; `ask` when only the user can make a direction-changing choice; `bounded conditional` when direction and safe action remain clear without the missing evidence; `blocker` when a contradiction or missing decision prevents a safe contract.
   - After a probe, return to Enrich with the evidence and reclassify. When no material gap remains, compile.
   - Use a reversible default only when it changes neither Goal nor Boundary. Record its evidence state and cost of being wrong in the owning slot; never default a user-owned direction change.

4. **Compile**
   - Compile deterministically: the same resolved input must yield the same semantic commitments, order, and execution-protection choices. Wording may vary.
   - Render in this fixed order: desired change → current facts and bounded uncertainty → protected boundary → work to complete now → completion or blocker. These are semantic slots, not required headings.
   - Keep every slot distinct; do not merge slots. Never reorder or silently omit a material slot; give each fact one home and return one artifact without competing variants or intake analysis.
   - Write the result as minimum-sufficient, self-contained engineer-to-engineer prose. Keep decisions and real invariants, express intent instead of imitating examples, and reference rich artifacts instead of replaying them.
   - Keep the default artifact out of spec form: no phases, implementation sequence, ticket decomposition, command inventory, or full acceptance checklist.
   - For repo-changing work, carry an explicit write boundary when multiple edit surfaces, shared state, unrelated user changes, or likely scope drift make implicit scope unsafe. Prefer verified writable paths or ownership over a blacklist.
   - When the requested result needs a correctness or completion claim, read [completion-trust.md](references/completion-trust.md). Compile only the material Proof obligation, Integrity boundary, and self-attestation policy into their owning slots rather than adding another section.
   - If the user requests a fresh-session handoff, save the concise contract as Markdown in the operating system's temporary directory—not the workspace—reference existing artifacts, redact sensitive context, add `Suggested skills`, and return the absolute path.

5. **Validate**
   - Confirm the artifact maps back to all five semantics in order, every material hint appears once, territory claims have evidence, and remaining uncertainty has bounded effect.
   - Return to Enrich only when a consumer would otherwise have to rediscover requirement meaning; downstream implementation investigation is allowed.
   - Remove any sentence or mechanism whose absence would not change intent, protected boundaries, evidence, or completion behavior.
   - Finish the current pass in exactly one state: complete contract, contract ready for independent acceptance, probe with its next evidence check, one direction-changing question, contract with one bounded conditional, or exact blocker. Do not emit the intake analysis.

## Output

In Artifact mode, return one concise Intent Contract or the requested carrier. For Chinese output, target roughly 100–200 characters and keep routine takes within 1,000 characters; exceed the budget only for material boundaries, evidence, or blockers. In Embedded mode, continue the caller's workflow after intake.

Apply typed authority: the current user statement owns intent; current repo, config, tests, and runtime evidence own territory. Preserve existing behavior and repo invariants unless the request changes them. Execution intent closes on an achieved result with trusted evidence; when self-attestation is forbidden, the executor closes only at `ready for independent acceptance` until external judgment passes. Exploration intent closes on a bounded decision or finding with remaining uncertainty explicit. Keep solution uncertainty open after requirement meaning is settled.
