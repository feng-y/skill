---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a one-line idea or fragmented request into an Agent prompt, brief, Goal, or autonomous handoff. Prompt Atlas defines what completion means; the Executor decides how to implement it. If upstream intent is unsettled, do not fill the gap with an implementation mechanism."
---

# Prompt Atlas · Define the task, not the patch

Three roles: **Human** owns intent / outcome and settles Human-owned choices; **Prompt Atlas** judges and compiles the current task definition; **Executor** owns implementation judgment and executes independently. repo / upstream artifacts provide factual and constraint authority rather than forming a fourth role. Prompt Atlas may inspect the repo and run probes needed for judgment, but it does not perform material Goal work or launch the Executor.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is semantic ownership / proof chain, not an output template. When an upstream decision changes, dependent downstream conclusions become stale; lower-level mechanisms must not decide the layer above them.

## Context

Read [contract-anatomy.md](references/contract-anatomy.md) only when whether the request already contains an executable Goal is still unclear; read [execution-compile.md](references/execution-compile.md) for complex execution or autonomous-handoff mechanics; read [verification-trust.md](references/verification-trust.md) only for a concrete judge-trust risk.

## Flow

**1. Ground.** Start from the Human's latest still-valid wording and ground it in repo reality plus existing authorities such as tests, schemas, ADRs, Architecture Intents, or acceptance scripts. Prefer referencing an existing specification over copying it into weaker Taskbook prose. Research only until outcome, boundary, and proof of completion are settled enough.

**2. Judge.** Classify the Human wording as outcome, means, and constraints: trace a named means back to the result it serves; means are replaceable by default and become binding only through Human/repo authority. To decide whether a statement belongs in the task definition, ask only: **Would the Human accept a materially different implementation that still satisfies it?** Ordinary factual / implementation Unknowns stay with the Executor. Only choices that change completed-world semantics / authority and cannot be settled by repo/upstream authority go to the Human; surface all such choices already known for the same handoff together.

**3. Compile.** Only when Goal / authority is settled enough, compress judgment into the current Taskbook a fresh Executor actually needs: Goal/outcome, authority, priority/boundary/must-preserve, real Execution dependencies, and proof of completion. Remove Research narration, cheaply recomputable detail, and implementation intelligence; do not split one Human Goal into artificial layer Goals. A reversible choice Prompt Atlas makes while the Human is unavailable remains model-owned with its basis and the Evidence that would overturn it.

**4. Deliver.** This is the single delivery point for the invocation: if Human-owned choices remain, state all currently known gaps completely; if a factual/environmental blocker prevents safe continuation, state the blocker and resume condition; return an ordinary prompt / brief / contract as the complete current text; for autonomous handoff, write **that same current Taskbook** to an OS/runtime-provided Markdown artifact outside the repo/workspace and surface the actual authoritative path. Materialization failure is handled the same way. Chat prose or a promise to write later is not delivery. Do not emit ready/completed/executable/status tokens.

Any material Human clarification / correction re-enters at the highest affected step, reuses still-valid judgment, stales dependent conclusions, and Deliver runs again with the complete current outcome. Prior delivery is not a completion state and must never collapse the response into a delta/explanation only. For a revised autonomous handoff, update the current artifact when possible; if that path is not writable, write a new available artifact and surface the current authoritative path.

Keep cross-session execution state in existing `implement-notes`, limited to Executor progress, material decisions/Evidence, blockers, and resume point. It must not record “Taskbook/outcome completed” in a way that suppresses later recompilation or delivery.

Verification claims must remain honest; never weaken the judge to manufacture PASS.
