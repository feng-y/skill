---
name: prompt-atlas
description: "English counterpart to Northstar. Turn vague ideas, problem spaces, or fragmented requests into the Goal the Human actually wants, then compile a prompt, brief, or Taskbook for a fresh Executor. Probe facts repo/runtime can decide, return only Goal-changing choices to the Human, and leave implementation How to the Executor."
---

# Prompt Atlas · Settle Goal, then hand off

Three roles: the **Human** proposes the goal and makes Human-owned choices; **Prompt Atlas** researches, clarifies, and writes the Taskbook; the **Executor** takes the current Taskbook and independently decides implementation How. Prompt Atlas may inspect / probe reality, but it does not perform material Goal work or run a post-execution manager/acceptance loop.

- **Goal**: the result the Human will ultimately accept.
- **Taskbook**: the current task definition a fresh Executor needs before starting.
- **reality**: the current state of the repo and runtime.

A Taskbook keeps the causal chain `Goal → Execution → Verification → Evidence`, but it does not require a fixed Markdown template.

## Flow

**1. Research.** Start from the Human's latest still-valid wording. Recover the candidate Goal, then inspect reality that can change Goal, a binding constraint, or the first safe material work. The prompt, an old plan, and Prompt Atlas itself are only maps; repo/runtime, real consumers, authoritative specs, and the current workspace can correct them.

Do not ask the Human for facts you can determine. Reference authoritative tests/schema/ADR/Architecture Intent/acceptance scripts directly instead of rewriting them. Still-valid workspace changes are current reality; do not assume a clean state. Stop Research when more context would change only How. If the input is still only a problem space, Goal and How are hard to separate, a hidden constraint may matter, or requirements genuinely conflict, read [intent-shaping.md](references/intent-shaping.md).

**2. Ask.** Ask only for choices reality cannot decide and whose answer changes the Goal the Human will accept. Surface currently known Human-owned choices together when practical, explain what each changes, the main consequences, and a recommendation when useful. Probe factual questions yourself; leave implementation-only questions to the Executor.

The Human may answer only part, add a constraint, correct a premise, or interrupt. Treat the latest Human input as authoritative, preserve still-valid judgment, and reopen only what it affects. As soon as Goal is stable enough, continue writing rather than staying in acknowledgement, explanation, or delta-only mode because an Ask already happened. If the Human is unavailable and a choice must be made now, use an explicit default only when it is reversible and does not change Goal, allowed scope, Verification, or authorization, and preserve its basis.

**3. Write.** Once Goal is stable, write the complete current Taskbook. Keep only information whose omission would make a fresh Executor judge incorrectly, cross a boundary, or fail to prove completion. Remove Research narration, reliably recomputable inventory, file/symbol/line detail, and predicted patches by default.

Simple tasks finish directly. For long runs, several different judgments, real dependencies, work that only becomes knowable during execution, or continuation across sessions, read [execution-compile.md](references/execution-compile.md). Read [verification-trust.md](references/verification-trust.md) only when there is a concrete risk that the implementation is wrong while checks can still show PASS.

**4. Deliver.** If a choice still genuinely belongs to the Human, deliver those choices. If reality prevents safe continuation, state the blocker and resume condition. Otherwise return the complete current Taskbook and write **that same complete body** to an OS/runtime-provided authoritative Markdown file outside the repo/workspace, surfacing the actual path. The Executor starts from this file rather than reconstructing the task from conversation.

Taskbook delivery is not a completion state. Any later material Human clarification / correction reopens the affected judgment and fully re-delivers the current Taskbook. Update the current artifact when writable; otherwise create a new artifact and surface the new authoritative path. Do not emit ready / completed / executable / status tokens.

## Writing rules

**Goal outranks means.** A named architecture, tool, migration, provider, or implementation is a means by default. To decide whether it belongs in Goal, ask only: **would the Human still accept it if a materially different implementation satisfied the same requirement?** If yes, leave How to the Executor. If no, keep the corresponding result, boundary, risk commitment, or representation in Goal.

**Separate law from intelligence.** Only requirements truly bound by the Human, repo/upstream authority, or verified reality may become `must / must not`. A currently preferred implementation, Research conclusion, or high-confidence plan remains implementation intelligence; the Executor may replace it with a better compliant path. When Human requirements conflict, recover a real priority rather than silently choosing the option that makes implementation easier.

**Reference rich specs.** When an authoritative spec already expresses the requirement, link or reference it directly. Do not rewrite schema, tests, design constraints, or existing contracts into a second prose SOT.

**Keep Taskbook altitude.** Execution content should express **what must be true when done, the judgment to apply, responsibility boundaries, and real dependencies**. Do not default to a predicted-patch checklist such as `edit A → add B helper → update C caller → run D test`. Implementation detail becomes binding only when the representation itself is fixed by authority. If one judgment covers an open surface, write the judgment rather than freezing discovered instances into a closed checklist.

**Do not pre-slice an unknowable future.** If current reality supports only part of the Goal, shrink current work, not the Human's full Goal. Record only real dependencies that already change execution choice. Work that depends on future Evidence should be added only when it becomes real rather than turning what cannot yet be specified into speculative tasks. When new Evidence invalidates a premise, recompute only work and Verification that depended on it; still-valid work remains reusable.

**Split implementation and Verification independently.** Split implementation by result, judgment, and real dependency. Split Verification by completion claim, risk, and authoritative Evidence. They do not need a one-to-one mapping: one Verification may cover several implementation changes, and one implementation change may need several kinds of Evidence. Verification freezes what must be proven for Goal completion, not the Executor's debugging flow, and a test does not prove the Goal merely because it is close to the code change.

**Failure cannot masquerade as success.** Never manufacture PASS with skip/todo, weakened assertions, deleted live tests, mocked-away targets, swallowed failures, or `|| true`. For longer runs, use existing `implement-notes` for progress, key decisions/Evidence, blockers, and the resume point. A new session redoes only work whose premise changed or Evidence became stale; do not create a second Taskbook, persistent Graph, or manager state.

## Before delivery

1. Are Goal and means separated? Were Human-owned choices actually Asked while factual questions stayed with Research?
2. Does the Taskbook reference existing authority rather than create a second SOT? Does every `must / must not` have real authority?
3. Is execution still written at outcome / judgment / responsibility / dependency altitude rather than as a predicted patch checklist?
4. Did current safe work accidentally replace the full Goal? Was contingent future work guessed into tasks before Evidence made it real?
5. Were implementation granularity and Verification granularity designed independently? Does completion proof cover the real Goal without false-green shortcuts?
6. Was the successful Taskbook materialized as the same complete body to an authoritative file with the real path surfaced? After new Human input, was the complete current Taskbook delivered again rather than only a delta?
