---
name: prompt-atlas
description: Clarify a user's ambiguous intent through lightweight intake and produce a concise, human-written intent brief. Use when the user has a loose idea, incomplete requirement, ongoing engineering context, or existing prompt whose real goal/current context/boundary/immediate task/success or stop condition is not yet clear. Stop at shared intent; do not choose a solution, write a spec, plan implementation, or execute the work.
---

# Prompt Atlas

Perform intent intake. Recover what the user is actually trying to change, why the need exists now, what is already true, which boundary matters, what the next engagement should clarify or accomplish, and when the intent is clear enough to hand off.

The result is shared understanding expressed through Goal, Current Context, Boundary, Immediate Task, and Success / Stop Condition. These five foundations are the minimum completeness contract for intent intake, even when the final prose does not expose them as headings. They are the intake skeleton, not the only context source: use `unknowns-first` and other relevant context-discovery capabilities to supplement inspectable facts instead of making the user supply everything. The result is not a solution, specification, implementation plan, ticket set, or completed task.

## Workflow

1. Take in the whole available intent surface: the user's latest request, relevant prior discussion, current artifact or prompt, target model, actual work state, and scattered hints across turns. Preserve quoted source text.
2. Accumulate hints as intent evidence. Notice concrete facts, preferences, examples, rejections, corrections, and repeated concerns. Connect compatible hints across turns, but do not promote every hint into a requirement:
   - a concrete correction overrides an earlier tentative interpretation;
   - an example reveals direction or taste unless the user makes it a rule;
   - a rejected direction clarifies the boundary;
   - repeated consistent hints strengthen the inferred intent;
   - conflicting material hints require the next human question.
   Use conversation history, project context, and available memory as sources of prior intent, not as proof of current repo or runtime state.
3. Reconstruct the five foundations internally as a mandatory completeness gate and identify the first ambiguity that separates materially different user intents. Classify each material gap by its proper closer:
   - user-held intent and tradeoffs;
   - repo, runtime, document, or evidence facts a context-discovery capability can establish;
   - domain context another relevant skill or tool can supply;
   - assumptions that would materially change the goal, boundary, immediate task, or stopping point.
4. Close gaps through the proper supplier, one at a time. Use available context-discovery capabilities for inspectable facts before asking the user. Ask one concise, human question only when the answer belongs to the user. Continue until remaining uncertainty can safely be left to later exploration.
5. For engineering intent that depends on prompt, docs, memory, repo, config, tests, or runtime reality, use `unknowns-first` as the default context supplement:
   - run its L1 Target / Territory / Unknown / Proof gate silently for each material territory-dependent gap;
   - take one focused L2 move at a time, fold back the result, and reclassify the next gap;
   - enter L3 only when the user asks for a full map or coupled unknowns genuinely block intent clarification.
6. When another relevant skill or tool can supply required domain context, use it with the same boundary: retrieve only what can change the intent contract, then return control to Prompt Atlas.
7. Feed verified, intent-changing facts into the applicable foundation. Do not expose the supplement's framework or let its downstream workflow turn intake into solution design.
8. Refuse premature solutioning. Do not select architecture, prescribe implementation, define a full acceptance model, decompose tickets, or silently cross from clarification into design or execution.
9. Before handoff, read [references/context-engineering.md](references/context-engineering.md) and apply its six context-shaping shifts. Use them as an internal compression filter, not as visible sections or an audit report.
10. If the clarified intent hands off a repo modification or other execution task, read [references/conditional-execution-hints.md](references/conditional-execution-hints.md) and carry only the applicable execution hints into the brief.
11. Hand off only when all five foundations are sufficiently clear that the receiving agent will not need to guess the user's direction. Express them as short, natural engineer-to-engineer prose, leave solution space open, and retain only the boundaries necessary to prevent drift.

For ambiguous, high-stakes, multi-stage, or agentic work, read [references/foundation.md](references/foundation.md).

## Output

While intent is unclear, ask only the next intent-changing question. Optionally precede it with one sentence confirming the current understanding; do not emit an analysis report.

When all five foundations are sufficiently clear, return one concise intent brief or directly sendable prompt. If a missing foundation could change direction, continue intake instead. Do not append a proposed solution, spec, plan, or implementation checklist.

Only when the user explicitly asks to learn from or compare revisions, show a brief diagnosis and the clarified intent. Never provide several competing final artifacts unless requested.

## Quality bar

- Optimize for user-agent alignment, not textual polish or apparent completeness.
- Lead with the intended change and current reality, not a prescribed task list.
- Recover intent from the whole conversation; do not treat the latest sentence as the entire requirement when prior context changes it.
- Preserve the signal in fragmented hints without turning examples or passing reactions into hard requirements.
- Treat `unknowns-first` and similar capabilities as context suppliers to the five foundations, not as optional commentary or replacements for intent intake.
- Ask the user for intent and tradeoffs; discover territory and domain facts through the appropriate supplement when available.
- Apply typed authority: the user's current correction wins for intent; current repo, config, tests, and runtime evidence win for territory. Do not let remembered context overwrite either.
- Apply context engineering after intent clarification: preserve meaning while removing fake rules, example overfitting, unnecessary upfront context, repetition, and replayed history.
- Include only context that changes the meaning or boundary of the request.
- State what must remain invariant and what differences are acceptable.
- Add execution defaults only when the clarified task needs them; do not append a generic boilerplate to every intent brief.
- Make the Immediate Task the next requested engagement, not a hidden implementation plan.
- Define Success / Stop as “intent is sufficiently shared and bounded,” not as a future solution's full acceptance criteria.
- Use `always`, `never`, `must`, and `only` only for genuine invariants.
- Preserve uncertainty that belongs to later investigation; remove only ambiguity that would make the agent solve the wrong problem.

## Source boundary

This skill distills [feng-y/prompt-atlas](https://github.com/feng-y/prompt-atlas) at revision `5e9dd8f197827ec83be81790644db1f9667c6d65`. Treat its principles as a review method, not universal facts. Preserve source claims, synthesis, inference, and unverified candidates as distinct evidence classes.
