# Autonomous Taskbook: compile a stable Goal into a minimum-sufficient execution contract

Use only after Goal is settled. The Taskbook must let a fresh Executor complete the Goal independently **without pre-writing the implementation for it**.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is compiler ownership / proof chain, not an output template. **Decision coverage must be complete; information coverage and patch coverage must not be.** Research may be deep; the Taskbook must compress it.

## Goal

Write one Human-owned Goal: desired result, confirmed boundary, must-preserve conditions, and final delivery. Include Why only when it changes tradeoffs. Explicit Human Verification requirements belong to Verification and are not duplicated back into Goal.

## Execution / Graph

The Taskbook normally keeps only a small number of **bounded work units**.

A Task should let the Executor independently advance under one coherent judgment to an observable outcome. Normally it needs only:

- the local outcome;
- applicability territory / starting reality only when omission would cause misjudgment;
- one stable judgment that repeatedly decides change / preserve / stop / branch;
- hard constraints that truly reduce the choice space;
- already-binding Verification obligations that determine whether the work is valid.

**A Task is not an executable delta and not a predicted patch.** Research finding one viable implementation does not make these details binding: exact file decomposition, symbol destination, line extraction, include/BUILD rewrites, command order, leaf-deletion order, or intermediate build/test steps used for failure localization. Freeze such How only when explicitly required by the Human, required by repo authority, required by real dependency/risk, or proven by Evidence to be the only safe route.

When many files/symbols/instances share one judgment, group them into one Task. Split only when outcome, dependency, authority, risk, or required Verification is genuinely different.

Graph expresses only real relationships that change execution judgment, such as dependency, parallel work units, shared writes, or joins that require combined Verification. Do not fragment work merely to make Graph more precise.

Preserve Human-confirmed strategy / scope boundary / must-preserve constraints. The ready frontier says what can execute now and does not redefine the Human Goal. Adjacent residual does not enter scope merely because it was discovered.

Still-valid workspace changes aligned with the Goal are starting reality. Reuse them; do not redo them or shrink the Goal around them. “Already changed” is not correctness Evidence.

**Task 0** exists only when a missing execution-time fact blocks the first safe material work, or required Verification explicitly requires a trigger before material work. It is not continued Research, an inventory, or a default checklist.

## Information compression

A Research finding does not automatically enter the Taskbook. Keep it only if it changes at least one of:

- Goal / boundary / must-preserve;
- a judgment the Executor will repeatedly apply;
- a work unit's real dependency / risk / authority;
- required Verification / Completion judgment;
- starting reality that cannot be safely rediscovered from the repo and whose loss would cause execution drift.

File line numbers, symbol counts, include details, candidate inventories, and known patch shapes that the Executor can safely rediscover from the repo are omitted by default. **More Evidence should compress into fewer, more reliable judgments—not more instructions.**

## Verification

Verification freezes **what must be proven**, not **how implementation/debugging should proceed** by default.

- Task — include a local check only when it is already binding and controls progression;
- Task Group / join — include separate proof only when combined behavior genuinely needs it;
- Goal — preserve delivery coverage required by repo authority or explicit Human requirements.

When provider, target, or scope depends on change surface / binding / runtime reality, compile the stable trigger/authority and let the Executor materialize the concrete action after it triggers. cleanup/refactor/expected `0-diff` cannot downgrade already-triggered required Verification.

Tactics such as “build after every moved type” or “test after every edited file” belong to the Executor by default. They become binding only when repo/Human authority or a specific risk requires them.

Read [verification-trust.md](verification-trust.md) only when judge trust genuinely needs strengthening.

## Evidence

Compile proof / trust requirements, not future results. Evidence needed for final judgment must be reviewable and cover the real claim. Executor narration or self-declared `PASS` is not Evidence. Reuse Evidence while its premises remain valid; new Evidence invalidates only affected conclusions.

## Completion Hook

The Taskbook carries a stop judgment without adding a Completion layer. It reads only **Goal / constraints + triggered required Verification + current valid Evidence**:

- whether the Goal's material outcome has minimum sufficient Evidence;
- whether must-preserve / confirmed boundaries / authority still hold;
- whether every triggered required Verification obligation has trustworthy Evidence.

If all hold, `STOP`. If a gap remains, continue existing work or materialize only contingent work that can close it. If no safe route remains, return accurate `BLOCKED`. An empty frontier or completed Tasks are not completion conditions by themselves.

## Handoff check

Before delivery, ask only:

- Does the Taskbook define the task instead of exposing Prompt Atlas research?
- Is each Task a bounded work unit rather than a file/function/patch step?
- Did one viable implementation get incorrectly promoted into a mandatory implementation?
- Are instances covered by one judgment grouped together?
- Does Graph contain only real execution relationships?
- Does Verification freeze required proof without turning debugging tactics into hard workflow?
- Have safely rediscoverable details that do not change judgment been removed?

If deleting a passage does not change the Executor's Goal, boundary, judgment, or completion condition, delete it.