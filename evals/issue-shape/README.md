# Issue Shape behavioral review

Eval-only. These cases protect Drafted Issue ownership, specialist routing, and the boundary between canonical Issue intent and downstream execution artifacts. They do not define tracker or MultiCA runtime semantics.

## What to judge

For each case, prefer a fresh session with the same model/tool profile. Judge the result against these invariants:

- the output remains useful without the original conversation, Northstar, or MultiCA;
- it preserves one canonical Drafted Issue instead of creating parallel intent/spec/plan artifacts;
- when the user explicitly asks to create / update an Issue and an authorized tracker action exists, it performs that action instead of stopping at a Markdown draft;
- `Draft` makes the intended change concrete when prose alone would drift, but does not become an implementation checklist;
- `Goal` is emitted only when it adds decision information;
- territory unknowns route to `$unknowns-first`, material Target ambiguity routes to `$intent-shape`, and long-term structure routes to `$architecture-evolution` only when earned;
- Northstar is optional and is used only for difficult intent / compile, not as a mandatory pre-stage;
- Issue body is current canonical intent; comments are history / evidence / correction; durable decisions fold back into the body;
- Issue granularity follows a cohesive engineering outcome, not one agent context window;
- implementation details and realized change belong to PR-side execution unless they reveal that the Issue intent itself is wrong.

A smoke run is enough to catch routing and contract regressions. Do not claim engineering-outcome uplift without controlled comparison on real tasks.

## Case 1 — Small direct issue, no Northstar

Prompt shape:

> Create an issue from this already-resolved change: invalid integer input in the known parser branch should return the existing specified error. The behavior and acceptance oracle are known.

Expected:

- produces a small Drafted Issue that can go directly to an executor;
- if an authorized tracker action is available, creates the real Issue and returns its reference rather than asking for another publish confirmation;
- does not call Northstar, Intent Shape, AE, or Unknowns First merely for process completeness;
- does not invent an abstract Goal when Problem + Draft + Acceptance are already sufficient;
- does not decompose files, patches, or tests into a Taskbook.

Failure: `Goal → Target → Taskbook → Issue` ceremony is introduced before the issue can exist, or an available authorized create action is replaced by a draft-only response.

## Case 2 — Concrete core-path Draft

Prompt shape:

> Turn the Hermes consolidation discussion into an issue. Current legacy/fs and Hermes paths coexist; the intended direction is one Hermes-owned execution path while preserving model-visible feature semantics.

Expected:

- Issue body contains a compact `Current → Target` Draft;
- ownership / removed path / semantic invariant are shown when material;
- no separate intent.md/spec.md/plan.md is created;
- if the target is already clear, `$intent-shape` is not invoked just because a Draft exists.

## Case 3 — Target ambiguity earns Intent Shape

Prompt shape:

> Create an issue for a request whose outcome is understood, but two materially different target core paths are still both consistent with the prose and differ in ownership.

Expected:

- recognizes that the Issue cannot safely freeze one Target yet;
- routes the one concrete decision to `$intent-shape`;
- consumes the resulting contrast / correction into the same Issue Draft or Decisions;
- does not require Northstar unless an additional difficult binding judgment remains.

## Case 4 — Territory unknown earns Unknowns First

Prompt shape:

> Shape a migration issue, but the current producer may be A or B and that fact changes who can own the target path.

Expected:

- does not draw a confident target based on an assumption;
- routes the decisive territory fact to `$unknowns-first`;
- folds verified Evidence back into the Issue;
- does not turn repository research into a generic mandatory Issue Shape phase.

## Case 5 — Long-term structure earns Architecture Evolution

Prompt shape:

> We know the product outcome, but the issue cannot state the target because the long-term responsibility may belong in module A or B and dependency direction changes with that choice.

Expected:

- recognizes a structural judgment rather than treating it as local Draft prose;
- routes to `$architecture-evolution` / its Architecture Shape specialist;
- folds only the durable structural decision needed by this Issue into Draft / Decisions;
- does not copy the architecture artifact wholesale into the Issue.

## Case 6 — Issue comments fold durable correction back

Prompt shape:

> The existing issue Draft says GitLab is polled by an activator before MultiCA takeover. A later comment records the accepted correction that GitLab webhook pushes activation instead. Update the issue.

Expected:

- updates the canonical Issue Draft / Decisions to the accepted webhook direction;
- preserves unrelated constraints and still-valid content;
- does not copy the full comment thread into the body;
- the old polling premise no longer appears as current intent.

## Case 7 — PR finding re-enters Issue only when intent changed

Prompt shape:

> During implementation, a PR review finds that the proposed listener ownership contradicts the Issue's intended lifecycle boundary. Record the next intent action.

Expected:

- treats this as Issue Evidence / correction because the intended shape is wrong;
- reopens only the affected Draft / Decision and updates the canonical Issue after the decision closes;
- ordinary implementation bugs would remain PR-local and would not churn the Issue.

## Case 8 — MultiCA is a consumer, not a dependency

Prompt shape:

> Produce the issue now. MultiCA may consume it later, but it is not installed yet.

Expected:

- produces the same independently useful Drafted Issue;
- does not add MultiCA-specific lifecycle, task state, session protocol, or context-window-sized decomposition;
- may preserve an execution-platform-neutral handoff requirement: the consumer must receive or deterministically fetch the full canonical Issue.

## Case 9 — Difficult intent can opt into Northstar

Prompt shape:

> The Issue has a useful Draft, but two binding interpretations imply materially different accepted outcomes and long-term commitments. Repo evidence cannot decide between them.

Expected:

- recognizes a difficult intent / Human-owned commitment problem;
- may route the Drafted Issue to `$northstar` for judgment / compile;
- Northstar enriches the same canonical intent rather than recreating a parallel Issue / spec;
- once the difficult choice is closed, execution may continue from the updated Issue.

## Review conclusion format

Record each case as `PASS`, `FAIL`, or `INCONCLUSIVE` with the smallest decisive excerpt / reason. Contract/routing smoke can justify merge safety for the skill semantics; it cannot prove that Drafted Issue improves real engineering outcomes without clean-session behavioral comparison on real work.
