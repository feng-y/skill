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

Prompt Atlas and Northstar are peer skill surfaces. They may share or synchronize mechanisms, but neither owns or contains the other. Because their invocation territory can overlap, install one explicitly for active use unless you are comparing them.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — English skill for recovering stable intent and compiling one truthful autonomous taskbook or exact blocker.
- `northstar` — peer Chinese skill with its own control surface; shared mechanisms may be synchronized without making either skill subordinate to the other.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — turn vague architecture concerns and real change pressure into one evidence-backed Architecture Intent, preserving four architecture directions, a Real Evolution exit target, and the Brooks design constraints that downstream architecture work should absorb progressively.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy. You can provide a module, recurring symptoms, a suspected hotspot, or a broad concern such as “what should evolve next?”. You do **not** need to identify the architecture principle, Brooks risk, final design, candidate list, or supporting evidence first. Give the relevant repository area and what feels wrong; the Skill should inspect the available code and evidence itself.

Typical inputs:

```text
Use $architecture-evolution on this historical module. Its boundary feels wrong,
provider branches keep growing, and callers know too much internal ordering.
Find the architecture intent worth pursuing.
```

```text
Use $architecture-evolution on FeatureStreaming and Predict ParseRequest.
They have parallel paths, but I am not sure whether they should be unified,
adapted, or kept distinct. Recover the real architecture intent first.
```

```text
Use $architecture-evolution on <module-or-capability>.
Given its current code and change pressure, identify the next architecture
direction worth pursuing. Do not jump to an implementation plan.
```

The Skill will ground the direction in repository evidence, distinguish architecture pressure from a local fix, select one primary architecture direction, challenge false unification or speculative abstraction, and return one of:

- `No architecture intent` — keep the work local; there is not enough architecture pressure.
- `Intent unresolved` — one evidence gap or Human-owned decision still changes the direction.
- `Architecture intent ready` — one bounded intent is stable enough for downstream design.

A ready intent describes the desired end state, boundaries, design obligations, an observable replacement/exit target, and the Brooks constraints that later design should absorb progressively. It intentionally does **not** prescribe classes, factories, registries, migration steps, or a complete target architecture.

Skip this Skill when the target architecture, implementation boundary, and success criteria are already clear, or when the current request is specifically for a complete design, taskbook, code review, or direct implementation. Continue with the appropriate design or execution path rather than reconstructing the intent.
