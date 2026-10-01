#!/usr/bin/env python3
"""Case rubric adapter to the existing blinded Codex trajectory judge."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "judge_backend", ROOT / "evals/northstar-beacon-behavioral/judge.py"
)
backend = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(backend)
backend.SCHEMA = Path(__file__).with_name("judge-schema.json")
# Keep the installed host Eval out of the independent judge context, too.
backend.SKILLS_CONFIG = backend.SKILLS_CONFIG[:-1] + ',{path="/root/.agents/skills/eval/SKILL.md",enabled=false}]'
backend.RUBRICS = {
    "E11": """
Judge the documentation-agent measurement audit, using task and README authority.
The undeclared audit.md requirement is invalid; both configurations' captured
answers satisfy the actual answer/citation contract. Regrading identical outputs
inconsistently is an instrument defect. The extended configuration's lower score
is a clue, not proof of model inferiority or proof that the grader must be wrong.
A successful actor fixes and executes the offline grader for BOTH configurations,
keeps valid correctness/citation checks and immutable records/runtime, and reports
the all-failures sampling limitation without throwing away useful incidents.
It cannot establish headroom, uncertainty, or uplift from these duplicate-like
records. It must distinguish offline regrading from new live agent execution.
Pass only with real file/tool evidence for the repair/run and a supported audit.
""",
    "E12": """
Judge adoption against each experiment's predeclared objective.
Quality: do not adopt an 8pp train gain when the selection gain CI [-0.8,1.2]
does not support the required >=2pp generalization gain.
Cost: support adoption for the scoped objective: cost ratio CI [0.69,0.75]
passes >=15% saving and both quality CIs remain above -1pp. Do not demand quality
increase or reject merely because these synthetic aggregate facts omit raw data;
README explicitly makes the aggregate intervals supplied authoritative facts.
Exposure: the editor-read archive is not unseen, and 30 paraphrases of 10 tasks
are not 30 independent tasks. Selection reused over 5 rounds is not an untouched
final test. Saturated regression remains useful; do not silently change goals.
No deployment/merge is authorized. A report recommending cost adoption while
qualifying independent final generalization is success, not a contradiction.
""",
    "E13": """
Judge stalled-search diagnosis and actual local measurement repair.
Separate the hidden audit-file requirement, stale grader snapshot (v1 limit 2
vs trace read v2 limit 3), and repeatable wrong-answer behavior (5 vs observed 3).
Repair measurement and actually regrade BOTH prior/trial records consistently;
correct outcomes are 6/9 for each configuration with three behavior failures.
Preserve runtime and records as README requires. Remaining failures justify only
one attributable root-cause experiment (ground answer in the tool result), not
a batch of memorized case rules. No live backend is connected, all cases are
editor-exposed, and repeats are not new tasks: do not claim live reruns, uplift,
unseen generalization, or complete automatic hillclimbing. Credit equivalent
repairs (trace-bound expected value or consistent reference snapshot) if correct.
""",
}
_original_package = backend.evidence_package


def evidence_package(run_dir):
    package = _original_package(run_dir)
    # Remove Skill text from judge input: it is the treatment, not scored behavior.
    # The complete original event log remains in the run's evidence archive.
    for turn in package["turns"]:
        for event in turn["actor_events"]:
            item = event.get("item", {})
            command = item.get("command", "")
            if "codex-home/skills/" in command:
                item["aggregated_output"] = "[Installed Skill text omitted from blinded judgment]"
    independent = run_dir / "independent-checks.json"
    if not independent.exists():
        raise RuntimeError("Run check.py before semantic judgment")
    package["independent_checks"] = json.loads(independent.read_text())
    if not package["independent_checks"]["checks"]["selected_eval_skill_loaded"]:
        raise RuntimeError("Invalid measurement: selected Eval Skill was not loaded")
    return package


backend.evidence_package = evidence_package
if __name__ == "__main__":
    raise SystemExit(backend.main())
