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
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `prompt-atlas` — recover stable intent from a one-sentence goal or scattered hints, then compile the smallest truthful executable carrier or exact blocker for a downstream agent/runtime.
- `northstar` — Chinese-language edition of `prompt-atlas`, preserving the same intent, taskbook, execution-boundary, and acceptance semantics.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
