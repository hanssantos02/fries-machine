"""Add native Excel hyperlinks: fallback for the artifact engine's missing hyperlink API.

Only hyperlink relationships, link font styles and link-cell style references change.
Cell text, formulas, cached values, layout and all other ZIP entries are preserved.
"""
from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
import json
import re
from lxml import etree as E

root = Path('/home/hans/repos/fries-machine')
target = root / 'BOM_Automatic_Fries_Machine.xlsx'
data = json.loads((root / 'tmp/bom/lean-bom-data.json').read_text())
ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
main = ns['x']
rel_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
office_rel = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
sheet_path = 'xl/worksheets/sheet1.xml'
rels_path = 'xl/worksheets/_rels/sheet1.xml.rels'

with ZipFile(target) as z:
    entries = [(info, z.read(info.filename)) for info in z.infolist()]
contents = {info.filename: content for info, content in entries}
sheet = E.fromstring(contents[sheet_path])
styles = E.fromstring(contents['xl/styles.xml'])
strings = []
if 'xl/sharedStrings.xml' in contents:
    strings = [''.join(si.itertext()) for si in E.fromstring(contents['xl/sharedStrings.xml'])]

def value(cell):
    val = cell.find('x:v', ns)
    if cell.get('t') == 's':
        return strings[int(val.text)]
    if cell.get('t') == 'inlineStr':
        return ''.join(cell.find('x:is', ns).itertext())
    return val.text if val is not None else ''

cells = {c.get('r'): c for c in sheet.findall('.//x:sheetData/x:row/x:c', ns)}
snapshot = {addr: (value(c), c.findtext('x:f', namespaces=ns)) for addr, c in cells.items()}
sources = {s['id']: s['url'] for s in data['sources']}
items = {item['id']: item for key in ['a', 'b', 'c'] for item in data[key]}
links = {}
item_rows = {}
for addr, cell in cells.items():
    text = value(cell)
    if not isinstance(text, str):
        continue
    if addr.startswith('A') and text in items:
        item = items[text]
        item_rows[text] = re.search(r'\d+', addr).group()
        source_ids = re.findall(r'S\d+', item.get('source') or '')
        url = item.get('product_url') or next((sources[s] for s in source_ids if s in sources), None)
        if url:
            links['G' + re.search(r'\d+', addr).group()] = url
    found = re.search(r'https?://[^\s]+', text)
    if found:
        links[addr] = found.group().rstrip('.,;)')

assert links.get('G' + item_rows['A01']) == 'https://shopee.ph/product/580325202/15523024357'
assert links.get('G' + item_rows['B01']) == 'https://shopee.ph/product/1303238794/40333822650'

rels = E.fromstring(contents[rels_path]) if rels_path in contents else E.Element('Relationships', nsmap={None: rel_ns})
if rels.tag == 'Relationships':
    rels.tag = '{' + rel_ns + '}Relationships'
existing = sheet.find('x:hyperlinks', ns)
if existing is not None:
    for link in list(existing):
        # The BOM's generated links may have moved after inserting an item row.
        # Rebuild managed A/G anchors, rather than keeping a stale source target.
        if re.fullmatch(r'[AG]\d+', link.get('ref', '')):
            relationship = link.get('{' + office_rel + '}id')
            existing.remove(link)
            for rel in list(rels):
                if rel.get('Id') == relationship:
                    rels.remove(rel)
else:
    existing = E.Element('{' + main + '}hyperlinks', nsmap={'r': office_rel})
    # SpreadsheetML schema places hyperlinks before print/page/drawing elements.
    following = {'printOptions', 'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst'}
    index = next((i for i, child in enumerate(sheet) if E.QName(child).localname in following), len(sheet))
    sheet.insert(index, existing)

fonts = styles.find('x:fonts', ns)
formats = styles.find('x:cellXfs', ns)
style_map = {}
used_ids = {r.get('Id') for r in rels}
for number, (addr, url) in enumerate(links.items(), 1):
    relationship = 'bomLink' + str(number)
    while relationship in used_ids:
        relationship += '_'
    used_ids.add(relationship)
    E.SubElement(rels, '{' + rel_ns + '}Relationship', Id=relationship, Type=office_rel + '/hyperlink', Target=url, TargetMode='External')
    E.SubElement(existing, '{' + main + '}hyperlink', ref=addr, attrib={'{' + office_rel + '}id': relationship}, tooltip='Open supplier or reference page')
    cell = cells[addr]
    base = int(cell.get('s', '0'))
    if base not in style_map:
        base_format = formats[base]
        base_font = fonts[int(base_format.get('fontId', '0'))]
        font = deepcopy(base_font)
        for child in list(font):
            if E.QName(child).localname in {'color', 'u'}:
                font.remove(child)
        E.SubElement(font, '{' + main + '}color', rgb='FF0563C1')
        E.SubElement(font, '{' + main + '}u', val='single')
        font_index = len(fonts)
        fonts.append(font)
        fmt = deepcopy(base_format)
        fmt.set('fontId', str(font_index))
        fmt.set('applyFont', '1')
        style_map[base] = len(formats)
        formats.append(fmt)
    cell.set('s', str(style_map[base]))
fonts.set('count', str(len(fonts)))
formats.set('count', str(len(formats)))

assert snapshot == {addr: (value(c), c.findtext('x:f', namespaces=ns)) for addr, c in cells.items()}
updates = {
    sheet_path: E.tostring(sheet, encoding='utf-8', xml_declaration=True),
    'xl/styles.xml': E.tostring(styles, encoding='utf-8', xml_declaration=True),
    rels_path: E.tostring(rels, encoding='utf-8', xml_declaration=True),
}
staged = root / 'tmp/bom/native-links.staging'
with ZipFile(staged, 'w') as z:
    for info, content in entries:
        z.writestr(info, updates.pop(info.filename, content))
    for name, content in updates.items():
        z.writestr(name, content)
with ZipFile(staged) as z:
    assert z.testzip() is None
    saved = E.fromstring(z.read(sheet_path))
    saved_rels = {r.get('Id'): r for r in E.fromstring(z.read(rels_path))}
    saved_links = saved.findall('x:hyperlinks/x:hyperlink', ns)
    for link in saved_links:
        rel = saved_rels[link.get('{' + office_rel + '}id')]
        if link.get('ref') in links:
            assert rel.get('Target') == links[link.get('ref')]
            assert rel.get('TargetMode') == 'External'
    assert set(links) <= {link.get('ref') for link in saved_links}
staged.replace(target)
(root / 'tmp/bom/hyperlink-check.json').write_text(json.dumps({'count': len(links), 'links': links}, indent=2) + '\n')
print(json.dumps({'native_clickable_links': len(links), 'prices_text_formulas_preserved': True}))
