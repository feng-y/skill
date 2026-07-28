# Prompt Foundation

Use these five foundations as the minimum completeness contract and skeleton for intent intake. They are not the only source of context, optional fields, visible headings, or a form, and they do not constitute a solution or spec.

## Five foundations

1. **Goal** — State the real problem and the change or result the user ultimately wants.
2. **Current Context** — State the current status and only the facts, evidence, or uncertainty that will affect judgment.
3. **Boundary** — State what must not change, drift, expand, or cross without approval. Distinguish genuine invariants from acceptable differences.
4. **Immediate Task** — State the concrete work the Intent Contract asks its consumer to complete now, without prescribing the implementation path.
5. **Success / Stop Condition** — State the semantic outcome and proportional evidence that fulfill the requested work, when further scope expansion should stop, or which real contradiction, missing authority, or unavailable requirement makes completion impossible under the current contract.

Embed these five elements naturally. A good prompt normally reads as a few connected paragraphs, not as `Goal / Context / Boundary / Task / Done` fields.

These five foundations describe the work contract. Prompt Atlas has a separate internal completion test: do not finish intake while a missing foundation would leave the intent direction unresolved or force a consumer to reconstruct it. A foundation may remain concise or contain an explicit unknown only when that unknown's effect is bounded and resolving it is unnecessary to understand the requested work.

## Consumer profiles

Treat different output-oriented skills as consumer profiles of the same Intent Take:

- a direct executor may consume the contract as natural engineering prose;
- an autonomous-goal profile may render verified baselines, path boundaries, progress state, incentive-safe checks, and executable verification explicitly;
- a spec / issue / execution pipeline may progressively elaborate design and work breakdown.

Prompt Atlas preserves the common semantic contract and selects execution-quality protections proportionally; it does not impose one consumer's mechanics on every route. The carrier is secondary: if the user requests a goal brief, the completed Intent Take may be rendered as one, but the goal workflow cannot substitute a future investigation for requirement completion.

Treat [`leader`](https://github.com/KKKKhazix/khazix-skills/blob/main/leader/SKILL.md) as a coverage floor for agentic Intent Take. Prompt Atlas must retain its repo-first investigation, result-versus-means separation, explicit assumptions, execution-versus-exploration completion, measured baselines, scope controls, evidence, continuity, blocker, and incentive-safe evaluation capabilities. Prompt Atlas adds multi-turn hint synthesis, memory fold-back, typed authority, evidence closure, and consumer-neutral reuse. What remains specific to Leader is its fixed `/goal` delivery envelope and always-heavy autonomous preset, not the quality mechanisms themselves. Apply the relevant mechanisms through [the execution-quality profile](conditional-execution-hints.md).

The carrier never changes the underlying Goal, Current Context, Boundary, Immediate Task, or Success / Stop semantics. It only selects how much verified execution machinery to render around them.

Source: `guides/prompt-foundation-structure.md` and `principles/transferable-principles.md` in [Prompt Atlas](https://github.com/feng-y/prompt-atlas), revision `5e9dd8f197827ec83be81790644db1f9667c6d65`.
