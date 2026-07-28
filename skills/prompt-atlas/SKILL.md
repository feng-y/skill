---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered cross-turn hints into a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, autonomous, spec, issue, or execution work. Do not substitute an intent brief for execution the user already requested.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is trying to change, why it matters now, what is already true, what must not drift, what work should happen now, and what outcome or blocker closes the request.

Compile five minimum semantics:

- **Goal** — the real problem and desired change;
- **Current Context** — only current facts, evidence, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, and approval limits;
- **Immediate Task** — what the consumer should complete now without prescribing the implementation;
- **Success / Stop** — the outcome and proportional evidence that fulfill the work, stop expansion, or expose a real blocker.

Keep the five semantics distinct and ordered. Visible headings are optional; prose style is secondary to semantic stability. Prompt Atlas must work standalone. It may inspect current repo evidence for this task, but it does not build a durable repo-identity harness, select an architectural evolution path, write a spec, plan implementation, or execute the work.

Choose the output mode from the user's request:

- **Artifact mode** — when the user asks for an intent brief, prompt, goal carrier, or handoff, return the completed Intent Contract.
- **Embedded mode** — when a broader workflow invokes intake before doing the requested work, establish the contract internally and return control to that workflow; do not replace the requested implementation, review, or decision with a prompt.

## Intent Take loop

1. **Capture**
   - Start equally well from a one-sentence goal or scattered hints across turns.
   - Treat current corrections as overrides, examples as direction unless made mandatory, rejections as boundary evidence, and repetition as stronger evidence rather than more output.
   - Separate desired result, suggested means, and hard constraint. Keep means open unless the user makes them binding.
   - Use conversation, project context, and available Memory as intent evidence, never as proof of current repo state. When relevant ChatGPT context is already available, read [chatgpt-memory.md](references/chatgpt-memory.md).

2. **Enrich**
   - Classify the first material gap by its closer: user-held intent, inspectable territory, or another domain capability.
   - For engineering work, use `unknowns-first` when available. Otherwise apply its light gate directly: Target / Territory / first route-changing Unknown / minimum Proof.
   - Close only task-level unknowns that could change one of the five semantics or a necessary execution protection. Use the smallest sufficient chain through code, config, tests, runtime, traces, or another authoritative source.
   - Keep broader repo identity work and implementation choices out of intake. Fold supported conclusions, not investigation transcripts, into the contract.
   - If evidence is unavailable, keep a bounded conditional when direction remains clear; otherwise state the exact blocker.

3. **Resolve**
   - Ask one concise question only when the answer belongs to the user and would change direction. Do not ask for facts that territory evidence can supply.
   - Preserve an unresolved human contradiction as a blocker rather than inventing a compromise.

4. **Compile**
   - Compile deterministically: the same resolved input must yield the same semantic commitments, order, and execution-protection choices. Wording may vary.
   - Render in this fixed order: desired change → current facts and bounded uncertainty → protected boundary → work to complete now → completion or blocker. These are semantic slots, not required headings.
   - Keep every slot distinct; do not merge slots. Never reorder or silently omit a material slot; give each fact one home and return one artifact without competing variants or intake analysis.
   - Write the result as minimum-sufficient, self-contained engineer-to-engineer prose. Keep decisions and real invariants, express intent instead of imitating examples, and reference rich artifacts instead of replaying them.
   - Keep the default artifact out of spec form: no phases, implementation sequence, ticket decomposition, command inventory, or full acceptance checklist.
   - For direct or autonomous work, read [execution-readiness.md](references/execution-readiness.md), select only protections whose absence could change completion behavior, and place each under the semantic slot it constrains rather than adding another section.
   - If the user requests a fresh-session handoff, save the concise contract as Markdown in the operating system's temporary directory—not the workspace—reference existing artifacts, redact sensitive context, add `Suggested skills`, and return the absolute path.

5. **Validate**
   - Confirm the artifact maps back to all five semantics in order, every material hint appears once, territory claims have evidence, and remaining uncertainty has bounded effect.
   - Return to Enrich only when a consumer would otherwise have to rediscover requirement meaning; downstream implementation investigation is allowed.
   - Remove any sentence or mechanism whose absence would not change intent, protected boundaries, evidence, or completion behavior.
   - Finish as `complete`, continue with the one useful question, or state the blocker. Do not emit the intake analysis.

## Output

In Artifact mode, return one concise Intent Contract or the requested carrier. For Chinese output, target roughly 100–200 characters and keep routine takes within 1,000 characters; exceed the budget only for material boundaries, evidence, or blockers. In Embedded mode, continue the caller's workflow after intake.

Apply typed authority: the current user statement owns intent; current repo, config, tests, and runtime evidence own territory. Preserve existing behavior and repo invariants unless the request changes them. Execution intent closes on an achieved result with evidence; exploration intent closes on a bounded decision or finding with remaining uncertainty explicit. Keep solution uncertainty open after requirement meaning is settled.
