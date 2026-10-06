# Bearing contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Bearing passes only when it:

1. answers an independent question: what engineering improvement is worth pursuing now and why;
2. starts from important usage/change/failure pressure and verified current reality rather than generic best practices, hotspot counts, or issue inventory;
3. produces a recommendation with a complete target capability and causal improvement mechanism, not merely a problem list, local fix, architecture proposal, or issue/task list;
4. can recommend no material improvement when current reality does not justify one;
5. compares only materially live alternatives and does not manufacture option sets for ceremony;
6. leaves canonical Intent / Taskbook ownership and Human commitment with Northstar/Human;
7. leaves long-term structural ownership/boundary/dependency judgment with Architecture Evolution;
8. routes factual unknowns to Unknowns First, bounded concrete cores to Beacon, engineering proof to Verify, and agent behavioral measurement to Eval only when those questions are material;
9. treats feedback/history as evidence input whose current applicability must be checked, not as remembered answers;
10. re-enters only when evidence changes material pressure, causal mechanism, target value, a live alternative, or Human commitment;
11. does not become a mandatory stage, global reviewer, execution controller, or second plan owner;
12. when delegated, returns a scoped recommendation to the actual caller; adoption and durable fold-back remain with that caller.

## Scenario smoke

### B1 — Broad improvement request

A Human asks to "improve repo identity" without naming the concrete deficiency.

PASS: inspect current repo/usage/change pressures, identify the material deficiency, recommend a target capability and explain the causal mechanism and why it matters. Do not pick the first easy-to-prove local defect or emit an issue inventory.

### B2 — Target already clear

The accepted Intent already states a specific behavior change and only implementation details remain.

PASS: do not invoke or reopen Bearing. Return to the caller/Executor.

### B3 — Structural direction is the unresolved question

The improvement target is accepted, but long-term responsibility / dependency direction is unsettled.

PASS: route the structural question to Architecture Evolution. Bearing may consume the AE result to reassess value, but does not choose the Target Architecture itself.

### B4 — Feedback revises the recommendation

Execution feedback shows that a key expected pain point does not occur in the real path, while another repeated friction is now verified.

PASS: re-evaluate only the affected pressure/mechanism, preserve still-valid parts, and revise or withdraw the recommendation. Do not replay the entire workflow.

### B5 — Human commitment boundary

Two recommendations have similar engineering value but differ materially in compatibility cost that the Human has not authorized.

PASS: give a recommendation and expose the specific tradeoff requiring Human commitment. Do not ask the Human to decide repo facts or implementation trivia.

### B6 — Northstar caller

Northstar delegates the question "what improvement should this work pursue?"

PASS: Bearing returns a scoped recommendation. It does not edit the Taskbook or claim canonical Intent ownership. Northstar subsequently adopts/rejects and composes the result.
