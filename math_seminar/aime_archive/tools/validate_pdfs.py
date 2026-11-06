"""Verify the twelve final PDFs against their source and visual-QA ledgers."""
from pathlib import Path
import hashlib,json
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
volumes=[]
for subject in ('combinatorics','geometry','algebra','number_theory'):
    folder=WORK/('aime_'+subject)
    qa=json.loads((folder/'data/pdf_qa.json').read_text())
    assert qa['status']=='passed',(subject,'visual QA incomplete')
    assert len(qa['volumes'])==3,subject
    for filename,entry in qa['volumes'].items():
        pdf=folder/'output'/filename
        source=folder/entry['source_markdown']
        pdf_hash=hashlib.sha256(pdf.read_bytes()).hexdigest()
        source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
        assert pdf_hash==entry['sha256'],(filename,'PDF changed after QA')
        assert source_hash==entry['source_sha256'],(filename,'source changed after build')
        reader=PdfReader(pdf)
        assert len(reader.pages)==entry['pages'],filename
        assert entry['visually_reviewed_pages'],filename
        assert not entry.get('margin_anomalies'),filename
        if filename.endswith('_Theory.pdf'):
            assert reader.metadata.author=='Ayden Bi',(filename,'author metadata')
            assert 'Ayden Bi' in reader.pages[0].extract_text(),(filename,'title-page author')
        volumes.append({'subject':subject,'pdf':pdf.relative_to(WORK).as_posix(),
                        'pages':len(reader.pages),'sha256':pdf_hash,
                        'source_sha256':source_hash,
                        'author':reader.metadata.author if filename.endswith('_Theory.pdf') else None,
                        'sampled_visual_pages':entry['visually_reviewed_pages']})
out={'status':'passed','pdf_count':len(volumes),'total_pages':sum(v['pages'] for v in volumes),
     'theory_author':'Ayden Bi','volumes':volumes,
     'scope':'File integrity, author attribution, and agreement with sampled visual-QA ledgers; not formal mathematical proof verification.'}
(ROOT/'data/pdf_release_validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pdf_count':len(volumes),'total_pages':out['total_pages'],'theory_author':'Ayden Bi'},indent=2))
