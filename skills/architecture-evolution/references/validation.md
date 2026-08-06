# Validate Architecture Evolution

This file validates whether the Skill improves architecture diagnosis and design. It does not claim that any implementation has preserved behavior.

The primary test is paired comparison on the same repository snapshot and task:

```text
A. Base model without architecture-evolution
B. Same model and tools with architecture-evolution
```

Freeze the task text, repository commit, available docs, model/version, tool permissions, and time/token budget before comparing outputs.

## What to score

Score each dimension `0`, `1`, or `2`.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Evidence grounding | mostly taste or labels | some code evidence | precise observed facts separated from inference and Unknown |
| Primary diagnosis | misses or lists many smells | plausible symptom | identifies one root ownership/seam error and checks a counterexample |
| Design quality | pattern naming or vague target | useful partial design | explicit responsibility, variation owner, dependency direction, and seam |
| Scope control | broad cleanup/redesign | mostly bounded | one target, one primary violation, explicit do-not-change boundary |
| Abstraction restraint | adds layers without proof | mixed | rejects speculative seams and states concrete replacement/deletion |
| Improvement proof | “cleaner/decoupled” claim | some before/after | observable change-locality, ownership, dependency, caller-knowledge, and deletion checks |
| Negative-case judgment | forces architecture work | hesitant | correctly returns `No architecture change` with evidence |

A strong result improves diagnosis and design without increasing false-positive architecture work.

## Minimum probe set

Run at least four independent cases. Use real repository cases when possible; synthetic cases are acceptable only when they preserve realistic call, ownership, and compatibility evidence.

### P1 — Variation ownership leak

Shape:

- provider/family/mode decisions are repeated across construction, execution, config, or callers;
- some repeated syntax represents the same variation, while at least one similar check has a different responsibility.

Expected Skill behavior:

- selects Rule 1 or Rule 2;
- distinguishes repeated interpretation from legitimate separate semantics;
- assigns a single variation owner;
- does not mechanically prescribe polymorphism;
- identifies concrete switches or duplicate facts that can disappear.

Candidate real case: ModelCurator provider/family branch convergence.

### P2 — Mixed primary and auxiliary responsibility

Shape:

- one module combines core semantics with metrics/debug/cache/config/compatibility;
- some auxiliary behavior should remain internal rather than becoming a public layer.

Expected Skill behavior:

- selects Gate 4 only after identifying independent change reasons;
- keeps intrinsic behavior and private implementation inside the main capability;
- separates only the responsibilities with real ownership or verification independence;
- avoids one-module-per-concern overdesign.

Candidate real case: FeatureStreaming/Predict ParseRequest alignment.

### P3 — Shallow seam and consumer reassembly

Shape:

- wrapper or interface forwards calls;
- callers assemble config, runtime, type, state, or ordering outside the module;
- tests mirror internal steps.

Expected Skill behavior:

- selects Rule 3;
- applies the deletion test;
- designs a coherent capability seam;
- reduces caller knowledge and test penetration;
- removes or deepens the shallow layer instead of adding another wrapper.

Candidate real case: Galaxy request responsibility moving from derived classes to the common module.

### N1 — Negative architecture case

Shape:

- a local bug or small mechanical change has clear ownership and no repeated change pressure;
- no dependency, caller-knowledge, or responsibility problem is evidenced.

Expected Skill behavior:

- returns `Status: No architecture change`;
- recommends a local implementation boundary;
- does not invent a provider, registry, interface, manager, or broad cleanup.

## Pass conditions for V0

The Skill is worth retaining when all conditions hold:

1. On at least two of P1–P3, the Skill arm improves the combined `Primary diagnosis + Design quality + Improvement proof` score by at least 2 points over the base arm.
2. On all positive cases, the Skill arm names one primary violation rather than returning an unranked smell inventory.
3. The Skill arm does not score lower on scope control or abstraction restraint on any case.
4. N1 returns `No architecture change`; forcing an architecture redesign is a V0 failure.
5. Every `Design ready` output contains a non-vague `Delete` or explicitly proves which caller knowledge or invalid dependency disappears instead.
6. Claims remain bounded to design quality; no output claims behavior preservation without executed evidence.

## Failure patterns to record

When a probe fails, classify the failure before changing the Skill:

- `signal miss` — the relevant code evidence was not found;
- `root-cause miss` — symptoms were found but ownership/seam diagnosis was wrong;
- `pattern reflex` — the model jumped to a design pattern;
- `scope expansion` — one target became broad redesign;
- `false abstraction` — new interfaces/layers did not remove knowledge or old paths;
- `difference collapse` — real business differences were merged;
- `false positive` — a local task was upgraded into architecture work;
- `unverifiable gain` — benefits were stated without observable before/after checks.

Only add or rewrite a rule after the same failure pattern appears in more than one representative case. Do not expand the Skill to cover a one-off miss.

## Claim boundary

A static output review can establish only that the Skill produced a better grounded design contract. It cannot establish:

- implementation correctness;
- behavior equivalence;
- successful migration or deletion;
- lower future maintenance cost in production;
- general superiority over other architecture Skills.

Those claims require implementation, repository verification, and repeated real-task evidence.
