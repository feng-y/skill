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
- `architecture-evolution` — turn vague architecture concerns and real change pressure into one evidence-backed, bounded Architecture Intent that is ready for downstream design.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy. Give the relevant repository area and the recurring pressure or concern; the Skill should inspect the available code and evidence itself.

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

The Skill grounds the direction in repository evidence, distinguishes architecture pressure from a local fix, applies architecture judgement, and returns one of:

- `No architecture intent` — keep the work local; there is not enough architecture pressure.
- `Intent unresolved` — one evidence gap or Human-owned decision still changes the direction.
- `Architecture intent ready` — one bounded intent is stable enough for downstream design.

A ready intent explains the problem, background, direction, and boundary, and fixes one stable outcome-level acceptance rule. It may briefly name a few basic target shapes when useful, but stops before concrete target design; lint/test/verification methods remain downstream choices.

Skip this Skill when the target architecture and implementation boundary are already clear, or when the current request is specifically for a complete design, taskbook, code review, or direct implementation.
