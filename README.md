# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills (currently installs Prompt Atlas, Northstar, Unknowns First, and Architecture Evolution):

```bash
npx skills@latest add feng-y/skill --all
```

Prompt Atlas and Northstar are two language surfaces of the same Skill semantics: **Prompt Atlas is the English version and Northstar is the Chinese version**. Their runtime model, decision boundaries, taskbook semantics, Verification/Evidence behavior, and eval cases should remain behaviorally aligned; changes to one should be synchronized to the other unless the difference is purely language-specific. Because their invocation territory overlaps, install the language surface you want to use unless you are explicitly comparing the two.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — English version of the shared Northstar/Prompt Atlas semantics for recovering a stable Goal and compiling one truthful autonomous taskbook or exact blocker.
- `northstar` — Chinese version of the same semantics and behavior; changes should stay synchronized with Prompt Atlas rather than evolving as an independent control surface.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — start from a named module and its direct structural neighborhood, recover the real capability and any evidence-backed provider boundaries, choose a Target Architecture, and compile it into a few concrete Architecture Improvements without dropping into implementation design.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy, a historical module keeps accumulating structural pressure, or you need to decide what that area should become rather than only identify a smell.

Typical inputs:

```text
Use $architecture-evolution on this historical module. Its boundary feels wrong,
provider branches keep growing, and callers know too much internal ordering.
Find the target architecture and the highest-value architecture improvements worth advancing.
```

```text
Use $architecture-evolution on FeatureStreaming and Predict ParseRequest.
They have parallel paths, but I am not sure whether they should be unified,
adapted, or kept distinct. Re-identify the capability and stable common/specific boundary from repo reality.
```

```text
Use $architecture-evolution on <module-or-capability>.
Start from this area and its direct upstream/downstream, choose a target architecture if the evidence is sufficient,
then compile it into concrete architecture improvements. Stop before implementation design.
```

Research is bounded by default: anchor on the named module, inspect direct upstream/downstream, infer the capability from actual responsibility rather than module names, redraw its boundary, then expand only the stable specific variations that can change the architecture decision. A provider boundary is created only when durable semantics/lifecycle/performance/deployment evidence proves real variation; otherwise the result stays one capability. Wider repo search is targeted only when local evidence cannot close a material authority/SOT/identity/contract question.

The architecture kernel stays small: clear layering and one-way dependencies; cohesive and simple modules; correct abstraction vs specific boundaries; primary responsibility shaping the structure instead of auxiliary concerns; and real structural exit rather than complexity relocation. `change locality`, caller knowledge, SOT/control/lifecycle, variation and Brooks are supporting evidence/challenge context, not mandatory analysis checklists.

A ready result is compiled into a thin Architecture Program rather than returning the full reasoning. It keeps the structural adjustment, long-term architecture, and at most three highest-value Architecture Improvements. Each improvement must produce a concrete structural gain, make old knowledge/authority/dependency/path or accidental complexity actually exit, and have a structural done condition. Research questions do not count; if only two real improvements exist, only two are returned. Ordering appears only when a real architecture dependency exists.

It returns one of:

- `No architecture evolution` — the pressure does not justify architecture work; keep the change local.
- `Architecture unresolved` — a Material Unknown / Human decision / real architecture fork still lacks enough evidence, or no candidate change can yet be proven to improve the structure.
- `Architecture decision ready` — Target Architecture is stable and has been compiled into a bounded Architecture Program that can enter Implementation Design / execution.

A ready program may choose stable layering/dependency, module responsibility, abstraction/specific and necessary authority/lifecycle boundaries. It does not prescribe concrete class/API/file layouts, helper forms, flag schemas, MR/task breakdowns or verification providers unless repo/Human authority makes such representation itself an invariant.

Skip this Skill when the problem is local, when Target Architecture is already settled and only implementation design remains, or when the request is specifically for code review / direct execution rather than architecture reasoning.
