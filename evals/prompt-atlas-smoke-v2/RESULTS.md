# Prompt Atlas current-head smoke eval v2

## Claim boundary

This is a current-head **compiler smoke** focused on the corrected Task 0
semantics and regression coverage around intent, Human boundaries, routing,
proportional execution structure, and completion trust.

- The cases were supplied as self-contained inputs against the current Prompt
  Atlas snapshot.
- The runner was GPT-5.6 Thinking in one conversation. Inputs were isolated by
  instruction, but model/context isolation was not independently enforceable.
- Exact outputs are frozen in `ARTIFACTS.md`.
- No current-head executor implementation or hidden oracle was run.
- Historical `prompt-atlas-leader-v3` oracle evidence remains supporting trust
  evidence for two older frozen fixtures; it is not counted as current-head
  execution evidence.

This eval can reject merge readiness for covered compiler behavior. It cannot
establish statistical production completion rate or broad Leader parity.

## Evaluated snapshot

- `skills/prompt-atlas/SKILL.md` blob:
  `af1ba1fea24cd03d493ed404b2d1d7e9c8e89c3a`
- `references/contract-anatomy.md` blob:
  `1190fcbeb030b7c11db5b92314d777327359ed08`
- `references/execution-compile.md` blob:
  `3fc32d0af8ed7d92d88e3cdfede92e4ee8554b8e`
- `references/completion-trust.md` blob:
  `b2af67ae34bdbbc011a1bed742be4ba0fc545fa5`
- `agents/openai.yaml` blob:
  `866043970ae36059047f872de2df890c970f5dbd`

## Regression that caused the repair

The prior Task 0 wording defined it only as a factual preflight for
carrier-shaping facts unavailable during compile. That preserved command and
baseline truth, but underrepresented two transferable Leader behaviors:

1. expose carrier-versus-reality disagreement before sunk cost;
2. require a short opening alignment so executor misunderstanding is visible
   before material modification.

That definition could still let a misread Goal or route survive until ordinary
execution. The merge recommendation was therefore withdrawn until the Task 0
semantics and smoke coverage were corrected.

## Corrected Task 0 contract

Task 0 is now conditional and may settle:

- critical facts and assumptions available only in the execution environment;
- disagreement between the carrier and execution reality;
- executor understanding of the Goal, initial route/order, and main risk.

It may expose a true Ask Human boundary earlier than ordinary execution would,
but it may not postpone one already visible during compile.

Outcome routing:

- aligned → begin material work;
- clear-carrier misunderstanding → correct understanding, no Human input;
- factual/planning mismatch inside intent/boundaries → revise and continue;
- change intent / change confirmed boundary / confused intent → return to Intent
  Take before affected modification;
- branch-only blocker → park and continue independent work;
- no safe route → `Status: Blocked`.

Task 0 is not mandatory for clear, local, reversible work.

## Rubric

Each case receives applicable points for:

1. **Intent fidelity** — preserves every explicit requested result, accepted
   behavior, and confirmed boundary.
2. **Human-boundary precision** — asks only for change-intent,
   change-confirmed-boundary, or confused-intent decisions.
3. **Terminal routing** — chooses `Unresolved Intent`, `Blocked`, or
   `Executable` correctly.
4. **Task 0 precision** — uses Task 0 only for material pre-run settlement,
   includes disagreement/understanding when needed, and does not delay a visible
   Human decision.
5. **Executable usefulness** — gives a safe first action/evidence route with no
   more control structure than needed.
6. **Trust** — protects judging surfaces and prevents executor self-attestation
   from becoming global PASS when residual proof risk requires independence.

**Intent completion rate** is the percentage of cases passing items 1–3
together. It measures compiler intent preservation/routing on covered cases, not
final implementation success.

## Case results

| Case | Expected core behavior | Result |
| --- | --- | --- |
| S1 Confused Goal | Ask now; do not defer to Task 0 | PASS |
| S2 False-green discount | Direct carrier, no unnecessary Task 0/Graph, independent acceptance | PASS |
| S3 Parser migration | Preserve full behavior/removal, necessary scope stays executor-owned | PASS |
| S4 Necessary implementation expansion | No Human question and no Task 0 for an already-known fact | PASS |
| S5 Execution-only preconditions | Task 0 verifies reality and emits opening alignment | PASS |
| S6 Executor understanding disagreement | Correct clear-carrier misread; true conflict re-enters Intent Take | PASS |
| S7 Compile-visible boundary conflict | `Unresolved Intent`; never hide in Task 0 | PASS |
| S8 Global non-intent blocker | `Blocked`, not Human question | PASS |
| S9 Branch-local blocker | Park affected branch and continue safe work | PASS |
| S10 Simple direct task | No Task 0, Graph, durable state, or extra controller | PASS |

## Scores

| Metric | Result |
| --- | --- |
| Intent completion rate | **10/10 = 100%** |
| Human-boundary precision | **10/10** |
| Correct terminal routing | **10/10** |
| Task 0 precision cases | **4/4** — S5, S6, S7, S10 |
| Executable usefulness | **7/7** |
| Trust preservation on adversarial cases | **2/2** |
| Unnecessary Task 0 on clear work | **0 cases** |
| Unnecessary Graph / mandatory durable state | **0 cases** |

## SOT consistency review

### Main Skill → references

- `SKILL.md` defines Task 0 as pre-execution settlement of critical
  preconditions, carrier-versus-reality disagreement, and executor
  understanding.
- `contract-anatomy.md` preserves the Stage 1 boundary: compile-visible Human
  decisions are handled now; Task 0 is only for disagreement that requires the
  execution environment to expose.
- `execution-compile.md` is the detailed SOT for opening alignment and outcome
  routing.
- `completion-trust.md` remains independent of Task 0 and unchanged.

**Result:** PASS. The files elaborate one semantic rule rather than defining
competing Task 0 meanings.

### Public interface

README and `agents/openai.yaml` still expose the same two-stage responsibility,
three Human boundaries, and artifact-only default. No entry-interface change was
required for the Task 0 repair.

**Result:** PASS.

### Terminal states and runtime control

- Task 0 does not introduce a fourth terminal state or a new Human gate.
- `Unresolved Intent`, `Blocked`, and `Executable` remain exhaustive compile
  outcomes.
- Direct loop remains default; Task 0 is a conditional first action rather than
  a mandatory workflow stage.
- Opening alignment is a brief runtime-visible receipt, not a forced durable
  file or separate manager role.

**Result:** PASS.

## Leader alignment review

Corrected Task 0 now covers the transferable Leader behavior more accurately:

- validate numbers, commands, baselines, assumptions, and false-green checks;
- surface disagreement before modification;
- state understood Goal, order, and main risk before work begins;
- stop affected work when a true intent/boundary issue is exposed;
- continue independent safe work when only one branch is blocked.

Prompt Atlas still does not import Leader's mandatory `PROGRESS.md`,
`BLOCKED.md`, fixed retries, fixed role topology, or `/goal` transport.

**Result:** PASS.

## Loop / context / graph / prompt review

- **Loop:** Task 0 improves the first observe/evaluate boundary before the normal
  act loop; it does not become a second runtime framework.
- **Context:** the opening receipt externalizes only decision-relevant Goal,
  route/order, risk, and disagreement; it does not replay conversation history.
- **Graph:** Task 0 remains one conditional action. Graph appears only for real
  dependency, ownership, parallel readiness, evidence flow, or recovery.
- **Prompt:** the main skill states outcome and authority; detailed Task 0
  mechanics remain progressively disclosed in `execution-compile.md`.

**Result:** PASS.

## Matt-style skill architecture review

- **Public interface fidelity:** PASS.
- **Progressive disclosure:** PASS; the main skill carries the invariant while
  detailed routes live in one deep reference.
- **Module depth:** PASS; Task 0 exposes a small interface over fact validation,
  disagreement detection, alignment, and routing.
- **Locality/SOT:** PASS with deliberate kernel repetition only.
- **Task proportionality:** PASS; S10 proves clear work is not forced through
  Task 0.
- **Deletion test:** PASS; removing the detailed Task 0 section would lose
  material handoff-alignment behavior or force it back into the main skill.

## Limitations

- Same-conversation context may bias outputs.
- No independent second rater/model was used.
- No current-head executor implementation or hidden oracle was run.
- Ten cases do not establish broad completion-rate uplift.
- Historical paired evaluation is still stronger implementation/trust evidence,
  but covers an older Prompt Atlas snapshot and two fixtures.

## Verdict

**PASS for merge-level compiler smoke after the Task 0 correction.**

The corrected semantics close the identified Leader-alignment gap without adding
a mandatory stage, fourth Human gate, fixed state file, or unnecessary Graph.
No covered-case semantic blocker remains.
