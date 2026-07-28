---
name: prompt-atlas
description: Clarify a user's ambiguous intent through lightweight intake and produce a concise, consumer-ready Intent Contract covering goal, current context, boundary, immediate task, and success or stop conditions. Use when the user has a loose idea, incomplete requirement, ongoing engineering context, or existing prompt that should be directly executable or consumable by a spec, issue, or execution workflow. Stop before choosing a solution, writing a spec, planning implementation, or executing the work.
---

# Prompt Atlas

Perform intent intake. Recover what the user is actually trying to change, why the need exists now, what is already true, which boundary matters, what work should happen now, and what outcome or blocker closes the request.

The result is a consumer-ready Intent Contract expressed through Goal, Current Context, Boundary, Immediate Task, and Success / Stop Condition. These five foundations are the minimum completeness contract for intent intake, even when the final prose does not expose them as headings. They describe the requested work, not Prompt Atlas's own intake loop. The contract may be consumed directly to complete the request or transformed by a known workflow into a spec, issues, or execution loop; do not make it depend on an unspecified later stage. Use `unknowns-first` and other relevant context-discovery capabilities to supplement inspectable facts instead of making the user supply everything.

Prompt Atlas is the semantic core of Intent Take. Its primary completion criterion is finished requirement understanding, not a particular container. Default to a consumer-neutral contract; when the user explicitly requests a goal brief or another carrier, render the same completed intent into that carrier without letting the carrier's mechanics replace or postpone intent completion. Prompt Atlas retains the execution-quality capabilities needed by those consumers—verified baselines, scope controls, evidence, continuity, blockers, and incentive-safe evaluation—behind conditional profiles instead of forcing one heavy template onto every request.

## Intent Take Loop

Run five stages. Move backward only to close the first direction-changing gap; do not restart the whole intake.

1. **Capture**
   - Read the latest request, relevant conversation, current artifact, actual work state, and scattered hints across turns. Preserve quoted source text.
   - Treat corrections as overrides, examples as direction unless made mandatory, rejections as boundary evidence, and repeated compatible hints as stronger intent evidence.
   - Separate the desired result, a suggested means, and a hard constraint. Preserve the result as intent; keep the means as a hypothesis unless the user makes it mandatory; require a user decision or territory evidence before treating a constraint as law.
   - Use conversation history, project context, and available memory as intent evidence, not as proof of current repo or runtime state. On ChatGPT surfaces with relevant Memory context already available, apply [references/chatgpt-memory.md](references/chatgpt-memory.md).
   - Exit only after every source hint is represented as intent, context, boundary, or a typed unknown, and all five foundations have a draft.

2. **Enrich**
   - Classify the first material gap by its proper closer: user-held intent, inspectable territory, or relevant domain capability.
   - For engineering territory, use `unknowns-first` as the default supplement: run L1 silently, take one focused L2 move at a time, and use L3 only when the user asks for a full map or coupled unknowns block the contract.
   - Use another relevant skill or tool when it can supply required domain context.
   - Close each inspectable unknown that could change a foundation by following the smallest sufficient evidence chain through code, config, tests, runtime, traces, target ref, or another authoritative source. Finding a likely file or writing “verify whether” is not closure.
   - For migrations, refactors, shared-boundary changes, and behavior-preserving work, run one `unknowns-first` blindspot pass before exit. Account for the touched responsibility surface—producer, representation or accessor, current owners, active consumers, production bindings, target-ref state, and proportional proof—or mark an element as evidenced out of scope.
   - Fold the supported conclusion—not the search transcript—into the applicable foundation. Keep design and implementation choices open after the requirement's meaning is settled.
   - When required evidence is unavailable, decide whether a bounded conditional still leaves the work unambiguous; otherwise record the exact evidence blocker instead of delegating unfinished intent discovery to the consumer.
   - Exit only when every discoverable foundation-changing unknown and every in-scope blindspot surface has a supported conclusion, and a consumer will not need to repeat context discovery to understand the requirement.

3. **Resolve**
   - Ask one concise human question only when the answer belongs to the user and would change Goal, Boundary, Immediate Task, or Success / Stop.
   - Fold the answer into the draft, then return only to the affected Capture or Enrich step.
   - If a human-held contradiction cannot be resolved, preserve one explicit blocker rather than inventing a compromise.
   - Exit when no user-held direction-changing ambiguity remains.

4. **Compile**
   - Produce one self-contained, consumer-ready Intent Contract in short, natural engineer-to-engineer prose. Do not expose the five labels unless requested.
   - Make it minimum-sufficient: keep a sentence only when it changes a foundation, preserves necessary evidence, or materially improves the consumer's completion quality. Point to rich sources instead of replaying their contents.
   - Keep the default artifact out of spec form: express the work in a few connected sentences, not phases, ordered implementation steps, command lists, or acceptance checklists. Render detailed execution machinery only for an explicitly selected carrier that needs it.
   - Treat the carrier as presentation: use the user's requested carrier, otherwise keep the contract route-neutral. A direct executor or an explicit spec / issue / execution workflow must be able to consume the same semantics without reconstructing intent.
   - Refuse premature solutioning: do not select architecture, prescribe implementation, define a full acceptance model, or decompose tickets.
   - Apply [references/context-engineering.md](references/context-engineering.md) as an internal compression filter.
   - If the result may be consumed directly for execution, apply the applicable [execution-quality profile](references/conditional-execution-hints.md). Keep portable quality semantics in a route-neutral contract; add carrier-specific mechanics only when that consumer is selected.
   - If the user asks a fresh agent or session to continue, or asks to save the result outside the workspace, apply the [temporary Intent Take carrier](references/temporary-handoff.md).

5. **Validate**
   - Confirm that Goal, Current Context, Boundary, Immediate Task, and Success / Stop describe the requested work rather than Prompt Atlas's own process.
   - If the next agent must repeat repo or domain investigation to learn what the requirement means, return to Enrich. Investigation that only chooses how to implement the settled requirement may remain downstream.
   - Run the subtraction test: remove every sentence and execution mechanism whose absence would not change requirement understanding, protected boundaries, evidence, or completion behavior. Return to Compile when a routine brief exceeds the output budget or reads like a specification.
   - Confirm that every material territory claim is supported, every remaining unknown has a bounded effect, and the artifact is accurate, self-contained, and finished in the requested form.
   - When the target repo owns a verification policy or another rich completion specification, confirm that Success / Stop carries the complete applicable gate set and evidence-state semantics; one omitted required gate keeps the take incomplete.
   - `complete`: return the artifact.
   - `continue`: return to Enrich or Resolve for the first missing direction-changing fact; expose only the one useful question when user input is required.
   - `blocked`: state the contradiction or missing human decision that prevents a valid contract and stop.

For ambiguous, high-stakes, multi-stage, or agentic work, read [references/foundation.md](references/foundation.md).

## Output

While intent is unclear, ask only the next intent-changing question. Optionally precede it with one sentence confirming the current understanding; do not emit an analysis report.

When all five foundations are sufficiently clear, finish the current request with one concise intent brief or directly usable prompt, according to what the user asked for. If a missing foundation could change direction, continue intake instead. If a human-held contradiction makes completion impossible here, state that blocker and the one decision needed. Do not append a proposed solution, spec, plan, or implementation checklist.

Intent Take is naturally short because it completes requirement understanding while leaving specification, solution, decomposition, and execution detail outside its boundary. For Chinese output, target roughly 100–200 characters by default and keep routine Intent Takes within 1,000 characters; use equivalent brevity in other languages. This is a compression budget, not permission to omit a material foundation, boundary, or blocker.

Only when the user explicitly asks to learn from or compare revisions, show a brief diagnosis and the clarified intent. Never provide several competing final artifacts unless requested.

## Quality bar

- Optimize for user-agent alignment, not textual polish or apparent completeness.
- Lead with the intended change and current reality, not a prescribed task list.
- Apply typed authority: the user's current correction wins for intent; current repo, config, tests, and runtime evidence win for territory. Do not let remembered context overwrite either.
- Include only context that changes the meaning or boundary of the request.
- State what must remain invariant and what differences are acceptable.
- Make the Immediate Task the concrete work the Intent Contract asks its consumer to complete now, not Prompt Atlas's formatting activity, an undefined later stage, or a hidden implementation plan.
- Match completion semantics to the work: execution intent closes on an achieved result with evidence; exploration intent closes on a bounded decision or finding with remaining uncertainty made explicit. Do not force fake metrics onto work whose value requires judgment.
- Use `always`, `never`, `must`, and `only` only for genuine invariants.
- Preserve uncertainty that belongs to solution choice or implementation. Close inspectable uncertainty that changes requirement meaning; keep an unresolved item only when its effect is bounded or its unavailable evidence is the explicit blocker.

## Source boundary

This skill distills [feng-y/prompt-atlas](https://github.com/feng-y/prompt-atlas) at revision `5e9dd8f197827ec83be81790644db1f9667c6d65`. Treat its principles as a review method, not universal facts. Preserve source claims, synthesis, inference, and unverified candidates as distinct evidence classes.
