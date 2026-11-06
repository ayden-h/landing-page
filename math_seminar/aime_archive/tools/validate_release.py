"""Audit archive coverage, cross-volume agreement, and local reading links."""
from pathlib import Path
from collections import Counter
import json,re

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
SUBJECTS=('combinatorics','geometry','algebra','number_theory')
records=json.loads((ROOT/'data/all_problems_and_solutions.json').read_text())
assert len(records)==len({r['id'] for r in records})==1065
expected={f'{y}-{e}-{n:02d}' for y in range(1983,2027)
          for e in (['A'] if y<2000 else ['I','II']) for n in range(1,16)}
assert {r['id'] for r in records}==expected
counts={}
for subject in SUBJECTS:
    folder=WORK/('aime_'+subject)
    want={r['id'] for r in records if subject in r['subjects']}
    got={p.stem for p in (folder/'worked_solutions').glob('*.md')}
    assert got==want,(subject,'solution membership',sorted(want-got),sorted(got-want))
    got={p.stem for p in (folder/'problems').glob('*.md')}
    assert got==want,(subject,'problem membership',sorted(want-got),sorted(got-want))
    counts[subject]=len(want)

bad_links=[];bad_chars=[];markdown_count=0
for folder in [ROOT]+[WORK/('aime_'+s) for s in SUBJECTS]:
    for path in folder.rglob('*.md'):
        markdown_count+=1;text=path.read_text()
        controls=sorted({ord(c) for c in text if ord(c)<32 and c not in '\n\t\r'})
        if controls:bad_chars.append([str(path.relative_to(WORK)),controls])
        navigation_text=re.sub(r'\$.*?\$', '', text, flags=re.S)
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)',navigation_text):
            if target.startswith(('http:','https:','mailto:','#','codex:')):continue
            target=target.split('#',1)[0].strip('<>')
            if target and not (path.parent/target).exists():
                bad_links.append([str(path.relative_to(WORK)),target])
assert not bad_chars,bad_chars
assert not bad_links,bad_links
out={'status':'passed','standard_papers':71,'unique_problem_slots':1065,
     'subject_counts':counts,'local_markdown_files_checked':markdown_count,
     'broken_local_links':bad_links,'control_character_errors':bad_chars,
     'scope':'Inventory and navigation audit; not a formal verification of all proofs.'}
(ROOT/'data/release_validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
