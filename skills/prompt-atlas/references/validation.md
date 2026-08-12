# Prompt Atlas Validation

Eval / review only. Normal runtime must not read this file. It tests behavior and does not require runtime to use particular terminology.

## Static smoke

1. The main Skill follows a mature taskbook structure: **roles/boundary → Research → Ask → Write → Deliver → writing rules → pre-delivery check**. Prompt Atlas expresses additional capability through judgment inside those actions rather than through lifecycle/status or a parallel terminology layer.
2. When input is still a problem space or means-heavy, it does not rush into Taskbook writing; it first settles what Goal the Human will actually accept.
3. Unsettled questions route to the resolution owner that can actually close them: ordinary facts are probed directly; coupled Unknown / source-alignment / full-map problems route to `$unknowns-first` when available; long-lived module responsibility/boundary/dependency-direction/Target-Architecture judgments route to `$architecture-evolution` when available; only Human-owned Goal choices go to Ask; implementation How stays with the Executor. If a specialist is unavailable, make only the smallest equivalent judgment needed to close the current Goal/Taskbook rather than copying a second protocol.
4. Ask batches the Human-owned choices whose prerequisites are already settled and that can be answered independently now, with consequences/recommendation. Downstream choices that still depend on an open Human decision are not asked early. After a partial answer, new constraint, interruption, or correction, Prompt Atlas resumes from affected judgment and continues to Write/Deliver once Goal is stable.
5. Research stops when more context changes only How; authoritative specs are referenced directly; current workspace is reality, not a reason to require clean state or treat an existing diff as correctness proof.
6. The Taskbook makes only truly authoritative requirements binding and keeps preferred implementation replaceable. Execution content stays at outcome/judgment/boundary/dependency altitude rather than a predicted file/helper/test checklist.
7. In complex execution, the subset safe to advance now cannot replace or shrink the full Goal; only real dependencies that change execution choice are recorded, and contingent future work is not pre-sliced into speculative tasks.
8. Implementation granularity and Verification granularity are independent: implementation splits by result/judgment/dependency, Verification by completion claim / risk / authority, with no one-to-one requirement.
9. Verification states what must be proven rather than prescribing debugging flow; the judge cannot be weakened to manufacture PASS, and extra trust checks appear only for a concrete false-green risk.
10. Every successful Taskbook is materialized as the same complete body to an authoritative Markdown file outside repo/workspace and the real path is surfaced; chat-only delivery fails.
11. After either an Ask or a prior Taskbook delivery, material Human clarification/correction reopens affected judgment and fully re-delivers the current Taskbook. Previous Ask/delivery is not completion state. Specialist output is folded back only as current decision/Evidence; it never becomes a second Prompt Atlas SOT.

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

### S9 — Taskbook keeps Leader-level altitude
The task spans three modules and many files, and Research has already found likely edit points.

PASS: organize the Taskbook by outcome, responsibility boundary, judgment, real dependency, and completion proof. A step-by-step `edit A.cpp / add BHelper / update C caller / run DTest` patch checklist fails unless those representations are themselves authoritative invariants.

### S10 — Existing workspace work
Prompt Atlas is invoked with still-valid changes already aligned to Goal but not fully verified.

PASS: treat them as reality and continue. Do not demand a clean checkout, treat the diff as correctness proof, or shrink Goal to “finish this diff.”

### S11 — Only part is safe now
Full Goal needs A/B/C; current reality makes only A safe to advance, while whether B is needed depends on Evidence from A.

PASS: keep the full Goal and advance only A for now. After A's Evidence arrives, decide B/C. Do not redefine Goal as A.

### S12 — Implementation and Verification have different granularity
Implementation naturally splits into Work A and Work B by responsibility, but the final completion claim needs one integration verification across both, while Work A also carries an independent compatibility claim.

PASS: keep A/B as implementation work; Verification is the integration claim plus A's compatibility claim. Do not manufacture `A→testA, B→testB`, and do not split implementation merely to mirror tests.

### S13 — Known dependency plus future discovery
Current reality proves `A → {B,C} → D`, while execution may expose additional contingent work later.

PASS: write the relations that already change execution choice; do not intentionally expose only A, and do not predict contingent future work. Add future work only when Evidence makes it real.

### S14 — PASS may be false-green
Visible verification can be bypassed with skip/mock/threshold changes, or it does not actually observe target behavior.

PASS: do not weaken the judge. Add only the minimum check that falsifies the concrete risk. No generic hidden-test/independent-review ceremony without a concrete risk.

### S15 — A simple Goal stays simple
The Human already supplied a clear result, boundaries, and Verification, and repo reality introduces no upstream fork.

PASS: Research briefly, then Write/Deliver. Do not force a full map, architecture specialist, or extra Ask merely to demonstrate stronger problem-solving capability.

### S16 — Successful output must land in a file
Goal is stable and Prompt Atlas has produced the complete Taskbook.

PASS: the same complete Taskbook is written to an authoritative Markdown file outside repo/workspace and the actual path is surfaced. Chat may also show the body, but “chat only / tell Human to save it / let Executor reconstruct from conversation” fails.

### S17 — Human clarifies after delivery
Prompt Atlas has already written the authoritative Taskbook file; the Human changes a requirement that materially affects Goal or Verification.

PASS: re-enter affected judgment and fully update the current artifact. If the old path is not writable, materialize a new artifact and surface its authoritative path. Delta-only explanation fails; Prompt Atlas must not execute the Taskbook itself.

### S18 — One problem needs different resolution capabilities
One problem space simultaneously contains: a repo fact that can be checked directly; a coupled set of Unknowns that needs a full map before the route is clear; a long-lived architecture judgment about module responsibility/boundary/dependency direction; a product tradeoff only the Human can make; and a pure implementation-How question.

PASS: route them respectively to ordinary probe, available `$unknowns-first`, available `$architecture-evolution`, Ask, and the Executor. Prompt Atlas consumes specialist decision/Evidence and continues converging the same Goal/Taskbook. Sending all five through generic Research, asking the Human all five, or treating specialist output as a second Taskbook fails. If a specialist is unavailable, only the smallest equivalent judgment needed to close the current Goal/Taskbook is allowed; copying its full protocol fails.

### S19 — Human choices have prerequisites
There are three Human-owned choices. A and C can be answered independently now. Whether B exists and what its options are both depend on A.

PASS: ask A/C together in the first round with consequences/recommendation; do not ask B yet. After A closes, ask B if it still exists. Asking only A serializes C unnecessarily; asking A/B/C together forces the Human to guess B before its premise is known. Both fail.

## Comparison with Leader

Leader is Prompt Atlas's **structural and taskbook-quality baseline**: clear roles; stable Research → Ask → Write → Deliver actions; research facts before asking; batch real Human choices; reference existing specs; keep Taskbook at goal/judgment altitude; treat Verification as an independent judging surface; and never let the Executor weaken the judge to manufacture success.

Prompt Atlas must add upstream problem-solving and handoff control on top of that baseline: **settle Goal when input is not yet executable; Ask only the currently answerable Human-decision frontier and continue after answers/interruption; route unsettled questions to the owner/capability that can actually resolve them instead of collapsing everything into Research/Ask; preserve Executor judgment over How; advance only safe work without losing full Goal; separate implementation granularity from Verification granularity; materialize every successful Taskbook to an authoritative file; and fully re-deliver after later Human changes.**

If its structure drifts away from a mature taskbook skill, or these additional capabilities are not observable in eval, Prompt Atlas has regressed.

## Comparison with Wayfinder

Wayfinder's high-value baseline is **Map + resolution routing**: the Map is a canonical cross-session decision control plane containing the destination, decisions already made, and work still needing resolution; the current question is then routed by type to research, prototype, grilling/task and related specialist capability such as domain-modeling. The value comes from those different resolution capabilities feeding decisions back into one destination until no decision remains that blocks later execution.

Prompt Atlas does not copy Wayfinder's tracker/ticket protocol or own a second persistent Map. This repo already has the relevant owners: coupled Unknown / source-alignment / full-map work belongs to `unknowns-first`; long-lived structural judgment belongs to `architecture-evolution`; ordinary Human choices stay in Prompt Atlas Ask; pure How stays with the Executor. Prompt Atlas is responsible for **recognizing which resolution capability the current problem needs, folding its result back into the same Goal/Taskbook, and continuing to a high-quality handoff**.

Wayfinder's fog/frontier semantics can support that process, but they are not the primary benchmark. If Prompt Atlas remembers only “map != reality / do not pre-slice the future” while failing to choose the right resolution capability, it has not absorbed Wayfinder's core value.

## Behavioral eval

Under same model / repo snapshot / tool permission / clean session compare at least: ambiguous problem space, named means, mixed fact/Human/How, specialist-capability routing, dependent Human-choice frontier, Ask interruption/reply, mixed constraint/implementation, replaceable implementation advice, Taskbook altitude, partial-safe execution, implementation-vs-verification granularity, simple executable Goal, file materialization, and full re-delivery after Human correction.

Without clean-session results, only static/scenario contract review may be claimed; behavioral parity/uplift remains `NOT RUN`.
