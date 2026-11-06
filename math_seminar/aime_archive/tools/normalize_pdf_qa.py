"""Make the independently produced PDF inspection ledgers portable."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
for subject in ('combinatorics','geometry','algebra','number_theory'):
    folder=ROOT.parent/('aime_'+subject)
    path=folder/'data/pdf_qa.json'
    data=json.loads(path.read_text())
    assert data['status']=='passed',(subject,'inspection is not complete')
    entries=data['volumes']
    if isinstance(entries,list):entries={Path(e['pdf']).name:e for e in entries}
    for filename,entry in entries.items():
        source=Path(entry['source_markdown'])
        if source.is_absolute():source=source.relative_to(folder)
        entry['source_markdown']=source.as_posix()
        if 'pdf' in entry:entry['pdf']='output/'+filename
        entry['sha256']=entry.get('sha256',entry.get('pdf_sha256'))
        entry['source_sha256']=entry.get('source_sha256',entry.get('source_markdown_sha256'))
        entry['visually_reviewed_pages']=entry.get('visually_reviewed_pages',entry.get('sampled_physical_pages'))
        entry['margin_anomalies']=entry.get('margin_anomalies',entry.get('all_page_text_bounds',{}).get('pages_outside_body_margin',[]))
    data['volumes']=entries
    def portable(value):
        if isinstance(value,list):return [portable(v) for v in value]
        if isinstance(value,dict):return {portable(k):portable(v) for k,v in value.items()}
        if isinstance(value,str):
            value=value.replace(str(ROOT.parent)+'/', '')
            value=re.sub(r'/private/var/folders/[^`]+','<temporary extracted image>',value)
            if value.startswith('/tmp/aime-research/'):
                value='temporary research cache/'+Path(value).name
        return value
    data=portable(data)
    data['preview_storage_note']='Rendered inspection images were kept in the temporary research cache; the published deliverables are the PDFs and editable manuscripts.'
    path.write_text(json.dumps(data,indent=2)+'\n')
print('Normalized four PDF QA ledgers without changing their findings.')
