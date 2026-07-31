# Stable Intent IR

Use this reference when Stage 1 authority, Goal closure, or stability is not obvious. Stable Intent is source semantics for Execution Compile, not an executor-facing taskbook.

## What to preserve

Keep only information that can change downstream judgment:

- the desired end state and underlying problem;
- decision-relevant **Why / design intent**;
- current territory facts, provenance, evidence state, and material unknowns;
- Human-confirmed choices, priorities, approvals, and boundaries;
- current task scope when it differs from the broader Goal;
- observable success and trusted proof semantics;
- requested delivery semantics when material.

Conversation history, rejected reasoning, and implementation detail are context only when they still affect one of those semantics.

## Authority

Keep these classes distinct:

- **User-owned intent** — requested outcomes, accepted behavior, confirmed decisions, core scope and boundaries, Human-owned priorities/trade-offs, approvals, protected proof requirements, and any decision-relevant Why / design direction explicitly made part of the request. These change only with new user authority.
- **Territory reality** — authoritative code, tests, traces, schemas, artifacts, measurements, and other evidence. Better evidence may revise facts, feasibility, necessary work inside settled boundaries, and proof obligations without rewriting intent.
- **Inference / recommendation** — useful judgment, including a model-proposed candidate Goal, but not settled authority.
- **Unknown** — unresolved until evidence, a safe delegated decision, or Human authority settles its material consequence.

An explicit requested outcome remains authoritative even when grounding reveals more work, stronger proof, or higher cost. If it cannot be preserved inside settled boundaries, surface the conflict rather than silently weakening the outcome.

## Why / design intent

Preserve rationale when it helps a later executor choose among unforeseen but valid paths. A useful Why names the underlying problem, undesirable property, or desired direction beyond the literal surface edit. Drop rationale that only narrates how the conversation arrived here.

A design direction is Human-owned only when the Human made it part of the desired result, boundary, or decision-relevant Why. Routine architecture and implementation choices remain downstream How when they preserve those semantics.

## Grounding

Ground the smallest set of unknowns needed to establish meaning, feasibility inside settled authority, Goal closure, or success/proof semantics. Prefer authoritative evidence and rich existing references.

For repo work, preserve governing constraints or acceptance paths when they affect meaning or proof, and capture a sourced baseline when success is relative to current behavior. Leave work-surface discovery, dependency mapping, command validation, and implementation design to Execution Compile unless they are required for intent stability.

Grounding should reduce the Human decision surface, not replace it. Close context/reality unknowns from evidence when possible, then rescan what remains. Do not ask the Human for facts that authoritative evidence can settle; do not keep researching merely to avoid surfacing a remaining non-delegable Human-owned choice.

When the required evidence is accessible in the current turn, perform the focused check rather than returning a research instruction to the Human. Surface a probe as the remaining alignment item only when it cannot be performed now, requires unavailable authority/access, or the caller explicitly requested a probe plan rather than convergence.

Separate an authoritative scope rule from factual membership. The Human may define what qualifies, prioritize categories, or name explicit inclusions/exclusions while expressing only a tentative belief about which concrete entities satisfy that rule. Preserve the rule and explicit decisions as authority; treat tentative membership as a territory hypothesis. Derive the member set from evidence at the first stage where it affects judgment: in Intent Take when it could change Goal closure or a Human decision, otherwise in Execution Compile when it determines concrete work. Retain enough provenance to defend each material classification, and surface only residual cases whose classification depends on Human-owned semantics rather than observable reality.

## Unknown routing

Unknown is a mechanism for reducing unnecessary Human questions, not for eliminating Human judgment.

Route it by consequence:

- if evidence can settle it, investigate instead of asking;
- if it changes only reversible implementation How, preserve it for execution rather than closing it during Intent Take;
- if it may change execution theory but not Stable Intent, let execution probe and replan;
- if Goal and all Stable Intent boundaries are settled and a reasonable choice is reversible or reliably mismatch-detectable, let Execution Compile make a **visible delegated decision**;
- if the remaining material consequence changes the requested outcome, accepted behavior, core scope, core boundaries, Human-owned priority/trade-off, approval, protected proof, or confirmed design intent, ask the smallest Human decision needed;
- if required evidence or authority is unavailable, preserve the exact unknown and the probe or condition that could resolve it.

A delegated decision is not Human-confirmed intent. Record it as visibly unconfirmed with its basis, consequence if wrong, and detection or rollback path. It may close execution orchestration while preserving Human authority.

Necessary implementation expansion inside settled scope and boundaries is not a scope decision. Redefining what is included, excluded, protected, or accepted is intent-shaping even when the change is technically reversible.

Do not convert every unknown into HITL. Equally, do not hide an intent-shaping Goal-, behavior-, scope-, boundary-, trade-off-, approval-, proof-, or confirmed-design decision behind “the compiler chose” or “the executor can decide.” The purpose is to ask the Human less often and more precisely, not to screen the Human out.

## Goal closure

A Goal is closed when existing Human authority establishes one coherent requested end state and the boundary of what this turn is expected to accomplish. It need not settle implementation How or every broader future decision.

A prompt may instead expose a problem space: concern, hypothesis, competing questions, possible end states, or active Human deliberation. When missing reality could materially change which Goal is sensible, do not treat every question as requested execution scope and do not choose a Goal merely because one path looks useful.

Reduce only the decision-relevant context unknowns needed to make the choice meaningful. Then return the sharper problem model, the smallest materially distinct candidate Goal or options, their consequences, and a recommendation. A candidate Goal proposed by the model remains inference until a subsequent Human message confirms, selects, or corrects it; self-review, more research, or repeated wording cannot promote it to Stable Intent.

On that subsequent Human message, reconcile it against the candidate and preserved evidence rather than restarting discovery. Confirmation or selection closes that Goal; correction updates it; a partial or still-deliberative response keeps only the remaining decision surface open. Reuse still-valid facts and decisions.

Do not over-block execution. If the Human has already established a complete minimum outcome, broader questions, later go/no-go decisions, or implementation unknowns remain separate from the current Goal rather than reopening settled authority.

## Human and delegated decisions

Before declaring intent stable, actively check whether any unresolved choice still belongs to Human authority and would materially change the requested outcome, accepted behavior, core scope, core boundaries, Human-owned priority/trade-off, approval, protected proof, or confirmed design intent.

When such a choice remains, expose the smallest useful decision surface: materially distinct options, the consequence that makes them different, and a concise recommendation. Related unknowns may be resolved or compressed first, but inference, recommendation, delegated choice, or model preference must not silently erase the remaining Human choice.

More work, wider necessary implementation scope inside settled boundaries, several valid implementation approaches, or future replanning do not by themselves require Human input.

A delegated default is allowed only after the Goal and all intent-shaping boundaries are closed and when it preserves them, has an evidence-backed or convention-backed preferred choice, and is reversible or safely mismatch-detectable. It cannot form or reinterpret Goal, redefine core scope, relax a core boundary, change a Human-owned trade-off, replace confirmed design intent, or authorize a protected/high-risk action.

For **artifact-only** handoff, the carrier may include a broader visible recommended default because the caller can review or change it before execution. For **compile-and-run**, only a default safe enough to execute without another Human turn may close the branch. In both modes, keep the decision visibly unconfirmed and state its basis, wrong-choice consequence, and mismatch/rollback path.

If evidence proves the requested outcome infeasible and there is no meaningful Human choice, return the blocker rather than manufacturing a decision.

## Intent convergence runtime

Intent Take runs as an interactive compile-time convergence loop. It may use available tools and Human turns, but it does not need the later execution Graph or execution continuity state.

Across turns, recover only the semantic state needed to continue:

- the current candidate or confirmed Goal;
- Human-confirmed authority and boundaries;
- still-valid evidence and material unknowns;
- the smallest remaining Human decision surface or unavailable probe.

Each new Human message or authoritative fact updates that state: reconcile it with the current candidate, preserve still-valid facts and decisions, and remove only the choices that are actually closed. Do not restart discovery merely because a new turn began, and do not retain the whole conversation when these semantics are recoverable directly.

The loop exits only when Stable Intent is reached or the smallest unresolved decision/probe/blocker has been returned. Execution Compile is the next semantic runtime; it is not another iteration of Goal formation.

## Stability

Stable Intent is sufficient when Execution Compile no longer needs to rediscover:

- the problem and complete requested outcome;
- Human-authoritative choices and all intent-shaping boundaries;
- which material facts are verified, inferred, or unknown;
- what trusted success means;
- delivery semantics that must survive lowering.

It also requires that the Goal is closed and the Human-decision scan finds no unresolved non-delegable intent-shaping choice. Context and execution unknowns may remain when they do not change those source semantics and can safely be investigated, delegated, or resolved downstream.

Implementation discovery, decomposition, dependency mapping, local architecture How, execution topology, command order, retries, and runtime state remain Stage 2/runtime concerns unless resolving them would change those source semantics.

When intent is not stable, perform any accessible focused grounding first, then return the best current understanding plus only the smallest remaining alignment surface. If unavailable decision-relevant reality is missing, surface the focused probe or blocker. If Goal closure or another non-delegable intent-shaping decision remains, ask explicitly with options, consequences, and recommendation. New user authority or authoritative evidence can move intent forward; rewriting alone cannot turn uncertainty into fact or authority.

## Boundary with Execution Compile

Execution Compile may ground implementation territory, close material execution branches with evidence or safe visible delegated decisions, derive work boundaries and dependencies inside Stable Intent, and lower proof semantics into execution shape. It may not form, reinterpret, or self-authorize any Stable Intent semantic.

If Stage 2 evidence shows that Stable Intent cannot be preserved or requires a new Human decision about Goal, accepted behavior, core scope or boundaries, Human-owned trade-offs, approval, protected proof, or confirmed design intent, that is an Intent Take re-entry, not an Execution Decision.

The final executable artifact contains only the lowered semantics that matter to execution judgment; it is not Stable Intent followed by an execution appendix.
