"""Assemble the reviewed records into a readable, traceable AIME collection."""
from pathlib import Path
from collections import Counter, defaultdict
import json, re

ROOT=Path(__file__).resolve().parents[1]
META={r['id']:r for r in json.loads((ROOT/'data/archive_metadata.json').read_text())}

def label(ident):
    year,exam,num=ident.split('-')
    return f'{year} AIME'+('' if exam=='A' else ' '+exam)+f' Problem {int(num)}'

def paragraph(value):
    if isinstance(value,list):return '; '.join(map(str,value))
    if isinstance(value,dict):return json.dumps(value,ensure_ascii=False)
    return str(value)

def assemble():
    records=[]; decisions=[]
    for era in ('early','middle','recent'):
        records+=json.loads((ROOT/f'solutions/{era}.json').read_text())
        decisions+=json.loads((ROOT/f'data/{era}_classification.json').read_text())
    records.sort(key=lambda r:r['id']); decisions.sort(key=lambda r:r['id'])
    assert len(decisions)==1065 and len({d['id'] for d in decisions})==1065
    wanted={d['id'] for d in decisions if d['include']}
    assert len(records)==len({r['id'] for r in records})
    assert {r['id'] for r in records}==wanted, sorted(wanted-{r['id'] for r in records})
    for sub in ('problems','worked_solutions'):(ROOT/sub).mkdir(exist_ok=True)
    problems=['# AIME Combinatorics Problem Collection\n',
      'Original mathematical restatements, 1983–2026. Contest credit: MAA American Mathematics Competitions. Refer to the linked source for official wording and diagrams. Answers and worked solutions are in the separate solution collection.\n']
    solutions=['# AIME Combinatorics Worked Solutions\n',
      'New exposition after consultation of published solutions. Source review and verification are recorded for each item; an answer-key comparison is not an independent proof check. See the coverage report for limitations.\n']
    methods=defaultdict(list); sources=[]; unresolved=[]
    for r in records:
        for k in ('id','title','restatement','solution','answer','tags','verification','status'):assert k in r,(r['id'],k)
        assert 0<=int(r['answer'])<=999,(r['id'],r['answer'])
        m=META[r['id']];url=m['source_url'];name=label(r['id'])
        r['source_url']=url;r['contest_credit']='MAA American Mathematics Competitions'
        r['authorship']='Newly written exposition after source consultation; not claimed to be solved blind.'
        reviewed=r.get('source_reviewed_indices',[])
        if r.get('source_index_base',0)==1:reviewed=[i-1 for i in reviewed]
        assert len(set(reviewed))==len(reviewed),(r['id'],'duplicate review index')
        assert all(0 <= i < m['available_source_solutions'] for i in reviewed),(r['id'],'invalid source index')
        r['source_reviewed_indices']=reviewed;r['source_index_base']=0
        if r['status']!='solved':unresolved.append(r['id'])
        question=f"# {name}: {r['title']}\n\n{r['restatement']}\n\n[Published problem and solutions]({url}) · MAA AMC.\n"
        review=paragraph(r.get('source_review','Review scope not recorded.'))
        worked=question+f"\n## Solution\n\n{r['solution']}\n\n**Answer:** {int(r['answer']):03d}.\n\n**Methods:** {', '.join(r['tags'])}.\n\n**Verification:** {paragraph(r['verification'])}\n\n**Source comparison:** {review}\n\n**Archived alternatives reviewed:** {len(reviewed)} of {m['available_source_solutions']}. Indices in the data are zero-based.\n\n**Status:** {r['status']}.\n"
        (ROOT/'problems'/f"{r['id']}.md").write_text(question)
        (ROOT/'worked_solutions'/f"{r['id']}.md").write_text(worked)
        problems.append(question.replace('# ','## ',1))
        solutions.append(worked.replace('# ','## ',1).replace('\n## Solution','\n### Solution'))
        for tag in r['tags']:methods[tag].append(r)
        sources.append({'id':r['id'],'source_url':url,'available_alternatives':m['available_source_solutions'],'reviewed_indices':reviewed,'source_review':review})
    (ROOT/'Problems.md').write_text('\n'.join(problems))
    (ROOT/'Worked_Solutions.md').write_text('\n'.join(solutions))
    (ROOT/'data/problems_and_solutions.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'data/classification.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'data/source_review.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
    index=['# AIME Combinatorics Method Index\n','Problems can occur under several methods. Read the statement before opening its solution.\n']
    for tag,rs in sorted(methods.items()):
        index.append(f'## {tag}\n')
        index.extend(f"- [{label(r['id'])}: {r['title']}](worked_solutions/{r['id']}.md)" for r in rs)
        index.append('')
    (ROOT/'Method_Index.md').write_text('\n'.join(index))
    source_md=['# Published source solution directory\n',
      'These links lead to the published statements and alternative solutions. Community solution text is not republished here. Each contribution retains its source attribution. The original source transcriptions were downloaded to a temporary research cache for review; those raw texts are excluded from this public repository because their redistribution rights were not established.\n',
      '| Problem | Available alternatives in retrieved snapshot | Alternatives read | Published source |',
      '|---|---:|---:|---|']
    for r in sources:source_md.append(f"| {r['id']} | {r['available_alternatives']} | {len(r['reviewed_indices'])} | [Source]({r['source_url']}) |")
    (ROOT/'Published_Solution_Sources.md').write_text('\n'.join(source_md)+'\n')
    report={'years':[1983,2026],'exam_count':71,'all_problem_slots_audited':1065,'included_problems':len(records),'excluded_problems':1065-len(records),'authored_solutions':len(records),'unresolved_ids':unresolved,'available_source_alternatives':sum(s['available_alternatives'] for s in sources),'reviewed_source_alternatives':sum(len(s['reviewed_indices']) for s in sources),'by_year':dict(sorted(Counter(r['id'][:4] for r in records).items())),'status_counts':dict(Counter(r['status'] for r in records))}
    (ROOT/'data/coverage.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':assemble()
