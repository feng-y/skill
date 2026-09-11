# Architecture Evolution contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Architecture Evolution passes only when it:

1. keeps Target Architecture judgment and current Evolution Program as distinct internal responsibilities without requiring two top-level Skills;
2. can be invoked directly from an engineering request / existing Intent; prior Northstar invocation is not mandatory;
3. derives responsibility / knowledge ownership before boundary and dependency direction;
4. introduces variation/layering only when stable independent change justifies it;
5. treats current modules / patches as reality Evidence, not Target authority;
6. reuses a still-valid Target; migration cost or patch churn alone does not redesign Target;
7. compares verified Current → Target gaps and selects only high-leverage structural moves with real exits;
8. leaves implementation How to Executor; AE defines structural semantics while `$evidence` may verify already-adopted structural completion claims;
9. does not treat behavior parity from Replay/test/build as proof of architecture improvement by itself;
10. uses canonical Northstar Intent / Human commitments as accepted boundary when present, without maintaining an independent Goal layer;
11. reopens only affected Target / Program when research, execution, review or verified Evidence changes a structural premise.

## Scenario smoke

### A1 — Direct invocation
User asks to evolve a named subsystem but no Northstar artifact exists.

PASS: consume the current request + authority + reality directly; do not require a synthetic Northstar pre-stage.

### A2 — Named module is only investigation scope
PASS when long-term owner follows change pressure / knowledge, not the module named in the request.

### A3 — No stable variation
PASS when no provider/layer is added solely for architecture aesthetics.

### A4 — Real variation
PASS when stable semantics may own an internal provider/adapter boundary while callers depend on stable owner semantics.

### A5 — Dependency follows ownership
PASS when historical helper placement does not dictate Target dependency.

### A6 — Legitimate dependency stays
PASS when authoritative semantic dependency remains explicit instead of being copied/merged to reduce edges.

### A7 — Target reuse
PASS when a valid Target survives current implementation churn and only Program is recomputed.

### A8 — Structural gain requires exit
PASS when facade/provider additions without old authority/knowledge exit are rejected as complexity relocation.

### A9 — Behavior parity is not architecture proof
A DaVinci Replay or equivalence backend reports behavior parity, but old owner remains authoritative.

PASS: parity is useful Evidence for behavior/compatibility only. Architecture improvement remains unproven until direct structural claims are checked.

### A10 — Evidence verifies adopted structural claim
Target already requires old authority exit and callers to depend only on the stable owner boundary.

PASS: `$evidence` may inspect realized owner/dependency/residue and judge those already-adopted claims without redesigning Target. The chosen backend may be repo inspection, runtime observation, or other direct source; Replay is not assumed to own this judgment.

### A11 — New architecture fork
Verification reveals a previously undecided long-term ownership choice.

PASS: return to AE and reopen only the affected Target/Program. A local implementation defect does not trigger redesign.

### A12 — Evidence-driven re-entry
Execution/review discovers a new runtime fact that changes migration cost but not Target premise.

PASS: only Program is recomputed. A new long-term authority fork reopens Target; a local implementation defect does not.

### A13 — No architecture change earned
PASS when a local change fully fits the current correct owner and AE returns local/no-evolution.
