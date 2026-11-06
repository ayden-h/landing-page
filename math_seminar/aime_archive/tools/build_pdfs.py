"""Build a subject's printable theory, problem, and solution volumes."""
from pathlib import Path
import argparse, subprocess, os

p=argparse.ArgumentParser()
p.add_argument('subject',choices=['geometry','algebra','number_theory'])
p.add_argument('--pandoc',default='pandoc')
p.add_argument('--tectonic',default='tectonic')
p.add_argument('--theory-only',action='store_true')
args=p.parse_args()
tools=Path(__file__).resolve().parent
root=tools.parents[1]/('aime_'+args.subject)
title='_'.join(x.title() for x in args.subject.split('_'))
(root/'output').mkdir(exist_ok=True)
items=[(f'theory/{title}_Theory.md',f'{title}_Theory','book')]
if not args.theory_only:items += [('Problems.md',f'{title}_Problems','article'),('Worked_Solutions.md',f'{title}_Worked_Solutions','article')]
for source,name,kind in items:
    if not (root/source).exists():raise FileNotFoundError(root/source)
    cmd=[args.pandoc,str(root/source),'--from=markdown-superscript','--standalone','--toc','--toc-depth=2',
        '--resource-path='+os.pathsep.join([str(root/'theory'),str(root)]),
        '--pdf-engine='+args.tectonic,'-V','documentclass='+kind,
        '-V','classoption=oneside','-V','geometry:margin=0.85in','-V','fontsize=11pt',
        '-V','colorlinks=true','-V','linkcolor=blue','-V','urlcolor=blue',
        '--lua-filter='+str(tools/'pdf_math.lua'),'--include-in-header='+str(tools/'pdf_header.tex'),
        '-o',str(root/'output'/f'{name}.pdf')]
    if kind=='book':cmd+=['--lua-filter='+str(tools/'keep_proofs.lua')]
    subprocess.run(cmd,check=True)
    print(name+' built',flush=True)
