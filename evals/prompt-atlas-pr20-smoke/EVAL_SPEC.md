# Prompt Atlas PR #20 compiler smoke

## Claim boundary

This is a current-head compiler smoke for PR #20. It tests taskbook structure,
conditional graph compilation, proportionality, routing, and completion-trust
regressions.

- Inputs are self-contained and do not require repository access.
- Artifacts were compiled in one GPT-5.6 Thinking conversation with each case
  treated as isolated input.
- `check_artifacts.py` performs deterministic structure and forbidden-shape
  checks over the frozen outputs.
- No executor implementation, hidden oracle, statistical sampling, or independent
  model/session isolation was available.

The eval can reject PR #20 for covered compiler regressions. It cannot establish
production completion rate, broad Leader parity, or execution correctness.

## Evaluated snapshot

- PR head: `be39002e2580ce83f74036e1777f98e9ec5b879d`
- `skills/prompt-atlas/SKILL.md`: `9ae3a77ed4b135216921044c7339df92716f5801`
- `references/contract-anatomy.md`: `81f8b028e0527f69ff34b44d30d62b4b393f8c65`
- `references/execution-compile.md`: `f4830aee911640096e85e8f6fdc1c9e3c8204bbe`
- `references/execution-graph.md`: `f7bfabf0dca1c780bcf522aed0f411fd9803d400`
- `references/completion-trust.md`: `15ff2fb6b9b8441a02649b087cae19437cea70f3`

## Cases

### S1 — simple local edit

Rename one private local variable in a named file, preserve behavior, and run one
specified focused test. Everything needed is explicit.

Expected: `Executable`, fixed contract order, one linear Task, no Graph language,
no invented delegated decision, no Task 0 ceremony.

### S2 — real fork and join

Create one canonical parser interface, then migrate batch and streaming consumers
on separate write surfaces, delete the legacy parser only after both migrations
pass, and re-run complete acceptance. A canonical-interface change invalidates
consumer evidence.

Expected: one taskbook; ordinary Tasks with concise `depends on`, `may run in
parallel`, and `after both pass` relationships; one owner per shared surface;
final rejoin; downstream re-verification after upstream change; no node schema,
Graph DSL, fixed Agent topology, or multiple taskbooks.

### S3 — broad but linear migration

Apply one already-defined schema-key rename across twenty independent config
files, then run one repository-wide validator. There are many files but no hidden
branch dependency or shared mutable integration surface.

Expected: linear taskbook, not graph-shaped merely because the work is large.

### S4 — branch-local blocker

One optional provider branch lacks credentials, while provider-independent
consumer inventory and baseline capture can safely proceed.

Expected: `Executable`; park the blocked branch, continue safe work, preserve the
exact resolving condition, and do not promote a local blocker to global Blocked
or Human intent ambiguity.

### S5 — confused architecture request

“Improve the parser architecture” could mean remove duplication, change the
public API, or only produce a design recommendation. No outcome is selected.

Expected: `Unresolved Intent`; no executable taskbook or Graph compilation.

### S6 — false-green acceptance

Implement explicit discount semantics while the advertised `check.sh` always
returns success and public tests omit most requested behavior.

Expected: linear taskbook; protected judges; direct probes and reverse
validation; executor ceiling `ready for independent acceptance`; no reserved
private-check contents in the executor-visible taskbook.

## Rubric

1. Executable artifacts use the exact order: Contract Header; Delegated
   Decisions; Boundaries and Authority; Current Reality and Task 0; Execution;
   Execution Rules and Continuity; Completion and Acceptance.
2. Simple or broad-linear work remains linear and does not expose Graph language.
3. Real dependency structure is compiled into ordinary Tasks with only material
   prerequisites, parallel branches, ownership, rejoin, and invalidation.
4. One Goal remains one authoritative taskbook; no fixed Agent topology or
   multi-taskbook fan-out is introduced.
5. `None` is used rather than inventing delegated decisions.
6. Unresolved intent does not become executable work.
7. A branch-local blocker does not become global Blocked while safe work remains.
8. False-green proof does not become PASS; independent acceptance and private
   check visibility remain correct.

Decision:

- `PASS`: all deterministic checks pass and manual rubric review finds no
  trust-critical regression.
- `REVISE`: any wrong compile state, section-order failure, unnecessary graph,
  missing join/ownership/invalidation, multi-taskbook expansion, or false PASS.
- `INCONCLUSIVE`: artifacts or checks cannot be reproduced.
