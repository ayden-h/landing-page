from pathlib import Path
import json,subprocess,re
OUT=Path(__file__).parent.resolve();P=OUT/'Combinatorics_Research_Package'
records=[json.loads(x) for x in (P/'audit/source_ledger.jsonl').read_text().splitlines()]
text='''---
title: "Collected Olympiad Combinatorics Problems"
subtitle: "770 source statements • partial research corpus"
author: "Compiled for haohao; original sources credited in the ledger"
date: "5 November 2026"
lang: en-US
---

# Scope and attribution {.unnumbered}

This volume prints the 770 source statements included in the companion research package. It is **not a complete historical collection** and its source classifications and transcriptions have not all been independently verified. Mixed-domain candidates are included when the source tags indicate a combinatorial component. Problem numbers, years and contest labels can contain extraction errors.

These statements are reproduced from MathNet under its CC BY 4.0 fallback for records with no explicit original rights assertion in the recovered metadata. Records with an explicit rights assertion, detected external statement figures, or known out-of-scope classification are excluded here and retained as pointers in the complete catalog. This filtering does not establish that every remaining transcription is error-free or complete.

Source: [MathNet](https://mathnet.mit.edu/), by Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman and Antonio Torralba, ICLR 2026. [Dataset and rights statement](https://huggingface.co/datasets/ShadenA/MathNet). [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original contest/source authors and booklet metadata are retained in the package's source ledger and individual problem files. Each entry links to its recovered source record.

Changes from the retrieved text: document grouping and typesetting; normalized contest labels where a discrepancy could be resolved. A few nonstandard TeX display commands may be normalized without changing the intended mathematics. Source prose is otherwise retained. Some entries are in their source language.

The separate **Worked Solutions** volume contains 26 reviewed, rewritten proofs. Files in `source_solutions/` contain additional supplied solutions with an explicit unreviewed label. Do not assume that an imported source proof has the same status as a reviewed case study.

Read **Coverage_Report.md** for exact counts, gaps, known defects and the distinction between competitions, shortlists, selection rounds and pipeline supplements.

'''
typesetting_changes=[]
for code in sorted(set(r['corrected_competition_code'] for r in records if r['statement_included'])):
    text+='\n# '+code+'\n\n'
    for r in sorted([x for x in records if x['corrected_competition_code']==code and x['statement_included']],key=lambda x:(x.get('year') or 0,x['slug'])):
        statement=(P/r['problem_file']).read_text().split('## Problem\n\n',1)[1]
        original_statement=statement
        statement=statement.replace('\\overarc','\\widehat')
        statement=re.sub(r'\\(?:begin|end)\{equation\*\}\s*\n','',statement)
        statement=statement.replace('✓',r'$\checkmark$')
        if statement!=original_statement:typesetting_changes.append({'slug':r['slug'],'changes':'Nonstandard overarc mapped to widehat, nested equation-star wrappers removed, or checkmark rendered as a math symbol, as applicable. Original text preserved in problems/.'})
        label=f"{r.get('year') or 'Year unknown'} — {r.get('problem_number') or 'Number unknown'}"
        text+='\n## '+label+'\n\n'
        text+=f"**Record:** `{r['slug']}`. **Category:** {r['scope_status'].replace('_',' ')}. [Source]({r['source_url']}).\n\n"
        text+=statement+'\n\n'
(P/'Collected_Problems.md').write_text(text)
(P/'audit/Typesetting_Changes.json').write_text(json.dumps(typesetting_changes,indent=2))
cmd=['pandoc',str(P/'Collected_Problems.md'),'-o',str(P/'Collected_Problems.pdf'),'--pdf-engine=xelatex','--from=markdown+tex_math_single_backslash','--top-level-division=chapter','--toc','--toc-depth=1','-V','documentclass=report','-V','fontsize=10pt','-V','papersize=letter','-V','geometry:margin=0.8in','-V','mainfont=DejaVu Serif','-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono','--include-in-header='+str(OUT/'pdf_header.tex')]
run=subprocess.run(cmd,capture_output=True,text=True,cwd=P)
(OUT/'Collected_Problems_build.log').write_text(run.stdout+run.stderr)
print('Collected_Problems',run.returncode,run.stderr[-4000:],flush=True)
raise SystemExit(run.returncode)
