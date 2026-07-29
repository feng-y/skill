# Intent artifact quality

Use this reference when intent-artifact quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

An artifact is sufficient when the next consumer can start and sustain the goal loop without re-deriving what the user means. Preserve only what can change loop behavior or judgment: the desired end state, current territory and proof state, Human authority, hard constraints and approvals, action freedom, trusted evaluation evidence, required delivery shape, and repeat/stop rules.

A repo-scoped artifact is incomplete when an authoritative local constraint or acceptance rule can materially change Constraints, Evaluation, or completion but is left for the next consumer to rediscover. Preserve the governing requirement, not a speculative execution procedure.

Prompt Atlas supports iterative alignment but does not own continuation across turns. Each invocation should produce the best current artifact or the smallest useful decision surface and stop. A later user turn may improve intent fidelity when it supplies new user authority. New territory evidence, changed external constraints, or downstream results may improve grounding or expose mismatch, infeasibility, or missing proof, but do not by themselves change user-owned intent. Repeated self-refinement on the same information may improve consistency, completeness, or expression, but is quality review rather than evidence of intent convergence.

Explicit requested outcomes are part of intent authority, not disposable implementation suggestions. Grounding may add prerequisites, widen necessary implementation or verification scope within existing user-owned boundaries and approval limits, expose higher cost, or prove an outcome infeasible; it must not silently turn “do this now” into “defer this,” “split this out,” or “do a weaker version.” If preserving the outcome requires crossing a user-owned boundary or approval limit, or evidence otherwise cannot resolve the conflict while preserving the outcome, the artifact is not stable until the user resolves the material choice or the result honestly closes on a blocker with no meaningful choice available. A stable artifact must preserve every explicit user-owned outcome with its original authority unless later user authority supersedes it.

Prefer material State over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More context or prose does not improve the artifact unless it changes downstream judgment or removes a material failure mode. Compile the loop's authority and control semantics, but let the runtime organize concrete tasks, execute tools, and update the plan from repo observations.

## Agent-facing structure

In Executable Artifact mode, structure is part of contract correctness rather than presentation preference. Emit `Status: Executable`, then use stable canonical field names across languages and localize the values. The carrier uses this exact semantic order:

1. **Goal** — desired end state and real problem to solve;
2. **State** — current baseline, relevant territory facts, evidence/proof state, starting references, completed work, and material unknowns;
3. **Decisions** — only material Human-confirmed choices or approvals;
4. **Constraints** — hard boundaries, invariants, acceptable differences, scope/approval limits, and protected judging/oracle rules;
5. **Loop** — the `Act → Observe → Evaluate → Next` directive and dynamic task-organization authority;
6. **Evaluation** — the evaluator-visible Goal condition, direct proof, and `MET` / `UNMET` feedback rule;
7. **Output** — required downstream deliverable/response shape, final evidence, resulting State, and real blockers;
8. **Control** — start, repeat, replan, State update, complete, and block rules.

These fields encode different roles and authority and must not be flattened into one prose summary:

- **Goal** answers “what state should be true when this succeeds?”; include motivation only when it materially changes that state or downstream judgment;
- **State** may challenge feasibility but does not silently become intent, a Human decision, or a constraint;
- **Decisions** contains only Human authority, never model recommendations, guesses, reversible defaults, or repo facts;
- **Constraints** defines what downstream may not violate or cross; implementation inconvenience is not a constraint;
- **Loop** owns action progression and dynamic task organization, but cannot silently weaken or split away the Goal;
- **Evaluation** defines observable completion, trusted evidence, and the unmet reason that feeds the next action; target state and proof state remain distinguishable;
- **Output** defines the final deliverable and evidence report, not the judge;
- **Control** owns repeat and stop semantics, not Goal meaning.

For verification, keep protected judging rules separate from evaluation evidence. For example, “replay/diff may not be replaced by build-only evidence” belongs in **Constraints**; “the affected replay/diff paths pass with no unexpected difference” belongs in **Evaluation**.

This structure aligns with current goal-loop behavior: an explicit condition, current State, actions, observations, evaluator feedback, and repeat/stop control. Keep the contract dense enough to execute in a fresh session without freezing concrete patch sequencing, exact command order, retry counts, or executor topology.

An Executable Goal Loop Contract should be usable as one self-contained input unit in a fresh consumer session. Do not require the Human to extract a condition, add a separate “please implement” prompt, or decide which subset to pass downstream. This fixed structure applies only after intent and required grounding are sufficient for safe, measurable work; unresolved Human decisions, blocking probes, or real blockers remain the smaller `Status: Unresolved` output. Embedded mode may use a caller-owned schema.

## Executable quality

An Executable Goal Loop Contract has enough information for the consumer to own the outcome rather than merely produce a plan. Include, when material:

- the measurable end state and every explicit requested outcome;
- the current baseline, authoritative references or entry points, and evidence state needed to begin;
- confirmed Human decisions, write or approval scope, invariants, accepted differences, and non-goals;
- action authority that permits repo investigation, implementation, dynamic task organization, and replanning without prescribing a patch sequence;
- direct proof obligations and evaluator checks that distinguish `MET` from a plausible-looking partial result;
- feedback semantics that turn an `UNMET` reason into the next action;
- the expected deliverable, resulting State, concise completion evidence, and any true remaining blocker.

The Evaluation must form a durable goal condition: one observable end state, the check or evidence that demonstrates it, and the Constraints that must remain true. Map each explicit requested outcome to at least one observable result or proof obligation. Do not allow a build, lint pass, file edit, analysis document, or implementation summary to stand in for requested behavior unless it directly proves that behavior.

## Dynamic task organization

Task organization is a runtime expression of the loop, not frozen Intent:

- for a small task, maintain one current task and its local done condition;
- for a larger task, create the minimum tasks, dependencies, and local done conditions needed to expose the next unblocked action;
- after each observation and Evaluation, update completed evidence, current State, and the next action;
- revise or replace planned tasks when repo evidence changes How, while preserving Goal, Decisions, Constraints, and Evaluation;
- when initial State lacks implementation detail, ground and reconcile the task organization first, then continue within the same loop rather than returning an analysis deliverable.

Do not preassign agent topology or parallelism. The runtime may parallelize independent work when current evidence supports it.

## Architecture work

Ordinary implementation unknowns do not block Executable status. Architecture work is also Executable when the requested structural outcome, stable kernel, boundaries, and Evaluation are clear enough for repo evidence to refine the design inside the same continuing loop. In that case:

- **Goal / Constraints** — freeze the business outcome, behavior invariants or accepted-difference boundaries, compatibility boundary, approval limits, and only user-confirmed or authoritative governing architecture principles; do not promote inferred design preferences into hard constraints.
- **State** — distinguish verified architecture facts, their provenance, the current Architecture Intent, and unknowns that can still change owner, responsibility boundary, provider, dependency direction, target abstraction, structural decomposition, or migration commitment.
- **Loop** — direct work toward the complete currently requested structural outcome while letting observations revise the design and task organization; do not replace the requested outcome with one provisional slice.
- **Evaluation** — cover the full requested structural result, preservation of settled behavior invariants and accepted-difference boundaries, and direct verification. New evidence may revise the design or plan, but it does not authorize early `MET` on a partial result.
- **Output** — require the normal structural deliverable and concise verification evidence. Include an Architecture Intent delta and provenance only when target-shaping hypotheses materially changed during execution.

An incremental stage may be the Goal only when the user explicitly requested or approved that stage. Otherwise evidence gathering and intermediate structural changes are loop iterations toward the full Goal. If no safe next action toward the full requested outcome exists without a new Human-owned decision, the result is unresolved rather than an analysis-only or partial-delivery contract.

## Control quality

Control must make the goal loop deterministic at its boundaries:

- **Start** — pass the entire contract as authoritative input and begin the first useful action immediately;
- **Repeat** — while Evaluation is `UNMET`, feed its evidence-based reason into State and select the next action;
- **Replan** — update runtime task organization when observations change How; never silently change Human-owned intent;
- **State update** — retain completed work, evidence, current gaps, and next action in the runtime's available task/progress state so later iterations do not restart;
- **Complete** — stop only when Evaluation returns trusted `MET`;
- **Block** — stop only when no safe next action remains without a new Human-owned decision, permission, authority expansion, or unavailable required external evidence.

Difficulty, task size, an incomplete first attempt, or an `UNMET` evaluation is not a blocker. Do not stop at research, a plan, a partial patch, or a completion claim without evidence. The runtime may realize this Control through its native agent loop, `/goal`, Leader, or an equivalent carrier.

Control must not restate the whole contract, invent a requirement, weaken a proof obligation, or freeze the downstream plan.

## Stability

Compression, handoff, later evidence, and subsequent alignment turns may enrich the artifact but must not silently change authority or state:

- Goal, explicit requested outcomes, user-owned priorities, confirmed Decisions, and user-owned Constraints change only with new user authority;
- still-valid settled semantics from a prior Atlas artifact provide the baseline for a later alignment turn; inferred, unknown, or unverified state remains such until authority or evidence changes it;
- State facts follow current authoritative evidence and may change with better evidence without rewriting user-owned intent;
- downstream results or feedback may reveal mismatch, infeasibility, or missing evidence, but do not by themselves override a confirmed decision or requested outcome;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting or repeated self-review;
- superseded meaning is replaced rather than accumulated beside current intent;
- runtime implementation judgment and task organization stay revisable unless the user makes one part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable;
- Output changes only when the user or named consumer changes the required delivery shape, not because Atlas prefers a different presentation.

Shortening, self-review, carrier adaptation, or handoff guidance removes redundancy and improves usability; it does not create new authority. None may change settled intent, erase uncertainty, weaken proof obligations, or blur the distinction between target and current state.

The artifact is consumer-ready when the next consumer does not need to reinterpret Goal, rediscover current State or a settled Decision, infer who owns a Constraint, guess whether an explicit requested outcome was silently deferred, invent the evaluator, infer the desired Output, or guess when to repeat or stop.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).
