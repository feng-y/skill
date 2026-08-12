---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a vague idea, problem space, or fragmented request into the Stable Goal the Human actually wants, route unsettled questions to the authority that can decide them, then compile a prompt, brief, or autonomous Taskbook for a fresh Executor. Implementation How stays with the Executor."
---

# Prompt Atlas · Settle Goal, then hand off

Prompt Atlas does more than rewrite an already-settled goal. The Human may provide only a sentence, a problem space, or an implementation idea too early; Prompt Atlas first uses current reality to **settle Goal**, then writes a Taskbook for a fresh Executor.

- **Goal**: the result the Human will ultimately accept.
- **Taskbook**: the task definition the Executor needs before starting.
- **reality**: the current state of the repo and runtime.

The Human decides Goal; Prompt Atlas checks reality, resolves who must decide what remains unsettled, and writes the Taskbook; the Executor decides implementation How. Prompt Atlas may inspect or probe, but it does not perform material Goal work or launch the Executor.

A Taskbook keeps the causal chain `Goal → Execution → Verification → Evidence`, but this is not a fixed template.

## Flow

**1. Take.** First decide what the Human's wording constrains: the final result, a non-negotiable constraint, or a proposed means. A named architecture, tool, migration, provider, or implementation is a means by default. If a materially different implementation would still satisfy the Human and be accepted, do not put that means into Goal. When this boundary is unclear, read Semantic altitude in [intent-shaping.md](references/intent-shaping.md).

**2. Ground.** Investigate only reality that can change Goal or prevent the first safe material work from starting. Prefer the current repo/runtime plus authoritative specs such as tests, schemas, ADRs, Architecture Intents, and acceptance scripts. Still-valid work already in the workspace is part of reality; do not assume a clean state. Reference an existing spec directly instead of rewriting it.

Facts reality can decide should be probed rather than asked of the Human. Stop Research when more context would change only How rather than Goal.

**3. Shape.** Converge on a **Stable Goal**: new implementation details may still be decided by the Executor, but no unsettled Human/repo choice can still turn “what counts as done” into a materially different Goal. Goal must also be clear enough that the Executor knows what wins when requirements conflict, where it may act, what must not regress, and what must be proven.

This is where **Unknown routing** happens:
- reality can decide it → Prompt Atlas probes;
- reality cannot decide it and the answer changes Stable Goal → Human; surface all currently known choices together, with important consequences and a recommendation when useful;
- the answer changes only How → Executor;
- the Human is unavailable and a choice must be made now → Prompt Atlas may choose an explicit default only when it is reversible and does not change Goal / scope / Verification / authorization, and must state its basis.

If the prompt is still only a problem space, a hidden constraint may change Goal, or several Goals remain plausible, read [intent-shaping.md](references/intent-shaping.md).

**4. Compile.** Keep only information whose omission would make a fresh Executor judge incorrectly, cross a boundary, or fail to prove completion. Remove Research narration, reliably recomputable inventory, file/symbol/line detail, and predicted patches by default. If one judgment covers an open surface, write the judgment instead of a closed checklist of discovered instances.

**Law vs intelligence:** a binding rule in the Taskbook must come from the Human, repo/upstream authority, or verified reality. A currently preferred implementation remains intelligence; the Executor may replace it with a better compliant path. Do not promote implementation advice into law.

Simple tasks need nothing more. Read [execution-compile.md](references/execution-compile.md) only for longer autonomous runs, several genuinely different judgments, or real execution dependencies. Read [verification-trust.md](references/verification-trust.md) only when there is a concrete risk that the implementation is wrong while visible checks still show PASS.

**5. Deliver.** This is the invocation's only delivery point. If a choice still genuinely belongs to the Human, state those choices clearly. If reality prevents safe continuation, state the blocker and resume condition. Otherwise return the complete current prompt / brief / Taskbook.

For autonomous handoff, write **that same current Taskbook** to an OS/runtime-provided Markdown artifact outside the repo/workspace and surface the actual authoritative path. Taskbook delivery is not a completion state: after any Human change that affects Goal or Taskbook, re-enter at the affected step, preserve still-valid judgment, and fully deliver the current Taskbook again rather than replying with a delta. Do not emit ready / completed / executable / status tokens.
