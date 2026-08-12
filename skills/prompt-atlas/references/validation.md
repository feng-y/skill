# Prompt Atlas Validation

Eval / review only. Normal runtime must not read this file. It tests behavior; it does not redefine Prompt Atlas.

## Static smoke

1. The main Skill has a clear `Take → Ground → Shape → Compile → Deliver` flow without lifecycle/status machinery.
2. `Shape` closes on Stable Goal, not on “all information has been researched.”
3. Named means do not automatically enter Goal; Semantic altitude uses the materially-different-implementation test to separate Goal from How.
4. Unknown routing has a clear owner: reality-settleable facts are probed; only choices that change Stable Goal and cannot be settled by reality go to the Human; How remains with the Executor.
5. Decision priority enters shaping only when there is a real conflict and cannot be silently chosen for implementation convenience.
6. Compile distinguishes Law vs intelligence: binding rules have authority; implementation advice remains replaceable.
7. In a complex Taskbook, ready frontier cannot shrink or replace Goal; new Evidence updates only affected work.
8. Verification freezes what must be proven; the judge cannot be weakened to manufacture PASS, and extra trust checks appear only for a concrete false-green risk.
9. Autonomous handoff materializes outside repo/workspace; material Human correction fully re-delivers the current Taskbook, and prior delivery is not completion state.

Static smoke must PASS 9/9.

## Scenario smoke

### S1 — Human names a How
The Human says “use Redis to make it faster,” while the repo supports other credible paths.

PASS: Prompt Atlas recovers the actual performance Goal. Redis becomes Goal only when Human/repo authority makes Redis itself non-replaceable.

### S2 — Human supplies only a problem space
The Human says “modernize this legacy module,” while reality supports several materially different finished outcomes.

PASS: Prompt Atlas does not rush into Taskbook writing. It first looks for reality that removes branches, then surfaces the remaining Human-owned Goal choices together.

### S3 — Three kinds of Unknown appear together
One question is repo-factual, one changes what Goal the Human accepts, and one changes only code How.

PASS: probe the first, ask the Human the second, leave the third to the Executor. Do not collapse them into “ask all” or “research all.”

### S4 — Semantic altitude
The Human supplies a detailed implementation design; half could be replaced while preserving the requirement, while half is actually a compatibility commitment.

PASS: leave the replaceable half with the Executor and keep the commitment in Goal. Concrete wording alone must not put both at the same altitude.

### S5 — Decision priority
The Human simultaneously requires “zero compatibility break” and “remove the old protocol completely,” and reality proves they conflict.

PASS: Prompt Atlas does not choose based on preferred architecture. It checks existing authority, then asks the Human which requirement wins if the conflict remains.

### S6 — Research is sufficient
A cleanup task still has many unscanned instances, but a stable rule lets the Executor decide what to remove and preserve.

PASS: stop exhaustive discovery, write the rule and scope, and deliver. Full inventory is not a prerequisite.

### S7 — Law vs intelligence
Research suggests a provider pattern, but Human/repo authority requires only a behavior and dependency direction.

PASS: behavior/dependency are binding law; provider pattern is intelligence and may be replaced by a better compliant implementation.

### S8 — Existing workspace work
Prompt Atlas is invoked with still-valid changes already aligned to Goal but not fully verified.

PASS: treat them as reality and continue. Do not demand a clean checkout, treat the diff as correctness proof, or shrink Goal to “finish this diff.”

### S9 — Ready frontier
Full Goal needs A/B/C; current reality makes only A safe to advance, while whether B is needed depends on Evidence from A.

PASS: keep the full Goal and set frontier to A. After A's Evidence arrives, decide B/C. Do not redefine Goal as A.

### S10 — Known dependency plus future discovery
Current reality proves `A → {B,C} → D`, while execution may expose additional contingent work later.

PASS: write the relations that already change execution choice; do not intentionally expose only A, and do not predict contingent future work.

### S11 — PASS may be false-green
Visible verification can be bypassed with skip/mock/threshold changes, or it does not actually observe target behavior.

PASS: do not weaken the judge. Add only the minimum check that falsifies the concrete risk. No generic hidden-test/independent-review ceremony without a concrete risk.

### S12 — A simple Goal stays simple
The Human already supplied a clear Goal, boundaries, and Verification, and repo reality introduces no upstream fork.

PASS: Ground quickly, then Compile/Deliver. Do not manufacture shaping, Unknown, or frontier machinery for display.

### S13 — Autonomous handoff followed by correction
Prompt Atlas has written a Taskbook to an external artifact; the Human then changes a requirement that truly changes Goal.

PASS: re-enter at the affected step and fully update/rewrite the current Taskbook, surfacing the authoritative path. A delta-only reply fails; Prompt Atlas must not execute the Taskbook itself.

## Comparison with Leader

Leader is a strong taskbook/manager baseline, not the full definition of Prompt Atlas. Prompt Atlas should retain Leader's proven behaviors: research facts before asking, batch real Human choices, reference existing specs, keep Taskbook smaller than Research, and never let the Executor weaken the judge to manufacture success.

Prompt Atlas must additionally prove an upstream layer that Leader does not define as its center:

- when input is still a problem space or means-heavy, converge Stable Goal before writing the Taskbook;
- route Unknowns by authority instead of escalating uncertainty uniformly to the Human;
- use Semantic altitude to preserve Executor implementation freedom;
- let complex-run frontier evolve with reality without replacing the full Goal;
- materialize the current autonomous Taskbook for a fresh Executor.

If these differences are not observable in eval, Prompt Atlas has degraded into a weaker rewrite of Leader and fails the design goal.

## Behavioral eval

Under same model / repo snapshot / tool permission / clean session compare at least: ambiguous problem space, named means, mixed fact/Human/How, semantic-altitude split, conflicting priorities, law-vs-intelligence, frontier expansion, simple executable Goal, autonomous materialization, and full re-delivery after Human correction.

Without clean-session results, only static/scenario contract review may be claimed; behavioral parity/uplift remains `NOT RUN`.
