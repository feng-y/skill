---
name: prompt-atlas
description: Clarify a user's ambiguous intent through lightweight intake and produce a concise, human-written intent brief. Use when the user has a loose idea, incomplete requirement, ongoing engineering context, or existing prompt whose real goal/current context/boundary/immediate task/success or stop condition is not yet clear. Stop at shared intent; do not choose a solution, write a spec, plan implementation, or execute the work.
---

# Prompt Atlas

Perform intent intake. Recover what the user is actually trying to change, why the need exists now, what is already true, which boundary matters, what the next engagement should clarify or accomplish, and when the intent is clear enough to hand off.

The result is shared understanding expressed through Goal, Current Context, Boundary, Immediate Task, and Success / Stop Condition. It is not a solution, specification, implementation plan, ticket set, or completed task.

## Workflow

1. Take in the whole available intent surface: the user's latest request, relevant prior discussion, current artifact or prompt, target model, actual work state, and scattered hints across turns. Preserve quoted source text.
2. Accumulate hints as intent evidence. Notice concrete facts, preferences, examples, rejections, corrections, and repeated concerns. Connect compatible hints across turns, but do not promote every hint into a requirement:
   - a concrete correction overrides an earlier tentative interpretation;
   - an example reveals direction or taste unless the user makes it a rule;
   - a rejected direction clarifies the boundary;
   - repeated consistent hints strengthen the inferred intent;
   - conflicting material hints require the next human question.
3. Reconstruct the five foundations internally and identify the first ambiguity that separates materially different user intents. Separate:
   - user-held intent and tradeoffs;
   - facts the agent can discover from the repo or evidence;
   - assumptions that would materially change the goal, boundary, immediate task, or stopping point.
4. Close intent gaps one at a time. Discover inspectable facts directly; ask one concise, human question when the answer belongs to the user. Continue intake across turns until the remaining ambiguity can safely be left to later exploration.
5. When prompt, docs, memory, and repo reality may diverge, invoke `unknowns-first` if available:
   - use its L1 Target / Territory / Unknown / Proof gate silently by default;
   - use at most one focused L2 probe when it can materially improve Current Context;
   - enter L3 only when the user asks for a full map or coupled unknowns genuinely block intent clarification.
6. Feed only verified, intent-changing territory facts back into Current Context. Do not turn context discovery into solution design.
7. Refuse premature solutioning. Do not select architecture, prescribe implementation, define a full acceptance model, decompose tickets, or silently cross from clarification into design or execution.
8. When the intent is stable enough, express it as short, natural engineer-to-engineer prose. Leave solution space open and retain only the boundaries necessary to prevent drift.

For ambiguous, high-stakes, multi-stage, or agentic work, read [references/foundation.md](references/foundation.md).

## Output

While intent is unclear, ask only the next intent-changing question. Optionally precede it with one sentence confirming the current understanding; do not emit an analysis report.

When intent is sufficiently clear, return one concise intent brief or directly sendable prompt. Do not append a proposed solution, spec, plan, or implementation checklist.

Only when the user explicitly asks to learn from or compare revisions, show a brief diagnosis and the clarified intent. Never provide several competing final artifacts unless requested.

## Quality bar

- Optimize for user-agent alignment, not textual polish or apparent completeness.
- Lead with the intended change and current reality, not a prescribed task list.
- Recover intent from the whole conversation; do not treat the latest sentence as the entire requirement when prior context changes it.
- Preserve the signal in fragmented hints without turning examples or passing reactions into hard requirements.
- Use `unknowns-first` to improve factual context, not to replace intent intake or expand every request into an unknown map.
- Include only context that changes the meaning or boundary of the request.
- State what must remain invariant and what differences are acceptable.
- Make the Immediate Task the next requested engagement, not a hidden implementation plan.
- Define Success / Stop as “intent is sufficiently shared and bounded,” not as a future solution's full acceptance criteria.
- Use `always`, `never`, `must`, and `only` only for genuine invariants.
- Preserve uncertainty that belongs to later investigation; remove only ambiguity that would make the agent solve the wrong problem.

## Source boundary

This skill distills [feng-y/prompt-atlas](https://github.com/feng-y/prompt-atlas) at revision `5e9dd8f197827ec83be81790644db1f9667c6d65`. Treat its principles as a review method, not universal facts. Preserve source claims, synthesis, inference, and unverified candidates as distinct evidence classes.
