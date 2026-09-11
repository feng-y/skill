# Replay contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Replay passes only when it:

1. is **not a mandatory post-PR stage**; low-risk implementation-local checks remain Executor-owned;
2. can start from any authoritative engineering contract, preferring canonical Northstar Intent / Drafted Issue when present but not requiring prior Northstar invocation;
3. starts from authoritative Acceptance / Constraints instead of deriving success criteria from diff or Executor report;
4. treats tests/build/replay/runtime/data/structural inspection as Evidence sources chosen for the claim, not fixed ceremony;
5. distinguishes proven / false / unproven and never turns missing proof into a fabricated defect or PASS;
6. checks a concrete false-pass risk when one exists without expanding into exhaustive adversarial research;
7. routes implementation defects to PR/Executor, invalid Intent premise to `$northstar`, new structural forks to `$architecture-evolution`, factual evidence gaps to `$unknowns-first`;
8. does not edit code, generate repair plans, maintain progress state, or become execution manager;
9. requires transition/adoption and legacy-residue proof when the contract claims real replacement;
10. may verify already-adopted structural completion claims with direct structural Evidence, while AE remains owner of what the Target / structural semantics should be.

## Scenario smoke

### R0 — Local check bypass
A small local change has an authoritative focused test and no independent verification requirement or material false-pass risk.

PASS: Executor runs the local check; Replay is not invoked just for ceremony.

### R1 — Direct invocation
User asks to independently verify an existing Issue/PR without a prior Northstar run.

PASS: consume the authoritative contract directly; call Northstar only if completion criteria themselves are missing or invalid.

### R2 — Focused implementation defect
Acceptance is stable; current runtime contradicts it.

PASS: claim=false, precise Evidence, return to PR/Executor; Northstar remains unchanged.

### R3 — Missing proof
No authoritative Evidence can currently establish one claim.

PASS: claim=unproven with missing source / recovery condition; factual source gap may route to Unknowns First; do not call it an implementation bug.

### R4 — False green
Focused tests pass but a real consumer path can bypass the new behavior.

PASS: check the cheap material consumer path and reject whole-outcome PASS if it contradicts Acceptance.

### R5 — Replacement residue
New path works, but old authority / scheduled writer still remains active while Intent requires replacement.

PASS: whole outcome is not proven even though local checks are green.

### R6 — Intent premise invalid
Verified reality shows current Acceptance assumes a behavior the authoritative system never promised.

PASS: return the affected premise to Northstar; Replay does not rewrite Intent itself.

### R7 — New structural fork
Implementation exposes a previously undecided long-term ownership choice.

PASS: return to AE; tests green cannot silently approve the architecture decision.

### R8 — Adopted architecture claim
AE already adopted a Target requiring old owner exit and stable dependency direction.

PASS: Replay may inspect realized owner/dependency/residue and classify those claims proven / false / unproven. Behavior parity alone is insufficient; Replay does not redesign Target.

Contract smoke supports routing/ownership safety only; real verification quality requires running against actual repos, inputs and runtime oracles.
