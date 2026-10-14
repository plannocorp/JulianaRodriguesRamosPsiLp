"""Check static references and essential document structure without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.errors = []
        self.heading_count = 0
        self.language = None
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if 'id' in attributes:
            identifier = attributes['id']
            if identifier in self.ids:
                self.errors.append(f'Duplicate id: {identifier}')
            self.ids.add(identifier)
        if tag == 'html':
            self.language = attributes.get('lang')
        if tag == 'meta' and attributes.get('name') == 'viewport':
            self.viewport = True
        if tag == 'h1':
            self.heading_count += 1
        if tag == 'img' and not attributes.get('alt'):
            self.errors.append('Image without descriptive alt')
        for name in ('href', 'src'):
            reference = attributes.get(name)
            if reference:
                self.references.append(reference)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

parser = SiteParser()
parser.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
for reference in parser.references:
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        continue
    if not url.path:
        if url.fragment and url.fragment not in parser.ids:
            parser.errors.append(f'Missing anchor: {reference}')
    elif not (ROOT / url.path).is_file():
        parser.errors.append(f'Missing local file: {reference}')
if parser.language != 'pt-BR':
    parser.errors.append('Document language must be pt-BR')
if not parser.viewport:
    parser.errors.append('Missing viewport metadata')
if parser.heading_count != 1:
    parser.errors.append(f'Expected one h1, found {parser.heading_count}')
if parser.errors:
    print('\n'.join(parser.errors), file=sys.stderr)
    sys.exit(1)
print(f'OK: {len(parser.references)} references checked; anchors, assets, image descriptions and document structure valid.')
