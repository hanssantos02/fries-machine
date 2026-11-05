from pathlib import Path
import json
from zipfile import ZipFile

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';data=json.loads(p.read_text())
item=next(x for x in data['a'] if x['id']=='A07')
assert item['price']==40 and item['qty']==7
url='https://shopee.ph/product/447511770/11436017124'
item.update(spec='SHOPO/SHOPOMATIC roller-lever mechanical microswitch, three terminals pictured; exact manufacturer model and COM/NO/NC order unverified. Four provisional basket stops plus three coil indexes. Confirm dimensions/lever travel, reliable low-current contact operation and dry/cool mounting',price=22,status='SCREENSHOT PHP 22 for 1 piece, 15 Oct 2026; delivery extra. Verify contact functions, low-current reliability and mechanical/environmental fit',store='Shopee PH / SHOPOMATIC.ph',source='S22',product_url=url,why='Four provisional switches sense basket endpoints and three sense flavor-coil indexes so the controller knows when to stop motion. Signal inputs only, not motor/heater power switches or certified emergency-stop contacts. Reuse the same seven in final build; final count depends on existing mechanism.')
data['sources'].append({'id':'S22','label':'User screenshot 15 Oct 2026: SHOPOMATIC.ph SHOPO roller-lever microswitch PHP 22 per piece, explicitly 1 piece per order. Three terminals pictured; actual model/contact ordering, low-current reliability, dimensions and sealing unverified.','url':url})
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

p=root/'docs/BOM.md';t=p.read_text().replace('Step 30. Updated','Step 31. Updated',1).replace('PHP 17,383.40','PHP 17,257.40',1).replace('PHP 16,189.40','PHP 16,063.40',1).replace('PHP 9,309.00','PHP 9,183.00',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A07 |'):
        lines[i]=f"| A07 | {item['name']} | {item['spec']} | 7 | 22.00 | 154.00 | [Shopee SHOPOMATIC.ph]({url}); {item['status']} [S22] | {item['why']} |"
t='\n'.join(lines)+'\n'
t=t.replace('## Compatibility and selection checks\n\n','## Compatibility and selection checks\n\n- **A07 roller microswitches:** Correct mechanical style for contact-operated basket limits/coil indexes. Screenshot price PHP 22 is **per piece**: seven cost PHP 154, replacing PHP 280 allowance (PHP 126 reduction). Three terminals are pictured, but identify actual COM/NO/NC from markings and later continuity checks; do not guess physical pin order. Check switch size, screw spacing, roller direction/travel and secure mounting within the existing layout. Keep switches out of oil/splash and high-temperature zones; sealing/temperature ratings are unverified. Digital sensing uses very small currents, so check applicable minimum load and stable contact operation; a large power-current marking does not guarantee microload reliability. [Manufacturer contact-selection guidance](https://www.ia.omron.com/product/cautions/29/safety_precautions.html) is general guidance, not this seller\'s datasheet. These are signal/position inputs, not hardwired safety-rated emergency-stop switches.\n\n',1)
t=t.replace('The earlier spreadsheet and detailed BOM are preserved',f'- [S22] [Shopee SHOPOMATIC.ph SHOPO roller microswitch]({url}): user screenshot dated 15 October 2026, **PHP 22 per piece** and “1 piece per order.” Three terminals pictured; exact model, terminal order, dimensions, environmental and low-current ratings remain unverified.\n\nThe earlier spreadsheet and detailed BOM are preserved',1);p.write_text(t)

p=root/'PROJECT.md';t=p.read_text().replace('PHP 17,383.40','PHP 17,257.40',1)
t=t.replace('- **Heating architecture:**','- **Position switches (A07):** [SHOPOMATIC.ph SHOPO roller microswitch](https://shopee.ph/product/447511770/11436017124), screenshot PHP 22 **per piece**, quantity seven = PHP 154: four provisional basket endpoints plus three coil indexes. Confirm actual COM/NO/NC markings, low-current reliability, switch dimensions/travel and dry/cool mounting. Signal inputs only; not certified safety-stop or motor/heater power contacts. Final quantity depends on existing mechanism.\n- **Heating architecture:**',1);p.write_text(t)

p=root/'docs/MOTOR_SELECTION.md';t=p.read_text().replace('Step 30 — 15 October 2026.**','Step 31 — 15 October 2026.**',1)
t=t.replace('## Inputs needed before choosing a basket motor','## A07 roller-switch source (Step 31)\n\nThe user-supplied [SHOPOMATIC.ph SHOPO roller microswitch](https://shopee.ph/product/447511770/11436017124) matches the proposed contact-actuated position-sensing form. Screenshot price is **PHP 22 for one piece**; seven provisionally cost PHP 154. Four detect proposed basket endpoints and three mark coil reference positions. Final placement/count still depends on the existing mechanism. No basket/coil layout is redesigned by choosing this listing.\n\nThree terminals are pictured; do not infer a particular manufacturer model or terminal order from appearance. **COM** is the common contact; **NC** means normally closed (connected to COM while unpressed); **NO** means normally open (connects to COM when pressed). Confirm markings/contact behavior on the delivered part during the approved phase. These signal switches do not directly switch motor/heater power, stop a moving assembly mechanically or replace the separate hardwired emergency-stop controls.\n\nConfirm switch body size, mounting-hole spacing, lever/roller travel and mounting rigidity. Use a cam/stop that actuates without overdriving the lever, and locate the switch away from hot oil, steam/splash and excessive heat; no sealing or heat rating is established. For low-current digital inputs, verify stable contact operation and applicable minimum load. [Omron manufacturer guidance](https://www.ia.omron.com/product/cautions/29/safety_precautions.html) notes possible contact faults when general-load switches are used at microloads; its product ratings are not assigned to this generic switch. Any eventual pull-up/interface choice and debounce behavior belong to the later wiring/firmware phase.\n\n## Inputs needed before choosing a basket motor',1);p.write_text(t)

p=root/'docs/FRYER_ASSESSMENT.md';t=p.read_text().replace('Table A is PHP 9,309','Table A is PHP 9,183').replace('PHP 17,383.40','PHP 17,257.40').replace('PHP 16,189.40','PHP 16,063.40');p.write_text(t)

p=root/'PROGRESS.md';t=p.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 30');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 31 — A07 roller-switch supplier/price added.** SHOPOMATIC.ph SHOPO roller microswitch PHP 22 per piece × seven = PHP 154. Four provisional basket endpoints plus three coil indexes; terminal functions, mounting/environment and low-current reliability need confirmation. Table A PHP 9,183; Table B PHP 8,074.40; priced materials PHP 17,257.40 before six unquoted materials/fees. Final-use reuse, native clickable links, LCD and timed sequence retained; no Phase 2 approval.'+t[end:]
t=t.replace('Table A priced subtotal: **PHP 9,309.00**','Table A priced subtotal: **PHP 9,183.00**',1).replace('Priced materials subtotal A+B: **PHP 17,383.40**','Priced materials subtotal A+B: **PHP 17,257.40**',1).replace('Without fryer allowance: **PHP 16,189.40**','Without fryer allowance: **PHP 16,063.40**',1)
log='''### A07 roller microswitch on 15 October 2026 (Step 31)

- Reviewed user SHOPOMATIC.ph SHOPO listing/screenshot: roller lever, three terminals pictured, PHP 22 and explicit 1 piece per order. Direct product page inaccessible. No exact manufacturer model, terminal ordering, environmental or low-current ratings inferred from photo.
- Added candidate supplier/link and observed price to A07. Quantity seven retained: four provisional basket endpoints and three coil indexes. Correct sensing form, subject to actual mounting/travel/contact reliability and protected dry/cool placement. These are signal switches, not motor/heater power contacts or safety-rated emergency-stop devices.
- Omron primary contact-selection guidance supports checking low-current contact reliability/minimum applicable load; manufacturer ratings not assigned to seller switch. COM/NC/NO definitions saved without guessing physical pin order or starting wiring/firmware.
- A07 PHP 154 replaces PHP 280 allowance, PHP 126 reduction. Table A PHP 9,183; Table B PHP 8,074.40; priced materials PHP 17,257.40 (without fryer PHP 16,063.40). Six material quotes/conditions and separate fees remain. No duplicate prototype switches or spare quantity added.
- Updated PROJECT, readable BOM, motor guide and fryer budget note. No purchase, physical test, firmware, package install or phase transition.

'''
t=t.replace('### LR7843 selected price and description on 15 October 2026 (Step 30)',log+'### LR7843 selected price and description on 15 October 2026 (Step 30)',1);p.write_text(t)
with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    (root/'tmp/bom/before-a07-sheet.xml').write_bytes(z.read('xl/worksheets/sheet1.xml'))
    (root/'tmp/bom/before-a07-strings.xml').write_bytes(z.read('xl/sharedStrings.xml'))
print('A07 PHP22 x7=154; PHP126 reduction. A PHP9183; priced materials PHP17257.40.')
