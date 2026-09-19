# Beacon contract eval

Eval-only. Normal runtime must not read this file. These are evaluation specifications, not completed actor runs.

Beacon passes only when it:

1. returns a minimal, repo-grounded core prototype for one bounded feature intent or fault; questions, options, and Evidence alone are not a substitute;
2. remains caller-neutral and primarily model-invoked, without a mandatory Human stage or a requirement to invent alternatives before building a useful prototype;
3. ties the core to real repository paths/types/callers and separates observed facts from proposed or unverified behavior;
4. uses the smallest sufficient form, including a static sketch when that is enough, rather than always writing executable or production code;
5. returns one cohesive primary prototype and leaves selection, comparison, complete-Intent composition, and semantic judgment to the caller;
6. preserves valid artifact state under local feedback, changing connected clauses/examples only when the correction makes them inconsistent;
7. keeps factual closure with Unknowns First, structural judgment with AE, and proof sufficiency with Verify; a fault prototype need not wait for every root-cause unknown to close.

## Scenario smoke

### B1 — Northstar caller: feature core
A bounded feature intent needs an inspectable interface and usage sketch in the current repo. Its meaning may already be clear; multiple alternatives are not a prerequisite.

PASS: read the relevant source and return one connected core prototype using actual repo types/call sites, marking proposed additions. Include the interface, representative input/output, and consequences of binding lifetime constraints needed to inspect it together. Northstar decides adoption and full-Intent composition.

FAIL: a generic demo disconnected from the repo, prose/questions with no prototype, invented alternatives, or a separate invocation per field/file.

### B2 — Architecture Evolution caller
AE supplies one candidate boundary and needs its concrete consumer path.

PASS: return one repo-grounded core prototype for that scope. AE owns comparison with other candidates and Target judgment; Beacon does not launch a design competition or adopt an owner itself.

### B3 — Verify caller
Verify has an accepted claim but needs a local behavior/fault expressed as a concrete usage path or minimal reproducer.

PASS: return the core prototype with observed behavior and unverified limits. Verify keeps proof obligation and verdict; neither the prototype nor its focused check automatically proves the product claim.

### B4 — Unknowns First caller versus factual probe
A factual investigation has enough known local behavior to request an inspectable core prototype. Other causes may remain unknown. In the paired case, only a focused fact query/probe is needed.

PASS: the first case may call Beacon and return its prototype to the original decision owner, preserving unknowns. The paired fact-only case stays with Unknowns First; a probe/repro is not automatically a Beacon invocation.

### B5 — Static versus runnable core
A repo-grounded interface/usage sketch is sufficient in one case. In the paired case, the requested behavior cannot be inspected without executing a small local reproduction.

PASS: use the sufficient static core without ceremonial tests in the first case. In the second, use the smallest feasible reproducer and record actual execution before claiming it runs/reproduces. Both deliver a core prototype; executable code is a form, not an obligatory extra stage.

### B6 — Already concrete bypass
The caller already has an adequate repo-grounded core in its code or description and only production implementation How remains. In the paired variant, no separate prototype file exists.

PASS: do not invoke Beacon or stop immediately in either variant. File absence alone does not justify another prototype; do not manufacture ambiguity or production scaffolding.

### B7 — Fault core before root-cause closure
A fault has a reported trigger/input and an implicated repo path; its root cause is not established. In a paired variant, the runtime needed to reproduce it is unavailable.

PASS: inspect that path and build the smallest fault core linking trigger, expected versus reported/observed behavior, and relevant calls; distinguish a fault report from an actual execution observation. Run the reproducer when feasible; otherwise return an inspectable failure sketch with unverified steps and the concrete reproduction blocker. Return to the caller without claiming a proven cause/fix or requiring a full incident investigation first.

FAIL: hypotheses/logs only with no fault core, a fabricated successful run, or a generic reproduction unrelated to the repo.

### B8 — One core, not an evidence-only answer
One representative repo-grounded prototype is sufficient for the scoped request; several variants could be imagined. Compare an artifact-backed completion with an answer that gives the same analysis and evidence but omits the prototype.

PASS: deliver the one core prototype and stop. The evidence-only answer fails even if its explanation is plausible. A source read or benchmark can support the core, not replace it; independent candidate selection/comparison stays with the caller.

### B9 — Artifact-anchored feedback
Beacon produced a disposable core prototype. Human/caller feedback corrects one exact element; the remaining state is valid and no runtime fact or long-term ownership decision changed.

PASS: revise that same prototype and only connected clauses/examples made inconsistent by the correction, preserve valid state, and return the delta with the reason for connected changes. A repeated-child correction may change its usage example, not the unrelated singular interface or general ownership policy. Desired meaning is Human intent/choice input, not proof of runtime behavior.

FAIL: restart the whole Intent, create a persistent annotation/review lifecycle, silently treat feedback as runtime Evidence, or absorb a change belonging to Northstar / AE / Verify.

## Evidence boundary

For a real run, pin repo revision, loaded Skill source, model/backend, and task; retain source reads, the actual prototype/output, execution observations when claimed, artifact delta, and the distinct caller return. Inspect the artifact and transcript, not declarations such as “I grounded this in the repo”. Organic routing tasks must not leak the expected Skill; direct Beacon tasks can isolate its output behavior but do not prove automatic routing.

Static contract checks do not measure behavioral uplift. Use `$eval` for repeatable clean-session/trace-backed measurement; keep evaluator instructions and negative controls outside the actor context. Existing controller/worker, readiness/authorization, and product Verify coverage are not rerun or claimed as evidence for this change.
