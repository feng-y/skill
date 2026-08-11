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
- `architecture-evolution` — turn real change pressure and repo reality into an evidence-backed Architecture Decision, choosing a clear target structure and architecture-level evolution path without dropping into implementation design.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy, a historical system keeps accumulating structural pressure, or you need to decide what the next architecture should actually become rather than only identify a smell.

Typical inputs:

```text
Use $architecture-evolution on this historical module. Its boundary feels wrong,
provider branches keep growing, and callers know too much internal ordering.
Find the architecture decision worth pursuing and explain how the architecture should evolve.
```

```text
Use $architecture-evolution on FeatureStreaming and Predict ParseRequest.
They have parallel paths, but I am not sure whether they should be unified,
adapted, or kept distinct. Decide the right abstraction/specific boundary from repo reality.
```

```text
Use $architecture-evolution on <module-or-capability>.
Given its current code and change pressure, choose a target architecture if the evidence is sufficient,
and stop before implementation design.
```

The Skill keeps the architecture kernel intentionally small. It judges whether layering and dependencies are clear and one-way; whether modules are cohesive and simply organized; whether common abstraction and specific capability are balanced correctly; whether the primary responsibility shapes the architecture instead of concerns that are merely auxiliary for that capability; and whether the change makes old structural complexity actually exit.

`change locality`, caller knowledge, SOT/control/lifecycle, variation and complexity relocation are supporting evidence for those judgments rather than a mandatory analysis checklist. Real alternatives are compared only when they change a long-lived architecture boundary; naming or class-layout differences do not count.

It returns one of:

- `No architecture evolution` — the pressure does not justify architecture work; keep the change local.
- `Architecture unresolved` — a Material Unknown / Human decision or a real architecture fork still lacks enough evidence to choose safely.
- `Architecture decision ready` — Target Architecture, key trade-offs, boundaries and architecture-level evolution are stable enough to enter Implementation Design / execution.

A ready decision may choose stable layering/dependency, module responsibility, abstraction/specific and necessary authority/lifecycle boundaries. It does not prescribe concrete class/API/file layouts, helper forms, flag schemas, task breakdowns or verification providers unless repo/Human authority makes such representation itself an invariant.

Skip this Skill when the problem is local, when Target Architecture is already settled and only implementation design remains, or when the request is specifically for code review / direct execution rather than architecture reasoning.
