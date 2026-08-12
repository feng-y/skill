# Prompt Atlas Validation

Eval / review only. Normal runtime must not read this file. It tests behavior and does not require runtime to use particular terminology.

## Static smoke

1. The main Skill clearly separates **Capabilities** from **Flow**: Capabilities define what Prompt Atlas can judge and handle; `Take → Ground → Shape → Compile → Deliver` is only the playbook for one task and must not redefine or shrink the capability surface.
2. When input is still a problem space or means-heavy, it does not rush into Taskbook writing; it first settles what result the Human will actually accept.
3. Facts repo/runtime can decide are probed first; only choices reality cannot settle and that change Goal go to the Human; implementation How remains with the Executor.
4. Research stops when more context can change only How; an executable Goal is not delayed merely to eliminate Unknowns.
5. Existing authoritative specs are referenced directly; the current workspace is reality, not a reason to require clean state or treat the existing diff as correctness proof.
6. The Taskbook makes only truly authoritative requirements binding; a currently preferred implementation remains replaceable.
7. In complex execution, the subset safe to advance now cannot replace or shrink the full Goal; only real dependencies that change execution choice are recorded.
8. Verification states what must be proven rather than prescribing debugging flow; the judge cannot be weakened to manufacture PASS, and extra trust checks appear only for a concrete false-green risk.
9. Autonomous handoff materializes outside repo/workspace; after a Human change affecting Goal/Taskbook, the complete current Taskbook is delivered again, and prior delivery is not completion state.

Static smoke must PASS 9/9.

## Scenario smoke

### S1 — Human names a How
The Human says “use Redis to make it faster,” while the repo supports other credible paths.

PASS: Prompt Atlas recovers the actual performance Goal. Redis becomes fixed only when Human/repo authority makes Redis itself non-replaceable.

### S2 — Human supplies only a problem space
The Human says “modernize this legacy module,” while reality supports several materially different finished outcomes.

PASS: Prompt Atlas does not rush into Taskbook writing. It first looks for reality that removes branches, then surfaces the remaining Human-owned Goal choices together.

### S3 — Three unsettled questions appear together
One question is repo-factual, one changes the Goal the Human will accept, and one changes only code How.

PASS: probe the first, ask the Human the second, leave the third to the Executor. Do not collapse them into “ask all” or “research all.”

### S4 — A concrete plan mixes implementation with a real constraint
The Human supplies a detailed implementation design; half could be replaced while preserving the requirement, while half is actually a compatibility commitment.

PASS: leave the replaceable half with the Executor and keep the commitment in Goal. Concrete wording alone must not put both at the same level.

### S5 — Human requirements conflict
The Human simultaneously requires “zero compatibility break” and “remove the old protocol completely,” and reality proves they conflict.

PASS: Prompt Atlas does not choose based on preferred architecture. It checks existing authority, then asks the Human which requirement wins if the conflict remains.

### S6 — Research is sufficient
A cleanup task still has many unscanned instances, but a stable rule lets the Executor decide what to remove and preserve.

PASS: stop exhaustive discovery, write the rule and scope, and deliver. Full inventory is not a prerequisite.

### S7 — Preferred implementation is not a hard requirement
Research suggests a provider pattern, but Human/repo authority requires only a behavior and dependency direction.

PASS: behavior/dependency are binding requirements; provider pattern remains replaceable and the Executor may choose another compliant implementation.

### S8 — Existing workspace work
Prompt Atlas is invoked with still-valid changes already aligned to Goal but not fully verified.

PASS: treat them as reality and continue. Do not demand a clean checkout, treat the diff as correctness proof, or shrink Goal to “finish this diff.”

### S9 — Only part is safe now
Full Goal needs A/B/C; current reality makes only A safe to advance, while whether B is needed depends on Evidence from A.

PASS: keep the full Goal and advance only A for now. After A's Evidence arrives, decide B/C. Do not redefine Goal as A.

### S10 — Known dependency plus future discovery
Current reality proves `A → {B,C} → D`, while execution may expose additional contingent work later.

PASS: write the relations that already change execution choice; do not intentionally expose only A, and do not predict contingent future work.

### S11 — PASS may be false-green
Visible verification can be bypassed with skip/mock/threshold changes, or it does not actually observe target behavior.

PASS: do not weaken the judge. Add only the minimum check that falsifies the concrete risk. No generic hidden-test/independent-review ceremony without a concrete risk.

### S12 — A simple Goal stays simple
The Human already supplied a clear result, boundaries, and Verification, and repo reality introduces no upstream fork.

PASS: Flow grounds quickly, then Compile/Deliver. A stronger capability surface must not force every task to expand all shaping/unknown/complex-execution capabilities.

### S13 — Autonomous handoff followed by correction
Prompt Atlas has written a Taskbook to an external artifact; the Human then changes a requirement that truly changes Goal.

PASS: re-enter at the affected step and fully update/rewrite the current Taskbook, surfacing the authoritative path. A delta-only reply fails; Prompt Atlas must not execute the Taskbook itself.

## Comparison with Leader

Leader is a strong taskbook/manager baseline, not the full definition of Prompt Atlas. Prompt Atlas should retain Leader's proven behaviors: research facts before asking, batch real Human choices, reference existing specs, keep Taskbook smaller than Research, and never let the Executor weaken the judge to manufacture success.

Prompt Atlas must additionally demonstrate upstream capability: **when input is not yet an executable Goal, settle Goal first; route different unsettled questions to the person or reality that can actually decide them; preserve Executor judgment over How; in complex execution advance only what is safe now without losing the full Goal; and materialize the current autonomous Taskbook for a fresh Executor.** Flow is only the default playbook for invoking these capabilities, not the boundary of the capability surface.

If these differences are not observable in eval, Prompt Atlas has degraded into a weaker rewrite of Leader and fails the design goal.

## Behavioral eval

Under same model / repo snapshot / tool permission / clean session compare at least: ambiguous problem space, named means, mixed fact/Human/How, mixed constraint/implementation, conflicting requirements, replaceable implementation advice, partial-safe execution, simple executable Goal, autonomous materialization, and full re-delivery after Human correction.

Without clean-session results, only static/scenario contract review may be claimed; behavioral parity/uplift remains `NOT RUN`.
