from pathlib import Path
import json
from zipfile import ZipFile
from xml.etree import ElementTree as ET

root=Path('/home/hans/repos/fries-machine')
path=root/'tmp/bom/lean-bom-data.json'
data=json.loads(path.read_text())
item=next(i for i in data['a'] if i['id']=='A01')
assert item['price']==1030
item.update(
    spec='ATmega2560, 5 V logic, full-size Mega 2560 R3 compatible board. Selected seller option: 2560 R3 With Cable; pictured assembled female headers and USB A-to-B cable. Confirm actual USB-serial chip on delivery',
    price=699,
    status='SCREENSHOT: selected 2560 R3 With Cable PHP 699, 15 Oct 2026; delivery extra; board not yet tested',
    source='S16',
    store='Shopee PH / SAMIORE.ph (SAMIROB listing)',
)
data['sources']=[s for s in data['sources'] if s['id']!='S1']
source=next(s for s in data['sources'] if s['id']=='S16')
source['label']='User screenshot 15 Oct 2026: Shopee SAMIORE.ph/SAMIROB selected 2560 R3 With Cable PHP 699; pictured full-size board, assembled headers and USB A-to-B cable. Shipping extra; actual board/USB-serial chip untested.'
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

path=root/'docs/BOM.md'
text=path.read_text().replace('Step 22. Updated','Step 23. Updated',1)
text=text.replace('PHP 18,888.40','PHP 18,557.40',1).replace('PHP 17,694.40','PHP 17,363.40',1).replace('PHP 10,814.00','PHP 10,483.00',1)
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A01 |'):
        lines[i]=f"| A01 | {item['name']} | {item['spec']} | 1 | 699.00 | 699.00 | [Shopee: 2560 R3 With Cable]({item['product_url']}); {item['status']} [S16] | {item['why']} |"
    elif line.startswith('- Full-size 5 V Mega remains'):
        lines[i]='- Full-size 5 V Mega remains suitable for the planned signal count and I2C LCD. User screenshot now visibly selects **2560 R3 With Cable at PHP 699**, so A01 replaces the old PHP 1,030 supplier reference: PHP 331 reduction, one controller/cable set only. Compact PRO variants remain alternatives requiring their own header/pinout checks. Actual supplied USB-serial chip and board function will be checked during approved testing. [Arduino Mega family reference](https://docs.arduino.cc/hardware/mega-2560) supports the platform, not clone quality.'
    elif line.startswith('- [S1]'):
        lines[i]=''
    elif line.startswith('- [S16]'):
        lines[i]='- [S16] [Shopee SAMIORE.ph/SAMIROB Mega listing](https://shopee.ph/product/580325202/15523024357): user screenshot dated 15 October 2026 visibly selects **2560 R3 With Cable, PHP 699**. Full-size board and USB A-to-B cable pictured. Delivery separate; actual USB-serial chip and board operation untested. Replaces the former PHP 1,030 supplier reference; no second board/cable purchase.'
path.write_text('\n'.join(lines)+'\n')

path=root/'PROJECT.md'
text=path.read_text().replace('PHP 18,888.40','PHP 18,557.40',1)
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- **Preferred controller:**'):
        lines[i]='- **Preferred controller:** Full-size Mega 2560 R3 compatible board, 5 V logic. User screenshot confirms [Shopee SAMIORE.ph/SAMIROB](https://shopee.ph/product/580325202/15523024357) option **2560 R3 With Cable at PHP 699**, before shipping. A01 now uses this price, replacing PHP 1,030 reference. Pictured assembled headers and USB A-to-B cable; actual USB-serial chip and operation to verify on delivery. Compact PRO alternatives are not additional purchases. No electronics purchase or software installation has been reported.'
path.write_text('\n'.join(lines)+'\n')

path=root/'docs/FRYER_ASSESSMENT.md'
text=path.read_text().replace('Table A remains PHP 10,814;', 'Following the Step 23 controller-price confirmation, Table A is PHP 10,483;')
text=text.replace('become **PHP 18,888.40**','become **PHP 18,557.40**').replace('PHP 17,694.40','PHP 17,363.40')
path.write_text(text)

path=root/'PROGRESS.md'
text=path.read_text()
start=text.index('**PHASE 1: MATERIALS BUYING, Step 22')
end=text.index('\n',start)
text=text[:start]+'**PHASE 1: MATERIALS BUYING, Step 23 — Selected controller price confirmed at PHP 699.** A01 is Shopee “2560 R3 With Cable,” one full-size Mega/cable set, replacing PHP 1,030 reference. Table A PHP 10,483; Table B PHP 8,074.40; priced materials PHP 18,557.40 before outstanding quotes/fees. Final-use motors, I2C LCD and timed sequence retained; no Phase 2 approval.'+text[end:]
text=text.replace('Table A priced subtotal: **PHP 10,814.00**','Table A priced subtotal: **PHP 10,483.00**',1)
text=text.replace('Priced materials subtotal A+B: **PHP 18,888.40**','Priced materials subtotal A+B: **PHP 18,557.40**',1)
text=text.replace('Without fryer allowance: **PHP 17,694.40**','Without fryer allowance: **PHP 17,363.40**',1)
log='''### Selected controller price on 15 October 2026 (Step 23)

- New user screenshot visibly selects **2560 R3 With Cable** at **PHP 699**; full-size board, assembled headers and USB A-to-B cable pictured. This resolves Step 22's variant-price uncertainty; PHP 199 headline is not used.
- Replaced A01 PHP 1,030 original supplier reference with PHP 699; kept supplier URL and quantity one. Removed unused original source S1 from current workbook source list; updated S16 with selected-price evidence. No additional board or cable budgeted.
- PHP 331 reduction: Table A PHP 10,483; Table B unchanged PHP 8,074.40; priced materials PHP 18,557.40, or PHP 17,363.40 excluding the fryer. Five unquoted material entries and separate fees still prevent a complete quotation.
- Updated PROJECT, BOM, fryer-assessment budget note and workbook inputs. Actual delivered board/USB-serial chip will be checked later. No physical purchase, firmware, installation or phase transition performed.

'''
text=text.replace('### Controller product link on 15 October 2026 (Step 22)',log+'### Controller product link on 15 October 2026 (Step 22)',1)
path.write_text(text)

n={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    s=ET.fromstring(z.read('xl/worksheets/sheet1.xml')); strings=[]
    if 'xl/sharedStrings.xml' in z.namelist():strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
    def cell(c):
        v=c.find('m:v',n); f=c.find('m:f',n)
        if c.get('t')=='s':value=strings[int(v.text)]
        elif c.get('t')=='inlineStr':value=''.join(c.find('m:is',n).itertext())
        else:value=v.text if v is not None else None
        return {'value':value,'formula':f.text if f is not None else None}
    (root/'tmp/bom/before-controller-price-cells.json').write_text(json.dumps({c.get('r'):cell(c) for c in s.findall('.//m:c',n)}))
print('A01 PHP699; A PHP10483; B PHP8074.40; priced materials PHP18557.40; reduction PHP331.')
