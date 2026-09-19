"""Scorer regressions only; these synthetic rows are not agent measurements."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("score.py")
FIELDS = (
    "intent_fidelity", "fact_grounding", "evidence_concretization",
    "architecture_reaction", "verification_fidelity", "targeted_reentry",
    "valid_work_preserved", "final_state_valid",
)
NEGATIVE = ("unnecessary_owner_call", "human_fact_question")


def row(variant="candidate", case="L1", repeat=1, good=True):
    return {
        "variant": variant, "case_id": case, "repeat": repeat,
        **dict.fromkeys(FIELDS, good), **dict.fromkeys(NEGATIVE, not good),
    }


class ScoreTests(unittest.TestCase):
    def run_score(self, rows, *args, raw=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.jsonl"
            path.write_text(raw if raw is not None else "\n".join(map(json.dumps, rows)), encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path), *args],
                                  capture_output=True, text=True, timeout=10)

    def assert_invalid(self, result, message):
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_opposite_directions_remain_distinguishable(self):
        bad = self.run_score([row("base"), row(good=False)], "--base", "base", "--candidate", "candidate")
        good = self.run_score([row("base", good=False), row()], "--base", "base", "--candidate", "candidate")
        self.assertEqual(bad.returncode, 0, bad.stderr)
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertIn("delta -100.0 pp", bad.stdout)
        self.assertIn("delta +100.0 pp", good.stdout)
        self.assertNotEqual(bad.stdout, good.stdout)
        self.assertIn("unnecessary_owner_call: 1/1 -> 0/1 clean; delta -100.0 pp", bad.stdout)

    def test_case_regression_is_not_pooled_away(self):
        result = self.run_score([row("base", "L1"), row("base", "L2", good=False),
                                 row(case="L1", good=False), row(case="L2")],
                                "--base", "base", "--candidate", "candidate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("case=L1", result.stdout)
        self.assertIn("case=L2", result.stdout)
        self.assertIn("delta -100.0 pp", result.stdout)
        self.assertIn("delta +100.0 pp", result.stdout)

    def test_duplicate_repeat_is_rejected(self):
        self.assert_invalid(self.run_score([row(), row()]), "duplicate")

    def test_single_arm_and_null_metrics_still_work(self):
        rows = [row(repeat=1), row(repeat=2, good=False)]
        for item in rows:
            item["architecture_reaction"] = None
        result = self.run_score(rows)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("variant=candidate case=L1 runs=2", result.stdout)
        self.assertIn("intent_fidelity: 1/2", result.stdout)
        self.assertIn("architecture_reaction: n/a", result.stdout)
        self.assertIn("No paired comparison", result.stdout)

    def test_missing_or_different_pairs_are_rejected(self):
        for candidate in (row(case="L2"), row(repeat=2)):
            with self.subTest(candidate=candidate):
                result = self.run_score([row("base"), candidate], "--base", "base", "--candidate", "candidate")
                self.assert_invalid(result, "case/repeat")

    def test_null_applicability_mismatch_is_rejected(self):
        candidate = row()
        candidate["verification_fidelity"] = None
        result = self.run_score([row("base"), candidate], "--base", "base", "--candidate", "candidate")
        self.assert_invalid(result, "applicability")

    def test_matched_nulls_do_not_become_zero_or_pass(self):
        rows = [row("base"), row()]
        for item in rows:
            item["architecture_reaction"] = None
        result = self.run_score(rows, "--base", "base", "--candidate", "candidate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("architecture_reaction: n/a -> n/a", result.stdout)
        self.assertNotIn("architecture_reaction: n/a -> n/a; delta", result.stdout)

    def test_invalid_identity_or_metric_is_rejected(self):
        for field, value in (("variant", ""), ("case_id", " L1"),
                             ("repeat", True), ("repeat", 0), ("repeat", 1.0),
                             ("intent_fidelity", 1), ("fact_grounding", "true")):
            with self.subTest(field=field, value=value):
                item = row()
                item[field] = value
                self.assert_invalid(self.run_score([item]), field)
        item = row()
        del item["fact_grounding"]
        self.assert_invalid(self.run_score([item]), "fact_grounding")

    def test_bad_json_empty_input_and_non_object_are_rejected(self):
        for raw, message in (("{\n", "line 1"), ("\n", "no eval rows"), ("[]", "object")):
            with self.subTest(raw=raw):
                self.assert_invalid(self.run_score([], raw=raw), message)

    def test_comparison_requires_two_present_distinct_variants(self):
        for args, message in ((("--base", "base"), "together"),
                              (("--base", "candidate", "--candidate", "candidate"), "distinct"),
                              (("--base", "missing", "--candidate", "candidate"), "missing variant")):
            with self.subTest(args=args):
                self.assert_invalid(self.run_score([row()], *args), message)

    def test_order_does_not_change_report(self):
        rows = [row("base", repeat=2), row(repeat=1), row("base", repeat=1), row(repeat=2)]
        args = ("--base", "base", "--candidate", "candidate")
        self.assertEqual(self.run_score(rows, *args).stdout, self.run_score(rows[::-1], *args).stdout)


if __name__ == "__main__":
    unittest.main()
