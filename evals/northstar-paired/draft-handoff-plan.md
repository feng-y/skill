# Caller-owned composition — PR #95 plan

Development/eval-only; not a runtime instruction. Continuation base: `6b03114e938b69a7cfa46c762118d8d2252b56af`.

## Decision and authority

The user's current direction is explicit: composition belongs to Northstar or another caller/controller, **not Prototype**. This supersedes the prior PR candidate's permission for Prototype to accept delegated assembly. Prototype remains one reusable construction capability; a small or complex commissioned problem does not create another Skill or grant composition ownership.

## Intended change

Northstar retains the original Intent, asks Human about material ambiguity or scope changes, and performs selection, composition and integration of returned prototypes/drafts into the primary Draft. Another authorized caller can perform that work in its own scope; a scheduler does not thereby acquire Intent, Architecture or proof authority.

Prototype constructs or revises the prototype/draft for the commissioned problem and returns its boundaries, observations and unresolved points. It does not choose how a collection of problem-level artifacts becomes a whole, assemble that collection, orchestrate more Prototype calls, or decide when the original Intent is satisfied. Multiple components inside one commissioned artifact do not turn ordinary construction into cross-artifact composition. Small/complex refers to the task, not to a new mode or fixed size limit.

When caller-side composition exposes a specific missing behavior or interface, the caller can commission that concrete problem, then integrate its result itself. Forwarding the entire composition assignment to Prototype, even with a renamed prompt, is not this boundary. If the composition is already supported, do it directly; do not invoke Prototype ceremonially.

Preserve current Human clarification/confirmation, explicit runnable experiments, factual discipline, original-caller return, AE structural judgment and Verify proof judgment. No new Skill, artifact registry, taskbook schema, runtime controller or singleton-prototype restriction.

## Placement

- Northstar and Prototype `SKILL.md` plus their invocation metadata: remove delegated-composition routing and assign positive composition responsibility to the caller.
- README and CHANGELOG: publish the current boundary and explicitly retire the unreleased delegated-assembly interpretation.
- Prototype contract eval and the existing Human/composition supplement: grade caller-side assembly, bounded missing-piece requests and complex direct construction separately.
- This plan and the current validation record: replace superseded development summaries; older revisions remain in Git. Do not rewrite frozen D1–D11 prompts or scorer code to simulate behavioral progress.

AGENTS.md already separates semantic owners and control-plane authority. AE/Verify/Unknowns First, material-compile, RDR and the original paired scorer require no change for this correction.

## Plan review 1 — ownership (before runtime edits)

Implementer self-review, not an independent reviewer session.

Reject retaining “delegated composition” as an exception: it directly conflicts with the current direction. Assign both choosing the combination and performing the assembly to the caller. Do not move only final approval while leaving assembly inside Prototype. Keep construction of a multi-component commissioned artifact valid; do not regress to “one tiny decision”.

Disposition: approved for the bounded runtime and entrypoint edits.

## Plan review 2 — counterexamples (before runtime edits)

- Existing compatible local artifacts: caller composes; no extra Prototype call.
- Missing concrete interface during composition: caller defines the gap, Prototype solves it, caller resumes assembly.
- Complex direct prototype request: same construction capability; no synthetic Northstar stage or internal composition scheduler.
- Oversized/unapproved scope: Northstar presents a concrete narrowing/retention choice and asks Human; no silent reduction and no repetitive approval for already-authorized work.
- Fact/architecture/proof conflict: corresponding owner resolves it; do not ask Prototype to determine the whole solution.

Disposition: approved. These are design counterchecks, not observed model executions.

## Validation and completion

Review descriptions, defaults, body, README and eval together. Check YAML, whitespace, relative links and exact published blob identities. Exercise contract walkthroughs for caller composition versus prototype construction and Human scope handling. Do not add unit tests that merely match the new prose.

The Python scorers, test suite and frozen D1–D11 are unchanged; their historical 26-test result is not a result from this continuation. No authenticated agent runner is available in this session, so do not claim clean-session or blinded behavioral uplift. Deliver the implemented change on PR #95 with the review record and a merge opinion; do not merge without authorization.
