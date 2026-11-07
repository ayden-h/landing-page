from pathlib import Path
import concurrent.futures,json,os,subprocess,re,shutil,sys
OUT=Path(__file__).resolve().parent;ROOT=OUT.parent
subjects=['Algebra','Geometry','Number_Theory']
inserts={
 'Algebra': [('## The parameter threshold','![The sharp value changes regime at lambda = 8.](figures/radical_threshold.pdf){width=90%}\n\n'),
             ('## Uniform monotone approximation','![For twelve units, the optimal prefixes select precisely the costs 1 through 12.](figures/marginal_costs.pdf){width=95%}\n\n')],
 'Geometry':[('# Circles as linear equations in a quadratic variable','![An admissible G14 configuration. The green line SK is the common tangent; the two target circles are blue and ochre.](figures/tangent_transfer.pdf){width=90%}\n\n')],
 'Number_Theory':[('## Bounding the smallest variable','![For quotient 4 and b = 8, the other root replaces 30 by 2. The solution pair descends from (30,8) to (8,2).](figures/vieta_jump.pdf){width=90%}\n\n')]
}
for s in subjects:
    P=OUT/(s+'_Research_Package');p=P/(s+'_Theory.md');text=p.read_text()
    text=re.sub(r'!\[[^\]]*\]\(figures/[^)]+\)\{width=\d+%\}\n\n','',text)
    for marker,fig in inserts[s]:text=text.replace(marker,fig+marker)
    p.write_text(text)
    header=(OUT/'pdf_header.tex').read_text().replace('Olympiad Combinatorics','Olympiad '+s.replace('_',' '))
    (P/'audit/pdf_header.tex').write_text(header)
    for script in ['draw_subject_figures.py','build_subject_pdfs.py']:shutil.copy2(OUT/script,P/'audit'/script)

env=os.environ.copy();env.update(TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}',TEXFORMATS=str(ROOT/'tmp/texfmt'),TEXINPUTS=str(ROOT/'tmp/texfmt')+':')
def build(pair):
    s,suffix=pair;P=OUT/(s+'_Research_Package');name=s+'_'+suffix;raw=suffix=='Collected_Problems'
    cmd=['pandoc',str(P/(name+'.md')),'-o',str(P/(name+'.pdf')),'--pdf-engine=xelatex','--from=markdown+tex_math_single_backslash','--top-level-division=chapter','--toc','--toc-depth='+('1' if raw else '2'),'-V','documentclass=report','-V','fontsize='+('10pt' if raw else '11pt'),'-V','papersize=letter','-V','geometry:margin=0.85in','-V','mainfont='+('DejaVu Serif' if raw else 'Latin Modern Roman'),'-V','sansfont='+('DejaVu Sans' if raw else 'Latin Modern Sans'),'-V','monofont=DejaVu Sans Mono','--include-in-header='+str(P/'audit/pdf_header.tex'),'--resource-path='+str(P)]
    if suffix=='Theory':cmd.append('--number-sections')
    r=subprocess.run(cmd,capture_output=True,text=True,env=env,cwd=P)
    (P/'audit'/(name+'_build.log')).write_text(r.stdout+r.stderr)
    return {'file':name,'returncode':r.returncode,'log_tail':r.stderr[-1500:]}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results=[]
    for r in pool.map(build,[(s,t) for s in subjects for t in ['Theory','Worked_Solutions','Collected_Problems'] if len(sys.argv)==1 or s+'_'+t in sys.argv[1:]]):
        print(json.dumps(r),flush=True);results.append(r)
(OUT/'subject_pdf_build_results.json').write_text(json.dumps(results,indent=2))
raise SystemExit(any(r['returncode'] for r in results))
