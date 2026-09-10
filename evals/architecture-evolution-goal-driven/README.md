# Architecture Evolution goal-driven AI-native eval

Eval-only. Normal runtime must not read this file. This suite checks the **combined Architecture Evolution surface** after responsibility split: `$architecture-shape` owns long-term Target Architecture judgment when Target is missing/stale, while `$architecture-evolution` owns the Current → Target structural gap and current Evolution Program. The external request may still enter through Architecture Evolution; the eval must not require both responsibilities to live in one Skill.

## Static smoke

1. Architecture Evolution owns current structural evolution / Program, not long-term Target design; it model-invokes `$architecture-shape` only when a usable Target is missing or a material Target premise has failed.
2. A still-valid authoritative Target is reused. Current implementation churn, migration cost or Program changes alone do not trigger Target redesign.
3. Architecture Shape treats a named module/package as investigation scope and Evidence, not automatically the Target boundary.
4. Architecture Shape derives responsibility / knowledge ownership before dependency direction; layering/providers exist only for stable variation, not as unconditional architecture rules.
5. Architecture Evolution compares verified Current → Target gaps and selects at most a few high-leverage structural moves; it does not re-derive Target from current code or Program convenience.
6. Program changes require structural gain + real exit. Adding a facade/provider/layer while old authority/path remains authoritative is not improvement.
7. The combined surface stops at Target judgment + structural Program / migration boundary / structural Evidence obligations. It does not prescribe file/class/API/patch How unless authority binds representation.
8. A claimed AI-native improvement must reduce unnecessary cross-boundary judgment/change/verification for representative Goals while preserving real independent responsibility and authority.

Static smoke must PASS 8/8.

## Scenario smoke

### G1 — Goal is not a module instruction

Human Goal: add a second FeatureTable source. The request mentions `FeatureDictModule` because that is where the current code lives.

PASS: the combined flow recovers the source-selection/loading change pressure and checks which capability should own it. Architecture Shape may keep or redraw the current module boundary from Evidence. Treating `FeatureDictModule` as Target owner solely because the Human named it fails.

### G2 — Related Goals may share one architecture pressure

Goals: add multiple storage backends; let callers switch backend without backend-specific code; keep backend lifecycle hidden from callers.

PASS: Architecture Shape may combine these Goals because they jointly pressure the same provider responsibility/boundary. It derives one coherent Target rather than producing three unrelated refactors; Architecture Evolution then derives only the current structural gaps worth advancing.

### G3 — Unrelated Goals must not be unified artificially

Goals: reduce login latency; redesign order-state ownership. Repo Evidence shows no shared authority/lifecycle/dependency premise.

PASS: keep the architecture judgments independent. Inventing a shared platform/module merely because both are supplied in one request fails.

### G4 — Capability pressure before module split

A large module contains config parsing, storage access, domain policy, and export behavior. Only storage/provider variation is expected to evolve independently; domain policy and export share one long-lived owner.

PASS: Architecture Shape first identifies the required capability/variation, then chooses Target boundary changes. Splitting every technical concern into its own module because the file is large fails.

### G5 — Cohesion means knowledge ownership, not code proximity

Candidate A moves related functions into one directory, but callers still choose backend, reconstruct config rules, and coordinate lifecycle. Candidate B keeps some physical files separate but makes one capability owner authoritative for those decisions.

PASS: prefer B when Evidence supports that responsibility. Directory-level concentration alone is not high cohesion.

### G6 — Do not layer without stable variation

A module has one stable implementation, no independent lifecycle/deployment/provider variation, and no Goal that requires implementation replacement.

PASS: Architecture Shape keeps the Target direct. Adding interface/domain/provider/infrastructure layers merely to look AI-native fails.

### G7 — Layer when change isolation is real

A capability owns stable domain semantics while storage/runtime implementations change independently under a stable contract and are selected by the owner rather than callers.

PASS: an internal provider/adapter boundary may be part of Target because it absorbs real variation. Class/interface/file representation remains implementation How unless authority fixes it.

### G8 — One-way dependency follows correct ownership

Current `B → A` exists because a helper/config historically lives in A. No semantic/authority/lifecycle relationship requires B to know A.

PASS: Architecture Shape reopens knowledge ownership/boundary first; only then can the Target remove or redirect the dependency. Simply introducing `IA` and preserving the same wrong knowledge placement fails.

### G9 — Legitimate stable dependency remains

B consumes an authoritative semantic contract owned by A; A and B have genuinely independent responsibilities.

PASS: preserve the explicit stable one-way dependency. Merging A/B or duplicating A's authority merely to lower coupling fails.

### G10 — AI-native locality must be observable

Target claims higher cohesion and lower coupling. For a representative Goal, fresh implementers still need to understand three unrelated modules, modify two historical owners, and assemble completion Evidence by bypassing the new facade.

PASS: Architecture Shape rejects the claimed Target improvement or continues Target design. A new abstraction with unchanged judgment/change/verification propagation is complexity relocation.

### G11 — Real locality improvement

Before: adding one provider requires edits in caller selection, config ownership, provider lifecycle, and tests spread across unrelated owners. After Target: one capability owner absorbs provider-specific knowledge; callers consume stable semantics; provider behavior and primary Evidence close near the owner; old caller-specific paths exit.

PASS: this is positive AI-native leverage even if total line count does not decrease. Architecture Evolution may then prioritize the structural gaps required to realize it.

### G12 — Behavior parity is not architecture proof

A migration passes existing replay/integration tests but the old owner remains authoritative and new callers still depend on its internals.

PASS: behavior Evidence proves compatibility only. Architecture improvement remains unproven until responsibility/authority/dependency exit claims are established.

### G13 — Structural Program, not patch plan

Target requires moving source-selection authority into a provider owner, redirecting consumers to the stable boundary, and retiring the old special path.

PASS: Architecture Evolution Program states these structural moves, dependencies, done conditions, real exits, and Evidence. File order, helper names, exact API, commit sequence, and concrete test commands remain implementation How unless already binding.

### G14 — Multiple related Goals do not imply complete redesign

Three related Goals pressure one capability boundary, but current Evidence does not justify redesigning neighboring lifecycle/observability modules.

PASS: Target and Program stay scoped to the decision-relevant boundary. Expanding into a complete repo architecture blueprint fails.

### G15 — Goal-driven no-evolution decision

A Goal can be implemented entirely inside the current correct owner; its stable contract, responsibility, dependency direction, and verification boundary remain valid, and the pressure is one-off.

PASS: Architecture Shape may return no-Target-change, and Architecture Evolution returns local/no-evolution. Neither manufactures a module split or provider just because the request asked for AI-native optimization.

### G16 — Related cross-boundary Goals stay coherent without merging owners

Goals jointly require a serving pipeline to support a new producer format, preserve one authoritative domain translation, and isolate downstream runtime failure. The Goals touch producer, semantic owner, and runtime owner; repo Evidence shows these responsibilities are genuinely independent but their contracts/dependencies must evolve together.

PASS: Architecture Shape keeps the independent owners and designs their Target boundary/dependency changes coherently. Architecture Evolution may form a Program with multiple structural cuts connected only by real dependencies. Forcing all Goals into one module, or splitting them into unrelated local refactors that cannot jointly satisfy the pipeline Goal, both fail.

### G17 — Clean source is not a behavior oracle

A refactor branch fails replay. The named clean base ref fails the same cases, while a separately identified release/golden runtime passes the same inputs and configuration. A discriminator traces the behavioral gap to an upstream request-data boundary, not to the slot/projection structure the refactor was changing.

PASS: the combined flow corrects causal attribution before changing Target or Program. If the Goal requires a green behavior baseline, Architecture Evolution keeps semantic restoration and structural evolution as distinct Program outcomes with separate behavior and structural Evidence, connected only by the real dependency that evolution must start from a trustworthy baseline. It does not treat a branch name, clean worktree, passing golden artifact, or failing candidate replay as interchangeable reality, and it does not ask Architecture Shape to widen slot/projection Target around an upstream data-owner defect.

FAIL: blame the refactor because its branch is red, declare base behavior authoritative because the ref is clean, merge restoration into the architecture claim so one PASS proves both, or redesign the named module before discriminating the failure owner.

## Evaluation notes

A clean-session paired evaluation should compare current main with the candidate on real repository Goals and observe at least:

- **Target fidelity / boundary correctness** for Architecture Shape: does Target address Goal-derived architecture pressure, place responsibility/knowledge correctly, and avoid false modules/layers/providers?
- **change-locality quality** for the Target: does a representative Goal require fewer unrelated responsibility/authority/dependency surfaces without hiding legitimate relationships?
- **evolution usefulness** for Architecture Evolution: does the Program identify Current → Target structural gaps + real exits at architecture altitude rather than vague advice or patch steps?
- **Target reuse discipline**: when a valid Target exists, does AE avoid needless strategic redesign as current reality changes?
- **startup cost**: repo reads/tool calls/tokens to first useful Target judgment and first useful Program judgment, measured separately when possible.

Without paired clean-session Evidence, claim only static/scenario contract improvement, not measured behavioral uplift.
