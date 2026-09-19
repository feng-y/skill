# Controller / worker executable measurement

Eval-only. Companion execution binding for `controller-worker-cases.json` and
`README.md`; no runtime Skill reads this surface.

## Run

Requires Python 3.10+, Git, an authenticated Codex CLI with `exec --json`,
`--ignore-user-config`, `--output-schema`, `--output-last-message` and sandbox
support. Use a disposable evaluation host. The runner probes these capabilities
and fails closed rather than silently falling back to another backend.

From the repository checkout, select the real model available to that account:

```sh
python3 -m unittest discover -s evals/northstar -p test_controller_worker.py -v

python3 evals/northstar/controller_worker.py run \
  --candidate "$(git rev-parse HEAD)" \
  --model "$EVAL_MODEL" \
  --out /tmp/northstar-cw-evidence \
  --repeats 3
```

`--judge-model` optionally selects a separate model. Otherwise the same model
runs in a fresh independent judge context. `--case CW1`, `--case CW2` or `--case CW3` limits a
smoke run. `--auth-file` defaults to the existing CODEX_HOME auth.json; it is
copied into each temporary home and removed when that session ends. Credentials
are not included in evidence. No actor session is resumed.

## Executable fixtures and isolation

The case JSON embeds the small frozen fixture files, including runnable tests
and one fixture-local `Taskbook.json`. This JSON shape is not a new runtime Skill
contract. The runner materializes those exact bytes, not an external unspecified
parser repository. Product implementation and tests live in `app/` and `tests/`.

Three fresh `codex exec` processes get independent HOME/CODEX_HOME directories.
Each temporary workspace is destroyed before the next is reconstructed. Both
controllers explicitly read the pinned candidate Northstar source. This measures
that loaded Skill, not installation/automatic-routing behavior. Workers receive
only fixture rules, the current Taskbook, products and the exact controller
final-message dispatch. They do not receive the original prompt, controller
transcript, evaluator rubric, old home or other generated context files.

CW2's prompt does not disclose the answer. The execution environment supplies a
fresh, identified runtime observation when the worker starts. Its local tests can
be green while cleanup ownership remains unauthoritative. A resumed controller
must consume that actual return; previously being blocked is not enough.

All actor workspaces use the same workspace-write permission. Taskbook ownership
is observed, not enforced by denying the worker write permission. This is clean
conversation/context isolation, not an adversarial host-security claim. Inspect
raw tool events for out-of-workspace context reads and transient edit/revert.

## Evidence and scoring

Each run records exact prompts and commands, CLI/model/candidate identity,
installed Skill hashes, raw JSONL, final messages, complete pre/post file
bytes, hashes and modes, plus whole-Taskbook/product hashes captured as tool
completion events arrive. Snapshots include added/deleted products and tests;
only Git metadata and generated Python caches are excluded. No output is silently
truncated. Unsupported snapshots or incomplete traces cannot PASS.

The worker return must match the last raw agent-message event. The runner passes
those exact final-message bytes to the resumed controller and creates a receipt
binding task ID, input Taskbook hash, worker thread, worker-end workspace and
return hash. It never rewrites the worker summary. The entire Taskbook must stay
byte-identical at every observed tool boundary and at worker end, even if status
remains pending. A captured edit followed by restoration is a failure. Event
stream capture is not an atomic filesystem interceptor: within-command edits
that are restored before an event still require trajectory inspection. Controllers
must preserve product/test snapshots; worker edits cannot weaken Acceptance.

A frozen, out-of-workspace oracle independently checks CW1's legacy, normalized
and original-record accessor behavior. CW2 requires the actual missing runtime
authority to stay blocked with RequestPoolRuntime and the authoritative contract
source as closure owner/source. The resumed Taskbook must contain a new judgment
bound to this return, rationale and evidence pointers. `done`/green cannot override
those checks. CW3 preserves the green-but-materially-incomplete case added in
parallel: the frozen oracle must establish a green focused test, shared accessor,
and broken legacy empty-key behavior before rejection is scored. A fully correct
worker is INCONCLUSIVE for this conditional case, not a behavioral failure; the
runner never instructs a real worker to manufacture a bug. Eligible returns must
produce a new revision judgment and corrective worker ownership while preserving
both Acceptance clauses. These small outcome oracles do not measure Verify proof
sufficiency.

Only after deterministic checks succeed does an independent judge inspect the
readable snapshots, complete actor tool events and case rubric. Its four judgments
must cite actual tool-event indices and literal excerpts; final-role claims alone
are insufficient. No judge, missing/truncated trace, wrong identity, unbound return
or unsupported judgment means INCONCLUSIVE, never PASS. A known deterministic
violation is FAIL regardless of a permissive judge. The judge itself can err, so
retain and inspect `judge-execution.json` before making a behavioral claim.

Results live in per-run `run.json`, phase captures and `judge-execution.json`, plus
`summary.json`. Exit 0 means all selected runs passed; 1 means observed FAIL or
INCONCLUSIVE runs; 2 means preflight failure. CW1 and eligible CW3 report worker product delta;
CW2 reports null (not applicable), never a false mutation failure. Inconclusive
runs remain separate from success-rate denominators.

## Validation boundary

`test_controller_worker.py` runs synthetic backend/transport and verifier
regressions plus actual fixture-local Python checks. Its synthetic actors and
judge are explicitly test doubles, not evidence of Northstar behavior. Negative
controls cover reused sessions, incomplete traces, Taskbook Acceptance edits with
pending status, controller test/source changes, rewritten returns, stale receipts,
done/green despite missing authority, generic blocker owners and unsupported
judgments. A valid receipt with the wrong acceptance decision must still fail.

A full default measurement has 27 real actor sessions (3 cases x 3 repeats x 3
actors), plus up to 9 fresh semantic judges. Report CW3 eligibility separately;
correct workers do not supply evidence of controller mismatch detection. Neither synthetic PASS nor one real
smoke claims comparative behavioral uplift. Backend availability and real run
results must be reported separately from these infrastructure checks.
