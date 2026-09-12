# Intent convergence control — PR #95 plan

Development/eval-only. Runtime truth lives in the Skills. Continuation base for this revision: `f2e2e2bafd9a6596b29c227742337b7100d0e68d`.

## Target

Align the Intent capability with the useful division seen in Matt-style wayfinding and pstack-style control without importing their persistent ticket maps or playbook taxonomy:

- **Northstar** owns the canonical engineering Intent and the convergence control around it.
- **Prototype** remains one reusable construction tool for a commissioned problem, small or complex; composition stays in the caller.
- **Unknowns First / Architecture Evolution / Verify** keep factual / structural / proof ownership.
- **Human** owns requirement meaning, scope and commitment choices that cannot be inferred from technical evidence.

The control objective is not “call every Skill” or “generate a Draft”. It is to reduce the material mismatch between the original Intent (or Human-confirmed scope) and the current primary Draft until a fresh Executor can continue without reconstructing the high-level decision.

## Runtime change

Northstar becomes an explicit dynamic loop:

`Recover → Compare gap → Route → Consume → Compose → Re-check`

This is reasoning guidance, not a persisted lifecycle or state machine. Clear work may collapse the loop into one pass. Complex work may revisit only the affected gap.

Gap routing remains small and stable:

- Human expectation / scope / commitment → Ask Human;
- territory fact → Unknowns First;
- concrete prototype / local draft / disposable experiment → Prototype;
- long-term structure → Architecture Evolution;
- proof → Verify;
- implementation How → Executor.

Northstar performs caller-side composition and overall Intent coverage checking. A missing concrete connection discovered during composition may be commissioned to Prototype, but the whole composition task does not move there.

## What is deliberately not added

- no new Intent-Control, Wayfinder or Orchestrator Skill;
- no durable gap object, decision-ticket schema or mandatory work map;
- no fixed stage ordering;
- no mandatory Human approval for already-authorized technical work;
- no prototype-count rule;
- no duplicated proof / architecture / factual judgment inside Northstar;
- no persistent execution-progress manager.

## Plan review 1 — ownership

Question: does “control” accidentally absorb specialist semantics?

Result: no. Northstar chooses why a gap must be closed and how returned results affect the overall Intent. The specialist still owns its judgment. Prototype remains pure construction; AE owns Target; Verify owns proof; Unknowns owns facts. External scheduling may decide when work runs but gains no semantic authority.

## Plan review 2 — counterexamples

- **Small direct fix:** one compact Draft, no specialist ceremony.
- **Two local prototypes:** Northstar connects them and checks overall coverage; Prototype does not compose them.
- **Large request:** Northstar proposes a scope cut or continued composition and asks Human only if the choice changes accepted scope/commitment.
- **Human already answered:** reuse the answer; no repeated interview.
- **Unknown producer / runtime behavior:** investigate territory rather than ask Human to guess.
- **Benchmark green but scope unclear:** technical PASS cannot replace Human acceptance.
- **All local checks green but integrated path incomplete:** overall Intent remains incomplete.
- **Only implementation How remains:** hand off; do not keep the convergence loop alive for ceremony.

Disposition: proceed with Northstar runtime + invocation metadata + focused contract eval only. Prototype and other runtime Skills require no semantic expansion for this change.

## Behavioral acceptance

Future clean-session eval should judge the trajectory, not literal Skill invocation names:

- material original requirements covered or explicitly scoped out with authority;
- unresolved decisions routed to the correct owner;
- returned problem-level results form a coherent integrated path;
- Human questions are necessary and non-redundant;
- fresh consumer does not reinterpret or recombine the solution.

These are eval lenses, not mandatory runtime fields. Existing paired cost / clarification / handoff metrics remain complementary.
