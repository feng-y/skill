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
- `architecture-evolution` — turn real change pressure and repo reality into an evidence-backed Architecture Decision: model the relevant architecture forces, compare materially different target architectures when a real fork exists, choose or remain unresolved, and shape the architecture-level evolution path.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy, a historical system keeps accumulating cross-boundary change pressure, or you need to decide what the next architecture should actually become rather than only identify a smell.

Typical inputs:

```text
Use $architecture-evolution on this historical module. Its boundary feels wrong,
provider branches keep growing, and callers know too much internal ordering.
Find the architecture decision worth pursuing and explain how the architecture should evolve.
```

```text
Use $architecture-evolution on FeatureStreaming and Predict ParseRequest.
They have parallel paths, but I am not sure whether they should be unified,
adapted, or kept distinct. Compare the materially different architecture directions
that current repo forces actually support.
```

```text
Use $architecture-evolution on <module-or-capability>.
Given its current code and change pressure, reconstruct the architecture forces,
choose a target architecture if the evidence is sufficient, and stop before implementation design.
```

The Skill does more than produce an intent. It reconstructs only the decision-relevant current architecture model (responsibility, authority/SOT, knowledge, control/lifecycle, dependency, variation and change-pressure relationships), explores real architecture forks without manufacturing option-count ceremony, compares trade-offs and complexity relocation, and shapes the architecture-level transition from current to target state.

It returns one of:

- `No architecture evolution` — the pressure does not justify architecture work; keep the change local.
- `Architecture unresolved` — a Material Unknown / Human decision or a real architecture fork still lacks enough forces to choose safely.
- `Architecture decision ready` — Target Architecture, key trade-offs, boundaries and architecture-level evolution are stable enough to enter Implementation Design / execution.

A ready decision may choose stable responsibility / authority / knowledge / control / lifecycle / dependency / essential-variation boundaries. It does not prescribe concrete class/API/file layouts, helper forms, flag schemas, task breakdowns or verification providers unless repo/Human authority makes such representation itself an invariant.

Skip this Skill when the problem is local, when Target Architecture is already settled and only implementation design remains, or when the request is specifically for code review / direct execution rather than architecture reasoning.
