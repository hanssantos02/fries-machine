from pathlib import Path
import json
from zipfile import ZipFile
from xml.etree import ElementTree as ET

root=Path('/home/hans/repos/fries-machine')
url='https://shopee.ph/product/580325202/15523024357'
path=root/'tmp/bom/lean-bom-data.json'
data=json.loads(path.read_text())
item=next(i for i in data['a'] if i['id']=='A01')
assert item['price']==1030
item.update(
    spec='ATmega2560, 5 V logic, full-size R3 layout. Shopee option: 2560 R3 With Cable; confirm supplied USB-serial chip/cable and assembled headers. Existing PHP 1030 is the original e-Gizmo board+cable reference, not a Shopee quote',
    store='Shopee / SAMIORE.ph candidate; e-Gizmo price reference',
    status='Shopee full-size option price UNCONFIRMED. PHP 199 is unselected/after voucher; retain original PHP 1030 reference pending selected price',
    source='S1; S16',
    product_url=url,
    why='Reads buttons and switches, controls timing/driver signals and the I2C LCD. Choose full-size 2560 R3 With Cable for existing layout; compact PRO variants need their own header/pinout check. Buy one controller and reuse it in final build.',
)
assert not any(s['id']=='S16' for s in data['sources'])
data['sources'].append({'id':'S16','label':'User screenshot 15 Oct 2026: Shopee SAMIORE.ph/SAMIROB Mega listing; choose full-size 2560 R3 With Cable. PHP 199 after voucher has no selected variant; actual option price unconfirmed. Arduino reference confirms Mega family capability; clone delivery untested.','url':url})
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

path=root/'docs/BOM.md'
text=path.read_text().replace('Step 20. Updated','Step 22. Updated',1)
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A01 |'):
        lines[i]=f"| A01 | {item['name']} | {item['spec']} | 1 | 1,030.00 | 1,030.00 | [Shopee: choose 2560 R3 With Cable]({url}); {item['status']} [S1, S16] | {item['why']} |"
text='\n'.join(lines)+'\n'
old='- Retain the full-size 5 V Mega candidate for common headers and included USB cable; no Wi-Fi or extra I/O board. A cheaper Pro Mini is an optional substitution, not another purchase; verify headers/cable and delivered cost first.'
new='- Full-size 5 V Mega remains suitable for the planned signal count and I2C LCD. Added the user-supplied Shopee listing to A01 as a clickable link: choose **2560 R3 With Cable**. The screenshot shows no selected variant and PHP 199 **after voucher**, so that amount is not used as its confirmed price. A01 retains PHP 1,030 from the original e-Gizmo reference until the selected Shopee price is observed. Compact MEGA2560 PRO / PRO TYPE-C can be functional alternatives but require their own header assembly, pinout and connector checks; do not buy another board in addition. [Arduino Mega family reference](https://docs.arduino.cc/hardware/mega-2560) supports the architecture, not this seller\'s product quality or exact clone USB interface.'
assert old in text
text=text.replace(old,new,1)
text=text.replace('The earlier spreadsheet and detailed BOM are preserved',f'- [S16] [Shopee SAMIORE.ph/SAMIROB Mega listing]({url}): user screenshot dated 15 October 2026; full-size **2560 R3 With Cable** is the matching option. Selected-option price unconfirmed; PHP 199 after-voucher headline is not accepted as its price. Original S1 PHP 1,030 reference remains in the price input.\n\nThe earlier spreadsheet and detailed BOM are preserved',1)
path.write_text(text)

path=root/'PROJECT.md'
text=path.read_text()
old='- **Preferred controller:** User permits recommendation. Proposed Mega 2560 R3 compatible board, 5 V logic, to simplify the many buttons/switches and motor interfaces. Previous spreadsheet used an ESP32; no electronics have been purchased.'
new='- **Preferred controller:** Full-size Mega 2560 R3 compatible board, 5 V logic. User-supplied [Shopee SAMIORE.ph/SAMIROB listing](https://shopee.ph/product/580325202/15523024357) added to A01; matching option **2560 R3 With Cable**. No variant selected in screenshot; PHP 199 is an after-voucher headline, not a confirmed option price. Retain original PHP 1,030 e-Gizmo reference pending the selected price. Compact PRO variants are alternatives needing header/pinout checks, not additional purchases. No electronics purchased; no software installation authorized.'
assert old in text
path.write_text(text.replace(old,new,1))

path=root/'PROGRESS.md'
text=path.read_text()
start=text.index('**PHASE 1: MATERIALS BUYING, Step 21')
end=text.index('\n',start)
text=text[:start]+'**PHASE 1: MATERIALS BUYING, Step 22 — Matching Mega controller link added to A01.** Recommend full-size Shopee option “2560 R3 With Cable.” Screenshot PHP 199 is after voucher with no variant selected; actual option price unconfirmed. Original PHP 1,030 controller price reference and PHP 18,888.40 priced materials subtotal retained. Final-use motors, LCD and timed cycle retained; Phase 1 continues.'+text[end:]
log='''### Controller product link on 15 October 2026 (Step 22)

- Reviewed user Shopee link/screenshot: listing mixes full-size 2560 R3 With Cable, MEGA2560-CH340G, compact MEGA2560 PRO and PRO TYPE-C. Recommend full-size With Cable to match the existing controller/layout and minimize beginner header soldering. No unsupported claim that compact PRO cannot operate the machine.
- Arduino primary Mega documentation confirms the ATmega2560 platform's 54 digital pins, 16 analog inputs and I2C capability for the proposed controls/LCD. This is a platform comparison, not proof of this clone's exact USB chip, supplied accessories, build quality or shipping condition. Direct Shopee access unavailable; user screenshot used for listing evidence.
- Added a clickable HYPERLINK to A01's Where-to-buy cell plus source S16 and exact option instruction. Screenshot PHP 199 is explicitly after voucher with no variant selected; do not assume it is the full-size With Cable price. A01 retains original e-Gizmo PHP 1,030 reference, clearly labeled; no claimed savings or total change. One board only, reused in final machine.
- Synchronized PROJECT and readable BOM. No new purchase, firmware, installation or physical build performed. Selected variant price and delivered-board checks remain pending; no phase transition.

'''
text=text.replace('### Product-link workflow on 15 October 2026 (Step 21)',log+'### Product-link workflow on 15 October 2026 (Step 21)',1)
path.write_text(text)

n={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    s=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    strings=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
    def cell(c):
        v=c.find('m:v',n);f=c.find('m:f',n)
        if c.get('t')=='s':value=strings[int(v.text)]
        elif c.get('t')=='inlineStr':value=''.join(c.find('m:is',n).itertext())
        else:value=v.text if v is not None else None
        return {'value':value,'formula':f.text if f is not None else None}
    (root/'tmp/bom/before-controller-cells.json').write_text(json.dumps({c.get('r'):cell(c) for c in s.findall('.//m:c',n)}))
print('A01 link/variant added; PHP1030 original reference retained; selected Shopee price unconfirmed.')
