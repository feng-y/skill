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

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `prompt-atlas` — accumulate the user's scattered hints, clarify the real intent, and stop before solution design or specification.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
