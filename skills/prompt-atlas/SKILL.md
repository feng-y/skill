---
name: prompt-atlas
description: Intake a user's real intent and turn it into a concise, human-written, verifiable task contract. Use when the user has a loose idea, incomplete task description, ongoing engineering context, or existing prompt that needs its true goal/current context/boundary/immediate task/success or stop condition recovered before producing a directly sendable prompt for ChatGPT, Codex, Claude Code, or another strong model.
---

# Prompt Atlas

Perform intent intake before prompt drafting. Recover what the user is actually trying to change, why the task exists now, what is already true, which boundary matters, what this turn should accomplish, and what makes it safe to stop. Then express that intent as a compact contract covering Goal, Current Context, Boundary, Immediate Task, and Success / Stop Condition.

Write like an engineer briefing a capable colleague. Give the model the right problem space and leave judgment, exploration, and tool choice to it unless a fixed mechanism is genuinely required.

## Workflow

1. Take in the whole available intent surface: the user's latest request, relevant prior discussion, current artifact or prompt, target model, and actual work state. Preserve quoted source text.
2. Reconstruct the five foundations internally. Separate:
   - user-held intent and tradeoffs;
   - facts the agent can discover from the repo or evidence;
   - assumptions that would materially change the goal, boundary, or completion verdict.
3. Close only route-changing intent gaps. Discover inspectable facts directly; ask one concise question only when the answer belongs to the user and different answers would produce materially different contracts.
4. When prompt, docs, memory, and repo reality may diverge, invoke `unknowns-first` if available:
   - use its L1 Target / Territory / Unknown / Proof gate silently by default;
   - use at most one focused L2 probe when it can materially improve Current Context;
   - enter L3 only when the user asks for a full map or coupled unknowns genuinely block the contract.
5. Feed only verified, decision-changing territory facts back into Current Context. Preserve unresolved route-changing unknowns as a boundary or stop condition; do not dump the unknown analysis into the final prompt.
6. Once intent is stable enough, remove model-expanded reasoning, long checklists, framework names, repeated process instructions, unnecessary tool order, and fake invariants.
7. Add only context and boundaries that materially affect judgment. Avoid replacing the model's judgment with a prewritten execution script.
8. Produce natural, continuous Markdown at the density of a practical engineer-to-engineer brief. Do not expose the five foundations as headings unless a formal contract or downstream parser genuinely needs them.

For ambiguous, high-stakes, multi-stage, or agentic work, read [references/foundation.md](references/foundation.md).

## Output

If intent is sufficiently clear, return one directly sendable prompt with no prefatory diagnosis, rubric, or explanation. Do not append commentary after it.

If a human-held intent choice is still missing, ask only that question and do not manufacture a final prompt around an arbitrary assumption.

Only when the user explicitly asks to learn from or compare revisions, show a brief diagnosis, a minimal rewrite, and one final prompt. Never provide several competing final prompts unless requested.

## Quality bar

- Lead with the intended outcome and current reality, not a prescribed task list.
- Recover intent from the whole conversation; do not treat the latest sentence as the entire requirement when prior context changes it.
- Use `unknowns-first` to improve factual context, not to replace intent intake or expand every request into an unknown map.
- Include only context that changes judgment; let the model inspect the available repo evidence.
- State what must remain invariant and what differences are acceptable.
- Bound the current turn without expanding every possible check.
- Define completion and stopping in terms of the task's real verdict or observable evidence.
- Use `always`, `never`, `must`, and `only` only for genuine invariants.
- Prefer “what outcome and semantic boundary matter” over “run these fifteen checks.”
- Enumerate expected outputs only when the task genuinely benefits from a structured verdict.
- Keep the final prompt short enough that a strong model can still exercise judgment.

## Source boundary

This skill distills [feng-y/prompt-atlas](https://github.com/feng-y/prompt-atlas) at revision `5e9dd8f197827ec83be81790644db1f9667c6d65`. Treat its principles as a review method, not universal facts. Preserve source claims, synthesis, inference, and unverified candidates as distinct evidence classes.
