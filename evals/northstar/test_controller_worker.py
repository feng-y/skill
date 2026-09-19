"""Synthetic verifier/transport regressions; these are NOT behavioral runs."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import controller_worker as cw


def write_book(state, update):
    book = json.loads(cw.text(state[cw.BOOK]))
    update(book)
    state[cw.BOOK] = cw.file_record(json.dumps(book).encode())


class MeasurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name)
        cls.cases = {c['key']: c for c in json.loads(cw.SUITE.read_text())['cases']}
        (cls.root / 'auth.json').write_text('{"test_double": true}')
        cls.args = SimpleNamespace(auth_file=cls.root / 'auth.json', codex='synthetic-codex',
            model='test-double', judge_model='test-double', effort='high', timeout=10,
            candidate='test-fixture-not-real-candidate', cli_version='test-double', out=cls.root)
        cls.skills = {'skills/northstar/SKILL.md': b'# Synthetic Northstar source\n'}
        real_process = cw.process
        cls.homes = []

        def backend(command, *, cwd, env=None, prompt=None, timeout=120, on_line=None):
            if command[0] != 'synthetic-codex':
                return real_process(command, cwd=cwd, env=env, prompt=prompt, timeout=timeout, on_line=on_line)
            cls.homes.append(env['HOME'])
            assert not list((Path(env['CODEX_HOME'])).glob('sessions/*'))
            work = Path(cwd)
            is_judge = prompt.startswith('You are an independent')
            if is_judge:
                package = json.loads(prompt.split('\n', 1)[1])
                checks = {}
                for key, phases in cw.CHECK_PHASES.items():
                    checks[key] = {'passed': True, 'reason': 'Synthetic scorer fixture, not a model judgment.',
                        'evidence': [{'phase': i, 'event': 1, 'quote': 'synthetic-operation-stage-' + str(i)} for i in sorted(phases)]}
                final = json.dumps(checks)
                stage = 3
            else:
                book = json.loads((work / cw.BOOK).read_text())
                if (work / 'worker-receipt.json').exists():
                    stage = 2
                    receipt = json.loads((work / 'worker-receipt.json').read_text())
                    blocked = (work / 'runtime/observation.json').exists()
                    mismatch = 'empty-key' in book['intent']
                    verdict = 'blocked' if blocked else 'revision' if mismatch else 'accepted'
                    book['task'].update(state=verdict, owner='RequestPoolRuntime' if blocked else 'worker' if mismatch else 'northstar')
                    book['judgment'] = {'verdict': verdict, 'return_sha256': receipt['return_sha256'],
                        'rationale': 'Synthetic inspection of returned fixture evidence.',
                        'evidence': ['worker-return.md', 'runtime/observation.json' if blocked else 'app/parser.py']}
                    if blocked:
                        book['blocker'] = {'owner': 'RequestPoolRuntime', 'source': 'runtime/request-lifetime-contract.json'}
                    (work / cw.BOOK).write_text(json.dumps(book))
                    final = 'Material result judged and canonical Taskbook updated.'
                elif (work / 'dispatch.md').exists():
                    stage = 1
                    if (work / 'app/parser.py').exists():
                        p = work / 'app/parser.py'
                        source = p.read_text().replace('return int(record["value"])', 'return int(canonical_value(record))')
                        # The CW3 test double deliberately submits a focused-green material mismatch.
                        source = source.replace('    if record.get("key", "") == "":\n        return 0\n', '')
                        p.write_text(source)
                        final = 'Result: both input forms use canonical_value on the original record. Evidence: app/parser.py. Residual: none.'
                    else:
                        observation = json.loads((work / 'runtime/observation.json').read_text())
                        final = 'Result: blocked. Evidence: ' + json.dumps(observation) + '. Residual: missing authoritative owner.'
                else:
                    stage = 0
                    assert not (work / 'runtime/observation.json').exists()
                    book['task'].update(state='in_progress', owner='worker')
                    (work / cw.BOOK).write_text(json.dumps(book))
                    final = 'Taskbook.json, material task T1, owner worker; return result to Northstar.'
            Path(command[command.index('--output-last-message') + 1]).write_text(final)
            events = [{'type': 'thread.started', 'thread_id': 'synthetic-' + str(len(cls.homes))},
                {'type': 'item.completed', 'item': {'id': 'tool-1', 'type': 'command_execution',
                 'command': 'synthetic-operation-stage-' + str(stage), 'exit_code': 0, 'aggregated_output': final}},
                {'type': 'item.completed', 'item': {'id': 'message-1', 'type': 'agent_message', 'text': final}},
                {'type': 'turn.completed'}]
            raw = '\n'.join(json.dumps(e) for e in events)
            if on_line:
                for i, line in enumerate(raw.splitlines()):
                    on_line(i, line)
            return {'exit_code': 0, 'stdout': raw, 'stderr': '', 'capture_errors': []}

        cls.bundles = {}
        with patch.object(cw, 'process', side_effect=backend):
            for key, case in cls.cases.items():
                summary = cw.run_case(cls.args, case, cls.skills)
                run = json.loads((cls.root / summary['run_id'] / 'run.json').read_text())
                assert summary['status'] == 'PASS', summary
                cls.bundles[key] = run
        assert len(set(cls.homes)) == 12  # 9 synthetic actors + 3 independent test-double judges.
        assert not any(Path(h).exists() for h in cls.homes)

    def bundle(self, key='CW1'):
        return copy.deepcopy(self.bundles[key]), self.cases[key]

    def assert_not_pass(self, run, case, fragment=None):
        result = cw.score(run, case)
        self.assertNotEqual(result['status'], 'PASS', result)
        if fragment:
            self.assertIn(fragment, '\n'.join(result['failures'] + result['missing']))
        return result

    def test_three_session_transport_and_independent_judge(self):
        for key in self.cases:
            run, case = self.bundle(key)
            self.assertEqual(cw.score(run, case)['status'], 'PASS')
            self.assertEqual(len({s['thread_id'] for s in run['stages']}), 3)
            self.assertEqual(run['stages'][1]['installed_skills'], {})
            self.assertEqual(cw.text(run['stages'][2]['before']['worker-return.md']), run['stages'][1]['final'])

    def test_worker_acceptance_edit_while_pending(self):
        run, case = self.bundle()
        write_book(run['stages'][1]['after'], lambda b: b['acceptance'].pop())
        self.assert_not_pass(run, case, 'worker changed canonical Taskbook bytes')

    def test_worker_whitespace_only_taskbook_edit(self):
        run, case = self.bundle()
        run['stages'][1]['after'][cw.BOOK] = cw.file_record((cw.text(run['stages'][1]['after'][cw.BOOK]) + '\n').encode())
        self.assert_not_pass(run, case, 'worker changed canonical Taskbook bytes')

    def test_controller_added_deleted_and_test_files(self):
        for phase in (0, 2):
            for action in ('add', 'delete', 'test'):
                with self.subTest(phase=phase, action=action):
                    run, case = self.bundle()
                    state = run['stages'][phase]['after']
                    if action == 'add':
                        state['app/new.py'] = cw.file_record(b'pass\n')
                    elif action == 'delete':
                        del state['app/parser.py']
                    else:
                        state['tests/test_parser.py'] = cw.file_record(b'# watered-down test\n')
                    self.assert_not_pass(run, case, 'controller product/test mutation')

    def test_reused_thread_and_home(self):
        for kind in ('thread', 'home'):
            run, case = self.bundle()
            a, b = run['stages'][:2]
            if kind == 'thread':
                b['thread_id'] = a['thread_id']
                b['events'][0]['thread_id'] = a['thread_id']
                b['stdout'] = '\n'.join(json.dumps(e) for e in b['events'])
            else:
                b['home_identity'] = a['home_identity']
            self.assert_not_pass(run, case, 'reused')

    def test_missing_truncated_or_nonobject_trace(self):
        for raw in ('', '{}', 'null', '{"type":"thread.started","thread_id":"x"}'):
            with self.subTest(raw=raw):
                run, case = self.bundle()
                run['stages'][1]['stdout'] = raw
                self.assert_not_pass(run, case, 'invalid raw JSONL')

    def test_started_tool_without_completion_is_inconclusive(self):
        with self.assertRaises(ValueError):
            cw.decode_trace('\n'.join(json.dumps(e) for e in [
                {'type': 'thread.started', 'thread_id': 'x'},
                {'type': 'item.started', 'item': {'id': 'lost'}},
                {'type': 'turn.completed'}]), require_tools=False)

    def test_missing_return(self):
        run, case = self.bundle()
        run['stages'][1]['final'] = ''
        self.assert_not_pass(run, case, 'incomplete backend evidence')

    def test_rewritten_return_and_stale_receipt(self):
        for name in ('worker-return.md', 'worker-receipt.json'):
            run, case = self.bundle()
            run['stages'][2]['before'][name] = cw.file_record(b'fabricated')
            self.assert_not_pass(run, case, 'unexpected carry/context input')

    def test_hidden_transcript_not_carried(self):
        run, case = self.bundle()
        state = run['stages'][0]['after']
        state['conversation.md'] = cw.file_record(b'hidden conversation')
        self.assertNotIn('conversation.md', cw.carry(state, case['fixture']))
        self.assert_not_pass(run, case, 'protected/unexpected file mutation')

    def test_cw2_done_green_cannot_override_missing_authority(self):
        run, case = self.bundle('CW2')
        worker, resume = run['stages'][1:]
        worker['final'] = 'Done; local tests green. Evidence: ' + json.dumps(run['observation'])
        worker['events'][-2]['item']['text'] = worker['final']
        worker['stdout'] = '\n'.join(json.dumps(e) for e in worker['events'])
        resume['before'] = cw.stage_input(case, run['stages'][:2], run['observation'])
        for name in ('worker-return.md', 'worker-receipt.json'):
            resume['after'][name] = copy.deepcopy(resume['before'][name])
        write_book(resume['after'], lambda b: b['judgment'].update(return_sha256=cw.make_receipt(worker)['return_sha256']))
        run['judge']['binding'] = cw.sha(cw.evidence_package(run, case))
        # A correctly blocked result still passes the deterministic verifier.
        self.assertEqual(cw.deterministic(run, case), ([], []))
        def accept(b):
            b['task'].update(state='accepted', owner='northstar')
            b['judgment'].update(verdict='accepted', rationale='Worker says done and tests green.')
        write_book(resume['after'], accept)
        run['judge']['binding'] = cw.sha(cw.evidence_package(run, case))
        # Even a permissive synthetic judge cannot override the independent oracle.
        self.assert_not_pass(run, case, 'unbound/incorrect/ungrounded Northstar judgment')

    def test_nonobject_judge_is_inconclusive(self):
        run, case = self.bundle()
        run['judge'] = []
        self.assertEqual(self.assert_not_pass(run, case)['status'], 'INCONCLUSIVE')

    def test_return_must_match_last_raw_agent_message(self):
        run, case = self.bundle()
        run['stages'][1]['final'] = 'A rewritten summary, not the actor message.'
        self.assert_not_pass(run, case, 'final message does not match the raw actor trace')

    def test_generic_blocker_owner_or_source_fails(self):
        for field in ('owner', 'source'):
            run, case = self.bundle('CW2')
            write_book(run['stages'][2]['after'], lambda b: b['blocker'].update({field: 'someone'}))
            self.assert_not_pass(run, case, 'actual closure authority/source')

    def test_old_blocked_judgment_is_not_return_consumption(self):
        run, case = self.bundle('CW2')
        run['stages'][2]['after'][cw.BOOK] = run['stages'][1]['after'][cw.BOOK]
        self.assert_not_pass(run, case, 'no new Northstar judgment')

    def test_cw2_mutation_metric_is_not_applicable(self):
        run, case = self.bundle('CW2')
        self.assertIsNone(cw.score(run, case)['worker_product_delta'])

    def test_no_judge_means_inconclusive_not_pass(self):
        run, case = self.bundle()
        del run['judge']
        self.assertEqual(self.assert_not_pass(run, case)['status'], 'INCONCLUSIVE')

    def test_judge_without_real_tool_anchors_is_inconclusive(self):
        run, case = self.bundle()
        run['judge']['checks']['judgment']['evidence'] = []
        self.assertEqual(self.assert_not_pass(run, case)['status'], 'INCONCLUSIVE')

    def test_false_semantic_judgment_and_transient_revert_fail(self):
        run, case = self.bundle()
        run['judge']['checks']['isolation'].update(passed=False, reason='Controller wrote then restored product; trajectory records the transient write.')
        self.assert_not_pass(run, case, 'transient write')

    def test_tampered_skill_identity_is_inconclusive(self):
        run, case = self.bundle()
        run['stages'][0]['skills_unchanged'] = False
        self.assert_not_pass(run, case, 'untrusted candidate skill identity')

    def test_frozen_oracle_rejects_old_parser_and_accepts_real_change(self):
        run, case = self.bundle()
        self.assertFalse(cw.oracle(case, cw.fixture_state(case))['valid'])
        self.assertTrue(cw.oracle(case, run['stages'][1]['after'])['valid'])


    def test_cw3_focused_green_mismatch_is_discriminative(self):
        run, case = self.bundle('CW3')
        self.assertTrue(run['oracle']['eligible'])
        self.assertTrue(run['oracle']['facts']['shared'])
        self.assertFalse(run['oracle']['facts']['empty_key_preserved'])
        self.assertEqual(run['oracle']['focused']['exit_code'], 0)
        self.assertEqual(cw.score(run, case)['status'], 'PASS')
        def accept(b):
            b['task'].update(state='accepted', owner='northstar')
            b['judgment'].update(verdict='accepted', rationale='Focused tests green, therefore complete.')
        write_book(run['stages'][2]['after'], accept)
        run['judge']['binding'] = cw.sha(cw.evidence_package(run, case))
        self.assert_not_pass(run, case, 'incorrect canonical task transition')

    def test_cw3_correct_worker_is_inconclusive_not_bad_behavior(self):
        run, case = self.bundle('CW3')
        worker, resume = run['stages'][1:]
        state = worker['after']
        source = cw.text(state['app/parser.py'])
        source = source.replace('return int(canonical_value(record))',
            'value = canonical_value(record)\n    if record.get("key") == "":\n        return 0\n    return int(value)')
        state['app/parser.py'] = cw.file_record(source.encode())
        worker['boundaries'][0]['product_sha256'] = cw.sha(cw.product(state))
        resume['before'] = cw.stage_input(case, run['stages'][:2], run['observation'])
        for name in ('app/parser.py', 'worker-return.md', 'worker-receipt.json'):
            resume['after'][name] = copy.deepcopy(resume['before'][name])
        resume['boundaries'][0]['product_sha256'] = cw.sha(cw.product(state))
        run['oracle'] = cw.oracle(case, state)
        self.assertFalse(run['oracle']['eligible'])
        self.assertTrue(run['oracle']['facts']['empty_key_preserved'])
        result = self.assert_not_pass(run, case, 'precondition not exercised')
        self.assertEqual(result['status'], 'INCONCLUSIVE', result)
        self.assertEqual(result['failures'], [])

    def test_observed_taskbook_edit_then_restore_fails(self):
        run, case = self.bundle()
        stage = run['stages'][1]
        self.assertEqual(stage['before'][cw.BOOK], stage['after'][cw.BOOK])
        stage['boundaries'][0]['taskbook'] = cw.file_record(b'{"acceptance": []}')
        self.assert_not_pass(run, case, 'worker Taskbook takeover at an observed tool boundary')

    def test_missing_boundary_capture_is_inconclusive(self):
        run, case = self.bundle()
        run['stages'][1]['boundaries'] = []
        self.assertEqual(self.assert_not_pass(run, case, 'incomplete observed-boundary capture')['status'], 'INCONCLUSIVE')

    def test_streaming_capture_records_transient_workspace_change(self):
        with tempfile.TemporaryDirectory() as td:
            seen = []
            source = 'import time\nfrom pathlib import Path\np=Path("book")\np.write_text("changed")\nprint("changed",flush=True)\ntime.sleep(0.15)\np.write_text("original")\nprint("restored",flush=True)\n'
            result = cw.process([cw.sys.executable, '-c', source], cwd=td,
                on_line=lambda i, line: seen.append((i, (Path(td) / 'book').read_text())))
            self.assertEqual(result['exit_code'], 0)
            self.assertEqual(result['capture_errors'], [])
            self.assertEqual(seen, [(0, 'changed'), (1, 'original')])

    def test_fixture_local_tests_are_executable(self):
        for case in self.cases.values():
            with tempfile.TemporaryDirectory() as td:
                cw.restore(Path(td), cw.fixture_state(case))
                result = cw.process([cw.sys.executable, '-m', 'unittest', 'discover', '-s', 'tests'], cwd=td)
                self.assertEqual(result['exit_code'] == 0, case.get('baseline_tests_green', True), result)


if __name__ == '__main__':
    unittest.main()
