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

- `prompt-atlas` — turn a one-sentence goal or scattered hints into a consumer-ready Intent Contract that can drive direct work or a spec / issue / execution workflow. Runtime-provided prior context follows the same authority and evidence rules; Prompt Atlas has no product-specific context adapter.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
