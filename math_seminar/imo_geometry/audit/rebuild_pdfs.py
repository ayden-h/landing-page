"""Rebuild this package's three PDFs with Pandoc and a working XeLaTeX installation."""
from pathlib import Path
import subprocess
P=Path(__file__).resolve().parent.parent
subject=next(p.stem.removesuffix('_Worked_Solutions') for p in P.glob('*_Worked_Solutions.md'))
for suffix in ['Theory','Worked_Solutions','Collected_Problems']:
    raw=suffix=='Collected_Problems';name=subject+'_'+suffix
    cmd=['pandoc',str(P/(name+'.md')),'-o',str(P/(name+'.pdf')),
         '--pdf-engine=xelatex','--from=markdown+tex_math_single_backslash',
         '--top-level-division=chapter','--toc','--toc-depth='+('1' if raw else '2'),
         '-V','documentclass=report','-V','fontsize='+('10pt' if raw else '11pt'),
         '-V','papersize=letter','-V','geometry:margin=0.85in',
         '-V','mainfont='+('DejaVu Serif' if raw else 'Latin Modern Roman'),
         '-V','sansfont='+('DejaVu Sans' if raw else 'Latin Modern Sans'),
         '-V','monofont=DejaVu Sans Mono',
         '--include-in-header='+str(P/'audit/pdf_header.tex'),'--resource-path='+str(P)]
    if suffix=='Theory':cmd.append('--number-sections')
    subprocess.run(cmd,cwd=P,check=True)
    print('Built',name+'.pdf')
