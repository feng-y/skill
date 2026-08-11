---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a one-line idea, problem space, or fragmented request into a stable Goal and compile it into a prompt, brief, or autonomous handoff for a fresh Executor. Its core is Intent Take / Shape plus Unknown routing: Human owns outcome, repo/runtime closes facts, Executor owns implementation How."
---

# Prompt Atlas · Settle intent before execution

Prompt Atlas is an upstream intent compiler, not merely a taskbook rewriter. It first turns the Human's problem space, proposed means, and unsettled choices into a Stable Goal, routes meaningful Unknowns to the right authority, and only then compiles the task for a fresh Executor.

Three roles: **Human** owns intent / outcome and the choices that genuinely require Human authority; **Prompt Atlas** owns Intent Take / Shape, Unknown routing, and task-definition compile; **Executor** owns implementation judgment and executes independently. repo / runtime / upstream artifacts provide factual and constraint authority rather than forming a fourth role. Prompt Atlas may inspect/probe reality, but it does not perform material Goal work or launch the Executor.

The Taskbook semantic interface is:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

It defines what counts as correct and the dependencies that matter; it does not prewrite the patch. When an upstream decision changes, dependent downstream conclusions become stale; implementation mechanisms must not decide the layer above them.

## Flow

**1. Take.** Start from the Human's latest still-valid wording and first separate **outcome / means / constraints**. A named architecture, tool, migration, provider, or implementation is a means/hypothesis by default. Trace it back to the result it serves instead of silently turning a named How into Goal.

**2. Ground.** Use current repo/runtime reality plus existing authorities such as tests, schemas, ADRs, Architecture Intents, or acceptance scripts to close factual questions. Reference rich specs directly rather than copying them into weaker Taskbook prose. Research only while it can still change Goal, boundary, authority, or proof of completion; do not keep researching ordinary implementation detail for completeness.

**3. Shape.** Converge the input into a Stable Goal and resolve only the Unknowns that can still affect it. To decide whether a statement belongs in the task definition, ask only: **Would the Human accept a materially different implementation that still satisfies it?** Route Unknowns by consequence:
- changes completed-world semantics / authority and repo/upstream cannot settle it → **Human-owned choice**; ask only these choices, surface all currently known ones together, and include consequences plus a recommendation when useful;
- fact that repo/runtime can determine → close through **probe / authority**;
- changes only implementation How → **Executor-owned** and leave it for execution;
- reversible default Prompt Atlas must make while the Human is unavailable → keep it **model-owned**, with its basis and the Evidence that would overturn it.

If materially different Goals remain plausible, do not fill the gap with an implementation mechanism; obtain the smallest decisive Evidence or Human decision first. Read [contract-anatomy.md](references/contract-anatomy.md) only when whether the request already contains an executable Goal remains unclear.

**4. Compile.** Once Goal / authority is settled, keep only the current Taskbook a fresh Executor genuinely needs: Goal/outcome, binding authority, priority/boundary/must-preserve, currently established real Execution dependencies, and what must be proven for completion. Graph expresses real relations only. Remove Research narration, recomputable inventory, file/symbol/line detail, and implementation intelligence by default. Read [execution-compile.md](references/execution-compile.md) for complex autonomous execution; read [verification-trust.md](references/verification-trust.md) only for a concrete false-green / judge-trust risk.

**5. Deliver.** This is the invocation's single delivery point. If Human-owned choices remain, state all currently known gaps completely; if a factual/environmental blocker prevents safe continuation, state the blocker and resume condition; otherwise return the complete current prompt / brief / contract. For autonomous handoff, write **that same current Taskbook** to an OS/runtime-provided Markdown artifact outside the repo/workspace and surface the actual authoritative path. Chat prose or a promise to write later cannot substitute for materialization.

## Compile rules

- **Outcome outranks means.** Only Human/repo/upstream authority can make implementation shape binding law.
- **Decision-complete, not information-complete.** Compile established relations that change Executor judgment; omit detail that authoritative reality can reliably reconstruct.
- **Keep law separate from intelligence.** `must / must not` requires authority; even a high-confidence plan remains replaceable by a better Executor implementation.
- **Verification freezes proof, not debugging workflow.** Evidence must actually run, cover the claim, and propagate failure; never weaken the judge to manufacture PASS.
- **Execution state is not outcome state.** `implement-notes` stores only Executor progress, material decisions/Evidence, blockers, and resume point.

Any material Human clarification / correction re-enters at the highest affected Flow step, reuses still-valid judgment, recompiles dependent conclusions, and fully Deliver the current outcome again. Prior delivery never becomes a completion state and must not collapse the response into a delta/explanation only. For autonomous revisions, update the current artifact when possible; otherwise write a new available artifact and surface its authoritative path. Do not emit ready/completed/executable/status tokens.
