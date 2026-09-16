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
8. may model-invoke `$beacon` when the structural question is understood but one bounded caller path / usage / interface / boundary surface remains materially ambiguous; Beacon returns reaction Evidence and AE retains Target ownership;
9. leaves implementation How to the implementer; AE defines structural semantics while `$verify` may check already-adopted structural completion claims;
10. does not treat behavior parity from Replay/test/build as proof of architecture improvement by itself;
11. uses canonical Northstar Intent / Human commitments as accepted boundary when present, without maintaining an independent Goal layer;
12. reopens only affected Target / Program when research, execution, Beacon correction, review or verified Evidence changes a structural premise;
13. does not accept the first plausible design merely because it is coherent: when a material structural fork remains and prose cannot decide it, it may compare the minimum useful set of concrete reactions under the same structural criteria;
14. treats repeated cross-boundary workaround, extra state/parameters, type escape, duplicated knowledge, special paths, or proof bypass as architecture Evidence only when they expose a structural premise rather than a local implementation defect;
15. discards or revises the affected design when representative implementation Evidence falsifies its structural premise, instead of compensating around the bad boundary.

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

### A9 — Beacon makes structural consequence inspectable
AE has narrowed the structural question, but two candidate boundaries produce materially different caller paths that are hard to compare in prose.

PASS: AE invokes Beacon for same-form Core Path / usage contrast, consumes the result as reaction Evidence, and still makes the Target decision itself. Beacon does not select long-term owner or compose the complete Intent.

### A10 — Behavior parity is not architecture proof
A DaVinci Replay or equivalence backend reports behavior parity, but old owner remains authoritative.

PASS: parity is useful Evidence for behavior/compatibility only. Architecture improvement remains unproven until direct structural claims are checked.

### A11 — Verify adopted structural claim
Target already requires old authority exit and callers to depend only on the stable owner boundary.

PASS: `$verify` may inspect realized owner/dependency/residue and judge those already-adopted claims without redesigning Target. The chosen backend may be repo inspection, runtime observation, or other direct source; Replay is not assumed to own this judgment.

### A12 — New architecture fork
Verification reveals a previously undecided long-term ownership choice.

PASS: return to AE and reopen only the affected Target/Program. A local implementation defect does not trigger redesign.

### A13 — Evidence-driven re-entry
Execution/review discovers a new runtime fact that changes migration cost but not Target premise.

PASS: only Program is recomputed. A new long-term authority fork reopens Target; a local implementation defect does not.

### A14 — No architecture change earned
PASS when a local change fully fits the current correct owner and AE returns local/no-evolution.

### A15 — First design is not privileged
Two long-term boundary shapes both satisfy the prose-level responsibility statement, but they differ in whether callers must reconstruct private lifecycle knowledge.

PASS: AE does not simply keep the first design. It asks Beacon for the minimum same-scope concrete caller/usage reactions needed to expose the discriminator, compares them under the same ownership/change-locality criteria, then adopts/rejects the Target itself. It does not require a fixed number of candidates or a tournament when one contrast is enough.

### A16 — Implementation friction falsifies the boundary
A representative implementation of the adopted boundary repeatedly requires callers to pass owner-private state, duplicate normalization rules, add casts/escape hatches, and bypass the boundary for verification. These are not isolated coding mistakes and follow from the proposed ownership split.

PASS: treat the repeated friction as reaction Evidence against the affected structural premise, reopen only that Target decision, and revise/discard it. FAIL if AE preserves the Target and keeps adding compensating helpers/facades solely to make the implementation fit.

### A17 — Local implementation red is not architecture Evidence
A representative implementation hits a local bug or migration inconvenience, while ownership, dependency, and knowledge locality remain intact.

PASS: keep Target stable and route the local issue to the implementer / adjust Program if needed. Do not redesign architecture because implementation was inconvenient.

Static smoke checks semantic boundaries. Behavioral uplift requires organic structural tasks where the model is not instructed to generate multiple designs; the eval should observe whether it earns concrete competition only when a real discriminator remains, and whether later implementation Evidence can actually overturn its first design.
