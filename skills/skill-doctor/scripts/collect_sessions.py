#!/usr/bin/env python3
"""Collect recent local Codex/Claude conversations and installed skills.

Python 3.9+, stdlib only. Reads local files only and writes condensed transcripts
plus inventory.json to --out.
"""
import argparse, hashlib, json, os, re, subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

MAX_TEXT, MAX_TOOL, MAX_ENTRIES = 1800, 700, 180

def args():
    p=argparse.ArgumentParser(); p.add_argument('--harness',choices=('auto','codex','claude'),default='auto')
    p.add_argument('--repo',action='append',default=[]); p.add_argument('--all-conversations',action='store_true')
    p.add_argument('--include-global-skills',action='store_true'); p.add_argument('--include-subagents',action='store_true')
    p.add_argument('--days',type=int,default=45); p.add_argument('--max-sessions',type=int,default=12)
    p.add_argument('--skills-dir',action='append',default=[]); p.add_argument('--codex-home',default=os.environ.get('CODEX_HOME','~/.codex'))
    p.add_argument('--claude-home',default=os.environ.get('CLAUDE_CONFIG_DIR','~/.claude')); p.add_argument('--out',required=True)
    return p.parse_args()

def git_root(v='.'): 
    try:
        r=subprocess.run(['git','-C',str(Path(v).expanduser()),'rev-parse','--show-toplevel'],capture_output=True,text=True,timeout=5)
        if r.returncode==0 and r.stdout.strip(): return Path(r.stdout.strip()).resolve()
    except (OSError,subprocess.TimeoutExpired): pass
    return Path(v).expanduser().resolve()

def repos(vals):
    out=[]
    for v in vals or ['.']:
        p=git_root(v)
        if p not in out: out.append(p)
    return out

def discover_skills(rs,a):
    roots=[]
    for r in rs: roots += [r/'skills',r/'.agents'/'skills',r/'.codex'/'skills',r/'.claude'/'skills']
    roots += [Path(x).expanduser().resolve() for x in a.skills_dir]
    if a.include_global_skills: roots += [Path(a.codex_home).expanduser()/'skills',Path.home()/'.agents'/'skills',Path(a.claude_home).expanduser()/'skills']
    found={}
    for root in roots:
        if not root.is_dir(): continue
        for md in sorted(root.glob('*/SKILL.md')):
            if md.parent.name in found: continue
            try: text=md.read_text(encoding='utf-8',errors='replace')
            except OSError: continue
            m=re.search(r'^description:\s*["\']?(.*?)["\']?\s*$',text,re.M)
            found[md.parent.name]={'name':md.parent.name,'path':str(md),'description':(m.group(1) if m else '')[:500]}
    return found

def recent(root,patterns,cutoff):
    out={}; root=Path(root).expanduser()
    if not root.is_dir(): return []
    for pat in patterns:
        for p in root.glob(pat):
            try: ts=datetime.fromtimestamp(p.stat().st_mtime,tz=timezone.utc)
            except OSError: continue
            if ts>=cutoff: out[p]=(ts,p)
    return sorted(out.values(),reverse=True)

def strings(x,limit=20):
    out=[]; stack=[x]
    while stack and len(out)<limit:
        v=stack.pop()
        if isinstance(v,str): out.append(v)
        elif isinstance(v,dict): stack.extend(v.values())
        elif isinstance(v,list): stack.extend(v)
    return out

def record(obj):
    if not isinstance(obj,dict): return None,'',None,None
    payload=obj.get('payload') if isinstance(obj.get('payload'),dict) else {}
    msg=obj.get('message') if isinstance(obj.get('message'),dict) else {}
    role=msg.get('role') or payload.get('role') or obj.get('role') or (obj.get('type') if obj.get('type') in ('user','assistant') else None)
    cwd=obj.get('cwd') or payload.get('cwd'); tool=None; text=''
    content=msg.get('content') if msg else payload.get('content')
    if isinstance(content,list):
        parts=[]
        for b in content:
            if not isinstance(b,dict): continue
            if b.get('type')=='tool_use': tool=str(b.get('name') or 'tool'); parts.append(json.dumps(b.get('input') or {},ensure_ascii=False))
            elif b.get('type') in ('text','tool_result'): parts.extend(strings(b,4))
        text='\n'.join(parts)
    elif isinstance(content,str): text=content
    if not text: text='\n'.join(strings(msg or payload or obj,8))
    typ=str(obj.get('type') or '')
    if not tool and 'tool' in typ.lower(): tool=str(payload.get('name') or obj.get('name') or typ)
    return role,text,tool,cwd

def parse(path,harness,names):
    entries=[]; used=set(); cwd=None; calls=0; repeated=0; seen={}; edited=False
    try: f=path.open(encoding='utf-8',errors='replace')
    except OSError: return None
    with f:
        for line in f:
            try: obj=json.loads(line)
            except Exception: continue
            role,text,tool,rcwd=record(obj); cwd=cwd or rcwd
            if tool:
                calls+=1; key=hashlib.sha1((tool+text).encode('utf-8',errors='ignore')).hexdigest(); seen[key]=seen.get(key,0)+1
                if seen[key]>1: repeated+=1
                if any(k in tool.lower() for k in ('edit','write','patch')): edited=True
                entries.append((f'tool:{tool}',text[:MAX_TOOL]))
            elif role in ('user','assistant') and text.strip(): entries.append((role,text.strip()[:MAX_TEXT]))
            for n in names:
                if f'${n}' in text or f'/{n}' in text or f'skills/{n}' in text.lower(): used.add(n)
            if any(x in text for x in ('*** Begin Patch','apply_patch','edit_file','write_file')): edited=True
            if len(entries)>=MAX_ENTRIES: break
    if not entries: return None
    return {'id':hashlib.sha1(str(path).encode()).hexdigest()[:16],'source':harness,'path':str(path),'cwd':cwd,'skills_used':sorted(used),'has_code_edit_hint':edited,'tool_calls':calls,'repeated_tool_calls':repeated,'entries':entries}

def in_repo(cwd,rs):
    if not cwd: return False
    try: p=Path(cwd).expanduser().resolve()
    except OSError: return False
    for r in rs:
        try: p.relative_to(r); return True
        except ValueError: pass
    return False

def write_transcript(out,s):
    lines=[f"# Session {s['id']}",'',f"- source: {s['source']}",f"- cwd: {s.get('cwd')}",f"- skills_used: {', '.join(s['skills_used']) or 'none'}",f"- tool_calls: {s['tool_calls']}",f"- repeated_tool_calls: {s['repeated_tool_calls']}",f"- has_code_edit_hint: {s['has_code_edit_hint']}",'']
    for role,text in s['entries']: lines += [f'## {role}','',text,'']
    (out/'transcripts'/f"{s['id']}.md").write_text('\n'.join(lines),encoding='utf-8')

def main():
    a=args(); rs=repos(a.repo); out=Path(a.out).expanduser().resolve(); (out/'transcripts').mkdir(parents=True,exist_ok=True)
    skills=discover_skills(rs,a); cutoff=datetime.now(timezone.utc)-timedelta(days=a.days); src=[]
    if a.harness in ('auto','codex'): src += [('codex',p) for _,p in recent(Path(a.codex_home).expanduser(),('sessions/**/rollout-*.jsonl','archived_sessions/**/rollout-*.jsonl'),cutoff)]
    if a.harness in ('auto','claude'):
        pats=['projects/*/*.jsonl'] + (['projects/*/*/subagents/*.jsonl'] if a.include_subagents else [])
        src += [('claude',p) for _,p in recent(Path(a.claude_home).expanduser(),pats,cutoff)]
    parsed=[]
    for h,p in src:
        s=parse(p,h,skills.keys())
        if s and (a.all_conversations or in_repo(s.get('cwd'),rs)): parsed.append(s)
    parsed.sort(key=lambda s: Path(s['path']).stat().st_mtime if Path(s['path']).exists() else 0,reverse=True); sample=parsed[:max(0,a.max_sessions)]
    for s in sample: write_transcript(out,s)
    inv={'harness':a.harness,'repos':[str(r) for r in rs],'window_days':a.days,'sessions_scanned':len(src),'sessions_matched':len(parsed),'sessions_sampled':len(sample),'skills_found':len(skills),'skills':list(skills.values()),'sessions':[{k:v for k,v in s.items() if k!='entries'} for s in sample]}
    (out/'inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2),encoding='utf-8'); print(out)
if __name__=='__main__': main()
