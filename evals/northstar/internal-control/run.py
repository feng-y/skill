"""Bind internal-control cases to the existing Codex measurement backend."""
import argparse, concurrent.futures, importlib.util, json, os, shutil, subprocess, tempfile
from pathlib import Path
repo = Path(__file__).resolve().parents[3]
ap = argparse.ArgumentParser()
ap.add_argument('--out', type=Path, required=True)
ap.add_argument('--base', default='84faa9ef7ff6faab1855be9085eb8d0072f28e14')
ap.add_argument('--model', default='gpt-6.1-sol')
ap.add_argument('--repeats', type=int, default=1)
ap.add_argument('--workers', type=int, default=4)
ap.add_argument('--timeout', type=int, default=240)
args = ap.parse_args()
if args.repeats < 1:
    ap.error('--repeats must be positive')
spec = importlib.util.spec_from_file_location('cw', repo / 'evals/northstar/controller_worker.py')
cw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cw)
case = repo / 'evals/northstar/internal-control'
out = args.out.resolve()
out.mkdir(parents=True, exist_ok=False)
cw.save(out / 'identity.json', {'base': args.base, 'model': args.model, 'rubric_sha256': cw.sha((case / 'rubric.md').read_bytes()), 'prompts': {p.name: cw.sha(p.read_bytes()) for p in case.glob('*.txt')}, 'repeats': args.repeats, 'sandbox': 'danger-full-access'})
auth = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'auth.json'

def actor(arm, cell, repeat):
    with tempfile.TemporaryDirectory(prefix='northstar-internal-') as d:
        root = Path(d)
        work = root / 'work'
        home = root / 'home'
        ch = home / '.codex'
        ch.mkdir(parents=True)
        shutil.copyfile(auth, ch / 'auth.json')
        (ch / 'auth.json').chmod(384)
        shutil.copytree(case / 'fixture', work, ignore=shutil.ignore_patterns('__pycache__'))
        subprocess.run(['git', 'init', '-q'], cwd=work, check=True)
        subprocess.run(['git', 'add', '.'], cwd=work, check=True)
        subprocess.run(['git', '-c', 'user.name=Eval', '-c', 'user.email=eval@local', 'commit', '-qm', 'fixture'], cwd=work, check=True)
        target = work / '.agents/skills/northstar'
        target.mkdir(parents=True)
        if arm == 'base':
            for rel in ['SKILL.md', 'references/material-compile.md', 'references/feedback-log.md']:
                p = target / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(subprocess.check_output(['git', 'show', args.base + ':skills/northstar/' + rel], cwd=repo))
        else:
            shutil.copytree(repo / 'skills/northstar', target, dirs_exist_ok=True)
        env = {k: v for (k, v) in os.environ.items() if k in {'PATH', 'LANG', 'LC_ALL', 'HTTPS_PROXY', 'HTTP_PROXY', 'NO_PROXY', 'https_proxy', 'http_proxy', 'no_proxy', 'SSL_CERT_FILE'}}
        env.update(HOME=str(home), CODEX_HOME=str(ch), XDG_CONFIG_HOME=str(home / '.config'), TMPDIR=str(root), PYTHONDONTWRITEBYTECODE='1')
        initial_skill_sha256 = cw.sha((target / 'SKILL.md').read_bytes())
        prompt = (case / ('plan.txt' if cell == 'P' else 'implement.txt')).read_text()
        followup = (case / ('feasibility.txt' if cell == 'P' else 'review.txt')).read_text()
        turns = []
        sid = None
        for (i, prompt_text) in enumerate([prompt, followup]):
            final = root / 'final.txt'
            cmd = ['codex', 'exec'] + (['resume', sid] if sid else []) + ['--ignore-user-config', '--ignore-rules', '--json', '--skip-git-repo-check', '--disable', 'multi_agent', '-m', args.model, '-c', 'approval_policy="never"', '-c', 'sandbox_mode="danger-full-access"', '-c', 'model_reasoning_effort="medium"', '-o', str(final)]
            if not sid:
                cmd += ['--sandbox', 'danger-full-access']
            cmd += ['-']
            before = cw.snapshot(work)
            boundaries = []

            def observe(index, line):
                ev = json.loads(line)
                if ev.get('type') == 'item.completed' and ev.get('item', {}).get('type') in cw.TOOL_TYPES:
                    boundaries.append({'event': index, 'snapshot': cw.snapshot(work)})
            result = cw.process(cmd, cwd=work, env=env, prompt=prompt_text, timeout=args.timeout, on_line=observe)
            events = [json.loads(l) for l in result['stdout'].splitlines() if l.strip()]
            if sid is None:
                sid = next((e.get('thread_id') for e in events if e.get('type') == 'thread.started'), None)
            result.update(prompt=prompt_text, command=cmd, before=before, after=cw.snapshot(work), boundaries=boundaries, final=final.read_text() if final.exists() else '', events=events, thread_id=sid)
            turns.append(result)
            if result['exit_code'] or not sid:
                break
        contexts = []
        for f in (ch / 'sessions').rglob('*.jsonl'):
            for line in f.read_text().splitlines():
                e = json.loads(line)
                if e.get('type') == 'turn_context':
                    contexts.append(e.get('payload', {}).get('model'))
        record = {'arm': arm, 'cell': cell, 'repeat': repeat, 'skill_sha256': initial_skill_sha256, 'skill_unchanged': cw.sha((target / 'SKILL.md').read_bytes()) == initial_skill_sha256, 'models': contexts, 'turns': turns}
        cw.save(out / f'{arm}-{cell}-{repeat}.json', record)
        print(arm, cell, repeat, [t['exit_code'] for t in turns], flush=True)
with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
    list(pool.map(lambda pair: actor(*pair), [(a, c, n) for n in range(1, args.repeats + 1) for a in ['base', 'cand'] for c in ['P', 'I']]))
