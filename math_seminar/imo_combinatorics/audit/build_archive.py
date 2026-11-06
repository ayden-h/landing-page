"""Build a transparent, source-attributed research archive from recovered records."""
from pathlib import Path
import json,re,hashlib,collections,csv,shutil

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output';PKG=OUT/'Combinatorics_Research_Package'
for sub in ['problems','source_solutions','reviewed_solutions','reviewed_problems','audit']:(PKG/sub).mkdir(parents=True,exist_ok=True)
previews={r['slug']:r for r in json.loads((ROOT/'research/selection_preview.json').read_text())}
raw=[json.loads(p.read_text()) for p in sorted((ROOT/'research/full').glob('*.json'))]

worked=(OUT/'Worked_Solutions.md').read_text()+'\n'+(OUT/'Worked_Part2.md').read_text()+'\n'+(OUT/'Worked_Part3.md').read_text()
theory=(OUT/'Combinatorics_Theory.md').read_text()+'\n'+(OUT/'Theory_Part2.md').read_text()+'\n'+(OUT/'Theory_Part3.md').read_text()
(PKG/'Worked_Solutions.md').write_text(worked)
(PKG/'Combinatorics_Theory.md').write_text(theory)

cases=[];slug_to_w={}
for chunk in re.split(r'(?m)(?=^# W\d\d\.)',worked)[1:]:
    chunk=chunk.split('\n# Verification and reading notes')[0].strip()
    wid=re.search(r'^# (W\d\d)',chunk).group(1)
    title=chunk.splitlines()[0][2:]
    slug=re.search(r'\*\*Record:\*\* `([^`]+)`',chunk)
    if slug:slug_to_w[slug.group(1)]=wid
    statement=re.search(r'\*\*Problem\.\*\*(.*?)(?=\n\*\*(?:Answer|Hint|Solution|Lower bound))',chunk,re.S).group(1).strip()
    source=next(line for line in chunk.splitlines() if line.startswith('**Source:**'))
    ptext='# '+title+'\n\n'+source+'\n\n'+statement+'\n'
    (PKG/'reviewed_solutions'/f'{wid}.md').write_text(chunk+'\n')
    (PKG/'reviewed_problems'/f'{wid}.md').write_text(ptext)
    cases.append({'id':wid,'title':title,'source':source,'statement':statement,'record':slug.group(1) if slug else None})
assert len(cases)==26

known_errata={
 'apm_1989_ab9780':'Source solution has a reversed inequality in the common-neighbor/degree count. Use W03.',
 'chn_2006_c22bc5':'Source inequality direction in the averaging argument requires correction. Use W13.',
 'kor_2010_1dc4be':'Source weight formula has an exponent/reciprocal transcription defect. Use W22.',
 'mkd_2018_3ac94a':'The exposition of turn parity needs care; unequal even minimum valuations can draw. Use W23.',
 'rou_2016_9aa109':'The four-tile pinwheel occupies a (k+1)-by-(k+1) region, not k-by-k. Use W24.'
}

def classify(r):
    code=r['competition_code'];country=r['country'];sec=r.get('section') or '';cr=r.get('competition_raw') or '';pn=r.get('problem_number') or ''
    notes=[];scope='contest';corrected=code
    if code=='IMO':
        if country=='IMO' and (re.search(r'\b[ACGN]\d',pn) or 'Shortlist' in (r.get('booklet_title') or '')):
            corrected='IMO-SL';scope='shortlist';notes.append('Corrected IMO to shortlist using original problem code/booklet title.')
        elif country=='North Macedonia' or 'Arhimede' in cr or country=='Saudi Arabia':
            corrected='OUT-OF-SCOPE';scope='quarantine';notes.append('Source normalized code IMO contradicts original national/training/other-contest metadata.')
        elif country=='Mongolia':
            corrected='UNRESOLVED';scope='quarantine';notes.append('Booklet year/round/IMO attribution unresolved; not counted as a verified IMO problem.')
        elif country=='United States' and ('USAMO' in sec or 'Team Selection' in sec):
            corrected='USAMO' if 'USAMO' in sec else 'IMO-TST';scope='contest' if corrected=='USAMO' else 'selection';notes.append('Reclassified from booklet-level IMO label using explicit section.')
        elif country=='Vietnam':
            corrected='IMO-TST' if 'Selection' in sec else 'VMO';scope='selection' if corrected=='IMO-TST' else 'contest';notes.append('Reclassified from booklet-level IMO label using explicit section.')
        else:notes.append('IMO attribution is source-reported; original paper comparison remains incomplete.')
    if corrected in ['IMO-SL','BMO-SL']:scope='shortlist'
    if corrected=='BMO' and re.search(r'\b[ACGN]\s?\d',pn):
        corrected='BMO-SL';scope='shortlist';notes.append('Letter-number problem code indicates a shortlist candidate.')
    if corrected in ['IMO-TST','China-TST']:scope='selection'
    if corrected in ['JMO','KMO','IMOTC']:
        scope='pipeline_supplement';notes.append('National contest or camp; not a verified final IMO team-selection round.')
    if corrected=='EGMO-TST':
        scope='quarantine';notes.append('EGMO selection is outside the requested IMO-selection scope.')
    if r.get('year') is None:notes.append('Year is unknown; do not infer one from the slug.')
    if len(r.get('domains',[]))>1:notes.append('Mixed-domain candidate; inclusion follows a combinatorics tag, not exclusive classification.')
    return corrected,scope,notes

def has_image(s):return bool(re.search(r'!\[|<img|attached_image_|cdn\.mathpix',s or '',re.I))
records=[];source_solution_files=0;source_solution_texts=0;problem_files=0
hashgroups=collections.defaultdict(list)
for r in raw:
    slug=r['slug'];pv=previews[slug];source_slug=pv['source_slug']
    code,scope,notes=classify(r)
    url=f'https://mathnet.mit.edu/data_v2/full/{source_slug}/{slug}.json.gz'
    holder=r.get('booklet_copyright_holder');license_text=r.get('booklet_license')
    permitted=not holder and not license_text
    copyright_status='MathNet CC BY 4.0 fallback; no explicit assertion in recovered metadata' if permitted else 'Source pointer only: explicit original-rights assertion retained'
    st=r.get('problem_markdown') or ''
    sha=hashlib.sha256(re.sub(r'\s+',' ',st).strip().encode()).hexdigest()
    hashgroups[sha].append(slug)
    meta={k:v for k,v in r.items() if k not in ['problem_markdown','solutions_markdown','answers_markdown']}
    meta.update({'source_url':url,'source_slug':source_slug,'corrected_competition_code':code,'scope_status':scope,'classification_notes':notes,'rights_status':copyright_status,'statement_hash_whitespace_normalized':sha,'source_solution_count':len(r.get('solutions_markdown',[])),'reviewed_solution_id':slug_to_w.get(slug),'erratum':known_errata.get(slug),'statement_included':False,'source_solution_file':None,'included_source_solution_count':0,'statement_figure_dependent':has_image(st)})
    label=f"{code} | {r.get('country')} | {r.get('year') or 'year unknown'} | {r.get('section') or ''} | {r.get('problem_number') or ''}"
    attr='\n'.join(f'- {key[8:].replace("_"," ").title()}: {value}' for key,value in meta.items() if key.startswith('booklet_') and value)
    header=f'# {slug}\n\n{label}\n\n**Scope:** {scope}. **Review:** source text not independently verified.\n\n**Source:** [{slug}]({url})\n\n**Rights:** {copyright_status}.\n\n'+attr+'\n\n'
    if permitted and not has_image(st) and scope!='quarantine':
        filename=f'problems/{slug}.md';(PKG/filename).write_text(header+'## Problem\n\n'+st+'\n')
        meta['statement_included']=True;meta['problem_file']=filename;problem_files+=1
    else:
        meta['problem_file']=None
        if not permitted:notes.append('Full source text withheld because the dataset defers to an explicit rights assertion.')
        if has_image(st):notes.append('Statement has external figure dependencies; source pointer retained rather than an incomplete transcription.')
    goodsol=[]
    if permitted and scope!='quarantine':
        for i,s in enumerate(r.get('solutions_markdown',[]),1):
            if not has_image(s):goodsol.append((i,s))
    if goodsol:
        filename=f'source_solutions/{slug}.md'
        content=header+'**SOURCE-SUPPLIED, NOT INDEPENDENTLY REVIEWED.**\n\n'
        if slug in known_errata:content+='**KNOWN DEFECT:** '+known_errata[slug]+'\n\n'
        if slug in slug_to_w:content+=f'For the checked rewritten exposition, see `../reviewed_solutions/{slug_to_w[slug]}.md`.\n\n'
        for i,s in goodsol:content+=f'## Supplied solution {i}\n\n{s}\n\n'
        omitted=len(r.get('solutions_markdown',[]))-len(goodsol)
        if omitted:content+=f'{omitted} additional supplied solution(s) require external figures; use the source link.\n'
        (PKG/filename).write_text(content);meta['source_solution_file']=filename;meta['included_source_solution_count']=len(goodsol)
        source_solution_files+=1;source_solution_texts+=len(goodsol)
    records.append(meta)

duplicate_groups=[v for v in hashgroups.values() if len(v)>1]
for r in records:r['exact_statement_duplicates']=[x for x in hashgroups[r['statement_hash_whitespace_normalized']] if x!=r['slug']]
(PKG/'audit/source_ledger.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
(PKG/'audit/reviewed_cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2))
(PKG/'audit/duplicate_groups.json').write_text(json.dumps(duplicate_groups,indent=2))
stats={'retrieved_candidate_records':len(records),'normalized_exact_statement_groups':len(hashgroups),'duplicate_groups':len(duplicate_groups),'scope_counts':dict(collections.Counter(r['scope_status'] for r in records)),'source_problem_files':problem_files,'source_solution_files':source_solution_files,'source_solution_texts':source_solution_texts,'records_with_supplied_solutions_before_rights_figure_scope_filters':sum(r['source_solution_count']>0 for r in records),'reviewed_cases':26,'additional_official_2026_case':1,'all_history_complete':False,'all_solutions_independently_checked':False}
(PKG/'audit/counts.json').write_text(json.dumps(stats,indent=2))

fields=['slug','corrected_competition_code','country','year','section','problem_number','scope_status','statement_included','source_solution_count','included_source_solution_count','reviewed_solution_id','source_url','rights_status']
with (PKG/'Catalog.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(records)

def year_text(rs):
    ys=sorted(set(r['year'] for r in rs if r.get('year')))
    return ', '.join(map(str,ys)) if ys else 'No recovered records'
counts=collections.Counter(r['corrected_competition_code'] for r in records)
report=f'''# Coverage, provenance, and unfinished work

Research edition: 5 November 2026. **This is not a complete century-wide collection, and not every imported solution has been independently solved or checked.**

## Exact deliverable counts

- {len(records):,} retrieved MathNet candidate records, plus one additional official 2026 problem in the reviewed set.
- {len(hashgroups):,} distinct statement groups after whitespace-only exact normalization. Translation and semantic duplicates remain; this is not a unique-problem count.
- {problem_files:,} source statement files included after scope, rights and figure filters.
- {source_solution_files:,} files containing {source_solution_texts:,} source-supplied solution texts. These are **not independently reviewed** except where an explicit W-number points to the separate rewritten proof.
- 26 reviewed, rewritten case studies, each in its own problem and solution file; 25 correspond to retrieved records and W01 is additional.
- 20 transfer exercises with solutions in the theory book.

Candidate scope categories: {', '.join(f'{k}: {v}' for k,v in stats['scope_counts'].items())}.

## Definition of the target

The requested century is treated as calendar years 1927–2026, through the research date. A competition's years before it existed are not missing papers. However, an authoritative founding/cancellation calendar was not reconstructed for every selected competition, so this edition does not label every blank year “not held.” No authoritative ranking of the ten hardest competitions exists. The editorial contest set is IMO, RMM, CMO-China, USAMO, ARMO, IranMO, VMO, APMO, Balkan MO and EGMO. Difficulty was not measured problem by problem.

The country set follows the official 2026 team order: China, United States, Russia, Singapore, Vietnam, South Korea, India, North Korea, United Kingdom and Japan. This is a transparent recent-year convention, not an all-time top-ten ranking. Source: https://www.imo-official.org/results/team/year/2026/ .

National contests, camps, shortlists, team-selection exams and the actual international paper are different objects. The ledger preserves the source label, a corrected label where a contradiction could be resolved, and a scope status. It never treats the number of downloaded rows as certified historical coverage.

## Recovered years by contest family

Counts below are candidate records, not unique verified problems. A listed year indicates at least one recovered candidate, not a complete paper or complete combinatorics set. W01 (IMO 2026) is additional to this table.

| Family | Candidate records | Years with at least one recovered record |
|:--|--:|:--|
'''
for code in ['IMO','RMM','CMO-China','USAMO','ARMO','IranMO','VMO','APMO','BMO','EGMO','IMO-SL','BMO-SL']:
    rs=[r for r in records if r['corrected_competition_code']==code]
    report+=f'| {code} | {len(rs)} | {year_text(rs)} |\n'
report+='''
## Recovered national selection coverage

Only records explicitly classified as selection are counted in the second column. Pipeline supplements are separately counted and do not fill a final-selection gap.

| Country | Selection candidates | Pipeline supplements | Recovered selection years |
|:--|--:|--:|:--|
'''
for country in ['China','United States','Russia','Singapore','Vietnam','South Korea','India','North Korea','United Kingdom','Japan']:
    rs=[r for r in records if r['country']==country and r['scope_status']=='selection']
    supplement=sum(r['country']==country and r['scope_status']=='pipeline_supplement' for r in records)
    report+=f'| {country} | {len(rs)} | {supplement} | {year_text(rs)} |\n'
report+='''
## What is still missing

1. An authoritative per-year, per-round inventory for all ten competitions and all ten countries, including founding years, cancellations and unpublished selection tests.
2. Most early historical material: the downloaded candidates range from 1983 to 2025; the reviewed set adds 2026. This does not cover 1927–1982, nor every year after 1983.
3. Complete final-selection archives for Russia, South Korea, North Korea, the United Kingdom and Japan; only some national pipeline material or source pointers were recovered for several of them. Singapore coverage is very small.
4. Original-paper verification of every contest/year/problem attribution. Several source normalized codes were plainly wrong and have been corrected or quarantined.
5. Semantic deduplication across translations and reused selection problems. The UK archive expressly notes reuse, making this essential.
6. Independent solutions to every included problem, and independent review of every supplied solution. The verified-exposition set is W01–W26 only.
7. Restoration of external figures and any necessary permissions for source-text reproduction. Index-only records are not complete problem statements.
8. A theory synthesis based on the entire eventual corpus. This book derives its case-based synthesis from 26 reviewed problems and classical results, not all 1,116 downloaded records.

## Provenance and reproduction policy

The principal retrieval source is MathNet's website snapshot `312a167f6df5`, built 29 April 2026. Website and Hugging Face snapshots have different record counts and metadata schemas; they were not assumed interchangeable. The recovered website records preserve source booklets, authors, organization, language, rights fields, original competition strings and problem numbers where provided.

MathNet releases records under CC BY 4.0 where no explicit original rights are asserted, and says original rights assertions take precedence. This package conservatively withholds raw statements and raw solutions whenever the recovered record contains an explicit holder or license restriction. Such records retain bibliographic metadata and a source link. A missing rights field is not an independent legal investigation; the inclusion policy relies on MathNet's stated fallback license. Our restatements and rewritten mathematical expositions do not reproduce the withheld source prose.

Records requiring external images are not silently presented as complete. Figure-dependent source solutions are omitted while other self-contained solutions may be included. English translation was not performed across the whole corpus; source languages are retained.

All source-supplied proofs retain their status. Source OCR and model-assisted extraction can contain incorrect signs, formulas, numbering, translations and attributions. The audit's known errata are examples, not a warranty that no other errors remain. Another public IMO dataset was excluded after an algebraically false supplied argument was found; its proofs were not imported.

## Source register

- MathNet project and paper: https://mathnet.mit.edu/
- MathNet dataset and license statement: https://huggingface.co/datasets/ShadenA/MathNet
- CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
- Official IMO papers: https://www.imo-official.org/problems/
- Official 2026 IMO paper: https://www.imo-official.org/assets/documents/problems/2026/2026_eng.pdf
- RMM organizer archive, example year: https://rmms.lbi.ro/rmm2024/index.php?id=problems_math
- RMM historical links: https://bmos.ukmt.org.uk/home/rmm.shtml
- APMO official archive: https://www.apmo-official.org/problems
- EGMO official archive: https://www.egmo.org/
- USA TST archive: https://github.com/usa-tst-public/USA-TST-Archive
- UK selection tests: https://bmos.ukmt.org.uk/home/selection-tests.shtml

MathNet citation: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, *MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval*, ICLR 2026. Original contest organizations and source authors remain credited in each record where the dataset supplies them.

## Completion status against the four requested tasks

| Task | Status in this edition |
|:--|:--|
| Gather all historical combinatorics problems | Partial research archive; substantial missing years, rounds and figure/rights gaps |
| Solve all problems | 26 checked rewritten solutions; additional supplied solutions retained without independent verification |
| Read all solutions and derive theories | Synthesis from the reviewed set and classical theory; not an all-record review |
| Write a rigorous preparation book | Completed research-edition manuscript with proved tools, worked-case links and solved exercises; not a claim of encyclopedic completeness or external peer review |
'''
(PKG/'Coverage_Report.md').write_text(report)

errata='# Known source defects and classification repairs\n\nThese are detected examples, not an exhaustive audit.\n\n'
for s,e in known_errata.items():errata+=f'- **{s}:** {e}\n'
errata+='\n## Metadata repairs and quarantines\n\n'
for r in records:
    if r['competition_code']!=r['corrected_competition_code'] or r['scope_status']=='quarantine':
        errata+=f"- `{r['slug']}`: {r['competition_code']} → {r['corrected_competition_code']}; {r['scope_status']}. "+' '.join(r['classification_notes'])+'\n'
(PKG/'audit/Errata.md').write_text(errata)

allproblems='# Collected source problems\n\n'+f'{problem_files} source statements. This is a partial, source-attributed collection; consult Coverage_Report.md. Source classifications and text are not independently verified. Known scope mismatches and external-figure dependencies are excluded from this full-text file. Index-only records remain in Catalog.csv.\n\n'
for r in sorted(records,key=lambda r:(r['corrected_competition_code'],r.get('year') or 0,r['slug'])):
    if r['statement_included']:
        allproblems+='\n---\n\n'+(PKG/r['problem_file']).read_text()
(PKG/'Collected_Source_Problems.md').write_text(allproblems)

problembook='''---
title: "Olympiad Combinatorics: Problems and Archive Guide"
subtitle: "26 reviewed case-study problems, coverage report, and complete candidate index"
author: "Prepared for haohao"
date: "Research edition • 5 November 2026"
lang: en-US
---

# How to use this file {.unnumbered}

The first part gives the 26 reviewed case-study problems without hints or answers. Their solutions are in the separate worked-solutions volume. The second part reports the actual archive coverage. The final part indexes every retrieved candidate.

The full text of the included source problems is in the separate `Collected_Problems.pdf` and in `Collected_Source_Problems.md` in the companion ZIP, with one file per problem in `problems/`. Index-only records are not complete problem statements. Imported source solutions are separate from the reviewed solutions.

This is a partial research collection, not the complete historical corpus requested. The coverage report identifies the missing work explicitly.

'''
for c in cases:problembook+='\n# '+c['title']+'\n\n'+c['source']+'\n\n'+c['statement']+'\n'
problembook+='\n\\newpage\n\n'+report+'\n\\newpage\n\n# Candidate index {.unnumbered}\n\nEach entry is a source record, not necessarily a unique or correctly attributed historical problem. The CSV and JSON ledger contain full metadata, source links and classifications. “Text” means a statement file is included; “pointer” means use the ledger source link. “S” counts supplied source solutions included in this package, not checked proofs.\n\n'
for code in sorted(set(r['corrected_competition_code'] for r in records)):
    problembook+='\n## '+code+'\n\n'
    for r in sorted([x for x in records if x['corrected_competition_code']==code],key=lambda r:(r.get('year') or 0,r['slug'])):
        # Keep the printable index compact and Latin-script; full original names remain in the ledger.
        pnum=re.sub(r'[^\x20-\x7E]','?',r.get('problem_number') or '?')
        pnum=pnum.replace('|','/').replace('_','\\_')
        problembook+=f"- `{r['slug']}` — {r.get('year') or '?'}; {pnum}; {r['scope_status'].replace('_',' ')}; {'text' if r['statement_included'] else 'pointer'}; S={r['included_source_solution_count']}"+(f"; checked {r['reviewed_solution_id']}" if r['reviewed_solution_id'] else '')+'.\n'
(PKG/'Problems_and_Archive_Guide.md').write_text(problembook)

readme=f'''# Olympiad Combinatorics — research edition

Start with **Coverage_Report.md**. The all-history and all-solutions goals are not complete.

- Combinatorics_Theory.pdf / .md: proved methods, derived generalizations, 20 exercises with solutions.
- Worked_Solutions.pdf / .md: 26 checked rewritten historical cases.
- Problems_and_Archive_Guide.pdf / .md: case-study problems without answers, coverage and candidate index.
- Collected_Problems.pdf / .md: printable collection of the {problem_files} included source statements.
- Collected_Source_Problems.md: {problem_files} full source statements, with attribution.
- problems/: one file per included source statement.
- reviewed_problems/ and reviewed_solutions/: one file per W01–W26.
- source_solutions/: {source_solution_files} files, {source_solution_texts} supplied solutions; **not independently reviewed**.
- Catalog.csv: all {len(records)} retrieved candidates, including quarantine and pointer-only records.
- audit/: complete provenance, known defects, exact-duplicate groups, counts and finite verification results.

Mathematics is written in Markdown with LaTeX notation. The PDFs render the authored exposition. No external images are required for the reviewed cases. Some source-language text is not English.

For reuse of imported source text, retain its MathNet and original-source attribution and the CC BY 4.0 notice. Original rights assertions take precedence; those raw texts were withheld. Do not remove the review-status labels.
'''
(PKG/'README.md').write_text(readme)
(PKG/'ATTRIBUTION_AND_RIGHTS.md').write_text(report.split('## Provenance and reproduction policy')[1].split('## Completion status')[0])
for name in ['verify_examples.py','verification_results.json']:
    shutil.copy2(OUT/name,PKG/'audit'/name)
shutil.copy2(Path(__file__),PKG/'audit/build_archive.py')
print(json.dumps(stats,indent=2));print('package',PKG)
