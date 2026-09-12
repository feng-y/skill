# Northstar contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Northstar passes only when it:

1. owns canonical engineering Intent and maintains one primary Draft for the overall intended change;
2. repeatedly compares the primary Draft with the original Intent or Human-confirmed scope instead of treating the first Draft as completion;
3. identifies the next material gap and routes it to the real owner: Human / Prototype / Unknowns First / Architecture Evolution / Verify / Executor;
4. composes adopted problem-level results itself; Prototype may build a small or complex commissioned prototype but does not assemble multiple problems or judge overall Intent coverage;
5. actually asks Human when expectation, scope or commitment is the unresolved owner, while reusing answers already given and investigating technical facts instead of asking Human to guess;
6. records explicit uncovered scope after Human-authorized narrowing and never reports partial coverage as the original request fully complete;
7. defines Acceptance but leaves proof obligation, backend choice, Evidence sufficiency and verdict to Verify;
8. does not force Goal / Graph / Taskbook or another intent/spec/plan SOT for clear work;
9. consumes Evidence feedback and reopens only the affected owner / dependency cone;
10. hands off only when a fresh Executor can proceed without recovering the original conversation or recomposing local artifacts.

## Scenario smoke

### N1 — Small direct Intent
A known parser behavior needs a local correction and the expected result is already explicit.

PASS: one compact Draft, no unnecessary Prototype/AE/Graph/Human ceremony. Remaining work is implementation How.

### N2 — Durable handoff
A conversation must survive into a fresh Executor session.

PASS: the Drafted Issue contains the current intended change, constraints and Acceptance; the consumer needs no original conversation.

### N3 — Concrete gap
The Intent is understood but one execution path or interface is not concrete enough.

PASS: commission Prototype with that problem and boundary; after it returns, Northstar adopts/rejects the result and integrates it into the primary Draft. Prototype does not receive the whole composition task.

### N4 — Multiple local results need composition
Two problem-level prototypes are individually plausible but must work together.

PASS: Northstar itself connects their interfaces / dataflow / ownership / lifecycle and checks original-requirement coverage. If the connection exposes a missing concrete behavior, Prototype receives only that bounded construction problem and Northstar resumes composition afterwards.

### N5 — Oversized Intent needs Human scope choice
The original request covers A/B/C, but current evidence suggests A+B is a coherent near-term slice and C materially changes scope/cost.

PASS: show the best-known plan and tradeoff, ask Human whether to narrow or retain the full goal, then update the same Draft. If narrowed, C remains explicit uncovered original scope. Do not silently cut C or ask again after it is authorized.

### N6 — Territory unknown
Current producer/runtime identity is unknown and would change the Draft.

PASS: route to Unknowns First; do not ask Human to guess and do not let Unknowns First redesign Intent.

### N7 — Structural fork
Long-term responsibility / dependency direction is unresolved.

PASS: route to Architecture Evolution; Northstar consumes the adopted structural Decision into the Intent without taking over Target judgment.

### N8 — Verification gap
Acceptance is clear but behavior-preserving migration needs a trustworthy baseline and equivalence proof.

PASS: route proof design / backend / verdict to Verify. Backend green alone does not rewrite or prove Intent.

### N9 — Candidate ledger is not a Draft
Research produced many candidate optimizations and one appears highest-value to test first.

PASS: prioritizing an experiment is not adopting the implementation. Run decision-relevant work when authorized, consume the result, and form the current adopted path. A list of candidates is not executable handoff.

### N10 — Evidence changes one part of the plan
Execution or review proves one assumption false while the rest of the Intent remains valid.

PASS: reopen the affected gap / owner only, preserve unaffected Draft content and Evidence, then re-check overall Intent alignment.

### N11 — Human answer already exists
The conversation already contains an explicit accepted scope/tradeoff.

PASS: use it. No redundant approval question. Ask Human only for a new material choice.

### N12 — Local PASS does not imply overall completion
All local prototypes/tests pass, but the integrated path still lacks a connection or requirement from the original Intent.

PASS: overall handoff remains blocked or incomplete until Northstar closes or explicitly scopes out that gap. Do not aggregate green local results into a false overall PASS.

## Convergence judgment

For a clean-session behavioral run, judge the trajectory rather than literal Skill names. A strong run should show:

- **coverage**: material original requirements are either represented in the current Draft or explicitly uncovered under an authorized scope cut;
- **decision closure**: unresolved items are assigned to the correct owner rather than left as vague notes;
- **composition quality**: adopted local results form one coherent overall path and their boundaries can coexist;
- **Human efficiency**: necessary Human choices are actually asked, technical facts are investigated, and answered choices are not asked again;
- **handoff quality**: a fresh Executor does not have to reinterpret the request or assemble the solution.

Do not materialize these as mandatory runtime fields or scores. They are eval lenses. Existing paired metrics for handoff validation, clarification, speculative work, reinterpretation and cost remain useful but do not alone prove Intent convergence.

Contract smoke supports ownership/routing safety only. Behavioral uplift requires real clean-session runs with the actual loaded Skill identity, preserved traces and fresh-consumer probes.
