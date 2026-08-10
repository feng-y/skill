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
- `architecture-evolution` — turn vague architecture concerns and real change pressure into one evidence-backed Architecture Intent: identify the real architecture problem and its background, frame the target direction and boundary, and when useful expose a few basic target architecture identities without crossing into target design.

## Architecture Evolution usage

Use `architecture-evolution` when the architecture direction is still fuzzy. You can provide a module, recurring symptoms, a suspected hotspot, or a broad concern such as “what should evolve next?”. You do **not** need to identify the architecture principle, Brooks risk, final design, candidate list, or supporting evidence first. Give the relevant repository area and what feels wrong; the Skill should inspect the available code and evidence itself.

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

The Skill will ground the direction in repository evidence, distinguish architecture pressure from a local fix, recover the structural problem and the historical assumption that no longer fits, challenge false unification or speculative abstraction, and return one of:

- `No architecture intent` — keep the work local; there is not enough architecture pressure.
- `Intent unresolved` — one evidence gap or Human-owned decision still changes the direction.
- `Architecture intent ready` — one bounded intent is stable enough for downstream design.

A ready intent explains the architecture problem, why it exists now, the target direction, its boundary, and a real replacement/exit. If more than one basic target shape is genuinely worth comparing, it may include a small number of target architecture identities. Brooks risks, internal taxonomy, counterexample checks, and proof vocabulary remain reasoning machinery rather than output sections.

The Skill intentionally stops before target design: it does **not** prescribe concrete classes, interfaces, APIs, adapters, responsibility placement, call/data flows, migration steps, implementation slices, or verification plans. Its final answer follows the user's primary language; code symbols and stable protocol names can remain in their source language.

Skip this Skill when the target architecture, implementation boundary, and success criteria are already clear, or when the current request is specifically for a complete design, taskbook, code review, or direct implementation. Continue with the appropriate design or execution path rather than reconstructing the intent.
