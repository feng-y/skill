---
name: prompt-atlas
description: Compile a one-sentence goal or scattered, evolving cross-turn hints into an executable agent-facing artifact through two distinct stages. Intent Take recovers and grounds what the user actually wants, preserves settled authority across invocations, and returns a compact unresolved intent surface when a material Human decision still blocks convergence. Once intent is stable, Execution Compile lowers that intent into a small AFK-oriented execution graph with grounded task or issue nodes, closed material branches, real dependencies, verification gates, continuity semantics, and evidence-driven loops. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when another workflow needs intent intake or an executable task carrier.
---

# Prompt Atlas

Prompt Atlas is a two-stage compiler:

1. **Intent Take** — converge on what should be achieved and what must not drift.
2. **Execution Compile** — lower stable intent into a small executable graph that a capable agent can run with minimal Human orchestration.

Keep the stages separate. Stable Intent is compiler input to Execution Compile, not a prose section that gets an execution appendix. Intent Take does not plan implementation. Execution Compile does not reinterpret settled intent.

Assume current frontier models can investigate repositories, choose local implementation How, self-correct, and verify routine work. Compile only semantics that are costly to reconstruct, likely to cause drift, or useful for longer AFK execution. Do not encode generic reasoning procedures, fixed retry counts, fixed agent counts, speculative patch sequences, or workflow ceremony.

Use [contract-anatomy.md](references/contract-anatomy.md) when intent stability or authority is not obvious, [execution-compile.md](references/execution-compile.md) when graph shape or HITL placement is not obvious, and [completion-trust.md](references/completion-trust.md) when a material correctness or completion claim needs stronger proof.

## Stage 1 — Intent Take

### Recover

Recover from the current request, relevant corrections, prior decisions, examples, and any still-valid Atlas artifact. The current user owns intent; current authoritative evidence owns territory; the latest explicit correction supersedes older meaning.

Separate desired outcomes from suggested means and hard constraints. Preserve every explicit requested outcome with its original authority unless the user supersedes it. Evidence may expose prerequisites, wider necessary work inside settled boundaries, stronger proof, or infeasibility; it may not silently weaken, defer, split out, or replace the requested outcome.

Preserve rationale that can change downstream judgment. Keep the underlying problem or design intent when it helps an executor choose correctly among unforeseen but valid implementation paths. Do not carry conversational history merely because it occurred.

### Ground

Investigate only unknowns whose answers can materially change the Goal, user-owned Decisions, Constraints, Success semantics, feasibility, or whether intent is stable enough to compile. Prefer the smallest authoritative check and rich existing references such as code, tests, traces, schemas, artifacts, and rubrics.

For repo work, preserve governing local constraints and acceptance paths when they can change meaning or proof obligations. Capture a sourced baseline when success is relative to current behavior or measurement. Distinguish verified fact, inference, and unknown. Broader implementation discovery remains downstream unless it is needed to understand the request or determine whether the requested outcome is feasible.

### Resolve Human-owned intent

Ask only when evidence cannot settle a material choice whose resolution changes user-owned outcome, accepted behavior, scope or priority, approval, or a protected proof rule. Do not ask merely because the same outcome requires more work, wider necessary implementation scope inside settled boundaries, or a local implementation choice.

Normally expose the smallest useful decision surface with materially distinct options and a concise recommendation. Do not silently convert a recommendation, reversible default, or model preference into confirmed user intent. If authoritative evidence proves the requested outcome infeasible and no meaningful Human choice remains, return the exact blocker rather than a false question.

### Intent readiness

Intent is stable when a downstream compiler no longer needs to rediscover what the user means, what problem is being solved, which outcomes and boundaries are authoritative, or what result and proof would count as success. Ordinary implementation discovery, decomposition, local architecture choices, and execution replanning do not make intent unresolved.

When intent is not stable, stop after returning the best current intent plus the smallest unresolved Human decision, focused probe, bounded conditional/default, or exact blocker. Further convergence requires new user authority or new authoritative territory evidence; repeated rewriting alone cannot promote uncertainty into settled intent.

When intent is stable, treat the resulting semantics as **Stable Intent IR** and continue to Execution Compile. Do not emit a complete Intent Contract and then append execution instructions.

## Stage 2 — Execution Compile

Execution Compile consumes Stable Intent IR and produces one executable artifact. It is semantic lowering plus orchestration synthesis, not another intent pass. Compilation ends when that carrier is delivered: Prompt Atlas does not run the graph, own live execution state, or become the downstream workflow owner.

### Preserve judgment anchors

Carry forward only intent semantics that affect execution judgment:

- the underlying **Purpose / Why** when it prevents directional drift;
- the complete **Goal** and requested outcomes;
- settled Human decisions and hard boundaries;
- relevant grounded State, baselines, and proof obligations;
- the required delivery or completion semantics.

Transform these into the executable representation rather than duplicating the Intent IR verbatim.

### Ground execution reality

Ground enough execution territory to make the first graph truthful rather than speculative. Locate the actual repo/workspace or carrier binding, inspect the work surfaces and governing specifications that determine node boundaries or dependencies, and verify critical baselines, acceptance paths, or commands when accessible. Prefer references to rich existing specs over copying them.

Do not pretend an unavailable command, environment, baseline, or verifier was checked. Mark it unverified and either compile its verification as initial ready work or expose a real blocker when no safe work can start. This grounding is for orchestration truth; it must not reopen settled Intent.

### Close material execution branches

Before execution, identify unresolved choices whose alternatives would materially produce different task or issue graphs, dependencies, verification paths, scope, or architecture direction. Resolve them from settled intent, governing constraints, and authoritative evidence when possible.

If materially different execution graphs remain equally compatible with the settled intent and current evidence does not select among them, expose that decision as pre-execution HITL and stop. When the caller explicitly requires an executable carrier without another Human turn, a bounded unconfirmed execution default is allowed only when it preserves settled Goal and boundaries, is reversible or mismatch is reliably detectable, and is labeled as an assumption with its consequence; otherwise return `Status: Execution Decision`. This is branch closure, not Human orchestration. Do not ask for local, reversible implementation How that the executor can choose without changing the graph materially.

Record material closed branches with their basis; distinguish Human-confirmed choices, governing constraints, evidence-grounded execution decisions, visibly unconfirmed defaults, and non-binding guidance from executor-owned How.

### Compile a small execution graph

Compile the minimum graph that is useful to start and remain AFK:

- **Task / Issue nodes** are bounded work units with an outcome, relevant context, real dependencies, applicable boundaries, and local verification.
- **Edges** represent real dependency or evidence flow. Do not serialize independent work merely because prose would say “then.”
- **Checkpoints** decide local node completion or route work back for repair.
- **Global Gate** judges the complete Goal; local done must never imply global completion.
- **Human Gate** appears only for a newly exposed material branch that cannot be safely closed from intent or evidence.

Prefer a small or lazy graph. Do not predict the whole implementation when later evidence can refine it. Independent work may fan out; real dependencies remain ordered; completed trustworthy nodes should not be repeated merely because the remaining graph changes.

When parallel work shares mutable surfaces, compile enough ownership to avoid coordination HITL: keep write domains disjoint where possible, give each shared write surface one owner, make joins explicit, and invalidate/re-run evidence when an upstream change makes downstream proof stale. Runtime agent count remains an execution choice unless the user fixed it.

### Compile loop and continuity semantics

Each ready Task / Issue runs as an evidence-driven loop:

`Act → Observe → Evaluate → Next`

A failed local check routes first to diagnosis, a different How, or local replanning. Failure alone is not HITL. A blocked or Human-gated node is parked while independent ready work continues; the whole graph is blocked only when no safe ready work remains.

The graph runtime selects ready work, executes node loops, incorporates evidence, and may revise the remaining graph when observations invalidate the current execution theory. If the work may outlive one context, require recoverable execution state at the semantic level—trusted completed nodes and evidence, parked blockers or decisions, and next ready work—without mandating a particular progress file or runtime storage mechanism.

Continue while the Goal is not yet proven and safe evidence-producing work remains inside settled boundaries. Complete only when the Global Gate is satisfied by trusted evidence. Stop for Human input only when continuation truly requires closure of a material unresolved branch; stop as blocked only when no safe next action remains or required evidence/authority is genuinely unavailable.

## Executable artifact

Do not optimize for a particular field count. The final carrier must make the following semantics explicit enough that a fresh capable executor can act without re-deriving them:

- **Purpose** — the problem or design intent that should guide judgment when unplanned choices appear;
- **Goal** — the complete desired end state;
- **State** — the resolvable execution target, relevant grounded facts, baseline, evidence state, and starting references;
- **Decisions** — material execution branches already closed, with authority or evidence basis;
- **Graph** — the current Task / Issue nodes, real dependencies, local completion conditions, ownership where parallel work can collide, and enough initial ready work to start;
- **Boundaries** — hard scope, behavior, architecture, approval, and protected proof invariants; keep non-binding guidance visibly separate;
- **Verification** — local proof obligations and the trusted Global Gate, including any required independent acceptance boundary;
- **Runtime** — node-loop, graph-update, partial-block, recovery, continuity, HITL, completion, and true-block rules;
- **Delivery** — the requested deliverable or the executor's normal deliverable plus a concise evidence receipt.

The serialization may be compact and task-shaped. Do not add empty ceremony merely to fill headings, but do not compress away a semantic distinction that prevents drift, false completion, unnecessary HITL, or loss of AFK continuity.

For a simple task, the graph may be one work node plus verification and the Global Gate. Add structure only when real dependency, coordination, proof, or recovery needs it. For research or decision work, compile evidence-bearing probe/source-review/synthesis/comparison nodes; completion should report the best supported answer, provenance, material counterevidence or residual unknowns, and any exhausted direction that was ruled out with evidence rather than forcing code-style hard metrics.

If a fresh-session handoff is requested, save the selected executable artifact unchanged as Markdown in the operating-system temporary directory, reference existing artifacts instead of copying them, redact sensitive context, and return the absolute path.

## Output

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current best intent plus only the decision, probe, conditional/default, or blocker needed for further Intent Take.
- **`Status: Execution Decision`** — Stable Intent exists, but one material execution branch still needs closure before a useful graph can be compiled and no safe unconfirmed execution default applies.
- **`Status: Executable`** — one executable artifact produced by Execution Compile.

For `Status: Executable`, do not prepend the Stable Intent IR or append a second execution variant. Keep the carrier dense and agent-facing. Delivery ends Prompt Atlas; the downstream executor owns graph runtime and live state. Brevity is a budget, not permission to omit Purpose, authority, a material graph branch, verification integrity, or a requested outcome.