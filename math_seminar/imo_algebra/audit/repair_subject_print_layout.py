"""Repair source typography in printed collections; retain original source files."""
from pathlib import Path
import json,re

OUT=Path(__file__).resolve().parent
SUBJECTS=['Algebra','Geometry','Number_Theory']

def shorten_links(text):
    return re.sub(r'Official paper: (https://www\.imo-official\.org/\S+\.pdf) \.',r'Official paper: [PDF](\1).',text)

for p in (OUT/'subject_sources').glob('*Worked_Solutions.md'):
    p.write_text(shorten_links(p.read_text()))

for subject in SUBJECTS:
    package=OUT/(subject+'_Research_Package')
    for p in package.rglob('*.md'):
        if 'problems' in p.parts or 'source_solutions' in p.parts: continue
        text=p.read_text(); new=shorten_links(text)
        if text!=new:p.write_text(new)
    reviewed=package/'audit/reviewed_cases.json'
    reviewed.write_text(shorten_links(reviewed.read_text()))
    path=package/(subject+'_Collected_Problems.md')
    text=path.read_text()
    logpath=package/'audit/Typesetting_Changes.json'
    changes=json.loads(logpath.read_text())
    def replace(old,new,slug,description):
        global text
        if old in text:
            text=text.replace(old,new)
            entry={'slug':slug,'changes':description+' Raw source preserved separately.'}
            if entry not in changes:changes.append(entry)
    replace(r'\begin{array}{c}'+'\n'+r'\overline{ABC}',r'\begin{array}{cc}'+'\n'+r'\overline{ABC}','mkd_2008_e7301f','Matched array declaration to the two-column source rows.')
    recurrence=r'a_0 = 1, a_1 = 3 \text{ and } a_{n+2} = 1 + \left\lfloor \frac{a_{n+1}^2}{a_n} \right\rfloor \text{ for all } n \ge 0.'
    if '\n\n'+recurrence+'\nShow' in text:
        replace('\n\n'+recurrence+'\nShow','\n\n$$\n'+recurrence+'\n$$\n\nShow','vnm_2011_36c22e','Restored display-math delimiters around the recurrence.')
    equation=r'\angle BAC + \angle CAD + \angle DAB = \angle ABC + \angle CBD + \angle DBA, \\'+'\n'+r'\angle ACB + \angle BCD + \angle DCA = \angle ADB + \angle BDC + \angle CDA.'
    if '\n$$\n'+equation+'\n$$' in text:
        replace('\n$$\n'+equation+'\n$$','\n$$\n\\begin{gathered}\n'+equation+'\n\\end{gathered}\n$$','usa_2025_ed5827','Set the two equations on separate display rows.')
    replace(r'$$ii) \text{The line } CD \text{ passes through a fixed point when } C \text{ moves on } (O) \text{ so that } C \text{ does not coincide with } A \text{ and } B.$$',r'ii) The line $CD$ passes through a fixed point when $C$ moves on $(O)$ so that $C$ does not coincide with $A$ and $B$.','vnm_2005_7f10fc','Moved prose out of an unbreakable display equation.')
    replace(r'330\ у85',r'330\ \text{у}85','mkd_2009_ee8242','Used a text font for the source Cyrillic variable glyph.')
    replace(r'$P(1), P(2), \ldots, P(50)$',r'$P(1)$, $P(2)$, $\ldots$, $P(50)$','imo_2009_cf1420','Allowed line breaks between the listed polynomial values.')
    # Pandoc does not recognize a dollar delimiter followed by a space.
    parts=re.split(r'(?=\*\*Record:\*\* `)',text)
    for i,part in enumerate(parts):
        # Consume paired dollar spans in order, so the gap between $a$ and $b$
        # is never mistaken for a formula with whitespace at its edges.
        new=re.sub(r'(?<!\$)\$(?!\$)([^$\n]+)\$(?!\$)',lambda m:'$'+m.group(1).strip()+'$',part)
        if part!=new:
            slug=re.search(r'\*\*Record:\*\* `([^`]+)`',part)
            changes.append({'slug':slug.group(1) if slug else 'core','changes':'Removed spaces immediately inside inline math delimiters; formulas unchanged. Raw source preserved separately.'})
        parts[i]=new
    path.write_text(''.join(parts))
    logpath.write_text(json.dumps(changes,indent=2,ensure_ascii=False)+'\n')
    print(subject,len(changes),'typesetting notes')
