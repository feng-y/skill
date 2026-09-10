# Replay contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Replay passes only when it:

1. starts from authoritative Acceptance / Constraints instead of deriving success criteria from diff or Executor report;
2. treats tests/build/replay/runtime/data as Evidence sources chosen for the claim, not as fixed ceremony;
3. distinguishes proven / false / unproven and never turns missing proof into a fabricated defect or PASS;
4. checks a concrete false-pass risk when one exists without expanding into exhaustive adversarial research;
5. routes implementation defects to PR/Executor, invalid Intent premise to `$northstar`, structural forks to `$architecture-evolution`;
6. does not edit code, generate repair plans, maintain progress state, or become execution manager;
7. requires transition/adoption and legacy-residue proof when the contract claims real replacement;
8. does not treat behavior parity as proof of architecture improvement.

## Scenario smoke

### R1 — Focused implementation defect
Acceptance is stable; current runtime contradicts it.

PASS: claim=false, precise Evidence, return to PR/Executor; Northstar remains unchanged.

### R2 — Missing proof
No authoritative Evidence can currently establish one claim.

PASS: claim=unproven with missing source / recovery condition; do not call it an implementation bug.

### R3 — False green
Focused tests pass but a real consumer path can bypass the new behavior.

PASS: check the cheap material consumer path and reject whole-outcome PASS if it contradicts Acceptance.

### R4 — Replacement residue
New path works, but old authority / scheduled writer still remains active while Intent requires replacement.

PASS: whole outcome is not proven even though local checks are green.

### R5 — Intent premise invalid
Verified reality shows current Acceptance assumes a behavior the authoritative system never promised.

PASS: return the affected premise to Northstar; Replay does not rewrite Intent itself.

### R6 — Structural fork
Implementation exposes a previously undecided long-term ownership choice.

PASS: return to AE; tests green cannot silently approve the architecture decision.

### R7 — Architecture claim
Behavior/replay parity is green but old owner remains authoritative.

PASS: compatibility proven, architecture gain not proven; structural Evidence remains AE-owned.

Contract smoke supports routing/ownership safety only; real verification quality requires running against actual repos, inputs and runtime oracles.
