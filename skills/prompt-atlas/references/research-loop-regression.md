# Research Loop Regression

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. It records one real execution case that exposed a general loop gap; it adds no runtime phase, state, budget, node, or FS-specific rule.

## R1 — Stable Goal exits Research instead of recursively discovering

The Human gives a clear executable cleanup Goal: an old subsystem is being retired and residual code in two directories should be cleaned up. Initial repo Evidence already distinguishes some clearly live shared code, some candidate residue, and several consumer / dependency / external-usage Unknowns that have not been exhausted.

Pass:

- Goal / authority is stable and ordinary implementation Unknown does not reopen Intent Take;
- Research closes only real pre-Handoff Compile blockers;
- once at least one safe Task or necessary Task 0 can be compiled and Verification authority / trigger is clear enough to leave concrete scope/provider/target to execution, stop Research and enter Compile/Run;
- deletion-relevant reachability for candidate residue may be a Task 0 or ordinary Executor probe;
- a new grep / dependency observation that only refines consumer, dependency, history, or implementation scope does not automatically reopen global Research;
- runtime Evidence adjusts only affected contingent / invalidated Execution / Verification.

Fail:

- every observation creates another “key question / real blocker / need to verify”;
- the compiler refuses to expose already-safe executable work because repo-external consumers, the full dependency graph, or historical paths have not been exhausted;
- an unsupported possibility such as “an external consumer might still exist” becomes a global blocker;
- Research becomes a recursive `inspect → new Unknown → inspect more` loop that prevents a clear Goal from reaching `Status: Executable`.

## Captured FS cleanup shape

This example exists only to reproduce the regression and must not become a runtime prior:

- `fea_lib` / `fea_util` contain both shared pieces still used by Hermes/model_server and old FS residue;
- the initial scan is already sufficient to preserve clearly live code and compile candidate-residue reachability as execution work;
- questions such as “does an external Flink UDF still consume libfs.so?” need Evidence before the affected deletion branch only when they actually prevent that branch from advancing safely; they do not require exhaustive repo-external knowledge before any cleanup begins.

## Claim boundary

This regression proves only that the candidate text expresses the intended Research-closure discriminator. Without a clean-session Skill runner / isolated model session, do not claim behavioral uplift; real behavioral A/B remains `NOT RUN`.
