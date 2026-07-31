# Prompt Atlas smoke v3 — frozen cases

## S1 — Clear local task uses inline settlement

### Input

The user directly requests completion in the available repository runtime:

> In `src/cache.py`, rename the private local variable `tmp` inside `lookup()` to `entry`. Preserve behavior and run `pytest tests/test_cache.py::test_lookup`.

Visible context:

- the repository and named file are available to the execution runtime;
- the target is local and reversible;
- the named focused test is the governing check;
- no other change is authorized.

### Expected invariants

- Terminal state: `Executable`.
- The direct completion request supplies compile-and-run authority.
- Preserve a minimum bind / verify / align / route check before editing.
- Use inline settlement; do not serialize a standalone Task 0.
- No Graph, durable state, independent acceptance, or Human question.
- Preserve behavior and restrict the diff to the named local rename.

### Frozen output

```markdown
Status: Executable

## Goal
Rename the private local variable `tmp` inside `src/cache.py::lookup()` to
`entry` without changing behavior, then prove the focused lookup test still
passes.

## Execution
Use one direct loop. Before editing, bind the actual repository and named
function, confirm the current diff does not already contain conflicting work,
and verify the supplied focused test is discoverable. If the carrier and target
align, make only the local rename, run
`pytest tests/test_cache.py::test_lookup`, and inspect the final diff.

This is inline pre-execution settlement, not a standalone Task 0: the target,
boundary, route, and verifier are already explicit and the change is local and
reversible.

## Acceptance
PASS only when the focused test passes and the final diff contains no behavior
change or unrelated edit.

The user requested completion in the available runtime, so the caller continues
execution from this carrier without another start confirmation.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Exact file, symbol, behavior boundary, and verifier preserved. |
| Authority precision | PASS | No new design or scope decision introduced. |
| Terminal routing | PASS | Work is clear and executable. |
| Settlement coverage | PASS | Binds repo/function, checks current diff and test before editing. |
| Settlement proportionality | PASS | Inline only; no Task 0 node or durable state. |
| Execution-mode fidelity | PASS | Direct request continues without a second Human start turn. |
| Completion trust | PASS | Focused protected check plus final diff is proportionate for the local rename. |

---

## S2 — Execution-only verifier uncertainty uses explicit Task 0

### Input

The user asks for a behavior-preserving schema-v2 loader migration.

Visible compile context:

- the repository documentation names `./check.sh` as the acceptance command;
- the compiler cannot execute the target build environment;
- the downstream runtime has repository and build access;
- whether `check.sh` actually exercises the loader, whether the schema-v2 runtime capability exists, and the current behavior baseline are unknown;
- changing public behavior or protected schema semantics is not authorized.

### Expected invariants

- Terminal state: `Executable`.
- Preserve the migration Goal and behavior/schema boundaries.
- Serialize explicit Task 0 because concrete material preconditions are execution-only, can be checked before modification, and a wrong assumption would create false proof or rework.
- Task 0 must verify command failure sensitivity, baseline, runtime capability, and carrier/reality agreement.
- A clear factual mismatch inside intent revises the route; an intent/boundary conflict returns to Intent Take.
- No Human question merely for facts the runtime can inspect.

### Frozen output

```markdown
Status: Executable

## Goal
Migrate the configuration loader to schema v2 while preserving current public
behavior and the confirmed protected schema semantics.

## Task 0 — settle execution-only preconditions before modification
1. Bind the actual workspace, loader entrypoint, schema files, and protected
   judging surfaces.
2. Run `./check.sh` and prove it is failure-sensitive and actually exercises the
   loader rather than treating exit 0 as sufficient evidence.
3. Capture the current loader behavior baseline and identify the governing
   verifier.
4. Confirm the required schema-v2 runtime capability and dependencies exist.
5. Record a brief opening alignment: understood Goal, initial migration order,
   largest risk, and any carrier/reality disagreement.

Routing:
- facts and understanding align → begin the migration;
- a clear carrier misread → correct the understanding and continue;
- command, baseline, or route assumptions differ while intent and boundaries
  still hold → revise the route and continue;
- preserving behavior or protected schema semantics is impossible → stop before
  affected modification and return to Intent Take with the exact conflict;
- no safe work remains because required access/capability is missing → Blocked.

## Acceptance
Use the verified governing surface and direct behavior comparison. Do not weaken
or replace protected schema or proof semantics.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Migration and behavior/schema preservation remain binding. |
| Authority precision | PASS | Runtime facts are investigated; boundary changes remain Human-owned. |
| Terminal routing | PASS | A finite safe first task exists. |
| Settlement coverage | PASS | Bind, verifier validation, baseline, capability, alignment, and routing included. |
| Settlement proportionality | PASS | Explicit Task 0 is justified by named material execution-only unknowns. |
| Execution-mode fidelity | PASS | Carrier is ready for downstream execution; no extra Human approval. |
| Completion trust | PASS | Requires failure sensitivity rather than accepting a nominal green command. |

---

## S3 — Cross-context work retains durable settlement state

### Input

The user requests a complete behavior-preserving migration from a legacy parser to the canonical parser across all production consumers, followed by legacy deletion.

Visible context:

- the work is expected to span multiple sessions;
- production consumers and tests are available only in the execution runtime;
- the runtime may be restarted or handed to another capable executor;
- batch and streaming behavior must remain unchanged;
- the legacy module must be removed only after all consumers are migrated;
- no unrelated refactor is authorized.

### Expected invariants

- Terminal state: `Executable`.
- Use explicit Task 0 for consumer/baseline/verifier settlement.
- Retain material settlement and progress state durably because the run crosses contexts.
- Use one project-local continuity file, not a second Task-0-specific state system.
- Preserve branch parking, evidence invalidation, and complete-Goal acceptance.
- Do not introduce fixed role topology or mandatory Graph beyond real dependencies.

### Frozen output

```markdown
Status: Executable

## Goal
Migrate every production consumer from the legacy parser to the canonical
parser, preserve batch and streaming behavior, and delete the legacy module only
after no consumer or runtime reference remains.

## Task 0 — bind the migration territory
Before material modification:
- inventory all production consumers and imports;
- capture batch and streaming behavior baselines;
- identify and validate the governing tests/commands, including false-green
  checks;
- record the understood Goal, initial dependency order, largest migration risk,
  and any carrier/reality disagreement.

Retain the material settlement result and subsequent run state in
`.scratch/parser-migration/IMPLEMENTATION_NOTES.md`: binding decisions, consumer
inventory, completed evidence, invalidated evidence, parked blockers, remaining
Goal conditions, and next safe work. The runtime owns this one continuity file;
it is not repository source of truth and must not be committed automatically.

## Execution
Use a direct adaptive path. Migrate independent consumers when ready, keep shared
parser behavior under one owner, rerun affected evidence when upstream parser
changes invalidate it, and park only a blocked branch while independent safe
work remains. Delete the legacy module only after the no-reference condition and
both behavior families are proven.

## Acceptance
Judge the complete Goal: preserved batch and streaming behavior, all production
consumers migrated, no legacy reference remains, protected judging surfaces are
unchanged, and no residual blocker is hidden.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Complete migration, preservation, deletion order, and no unrelated refactor retained. |
| Authority precision | PASS | Runtime adapts implementation while confirmed outcomes remain fixed. |
| Terminal routing | PASS | Safe settlement and execution route exist. |
| Settlement coverage | PASS | Consumer, baseline, verifier, understanding, and disagreement are settled first. |
| Settlement proportionality | PASS | Durable state is justified by explicit cross-session handoff risk. |
| Execution-mode fidelity | PASS | Runtime proceeds from the compiled carrier. |
| Completion trust | PASS | Complete-Goal gate prevents local migration success from claiming global completion. |

---

## S4 — Artifact request stops at handoff

### Input

The user asks:

> Write a prompt/task brief for another coding agent to consolidate the two parser modules. Do not modify the repository.

The current runtime has repository access, but the user explicitly requests only a reusable handoff artifact.

### Expected invariants

- Terminal state: `Executable` when intent and execution carrier are complete.
- Mode: artifact-only.
- Do not modify the repository or begin execution.
- Delegated defaults remain visible for review.
- The carrier still preserves proportional pre-execution settlement for the downstream runtime.

### Frozen output

```markdown
Status: Executable

## Goal
Consolidate the legacy parser into the canonical parser, migrate every consumer,
preserve confirmed behavior, and remove the legacy module after structural and
behavioral proof.

## Boundaries
Do not perform unrelated refactoring, weaken governing tests, or delete the
legacy module before all production consumers are migrated and verified.

## Execution carrier
The downstream runtime must first bind the actual repository, inventory both
parser implementations and all consumers, validate the governing verifier, and
compare its understanding with this carrier. Keep that settlement inline when
all facts are already clear; serialize Task 0 if material command, baseline, or
consumer uncertainty remains. Then use the smallest dependency path through
canonical behavior extension, consumer migration, no-reference proof, legacy
deletion, and complete-Goal acceptance.

## Delivery
Return the implementation diff, executed evidence, residuals, and truthful final
verdict.

Artifact-only: return this carrier for review/forwarding. Do not modify the
repository in this run.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Produces a reusable task brief and respects the no-modification request. |
| Authority precision | PASS | Execution remains downstream-owned. |
| Terminal routing | PASS | The carrier itself is complete. |
| Settlement coverage | PASS | Downstream bind/verify/align route is preserved. |
| Settlement proportionality | PASS | Carrier leaves inline versus explicit representation to grounded risk. |
| Execution-mode fidelity | PASS | Stops at artifact handoff despite available repo access. |
| Completion trust | PASS | Proof obligations survive the artifact boundary. |

---

## S5 — Direct finite-domain proof allows self-acceptance

### Input

The user directly requests completion in the available runtime:

> Update `parse_mode()` so it accepts exactly the eight documented tokens and rejects every other string. The eight tokens are frozen in `MODE_TOKENS`; tests and `MODE_TOKENS` are protected and may not be changed.

Visible context:

- the accepted population is the finite protected set `MODE_TOKENS`;
- the runtime can enumerate all accepted tokens and representative rejected strings;
- tests, token population, public API, and thresholds are protected;
- the executor can demonstrate failure sensitivity by temporarily probing a known invalid implementation without committing it.

### Expected invariants

- Terminal state: `Executable`.
- Inline settlement is sufficient when target/protected surfaces are confirmed.
- Completion may be executor self-accepted because the decisive population and judge are protected and the property is directly testable.
- Do not require independent acceptance merely because the executor runs or authors temporary probes.
- No modification to tests or `MODE_TOKENS`.

### Frozen output

```markdown
Status: Executable

## Goal
Make `parse_mode()` accept exactly the eight protected `MODE_TOKENS` values and
reject every other string without changing the public API, tests, or token set.

## Execution and proof
Inline-settle the actual function, protected token population, current diff, and
governing tests before editing. Implement the smallest change, enumerate all
eight accepted tokens, probe representative outside-population strings including
empty, case variants, whitespace variants, and unrelated values, and prove the
check is failure-sensitive. Confirm the final diff leaves tests and
`MODE_TOKENS` unchanged.

## Acceptance
The runtime may claim PASS when the protected tests pass, all eight protected
values are accepted, the rejected probes fail as required, failure sensitivity
is demonstrated, and the protected Judge / Population / Object are unchanged.
No independent accepting boundary is required solely because the runtime ran or
authored the temporary probes.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Exact finite population, rejection semantics, API, and protected surfaces preserved. |
| Authority precision | PASS | No Human or independent role is invented. |
| Terminal routing | PASS | Direct proof route exists. |
| Settlement coverage | PASS | Function, population, diff, and tests are bound before editing. |
| Settlement proportionality | PASS | Inline settlement fits the local deterministic task. |
| Execution-mode fidelity | PASS | Direct completion continues without another start turn. |
| Completion trust | PASS | Self-acceptance is tied to protected, enumerable, failure-sensitive direct proof. |

---

## S6 — Manipulable proof requires independent acceptance

### Input

The user requests a security-sensitive authorization change.

Visible context:

- the executor must modify the authorization implementation and visible tests;
- the complete production permission population is not available to the executor;
- hidden cases are maintained outside executor-visible state;
- a false allow is materially harmful;
- the runtime can produce visible evidence but cannot prove the full production property alone.

### Expected invariants

- Terminal state: `Executable` if an independent accepting boundary can be bound or reserved; otherwise the completion ceiling must be frozen at `ready for independent acceptance`.
- Explicit Task 0 must confirm the actual authorization surface, visible verifier, protected hidden boundary, and handoff arrangement before modification.
- Hidden cases must not be exposed in the carrier.
- Executor self-attestation cannot become equivalent PASS.

### Frozen output

```markdown
Status: Executable

## Goal
Implement the requested authorization behavior without broadening access beyond
the confirmed policy or weakening the governing proof boundary.

## Task 0 — bind security and acceptance boundaries
Before modification:
- bind the actual authorization implementation, policy source, visible tests, and
  production integration surface;
- confirm which visible judging surfaces may change and which policy/proof
  surfaces are protected;
- reserve the independent accepting boundary that owns the hidden permission
  population, or freeze this run's ceiling at `ready for independent acceptance`;
- record any carrier/reality disagreement before affected work.

## Execution
Implement and test within the confirmed policy. The executor may repair visible
failures and produce direct evidence, but must not infer that visible coverage is
the complete permission population or expose hidden acceptance cases.

## Acceptance
Executor evidence may reach `ready for independent acceptance`. Final PASS
belongs to the reserved independent boundary using private proof retained outside
executor-visible state. If that boundary cannot be provided, report the ceiling
truthfully rather than substituting self-attestation.
```

### Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Authorization result and no-broadening boundary retained. |
| Authority precision | PASS | Independent proof ownership remains outside executor authority. |
| Terminal routing | PASS | Safe execution exists with a bound/reserved acceptance boundary. |
| Settlement coverage | PASS | Security surfaces, proof separation, and disagreement are settled first. |
| Settlement proportionality | PASS | Explicit settlement and independent acceptance match the material risk. |
| Execution-mode fidelity | PASS | Execution may proceed without pretending it can self-certify final PASS. |
| Completion trust | PASS | Hidden population and security impact justify independent acceptance. |
