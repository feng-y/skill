# Architecture Evolution contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Architecture Evolution passes only when it:

1. keeps Target Architecture judgment and current Evolution Program as distinct internal responsibilities without requiring two top-level Skills;
2. derives responsibility / knowledge ownership before boundary and dependency direction;
3. introduces variation/layering only when stable independent change justifies it;
4. treats current modules / patches as reality Evidence, not Target authority;
5. reuses a still-valid Target; migration cost or patch churn alone does not redesign Target;
6. compares verified Current → Target gaps and selects only high-leverage structural moves with real exits;
7. leaves implementation How to Executor and behavior/outcome verification to `$replay`;
8. uses Northstar Intent / Human commitments as accepted boundary and does not maintain an independent Goal layer.

## Scenario smoke

### A1 — Named module is only investigation scope
PASS when long-term owner follows change pressure / knowledge, not the module named in the request.

### A2 — No stable variation
PASS when no provider/layer is added solely for architecture aesthetics.

### A3 — Real variation
PASS when stable semantics may own an internal provider/adapter boundary while callers depend on stable owner semantics.

### A4 — Dependency follows ownership
PASS when historical helper placement does not dictate Target dependency.

### A5 — Legitimate dependency stays
PASS when authoritative semantic dependency remains explicit instead of being copied/merged to reduce edges.

### A6 — Target reuse
PASS when a valid Target survives current implementation churn and only Program is recomputed.

### A7 — Structural gain requires exit
PASS when facade/provider additions without old authority/knowledge exit are rejected as complexity relocation.

### A8 — Replay parity is not architecture proof
PASS when Replay green proves compatibility only; responsibility / authority / dependency improvement still requires structural Evidence.

### A9 — Replay reveals new architecture fork
PASS when only the affected Target/Program is reopened and behavior failure is not used to redesign an unrelated module.

### A10 — No architecture change earned
PASS when a local change fully fits the current correct owner and AE returns local/no-evolution.
