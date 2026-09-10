# Architecture Shape contract eval

Eval-only. These cases protect the Target Architecture ownership split; normal runtime must not read this file.

## Static smoke

Architecture Shape must:

1. own long-term Target Architecture judgment, not the current Evolution Program;
2. derive responsibility / knowledge ownership before module boundary and dependency direction;
3. introduce variation / layering only when stable independent change justifies it;
4. treat current modules, patches and dependency cleanliness as Evidence, not Target authority;
5. use representative change locality to challenge the Target instead of scoring cohesion/coupling cosmetically;
6. preserve real independent authority / lifecycle / failure semantics instead of merging them to lower edge count;
7. keep only real material alternatives and return deciding Evidence / reopen conditions;
8. stop and return to Architecture Evolution before migration priority, structural Program or implementation How.

Static smoke must PASS 8/8.

## Scenario smoke

### A1 — Current module is not Target authority

Goal: add a second source; the request names the module where the current single-source implementation lives.

PASS: derive the capability/knowledge owner from long-term change pressure and Evidence. Keeping the named module solely because it exists fails.

### A2 — No stable variation, no provider layer

One implementation exists, no independent lifecycle/deployment/provider change is expected, and the Goal does not require replacement.

PASS: keep the Target direct. Adding interface/domain/provider layers for architecture aesthetics fails.

### A3 — Real variation earns an internal boundary

Stable domain semantics must survive independently changing storage/runtime implementations under one owner.

PASS: Target may include an internal provider/adapter boundary while callers depend only on stable owner semantics.

### A4 — Dependency follows ownership

`B → A` exists only because shared config/helper code historically lives in A; no semantic authority requires the relationship.

PASS: reassign knowledge ownership before choosing the Target dependency. Wrapping A behind `IA` without fixing ownership fails.

### A5 — Legitimate dependency stays

B consumes an authoritative semantic contract owned by genuinely independent A.

PASS: preserve a stable one-way dependency. Merging owners or copying authority just to reduce coupling fails.

### A6 — Local Goal does not earn architecture change

The Goal fits entirely inside the current correct owner and does not alter stable responsibility, authority, lifecycle, boundary or dependency.

PASS: return `no-Target-change`; do not invent a redesign.

### A7 — Two real Target alternatives

Two long-term structures remain materially plausible because a Human-owned compatibility commitment is unresolved.

PASS: retain only the real alternatives, show the deciding constraint, and return the Human decision surface. Do not pick based on implementation convenience.

### A8 — Program belongs elsewhere

Target is already clear. The remaining question is whether to migrate one owner first or retire a legacy path first based on current cost/risk.

PASS: return to `$architecture-evolution`; do not rank migration work inside Architecture Shape.

## Combined Architecture Evolution smoke

When `$architecture-evolution` starts without a usable Target:

```text
Architecture Evolution
  → model-invoke $architecture-shape
  → Target + deciding Evidence returns
  → compare Current → Target
  → Evolution Program / local-no-evolution
```

When a valid Target already exists, Architecture Evolution must not invoke Architecture Shape merely because current implementation or migration conditions changed.

## Claim boundary

These cases support responsibility/routing contract safety only. Without controlled clean-session paired runs on real repo goals, do not claim measured architecture quality or token/tool efficiency improvement.
