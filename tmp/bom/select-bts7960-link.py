from pathlib import Path
import json
from zipfile import ZipFile
from lxml import etree as E

root=Path('/home/hans/repos/fries-machine')
path=root/'tmp/bom/lean-bom-data.json'
data=json.loads(path.read_text())
item=next(i for i in data['a'] if i['id']=='A04')
assert item['price']==268 and item['qty']==2
url='https://shopee.ph/product/1367148707/26183927355'
item.update(
    spec='User-supplied Shopee IBT-2/BTS7960-type module with two half-bridges forming ONE reversible brushed-DC motor driver per board. Candidate for proposed 12 V motors/5 V control; verify module ratings, running/stall current and cooling. Advertised 43 A is not a verified continuous board rating',
    price=275,
    store='Shopee PH / fulabs.ph (FU LABS)',
    status='SCREENSHOT PHP 275 per board, 15 Oct 2026; delivery extra. PROVISIONAL: final basket motor/driver match pending',
    source='S17; S18',
    product_url=url,
    why='One board powers and reverses one proposed basket DC motor; two boards cover provisional lift and tilt axes. Double refers to two half-bridges, not two independent motors. A single board is not the matching bipolar-stepper driver. Reuse in final build after validation.',
)
data['sources']=[s for s in data['sources'] if s['id']!='S5']
data['sources'].extend([
    {'id':'S17','label':'User screenshot 15 Oct 2026: fulabs.ph/FU LABS Shopee Double BTS7960 IBT-2-type board PHP 275 each. Two boards budgeted; final motor current/voltage and module cooling/quality unverified.','url':url},
    {'id':'S18','label':'Infineon BTS7960 manufacturer datasheet: each IC is a half-bridge; typical 43 A current limitation is not a continuous rating for a marketplace module. IC data do not establish this seller board quality or ratings.','url':'https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf'},
])
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

path=root/'docs/BOM.md';t=path.read_text().replace('Step 24. Updated','Step 25. Updated',1)
t=t.replace('PHP 18,557.40','PHP 18,571.40',1).replace('PHP 17,363.40','PHP 17,377.40',1).replace('PHP 10,483.00','PHP 10,497.00',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A04 |'):
        lines[i]=f"| A04 | {item['name']} | {item['spec']} | 2 | 275.00 | 550.00 | [Shopee fulabs.ph/FU LABS]({url}); {item['status']} [S17, S18] | {item['why']} |"
    elif line.startswith('- [S5]'):
        lines[i]=''
t='\n'.join(lines)+'\n'
note='- **A04 driver selection:** The user-supplied IBT-2/BTS7960-type board is a provisional match for the proposed brushed-DC basket motors, not a finalized match to an unknown motor. One board reverses one motor; two boards cost PHP 550 at the screenshot PHP 275 price. “Double” means two half-bridges forming one full H-bridge. A single module is not a replacement for a matched bipolar-stepper driver. Final acceptance needs actual motor voltage, running/start/stall current, module/terminal ratings and cooling. Infineon specifies the IC\'s typical current-limitation level around 43 A; that is not evidence of 43 A continuous operation for this seller\'s board. [Manufacturer datasheet](https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf).\n\n'
t=t.replace('## Compatibility and selection checks\n\n','## Compatibility and selection checks\n\n'+note,1)
t=t.replace('The earlier spreadsheet and detailed BOM are preserved',f'- [S17] [Shopee fulabs.ph/FU LABS BTS7960 module]({url}): user screenshot 15 October 2026, PHP 275 each before shipping; provisional final-motor match. Replaces the prior PHP 268 Circuitrocks reference.\n- [S18] [Infineon BTS7960 datasheet](https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf): IC half-bridge/current-limitation reference, not certification of the seller module.\n\nThe earlier spreadsheet and detailed BOM are preserved',1)
path.write_text(t)

path=root/'PROJECT.md';t=path.read_text().replace('PHP 18,557.40','PHP 18,571.40',1)
t=t.replace('- **Heating architecture:**','- **Basket driver candidate:** A04 user-supplied [Shopee fulabs.ph IBT-2/BTS7960-type module](https://shopee.ph/product/1367148707/26183927355), PHP 275 each, quantity two provisionally for lift/tilt. One board drives one brushed-DC motor in both directions. Match to actual motor current/voltage and module cooling before buying; advertised 43 A is not a verified continuous board rating. If basket steppers are selected, replace with matching stepper drivers rather than buying both alternatives.\n- **Heating architecture:**',1)
path.write_text(t)

path=root/'docs/FRYER_ASSESSMENT.md';t=path.read_text().replace('Following the Step 23 controller-price confirmation, Table A is PHP 10,483;', 'With the current controller/driver selections, Table A is PHP 10,497;').replace('PHP 18,557.40','PHP 18,571.40').replace('PHP 17,363.40','PHP 17,377.40');path.write_text(t)

path=root/'PROGRESS.md';t=path.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 24');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 25 — Shopee BTS7960 driver link/price added provisionally to A04.** PHP 275 each × two = PHP 550, a PHP 14 increase over the former source. Final basket motor/current match remains pending. Table A PHP 10,497; Table B PHP 8,074.40; priced materials PHP 18,571.40 before quotes/fees. Native clickable links, final-use reuse, I2C LCD and timed cycle retained; no Phase 2 approval.'+t[end:]
t=t.replace('Table A priced subtotal: **PHP 10,483.00**','Table A priced subtotal: **PHP 10,497.00**',1).replace('Priced materials subtotal A+B: **PHP 18,557.40**','Priced materials subtotal A+B: **PHP 18,571.40**',1).replace('Without fryer allowance: **PHP 17,363.40**','Without fryer allowance: **PHP 17,377.40**',1)
log='''### Basket DC driver product on 15 October 2026 (Step 25)

- Reviewed user fulabs.ph/FU LABS Shopee link and screenshot: IBT-2 marking, two power IC packages, one motor terminal pair and PHP 275 displayed. Direct page inaccessible; price/product evidence is the screenshot, not independently verified delivered hardware.
- A04 is the correct candidate architecture for the proposed brushed-DC lift/tilt motors, conditional on actual motor voltage/current/stall demand and board cooling/ratings. One module powers one reversible DC motor. “Double” is two half-bridges, not two independently driven motors. A single module is not the matched bipolar-stepper driver.
- Checked Infineon primary datasheet: BTS7960 IC is a half-bridge with a typical 43 A current-limitation level. This does not establish the marketplace module's continuous current capability, IC authenticity or thermal performance. Do not buy on the advertised current number alone.
- Replaced A04 supplier link/reference price with PHP 275 each, quantity two provisionally; subtotal PHP 550. Removed unused Circuitrocks S5 source, added S17 seller/S18 IC reference. Native clickable links must be reapplied after export.
- PHP 14 increase: Table A PHP 10,497; Table B PHP 8,074.40; priced materials PHP 18,571.40 (without fryer PHP 17,377.40). Five unquoted material entries and separate fee quotes remain. No additional duplicate driver set or practice motors.
- Updated PROJECT, BOM and fryer budget note. No physical purchase/test, firmware, package install or phase transition.

'''
t=t.replace('### Clickable Excel links on 15 October 2026 (Step 24)',log+'### Clickable Excel links on 15 October 2026 (Step 24)',1);path.write_text(t)

with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    (root/'tmp/bom/before-driver-sheet.xml').write_bytes(z.read('xl/worksheets/sheet1.xml'))
    (root/'tmp/bom/before-driver-strings.xml').write_bytes(z.read('xl/sharedStrings.xml') if 'xl/sharedStrings.xml' in z.namelist() else b'<sst/>')
print('A04 PHP275 x2=PHP550; A PHP10497; priced materials PHP18571.40; motor match provisional.')
