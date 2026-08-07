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
