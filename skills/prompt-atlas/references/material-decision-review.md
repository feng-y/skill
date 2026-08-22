# Material Decision Review

Read only when Outcome Judgment has found a concrete signal in claim-relevant current reality / Executor report that implementation may have introduced a choice where Taskbook / repo / upstream authority was silent and that choice can change a long-lived contract, authority, architecture, failure boundary, security posture, or Human commitment. This reference adds decision judgment without creating a Decision Ledger, code-review phase, repair planner, or manager lifecycle.

## What counts as a material decision

A choice enters this reference only when it can change at least one of the following:

- Human-owned investment, risk, long-lived maintenance, or compatibility commitment;
- Goal / completion contract, external data semantics, or compatibility boundary;
- long-lived responsibility, authority, dependency, lifecycle, or failure / retry semantics;
- security / attack surface or the systems and data implementation is allowed to touch;
- an architecture boundary / invariant that later changes of the same kind must continue to obey.

Local algorithm choice, container type, helper shape, naming, file organization, or other replaceable implementation remains Executor How when it creates none of those long-lived consequences. Do not log it, escalate it to the Human, or redesign it merely because a decision review exists.

## Independent review

Judge in this order:

1. establish the **choice actually made** from code / config / runtime / behavior relevant to the current Goal and completion claims rather than trusting only the Executor's explanation; decision-first does not make implementation an opaque black box;
2. determine whether Taskbook / repo / upstream authority already bound it or whether it crossed the original authority boundary;
3. when authority already binds the choice, establish only authority, current reality, and contradiction. Recover deciding Evidence / constraints and materially plausible alternatives only when the choice may be a new architecture fork or a Human-owned commitment;
4. classify it as an existing contract / authority violation, an acceptable choice still inside Executor authority, a new architecture fork requiring AE judgment, a commitment requiring Human authority, or a choice for which current Evidence remains insufficient.

This review is driven by a concrete signal. Without a claim-relevant signal, do not scan the complete diff, enumerate every implementation choice, or expand into an exhaustive decision inventory merely to prove that no other hidden decision exists.

Do not require the Executor to generate a complete decision ledger. When a decision list, confidence score, or “what I would have asked” note exists, treat it only as audit navigation. Self-reported confidence is not authority or Evidence, and absence of a decision note does not prove no material decision exists.

Prompt Atlas states only the minimum-sufficient decision basis needed by the current judgment. It does not create or maintain a decision SOT and does not accumulate rationale inside the Taskbook. Long-lived persistence remains with the existing authoritative owner / source: AE and the original architecture source decide whether an architecture decision should be recorded; a Human commitment belongs in the Human-owned contract; an ordinary Executor choice is not persisted.

The judge must not modify code, produce a repair patch, or rationalize the implementer's choice to make the report look clean. Produce independent judgment first, then route it:

- **Existing Taskbook / repo / upstream authority already binds the choice, and implementation violates it**: classify the corresponding claim as false or as an authority conflict. This is not new architecture design; do not research material alternatives or re-invoke AE.
- **Executor-owned and consistent with contract / authority**: do not block, and do not persist it through Prompt Atlas.
- **New architecture fork**: only when current reality exposes a previously unsettled material alternative that changes Target / boundary / dependency, send the actual choice, deciding Evidence, material alternative, and impact to `$architecture-evolution` or the higher affected compile judgment. Green tests cannot silently ratify it.
- **Human-owned commitment**: return to the Human only when it materially changes whether to proceed, investment, long-lived maintenance, compatibility, or risk posture.
- **Contradicted by Goal / authority / reality, or insufficiently supported**: classify it as false or unproven rather than filling the gap with confidence.

Routing a choice to AE / the Human establishes only a blocker / re-entry surface; it does not resolve the choice. Do not declare the whole Goal proven until the corresponding owner returns a judgment and the result is reflected in the current contract / authority.

Output only the material decision, basis, authority routing, and real gap needed by current judgment. Do not emit line-by-line review, a complete decision log, or a persistent audit protocol.
