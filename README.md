# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills:

```bash
npx skills@latest add feng-y/skill --all
```

Northstar is the Chinese counterpart to Prompt Atlas. While both directories remain for comparison, install one of them explicitly for active use rather than installing both.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — current English baseline for recovering stable intent and compiling one truthful autonomous taskbook or exact blocker.
- `northstar` — Chinese counterpart to `prompt-atlas`, preserving the same intent, execution-boundary, taskbook, and acceptance semantics.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — diagnose one evidence-backed architecture smell, redesign responsibility, variation ownership, dependency direction, and seam, then state how the improvement can be verified without adding another wrapper layer.
