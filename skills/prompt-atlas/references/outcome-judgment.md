# Outcome Judgment

Read only when the input is already Executor outcome / completion report / Evidence and a current authoritative Taskbook exists. This reference owns **independent judgment**: determine whether the finished world promised by the Taskbook has actually become current reality while serving as the Evidence feedback boundary for Graph evolution inside Execution. Judge the current outcome and verify candidate Evidence first. When implementation may have introduced a material decision where the contract was silent, read [material-decision-review.md](material-decision-review.md) on demand; then decide whether the affected Graph or higher judgment must evolve. This is not execution replay, repair planning, or a manager loop.

## Judge context: contract first, reality second, report last

The order itself is an independence boundary:

1. Read the current authoritative Taskbook first, plus any later still-valid Human corrections / repo / upstream authority. Recover Goal, binding constraints, completion claims, and the material boundaries that genuinely need proof.
2. Then inspect current repo/runtime reality for those claims, reading only territory needed to judge outcome. Do not shrink judging scope to the diff merely because the Executor edited particular files.
3. Consume the Executor report / task checklist / test output / decision note last. They are candidate Evidence, navigation, or claims to verify; they must not define what “done” means or why a choice is justified before the judge sees the contract and reality, and they cannot change the Graph before verification.

If Executor narrative conflicts with the authoritative Taskbook or verified reality, prefer Taskbook / current authority / verified reality. Independence does not require repeating complete Research; obtain only Evidence the current outcome judgment truly needs.

## Reconstruct the actual finished world

Judge **what is true now**, not what steps were performed.

For each material Goal / binding / completion claim:

- find current reality / authoritative Evidence that directly observes it;
- when the claim depends on a real consumer, runtime binding, ownership, compatibility, or failure behavior, inspect that real path rather than only checks near the patch;
- current workspace is reality; landed commits, modified files, or green tests do not substitute for outcome;
- one material work cut passing does not make a cross-cut Goal-level outcome true automatically.

Do not add architecture, style, test form, or implementation preferences that the Taskbook did not require as new success criteria during judgment.

## Contract-silent material-choice trigger

When claim-relevant current reality or the Executor report exposes a concrete signal that implementation made a choice not specified by Taskbook / repo / upstream authority, and that choice can change Human commitment, Goal / compatibility, long-lived responsibility / authority / dependency / lifecycle / failure / retry, security / attack surface, or an architecture invariant, read [material-decision-review.md](material-decision-review.md) for independent judgment.

Ordinary algorithms, containers, helpers, naming, file organization, and other replaceable How do not trigger it. A decision note / confidence score is only navigation, while absence of a ledger does not prove no choice exists. Read code / config / runtime whenever needed as current-reality Evidence. Without a concrete signal, do not expand into the complete diff / implementation inventory or enumerate every implementation choice merely to prove that no other hidden decision exists.

## Evidence and counter-Evidence

Evidence must be sufficiently direct, authoritative, fresh, attributable, and able to propagate failure for the current claim. Executor self-reported `PASS`, command presence, matching test names, artifact presence, or a “high-confidence decision” alone is not proof.

For high-value claims, ask for the smallest disconfirming check: **is there a cheap material current-reality observation that could directly falsify the Executor's completion narrative or material-decision rationale?** If yes, check it. Without a concrete risk, do not expand into exhaustive adversarial Research merely to look stricter.

When there is a concrete risk that implementation is wrong while visible checks can still PASS, read [verification-trust.md](verification-trust.md) and add only the smallest check that can falsify that risk.

Distinguish missing Evidence from Evidence that proves a claim false:

- current reality / Evidence contradicts the claim → the claim is not true;
- current Evidence is insufficient to decide → the claim is not yet proven;
- do not invent an implementation defect from “not proven,” and do not treat “no counterexample found” as proof.

## Whole-Goal judgment

Finally re-judge the entire Goal rather than summing local green signals. Acceptance requires all of the following:

- every material Goal / binding / completion claim has sufficient Evidence;
- current reality contains no material contradiction to those claims;
- known residue, partial paths, legacy authority, or runtime branches do not leave the Goal false in its real scope;
- Evidence covers the outcome required by the Taskbook rather than only patch proximity;
- every contract-silent material choice exposed by current Evidence has received independent judgment: choices inside Executor authority are confirmed consistent with contract / authority, and choices requiring higher authority have been resolved by the corresponding owner and reflected in the current contract / authority.

The last condition does not require proving that implementation contains no other hidden choice. Without a concrete signal, do not expand Research. A legitimate ordinary implementation choice also does not block completion merely because no decision note was written. **Routing is not resolution**: sending a choice to AE / the Human while that judgment is still pending leaves a blocker and cannot count as Goal-acceptance Evidence. An integration / ownership / compatibility outcome may span several implementation cuts; every local check can be green while the whole outcome is still false.

When expressing **completion degree**, report material-claim coverage: which claims are proven, disproven, or still unproven, and which gap prevents the whole Goal from being true. Do not turn task count, diff size, test count, or `7/8 tasks` into a completion percentage; activity volume is not Goal coverage.

## After judgment

Judgment produces the current decision first and only then decides whether the Graph inside the same Goal's Execution or a higher-level decision must change. Do not skip judgment and compile the Executor report / decision note directly into a repair plan:

- **Goal is proven**: accept the current outcome and state the material Evidence basis. When the acceptance judgment must explain a verified material choice, state only the minimum-sufficient basis in the current judgment. Prompt Atlas does not create or maintain a decision SOT and does not accumulate rationale inside the Taskbook.
- **Taskbook remains valid and only an existing claim is false / unproven**: identify the exact claim, current counter-Evidence / missing Evidence, and why it is material. If verified Evidence does not change remaining material work / dependencies, do not rewrite the gap into a file/helper/test tasklist.
- **Taskbook remains valid, but established Evidence / new reality makes previously contingent material work real or changes remaining work / dependencies**: re-enter only the affected Execution dependency cone; use the Graph to extend, remove, split, merge, or reorder only work the new reality affects, then fully re-deliver the Taskbook from latest reality. Unrelated Graph, Goal, and still-valid Evidence remain reusable.
- **A verified contract-silent material choice**: when existing Taskbook / repo / upstream authority already binds the choice and implementation violates it, classify the corresponding claim as false or as an authority conflict without researching material alternatives or re-invoking AE; when the choice remains inside Executor authority and satisfies the contract, do not block; only when current reality exposes a previously unsettled architecture fork that changes Target / boundary / dependency should it route to `$architecture-evolution` or the higher affected compile judgment; return to the Human only when the choice changes investment, long-lived maintenance, compatibility, or risk commitment. Routing to AE / the Human establishes only a blocker / re-entry surface. Do not declare the whole Goal proven until that owner returns a judgment and the current contract / authority is updated.
- **New reality invalidates a Taskbook premise / authority / completion contract**: re-enter from the higher affected Intent take / Intent compile judgment. Do not use an invalid contract as a repair specification.
- **Authoritative reality required for judgment is unavailable**: state the blocker and resume condition accurately; do not accept Executor self-report as a substitute.

Ordinary implementation failure does not return to the Human. Return only for a new Human-owned choice / authorization, or when reality makes safe continuation itself require Human authority.

Keep output minimum-sufficient: when only judgment is needed, return the decision, material claim basis, any material choice the current judgment must explain, and the real gap. Long-lived persistence remains with the existing authoritative owner / source rather than Prompt Atlas. When established Evidence has changed the Graph inside Execution, return the fully recompiled Taskbook for the affected cone. Do not emit line-by-line code review, a complete decision log, execution progress, debug narrative, or persistent supervision protocol.
