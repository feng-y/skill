# Stable Intent IR

Use this reference when Goal closure, authority, or the Human boundary is unclear. Stable Intent is source semantics for Execution Compile, not the first half of the taskbook.

## Preserve

Keep only what can change downstream judgment:

- requested end state and underlying problem;
- decision-relevant Why or design intent;
- Human-confirmed decisions, priorities, approvals, and boundaries;
- material facts with provenance and evidence state;
- task scope when it differs from the broader Goal;
- trusted success and delivery semantics.

Discard conversation history, rejected reasoning, and implementation detail unless they still affect one of those items.

## Authority

Keep four classes distinct:

- **Human intent** — requested result, accepted behavior, confirmed decisions, and boundaries;
- **territory reality** — code, tests, schemas, traces, artifacts, and measurements;
- **inference** — model judgment or recommendation;
- **unknown** — not yet settled.

Better evidence may change facts, feasibility, necessary implementation work, and proof obligations. Only new Human authority may change intent or confirmed boundaries.

A design direction is Human-owned only when the Human made it part of the result. Routine architecture remains implementation How when it preserves that meaning.

## Ask Human

Ask only when proceeding would:

1. change the requested result;
2. cross or relax a confirmed boundary or require high-risk authorization;
3. choose between materially different Goals that accessible evidence cannot resolve.

More work, wider implementation scope, decomposition, architecture How, command order, or replanning do not by themselves require Human input.

When a decision is required, expose the smallest real choice with consequences and a recommendation. Do not disguise inference as authority.

## Route unknowns

- evidence can settle it now → investigate;
- execution-only reality can settle it before modification → put it in Task 0;
- it affects only implementation How → let execution decide or experiment;
- one safe reversible choice preserves intent → use a visible delegated default with basis and rollback route;
- it reaches an Ask Human boundary → ask;
- evidence or capability is unavailable → park the affected branch if safe work remains, otherwise block truthfully.

## Stable boundary

Intent is stable when one coherent Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery semantics are clear, and no Ask Human condition remains.

Execution Compile may ground implementation territory and lower Stable Intent into Task 0, a graph, state, stop rules, and proof. It may not change intent or confirmed boundaries. The final taskbook contains only execution-relevant lowered semantics, not Stable Intent followed by an appendix.
