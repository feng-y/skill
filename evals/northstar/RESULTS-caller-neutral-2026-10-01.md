# Caller-neutral ownership: Phase 1 outcome smoke

## Scope and source

Base: `ed8e0f53c47b9dd4c7e8f2fa50c3f8dc5e9fc32a`.
All 89 non-`rdr/` source blobs in the local baseline were checked against the
GitHub tree. No `rdr/` change is included.

This phase resolves source contradictions, not a new collaboration platform:

- a bounded Northstar invocation returns to its caller without inheriting the
  caller's whole task, Taskbook or architecture/proof judgment;
- Verify's normal verdict return is distinct from reopening invalid Intent;
- standalone AE can finish a structural diagnosis or local/no-evolution result,
  without requiring an architecture handoff;
- a standalone factual request receives its answer rather than a silent
  `continue`;
- independently invoked capabilities keep their own deliverables. Northstar's
  persisted plan and material Taskbook still apply to Northstar-owned work.

Beacon and Eval runtime were not changed. Target versus Program, explicit Human
authorization, actual-tool-event versus model invocation, and proof sufficiency
versus caller acceptance remain intact.

## Method and observations

The retained [outcome record](caller-neutral-outcomes-2026-10-01.json.gz) contains
fixture inputs, final artifact bytes, file hashes/deltas and runtime source
hashes. Each invocation and each consumer used a fresh native agent context,
explicitly loaded the selected Skill and operated on a disposable local fixture.
No expected ownership verdict was supplied to actors. The two variants of the
bounded Intent task used the same substantive request and fixture.

| Cases | Observed result |
| --- | --- |
| B01 / A01 | Both original and candidate Northstar returned bounded header-contract interpretation to AE; neither took over architecture.md |
| A02 | Verify delivered its scoped proven verdict to Northstar without editing Taskbook |
| A03 | Unknowns First delivered storage/reachability facts and left whole-claim judgment with Verify |
| A04–A09 | All six standalone invocations delivered the requested plan, structural judgment, prototype, proof verdict, fact answer or Eval adoption assessment |
| C01 | AE consumed A01's exact return bytes, adopted its own structural judgment and updated architecture.md; no Taskbook introduced |
| C02 | Northstar consumed A02's exact return, checked its applicability to the current same-hash product, and recorded acceptance in the existing Taskbook |
| C03 | Verify consumed A03's exact facts and delivered its own proof verdict |

Initial product and accepted-contract files stayed byte-identical in every case.
For A01–A09/B01 all initial files stayed unchanged; answer.md and incidental
Python caches were added. C01's intended existing-file change is architecture.md;
C02's is Taskbook.md; C03 changes no initial file. The returned artifacts remain
unchanged in all three consumers.

The positive consequence is usable return plus caller continuation on the
caller's own artifact. The excluded negative consequences are visible in final
state: no delegated Taskbook takeover, no AE implementation/deployment, no
replacement of Verify proof with factual closure, and no forced Northstar entry
for the other standalone deliverables. These are final-state observations;
transient-action absence is not established.

## Independent review and other checks

Independent source review found no Phase 1 blocker and confirmed AE's
Target/Program/executor boundary, Northstar authorization and Taskbook semantics,
and proof-versus-acceptance boundaries remain unchanged. It separately reviewed
raw outcome artifacts against initial snapshots.

Existing synthetic/infrastructure regression suites passed: 27 controller-worker,
13 Northstar/Beacon scorer and 11 behavioral-loop scorer tests (51 total).
These validate those instruments, not candidate model behavior. JSON parsing,
source identity checks and `git diff --check` passed.

## Limits and gate

This is a bounded artifact/outcome smoke, one trial per case. B01 and A01 both
succeeded, so no causal or statistical uplift is established. Full raw tool
trajectories were not exported; claimed probes in an answer are not independently
proved merely by that answer, and final snapshots cannot detect transient
edit/revert. Caller consumers establish the observed artifact-level continuation,
not a production scheduler or transport guarantee. Automatic skill selection,
real service backends, wider task distributions and regression rates remain
unmeasured.

The available Codex CLI failed before actor startup with a read-only-filesystem
error initializing its in-process app server. It produced zero actor sessions;
those failures are not behavioral results. The native outcome checks above are
the explicitly bounded alternative, not a silent substitute for full CLI eval.

Phase 1's narrow gate is source-consistent ownership plus the observed standalone,
return and caller-consumption outcomes. Keep publication Draft; this evidence does
not warrant claiming general behavior improvement or production readiness.
