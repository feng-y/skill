# Intent IR quality

Use this reference when Intent Take stability, authority, or compression is not obvious. This is a quality reference for Stage 1, not an execution workflow.

## Intent sufficiency

Stable Intent IR is sufficient when Execution Compile no longer needs to rediscover what the user means. Preserve only semantics that can change downstream judgment:

- the desired end state and explicit requested outcomes;
- the underlying problem or design intent when it guides choices beyond literal task wording;
- relevant territory reality, evidence state, and material uncertainty;
- Human-confirmed decisions, priorities, approvals, and hard boundaries;
- the observable result and trusted proof obligations that define success;
- any requested delivery shape that materially constrains the result.

Do not preserve broad background, superseded discussion, rejected alternatives, or implementation detail merely because they appeared in conversation. Preserve rationale when losing it would make a later executor choose a locally valid but directionally wrong solution.

## Authority and territory

The current user owns intent. Current authoritative evidence owns territory.

Explicit requested outcomes are authoritative until the user supersedes them. Grounding may add prerequisites, widen necessary implementation or verification scope inside settled boundaries, expose higher cost, or prove infeasibility; it must not silently weaken, defer, split out, or replace an explicit requested outcome.

Territory facts may change with better evidence without rewriting user-owned intent. Recommendations, inferences, defaults, and unknowns remain distinguishable from confirmed decisions and verified facts. Repeated rewriting on unchanged information may improve expression or consistency but creates no new authority.

When evidence conflicts with an explicit outcome, investigate enough to determine whether the outcome can still be preserved by adding prerequisites, widening necessary scope inside settled authority, or strengthening proof. Ask only when preserving the outcome requires a material Human-owned change in outcome, accepted behavior, scope or priority, approval, or protected proof rule. If evidence proves infeasibility and no meaningful Human choice remains, return the blocker rather than a false decision.

## Why / design intent

Goal and rationale have different roles:

- **Goal** defines what should be true when the work succeeds.
- **Why / design intent** explains the underlying problem or desired structural direction that should guide judgment when several unforeseen paths satisfy the literal Goal.

Carry only decision-relevant rationale. A useful test is: if a capable executor encounters an unplanned but valid branch, would this rationale change which path best preserves the user's intent? If yes, keep it. If not, drop it as conversation history.

## Unknowns

Do not ask merely because territory is incomplete. Separate:

- **territory unknowns** that repo investigation, measurement, or later execution can settle;
- **executor-owned How** that can remain open without changing the intent;
- **Human-owned intent gaps** whose resolution changes the requested outcome, accepted behavior, scope or priority, approval, or protected proof rule.

Only the last category blocks Intent Take convergence. A wider necessary implementation surface or stronger verification obligation does not create a new Human decision when it remains inside settled boundaries.

## Stable Intent IR

Stable Intent IR is an internal compiler boundary, not necessarily the final user-facing artifact. It should make these roles recoverable without forcing a fixed serialized schema:

- Purpose / Why
- Goal and explicit requested outcomes
- grounded Context / State relevant to meaning
- Human Decisions
- Constraints / Boundaries
- Success and proof semantics
- requested Output semantics when material

Execution Compile consumes these semantics and may reorganize, compress, or lower them into a different executable representation. It must preserve authority and meaning, but it should not copy the Intent IR verbatim and append execution sections.

## Unresolved output

When Intent Take is not stable, return the smallest useful continuation surface rather than a padded executable artifact. Preserve the current best intent so the next turn does not have to reconstruct settled meaning, then expose only what blocks convergence, for example:

- **Current Intent** — the settled Goal, important Why, and boundaries so far;
- **Open Decision / Probe / Blocker** — the one material gap preventing stable compilation;
- **Why it matters** — what user-owned semantic would change;
- **Options** — only when a Human choice is actually needed, with materially distinct alternatives and a concise recommendation.

A later invocation should use still-valid settled semantics as its baseline. New user authority may change intent; new authoritative evidence may improve grounding. Rewriting alone cannot promote uncertainty into settled intent.

## Stability invariants

Across compression, later alignment turns, and Execution Compile:

- Goal and explicit requested outcomes change only with new user authority;
- confirmed Decisions and user-owned Constraints retain their authority until superseded;
- territory facts follow current authoritative evidence;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- proof gaps never become completion claims through rewriting;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment remains downstream unless it changes a user-owned semantic;
- target state, current evidence state, and accepted completion remain distinguishable.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md). When Stable Intent IR is ready to lower, apply [execution-compile.md](execution-compile.md).