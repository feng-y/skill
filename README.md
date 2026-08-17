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

Prompt Atlas is the English version of Northstar; Northstar is the Chinese version of Prompt Atlas. They should behave the same, so changes to one should be mirrored to the other unless the difference is purely language-specific. Since they cover the same tasks, install the language surface you want unless you are explicitly comparing them.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — English counterpart to Northstar: shape Human intent into the right Goal, preserve Executor judgment, and compile a high-altitude Taskbook whose successful delivery is materialized to an authoritative external Markdown file.
- `northstar` — Chinese counterpart to Prompt Atlas. It probes reality before asking, resumes after Human clarification or interruption, keeps implementation How with the Executor, and separates how work is organized from how completion is proven.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — recover the long-term structure of a module or capability from repo reality and design knowledge, distinguish local problems from architecture problems, and select the few highest-leverage evolutions worth advancing now.

## Architecture Evolution usage

Use `architecture-evolution` when a module keeps accumulating structural pressure, its long-term architecture is unclear, or several valid architecture directions compete for investment.

```text
Use $architecture-evolution on <module-or-capability>.
Given its current pressure and repo reality, decide the long-term structure and the highest-value architecture improvements worth advancing now.
```

Architecture Evolution may conclude that the problem is local, that a decisive fact or Human choice is still missing, that only the strategic design should be clarified, or that a small set of architecture improvements is worth advancing. A target-structure gap is not automatically a task.

See [`skills/architecture-evolution/README.md`](skills/architecture-evolution/README.md) for the capability overview and [`skills/architecture-evolution/OPERATIONS.md`](skills/architecture-evolution/OPERATIONS.md) for the operating guide.

The authoritative runtime semantics remain in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; user documentation does not define a second runtime contract.
