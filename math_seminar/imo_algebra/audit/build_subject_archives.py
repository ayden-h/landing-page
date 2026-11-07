"""Reproducible packaging of the three subject research editions.

Raw input is a locally recovered MathNet website snapshot, not an assertion
of complete historical coverage. Missing full records remain catalog pointers.
"""
from pathlib import Path
import ast, collections, csv, hashlib, json, re, shutil

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output'
PREV={r['slug']:r for r in json.loads((ROOT/'research/three_subjects_preview.json').read_text())}
SELECTED=json.loads((ROOT/'research/reviewed_subject_candidates.json').read_text())
SUBJECTS={'Algebra':('algebra','Algebra','A'), 'Geometry':('geometry','Geometry','G'),
          'Number_Theory':('number_theory','Number Theory','N')}
COUNTRIES=['China','United States','Russia','Singapore','Vietnam','South Korea','India','North Korea','United Kingdom','Japan']
tree=ast.parse((OUT/'build_archive.py').read_text())
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='classify')
env={'re':re};exec(compile(ast.Module(body=[fn],type_ignores=[]),'classifier','exec'),env)
classify=env['classify']
ERRATA={
 'imo_2006_e3e5ce':'The negative two-cycle partner is -1-a, not 1-a. Corrected in A03.',
 'imo_2013_d960d1':'The recovered statement omits v_1=1 in one initialization. Supplied explicitly in A06.',
 'imo_2024_5877d2':'The cost-table explanation has row/index slips; the variables are x_0 through x_n. Corrected in A11.',
 'imo_2020_48d762':'The checked A14 proves Version 1 only; an imported Version 2 comparison also repeats the wrong sign label.',
 'imo_2017_e0103e':'A displayed pentagon angle sum has a plus/minus transcription error. Corrected in G09.',
 'imo_2015_d499b1':'Recovered proof omits definitions and preliminary collinearity. Reconstructed in G14.',
 'imo_2013_22bd4a':'One proof is truncated; G05 supplies a complete coordinate argument and intersection branch check.',
 'imo_2006_472d44':'Sampled decimal need not lie strictly between zero and one. Endpoint possibility retained in N02.',
 'imo_2019_199a44':'One imported proof has a malformed square-root bound; N09 uses a separately checked inequality chain.',
 'imo_2019_05dd86':'Zero-polynomial convention would trivialize the closure condition; the substantive nonconstant version is made explicit in N10.',
 'imo_2019_aedde5':'One imported alternate proof reverses a binomial ratio and invokes unnecessary Dirichlet machinery. N11 proves the exact criterion directly.',
 'imo_2024_8acaec':'Attached source solution concerns an unrelated finite-set problem. Its solution text is withheld from this edition; the statement and pointer retain a mismatch warning.'
}

def has_image(s):return bool(re.search(r'!\[|<img|attached_image_|cdn\.mathpix',s or '',re.I))
def normalized(s):
    s=s.replace('\\overarc','\\widehat').replace('✓',r'$\checkmark$')
    s=re.sub(r'\\(?:begin|end)\{equation\*\}\s*\n','',s)
    return s
def years(rows):
    return ', '.join(map(str,sorted({r['year'] for r in rows if r.get('year')}))) or 'None recovered'

summaries={}
for subject,(key,domain,prefix) in SUBJECTS.items():
    P=OUT/(subject+'_Research_Package')
    for d in ['problems','source_solutions','reviewed_problems','reviewed_solutions','audit','figures']:(P/d).mkdir(parents=True,exist_ok=True)
    for suffix in ['Theory','Worked_Solutions']:
        shutil.copy2(OUT/'subject_sources'/f'{subject}_{suffix}.md',P/f'{subject}_{suffix}.md')
    worked=(P/f'{subject}_Worked_Solutions.md').read_text()
    cases=[];checked={}
    for chunk in re.split(r'(?m)(?=^# '+prefix+r'\d\d\.)',worked)[1:]:
        chunk=re.split(r'\n# (?:Source|Attribution)',chunk,1)[0].strip()
        cid=re.match(r'# ('+prefix+r'\d\d)',chunk).group(1)
        source=next(l for l in chunk.splitlines() if l.startswith('**Source:**'))
        slug=re.search(r'\*\*Record:\*\* `([^`]+)`',chunk)
        if slug:checked[slug.group(1)]=cid
        statement=re.search(r'\*\*Problem\.\*\*(.*?)(?=\n\*\*(?:Discovery|Solution))',chunk,re.S).group(1).strip()
        title=chunk.splitlines()[0][2:]
        (P/'reviewed_solutions'/f'{cid}.md').write_text(chunk+'\n')
        (P/'reviewed_problems'/f'{cid}.md').write_text(f'# {title}\n\n{source}\n\n{statement}\n')
        cases.append(dict(id=cid,title=title,source=source,statement=statement,record=slug.group(1) if slug else None))
    assert len(cases)==16,(subject,len(cases))
    rows=[];groups=collections.defaultdict(list);compact=[]
    candidates=[r for r in PREV.values() if domain in r.get('domains',[]) or r['slug'] in SELECTED[key]]
    for pv in sorted(candidates,key=lambda r:r['slug']):
        slug=pv['slug'];rawpath=ROOT/'research/full'/(slug+'.json')
        recovered=rawpath.exists();r=json.loads(rawpath.read_text()) if recovered else dict(pv)
        r.setdefault('competition_code',pv.get('competition_code','UNKNOWN'));r.setdefault('country',pv.get('country','Unknown'))
        code,scope,notes=classify(r)
        notes=[s.replace('a combinatorics tag',f'a {domain.lower()} tag') for s in notes]
        if slug in SELECTED[key] and domain not in pv.get('domains',[]):notes.append('Included in the checked subject core using original shortlist problem classification, despite incomplete domain tags.')
        url=f"https://mathnet.mit.edu/data_v2/full/{pv['source_slug']}/{slug}.json.gz"
        permitted=recovered and not r.get('booklet_copyright_holder') and not r.get('booklet_license')
        rights=('MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata' if permitted else
                'Source pointer only: explicit original-rights assertion retained' if recovered else
                'Full record not recovered; rights not established; catalog pointer only')
        st=r.get('problem_markdown') or ''
        sha=hashlib.sha256(re.sub(r'\s+',' ',st).strip().encode()).hexdigest() if recovered else None
        if sha:groups[sha].append(slug)
        meta={k:v for k,v in r.items() if k not in ['problem_markdown','solutions_markdown','answers_markdown','problem_preview_markdown']}
        meta.update(source_url=url,source_slug=pv['source_slug'],full_record_recovered=recovered,
                    corrected_competition_code=code,scope_status=scope,classification_notes=notes,rights_status=rights,
                    statement_hash_whitespace_normalized=sha,source_solution_count=len(r.get('solutions_markdown',[])) if recovered else pv.get('solution_count'),
                    reviewed_solution_id=checked.get(slug),erratum=ERRATA.get(slug),statement_included=False,
                    problem_file=None,source_solution_file=None,included_source_solution_count=0,
                    statement_figure_dependent=has_image(st) if recovered else None)
        label=f"{code} | {r.get('country')} | {r.get('year') or 'year unknown'} | {r.get('section') or ''} | {r.get('problem_number') or ''}"
        attr='\n'.join(f'- {k[8:].replace("_"," ").title()}: {v}' for k,v in r.items() if k.startswith('booklet_') and v)
        header=f'# {slug}\n\n{label}\n\n**Scope:** {scope}. **Review:** source text not independently verified.\n\n**Source:** [{slug}]({url})\n\n**Rights:** {rights}.\n\n'+attr+'\n\n'
        if meta['erratum']:header+='**Known source issue:** '+meta['erratum']+'\n\n'
        if permitted and st and not has_image(st) and scope!='quarantine':
            path=f'problems/{slug}.md';(P/path).write_text(header+'## Problem\n\n'+st+'\n')
            meta.update(statement_included=True,problem_file=path)
        elif not recovered:notes.append('Full source request unavailable in this run; preview metadata alone does not establish a complete statement.')
        else:
            if not permitted:notes.append('Raw source prose withheld because original rights take precedence over fallback license.')
            if has_image(st):notes.append('External statement figures detected; retained as pointer to avoid incomplete reproduction.')
        sols=[]
        if permitted and scope!='quarantine' and slug!='imo_2024_8acaec':
            sols=[(i,s) for i,s in enumerate(r.get('solutions_markdown',[]),1) if s.strip() and not has_image(s)]
        if sols:
            path=f'source_solutions/{slug}.md'
            body=header+'**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**\n\n'
            if slug in checked:body+=f'Checked rewritten solution: [${checked[slug]}](../reviewed_solutions/{checked[slug]}.md).\n\n'.replace('[$','[')
            body+='\n\n'.join(f'## Supplied solution {i}\n\n{s}' for i,s in sols)+'\n'
            (P/path).write_text(body);meta.update(source_solution_file=path,included_source_solution_count=len(sols))
        rows.append(meta)
    for r in rows:r['exact_statement_duplicates']=[x for x in groups.get(r['statement_hash_whitespace_normalized'],[]) if x!=r['slug']]
    stats=dict(subject=domain,candidate_records=len(rows),full_records_recovered=sum(r['full_record_recovered'] for r in rows),
               unrecovered_full_records=sum(not r['full_record_recovered'] for r in rows),
               source_problem_files=sum(r['statement_included'] for r in rows),source_solution_files=sum(bool(r['source_solution_file']) for r in rows),
               source_solution_texts=sum(r['included_source_solution_count'] for r in rows),reviewed_cases=16,
               additional_reviewed_official_cases=sum(c['record'] is None for c in cases),
               scope_counts=dict(collections.Counter(r['scope_status'] for r in rows)),
               all_history_complete=False,all_solutions_independently_checked=False,
               target_window='1927–2026; recovered coverage is partial',snapshot='312a167f6df5')
    summaries[subject]=stats
    (P/'audit/counts.json').write_text(json.dumps(stats,indent=2))
    (P/'audit/reviewed_cases.json').write_text(json.dumps(cases,indent=2,ensure_ascii=False))
    (P/'audit/source_ledger.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    (P/'audit/duplicate_groups.json').write_text(json.dumps([v for v in groups.values() if len(v)>1],indent=2))
    fields=['slug','corrected_competition_code','country','year','section','problem_number','scope_status','full_record_recovered','statement_included','source_solution_count','included_source_solution_count','reviewed_solution_id','source_url','rights_status']
    with (P/'Catalog.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    report=f'''# {domain}: coverage and provenance

Research edition, 6 November 2026. **This is a partial research archive, not a complete century-wide collection or a claim that every imported problem has been independently solved.**

## Exact counts

- {stats['candidate_records']:,} candidate catalog records; subject tags overlap across volumes.
- {stats['full_records_recovered']:,} full source records recovered; {stats['unrecovered_full_records']:,} remain metadata and source pointers.
- {stats['source_problem_files']:,} full source statement files after rights, scope and external-figure filters.
- {stats['source_solution_files']:,} files containing {stats['source_solution_texts']:,} source-supplied solution texts, explicitly not independently reviewed.
- 16 checked, rewritten case studies, each with a separate problem and solution file; {stats['additional_reviewed_official_cases']} additional official-paper cases outside the retrieved candidate catalog.
- A proved theory manuscript and a solved transfer workshop.

Counts are records, not certified unique historical problems. Whitespace-only exact duplicates are identified in the ledger; translations and semantic duplicates remain. A recovered year means at least one candidate was found, not that the whole paper or subject set is complete.

## Scope convention

The target is calendar years 1927–2026 through the research date. There is no authoritative objective ranking of the ten hardest competitions. For consistency with the combinatorics edition, the editorial set is IMO, RMM, CMO-China, USAMO, ARMO, IranMO, VMO, APMO, Balkan MO and EGMO. The recent-year country convention is China, United States, Russia, Singapore, Vietnam, South Korea, India, North Korea, United Kingdom and Japan, following the 2026 IMO team order cited in the original edition: https://www.imo-official.org/results/team/year/2026/ . This is not an all-time country ranking or a ranking of individual problems.

National contests, camps, shortlists, final selection rounds and actual IMO papers remain distinct in the catalog. Inconsistent normalized contest labels are corrected where the original section identifies the round; unresolved contradictions are quarantined. Domain tags are retrieval aids and may be incomplete or wrong. Mixed-domain problems appear in more than one subject package.

## Candidate years by family

| Family | Candidates | Years with at least one candidate |
|:--|--:|:--|
'''
    for code in ['IMO','IMO-SL','RMM','CMO-China','USAMO','ARMO','IranMO','VMO','APMO','BMO','BMO-SL','EGMO']:
        rs=[r for r in rows if r['corrected_competition_code']==code];report+=f'| {code} | {len(rs)} | {years(rs)} |\n'
    report+='\n## Selection coverage\n\n| Country | Explicit selection candidates | Pipeline supplements | Selection years |\n|:--|--:|--:|:--|\n'
    for c in COUNTRIES:
        rs=[r for r in rows if r.get('country')==c and r['scope_status']=='selection'];ps=sum(r.get('country')==c and r['scope_status']=='pipeline_supplement' for r in rows)
        report+=f'| {c} | {len(rs)} | {ps} | {years(rs)} |\n'
    report+='''
## Gaps and limits

The century-wide per-round inventory is unfinished. Early decades, unpublished selection rounds, many national archives, external statement figures and some full source records are absent. A blank year is not labeled “not held” without a verified contest calendar. Most recovered website material is from 1983–2025; selected official-paper cases do not make that range exhaustive. The most recent 2026 papers have not been systematically added to these three subject archives.

The checked core is 16 cases, not every source solution. The theory derives from that core and classical tools, not an all-record review. Several source proofs are incomplete or erroneous; detected defects are listed in audit/Errata.md. The 2024 N2 record with an unrelated attached solution is retained as a statement/pointer but its mismatched solution is withheld. There is no claim of external peer review or research novelty.

## Attribution and reproduction

The source is MathNet website snapshot 312a167f6df5, built 29 April 2026. MathNet's dataset description supplies a CC BY 4.0 fallback where no explicit original rights are asserted and gives original assertions precedence. This edition conservatively withholds raw prose when an explicit holder or license field is present, or when full metadata was not recovered. External figure dependencies are not silently presented as complete text. The source ledger and individual files retain booklet authors, editors, organization, language and rights fields where supplied. Missing metadata is not an independent legal investigation.

Source texts are grouped and typeset; only logged TeX compatibility changes are made to the printable collection. Checked statements and proofs are separately rewritten with necessary corrections. Imported source solutions retain their unreviewed label, including known defects when preserved for audit.

MathNet citation: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. Original contest organizations and source contributors remain credited in each record.

Sources: https://mathnet.mit.edu/ ; https://huggingface.co/datasets/ShadenA/MathNet ; https://creativecommons.org/licenses/by/4.0/ ; https://www.imo-official.org/problems/ ; https://rmms.lbi.ro/ ; https://www.apmo-official.org/problems ; https://www.egmo.org/ ; https://github.com/usa-tst-public/USA-TST-Archive ; https://bmos.ukmt.org.uk/home/selection-tests.shtml .

## Status against the requested project

| Request | Status in this research edition |
|:--|:--|
| Gather all historical problems | Partial catalog and source collection; missing years and rounds documented |
| Solve every problem | Sixteen complete checked expositions; larger source-supplied solution archive is unreviewed |
| Derive definitions and theorems | Proved toolkit and extensions from the checked core and classical mathematics |
| Write an advanced preparation book | Theory, worked solutions, solved exercises and seminar program completed for this edition |
'''
    (P/'Coverage_Report.md').write_text(report)
    err='# Known source defects and classification repairs\n\nThis is a list of detected examples, not an exhaustive audit.\n\n'
    for r in rows:
        if r['erratum']:err+=f"- `{r['slug']}`: {r['erratum']}\n"
        if r['competition_code']!=r['corrected_competition_code'] or r['scope_status']=='quarantine':err+=f"- `{r['slug']}`: {r['competition_code']} → {r['corrected_competition_code']}; "+' '.join(r['classification_notes'])+'\n'
    (P/'audit/Errata.md').write_text(err)
    allraw='# Collected source problems\n\nPartial source-attributed archive. See Coverage_Report.md for status and rights.\n\n'
    for r in rows:
        if r['statement_included']:allraw+=(P/r['problem_file']).read_text()+'\n---\n\n'
    (P/'Collected_Source_Problems.md').write_text(allraw)
    book=f'''---
title: "Olympiad {domain}: Collected Problems"
author: "Ayden Bi"
date: "Research edition • 6 November 2026"
lang: en-US
---

# Scope and attribution {{.unnumbered}}

This volume contains sixteen restated problems from the checked core, followed by {stats['source_problem_files']:,} source-provided statements. It is a partial collection. Source classifications, numbering and transcriptions are not all independently verified. Mixed-domain records may occur in other subject volumes. The corresponding proofs are in the separate worked volume and the individually labeled source-solution files.

The source statements are reproduced under MathNet's CC BY 4.0 fallback where recovered metadata contains no explicit original rights assertion. The complete package preserves original booklet credits and metadata. Figure-dependent statements and records with uncertain or explicit original rights remain source pointers. Original source wording is retained apart from logged typesetting compatibility repairs. The checked core is separately restated and corrected.

MathNet: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. Sources: https://mathnet.mit.edu/ ; https://huggingface.co/datasets/ShadenA/MathNet ; https://creativecommons.org/licenses/by/4.0/ . Original source contributors are credited in the ledger and individual problem files.

Read Coverage_Report.md for exact counts, historical gaps, withheld records and the distinction between actual contests, shortlists and selection material. The author credit identifies this compiled edition and its authored expositions, not authorship of the historical problems.

# The sixteen checked-core problems

'''
    for c in cases:book+=f"## {c['title']}\n\n{c['source']}\n\n{c['statement']}\n\n"
    changes=[]
    for code in sorted({r['corrected_competition_code'] for r in rows if r['statement_included']}):
        book+='\n# '+code+' source statements\n\n'
        for r in sorted([r for r in rows if r['statement_included'] and r['corrected_competition_code']==code],key=lambda r:(r.get('year') or 0,r['slug'])):
            st=(P/r['problem_file']).read_text().split('## Problem\n\n',1)[1];ns=normalized(st)
            if ns!=st:changes.append({'slug':r['slug'],'changes':'Removed nested equation-star wrappers, normalized overarc or checkmark. Raw source preserved separately.'})
            book+=f"## {r.get('year') or 'Year unknown'} — {r.get('problem_number') or 'Number unknown'}\n\n**Record:** `{r['slug']}`. **Category:** {r['scope_status'].replace('_',' ')}. [Source]({r['source_url']}).\n\n"
            if r['erratum']:book+='**Source issue:** '+r['erratum']+'\n\n'
            book+=ns+'\n\n'
    (P/f'{subject}_Collected_Problems.md').write_text(book)
    (P/'audit/Typesetting_Changes.json').write_text(json.dumps(changes,indent=2))
    readme=f'''# IMO {domain} research edition

**Author of the theory book and rewritten expositions: Ayden Bi.** Historical problems and source-supplied solutions retain their original attribution.

- [{domain} theory]({subject}_Theory.pdf): definitions, proved tools, extensions, solved transfer exercises and a seminar program.
- [Worked solutions]({subject}_Worked_Solutions.pdf): 16 checked, rewritten case studies.
- [Collected problems]({subject}_Collected_Problems.pdf): the core plus {stats['source_problem_files']:,} source statements.
- [Coverage report](Coverage_Report.md): exact counts and unfinished historical coverage.
- [Catalog](Catalog.csv): {stats['candidate_records']:,} candidates, including missing-source and index-only records.

The source archive has {stats['source_solution_files']:,} solution files containing {stats['source_solution_texts']:,} supplied texts. **These are not independently reviewed** unless an explicit case number links to a separate rewritten proof. This edition does not claim all historical problems or all solutions are complete. Difficulty is an editorial selection, not an objective ranking.

## Files

`reviewed_problems/` and `reviewed_solutions/` contain the sixteen paired core files. `problems/` and `source_solutions/` contain attributed source material after scope, rights and figure filters. `audit/` contains the full provenance ledger, detected errors, counts, exact duplicate groups and verification material. Editable Markdown accompanies every PDF. SHA256SUMS.txt records checksums.

The MathNet fallback license applies to eligible imported source text as described in the coverage report; original rights assertions take precedence. Original booklet credits are retained. No authorship of historical problems is implied by the book author credit.
'''
    (P/'README.md').write_text(readme)
    shutil.copy2(__file__,P/'audit/build_subject_archives.py')
    print(subject,json.dumps(stats),flush=True)
(OUT/'three_subjects_counts.json').write_text(json.dumps(summaries,indent=2))
