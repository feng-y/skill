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

- `prompt-atlas` — turn a one-sentence goal or scattered hints into a consumer-ready Intent Contract that can drive direct work or a spec / issue / execution workflow. When a runtime already provides prior conversation, project, or memory context, Prompt Atlas consumes it as prior context under the same authority and evidence rules rather than through a product-specific adapter.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
