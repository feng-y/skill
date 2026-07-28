# Conditional execution hints

Use these hints only when the clarified intent is being handed to an agent for repo modification or another execution task. Select the ones that materially protect this request and blend them into natural prose. Do not append all four as boilerplate.

## Completion and scope

Use when the user expects the receiving agent to carry the request through implementation rather than stop at analysis, diagnosis, design, or review:

> Complete the request, keeping the modification scope aligned with the user's intent.

Do not use this wording to silently authorize external writes, rollout, deployment, or other actions outside the clarified boundary.

## Behavior and invariants

Use for refactors, migrations, fixes, cleanup, or other changes where behavior preservation is implied:

> Preserve existing behavior and repo invariants unless the task explicitly requires changing them.

Omit or narrow it when changing behavior is itself the intent. Name any known acceptable differences rather than forcing false equivalence.

## Evidence

Use when correctness must be established against a repo:

> Use the tests, checks, and other evidence available in the current repo to gain enough confidence that the change is correct.

Keep the evidence bar proportional to risk. Do not invent fixed commands before the receiving agent inspects the repo.

## Routine judgment and escalation

Use for agentic execution when the user wants routine decisions handled autonomously:

> Make routine execution decisions independently; stop for confirmation only when an ambiguity would materially change the implementation direction.

This does not waive approval for destructive, irreversible, production, financial, security, or externally consequential actions.

## Selection rule

- Pure intent clarification: include none.
- Research, diagnosis, or review: usually include only the relevant evidence and escalation meaning, rewritten for that work type.
- Repo implementation: commonly include scope, applicable invariants, evidence, and autonomy.
- Explicit behavior change: do not add a generic behavior-preservation rule; preserve only unaffected invariants.
