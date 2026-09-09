# Instruction compression and bounded follow-through

Eval-only for Northstar. Normal runtime must not load this file.

Base: `a8ee2fe856aab8eed126c3d3758fd540d2b74e73` (main, 2026-09-09 inspection). This work does not include the unmerged scope/transition changes in PR #82.

## Change and authority

The base repeats intent/compile/Graph/judgment instructions in the skill description, root body, final checklist, and `agents/openai.yaml`. Its own [static smoke](../../skills/northstar/references/validation.md#static-smoke), item 11, already requires the YAML to be a thin invocation pointer / input router.

The candidate keeps runtime semantics in the existing SKILL/reference owners: concise trigger descriptions, invocation-only YAML, one definition of each core discriminator, and direct routing of outcome input to the existing judgment reference. It clarifies that section boundaries and a first draft do not create approval gates, without authorizing Northstar to execute Goal work or bypass real Human choices.

Independent guidance checked on 2026-09-09: [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model#instruction-following) recommends auditing instruction conflicts and defining follow-through; [Build skills](https://learn.chatgpt.com/docs/build-skills) recommends concise trigger descriptions and progressive disclosure. These motivate the audit, not a claim of behavioral uplift or an Astra-only runtime branch.

No new role, phase, state, protocol, model profile, or runtime reference. Existing runtime references, repo AGENTS.md, AE, and RDR remain unchanged. The removed material is duplicated exposition/checklists, not Goal shaping, executable-contract content, real Graph relations, or independent judgment.

## Retention review

Review the candidate against all 12 static checks and S1-S40 in the existing [Northstar validation](../../skills/northstar/references/validation.md). In particular:

| Existing cases | Must survive compression |
| --- | --- |
| S1-S8, S19, S34, S36 | Bounded reality inspection, Goal vs means, genuine Human choice, conditional specialist resolution; no premature compile. |
| S9-S13, S27-S33, S35, S38 | Executable contract, complete known Graph, independent branches, cohesive work, contingent frontier, and Executor How. |
| S14-S17, S39-S40 | Goal-level proof, authoritative fallback, proportional checks, defaults/obligations grounded in the correct authority and surface. |
| S18, S23-S26, S29, S32 | Taskbook-first independent judgment, whole-Goal acceptance, false vs unproven, verified-Evidence gating, and correct re-entry. |
| S20-S22, S37 | Current workspace, correction of only the affected cone, identical external-file handoff, and no execution takeover. |

This is a semantic contract review, not 40 agent executions. Do not count byte reduction or wording checks as behavioral Evidence.

## Focused clean-session probes

Use [the paired harness](README.md) with pinned real tasks and identical model/effort, tools, host, and Human answer policy. The following are probe specifications, not measured results; freeze concrete repo facts and prompts before either arm runs.

### A. Ready contract, no invented approval

Provide a clear Goal, binding scope, known safe start, and adequate completion obligations; request a Taskbook, not implementation. Both UI-default-prompt and explicit skill invocation should deliver the complete identical-body external artifact in the same invocation. No “approve this draft before I compile” question, unnecessary reference sweep, implementation, or Executor launch. Judge extra confirmation using the existing `clarifications[].contract_changing` field; validate the handoff independently.

### B. Real Human decision remains open

Use an otherwise clear task with independently answerable work plus an unresolved choice that materially changes long-term maintenance or investment. Inspect available facts, expose only the current genuine choice, and preserve independent work. Do not use “follow-through” to decide the Human commitment, silently narrow the Goal, or freeze an unrelated branch. This remains a contract/authority guard, not a benchmark reward for asking fewer questions.

### C. Outcome input bypasses redundant shaping

Provide a current authoritative Taskbook and an Executor report claiming local checks prove a cross-boundary outcome; authoritative reality leaves that outcome unproven. Route to `outcome-judgment.md` without reopening settled Intent. Recover the contract before consuming the report as candidate Evidence, return the precise unproven claim, and do not accept local green as whole-Goal proof or invent a repair checklist.

### D. Verified invalidation still permits re-entry

Vary C so verified current reality invalidates a material premise of the Taskbook, while an unrelated branch remains valid. Re-enter the highest affected intent/compile judgment and fully re-deliver the corrected Taskbook, preserving unaffected work/Evidence. “Do not redo Intent take merely because this is a new invocation” must not become “never reopen Intent take.” If a new Human commitment is required, return that real choice instead of silently deciding it.

A/B concern compilation and can use the existing scorer fields. C/D concern outcome judgment; retain separate transcripts and claim-based adjudication rather than inventing executable-handoff scores for judgment-only calls. Do not expand the scorer schema or relabel judgment calls as handoffs.

## Validation record and claim boundary

2026-09-09: YAML/frontmatter parsing, invocation targets, unchanged interface keys, UTF-8/newlines/whitespace, and all eight root reference paths checked locally against the retrieved repository inventory. Manual review covered the 12 static gates and S1-S40 contract expectations. Review corrected an overbroad “do not restart Intent take” phrase so genuine evidence-driven re-entry remains allowed.

No clean-session model runs or fresh-Executor probes were executed: this editing environment has no Codex/Claude executable. No latency, token, clarification-rate, or task-success uplift is claimed. The paired harness's existing sample and blind-adjudication requirements remain unchanged; synthetic/schema data must not be submitted as behavioral results.
