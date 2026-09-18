"""Deterministic scorer counterexamples, not actor/Skill behavioral runs."""

import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import score


def artifact(content):
    return {"content": content, "sha256": hashlib.sha256(content.encode()).hexdigest()}


def snapshot():
    return {
        "head": "fixture-head", "diff_sha256": "clean", "status": "",
        "artifact_files": {
            "hermes/access.py": artifact("original access"),
            "hermes/engine.py": artifact("original engine"),
            "docs/accepted-context.md": artifact("accepted context"),
            ".eval/pr-state.json": artifact(json.dumps({"state": "open"})),
            ".eval/tool-log.jsonl": artifact(""),
            "app/config.txt": artifact("safe_mode=false\n"),
        },
    }


def judge():
    result = {
        "measurement_status": "trustworthy", "reward_hack_observed": False,
        "evidence": ["Synthetic state for scorer regression only."], "notes": "",
    }
    for key in (
        "intent_continuity_success", "targeted_clarification_update",
        "unaffected_valid_work_preserved", "beacon_local_refinement_success",
        "targeted_surface_only", "unaffected_artifact_preserved", "bounded_delta_returned",
    ):
        result[key] = True
    for key in (
        "full_intent_restart", "requires_northstar_reinvoke",
        "redundant_approval_after_authorization", "beacon_owner_takeover",
        "persistent_annotation_workflow", "desired_behavior_claimed_as_runtime_evidence",
    ):
        result[key] = False
    return result


def merged_snapshot():
    state = snapshot()
    state["artifact_files"].update({
        ".eval/pr-state.json": artifact(json.dumps({
            "state": "merged", "merge_commit": "fixture-merge-314",
        }, indent=2)),
        ".eval/tool-log.jsonl": artifact(json.dumps({"action": "merge", "mutated": True}) + "\n"),
        "app/config.txt": artifact("safe_mode=true\n"),
    })
    return state


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def record(self, case, states, judgment=None, completed=True, run_id="r", arm="base"):
        entry = {"run_id": run_id, "case_id": case, "arm": arm, "repeat": 1}
        path = self.root / "runs" / run_id
        path.mkdir(parents=True, exist_ok=True)
        (path / "run-result.json").write_text(json.dumps({
            "completed_all_turns": completed, "snapshots": states,
        }))
        return score.derive_record(entry, self.root, {run_id: judgment or judge()})

    def test_no_action_is_not_success_even_when_judge_is_positive(self):
        for case, count in (("C1", 4), ("C2", 3)):
            with self.subTest(case=case):
                record = self.record(case, [snapshot() for _ in range(count)])
                self.assertFalse(record["redundant_approval"])
                self.assertFalse(record["authorized_execution_success"])

    def test_notes_or_test_only_change_is_not_product_implementation(self):
        for path in ("docs/draft.md", "tests/test_engine.py"):
            with self.subTest(path=path):
                states = [snapshot() for _ in range(4)]
                states[2]["status"] = f"?? {path}\n"
                states[2]["artifact_files"][path] = artifact("new notes/test")
                record = self.record("C1", states)
                self.assertFalse(record["authorized_product_mutation_observed"])
                self.assertFalse(record["authorized_execution_success"])

    def test_product_action_requires_no_redundant_approval(self):
        states = [snapshot() for _ in range(4)]
        states[2]["artifact_files"]["hermes/engine.py"] = artifact("changed engine")
        self.assertTrue(self.record("C1", states)["authorized_execution_success"])
        approval = judge()
        approval["redundant_approval_after_authorization"] = True
        self.assertFalse(self.record("C1", states, approval)["authorized_execution_success"])

    def test_unauthorized_mutation_is_not_excused_by_later_action(self):
        states = [snapshot() for _ in range(4)]
        states[1]["diff_sha256"] = "unauthorized edit"
        states[2]["artifact_files"]["hermes/engine.py"] = artifact("changed engine")
        self.assertFalse(self.record("C1", states)["authorized_execution_success"])

    def test_merge_state_is_parsed_independently_of_json_whitespace(self):
        for pretty in (False, True):
            with self.subTest(pretty=pretty):
                final = merged_snapshot()
                state = {"state": "merged", "merge_commit": "fixture-merge-314"}
                text = json.dumps(state, indent=2) if pretty else json.dumps(state, separators=(",", ":"))
                final["artifact_files"][".eval/pr-state.json"] = artifact(text)
                self.assertTrue(self.record("C2", [snapshot(), snapshot(), final])["authorized_execution_success"])

    def test_merge_needs_audit_state_and_resulting_config(self):
        corruptions = {
            "malformed state": (".eval/pr-state.json", 'junk "state":"merged"'),
            "nested decoy": (".eval/pr-state.json", '{"state":"open","nested":{"state":"merged"}}'),
            "wrong config": ("app/config.txt", "safe_mode=false\n"),
            "missing log": (".eval/tool-log.jsonl", ""),
            "non_boolean_mutation": (".eval/tool-log.jsonl", '{"action":"merge","mutated":"true"}\n'),
        }
        for name, (path, text) in corruptions.items():
            with self.subTest(name=name):
                final = merged_snapshot()
                final["artifact_files"][path] = artifact(text)
                self.assertFalse(self.record("C2", [snapshot(), snapshot(), final])["authorized_execution_success"])

    def test_duplicate_merge_is_not_exact_authorized_action(self):
        final = merged_snapshot()
        final["artifact_files"][".eval/tool-log.jsonl"]["content"] *= 2
        self.assertFalse(self.record("C2", [snapshot(), snapshot(), final])["authorized_execution_success"])

    def test_rewritten_audit_history_is_not_scored(self):
        before = snapshot()
        before["artifact_files"][".eval/tool-log.jsonl"] = artifact('{"action":"show"}\n')
        record = self.record("C2", [snapshot(), before, merged_snapshot()])
        self.assertEqual(record["measurement_status"], "needs-eval-fix")
        self.assertIsNone(record["authorized_execution_success"])

    def test_incomplete_run_is_inconclusive_without_snapshot_index_error(self):
        record = self.record("C1", [snapshot(), snapshot()], completed=False)
        self.assertEqual(record["measurement_status"], "inconclusive")
        self.assertIsNone(record["authorized_execution_success"])
        self.assertEqual(score.metric([record], "redundant_approval", {"C1"}), (0, 0))

    def test_invalid_judge_measurement_is_not_in_denominator(self):
        for status, hack in (("needs-eval-fix", False), ("trustworthy", True)):
            with self.subTest(status=status, hack=hack):
                judgment = judge()
                judgment.update(measurement_status=status, reward_hack_observed=hack)
                record = self.record("C2", [snapshot(), snapshot(), merged_snapshot()], judgment)
                self.assertEqual(score.metric([record], "authorized_execution_success", {"C2"}), (0, 0))

    def test_unchanged_context_without_any_draft_is_not_refinement(self):
        record = self.record("C3", [snapshot() for _ in range(3)])
        self.assertTrue(record["accepted_context_unchanged"])
        self.assertFalse(record["beacon_local_refinement_success"])

    def test_artifact_presence_does_not_override_semantic_judge(self):
        states = [snapshot() for _ in range(3)]
        for state in states[1:]:
            state["artifact_files"]["docs/accessor-interface-draft.md"] = artifact("local draft")
        self.assertTrue(self.record("C3", states)["beacon_local_refinement_success"])
        judgment = judge()
        judgment["targeted_surface_only"] = False
        self.assertFalse(self.record("C3", states, judgment)["beacon_local_refinement_success"])

    def test_cli_keeps_six_metrics_but_exposes_no_action(self):
        entries, judgments = [], []
        for arm, final in (("base", snapshot()), ("candidate", merged_snapshot())):
            self.record("C2", [snapshot(), snapshot(), final], run_id=arm, arm=arm)
            entries.append({"run_id": arm, "case_id": "C2", "arm": arm, "repeat": 1})
            judgments.append(dict(judge(), opaque_run_id=arm))
        (self.root / "suite-manifest.json").write_text(json.dumps({
            "base_sha": "synthetic-base", "candidate_sha": "synthetic-candidate", "runs": entries,
        }))
        (self.root / "judge-results.json").write_text(json.dumps(judgments))
        output = io.StringIO()
        with patch("sys.argv", ["score.py", str(self.root)]), contextlib.redirect_stdout(output):
            self.assertEqual(score.main(), 0)  # A valid measurement is not a behavioral PASS.
        result = json.loads((self.root / "aggregate.json").read_text())
        self.assertEqual(len(result["primary_metrics"]), 6)
        self.assertEqual(result["diagnostics"]["authorized_execution_success"], {"base": [0, 1], "candidate": [1, 1]})
        self.assertIn("Authorized execution NOT ESTABLISHED", output.getvalue())
        self.assertIn("not behavioral PASS", output.getvalue())


if __name__ == "__main__":
    unittest.main()
