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

`--all` installs both language variants. Use `prompt-atlas` for English taskbooks and `northstar` for Chinese taskbooks.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `prompt-atlas` — recover stable intent from a one-sentence goal or scattered hints, then compile the smallest truthful executable carrier or exact blocker for a downstream agent/runtime. Use when the taskbook should be written in English.
- `northstar` — complete Chinese-language edition of `prompt-atlas`, preserving the same intent, taskbook, execution-boundary, and acceptance semantics. Use when the taskbook should be written in Chinese.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
