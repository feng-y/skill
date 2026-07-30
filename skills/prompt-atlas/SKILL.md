---
name: prompt-atlas
description: "Compile a one-sentence goal or scattered, evolving cross-turn hints into a consumer-ready Intent Contract or requested carrier. Preserve settled semantics across invocations, incorporate new user authority, and refresh territory grounding from authoritative evidence. In explicit Artifact mode, return either `Status: Executable` with a Goal Loop Contract containing Goal, State, Decisions, Constraints, Loop, Evaluation, Output, and Control, or `Status: Unresolved` with the smallest gap that still prevents safe execution. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when another workflow explicitly needs intent intake before execution. Explicit /prompt-atlas use returns the compiled artifact as the terminal result of this invocation."
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground only the territory that can change the contract, resolve Human-owned decisions, and compile an artifact that a capable agent can execute without rediscovering meaning, authority, completion, or control.

Assume current frontier models can investigate repositories, organize work, self-correct, and verify routine changes. Do not add generic always-plan, always-review, fixed-taskbook, or always-use-subagent scaffolding. Encode the parts that remain costly to reconstruct or unsafe to improvise: user authority, hard boundaries, material state, proof integrity, global completion, and complexity/stop control.

Compile these minimum semantics:

- **Goal Condition** — the desired end state and real problem;
- **Current State** — relevant facts, evidence, proof state, starting references, completed work, and bounded uncertainty;
- **Authority / Boundary** — confirmed decisions, invariants, accepted differences, scope and approval limits, and protected judging rules;
- **Loop Directive** — how the executor may act, organize tasks, learn from observations, and change implementation How;
- **Evaluation / Control** — what makes the complete Goal `MET`, how `UNMET` drives the next action, which control form is sufficient, and what can honestly stop work.

For architecture evolution, also compile the current **Architecture Intent**: the user-confirmed or governing architecture kernel, verified structural facts with provenance, the evidence-revisable target hypothesis, and target-shaping unknowns. Put only confirmed or authoritative principles in Constraints. Repo evidence may revise the design and task organization, but not silently replace the requested structural outcome.

Prompt Atlas owns intent understanding, necessary grounding, executable-readiness judgment, and contract compilation. It does not execute the loop, own live runtime state, or act as a durable repo harness. New user authority may change user-owned intent; better territory evidence may change State, feasibility, proof obligations, necessary scope inside existing authority, or the current Architecture Intent. Rewriting alone changes neither.

Choose the output mode from the invocation:

- **Artifact mode** — default for explicit `/prompt-atlas` use and direct requests to clarify, consolidate, prepare, hand off, or rewrite a requirement. Return exactly one `Status: Executable` or `Status: Unresolved` artifact and stop.
- **Embedded mode** — only when another capability explicitly invokes Prompt Atlas as intake. Return the compiled intent in the caller's carrier or schema and stop Prompt Atlas. Do not infer this mode merely because execution may follow.

Read [contract-anatomy.md](references/contract-anatomy.md) when contract sufficiency, execution control, architecture work, or stability is not obvious. Read [completion-trust.md](references/completion-trust.md) when the result needs a material correctness or completion claim.

## Intent Take

### 1. Recover

Use the current request, relevant corrections, prior decisions, examples, and any still-valid Atlas artifact. The current user owns intent; current authoritative evidence owns territory; the latest explicit correction supersedes older meaning.

Recover outcomes separately from suggested means and hard constraints. Preserve every explicit requested outcome with its original authority unless the user supersedes it. Evidence may expose prerequisites, wider necessary work inside settled authority, stronger proof, or infeasibility; it may not silently turn “do this” into “defer it,” “do one slice,” or “do something weaker.”

Judge sufficiency at the level the invocation must establish: outcome, behavior/capability contract, or a user-owned solution commitment. Leave downstream design freedom open unless it changes an outcome, boundary, approval, priority, or proof obligation.

### 2. Ground

Investigate only unknowns that can materially change Goal, State, Decisions, Constraints, Evaluation, Architecture Intent, or executable readiness. Prefer the smallest authoritative check and rich existing references such as code, tests, traces, schemas, artifacts, and rubrics.

For repo work:

- include governing local constraints and acceptance paths that can change execution or completion;
- preserve a consumer-resolvable execution target: the current repo/workspace root, or a repository identity plus revision and materialization instruction. If the caller's carrier already binds the workspace, state that dependency explicitly; a commit hash or filename alone is not a locator;
- capture a sourced baseline when success is relative to current behavior or measurement;
- run critical commands when accessible; otherwise mark them `unverified` rather than presenting them as facts;
- distinguish verified fact, inference, and unknown;
- when evidence conflicts with an explicit outcome, determine whether prerequisites, necessary scope, or stronger proof can preserve it inside current authority before asking the user.

For architecture work, ground enough to identify the stable kernel, verified facts, current target hypothesis, and unknowns that can change ownership, boundary, provider, dependency direction, abstraction, decomposition, or migration commitment. Leave broader implementation discovery to the executable loop.

### 3. Resolve Human decisions

Ask only when evidence cannot settle a material choice that belongs to the user. A choice is Human-owned when evidence-compatible options materially differ in observable outcome, accepted behavior, scope or priority, risk acceptance, approval, or a protected proof rule. If options differ only in implementation How, leave them to the executor. If evidence can decide, ground first.

Normally ask once, with no more than five compact questions. Give 2–4 materially distinct options and one concise recommendation with its basis. Exceed this budget only when omitting a decision would corrupt the Goal or authority.

Do not silently treat a recommendation or default as confirmed. A visibly unconfirmed default is allowed only when it preserves Goal and user-owned Constraints, is bounded and reversible, and makes mismatch detectable. If authoritative evidence proves infeasibility and no meaningful choice remains, return the exact blocker rather than a false question.

### 4. Compile and validate

Compile when the next consumer can start meaningful work without another Human-owned decision, approval, or authority expansion, and the full Goal can be judged from an observable end state, stated evidence, and protected Constraints. Ordinary repo investigation, implementation design, task decomposition, local architecture choices, and replanning do not make intent unresolved.

Before emitting, check that:

- every explicit requested outcome is still present or explicitly superseded;
- facts, inferences, unknowns, recommendations, and Human decisions retain their authority;
- the next consumer can locate or materialize the intended execution target from the artifact plus any explicitly named carrier binding;
- critical commands and baselines are labeled by evidence state;
- the selected control form is the least complex one that can preserve coordination and recovery;
- local task completion cannot be mistaken for global `MET`;
- plausible false-pass routes are frozen when completion trust is material;
- an `UNMET` reason has a safe route back into work, or the artifact names the exact true blocker.

## Executable artifact

Emit `Status: Executable`, then these canonical headings in this exact order. Localize values, not field names:

1. **Goal** — the complete desired end state, not a work list.
2. **State** — the consumer-resolvable execution target or explicit carrier binding, relevant baseline, facts and provenance, evidence/proof state, starting references, completed work, material unknowns, and whether critical gates are verified or unverified. Identify whether the Goal seeks a changed state or a decision-grade answer when that changes evaluation.
3. **Decisions** — only material choices and approvals explicitly confirmed by the user. State “none beyond the request” rather than inventing one.
4. **Constraints** — hard boundaries, invariants, accepted differences, scope/approval limits, priorities needed to resolve conflict, and protected Judge/Population/Object/Metric rules. For repo-changing work, make write scope explicit when leaving it implicit creates material expansion risk. Do not turn convenience into law.
5. **Loop** — `Act → Observe → Evaluate → Next`. Give the first useful direction and authority to create or update the minimum task organization, perform local verification, execute unblocked work, and revise How from evidence. Do not freeze a speculative patch sequence.
6. **Evaluation** — the full Goal condition and direct evidence required for global `MET`. For structured work, distinguish local done evidence from the global Gate. Each iteration returns `MET` or `UNMET` with a short evidence-based reason; compromised or insufficient proof is `UNMET`. When governing or risk-triggered independent acceptance is part of trusted completion, name the accepting boundary: executor evidence can reach only `ready for independent acceptance`, and global `MET` requires that boundary's result.
7. **Output** — the requested deliverable, or the normal deliverable plus a concise receipt. A completion receipt maps Goal conditions to actual evidence and resulting State. A block receipt names unmet conditions, attempted evidence-producing paths, the exact missing authority/evidence, and what would unblock work.
8. **Control** — start, repeat, replan, State update, complexity escalation, complete, and block rules. Start with the least complex sufficient control form; escalate only when coordination, isolation, recovery, or independent challenge requires it. Repeat while `UNMET` and safe evidence-producing work remains. Replan when a path stops reducing uncertainty or remaining Goal conditions. Complete only on trusted global `MET`; block only when no safe next action remains inside settled authority and any explicit budget.

The field boundaries are strict. Goal is the end state; State is territory and proof reality; Decisions records Human authority; Constraints defines what cannot drift; Loop progresses and organizes work; Evaluation judges the whole Goal; Output delivers results and evidence; Control chooses execution complexity and governs repeat/stop.

Task organization stays inside Loop. A simple task may remain one current action and local check. A larger task may use the minimum dependencies and local done conditions needed to expose unblocked work. Durable state or a compiled workflow is justified only when a single context cannot reliably coordinate or recover the task. Independent verification is a risk-triggered proof escalation, not a default execution stage.

For a knowledge, research, or selection Goal, keep the same loop but evaluate decision relevance, source/provenance quality, counterevidence, and material uncertainty instead of inventing code-oriented or numeric completion metrics.

For architecture work, Goal and Evaluation must cover the complete currently requested structural outcome. Repo evidence may revise the hypothesis, design, and task organization inside the loop. An evidence-gathering step or provisional slice is not the final Goal unless the user explicitly made it so.

When uncertainty still prevents this contract, emit `Status: Unresolved` with only the smallest useful Human decision, focused probe, bounded conditional/default, or exact blocker and what could resolve it. Do not pad unresolved intent into the eight-section contract.

If the user requests a fresh-session handoff, save the unchanged selected artifact as Markdown in the operating-system temporary directory, reference existing artifacts instead of copying them, redact sensitive context, and keep any material suggested skills inside Control. Return its absolute path as the delivery envelope; do not emit a second variant in chat.

## Output

In Artifact mode, return exactly one selected outcome and no surrounding analysis. Keep it dense. Brevity is a budget, not permission to omit authority, material State, proof integrity, complexity/stop control, or a requested outcome. In Embedded mode, honor the caller's schema without starting downstream work.
