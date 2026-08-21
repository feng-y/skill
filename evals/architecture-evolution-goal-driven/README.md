# Architecture Evolution goal-driven AI-native eval

Eval-only. Normal Architecture Evolution runtime must not read this file. This suite checks whether AE turns one or more related Goals into a grounded architecture evolution judgment rather than a generic refactor checklist.

## Static smoke

1. The main Skill still uses the existing `research → judgment → anchor / focus → delivery` shape. Goal-driven design does not introduce a second lifecycle, planner, compiler contract, or execution manager.
2. A named module/package is an investigation scope and reality signal, not automatically the Target boundary.
3. High cohesion, low coupling, layering, providers, contracts, and one-way dependencies are outcomes/means justified by Goal pressure + repo reality, not unconditional architecture rules.
4. AE derives responsibility/module boundary before dependency direction. A clean dependency graph cannot rescue a wrong capability decomposition.
5. Internal layering is introduced only for stable variation/change isolation inside a correct owner; there is no mandatory `interface/domain/provider/infrastructure` template.
6. AE stops at architecture outcome, structural migration boundary, structural done conditions, and Evidence obligations. It does not prescribe file/class/API/patch/test-provider How unless authority binds representation.
7. A claimed AI-native improvement must reduce unnecessary cross-boundary judgment/change/verification for representative Goals while preserving real independent responsibility and authority.
8. Program changes require structural gain + real exit. Adding a facade/provider/layer while the old authority/path remains authoritative is not improvement.

Static smoke must PASS 8/8.

## Scenario smoke

### G1 — Goal is not a module instruction

Human Goal: add a second FeatureTable source. The request mentions `FeatureDictModule` because that is where the current code lives.

PASS: AE recovers the source-selection/loading change pressure and checks which capability should own it. It may keep or redraw the current module boundary from Evidence. Treating `FeatureDictModule` as the Target owner solely because the Human named it fails.

### G2 — Related Goals may share one architecture pressure

Goals: add multiple storage backends; let callers switch backend without backend-specific code; keep backend lifecycle hidden from callers.

PASS: AE may combine these Goals because they jointly pressure the same provider responsibility/boundary. It derives one coherent Target rather than producing three unrelated refactors.

### G3 — Unrelated Goals must not be unified artificially

Goals: reduce login latency; redesign order-state ownership. Repo Evidence shows no shared authority/lifecycle/dependency premise.

PASS: keep the architecture judgments independent. Inventing a shared platform/module merely because both are supplied in one request fails.

### G4 — Capability pressure before module split

A large module contains config parsing, storage access, domain policy, and export behavior. Only storage/provider variation is expected to evolve independently; domain policy and export share one long-lived owner.

PASS: AE first identifies the required capability/variation, then chooses boundary changes. Splitting every technical concern into its own module because the file is large fails.

### G5 — Cohesion means knowledge ownership, not code proximity

Candidate A moves related functions into one directory, but callers still choose backend, reconstruct config rules, and coordinate lifecycle. Candidate B keeps some physical files separate but makes one capability owner authoritative for those decisions.

PASS: prefer B when Evidence supports that responsibility. Directory-level concentration alone is not high cohesion.

### G6 — Do not layer without stable variation

A module has one stable implementation, no independent lifecycle/deployment/provider variation, and no Goal that requires implementation replacement.

PASS: keep the structure direct. Adding interface/domain/provider/infrastructure layers merely to look AI-native fails.

### G7 — Layer when change isolation is real

A capability owns stable domain semantics while storage/runtime implementations change independently under a stable contract and are selected by the owner rather than callers.

PASS: an internal provider/adapter boundary may be part of Target because it absorbs real variation. AE still leaves class/interface/file representation to implementation unless authority fixes it.

### G8 — One-way dependency follows correct ownership

Current `B → A` exists because a helper/config historically lives in A. No semantic/authority/lifecycle relationship requires B to know A.

PASS: reopen knowledge ownership/boundary first; then remove or redirect the dependency as the Target requires. Simply introducing `IA` and preserving the same wrong knowledge placement fails.

### G9 — Legitimate stable dependency remains

B consumes an authoritative semantic contract owned by A; A and B have genuinely independent responsibilities.

PASS: preserve the explicit stable one-way dependency. Merging A/B or duplicating A's authority merely to lower coupling fails.

### G10 — AI-native locality must be observable

Target claims higher cohesion and lower coupling. For a representative Goal, fresh implementers still need to understand three unrelated modules, modify two historical owners, and assemble completion Evidence by bypassing the new facade.

PASS: reject the claimed improvement or continue Target design. A new abstraction with unchanged judgment/change/verification propagation is complexity relocation.

### G11 — Real locality improvement

Before: adding one provider requires edits in caller selection, config ownership, provider lifecycle, and tests spread across unrelated owners. After Target: one capability owner absorbs provider-specific knowledge; callers consume stable semantics; provider behavior and primary Evidence close near the owner; old caller-specific paths exit.

PASS: this is positive AI-native leverage even if total line count does not decrease.

### G12 — Behavior parity is not architecture proof

A migration passes existing replay/integration tests but the old owner remains authoritative and new callers still depend on its internals.

PASS: behavior Evidence proves compatibility only. Architecture improvement remains unproven until responsibility/authority/dependency exit claims are established.

### G13 — Structural Program, not patch plan

Target requires moving source-selection authority into a provider owner, redirecting consumers to the stable boundary, and retiring the old special path.

PASS: Program states these structural moves, dependencies, done conditions, real exits, and Evidence. File order, helper names, exact API, commit sequence, and concrete test commands remain implementation How unless already binding.

### G14 — Multiple related Goals do not imply complete redesign

Three related Goals pressure one capability boundary, but current Evidence does not justify redesigning neighboring lifecycle/observability modules.

PASS: Target and Program stay scoped to the decision-relevant boundary. Expanding into a complete repo architecture blueprint fails.

### G15 — Goal-driven no-evolution decision

A Goal can be implemented entirely inside the current correct owner; its stable contract, responsibility, dependency direction, and verification boundary remain valid, and the pressure is one-off.

PASS: return a local/no-architecture-evolution judgment. AE must not manufacture a module split or provider just because the request asked for AI-native optimization.

### G16 — Related cross-boundary Goals stay coherent without merging owners

Goals jointly require a serving pipeline to support a new producer format, preserve one authoritative domain translation, and isolate downstream runtime failure. The Goals touch producer, semantic owner, and runtime owner; repo Evidence shows these responsibilities are genuinely independent but their contracts/dependencies must evolve together.

PASS: AE keeps the independent owners, designs their boundary/dependency changes coherently under one Strategic Design, and may form a Program with multiple structural cuts connected by real dependencies. Forcing all Goals into one module, or splitting them into unrelated local refactors that cannot jointly satisfy the pipeline Goal, both fail.

## Evaluation notes

A clean-session paired evaluation should compare current main with the candidate on real repository Goals and observe at least:

- Target fidelity: does the proposal address the Goal-derived architecture pressure rather than generic smells?
- boundary correctness: does responsibility/knowledge move to the owner that should absorb the change?
- false-architecture rate: how often does AE invent modules/layers/providers for one-off or unsupported variation?
- change-locality quality: does a representative Goal require fewer unrelated responsibility/authority/dependency/verification surfaces without hiding legitimate relationships?
- evolution usefulness: does the Program identify structural moves + real exits at architecture altitude rather than vague advice or patch steps?
- startup cost: repo reads/tool calls/tokens to first useful architecture judgment.

Without paired clean-session Evidence, claim only static/scenario contract improvement, not measured behavioral uplift.
