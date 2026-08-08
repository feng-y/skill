# Stable Intent

Read this only when it is unclear whether the request already contains one executable Goal.

## Problem space is not a Goal

Concerns, hypotheses, comparisons, mixed questions, conflicting outcomes, and broad verbs such as improve, simplify, optimize, clean up, or modernize usually describe a problem space. Ground enough evidence to reveal the real choice; do not turn a plausible model recommendation into Human authority.

Separate **outcome** from **means**. A named architecture, tool, migration, or implementation may be only the Human's current hypothesis. Treat it as required only when the Human explicitly makes it part of the Goal or a confirmed boundary.

## Authority

Keep distinct:

- **Human** — owns Goal, acceptable result/behavior, explicit priorities, explicit verification requirements, approvals, and confirmed boundaries;
- **reality** — evidence that may revise facts, feasibility, implementation work, and Verification needs;
- **inference** — model interpretation, recommendation, or default;
- **Unknown** — an unsettled consequence.

Evidence may prove a proposed route wrong; it cannot silently rewrite the Goal. Explicit Human verification requirements remain binding, but they belong to Verification authority rather than Goal semantics.

Implementation How may remain unresolved after Stable Intent; the Executor owns it unless it would change Goal, confirmed boundaries, Human verification authority, priority, or authorization.

## Minimal context and Unknown

Intent Take loads only the context needed to distinguish the Goal correctly: latest still-valid Human intent, evidence that can change the choice, confirmed boundaries, and any explicit Human verification requirement that must be preserved for Verification. Do not load broader history merely to make context feel complete; stop when the decision boundary is clear.

Unknown evidence reduction, consequence routing, and delegated defaults are defined once in [SKILL.md](../SKILL.md). This file only owns authority and Goal-closure semantics.

## Closure

Stable Intent requires one coherent Human-owned Goal and Why, the declared end state, must-preserve conditions, confirmed boundaries, material reality, relevant priorities, and delivery. Explicit Human verification requirements do not define the Goal but must be preserved before execution as binding Verification input.

If materially different Goals remain plausible, emit `Status: Unresolved Intent` with the current understanding, the consequences of the fork, a recommendation when useful, and the smallest Human decision or evidence probe. Do not emit executable work.
