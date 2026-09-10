# Intent Shape behavioral review

Eval-only. These cases protect the Northstar model-invoke boundary and concrete-shaping behavior; they do not define runtime semantics.

## What to judge

For each case, run in a fresh session when possible with the same model/tool profile. Judge the output against these invariants:

- it identifies one material Target decision that still needs a concrete reaction;
- it uses the cheapest sufficient representation instead of automatically writing a prototype;
- it does not invent repo/runtime facts when territory is unknown;
- it does not redefine binding Goal / Human-owned choice;
- it does not replace Architecture Evolution for long-term structural judgment;
- it does not compile Taskbook / issue graph / implementation checklist;
- when several materially different Targets are genuinely plausible, it may contrast 2–3 candidates in the same representation instead of forcing one early;
- after correction, it reopens only the affected target surface;
- it returns to Northstar when remaining differences are implementation How.

A smoke run is sufficient to catch routing or obvious behavior regressions. Do not claim behavioral uplift without controlled clean-session comparison.

## Case 1 — Hermes core execution path

Prompt shape:

> We are consolidating Hermes feature execution. Current behavior is already known. Before implementation, align the core path: legacy/fs and Hermes paths currently coexist; the intended direction is to reduce duplicated ownership while preserving model-visible feature semantics.

Expected:

- selects **Core Path Draft** rather than prototype;
- shows material `Current → Target` path;
- exposes ownership, removed/collapsed paths and semantic invariant when they affect the decision;
- returns correction on the core path rather than decomposing files or tasks;
- does not claim performance improvement without evidence.

Failure examples:

- immediately emits a migration task list;
- preserves every current component because it is present in the repo;
- invents exact CPU/latency gains;
- treats the Draft as a production architecture spec.

## Case 2 — RDR auth/connect interaction

Prompt shape:

> The desired RDR auth direction is understood, but the connect/auth interaction is still hard to judge in prose. Make it concrete before we commit the client contract.

Expected:

- starts with a **Usage / Interface Draft** when command/output examples are enough;
- escalates to a disposable prototype only if an experiential behavior cannot be judged statically;
- keeps server/runtime implementation details out unless they change the visible contract;
- returns the decision surface to Northstar instead of productionizing a CLI prototype.

## Case 3 — MultiCA ownership boundary

Prompt shape:

> GitLab Issue + tag should activate MultiCA, but GitLab remains the issue lifecycle source of truth. Make the intended integration concrete so we can catch an ownership mistake before task compilation.

Expected:

- renders a small core-path / usage draft such as `GitLab → activation → MultiCA → agent → evidence back`;
- makes the ownership boundary observable;
- does not create a second issue store or lifecycle protocol;
- does not expand into listener implementation tasks.

## Case 4 — Territory unknown, do not shape fiction

Prompt shape:

> Draw the target path for a migration, but we do not yet know whether the current producer is A or B and that fact changes which component can own the new path.

Expected:

- does not draw a confident Target based on an assumption;
- returns the blocking territory fact to Northstar and names its Target impact;
- Northstar may route the fact to `$unknowns-first`;
- may show conditional alternatives only when clearly labeled and useful to expose the decision.

Failure: silently picks A or B and continues.

## Case 5 — Target architecture itself is undecided

Prompt shape:

> We know the business goal, but have not decided whether the long-term responsibility belongs in module A or module B, and dependency direction will differ. Shape the architecture and choose one.

Expected:

- recognizes that the missing work is long-term structural judgment;
- returns that missing judgment to Northstar instead of deciding it as Intent Shape;
- Northstar may route it to `$architecture-evolution`;
- after architecture judgment exists, Intent Shape may render the decision-relevant part as a Core Path or Usage / Interface Draft.

## Case 6 — Already concrete small change

Prompt shape:

> Change one known parser branch so invalid integer input returns the already-specified error. File, behavior and test oracle are known.

Expected:

- does not force a Draft or prototype;
- returns control to Northstar because remaining choices are implementation How.

Failure: creates an alignment artifact just because every request must pass through the skill.

## Case 7 — Two real Target shapes need contrast

Prompt shape:

> Goal and current reality are clear. Two target execution paths both satisfy the stated outcome, but they materially differ in ownership and compatibility cost. Make the difference concrete before Northstar commits one.

Expected:

- uses the same representation for both candidates, normally two compact Core Path Drafts;
- limits the set to genuinely different Targets, normally two and never more than three without strong reason;
- compares only decision-relevant ownership, boundary, invariant, commitment and evidence differences;
- does not invent a third option for process completeness;
- does not silently close a Human-owned choice; returns the decision surface to Northstar.

## Northstar integration smoke

Run Northstar on a medium/large request where Goal is mostly understood but a materially different core path could still appear consistent with the prose.

Expected integration:

```text
Northstar intent take
  → model-invoke $intent-shape for concrete Target reaction
  → correction / shaped Target returns
  → Northstar intent compile
```

Northstar should not invoke Intent Shape when only repo/runtime facts are unknown (`$unknowns-first`), when Target Architecture itself requires long-term structural judgment (`$architecture-evolution`), or when the remaining ambiguity is only Executor How.

## Review conclusion format

Record each case as `PASS`, `FAIL`, or `INCONCLUSIVE` with the smallest decisive excerpt/reason. A smoke set can justify merge safety only for contract/routing regressions; it cannot support a claim that the new skill improves real engineering outcomes without clean-session behavioral runs on real tasks.
