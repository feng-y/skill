# Prompt Atlas PR #20 smoke artifacts

## S1 — simple local edit

```markdown
Status: Executable

## Contract Header
This taskbook is the execution source. Goal: rename the specified private local
variable without changing behavior. Completed world: the rename is present, the
focused test passes, and the diff contains no unrelated change. Declared delivery:
one code change plus evidence. Priority: behavior preservation, then requested
rename, then minimal diff. “Must” is binding; implementation suggestions are
guidance.

## 1. Delegated Decisions
None.

## 2. Boundaries and Authority
Modify only the named occurrence and any directly required same-scope reference.
Do not change public names, behavior, tests, or tooling. The Executor owns the
mechanical rename and local cleanup inside that boundary.

## 3. Current Reality and Task 0
The file, occurrence, focused test command, and success condition are supplied.
No Task 0 is needed; do not repeat discovery ceremonially.

## 4. Execution
### Task 1 — rename and verify
Rename the private local variable, run the supplied focused test, and inspect the
diff. PASS when the test succeeds and the diff contains only the intended rename.

## 5. Execution Rules and Continuity
Do not weaken or skip the focused test. Record only a material deviation or
blocker in the existing implementation note, if one exists.

## 6. Completion and Acceptance
PASS requires the focused test output and a clean minimal diff. Report the changed
file, test result, and any residual; activity narration is not evidence.
```

## S2 — real fork and join

```markdown
Status: Executable

## Contract Header
This taskbook is the execution source. Goal: make the canonical parser the only
parser, migrate batch and streaming consumers while preserving both behavior
families, then remove the legacy parser. Completed world: all consumers use the
canonical interface, legacy code and references are gone, and complete behavior
acceptance passes. Declared delivery: one integrated migration. Priority:
behavior preservation, canonical ownership, complete migration, then minimal
diff. Hard boundaries are binding; implementation details remain guidance.

## 1. Delegated Decisions
- Decision: use separate batch and streaming migration Tasks after the canonical
  interface is settled.
- Default: allow them to run in parallel because their write surfaces are
  disjoint.
- Basis: both consume the same settled interface but do not need each other’s
  implementation result.
- Cost if wrong: merge conflict or stale evidence.
- Detection/rollback: stop parallel work if ownership overlaps; serialize the
  affected Task and rerun its verification.

## 2. Boundaries and Authority
The canonical parser implementation has one owner. Batch-consumer paths and
streaming-consumer paths have separate write ownership. The legacy module may be
deleted only after both migrations pass. Tests, schemas, and acceptance scripts
are protected. The Executor may choose the canonical API How inside the confirmed
behavior contract.

## 3. Current Reality and Task 0
Before material change, bind the workspace, verify the current consumers and
protected commands, capture batch and streaming baselines, and confirm the write
surfaces are actually disjoint. If reality differs but Goal and boundaries hold,
revise the ordering; if preserving behavior requires a boundary change, return to
Intent Take before affected modification.

## 4. Execution
### Task 1 — settle canonical behavior
Extend the canonical parser to cover the confirmed batch and streaming semantics.
Verify both direct behavior families. PASS freezes the interface consumed by
Tasks 2 and 3.

### Task 2 — migrate batch consumers
Depends on Task 1. Own only batch-consumer paths. May run in parallel with Task 3.
Verify all batch consumers against the preserved baseline. If Task 1 later changes
the consumed interface or behavior, this evidence is invalid and must be rerun.

### Task 3 — migrate streaming consumers
Depends on Task 1. Own only streaming-consumer paths. May run in parallel with
Task 2. Verify trace and streaming behavior against the preserved baseline. If
Task 1 later changes the consumed interface or behavior, this evidence is invalid
and must be rerun.

### Task 4 — remove legacy code and close the migration
After both Tasks 2 and 3 pass, delete the legacy parser and remove all remaining
references. Re-run complete batch, streaming, structural, and protected baseline
acceptance after integration. Only this complete result may close the Goal.

## 5. Execution Rules and Continuity
One implementation note records material replans, ownership changes, invalidated
evidence, and blockers. Do not allow concurrent writes to the same mutable
surface. Local Task PASS unlocks dependent work but is not complete-Goal PASS.

## 6. Completion and Acceptance
PASS requires Tasks 1–4 integrated, zero legacy references, preserved batch and
streaming behavior, protected judges unchanged, and complete acceptance rerun
after the final integration. Report actual evidence and exact residuals.
```

## S3 — broad but linear migration

```markdown
Status: Executable

## Contract Header
This taskbook is the execution source. Goal: apply the confirmed schema-key rename
to all twenty named config files without changing values or unrelated structure.
Completed world: every target uses the new key, no old key remains in scope, and
the repository validator passes. Declared delivery: one repository-wide config
migration. Priority: semantic preservation, complete target coverage, then minimal
diff. Hard rules bind; edit order is guidance.

## 1. Delegated Decisions
None.

## 2. Boundaries and Authority
Write only the twenty named config files. Do not change schema meaning, values,
validator code, or unrelated formatting. The Executor owns edit order.

## 3. Current Reality and Task 0
The target set, exact rename, and validator are supplied. Verify the target set and
validator once before modification; no broader discovery or topology is needed.

## 4. Execution
### Task 1 — apply the complete rename
Update the twenty files, search the declared scope for the old key, run the
repository-wide validator, and inspect the aggregate diff. PASS when all targets
use the new key, the old key is absent in scope, values are unchanged, and the
validator succeeds.

## 5. Execution Rules and Continuity
Keep one linear pass and one aggregate verification. Do not split the work into
independent execution contracts merely because many files are involved.

## 6. Completion and Acceptance
PASS requires complete scope coverage, validator output, and a diff proving no
value or unrelated-format drift. Report residual files exactly if non-PASS.
```

## S4 — branch-local blocker

```markdown
Status: Executable

## Contract Header
This taskbook is the execution source. Goal: complete all provider-independent
migration preparation now while preserving the unavailable optional-provider
branch and its exact resolving condition. Completed world: safe inventory and
baseline work is delivered, the blocked branch is not falsified as complete, and
continuation is explicit. Declared delivery: bounded safe progress plus blocker
record. Priority: truthfulness, safe progress, then speed.

## 1. Delegated Decisions
- Decision: park the optional-provider branch instead of globally blocking.
- Default: continue provider-independent work.
- Basis: the missing credential affects only that branch.
- Cost if wrong: supposedly independent work may rely on provider-specific facts.
- Detection/rollback: Task 0 checks that dependency; stop affected work if found.

## 2. Boundaries and Authority
Do not fabricate provider results or broaden credentials. Inventory and baseline
capture may proceed only where they do not require the unavailable provider.

## 3. Current Reality and Task 0
Confirm which actions are provider-independent. Record the optional-provider
blocker as: missing credential, affected branch, attempted access, and resolving
condition. If no safe independent work remains, route to `Status: Blocked`;
otherwise continue.

## 4. Execution
### Task 1 — inventory independent consumers
Produce the complete provider-independent consumer inventory and verify its scope.

### Task 2 — capture protected baselines
Depends only on the available environment and may proceed while the provider
branch is parked. Record commands, outputs, and evidence limits.

### Parked branch — optional provider
Do not execute or claim PASS. Resume only when the named credential is available,
then run its governing verifier before integration.

## 5. Execution Rules and Continuity
Keep the blocker and safe evidence in one implementation note. Do not convert a
branch-local blocker into a Human intent question or global failure while Tasks 1
or 2 remain safe.

## 6. Completion and Acceptance
This bounded delivery passes when Tasks 1 and 2 are complete and the parked branch
has an exact, truthful resolving condition. The overall provider migration remains
non-PASS until the parked branch is resumed and accepted.
```

## S5 — confused architecture request

```markdown
Status: Unresolved Intent

Current understanding:
- “Improve the parser architecture” could mean removing duplicate implementation
  while preserving the API, redesigning the public API, or producing only a
  design recommendation.
- These outcomes grant different authority, produce different deliveries, and
  have different acceptance conditions.

Human decision needed:
Choose the Goal for this pass:
1. Consolidate implementation while preserving public behavior and API.
2. Redesign the public API and migrate consumers.
3. Produce a decision-ready architecture recommendation without implementation.

Recommendation: choose 1 when the immediate problem is duplication. Do not emit
an executable taskbook until the owned outcome is selected.
```

## S6 — false-green acceptance

```markdown
Status: Executable

## Contract Header
This taskbook is the execution source. Goal: implement the complete requested
discount semantics while preserving the public `final_price` API. Completed
world: valid fraction and percentage inputs normalize correctly, all prohibited
inputs fail, and protected files remain unchanged. Declared delivery: one code
change plus trustworthy evidence. Priority: runtime semantics, input rejection,
API preservation, then minimal diff.

## 1. Delegated Decisions
None.

## 2. Boundaries and Authority
Do not modify tests, `check.sh`, public API shape, or dependencies. The Executor
owns implementation How only. Protected judges and the requested input population
may not be weakened or narrowed.

## 3. Current Reality and Task 0
The implementation currently coerces values with `float`. Public tests cover only
the fraction path. `check.sh` always prints success and exits zero, so it is a
protected required command but not proof. No additional Task 0 discovery is
needed.

## 4. Execution
### Task 1 — implement and prove the semantics
Implement the smallest type, finiteness, range, and normalization change. Run the
protected public commands, then direct probes covering all valid boundaries and
invalid type/value families. Prove failure sensitivity with a bounded known-bad
case or equivalent reverse validation, restore normal state, and rerun the proof.
PASS at this Task means implementation evidence is ready for an independent
accepting boundary.

## 5. Execution Rules and Continuity
Do not edit or bypass the judges, swallow failures, reduce the population, or
replace the real implementation with a mock. Record actual outputs and any
compromised proof.

## 6. Completion and Acceptance
The Executor ceiling is `ready for independent acceptance` because the public
suite omits most requested behavior and executor-authored probes cannot
self-certify global PASS. A non-implementing Acceptor must independently rerun the
full edge/type matrix, confirm the API and protected files, and report PASS or the
exact residual. Reserved private-check contents are not included in this taskbook.
```
