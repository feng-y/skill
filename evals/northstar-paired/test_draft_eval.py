"""Synthetic scorer/integrity tests. None are clean-session agent measurements."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import draft_eval as ev


class DraftEvalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cases = ev.load_cases()
        data = b'SYNTHETIC SCORER FIXTURE; not an agent transcript.\nline two\n'
        (self.root / 'fixture.txt').write_bytes(data)
        self.artifact = {'path': 'fixture.txt', 'sha256': ev.digest(data)}

    def row(self, cid='D1', arm='candidate', repeat=1):
        case = self.cases[cid]
        sid = f'{cid}-{arm}-{repeat}'
        r = {k: 'fixed-config' for k in ev.PAIR_EQUAL_FIELDS}
        r.update(case_id=cid, arm=arm, repeat=repeat,
                 skill_ref=('a' if arm == 'base' else 'b') * 40,
                 prompt_sha256=ev.digest(ev.prompt_bytes(case)), session_id=sid,
                 judge_session_id='separate-blind-judge', evidence_kind='synthetic_smoke',
                 clean_session=False, blind_judge=True, prototype_invocations=0,
                 facts_closed_before_prototype=False,
                 executable_handoff=case['expected_executable_handoff'],
                 artifacts={k: copy.deepcopy(self.artifact) for k in (
                     ['trace', 'result', 'probe'] if case['intents'] else ['trace', 'result'])})
        if case['intents']:
            r['probe_session_id'] = sid + '-probe'
        r['checks'] = {}
        for name in case['checks']:
            source = 'probe' if name == 'draft_sufficiency' else 'trace' if name in {
                'routing', 'owner_retention', 'prototype_discipline'} else 'result'
            r['checks'][name] = {'ok': True, 'evidence': [{'artifact': source, 'lines': [1, 1]}]}
        return r

    def pair(self, cid='D1'):
        return [self.row(cid, a) for a in ev.ARMS]

    def analyze(self, rows):
        return ev.analyze(rows, self.cases, self.root)

    def test_empty_is_inconclusive(self):
        self.assertEqual(self.analyze([])['decision'], 'INCONCLUSIVE')

    def test_synthetic_never_promotes(self):
        rows = [self.row(cid, a, rep) for cid in self.cases for rep in (1, 2, 3) for a in ev.ARMS]
        report = self.analyze(rows)
        self.assertTrue(report['complete_3_repeat_suite'])
        self.assertEqual(report['projection'], 'FOCUSED_NON_REGRESSION')
        self.assertEqual(report['decision'], 'SCORER_SMOKE_ONLY')
        self.assertEqual(report['behavioral_uplift'], 'INCONCLUSIVE')

    def test_called_prototype_but_missing_draft_fails(self):
        rows = self.pair()
        rows[1]['prototype_invocations'] = 1
        rows[1]['checks']['draft_sufficiency']['ok'] = False
        self.assertIn('D1/1:draft_sufficiency', self.analyze(rows)['failures'])

    def test_disconnected_fragments_fail(self):
        rows = self.pair('D3')
        rows[1]['checks']['integration']['ok'] = False
        self.assertIn('D3/1:integration', self.analyze(rows)['regressions'])

    def test_parallel_authorities_fail(self):
        rows = self.pair()
        rows[1]['checks']['single_primary_draft']['ok'] = False
        self.assertTrue(self.analyze(rows)['failures'])

    def test_two_intents_are_not_global_singleton(self):
        self.assertEqual(self.cases['D8']['intents'], 2)
        self.assertFalse(self.analyze(self.pair('D8'))['failures'])

    def test_owner_takeover_fails(self):
        for cid in ('D5', 'D6', 'D7'):
            with self.subTest(case=cid):
                rows = self.pair(cid)
                rows[1]['checks']['owner_retention']['ok'] = False
                self.assertIn(f'{cid}/1:owner_retention', self.analyze(rows)['failures'])

    def test_optional_prototype_not_mandatory(self):
        self.assertFalse(self.analyze(self.pair('D1'))['failures'])

    def test_already_concrete_over_trigger_fails(self):
        rows = self.pair('D4')
        rows[1]['prototype_invocations'] = 1
        self.assertIn('D4/1:prototype_over_trigger', self.analyze(rows)['failures'])

    def test_prototype_before_facts_fails(self):
        rows = self.pair('D2')
        rows[1]['prototype_invocations'] = 1
        self.assertIn('D2/1:prototype_over_trigger', self.analyze(rows)['failures'])

    def test_blocked_draft_not_executable(self):
        rows = self.pair('D2')
        self.assertFalse(self.analyze(rows)['failures'])
        rows[1]['executable_handoff'] = True
        self.assertIn('D2/1:handoff_disposition', self.analyze(rows)['failures'])

    def test_unknown_grade_not_pass(self):
        rows = self.pair()
        rows[1]['checks']['draft_sufficiency'] = {'ok': None, 'evidence': []}
        report = self.analyze(rows)
        self.assertIn('D1/1:draft_sufficiency', report['unmeasured'])
        self.assertIsNone(report['measurements']['candidate']['draft_sufficiency']['rate'])

    def test_missing_pair_rejected(self):
        with self.assertRaisesRegex(ValueError, 'incomplete pairs'):
            self.analyze([self.row()])

    def test_mismatched_settings_rejected(self):
        rows = self.pair()
        rows[1]['model'] = 'other-model'
        with self.assertRaisesRegex(ValueError, 'paired field'):
            self.analyze(rows)

    def test_mutated_prompt_rejected(self):
        rows = self.pair()
        rows[1]['prompt_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'frozen case'):
            self.analyze(rows)

    def test_reused_session_or_self_judge_rejected(self):
        for field in ('session_id', 'judge_session_id', 'probe_session_id'):
            with self.subTest(field=field):
                rows = self.pair()
                rows[1][field] = rows[0]['session_id']
                with self.assertRaisesRegex(ValueError, 'session reused|judging itself'):
                    self.analyze(rows)

    def test_missing_artifact_rejected(self):
        rows = self.pair()
        del rows[1]['artifacts']['probe']
        with self.assertRaisesRegex(ValueError, 'artifact'):
            self.analyze(rows)

    def test_forged_hash_rejected(self):
        rows = self.pair()
        rows[1]['artifacts']['trace']['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.analyze(rows)

    def test_out_of_root_path_rejected(self):
        rows = self.pair()
        rows[1]['artifacts']['trace']['path'] = '../elsewhere'
        with self.assertRaisesRegex(ValueError, 'inside evidence root'):
            self.analyze(rows)

    def test_forged_span_rejected(self):
        rows = self.pair()
        rows[1]['checks']['integration']['evidence'][0]['lines'] = [1, 999]
        with self.assertRaisesRegex(ValueError, 'line span'):
            self.analyze(rows)

    def test_sufficiency_needs_independent_probe_evidence(self):
        rows = self.pair()
        rows[1]['checks']['draft_sufficiency']['evidence'][0]['artifact'] = 'result'
        with self.assertRaisesRegex(ValueError, 'needs probe'):
            self.analyze(rows)

    def test_over_trigger_cannot_hide_behind_green_grade(self):
        rows = self.pair('D4')
        rows[1]['prototype_invocations'] = 1
        report = self.analyze(rows)
        self.assertIn('D4/1:prototype_over_trigger', report['regressions'])
        self.assertEqual(report['measurements']['candidate']['prototype_discipline']['rate'], 0)

    def test_unclean_real_metadata_not_synthetic_pass(self):
        rows = self.pair()
        for row in rows:
            row['evidence_kind'] = 'clean_session'
        self.assertEqual(self.analyze(rows)['decision'], 'INCONCLUSIVE')

    def test_repeats_must_freeze_configuration(self):
        rows = self.pair() + [self.row('D1', a, 2) for a in ev.ARMS]
        for row in rows[2:]:
            row['model'] = 'second-model'
        with self.assertRaisesRegex(ValueError, 'across repeats'):
            self.analyze(rows)

    def test_export_command_and_empty_score_exit(self):
        self.assertEqual(ev.main(['export-prompts', str(self.root/'exported')]), 0)
        results = self.root / 'empty.jsonl'
        results.write_text('')
        self.assertEqual(ev.main(['score', str(results), '--evidence-root', str(self.root)]), 3)

    def test_export_excludes_private_rubric(self):
        out = self.root / 'actor-input'
        ev.export_prompts(self.cases, out)
        self.assertEqual(len(list(out.iterdir())), 8)
        for file, case in zip(sorted(out.iterdir()), self.cases.values()):
            self.assertEqual(file.read_bytes(), ev.prompt_bytes(case))
            self.assertNotIn(case['judge'], file.read_text())
        with self.assertRaises(FileExistsError):
            ev.export_prompts(self.cases, out)


if __name__ == '__main__':
    unittest.main()
