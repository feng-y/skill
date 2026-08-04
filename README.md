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

Northstar is currently being reviewed as the Chinese replacement for Prompt Atlas. While both directories remain for comparison, install one of them explicitly rather than installing both. Once the rewrite is stable, only the selected version should remain.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `prompt-atlas` — current English baseline for recovering stable intent and compiling one truthful autonomous taskbook or exact blocker.
- `northstar` — Chinese rewrite and rename candidate for `prompt-atlas`, preserving the same intent, execution-boundary, taskbook, and acceptance semantics.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
