from pathlib import Path
import subprocess,json,re,shutil
OUT=Path(__file__).parent.resolve();P=OUT/'Combinatorics_Research_Package'
work=P/'Worked_Solutions.md'
s=work.read_text()
s=re.sub(r'!\[[^\]]*\]\(figures/[^)]+\)\{width=\d+%\}\n\n','',s)
s=s.replace('**Transfer.** Classify one legal move', '![A synchronized height-two jump on an eight-column board.](figures/bishop_xor.pdf){width=95%}\n\n**Transfer.** Classify one legal move')
s=s.replace('**Generalization.** The theory book', '![The sharp four-block doubly stochastic matrix.](figures/stochastic_blocks.pdf){width=70%}\n\n**Generalization.** The theory book')
s=s.replace('**Audit note.** The four-tile construction', '![A maximal eight-tile placement for k=5 and n=8.](figures/maximal_tiles.pdf){width=70%}\n\n**Audit note.** The four-tile construction')
work.write_text(s)
for name in ['Combinatorics_Theory','Worked_Solutions','Problems_and_Archive_Guide']:
    cmd=['pandoc',str(P/(name+'.md')),'-o',str(P/(name+'.pdf')),'--pdf-engine=xelatex','--from=markdown+tex_math_single_backslash','--top-level-division=chapter','--toc','--toc-depth=2','-V','documentclass=report','-V','fontsize=11pt','-V','papersize=letter','-V','geometry:margin=0.85in','-V','mainfont=Latin Modern Roman','-V','sansfont=Latin Modern Sans','-V','monofont=DejaVu Sans Mono','-V','colorlinks=true','--include-in-header='+str(OUT/'pdf_header.tex'),'--resource-path='+str(P)]
    if name=='Combinatorics_Theory':cmd.append('--number-sections')
    run=subprocess.run(cmd,capture_output=True,text=True,cwd=P)
    (OUT/(name+'_build.log')).write_text(run.stdout+run.stderr)
    print(name,run.returncode,run.stderr[-2500:],flush=True)
    if run.returncode:raise SystemExit(run.returncode)
shutil.copy2(OUT/'draw_figures.py',P/'audit/draw_figures.py')
shutil.copy2(OUT/'pdf_header.tex',P/'audit/pdf_header.tex')
shutil.copy2(OUT/'build_pdfs.py',P/'audit/build_pdfs.py')
