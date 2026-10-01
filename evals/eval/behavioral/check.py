#!/usr/bin/env python3
"""Independent state and counterexample checks; semantic decisions use judge.py."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def check(run):
    result = json.loads((run / 'run-result.json').read_text())
    before, after = [s['artifact_files'] for s in result['snapshots']]
    case = result['case_id']
    immutable = {'E11': ['runtime.txt', 'records.json', 'surface.json'],
                 'E12': ['experiments.json', 'exposure.json'],
                 'E13': ['runtime.txt', 'records.json', 'attempts.json']}[case]
    checks = {f'preserved:{p}': before[p]['sha256'] == after.get(p, {}).get('sha256') for p in immutable}
    checks['completed'] = result['completed_all_turns']
    checks['findings_written'] = 'findings.md' in after
    events = [json.loads(line) for line in (run / 'turn-1.jsonl').read_text().splitlines()]
    checks['selected_eval_skill_loaded'] = any(
        e.get('type') == 'item.completed'
        and e.get('item', {}).get('type') == 'command_execution'
        and 'codex-home/skills/' in e['item'].get('command', '')
        and '/eval/SKILL.md' in e['item'].get('command', '')
        and '# Eval' in e['item'].get('aggregated_output', '')
        and e['item'].get('exit_code') == 0
        for e in events
    )
    if case != 'E12':
        records = json.loads(before['records.json']['content'])
        expected = {r['id']: r['answer']['retry_limit'] == 3 and r['answer']['citation'] == 'ops/retry' for r in records}
        actual = json.loads(after.get('scores.json', {}).get('content', '{}'))
        checks['both_configurations_regraded_correctly'] = actual == expected
        # Use fresh copies to avoid changing the captured actor workspace.
        # An always-pass grader must fail these two independent probes.
        for field, wrong in [('retry_limit', 19), ('citation', 'unrelated/doc')]:
            with tempfile.TemporaryDirectory(prefix='eval-grader-probe-') as directory:
                workspace = Path(directory) / 'workspace'
                shutil.copytree(run / 'workspace', workspace, ignore=shutil.ignore_patterns('.git', '__pycache__'))
                mutated = json.loads(json.dumps(records))
                for row in mutated:
                    row['answer'][field] = wrong
                    row['artifacts'] = ['audit.md']
                (workspace / 'records.json').write_text(json.dumps(mutated))
                (workspace / 'scores.json').unlink(missing_ok=True)
                proc = subprocess.run([sys.executable, 'grade.py'], cwd=workspace, text=True, capture_output=True, timeout=30)
                path = workspace / 'scores.json'
                scores = json.loads(path.read_text()) if path.exists() else {}
                checks[f'rejects_wrong:{field}'] = proc.returncode == 0 and scores == {r['id']: False for r in mutated}
    output = {'case_id': case, 'checks': checks, 'all_pass': all(checks.values())}
    (run / 'independent-checks.json').write_text(json.dumps(output, indent=2) + '\n')
    return output


if __name__ == '__main__':
    root = Path(sys.argv[1])
    results = {p.name: check(p) for p in sorted((root / 'runs').iterdir())}
    (root / 'independent-checks.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
    raise SystemExit(0 if all(r['all_pass'] for r in results.values()) else 1)
