# Verification Trust

Read only when visible Verification has a **concrete and material false-green / gameability / independence risk**. Normal Verification scope, provider triggers, and Evidence freshness/reuse belong to [execution-compile.md](execution-compile.md); this file owns only whether a PASS can be trusted.

## Trust question

Without a binding independence requirement, ask only:

> Is there a concrete failure mode where Goal / required Verification is not actually satisfied, yet the Executor can still obtain visible PASS?

If not, stop adding trust machinery. General uncertainty, incomplete exploration, or “more verification feels safer” is not a trust gap.

Material gaps include a judge that does not observe the target, an oracle the Executor can modify or bypass, fixed samples that can be overfit, failures that do not propagate, or decisive Evidence that exists only as implementer self-report.

## Judge integrity

Unless Human/repo authority explicitly permits it while preserving equivalent trusted proof, do not manufacture PASS through skip/todo, weakened assertions or coverage, deleting live tests, mocking away the real target, lowering thresholds, swallowing failure propagation, or modifying the acceptance judge.

When a key judge may be empty, false-green, or silently broken, inject one controlled local failure to prove the failure signal, restore it, then run normal Verification. This reverse check proves judge sensitivity only; it does not replace Goal behavior Evidence.

## Additional trust Evidence

Add only the minimum Evidence that directly attacks the concrete gap:

- **isolated/private check**: derived from the same public Goal / Verification requirement and adds no hidden requirement; it must be created before execution and stay isolated to retain private-evidence value;
- **independent Evidence**: when a decisive claim cannot be trusted from the implementation chain itself, a non-implementing subject re-obtains Evidence in the authoritative environment. Using the same model/provider neither proves nor disproves independence by itself.

These do not form a fixed Acceptance workflow and are not required for every task. If necessary trust Evidence cannot be obtained, report the evidence gap accurately rather than downgrading it into PASS.
