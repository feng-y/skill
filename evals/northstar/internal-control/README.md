# Internal Northstar control without handoff

F18 supplies the incident shape and Human correction. This focused eval measures
Northstar's internal action choice, not a mandatory controller/worker protocol.
Both cells explicitly forbid external agents while allowing local product writes.

- P starts with a target-behavior description, then asks about the existing debug
  path and feature lifetime in the same session. It should produce and revise a
  real plan without implementing the product.
- I explicitly authorizes implementation in the current session, then reviews
  final-response coverage and observer responsibilities in that same context.
  It should execute autonomously and retain the same plan/Intent responsibility.

`run.py` binds these cases to the process/snapshot helpers in the existing
`controller_worker.py` backend. Each actor has a disposable HOME/CODEX_HOME and
workspace, copies only existing auth, and loads its pinned base or working-tree
Northstar under `.agents/skills`. The follow-up resumes the same native session.
Auth is removed with the temporary home and is never included in Evidence.
This measures the loaded skill, not installation into the user's existing home.
The Python fixture reproduces feature → score → response, not C++ shared_ptr.

From the repository root, with an authenticated Codex CLI:

```sh
python3 evals/northstar/internal-control/run.py \
  --out /tmp/northstar-internal-control-evidence --repeats 2
```

The runner uses `gpt-6.1-sol`, medium effort, explicit action-boundary snapshots
and full JSONL. `--base`, `--model`, `--timeout` and `--workers` are configurable.
Workspace-write sandboxing is unavailable on the measured host (`bwrap:
pivot_root: Operation not permitted`), so actors run without a filesystem sandbox
in disposable directories. This is an isolation convention, not a host-security
boundary. Inspect traces for access outside the workspace. Disabling multi_agent
alone did not remove delegation tools here; actual tool calls must satisfy the
Human no-delegation constraint.

`identity.json` locks the rubric and prompts before launch. Each actor record
retains exact command/prompt, model/session identity, skill hash/immutability,
full trace, final messages, pre/post files and tool-boundary snapshots. Inspect
all tool events and the real plan; final text or final product hashes alone cannot
establish ownership or absence of transient edits. A within-command edit/revert
may evade boundary snapshots and requires inspecting command text. Run original
fixture tests and the external oracle in the rubric on restored final products.
Any incomplete trace, failed access or stale return is inconclusive unless an
actual violation was already observed.

Two repeats are a bounded smoke, not statistical uplift. Developmental runs with
different prompts, permissions or rubrics must stay separate. Results and these
limitations belong in RESULTS; normal Northstar runtime must not load eval cases.

The runtime change retains Northstar's existing semantic ownership and execution
versus proof boundaries. It compresses the old convergence/readiness/authorization
paragraphs into internal action selection, aligns the entry prompt and removes
mandatory-sounding execution handoff wording. No new role, state, protocol,
authority or lifecycle is introduced, and no breaking semantic migration occurs.
