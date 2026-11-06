"""Build the three subject collections from the fully audited era records."""
from pathlib import Path
from collections import Counter,defaultdict
import json

ROOT=Path(__file__).resolve().parents[1]
META={r['id']:r for r in json.loads((ROOT/'data/archive_metadata.json').read_text())}
SUBJECTS=('geometry','algebra','number_theory')

def label(ident):
    y,e,n=ident.split('-')
    return f'{y} AIME'+('' if e=='A' else ' '+e)+f' Problem {int(n)}'
def prose(value):
    if isinstance(value,str):
        if value.startswith('https://') and not any(c.isspace() for c in value):return '[Verified source]('+value+')'
        return value
    if isinstance(value,list):return '; '.join(map(str,value))
    if isinstance(value,dict):return ' '.join(f"**{k.replace('_',' ').capitalize()}:** {prose(v)}" for k,v in value.items())
    return json.dumps(value,ensure_ascii=False)
def write_json(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    records=[];decisions=[]
    for era in ('early','middle','recent'):
        records+=json.loads((ROOT/f'solutions/{era}.json').read_text())
        decisions+=json.loads((ROOT/f'data/{era}_classification.json').read_text())
    assert len(records)==len({r['id'] for r in records})==1065,'Incomplete or duplicate solution inventory'
    assert len(decisions)==len({r['id'] for r in decisions})==1065,'Incomplete or duplicate classification inventory'
    assert {r['id'] for r in records}==set(META)=={r['id'] for r in decisions}
    byid={r['id']:r for r in records};dbyid={d['id']:d for d in decisions}
    for r in records:
        m=META[r['id']];d=dbyid[r['id']]
        assert d['subjects'] and set(d['subjects'])<=set(SUBJECTS)|{'combinatorics'}
        r['subjects']=d['subjects'];r['classification_reason']=d.get('reason',d.get('reason_specific_to_problem',''))
        assert r['classification_reason'],r['id']
        for key in ('title','restatement','solution','answer','tags','verification','status'):assert key in r,(r['id'],key)
        assert r['status']=='solved',r['id']
        assert 0<=int(r['answer'])<=999,r['id']
        if m['answer'] and int(r['answer'])!=int(m['answer']):
            assert r.get('variant_note') or r.get('source_correction'),(r['id'],'unexplained answer difference')
        inds=r.get('source_reviewed_indices',[])
        if r.get('source_index_base',0)==1:inds=[i-1 for i in inds]
        assert sorted(inds)==list(range(m['available_source_solutions'])),(r['id'],'incomplete source-entry review')
        r['source_reviewed_indices']=sorted(inds);r['source_index_base']=0
        r['source_url']=m['source_url'];r['contest_credit']='MAA American Mathematics Competitions'
        r['authorship']='New exposition after consultation of published methods; not claimed to be a blind solution.'
    records.sort(key=lambda r:r['id']);decisions.sort(key=lambda d:d['id'])
    write_json(ROOT/'data/classification.json',decisions)
    write_json(ROOT/'data/all_problems_and_solutions.json',records)
    totals={}
    for subject in SUBJECTS:
        root=ROOT.parent/('aime_'+subject);title=subject.replace('_',' ').title()
        for sub in ('problems','worked_solutions','data','output'):(root/sub).mkdir(exist_ok=True)
        chosen=[r for r in records if subject in r['subjects']]
        problems=[f'# AIME {title} Problem Collection\n',
            'New mathematical restatements of the standard 1983–2026 archive. Contest credit: MAA American Mathematics Competitions. Linked sources supply official wording and diagrams.\n']
        solutions=[f'# AIME {title} Worked Solutions\n',
            'New exposition after source consultation. Each entry records its source review and verification; see the coverage and provenance reports for their precise scope.\n']
        methods=defaultdict(list);sources=[]
        for r in chosen:
            ident=r['id'];m=META[ident];url=r['source_url'];review=prose(r.get('source_review',''))
            q=f"# {label(ident)}: {r['title']}\n\n{r['restatement']}\n\n[Published problem and solutions]({url}) · MAA AMC.\n"
            correction=r.get('source_correction',{})
            answer_label='Reported answer' if isinstance(correction,dict) and correction.get('type')=='literal_statement_inconsistency' else 'Answer'
            sol=q+f"\n## Solution\n\n{r['solution']}\n\n**{answer_label}:** {int(r['answer']):03d}.\n\n**Methods:** {', '.join(r['tags'])}.\n\n**Verification:** {prose(r['verification'])}\n\n**Source comparison:** {review}\n\n**Archived entries inspected:** {len(r['source_reviewed_indices'])} of {m['available_source_solutions']}. Zero-based indices are recorded in the data; linked media are not implicitly claimed reviewed.\n"
            if correction:sol+='\n**Source correction:** '+prose(correction)+'\n'
            if r.get('variant_note'):sol+='\n**Version note:** '+prose(r['variant_note'])+'\n'
            sol+='\n**Subject classification:** '+', '.join(r['subjects'])+'. '+r['classification_reason']+'\n'
            (root/'problems'/f'{ident}.md').write_text(q);(root/'worked_solutions'/f'{ident}.md').write_text(sol)
            problems.append(q.replace('# ','## ',1));solutions.append(sol.replace('# ','## ',1).replace('\n## Solution','\n### Solution'))
            for tag in r['tags']:methods[tag].append(r)
            sources.append({'id':ident,'url':url,'available_entries':m['available_source_solutions'],'reviewed_indices':r['source_reviewed_indices'],'review':review})
        (root/'Problems.md').write_text('\n'.join(problems));(root/'Worked_Solutions.md').write_text('\n'.join(solutions))
        index=[f'# AIME {title} Method Index\n','A problem can appear under several methods and in several subject volumes.\n']
        for tag,rows in sorted(methods.items()):
            index.append('## '+tag+'\n');index += [f"- [{label(r['id'])}: {r['title']}](worked_solutions/{r['id']}.md)" for r in rows];index.append('')
        (root/'Method_Index.md').write_text('\n'.join(index))
        source_md=['# Published source directory\n','Source text was inspected in a temporary research cache and is not bulk-republished here. The links retain access to the published statements and alternatives. Counts describe stored entries, including comments or link-only entries, not necessarily independent complete proofs.\n','| Problem | Stored entries | Entries inspected | Published source |','|---|---:|---:|---|']
        source_md += [f"| {r['id']} | {r['available_entries']} | {len(r['reviewed_indices'])} | [Source]({r['url']}) |" for r in sources]
        (root/'Published_Solution_Sources.md').write_text('\n'.join(source_md)+'\n')
        coverage={'years':[1983,2026],'exam_count':71,'all_slots_classified':1065,'included_problems':len(chosen),'completed_solutions':len(chosen),'unresolved_ids':[],'stored_source_entries':sum(s['available_entries'] for s in sources),'inspected_source_entries':sum(len(s['reviewed_indices']) for s in sources),'by_year':dict(sorted(Counter(r['id'][:4] for r in chosen).items()))}
        write_json(root/'data/problems_and_solutions.json',chosen);write_json(root/'data/source_review.json',sources);write_json(root/'data/coverage.json',coverage)
        write_json(root/'data/classification.json',[dict(d,include=subject in d['subjects']) for d in decisions]);totals[subject]=coverage
    write_json(ROOT/'data/coverage.json',{'unique_problem_slots':1065,'all_source_entries':sum(m['available_source_solutions'] for m in META.values()),'subject_counts':{k:v['included_problems'] for k,v in totals.items()},'hybrid_policy':'Substantive subjects overlap; counts are not intended to sum to1065.'})
    print(json.dumps({k:{'problems':v['included_problems'],'source_entries':v['stored_source_entries']} for k,v in totals.items()},indent=2))

if __name__=='__main__':main()
