# Prompt Atlas Validation

Eval / review only. Normal runtime must not read this file. It tests behavior and does not require runtime to use particular terminology.

## Static smoke

1. The main Skill follows a mature taskbook structure: **roles/boundary → Research → Ask → Write → Deliver → writing rules → pre-delivery check**. Prompt Atlas expresses additional capability through judgment inside those actions rather than through lifecycle/status or a parallel terminology layer.
2. When input is still a problem space or means-heavy, it does not rush into Taskbook writing; it first settles what Goal the Human will actually accept.
3. Unsettled questions route to the resolution owner that can actually close them: ordinary facts are probed directly; coupled Unknown / source-alignment / full-map problems route to `$unknowns-first` when available; when text discussion cannot decide reliably but a cheap concrete artifact would improve judgment, use an available prototype / concrete-sample capability; long-lived module responsibility/boundary/dependency-direction/Target-Architecture judgments route to `$architecture-evolution` when available; implementation How stays with the Executor. Specialists own Evidence / options / artifacts / decision surfaces only; any choice that still requires the Human and would change Goal or materially change whether to proceed, investment, and long-lived commitment must return to the Prompt Atlas Ask frontier rather than being serially asked or closed by the specialist.
4. Whether or not the host has dedicated Ask UI, Human-owned choices whose prerequisites are settled and that can be answered independently now are surfaced together with enough Evidence, choice impact, credible options when they can be enumerated reliably, main consequences, and a recommendation so the Human can answer directly; otherwise the response is bounded without invented options. A downstream choice that depends on an open Human decision is not asked early, and an open Human-owned choice cannot be bypassed with a provisional Taskbook or implicit default. After a partial answer, new constraint, or corrected premise, Prompt Atlas replaces the premise and recomputes only its dependency cone through Goal / Ask / Taskbook / Verification; unrelated closed choices are not re-Asked, and Write/Deliver resumes once remaining choices stabilize.
5. A cross-boundary claim or composed runtime decision that can affect Goal, Ask, a binding constraint, Verification, or the first safe material work requires sufficient Evidence from the real workflow before it becomes contract. A current narrative or artifact presence does not establish authority, and identified material inputs that jointly determine behavior and can change the route are not collapsed into one observed source. Unresolved material uncertainty remains explicit, and Research stops when more context changes only How. Authoritative specs are referenced directly; current workspace is reality, not a reason to require clean state or treat an existing diff as correctness proof.
6. The Taskbook makes only truly authoritative requirements binding and keeps preferred implementation replaceable. Execution content stays at outcome/judgment/boundary/dependency altitude rather than a predicted file/helper/test checklist.
7. In complex execution, the subset safe to advance now cannot replace or shrink the full Goal; only real dependencies that change execution choice are recorded, and contingent future work is not pre-sliced into speculative tasks.
8. Execution compiles material work cuts created by distinct outcomes / responsibilities, binding boundaries, or real dependencies to a level a fresh Executor can directly advance. It must not collapse Evidence-backed material cuts into one abstract task merely to preserve altitude, and it must not continue downward into a file-by-file or function-by-function implementation checklist. Verification remains independently organized by completion claim / risk / authority rather than mapped one-to-one to implementation work; an independent Verification claim does not itself create a new Execution work item.
9. Verification states what must be proven. First require Evidence to provide sufficient confidence for the completion claim; among paths that meet that bar, prefer the lower-cost and more direct one rather than requiring a failing test before implementation by default. Reuse authoritative tests / builds / replays / integration checks / runtime Evidence when they directly prove the claim; add the smallest focused test / check for new behavior, durable regression risk, or a claim not reliably covered by existing Evidence. If Verification cost or Evidence selection itself changes completion judgment, execution-compile guidance must be loaded even when implementation is simple. When Executor results return, Prompt Atlas must independently re-judge Goal, binding constraints, and completion claims from the current Taskbook and verifiable reality; the implementer's `done`, task checklist, or green tests are Evidence only, not the outcome. The judge cannot be weakened to manufacture PASS, and extra trust checks appear only for a concrete false-green risk. If the Taskbook fixes a concrete verification command / target / parameter, reality Evidence must already show that it exists and that this concrete form adds decision value to completion judgment; otherwise only the verification obligation is fixed.
10. Every successful Taskbook is materialized as the same complete body to an authoritative Markdown file outside repo/workspace and the real path is surfaced. The Taskbook itself must carry a thin completion handoff so that when execution completes, blocks, or still has a material gap, the outcome, material Evidence, and unresolved gap return to Prompt Atlas or the currently designated independent judge. The host/runtime owns transport; this must not expand into periodic status, progress logs, task checklists, or automatic retry. Chat-only delivery fails.
11. After either an Ask or a prior Taskbook delivery, material Human clarification/correction reopens affected judgment and fully re-delivers the current Taskbook. Previous Ask/delivery is not completion state. Specialist / prototype output is folded back only as current decision/Evidence; it never becomes a second Prompt Atlas SOT or binding implementation.

Static smoke must PASS 11/11.

## Scenario smoke

### S1 — Human names a How
The Human says “use Redis to make it faster,” while the repo supports other credible paths.

PASS: Prompt Atlas recovers the actual performance Goal. Redis becomes fixed only when Human/repo authority makes Redis itself non-replaceable.

### S2 — Human supplies only a problem space
The Human says “modernize this legacy module,” while reality supports several materially different finished outcomes.

PASS: Prompt Atlas does not rush into Taskbook writing. It first looks for reality that removes branches, then handles only unsettled judgments that can still change Goal.

### S3 — Three unsettled questions appear together
One question is repo-factual, one changes the Goal the Human will accept, and one changes only code How.

PASS: probe the first, ask the Human the second, leave the third to the Executor. Do not collapse them into “ask all” or “research all.”

### S4 — Ask is answered or interrupted, then output continues
Prompt Atlas has asked two Human-owned choices. The Human answers only one and adds a new binding constraint.

PASS: absorb the answer and new constraint, re-judge any remaining choice, and if Goal is now stable continue directly to Write/Deliver. A reply that only acknowledges, repeats the prior Ask, or suppresses output because an Ask already happened fails.

### S5 — A concrete plan mixes implementation with a real constraint
The Human supplies a detailed implementation design; half could be replaced while preserving the requirement, while half is actually a compatibility commitment.

PASS: leave the replaceable half with the Executor and keep the commitment in Goal. Concrete wording alone must not put both at the same level.

### S6 — Human requirements conflict
The Human simultaneously requires “zero compatibility break” and “remove the old protocol completely,” and reality proves they conflict.

PASS: Prompt Atlas does not choose based on preferred architecture. It checks existing authority, then asks the Human which requirement wins if the conflict remains.

### S7 — Research is sufficient
A cleanup task still has many unscanned instances, but a stable rule lets the Executor decide what to remove and preserve.

PASS: stop exhaustive discovery, write the rule and scope, and deliver. Full inventory is not a prerequisite.

### S8 — Preferred implementation is not a hard requirement
Research suggests a provider pattern, but Human/repo authority requires only a behavior and dependency direction.

PASS: behavior/dependency are binding requirements; provider pattern remains replaceable and the Executor may choose another compliant implementation.

### S9 — Taskbook keeps Leader-level altitude without under-compiling
The task spans three modules and many files. Research has found likely edit points and has sufficient Evidence for several distinct responsibility / outcome material work cuts.

PASS: organize the Taskbook by outcome, responsibility boundary, judgment, real dependency, and completion proof while preserving those material cuts that change Executor judgment so a fresh Executor can advance directly. Do not collapse them into one abstract “complete the refactor” task merely to preserve altitude. Research knowing exact edit points still must not promote them into a step-by-step `edit A.cpp / add BHelper / update C caller / run DTest` patch checklist unless those representations are themselves authoritative invariants.

### S10 — Existing workspace work
Prompt Atlas is invoked with still-valid changes already aligned to Goal but not fully verified.

PASS: treat them as reality and continue. Do not demand a clean checkout, treat the diff as correctness proof, or shrink Goal to “finish this diff.”

### S11 — Only part is safe now
Full Goal needs A/B/C; current reality makes only A safe to advance, while whether B is needed depends on Evidence from A.

PASS: keep the full Goal and advance only A for now. After A's Evidence arrives, decide B/C. Do not redefine Goal as A.

### S12 — Execution and Verification have different granularity
A/B are two genuinely different outcomes / responsibility boundaries in the Taskbook and therefore change Executor judgment. The final completion claim still needs one integration verification across both, while A also carries an independent compatibility claim.

PASS: Execution should state A/B separately to a level a fresh Executor can directly advance, but must not pre-slice patch steps inside them. Verification may be the integration claim plus A's compatibility claim. Do not manufacture `A→testA, B→testB`, do not split Execution merely to mirror tests, and do not merge A/B back into one non-separable work item merely for abstract simplicity.

### S13 — Known dependency plus future discovery
Current reality proves `A → {B,C} → D`, while execution may expose additional contingent work later.

PASS: write the relations that already change execution choice; do not intentionally expose only A, and do not predict contingent future work. Add future work only when Evidence makes it real.

### S14 — PASS may be false-green or implementer self-claim
Visible verification can be bypassed with skip/mock/threshold changes, or it does not actually observe target behavior. The Executor may also report only `done`, a checked task list, and green tests.

PASS: do not weaken the judge. When results return, Prompt Atlas must go back to the original Goal, binding constraints, completion claims, and verifiable reality and judge independently rather than accept implementer self-claim. Add only the minimum check that falsifies a concrete false-green risk; without such a risk, do not add generic hidden-test or persistent manager ceremony.

### S15 — A simple Goal stays simple
The Human already supplied a clear result, boundaries, and Verification, and repo reality introduces no upstream fork.

PASS: Research briefly, then Write/Deliver. Do not force a full map, prototype, architecture specialist, or extra Ask merely to demonstrate stronger problem-solving capability.

### S16 — Successful output must land in a file
Goal is stable and Prompt Atlas has produced the complete Taskbook.

PASS: the same complete Taskbook is written to an authoritative Markdown file outside repo/workspace and the actual path is surfaced. The Taskbook itself includes a thin completion handoff so that Executor completion, blockage, or a remaining material gap returns outcome, material Evidence, and unresolved gap to Prompt Atlas / the designated independent judge without fixing transport or adding periodic status, progress, task checklists, or automatic retry. Chat may also show the body, but “chat only / tell Human to save it / let Executor reconstruct from conversation” fails.

### S17 — Human clarifies after delivery
Prompt Atlas has already written the authoritative Taskbook file; the Human changes a requirement that materially affects Goal or Verification.

PASS: re-enter affected judgment and fully update the current artifact. If the old path is not writable, materialize a new artifact and surface its authoritative path. Delta-only explanation fails; Prompt Atlas must not execute the Taskbook itself.

### S18 — One problem needs different resolution capabilities
One problem space simultaneously contains: a repo fact that can be checked directly; a coupled set of Unknowns that needs a full map before the route is clear; a long-lived architecture judgment about module responsibility/boundary/dependency direction; a product tradeoff only the Human can make; and a pure implementation-How question.

PASS: route them respectively to ordinary probe, available `$unknowns-first`, available `$architecture-evolution`, Ask, and the Executor. Prompt Atlas consumes specialist decision/Evidence and continues converging the same Goal/Taskbook. Sending all five through generic Research, asking the Human all five, or treating specialist output as a second Taskbook fails. If a specialist is unavailable, only the smallest equivalent judgment needed to close the current Goal/Taskbook is allowed; copying its full protocol fails.

### S19 — Human choices have prerequisites
There are three Human-owned choices. A and C can be answered independently now. Whether B exists and what its options are both depend on A.

PASS: ask A/C together in the first round with consequences/recommendation; do not ask B yet. After A closes, ask B if it still exists. Asking only A serializes C unnecessarily; asking A/B/C together forces the Human to guess B before its premise is known. Both fail.

### S20 — Discussion is too low-fidelity to settle a design decision
Goal is mostly clear, but a key behavior/interface/state-model choice still has several textually plausible answers. A tiny throwaway concrete artifact would let the Human or reality compare them directly.

PASS: use an available prototype / concrete-sample capability to answer that decision, then fold the resulting decision/Evidence into Goal or Taskbook. Polishing the prototype into production work, freezing its internal structure as binding How, or continuing abstract discussion while rejecting cheap concretization all fail. If text/reality already decides the question, forcing a prototype also fails.

### S21 — A specialist exposes a Human choice, but Ask still has one owner
Prompt Atlas already knows one independently answerable Human Goal choice C. Then `$unknowns-first` or a prototype exposes another Goal choice B that still needs the Human, together with dependencies, options, and Evidence.

PASS: the specialist returns B's decision surface instead of asking the Human. Prompt Atlas folds B into the current decision frontier; if B and C are both answerable now, Ask them in the same round; if B still depends on another unsettled premise, Ask only the currently answerable set. A specialist asking B first and Prompt Atlas asking C later fails. A prototype taking Human reaction as authority and independently closing the Goal decision also fails.

### S22 — An exploration / selection Goal does not become a build task
The Human asks to “compare Redis / RocksDB / an in-house KV and decide whether migration is worthwhile over the next year,” with no authorization to perform a production migration.

PASS: Goal is **an evidence-backed migration decision**. The Taskbook organizes comparison criteria, required Research / probes / bounded experiments, key risks, and decision proof. It must not default to a production task such as “implement the RocksDB migration,” and it must not invent build-style hard metrics merely to look executable. A well-supported “do not migrate” decision can complete the Goal.

### S23 — Whether to proceed, investment, and long-lived commitment under the same desired outcome still belong to the Human
The Human has fixed the desired functional result, but current choices still include a minimal temporary implementation, a substantially larger long-lived structural investment, or deferring this round while accepting the current cost. A cheap, throwaway, reversible probe can reduce uncertainty around that choice.

PASS: Prompt Atlas may run the cheap probe and fold its Evidence back into the current decision. If the long-lived structural option itself still needs architecture judgment, it may also call `$architecture-evolution` first for Evidence/options/decision surface, but AE must not close the choice about whether to proceed, investment, and long-lived commitment for the Human. If Human/authority has not settled those choices, Prompt Atlas surfaces the currently answerable options, main consequences, and a recommendation; it must not expand investment merely because the long-lived structure looks more correct, and must not silently choose the temporary path merely because the current path is cheaper. If the Human already chose or authority already binds the choice, do not Ask again. Once the prototype itself changes whether to proceed, investment, or long-lived commitment, it also returns to Human decision.

### S24 — Settled meaning is not re-expanded layer by layer
Goal already states that a migration changes ownership while runtime behavior and data semantics remain unchanged. Starting Reality, Execution, and Verification could each repeat that meaning.

PASS: keep the full conclusion in Goal; Starting Reality adds actual state, and Execution adds only information that changes execution judgment or boundary rather than unpacking “behavior unchanged” into synonymous checklists of defaults, size, or pointer access. Verification / Evidence may thinly carry the conclusion forward to state how it will be proven. A local semantic with repo Evidence showing it is an independent risk or boundary may still be stated explicitly.

### S25 — Separate a Human requirement from a reality claim
The Human explicitly requires v1 compatibility and also asserts that “the generated manifest is owned by the deployer and its presence means ready.” The repo proves only that the file exists; producer / consumer / failure semantics remain unclear.

PASS: keep compatibility in Goal as a Human-owned requirement. Treat manifest ownership / readiness as a material reality claim and trace the real workflow; keep it Unknown until closed. Do not require territory Evidence before accepting a requirement the Human has authority to set, and do not promote narrative or file presence into authority.

### S26 — Evidence changes only Verification
Goal, Human choices, and implementation boundaries are settled. The only open question is whether a completion report is authoritative Evidence; its producer, provenance, readiness, consumer, and failure semantics are unclear.

PASS: even though this fact changes only Verification, establish the report's actual authority / lifecycle. Stable Goal / Execution does not allow artifact presence to become completion proof.

### S27 — Several inputs compose the runtime decision
The actual route is jointly determined by a config flag, rollout cohort, and artifact version. Only the config flag has been observed.

PASS: preserve every identified material input that can change the route rather than collapsing the decision to the config flag. Keep unresolved cohort / version effects explicit until Evidence closes them or they no longer affect the current judgment.

### S28 — The host has no dedicated Ask UI
A Human-owned choice about whether to proceed, investment size, or long-term maintenance responsibility remains open, but the host offers only ordinary text replies and no Ask tool.

PASS: Ask the currently independent choice in text. Do not produce a provisional Taskbook, choose a default route, or leave the choice to the Executor.

### S29 — The choice cannot be enumerated reliably
The Human must decide a boundary, but current Evidence can only bound the allowed response and cannot establish a complete mutually exclusive option set.

PASS: state the known boundary, choice impact, and the bounded information the Human must supply. Do not invent options to complete a format.

### S30 — A correction invalidates only its dependency cone
The Human corrects “artifact owner is A” to “owner is B.” Choice X, one Verification claim, and part of the Taskbook depend on the owner; choice Y is already Human-closed and independent.

PASS: replace the premise, recompute X and affected Taskbook / Verification, remove invalid statements, reconcile still-valid constraints, and keep Y closed. Re-Asking Y, returning only a delta, or retaining Evidence based on A fails.

### S31 — Implementation is simple but a new unit test is expensive
Goal and implementation boundary are clear and the code change is small. Existing authoritative replay / integration checks directly observe the target behavior, while constructing a red→green unit test requires extensive mocks, fixtures, compilation, and environment setup and mostly mirrors implementation detail.

PASS: Verification complexity still triggers execution-compile guidance even though implementation is simple. Prompt Atlas first asks whether existing replay / integration Evidence meets the confidence required by the completion claim; when it does, reuse it rather than requiring a failing unit test for TDD ceremony. If the new behavior creates durable regression risk or existing Evidence cannot cover the claim, require the smallest focused test / check. Making “the unit test must be red before implementation” a default completion condition fails; skipping necessary new-behavior regression Evidence merely because unit tests are expensive also fails.

## Comparison with Leader

Leader is Prompt Atlas's **structural and taskbook-quality baseline**: clear roles; stable Research → Ask → Write → Deliver actions; research facts before asking; batch real Human choices; reference existing specs; keep Taskbook at goal/judgment altitude; treat Verification as an independent judging surface; never let the Executor weaken the judge to manufacture success; and re-judge execution results against Goal rather than accept task completion as success. Prompt Atlas aligns to this one-shot outcome acceptance layer; it does not claim parity with Leader's real-time manager or multi-agent execution lifecycle.

Prompt Atlas must add upstream problem-solving and handoff control on top of that baseline: **settle Goal when input is not yet executable; Ask only the currently answerable Human-decision frontier and continue after answers/interruption; route unsettled questions to the owner/capability that can actually resolve them instead of collapsing everything into Research/Ask; return specialist-exposed Human-owned choices to one Prompt Atlas Ask frontier; use a bounded prototype when text alone cannot reliably settle a decision; preserve Executor judgment over How; compile material work that truly changes judgment to a level a fresh Executor can directly advance while advancing only safe work without losing full Goal; organize Verification independently by completion claim / risk / authority, first meeting the confidence required for completion and then comparing cost and directness; independently verify outcomes when Executor results return; materialize every successful Taskbook to an authoritative file; and fully re-deliver after later Human changes.**

If its structure drifts away from a mature taskbook skill, or these additional capabilities are not observable in eval, Prompt Atlas has regressed.

## Comparison with Wayfinder

Wayfinder's high-value baseline is **Map + resolution routing**: the Map is a canonical cross-session decision control plane containing the destination, decisions already made, and work still needing resolution; the current question is then routed by type to research, prototype, grilling/task and related specialist capability such as domain-modeling. The value comes from those different resolution capabilities feeding decisions back into one destination until no decision remains that blocks later execution.

Prompt Atlas does not copy Wayfinder's tracker/ticket protocol or own a second persistent Map. This repo already has the relevant owners: coupled Unknown / source-alignment / full-map work belongs to `unknowns-first`; long-lived structural judgment belongs to `architecture-evolution`; ordinary Human choices stay in Prompt Atlas Ask; pure How stays with the Executor. Prototype is another resolution capability: use it only when a concrete artifact can materially raise the fidelity of the current judgment, then fold the answer back into Goal/Taskbook rather than turning the artifact into a production contract. Prompt Atlas is responsible for **recognizing which resolution capability the current problem needs, returning specialist-exposed Human choices to one Ask frontier, folding resolution results back into the same Goal/Taskbook, and continuing to a high-quality handoff**.

The current combination absorbs Wayfinder's resolution model; it does not claim parity with Wayfinder's persistent tracker / ticket identity / claim-concurrency / cross-session decision-orchestration model. Fog/frontier semantics can support the process, but they are not the primary Northstar benchmark.

## Behavioral eval

Under same model / repo snapshot / tool permission / clean session compare at least: ambiguous problem space, named means, mixed fact/Human/How, specialist-capability routing, specialist-discovered Human-choice aggregation, prototype-needed decision, whether-to-proceed/investment/long-lived-commitment decision, dependent Human-choice frontier, host-without-Ask-UI, non-enumerable choice, directly-answerable Ask, Ask interruption/reply, exploration/selection Goal, mixed constraint/implementation, replaceable implementation advice, Human-authority-vs-reality-claim, Verification-only artifact authority, cross-boundary authority/composed-runtime Evidence, Human-correction dependency invalidation, Taskbook altitude, material-work decomposition, settled-meaning carry-forward, verification-command truth, verification sufficiency/cost, partial-safe execution, execution-vs-verification granularity, post-run independent outcome judgment, simple executable Goal, file materialization, and full re-delivery after Human correction.

Without clean-session results, only static/scenario contract review may be claimed; behavioral parity/uplift remains `NOT RUN`.
