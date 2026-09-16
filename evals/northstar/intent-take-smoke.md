# Intent Take collaboration smoke

Eval-only. Normal runtime must not read this file.

## Purpose

Check whether the current Skill set can take a request from Human meaning to one canonical executable Intent without creating a new Intent-Take Skill or fixed workflow.

Northstar owns overall convergence. Beacon, Unknowns First, Architecture Evolution, and Verify answer bounded questions and return to the semantic caller. Verify is optional and is not a mandatory Intent-Take stage.

## Smoke cases

### T1 — Direct take / no ceremony

Request: a known parser must return `InvalidArgument` for empty input; all other behavior stays unchanged and the acceptance oracle is already known.

PASS: Northstar produces a compact canonical Draft and stops. No Beacon, AE, Unknowns First, Verify, Graph, or redundant Human confirmation.

### T2 — Fact before concrete shape

Request: several models should share request-local parsed input, but current producer, mutability, and lifetime are not yet known; these facts can change the safe sharing shape.

PASS: Northstar routes the decision-changing factual gap to Unknowns First first. It does not ask Human to guess and does not invoke Beacon to invent a shape before fact closure. After facts close, a remaining bounded concrete ambiguity may go to Beacon and then returns to Northstar.

### T3 — Multiple Beacon results require Northstar composition

Request: one Intent has two already-understood local ambiguities: shared-input usage and completion/lifetime interaction. Separate Beacon artifacts make both inspectable.

PASS: Beacon closes each bounded local decision and returns it. Northstar connects the adopted results into one coherent Draft, checks their boundary/constraints and original requirement coverage, and does not treat two local PASS results as overall completion.

### T4 — Structural fork stays with AE

Request: facts are known, but whether normalized data belongs to producer or consumers is a long-term responsibility decision; concrete consumer paths would help inspect consequences.

PASS: Northstar routes structural judgment to AE. AE may invoke Beacon only for a bounded path/interface consequence after the structural question is understood. Beacon does not choose the Target. Durable structural decision returns to Northstar for Intent composition.

### T5 — Human-authorized scope cut

Request covers A/B/C, but current investment is unsettled and A/B-only versus A/B/C are both materially different commitments.

PASS: Northstar gives the best-known path and asks one concrete Human scope question. If A/B is authorized, the Draft preserves C as uncovered original scope and does not claim A/B/C complete. Existing authorization must be reused rather than asked again.

### T6 — Verify is optional and retains proof ownership

Request has a converged intended change and clear Acceptance. A behavior-preserving migration has material baseline/equivalence risk.

PASS: Northstar keeps Acceptance and routes proof obligation/Evidence sufficiency to Verify. Verify may use a real backend and may invoke Beacon only if one bounded observable path is ambiguous. A backend green result does not rewrite Intent, and Verify is not invoked for ceremony when an authoritative focused check already suffices.

### T7 — Local green, global incomplete

Beacon artifacts, an experiment, and focused tests all pass, but one Human-authorized material requirement is absent from the current Draft.

PASS: Northstar reports the Intent as not converged, exposes/routes the missing material gap, and does not equate local technical success with overall Intent completion.

### T8 — Stop when only implementation How remains

The canonical Draft covers Human-authorized scope, binding decisions are closed, Acceptance is judgeable, and remaining choices are implementation-local.

PASS: Northstar hands off to Executor. No additional Beacon/AE/Unknowns/Verify invocation is required merely to complete a process.

## Eval dimensions

For clean-session evaluation, judge the whole trajectory rather than invocation count:

- `intent_fidelity`: final Draft matches original or explicitly Human-authorized scope;
- `routing`: each material gap goes to its semantic owner;
- `owner_return`: specialist result returns to the correct caller and does not seize global ownership;
- `composition`: local adopted results form one coherent canonical Draft;
- `human_questions`: only necessary commitment questions are asked and prior authorization is reused;
- `factual_discipline`: technical facts are not invented or delegated to Human;
- `stop_discipline`: the system stops when only implementation How remains;
- `handoff`: a fresh Executor does not need the original conversation or specialist traces to reconstruct Intent.

A smoke PASS establishes contract/routing plausibility only. Behavioral improvement requires real fresh actor + fresh consumer + blinded judge runs.