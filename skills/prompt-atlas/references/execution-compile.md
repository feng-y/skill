# Autonomous Taskbook

Use only after Goal is stable. Produce one compact authoritative taskbook an Executor can run without ordinary Human orchestration.

Keep the taskbook structure and semantic ownership fixed. Compile only context that constrains a future decision, execution step, Verification requirement, or Evidence judgment. Keep large supporting material by reference; state global facts once and Task-local differences locally. Do not recompile Goal / Execution / Verification / Evidence into a separate completion or acceptance model.

## Verification granularity

For development work, keep three meaningful Verification granularities without adding workflow stages:

- **Task-level Verification** — the cheapest sufficient check for one local behavior, reaching the nearest valid repo-verification boundary that directly covers the affected behavior;
- **Task-Group Verification** — broader verification at the smallest join or combined boundary where a coherent set of Tasks establishes behavior, a shared contract, migration slice, or dependency result that local checks cannot prove;
- **Goal-level Verification** — after relevant work converges, confirm that repo-required verification for the declared delivery is sufficiently covered by still-valid Evidence. This is a final coverage boundary, not a mandatory extra final command; reuse valid Task / Task-Group Evidence and run only required checks still uncovered or invalidated.

Lower-level PASS may unlock downstream work but cannot replace broader behavior that genuinely needs verification. Verification cost changes cadence and reuse, not whether required verification may be omitted.

## Repo verification authority

Before Handoff, read repo verification authority for the expected change surface. Derive required Verification from Goal, actual impact/reachability, material failure risk, and explicit Human verification requirements. Human verification requirements are binding Verification input; they are not Goal semantics and cannot be downgraded by Prompt Atlas or Executor.

Trace changed owner, shared responsibility, or system contract to effective binding/config and affected target/capability. When production binding authority exists, follow effective production configuration and real consumers. Known facts that trigger required Verification make it non-negotiable; “only cleanup/refactor” or expected `0-diff` cannot downgrade it. Put execution-only trigger derivation in Task 0 and state the Verification that becomes required when triggered.

Select concrete test/build/replay/static/symbol or other evidence providers from the repo verification system. A provider proves only what it actually covers. Do not default to a fixed bundle or enumerate checks for appearance. A documented command is only a claim until availability and signal propagation are evidenced; check before Handoff when possible, otherwise Task 0 owns it.

Research, selection, and decision work use the same structure: Execution contains evidence-producing investigation rather than implementation. Conclusions need source/date or a reproducible probe; fabricated citations, unrun measurements, and filler findings are failure.

## Contract Header

State briefly:

- this taskbook is the execution source;
- the one Human-owned Goal, including what success must make true and what must remain true;
- Why and the completed world;
- explicit Human verification requirements, if any, plus the Goal-level verification coverage that must be established;
- priority order when requirements conflict;
- hard rules versus guidance.

Goal itself defines success. Do not add a `Completion Contract`, completion properties, or another done taxonomy. Verification constrains how the Goal is proved; it does not redefine the Goal. State an execution stop budget only when one actually exists.

## 1. Delegated Decisions

Place compiler-owned reversible defaults here, before boundaries and execution, so Human authority remains visible.

Render each permitted delegated default as: decision → unconfirmed default → basis → cost if wrong → detection or rollback.

If none remains, state `None`; do not invent a choice to fill the section.

## 2. Boundaries and Authority

State expected write scope, protected no-write boundaries, and any authority-sensitive operations. The Executor may expand implementation scope when evidence proves it is necessary to reach Goal and sufficient Verification, provided confirmed boundaries, Human authority, and required Verification remain unchanged; material expansion must be visible in execution Evidence.

Bound dependency additions/upgrades, permissions, external-system writes, destructive actions, and other irreversible side effects. Name protected tests, schemas, verification scripts, CI, baselines, and other repo judges that must not be weakened. Call out tempting side work outside Goal.

State what the Executor may decide inside Goal, confirmed boundaries, authority, and required Verification. Actions beyond authority become an explicit blocker. Return to Intent Take only when safe continuation would require changing Goal, a confirmed boundary, explicit Human verification requirement, priority, or authorization. `Status: Blocked` applies only when no safe work remains.

## 3. Current Reality and Task 0

Record evidenced facts and baselines; mark unverified claims. Reuse the repository/runtime's normal implementation record when available; Prompt Atlas does not require a dedicated progress artifact.

When Task 0 is needed, it runs before material change. It binds the real repo/worktree/target, verifies critical commands and judges, detects no-op or false-green checks, and surfaces material mismatch between taskbook assumptions and execution reality. Evidence may revise facts, feasibility, implementation scope, remaining Tasks, Graph, and Verification needs; it may not redefine Goal.

If Task 0 owns a Verification trigger, resolve current changed owner/shared contract → effective binding/config → affected target/capability. Triggered Verification becomes required; an untriggered path needs evidence that the gate is inapplicable. If actual change surface or effective binding changes later, recompute Verification scope from repo authority.

When reality differs:

- correct a clear misreading that does not alter Goal/boundaries, then continue;
- if Goal and boundaries still hold, update remaining Execution / Graph;
- if a branch is blocked but independent safe work remains, park only that branch;
- if no safe work remains, return `Status: Blocked` with the exact resolving condition;
- if continuation requires changing Goal, confirmed boundaries, Human verification authority, priority, or authorization, return to Intent Take/Human.

Reuse Evidence whose premises remain valid; do not repeat discovery ceremonially.

## 4. Execution / Graph

Order Tasks by current real dependency. Each Task states at least: observable result, cheapest sufficient local Verification, and a decisive local PASS/FAIL condition.

For code changes, local Verification should reach the nearest valid repo-verification boundary that directly covers the affected behavior. Use red→green TDD when it is the clearest low-cost way to specify behavior or lock a regression, not as a universal ritual. If the normal local boundary is unavailable, state why and use the closest truthful direct probe.

A **Task Group** is a coherent set of ordinary Tasks whose combined behavior, shared contract, migration slice, or join needs broader Verification. It is only a Verification boundary, not a new taskbook section, persistent object, workflow, or Agent topology.

Place broader Verification at the smallest Task-Group boundary that proves the combined behavior: after a coherent set of Tasks, before dependent work consumes it, or at a branch join. Do not repeat expensive system-wide checks per Task. Reuse still-valid Evidence and rerun only Verification whose proven behavior may have been invalidated.

Keep simple work linear. When true branches, dependencies, shared writes, Task Groups, or joins would be hidden, read [execution-graph.md](execution-graph.md) and compile only the minimum real dependency structure. The Handoff Graph is a best-known starting snapshot; runtime Evidence may change the remaining frontier.

## 5. Execution Rules

- route new Unknown by what it can change: Goal/boundary/Human verification authority, execution fact, implementation How, Verification, or Evidence;
- Tasks/Graph are the current execution plan, not frozen scope. As Evidence changes dependencies or implementation reality, add/remove/split/merge/reorder only the remaining work inside stable Goal, boundaries, authority, and required Verification;
- if one branch is Blocked but independent work is ready, continue it; joins wait only for real dependencies;
- do not mechanically reopen completed work when Graph changes; reacquire Evidence only when its premises or required combined Verification changed;
- preserve Verification granularity: Task PASS and Task-Group PASS may unlock work but cannot substitute for Goal-level coverage actually required by the delivery;
- never downgrade triggered Verification. A provider/location may change only when the replacement remains equivalent or more authoritative under repo verification authority;
- preserve material decisions, evidence-changing deviations, replans, scope expansion, Verification-cadence changes, and blockers in normal repo/runtime implementation records when available; do not create Prompt-Atlas-specific state files;
- on resume, reuse only decisions and Evidence whose premises remain valid;
- do not skip tests, weaken assertions, narrow judged population, mock away the tested object, swallow failures, edit a judge, or accept a lower protected baseline unless Goal explicitly requires the change and equivalent trustworthy Evidence remains;
- critical checks that may silently no-op need reverse validation; visible judges that are gameable may require protected/private/independent Evidence under [verification-trust.md](verification-trust.md);
- every retry must change the hypothesis or approach; stop known-bad routes instead of repeating them;
- roll back unauthorized regression and report failure truthfully;
- follow repository branch, PR, and pre-submit rules.

## 6. Verification and Evidence

After relevant Tasks and Task Groups converge, confirm Goal-level repo verification coverage. Reuse still-valid lower-level Evidence and run only repo-required Verification that remains uncovered or whose premises were invalidated. Goal-level Verification is a final judgment boundary, not a ceremonial extra command.

Final Verification scope follows the **actual** change surface, effective binding/config, and real consumers/targets, not an early snapshot or the author's label for the change. Expected `0-diff`, cleanup, or refactor cannot shrink already-triggered Verification.

Evidence supports judgment only while its provider really ran, the provider covers the claimed behavior, target/revision/environment/binding/config premises remain valid, and judges/baselines were not weakened.

When the judging side can access the authoritative environment, reacquire final-judgment-critical repo-authoritative Evidence at reasonable cost rather than trusting only Executor summaries. Do not mechanically rerun every still-valid local check. When the environment is unavailable, require portable provenance: actual command/probe, target/revision, material binding/config, exit/verdict, and raw output or a stable artifact/reference. Unreviewable summaries are an evidence gap.

Ordinary protected visible repo Verification is the default. Read [verification-trust.md](verification-trust.md) only when false-green, gameability, silent failure, or independence risk requires stronger trust. Missing or stale required Evidence is non-PASS; obtain new Evidence, adjust remaining Execution/Graph, report a truthful blocker, or return to the relevant Human authority boundary.

The final report states the delivered result, Evidence supporting the judgment at Task / Task Group / Goal levels where applicable, exact residuals or blockers, and the next legitimate route. Do not replace Evidence with activity narration.

Before Handoff, verify that there is one Goal and one declared delivery; Goal is stable; explicit Human verification requirements are preserved; relevant repo verification authority has been read; known required Verification is compiled and execution-only triggers are in Task 0; at least one Task or required Task 0 can start; dependencies are grounded; simple work remains linear; Graph is used only where real relationships require it; every development Task has sufficient local Verification; every meaningful Task Group has broader Verification only when needed; Goal-level coverage remains possible; authority-sensitive operations are bounded; and no Completion/Acceptance layer, scheduler, manager, Graph engine, or fixed Agent topology has been introduced.
