# Intent artifact quality

Use this reference when executable-contract quality is not obvious. Add detail only when it changes loop behavior or judgment. This is a quality reference, not a second intake workflow.

Sections: [Goal attainment](#goal-attainment) · [Canonical structure](#canonical-structure) · [Outcome shape](#outcome-shape) · [Minimum control form](#minimum-control-form) · [Task and state semantics](#task-and-state-semantics) · [Architecture work](#architecture-work) · [Control quality](#control-quality) · [Stability](#stability)

## Goal attainment

An artifact is sufficient when a capable consumer can start and sustain the Goal Loop without re-deriving what the user means. Preserve the desired end state, material territory/proof state, Human authority, hard boundaries, action freedom, trusted evaluation, delivery shape, and repeat/stop control. Prefer authoritative references over prose that restates them.

Explicit requested outcomes are not disposable implementation suggestions. Grounding may add prerequisites, expand necessary work inside settled authority, strengthen proof, or expose infeasibility. It must not silently defer, weaken, or replace an outcome. A later turn changes user-owned intent only through new user authority; new evidence changes territory, feasibility, proof, or revisable Architecture Intent.

## Canonical structure

Emit `Status: Executable`, then:

1. **Goal** — complete desired end state;
2. **State** — current territory and proof reality;
3. **Decisions** — confirmed Human authority;
4. **Constraints** — what cannot drift or be crossed;
5. **Loop** — action progression and dynamic task organization;
6. **Evaluation** — local/global evidence and `MET` / `UNMET`;
7. **Output** — deliverable and completion/block receipt;
8. **Control** — complexity, repeat, replan, recovery, and stop.

Do not flatten the fields:

- State may challenge feasibility but does not silently become intent, a decision, or a constraint.
- Decisions never contains model recommendations, guesses, defaults, or repo facts.
- Loop may revise implementation How and task structure, not Goal or Human authority.
- Evaluation judges the whole Goal. A local check, build, lint pass, file edit, report, or partial slice is not global `MET` unless it directly proves the requested end state.
- Output reports the result and evidence; it does not define correctness.
- Control changes the execution carrier or next action, not the completion bar.

Protected judging rules belong in Constraints; evidence produced under those rules belongs in Evaluation. For example, “replay/diff may not be replaced by build-only evidence” is a Constraint, while “affected replay/diff paths show no unexpected difference” is Evaluation.

## Outcome shape

Use one Goal Loop for both outcome shapes:

- **Changed state** — Evaluation needs direct evidence of the requested behavior/result and any protected regression boundary.
- **Decision-grade answer** — Evaluation needs evidence coverage, provenance, relevant counterevidence, material uncertainty, and a result that supports the requested judgment. Do not invent a numeric target or code-change checklist for exploratory work.

When one Goal contains both, evaluate both. Do not let a research report replace a requested implementation, or an implementation replace a requested decision rationale.

## Minimum control form

Choose inside Control; do not add a top-level route:

1. **Direct loop (default)** — one executor, one current action, one local check, and the global Gate. Use when work fits one context and has no material coordination or recovery need.
2. **Structured loop** — the minimum task graph or compiled workflow needed for real dependencies, independently verifiable work, conflicting write surfaces, or coordination that one context cannot reliably hold. Each node has a local result, dependency, and evidence consumed downstream.
3. **Durable loop** — structured work plus a persistent execution ledger when work crosses sessions, waits on external state, spans multiple PRs, or otherwise must recover beyond the runtime's native context.

Escalate only on observed need. Collapse back when extra structure no longer changes correctness, coordination, or recovery. Agent count, model choice, exact parallelism, and workflow implementation remain runtime decisions unless the user made them part of intent.

Independent challenge is orthogonal to these three forms. Trigger it from proof risk: executor-designed acceptance, a plausible false pass, behavior-preserving migration, architecture work with material residual risk, a critical user path, or a governing requirement. Do not require a verifier for every routine change.

If the runtime parallelizes, give concurrent writers non-overlapping ownership, assign one owner to shared artifacts, and re-establish evidence invalidated by later integration. Do not precompile a multi-agent topology when no such execution choice has been made.

## Task and state semantics

Task organization is runtime state, not frozen Intent:

- direct work keeps one current action and its local done evidence;
- structured work creates only enough tasks, dependencies, and local done conditions to expose the next unblocked action;
- before structured execution, reconcile that every Goal condition and protected proof obligation has an execution or global-evaluation path, dependencies consume real upstream results, and at least one safe node is ready;
- after observing a result, write completed evidence, current gaps, and next action into the runtime's available state;
- replace planned tasks when evidence changes How, while preserving Goal, Decisions, Constraints, and Evaluation;
- if initial repo detail is insufficient, ground and reconcile the task organization first, then continue; investigation is not the final deliverable unless the Goal asks for it.

A local Gate answers whether one node produced trustworthy evidence usable by downstream work. The global Gate answers whether every current Goal condition is satisfied under Constraints. Only the global Gate can return `MET`.

## Architecture work

Architecture work is Executable when its requested structural outcome, governing kernel, boundaries, and Evaluation are clear enough for repo evidence to refine the design inside the same loop:

- **Goal / Constraints** freeze business outcome, behavior invariants or accepted differences, compatibility and approval boundaries, and only confirmed/governing architecture principles.
- **State** distinguishes verified structural facts and provenance, the current target hypothesis, and unknowns that can change ownership, boundary, provider, dependency direction, abstraction, decomposition, or migration commitment.
- **Loop** continues toward the complete requested structure while allowing evidence to revise design and task organization.
- **Evaluation** covers the full structural result, preserved behavior, and direct proof. A provisional slice cannot receive global `MET`.
- **Output** includes the structural deliverable and verification receipt; include an Architecture Intent delta only when target-shaping hypotheses changed materially.

An incremental stage is the Goal only when the user explicitly requested or approved that stage.

## Control quality

Control makes loop boundaries predictable:

- **Start** — begin the first evidence-producing action from the whole contract.
- **Repeat** — while global Evaluation is `UNMET`, feed its reason into State and select a safe next action.
- **Replan** — when observations invalidate How or an action stops reducing uncertainty/remaining Goal conditions, change the path rather than repeat it mechanically.
- **Recover** — preserve completed evidence, current gaps, and next action at the durability level selected above.
- **Complete** — stop only on trusted global `MET`.
- **Block** — stop only when no safe next action can proceed inside settled authority and explicit budget, including when continuation requires a new Human decision, permission, authority expansion, or unavailable required external evidence.

If the user or runtime supplies a time, token, attempt, or cost budget, preserve it in Control. Do not invent fixed counts. Without a numeric budget, use evidence gain as the cost guard: repeated work that produces no new evidence and closes no Goal condition must replan, reduce scope only with Human authority, or end honestly unresolved when no viable path remains.

Difficulty, task size, a failed attempt, or `UNMET` is not itself a blocker.

## Stability

Compression, later evidence, carrier changes, and later alignment turns may enrich the artifact but must preserve:

- Goal, explicit outcomes, confirmed Decisions, user-owned priorities, and user-owned Constraints until new user authority changes them;
- fact/inference/unknown and verified/unverified distinctions;
- recommendations as advisory and defaults as visibly unconfirmed;
- current territory facts according to the best authoritative evidence;
- target state separately from current proof state;
- runtime freedom over implementation and task organization;
- the requested Output shape;
- proof obligations and the global completion bar.

The artifact is consumer-ready when the next consumer does not need to reinterpret the Goal, rediscover material State or authority, invent the evaluator, guess whether a partial result was accepted, choose an execution carrier blindly, or infer repeat/stop rules.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).
