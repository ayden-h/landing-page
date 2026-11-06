"""Build the printable course and companion volumes using Pandoc and Tectonic."""
from pathlib import Path
import argparse, subprocess

parser=argparse.ArgumentParser()
parser.add_argument('--pandoc',default='pandoc')
parser.add_argument('--tectonic',default='tectonic')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
(root/'output').mkdir(exist_ok=True)
for source,name,kind in [('theory/Combinatorics_Theory.md','Combinatorics_Theory','book'),('Problems.md','Combinatorics_Problems','article'),('Worked_Solutions.md','Combinatorics_Worked_Solutions','article')]:
    if not (root/source).exists():continue
    cmd=[args.pandoc,str(root/source),'--from=markdown-superscript','--standalone','--toc','--toc-depth=2','--pdf-engine='+args.tectonic,
         '-V','documentclass='+kind,'-V','classoption=oneside','-V','geometry:margin=0.85in',
         '-V','fontsize=11pt','-V','colorlinks=true','-V','linkcolor=blue','-V','urlcolor=blue',
         '--lua-filter='+str(root/'tools/pdf_math.lua'),
         '--include-in-header='+str(root/'tools/pdf_header.tex'),
         '-o',str(root/'output'/f'{name}.pdf')]
    if kind=='book':cmd+=['--lua-filter='+str(root/'tools/keep_proofs.lua')]
    subprocess.run(cmd,check=True)
    print(name+' built')
