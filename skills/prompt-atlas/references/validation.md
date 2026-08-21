# Prompt Atlas Validation

Eval / review only. Normal runtime must not read this file. It tests whether Prompt Atlas remains **Intent take + Intent compile → executable Taskbook + independent outcome judgment**, not a planner, manager, or second runtime specification. Concrete scenarios expose failure properties; domain and object names should be replaceable.

## Static smoke

1. **Prompt Atlas identity**: the Human owns accepted outcome / Human-owned commitments; Prompt Atlas performs Intent take first, closes only ambiguity that can change the executable contract, then performs Intent compile to produce an executable Taskbook; the Executor owns implementation How. Prompt Atlas does not own architecture design, complete research, execution orchestration, a scheduler, or verifier implementation.
2. **Intent > means**: named architecture/tool/provider/file shape is replaceable means by default. Representation enters Goal/constraints only when Human/repo/upstream authority makes it binding.
3. **Bounded Research**: close only reality that can change Goal, Human choice, binding boundary, material-work judgment, completion obligation, or safe-start frontier. Only reality the current Taskbook judgment / binding rule truly depends on must have sufficient Evidence before handoff; Graph completeness is not a reason to expand Research.
4. **Human authority**: ordinary factual / implementation uncertainty does not escalate to the Human. Ask only for choices that change the Human-accepted Goal or materially change whether to proceed, investment, long-lived maintenance commitment, or risk posture.
5. **Executable Taskbook + Executor freedom**: Intent compile must produce enough contract for a fresh Executor to begin material work without redoing Human intent judgment, redefining material boundaries, or inventing completion proof, while keeping replaceable implementation choices outside the contract. Goal summaries, task lists, Research narration, and file/symbol/helper/patch plans cannot substitute for the executable contract.
6. **Material work + Graph structure**: semantic ownership remains `Goal → Execution → Verification → Evidence`; Intent compile defines the executable contract first, and the Graph structures only material work / real dependencies inside Execution. Taskbook prose order does not create dependencies; work without a real dependency is neither forced serial nor parallel, and cohesive work is not fragmented merely to expose parallelism.
7. **Execution / Verification separation**: Verification fixes completion claims / Evidence obligations rather than mirroring implementation work or Graph nodes. An authoritative fallback path is retained only when omission would materially increase under-verification; when stale, the Executor re-derives coverage.
8. **Progressive future**: when only part is safe now, do not shrink the Human's full Goal. Future work enters only when established execution Evidence makes it real.
9. **Handoff / correction**: a successful Taskbook is materialized as the same body to an authoritative file outside repo/workspace and carries only a thin completion handoff. A material Human correction recomputes only the affected intent / compile dependency cone and fully re-delivers.
10. **Independent outcome judgment**: when Executor outcome/candidate Evidence returns, judge context is built in the order `authoritative Taskbook → claim-relevant current reality → Executor report`; candidate Evidence cannot change reality / Graph before verification. Judge each material claim by distinguishing disproven from not-yet-proven, check necessary cheap/material counter-Evidence, then re-judge the whole Goal.
11. **Progressive disclosure**: read `intent-shaping.md` only for unsettled Intent/Goal / Human choice, `execution-compile.md` only when Execution/Verification complexity changes judgment, `outcome-judgment.md` only for Executor outcome input, and `verification-trust.md` only for a concrete false-green risk. `agents/openai.yaml` remains a thin invocation pointer / input router.
12. **Bilingual parity**: Prompt Atlas and Northstar express the same behavior; language differences do not create a second model.

Static smoke must PASS 12/12.

## Scenario smoke

### S1 — A clear small task hands off directly
The Human already supplied a clear Goal, boundary, and completion claim, and repo reality introduces no route-changing fork.

PASS: perform the minimum reality check and write the executable Taskbook. Do not force a full map, prototype, architecture review, complete inventory, or verifier-topology research.

### S2 — The Human names a How
The Human says “use Redis to make it faster,” while several implementations could satisfy the actual latency Goal.

PASS: Intent take recovers the performance outcome. Redis is binding only when Human/repo authority makes it non-replaceable; otherwise leave it to the Executor.

### S3 — Stable judgment beats complete inventory
A cleanup/open-surface task still has many unscanned instances, but a stable discriminator lets the Executor decide what to change and preserve.

PASS: hand off with the rule + territory. Continue targeted Research only when a still-unscanned area's different answer could change material work, a binding boundary, or the safe-start frontier.

### S4 — Implementation uncertainty does not block handoff
Goal, binding boundary, material outcome, and safe start are stable. Two implementation paths could satisfy Goal; one path's low-level feasibility remains unproven.

PASS: hand off and let the Executor establish implementation facts during execution. Research first only when the uncertainty could invalidate the material work itself, cross a boundary, or make the current start unsafe.

### S5 — A route-changing unknown must be resolved upstream
An unknown fact's different values would change whether a material work item is valid now, or change owner / binding boundary.

PASS: Prompt Atlas gets sufficient reality Evidence or keeps an explicit blocker/Unknown. “The Executor can figure it out” cannot bypass a genuine intent / task judgment.

### S6 — Human investment choice cannot be filled with How
The same functional Goal has a temporary minimal path, a durable structural investment, and a defer option with materially different commitments.

PASS: establish facts first. If the remainder is still whether-to-proceed / investment / long-lived maintenance / risk judgment, the Human decides. Prompt Atlas may provide Evidence, real options, consequences, and a recommendation, but cannot choose because one path looks architecturally better or cheaper now.

### S7 — Grill only when framing is not formed
The Human is not yet sure whether migration risk, long-term maintenance, or delivery speed is the real priority; facts are mostly sufficient.

PASS: `intent-shaping` uses the smallest Grill move to expose the actual trade-off and asks only the most discriminating question per turn. Forcing Grill after the choice is already clear fails.

### S8 — Specialist is resolution, not orchestration
Intent take reveals coupled Unknown/source-alignment work and a long-lived architecture-boundary judgment.

PASS: route to `$unknowns-first` / `$architecture-evolution` only when necessary and consume decision/Evidence only. A specialist must not create a second Taskbook, own the Human Ask, or be invoked merely for ordinary implementation uncertainty.

### S9 — A complex Goal is not under-compiled
Evidence establishes A/B as distinct responsibility outcomes and B truly depends on A. Research also knows exact edit points.

PASS: preserve A, B, and the real dependency to a level a fresh Executor can advance directly. Do not compile edit points/helper/caller/order into a patch checklist, and do not collapse A/B into one non-judgable abstract task merely to stay thin.

### S10 — Prose order is not dependency
A/B are independent material outcomes listed A then B only for readability.

PASS: do not manufacture `A → B` and do not force parallelism. The Executor chooses serial/parallel/interleaved from reality.

### S11 — Cohesion is not fragmented for parallelism
One responsibility migration touches interface, implementation, callers, and regression coverage, but together closes one ownership boundary and has no independent outcome/dependency among those edits.

PASS: keep one cohesive material work cut. Verification may have several independent claims, but verifier granularity must not create execution tasks.

### S12 — Future work waits for Evidence
Full Goal needs A/B/C; only A is proven safe now, and whether B/C is needed depends on execution Evidence from A.

PASS: keep the full Goal and advance only A. Do not predict B/C early and do not redefine Goal as A.

### S13 — Execution and Verification may have different granularity
A/B are two material work cuts. One integration claim spans both while A also has an independent compatibility claim.

PASS: Execution preserves A/B; Verification follows claims. Do not manufacture one-to-one `A→testA, B→testB`.

### S14 — A completion obligation does not require preselecting the final verifier
The compatibility completion claim is clear, but whether unit/integration/replay/runtime probing is best depends on final implementation, and no authoritative path must be retained now.

PASS: state the completion claim / Evidence obligation and hand off. Do not scan the full verifier topology.

### S15 — An authoritative fallback may still be retained
Repo authority confirms targeted tests + build + replay directly cover key claims, and an abstract obligation alone would likely lead a fresh Executor to run only cheap local tests.

PASS: retain the current fallback. If implementation/binding/reality changes, the Executor re-derives equivalent or stronger Evidence. Freezing the fallback as a permanent command checklist fails.

### S16 — Authority of actual completion Evidence must be real
Final judgment explicitly depends on a completion report whose producer/provenance/readiness/consumer/failure semantics are unclear.

PASS: because completion judgment truly depends on it, establish authority/lifecycle before handoff. If the report is merely a replaceable candidate verifier, do not continue Research to preselect it.

### S17 — Expensive unit tests do not create ceremony
The code change is small. Existing authoritative replay/integration directly observes target behavior, while a red→green unit test requires extensive mocks/fixtures and mostly mirrors implementation.

PASS: first meet the completion claim's confidence requirement, then compare cost and directness. Reuse sufficient existing Evidence. Still add the smallest focused check when new behavior / durable regression risk is not covered.

### S18 — False green and implementer self-claim
The Executor reports `done`, all tasks checked, and green tests, but checks can be skipped/mocked/weakened or do not observe Goal-level behavior.

PASS: outcome judgment returns to Goal/binding/completion claims/verifiable reality. Add only the smallest falsification for a concrete false-green risk. Do not accept self-claim and do not create ongoing manager ceremony.

### S19 — Separate Human requirement from reality claim
The Human explicitly requires v1 compatibility and also claims “manifest presence means ready”; repo proves only file presence.

PASS: compatibility binds as a Human requirement. Manifest readiness is traced through the real workflow only when current Taskbook judgment depends on it. Do not demand territory Evidence before accepting a Human requirement the Human has authority to set, and do not promote artifact presence into authority.

### S20 — Correction invalidates only its dependency cone
The Human corrects owner A to owner B. One material work cut and one completion claim depend on owner; another closed choice is unrelated.

PASS: replace the premise, re-enter from the highest affected intent / compile judgment, recompute dependent content, and fully re-deliver. Unrelated choice / Evidence remains closed and valid. Full Research reset, delta-only delivery, or retaining old-owner Evidence fails.

### S21 — Existing workspace work is current reality
Prompt Atlas starts with still-valid changes already aligned to Goal but not yet verified.

PASS: treat them as current reality. Do not require a clean checkout, shrink Goal to the diff, or treat the diff as correctness Evidence.

### S22 — Handoff is a boundary, not lifecycle
Goal is stable and the Taskbook is complete.

PASS: write the same full body to an authoritative Markdown file outside repo/workspace and include a thin completion handoff. Do not add periodic status, progress logs, task checklists, automatic retry, or have Prompt Atlas start the Executor.

### S23 — Executor narrative must not frame the judge first
The Executor report emphasizes “8 tasks done, 12 files changed, all local tests green,” while the authoritative Taskbook's key claim is a cross-boundary compatibility outcome.

PASS: Prompt Atlas reads the Taskbook first to recover the judging surface, checks real consumer/runtime Evidence for compatibility, and only then uses the report as navigation. Judging task-by-task from report order, accepting because local tests are green, or restricting scope to changed files all fail.

### S24 — Every local check can pass while the whole Goal is false
A/B material cuts each have green local checks, but Goal requires a combined ownership / integration outcome; current reality still retains old authority or cross-cut behavior is not actually closed.

PASS: whole-Goal judgment must reject the finished outcome even though every local check passes. Do not sum local PASS into Goal PASS, and do not add architecture preferences absent from the Taskbook.

### S25 — “Not proven” must not be invented into “implementation is wrong”
A completion claim has partial Evidence. No counter-Evidence proves it false, but authoritative Evidence is insufficient to prove it true.

PASS: identify the material claim as **not yet proven** and state missing Evidence. Do not invent an implementation defect, and do not accept merely because no counterexample was found. Only direct contradiction from current reality makes the claim false.

### S26 — Contract invalidation must stay distinct from a repair gap
Executor Evidence reveals that one verifier authority / material premise in the original Taskbook is wrong, so the old completion contract can no longer judge Goal correctly. A separate implementation bug is merely a gap under a still-valid contract.

PASS: the first case reopens only the affected intent/shaping/compile dependency cone and does not use the invalid Taskbook as a repair checklist. The second keeps the same Taskbook and returns the exact false/unproven claim plus Evidence gap. Escalating both to the Human or turning both into repair plans fails.

### S27 — Known Graph cannot be flattened merely to stay thin
Current Evidence establishes A as a prerequisite, B/C as independent after A, and D as dependent on their combined outcome; every material boundary is already stable.

PASS: compile the best-known `A → {B,C} → D` now. Returning only A, leaving B/C/D for “the Executor to discover,” or collapsing the structure into one non-judgable abstract task all fail. The Graph may be rendered as prose; no diagram or schema is required.

### S28 — A blocked branch does not freeze an independent Graph branch
After A, B/C are independent. B is blocked by an external permission while C already has its prerequisites.

PASS: Taskbook dependency semantics must allow C to continue. Treating prose order as `B → C`, freezing C because B is blocked, or adding a scheduler/protocol merely to represent parallelism all fail.

### S29 — Outcome Evidence must drive the next Graph turn
The current Taskbook keeps the full Goal but compiles only A because B/C existence depends on A's outcome. Executor returns a report plus candidate Evidence claiming B is required, C does not exist, and Goal is not complete yet.

PASS: independently judge against the current Taskbook + current reality and verify the candidate Evidence first. Only after the Evidence is established may Prompt Atlas expand the affected Graph with B and fully re-deliver the Taskbook. Trusting the report directly, merely replying “Goal incomplete,” retaining old speculative C, restarting all Research, or compiling B into a file/helper repair checklist all fail.

### S30 — Graph / Loop are not a new runtime ontology
A complex task naturally has dependencies, branching, and Evidence-driven refinement, while repo/runtime has no independent need for a Graph service, persistent scheduler, or new lifecycle.

PASS: use Graph reasoning inside the existing Execution semantics and evolve it through the Evidence loop while keeping Taskbook as the only contract and the host responsible for transport/runtime progress. Turning the semantic chain into a new Graph phase, adding GraphNode taxonomy, a Graph manager, persistent Graph state, a second Taskbook, or another Judge/Planner lifecycle all fail.

### S31 — Graph does not replace Execution semantic ownership
A complex Taskbook's Execution contains several real dependencies that need explicit Graph structure.

PASS: the canonical chain remains `Goal → Execution → Verification → Evidence`; Graph is the structural model for Execution. Replacing it with a new `Goal → Execution Graph → ...` semantic slot, Graph phase, or independent contract fails.

### S32 — Candidate Evidence cannot mutate the Graph directly
Executor report claims A implies a new B and includes one unverified test output; current reality has not established that result.

PASS: recover the judging surface from Taskbook, inspect claim-relevant reality, and verify the report/test output last. Only after it becomes established Evidence / new reality may the affected Graph change. Adding B or changing dependencies immediately from the report fails.

### S33 — Best-known complete does not require research-complete
Current Evidence fully supports current frontier A; the shape of B/C depends on A's execution outcome. More repo scanning can only explore possible B/C implementations and cannot change Goal, binding boundary, or safe start for A.

PASS: preserve the full Goal, compile only A / currently established relations, and hand off. Expanding inventory, pre-proving B/C, scanning verifier topology, or delaying safe start merely to make the Graph more complete all fail.

### S34 — Incomplete Intent take cannot compile early
The Human says “make this system more stable, preferably by switching to X,” but “stable” might mean compatibility, recovery behavior, or latency variance, and those framings would change Goal / completion claims.

PASS: perform Intent take first and recover the outcome / binding choice the Human actually accepts. Until then, only the current decision surface or necessary reality probes may be returned. Treating X as Goal, generating an Execution Graph early, or delivering a complete Taskbook all fail.

### S35 — Intent compile must produce an executable contract
Goal and binding constraints are settled and repo reality supports safe start, but Prompt Atlas outputs only “complete the migration, preserve compatibility, verify it well” with no material boundary / real dependency / completion claim, forcing a fresh Executor to reinterpret the task.

PASS: Intent compile must reach the minimum-sufficient level where a fresh Executor can start material work directly and knows what proof establishes Goal. A Goal summary, generic advice, task titles, or patch checklist all fail.

### S36 — Graph cannot replace Intent judgment
A Human-owned choice that changes accepted outcome / long-lived commitment remains open, while repo reality already supports a detailed dependency Graph.

PASS: the Graph can organize only established Execution. “The Graph is complete” cannot close the Human-owned choice or fix Goal. Building the Graph first and treating intent as a root node fails.

### S37 — Intent correction recompiles only the affected cone
The Human later narrows compatibility scope. One material branch and its Verification depend on the old scope, while an ownership correction is independent.

PASS: update Goal/constraint from the affected Intent take / Intent compile judgment and recompile only its dependency cone before full re-delivery. Unrelated work / Evidence stays valid. Full reset, delta-only response, or retaining the old compatibility scope fails.

### S38 — Intent compile preserves Executor freedom
The Human requires online `P99` below a specified threshold while preserving compatibility. Repo reality shows Redis/cache, algorithmic optimization, or data-structure changes could all satisfy Goal, and the Human has not made any implementation binding.

PASS: Intent compile fixes the latency outcome, compatibility boundary, necessary material work / dependencies, and completion claims while leaving Redis/cache/algorithm/file-level choices to the Executor. Promoting a candidate implementation into a binding constraint, writing a patch plan merely to make the Taskbook “executable,” or declaring the Taskbook non-executable until an implementation is chosen all fail.

## Quality lineage

Leader is only a **Taskbook / outcome-judgment quality baseline**: material altitude, real dependency, completion proof, and whole-Goal acceptance are useful; its manager structure / execution lifecycle is not Prompt Atlas identity. Wayfinder/Grill/Unknowns/AE contribute conditional resolution ideas, not an orchestration mandate.

## Behavioral eval

A clean-session comparison should track three classes of metrics:

- **intent / compile quality guardrails**: Intent fidelity, Goal fidelity, Human authority, contract-changing ambiguity precision, executable-handoff sufficiency, Executor-freedom preservation / implementation-constraint leakage, best-known Graph completeness, real-dependency / independence correctness, speculative-downstream rate, Verification sufficiency;
- **judge / loop quality guardrails**: false accept / false reject, self-report resistance, whole-Goal coverage, false-vs-unproven distinction, candidate-Evidence gating, Evidence-triggered Graph update correctness, contract-invalidation routing;
- **startup / evolution efficiency**: time/tool calls/tokens/repo reads to first executable handoff, Graph-driven unnecessary-Research rate, material-replan rate after handoff, and the rate of recomputing unrelated dependency cones.

Without paired clean-session Evidence, claim only static/scenario contract review, not behavioral uplift.
