# Caller-owned composition — review and validation

Development/eval-only. Continuation base: `6b03114e938b69a7cfa46c762118d8d2252b56af`; original PR base: `acc09e5040b808b46cc8f9aea17bbac988d639ab`.

## Current verdict

The user-directed ownership correction is implemented: Northstar or another authorized caller performs selection, assembly and overall alignment. Prototype is one construction tool for a commissioned problem, small or complex. It does not accept delegated composition or orchestrate further Prototype calls.

No remaining blocking contract contradiction was found in this bounded review. Keep PR #95 unmerged and draft while its outstanding behavioral acceptance is unproven. Actual clean-session actor / consumer / blinded judge executions in this continuation: **0 / 0 / 0**. Text/metadata checks and design walkthroughs are not model behavior measurements.

## Plan review before runtime edits

Two implementer self-review rounds are recorded in `draft-handoff-plan.md`: ownership placement, then counterexamples. They rejected keeping delegated assembly inside Prototype while moving only final approval outside it. They retained complex internal construction, original-caller return, explicit experiments, and Human scope clarification without recurring approval for already-authorized work.

## Implementation review 1 — cross-surface consistency

Inspected both Skill bodies, frontmatter, invocation defaults, README, prototype contract eval and the Human/composition supplement. Removed the old positive permissions to "compose existing parts" and the Northstar route that sent assembly to Prototype. Replaced the repeated Prototype composition workflow with a smaller commissioned-construction contract.

Corrected a bypass sentence so it requires BOTH no shape gap and no pending explicit experiment. The tool must not drop a runnable assignment just because the shape is known. Made the assembly exclusion explicit rather than merely forbidding autonomous selection.

## Implementation review 2 — counterexamples and eval quality

- Existing compatible artifacts: caller actually assembles them, not just reviews a Prototype-produced assembly.
- Missing concrete behavior at a connection: caller commissions that behavior; Prototype returns it and caller resumes integration. No renamed whole-composition assignment.
- Complex single artifact: necessary internal components remain legitimate construction; no one-field limit or internal orchestration framework.
- Unclear scope: Northstar asks Human with concrete tradeoffs; already-confirmed scope does not receive another interview.
- Independent AE/Verify caller: no synthetic Northstar stage, no transfer of structural/proof authority.
- Conflicting facts or absent execution: retain the real gap; do not invent evidence, force a positive experiment or claim the overall Intent complete.

The first supplemental C1 prompt gave away the intended tool route; removed that cue before publication. The first C2 prompt claimed an interface was supplied without specifying it; replaced it with a self-contained static request and explicit interface. Existing H1/H0 prompts and response policies are preserved; their private grading now checks who performs assembly, not only who approves it.

These are implementer contract walkthroughs, not independent reviewers or executed agent sessions. The C1/C2 checks are specified for future real base/candidate sessions, not scored here.

## Executed checks

- All 12 files in the source partial snapshot matched immutable GitHub blob identities before edits.
- Modified Skill YAML frontmatter and invocation metadata parsed; names and default invocation identifiers are valid.
- UTF-8, final newlines and trailing whitespace checks passed.
- `git diff --check` and `git apply --reverse --check --whitespace=error-all` passed against the local candidate.

The workspace is a verified partial snapshot recovered from the prior published bundle, not a clone or the user's development machine. Remote tree identity is checked before the branch is updated; the incremental patch and check records are retained in the accompanying bundle.

Only documentation/metadata and eval guidance changed. Frozen D1–D11, Python scorers, example records and test code are untouched. The unchanged 26-test scorer suite was not rerun; no historical pass count or synthetic benchmark is presented as this continuation's result. No Hermes implementation, machine installation, Skill Doctor or control-plane code was changed.
