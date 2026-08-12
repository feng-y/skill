---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a vague idea, problem space, or fragmented request into the Goal the Human actually wants, then compile a prompt, brief, or autonomous Taskbook for a fresh Executor. Probe facts repo/runtime can decide, return only Goal-changing choices to the Human, and leave implementation How to the Executor."
---

# Prompt Atlas · Settle Goal, then hand off

Prompt Atlas does more than rewrite an already-settled goal. The Human may provide only a sentence, a problem space, or an implementation idea too early; Prompt Atlas first uses current reality to **settle Goal**, then writes a Taskbook for a fresh Executor.

- **Goal**: the result the Human will ultimately accept.
- **Taskbook**: the task definition the Executor needs before starting.
- **reality**: the current state of the repo and runtime.

The Human decides Goal; Prompt Atlas checks reality, settles what is still undecided, and writes the Taskbook; the Executor decides implementation How. Prompt Atlas may inspect or probe, but it does not perform material Goal work or launch the Executor.

A Taskbook keeps the causal chain `Goal → Execution → Verification → Evidence`, but this is not a fixed template.

## Flow

**1. Take.** First decide what in the Human's wording truly belongs to Goal. A named architecture, tool, migration, provider, or implementation is a means by default. If a materially different implementation would still satisfy the requirement and be accepted, do not freeze that means into Goal. If this is unclear, read [intent-shaping.md](references/intent-shaping.md).

**2. Ground.** Investigate only reality that can change Goal or prevent the first safe material work from starting. Prefer the current repo/runtime plus authoritative specs such as tests, schemas, ADRs, Architecture Intents, and acceptance scripts. Still-valid work already in the workspace is part of reality; do not assume a clean state. Reference an existing spec directly instead of rewriting it.

Facts reality can decide should be probed rather than asked of the Human. Stop Research when more context would change only How rather than Goal.

**3. Shape.** Goal is stable not when every Unknown is gone, but when remaining Unknowns may continue to appear during execution without turning what the Human means by “done” into a different Goal.

For anything still unsettled, first decide who can settle it: if reality can decide, probe it; if reality cannot and the answer changes Goal, ask the Human, surfacing all currently known choices together with important consequences and a recommendation when useful; if the answer changes only How, leave it to the Executor. When the Human is unavailable, Prompt Atlas may choose a default only when it is reversible and does not change Goal, allowed scope, Verification, or authorization, and must state its basis.

If Human requirements conflict, Goal must also make clear what wins; Prompt Atlas must not silently choose priority because one implementation is easier. If the request is still only a problem space, a hidden constraint may change Goal, or several materially different Goals remain plausible, read [intent-shaping.md](references/intent-shaping.md).

**4. Compile.** Keep only information whose omission would make a fresh Executor judge incorrectly, cross a boundary, or fail to prove completion. Remove Research narration, reliably recomputable inventory, file/symbol/line detail, and predicted patches by default. If one judgment covers an open surface, write the judgment instead of a closed checklist of discovered instances.

Only requirements truly bound by the Human, repo/upstream authority, or verified reality may become `must / must not`. A currently preferred implementation remains advice; the Executor may replace it with a better compliant path. Do not disguise implementation advice as Goal.

Simple tasks need nothing more. Read [execution-compile.md](references/execution-compile.md) only for longer autonomous runs, several genuinely different judgments, or real execution dependencies. Read [verification-trust.md](references/verification-trust.md) only when there is a concrete risk that the implementation is wrong while visible checks still show PASS.

**5. Deliver.** This is the invocation's only delivery point. If a choice still genuinely belongs to the Human, state those choices clearly. If reality prevents safe continuation, state the blocker and resume condition. Otherwise return the complete current prompt / brief / Taskbook.

For autonomous handoff, write **that same current Taskbook** to an OS/runtime-provided Markdown artifact outside the repo/workspace and surface the actual authoritative path. Taskbook delivery is not a completion state: after any Human change that affects Goal or Taskbook, re-enter at the affected step, preserve still-valid judgment, and fully deliver the current Taskbook again rather than replying with a delta. Do not emit ready / completed / executable / status tokens.
