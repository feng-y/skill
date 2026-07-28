---
name: unknowns-first
description: "Use when map and territory may diverge in engineering work: unclear route, scope, proof, user intent, repo reality, runtime behavior, unfamiliar code/config, behavior-preserving change, migration/refactor, reference-first porting, mid-build deviation, or any correctness claim that needs repo/runtime evidence."
---

# Unknowns First

Unknowns First is the lightweight unknown gate for engineering work. It is the repo's single unknown-skill surface: both the default light gate and the heavy full-map branch live here, so full-map / handoff work does not route to a separate skill.

The map is the prompt, plan, memory, docs, and assumptions. The territory is the codebase, config, runtime behavior, tests, data, users, and constraints.

Core rule: when map != territory, do not guess. Expose the unknown, run a minimal probe, ask one route-changing question, or record an implementation note.

## When To Use

Use this for engineering work where a wrong assumption could change route, scope, implementation, verification, rollout, or user-visible behavior.

Skip it for pure lookup, casual explanation, writing-only work, or trivial shell output unless correctness depends on repo or runtime evidence.

Completion criterion: the task is either out of scope, or one unknown-gate level is selected.

## Levels

Pay only the level the task earns:

- **L1 Light gate**: default. Identify Target / Territory / Unknown / Proof, silently or in one concise note.
- **L2 Local move**: use one probe, blindspot pass, interview question, reference map, option set, concrete sample, vocabulary ladder, implementation note, verifier check, or post-change move.
- **L3 Full map**: read [references/full-map-workflow.md](references/full-map-workflow.md) when the user asks for a complete unknowns map, source alignment, full-map handoff, or when coupled unknowns should pause implementation.

Completion criterion: L1 is the default; L2/L3 activates when the gate trips, and the trigger plus unknown are named before expansion.

## L1 Light Gate

For every in-scope task, identify four facts:

- **Target**: intended behavior or decision.
- **Territory**: code, config, runtime, data, docs, tests, or user constraint that must be true.
- **Unknown**: the first thing that would make the plan wrong.
- **Proof**: minimum evidence needed before a correctness or completion claim.

Choose exactly one terminal output:

- `continue`: target, territory, first unknown, and proof are clear enough for direct work. May stay silent during routine direct work.
- `probe: <unknown>; next: <territory check>` when one territory check can shrink the unknown.
- `ask: <question>; changes: <route/scope/gate/behavior>` when one route-changing answer cannot be found in territory evidence.
- `note: <assumption-or-deviation>; proof impact: <impact>` when work can proceed but a conservative assumption or deviation must be preserved.
- `full-map: <why L3>; next: full-map workflow` when implementation should pause for L3.
- `must-verify-in-repo: <missing proof>; next verifier: <command-or-doc>` when the claim depends on missing or unrunnable proof.

Completion criterion: `continue` is the only terminal that may stay silent; every other terminal is visible before acting.

## Escalation Triggers

Escalate from L1 when continuing would guess and at least one trigger is present:

- unfamiliar module, domain, tool, API, data, or failure mode;
- cross-module, shared-boundary, migration, cleanup, refactor, behavior-preserving, or compatibility work;
- verification-sensitive task where a false claim matters;
- plan, docs, history, tests, logs, config, or runtime contradicts the current map;
- tacit taste, UX, API shape, output format, or workflow needs a concrete reaction;
- implementation reveals a hidden coupling, edge case, missing prior art, or better path.

Completion criterion: every expansion names the trigger and the unknown it is shrinking.

## L2 Local Moves

Use the cheapest move that changes the next action:

| Move | Use when | Output |
| --- | --- | --- |
| Probe | evidence can answer | one focused `rg`, file read, test discovery, config lookup, log check, or tiny repro |
| Blindspot pass | unknown unknown risk | landmine cards covering the touched responsibility surface, with evidence, why it bites, changed action |
| Interview | only the user can answer a route-changing question | one question plus why the answer changes route |
| Reference first | an existing implementation, trace, design, or config defines behavior | semantics map before port/copy: transfers, non-transfers, edge cases, sign-off point |
| Options | several interventions could work | options from cheapest safe slice to ambitious bet, with risk and proof |
| Concrete sample | taste, UX, API, output, or workflow is tacit | mock, sample, prototype, or contrasting directions grounded in real data or clearly labeled fake data |
| Vocabulary | the task lacks terms to judge quality | vocabulary ladder, quality bar, sharper prompt |
| Notes | work proceeds after a deviation or conservative assumption | concise implementation note with verification impact |
| Post-change | reviewers inherit non-obvious assumptions, landmines, or behavior claims | buy-in doc, reviewer checklist, behavior summary, or quiz tied to evidence |

Completion criterion: one move resolves the unknown, surfaces a human decision, or escalates to L3.

## L3 Full Map

Use L3 when the user asks to map unknowns, wants source alignment, or the unknowns are coupled enough that implementation should wait. Read [references/full-map-workflow.md](references/full-map-workflow.md). L3 is the canonical home for the repo's full-map, handoff, and post-map unknown artifacts.

Full-map mode has its own contract:

- silently scan the request, prior attempts, touched files/configs/tests, and constraints before opening;
- walk known knowns, known unknowns, unknown knowns, unknown unknowns, then handoff;
- name the current section;
- cite territory evidence;
- maintain a visible queue for known unknowns with closer (`territory`, `user`, or `OPEN`);
- use context probes for tacit taste, consumers, environment, vocabulary, and done criteria;
- sweep the touched responsibility surface for landmines before handoff;
- close decisions in front of the user;
- stop at the handoff only when the map itself is the requested deliverable, or when a real human-held blocker / reaction is still the next closer.

Completion criterion: the user holds the map, open items are visible, and the next implementation prompt does not need to rediscover the same unknowns. If the map has already closed route / readiness and no human-owned blocker remains, return control to the repo's next-capability selection instead of treating full-map completion itself as task completion.

## Verification

Before claiming completion, match proof to risk:

- direct/small: focused read plus nearest cheap command or test when available;
- refactor/migration/behavior preservation: regression tests, diff/replay/contract evidence, or explicit not-tested gap;
- cross-module/high-risk: build/typecheck plus targeted tests and any necessary replay/diff/manual evidence.

If proof is missing, use `must-verify-in-repo` or report the gap. Treat missing proof as an unfinished loop, not a completed task.

Completion criterion: final claims cite evidence actually run, or clearly name verification gaps.

## Fold Back

After non-trivial work, keep only lessons that prevent repeated rediscovery:

- wrong map assumption;
- probe that exposed territory;
- earlier statement that would have prevented the miss;
- note, doc, test, or follow-up that should preserve the lesson.

Completion criterion: the retro is shorter than the work it saves next time.

## Common Mistakes

- Expanding every task to L3. Use L1 unless implementation should pause.
- Asking the user before checking territory evidence. Probe first when repo evidence can answer.
- Carrying multiple moves at once. Use one local move, then reclassify.
- Treating missing proof as success. Name the verification gap.
- Writing durable lessons for one-off noise. Fold back only reusable lessons.
