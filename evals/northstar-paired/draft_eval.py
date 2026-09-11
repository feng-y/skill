#!/usr/bin/env python3
"""Evidence-checked sidecar for Draft/owner behavior; not an LLM judge or runner."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from score import ARMS, PAIR_EQUAL_FIELDS, validate_pairs

CASES_FILE = Path(__file__).with_name('draft-cases.json')
COMMON = {'routing', 'owner_retention', 'factual_discipline', 'prototype_discipline'}
DRAFT = {'single_primary_draft', 'draft_sufficiency', 'integration'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prompt_bytes(case):
    return (case['prompt'] + '\n').encode('utf-8')


def load_cases(path=CASES_FILE):
    items = json.loads(Path(path).read_text(encoding='utf-8'))['cases']
    cases = {c['id']: c for c in items}
    if not cases or len(cases) != len(items):
        raise ValueError('empty or duplicate case IDs')
    for c in cases.values():
        expected = COMMON | (DRAFT if c['intents'] else set())
        if set(c['checks']) != expected or len(c['checks']) != len(expected):
            raise ValueError(f"{c['id']}: incomplete check set")
        if not c['prompt'].strip() or c['prototype'] not in {
            'optional', 'forbidden', 'forbidden_before_fact_closure'
        }:
            raise ValueError(f"{c['id']}: invalid prompt/Prototype policy")
    return cases


def export_prompts(cases, out):
    # A new directory prevents stale rubrics or prior outputs leaking into input.
    out.mkdir(parents=True, exist_ok=False)
    for index, case in enumerate(cases.values(), 1):
        (out / f'{index:02d}.txt').write_bytes(prompt_bytes(case))


def artifact_lines(item, root):
    path = (root / item['path']).resolve()
    if Path(item['path']).is_absolute() or not path.is_relative_to(root.resolve()):
        raise ValueError('artifact must remain inside evidence root')
    data = path.read_bytes()
    if not data.strip() or digest(data) != item['sha256']:
        raise ValueError(f'artifact missing content or hash mismatch: {path.name}')
    return data.decode('utf-8').splitlines()


def validate(records, cases, root):
    actors, probes, judges = [], [], []
    for row in records:
        case = cases.get(row.get('case_id'))
        if case is None:
            raise ValueError('unknown case ID')
        for key in ('session_id', 'judge_session_id', 'skill_ref', *PAIR_EQUAL_FIELDS):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f'missing/non-string {key}')
        if not re.fullmatch(r'[0-9a-f]{40}', row['skill_ref']):
            raise ValueError('skill_ref must be an immutable commit SHA')
        if row['arm'] not in ARMS or type(row['repeat']) is not int or row['repeat'] < 1:
            raise ValueError('invalid arm/repeat')
        if row['prompt_sha256'] != digest(prompt_bytes(case)):
            raise ValueError('prompt differs from frozen case')
        if row['evidence_kind'] not in ('synthetic_smoke', 'clean_session'):
            raise ValueError('invalid evidence_kind')
        if type(row['clean_session']) is not bool or type(row['blind_judge']) is not bool:
            raise ValueError('clean_session and blind_judge must be booleans')
        count = row['prototype_invocations']
        if type(count) is not int or count < 0:
            raise ValueError('invalid Prototype count')
        if type(row['facts_closed_before_prototype']) is not bool:
            raise ValueError('fact closure must be boolean')
        actors.append(row['session_id'])
        judges.append(row['judge_session_id'])
        artifacts = row['artifacts']
        required = {'trace', 'result'} | ({'probe'} if case['intents'] else set())
        if set(artifacts) != required:
            raise ValueError('missing or unexpected trace/result/probe artifact')
        lines = {k: artifact_lines(v, root) for k, v in artifacts.items()}
        if case['intents']:
            probe = row.get('probe_session_id')
            if not isinstance(probe, str) or not probe.strip():
                raise ValueError('missing independent probe session')
            probes.append(probe)
            if type(row['executable_handoff']) is not bool:
                raise ValueError('executable_handoff must be boolean for Intent cases')
        elif row.get('executable_handoff') is not None:
            raise ValueError('independent AE/Verify/factual tasks are not Intent handoffs')
        if set(row['checks']) != set(case['checks']):
            raise ValueError('missing or unexpected grades')
        for name, grade in row['checks'].items():
            ok, witnesses = grade['ok'], grade['evidence']
            if ok is not None and type(ok) is not bool:
                raise ValueError('grade must be true, false or null')
            if not isinstance(witnesses, list) or (ok is not None and not witnesses):
                raise ValueError('measured grades require evidence spans')
            for w in witnesses:
                start, end = w['lines']
                if (w['artifact'] not in lines or type(start) is not int or type(end) is not int
                        or not 1 <= start <= end <= len(lines[w['artifact']])):
                    raise ValueError('invalid evidence line span')
            needs = 'probe' if name == 'draft_sufficiency' else 'trace' if name in {
                'routing', 'owner_retention', 'prototype_discipline'
            } else 'result'
            if ok is not None and not any(w['artifact'] == needs for w in witnesses):
                raise ValueError(f'{name} needs {needs} evidence')
    if len(set(actors + probes)) != len(actors + probes) or set(actors + probes) & set(judges):
        raise ValueError('candidate/probe session reused or judging itself')
    pairs = validate_pairs(records)
    for case_id in cases:
        for field in PAIR_EQUAL_FIELDS:
            if len({r[field] for r in records if r['case_id'] == case_id}) > 1:
                raise ValueError(f'{case_id}: frozen setting changed across repeats: {field}')
    for arm in ARMS:
        if len({r['skill_ref'] for r in records if r['arm'] == arm}) > 1:
            raise ValueError('arm revision changed within suite')
    return pairs


def gate_errors(row, case):
    errors = []
    if row['prototype_invocations'] and (case['prototype'] == 'forbidden' or (
            case['prototype'] == 'forbidden_before_fact_closure'
            and not row['facts_closed_before_prototype'])):
        errors.append('prototype_over_trigger')
    if case['intents'] and row['executable_handoff'] != case['expected_executable_handoff']:
        errors.append('handoff_disposition')
    return errors


def effective_grade(row, case, name):
    errors = gate_errors(row, case)
    if (name == 'prototype_discipline' and 'prototype_over_trigger' in errors
            or name == 'draft_sufficiency' and 'handoff_disposition' in errors):
        return False
    return row['checks'][name]['ok']


def analyze(records, cases, root):
    if not records:
        return {'decision': 'INCONCLUSIVE', 'runs': 0, 'reason': 'no agent runs',
                'behavioral_uplift': 'INCONCLUSIVE'}
    pairs = validate(records, cases, root)
    failures, regressions, improvements, unknown = [], [], [], []
    for (case_id, repeat), arms in pairs.items():
        case = cases[case_id]
        for name in case['checks']:
            base, candidate = (effective_grade(arms[a], case, name) for a in ARMS)
            item = f'{case_id}/{repeat}:{name}'
            if candidate is False:
                failures.append(item)
                if base is True:
                    regressions.append(item)
            if candidate is True and base is False:
                improvements.append(item)
            if base is None or candidate is None:
                unknown.append(item)
        for error in gate_errors(arms['candidate'], case):
            item = f'{case_id}/{repeat}:{error}'
            failures.append(item)
            if error not in gate_errors(arms['base'], case):
                regressions.append(item)
    complete = all(len({rep for cid, rep in pairs if cid == c}) >= 3 for c in cases)
    clean = all(r['evidence_kind'] == 'clean_session' and r['clean_session']
                and r['blind_judge'] for r in records)
    projection = ('REGRESSION' if regressions else 'FIX_REQUIRED' if failures
                  else 'INCONCLUSIVE' if unknown or not complete else 'FOCUSED_NON_REGRESSION')
    synthetic = all(r['evidence_kind'] == 'synthetic_smoke' for r in records)
    decision = projection if clean else 'SCORER_SMOKE_ONLY' if synthetic else 'INCONCLUSIVE'
    measurements = {}
    for arm in ARMS:
        measurements[arm] = {}
        for name in sorted(COMMON | DRAFT):
            values = [effective_grade(r, cases[r['case_id']], name) for r in records
                      if r['arm'] == arm and name in r['checks']]
            measured = sum(v is not None for v in values)
            measurements[arm][name] = {'pass': sum(v is True for v in values),
                'measured': measured, 'unknown': len(values) - measured,
                'rate': sum(v is True for v in values) / measured if measured else None}
    return {'decision': decision, 'projection': projection, 'runs': len(records),
            'complete_3_repeat_suite': complete, 'measurements': measurements,
            'failures': failures, 'regressions': regressions, 'improved_pairs': improvements,
            'unmeasured': unknown, 'behavioral_uplift': 'INCONCLUSIVE',
            'scope': 'Frozen reconstructed/constructed cases; no broad uplift or cost claim. '
                     'Artifact identity checks do not authenticate session-isolation metadata.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    export = sub.add_parser('export-prompts')
    export.add_argument('out', type=Path)
    score = sub.add_parser('score')
    score.add_argument('results', type=Path)
    score.add_argument('--evidence-root', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        cases = load_cases()
        if args.command == 'export-prompts':
            export_prompts(cases, args.out)
            print(f'Exported {len(cases)} organic prompts; no rubric or expected routes.')
            return 0
        records = [json.loads(line) for line in args.results.read_text(encoding='utf-8').splitlines()
                   if line.strip()]
        report = analyze(records, cases, args.evidence_root)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report['decision'] == 'FOCUSED_NON_REGRESSION':
            return 0
        return 1 if report['decision'] in ('FIX_REQUIRED', 'REGRESSION') else 3
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
