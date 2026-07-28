# Execution readiness

Use this reference only when the contract must drive direct or autonomous work. Intent Take decides which protections are necessary; the selected carrier or harness decides their concrete filenames, protocol, and executor topology.

## Select the necessary protections

- **Reality** — inspect the task-relevant repo, target ref, worktree, tests, config, runtime, and rich specifications. Distinguish verified laws from suggested approaches.
- **Baseline** — measure one when regression, migration, performance, coverage, cleanup, or count-based completion depends on it. Never invent a command or number.
- **Write boundary** — when drift is costly, prefer an allowlist of writable paths and permitted new files; treat the rest as read-only and preserve existing user changes.
- **Autonomy** — leave routine implementation judgment open. Resolve user-owned direction changes before an unattended run or expose a default, its evidence state, and the cost of being wrong.
- **Proof** — use evidence that exercises the requested behavior. Carry or reference every applicable repo-owned verification gate whose omission could create false completion.
- **Integrity** — freeze any baseline the executor could game. Add narrow anti-shortcut or negative checks only for plausible false-green paths.
- **Continuity** — add resumable progress and blocker state only when work may outlive one context window.
- **Stop-loss** — set retry, time, round, or rollback limits when repeated failure could waste substantial effort or degrade a verified baseline.
- **Independent evaluation** — when another verifier exists, keep a small outcome-focused assessment outside the executor-visible contract.
- **Parallel safety** — only with user authorization; give workers the same intent, non-overlapping writes, an owned integration seam, and post-integration proof.

Execution work closes on an achieved result with proportional evidence. Exploration closes on a bounded decision or finding, not fake implementation metrics.

## Realize them in the selected carrier

- If intake cannot verify a required baseline but execution can safely start by checking it, make that check the first precondition or Task 0. State what a mismatch blocks; do not postpone discoverable requirement understanding.
- Include exact commands only after verifying them in the current environment. When a gate itself could be false-green, prove it can fail before accepting its passing result.
- A long-running carrier may use `PROGRESS.md` and `BLOCKED.md`; the semantics are current objective, completed evidence, next action, and unresolved dependency. A contradiction that invalidates the result stops the affected work rather than becoming a routine blocker.
- Do not accept a degraded result as completion: roll back or preserve the last verified baseline and report the gap honestly.
- A build alone does not prove behavior equivalence when replay, trace, runtime, or contract evidence is the real proof.
