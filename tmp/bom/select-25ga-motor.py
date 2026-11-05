from pathlib import Path
import json
from zipfile import ZipFile

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';data=json.loads(p.read_text())
motor=next(x for x in data['a'] if x['id']=='A05')
assert motor['price']==500 and motor['qty']==3
url='https://shopee.ph/product/156048989/2380743022'
motor.update(spec='Candidate 25GA-370 brushed DC gearmotor; screenshot-selected 12 V 30 RPM, advertised 25 mm gearbox. Confirm rated running torque/duty, running/stall current, shaft/mounting and loaded-coil fit; nominally 2 seconds per revolution, not verified dispensing time',price=214,status='SCREENSHOT PHP 214, selected 12V 30RPM, 15 Oct 2026. PRE-ORDER ships in 5 days; delivery extra. HOLD torque/current/fit validation',source='S19',store='Shopee PH / seller 156048989',product_url=url,why='One motor turns each flavor coil; three are budgeted once for final-use reuse. Stop at the calibrated index switch, not elapsed motor time alone. Confirm torque and packet release with the loaded coil; match A06 driver to actual stall current. Not a basket motor selection.')
data['sources']=[x for x in data['sources'] if x['id']!='S6']
data['sources'].append({'id':'S19','label':'User screenshot 15 Oct 2026: Shopee seller 156048989 25GA-370, selected 12V 30RPM PHP 214 each; shipping section says PRE-ORDER ships in 5 days. Three units budgeted; torque/current/shaft/loaded-coil performance unverified.','url':url})
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

def current_totals(t):
    return t.replace('PHP 18,571.40','PHP 17,713.40',1).replace('PHP 17,377.40','PHP 16,519.40',1).replace('PHP 10,497.00','PHP 9,639.00',1)
p=root/'docs/BOM.md';t=current_totals(p.read_text()).replace('Step 25. Updated','Step 27. Updated',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A05 |'):
        lines[i]=f"| A05 | {motor['name']} | {motor['spec']} | 3 | 214.00 | 642.00 | [Shopee: 12V 30RPM 25GA-370]({url}); {motor['status']} [S19] | {motor['why']} |"
    elif line.startswith('- [S6]'):
        lines[i]=''
t='\n'.join(lines)+'\n'
t=t.replace('## Compatibility and selection checks\n\n','## Compatibility and selection checks\n\n- **A05 flavor-coil motor:** User confirms this role and supplies the selected 12 V/30 RPM 25GA-370 alternative. PHP 214 each × three = PHP 642, replacing the former PHP 1,500 SGM-370 candidate allowance (PHP 858 reduction). This records the new candidate and observed price, not proven loaded performance. Rated torque/duty, running/stall current, shaft/mounting and coil support/index-stop fit remain unresolved. A06 is still conditional on verified stall current below its stated limit; do not infer that from a 370 motor name. The screenshot shipping panel says pre-order despite “Ready Stock” in the title.\n\n',1)
t=t.replace('The earlier spreadsheet and detailed BOM are preserved',f'- [S19] [Shopee 25GA-370 motor]({url}): user screenshot dated 15 October 2026 selects **12V 30RPM at PHP 214**. Shipping panel: **pre-order, ships in 5 days**. Rated torque/current and loaded-coil fit unverified; delivery separate. Replaces A05\'s old candidate, not an additional set.\n\nThe earlier spreadsheet and detailed BOM are preserved',1)
p.write_text(t)

p=root/'PROJECT.md';t=p.read_text().replace('PHP 18,571.40','PHP 17,713.40',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Pending user-product review:**'):
        lines[i]='**Current A05 motor candidate:** User confirms flavor-coil role; prior candidate listing reported sold out. New [25GA-370 listing](https://shopee.ph/product/156048989/2380743022), selected **12 V/30 RPM at PHP 214 each**, quantity three, replaces the former A05 candidate allowance. Screenshot shows **pre-order, ships in 5 days**. Rated torque/duty, running/stall current, shaft/mounting and loaded-coil requirement remain open; A06 compatibility unverified. GA12-N20 is superseded and not purchased in parallel.'
p.write_text('\n'.join(lines)+'\n')

p=root/'docs/MOTOR_SELECTION.md';t=p.read_text().replace('Step 26 — 15 October 2026.**','Step 27 — 15 October 2026.**',1)
start=t.index('**Current prices and choice status:**');end=t.index('\n',start)
t=t[:start]+'**Current prices and choice status:** A05 now budgets three candidate **25GA-370 12 V/30 RPM** motors at **PHP 214 each (PHP 642)** from the user-supplied [Shopee listing](https://shopee.ph/product/156048989/2380743022). Selected variant/price are visible in the screenshot; shipping panel says **pre-order, ships in 5 days**, despite the “Ready Stock” title. This replaces the unavailable SGM-370 candidate and the superseded N20 inquiry; neither is bought alongside it. Rated torque/duty, running/stall current, shaft/mounting and loaded-coil turning requirement remain unverified. A06 estimated PHP 160 per channel (PHP 480 total) stays conditional on motor-current compatibility. No stepper set added in parallel.'+t[end:]
t=t.replace('## Pending GA12-N20 product review (Step 26, 15 October 2026)','## Superseded GA12-N20 review (Step 26, 15 October 2026)\n\n**Step 27 update:** User confirms this inquiry was for A05 and reports the earlier listing unavailable. The current candidate is now the 25GA-370 described above; the following N20 review is historical and is not the shopping instruction.',1)
t=t.replace('## Inputs needed before choosing a basket motor','## Current A05 acceptance checks (Step 27)\n\nThe selected 12 V rating matches the proposed nominal motor branch, subject to actual supplied ratings. Nominal 30 RPM corresponds to one revolution in two seconds; that does not prove packet dispensing time or loaded speed. A05 is still a brushed DC motor using the three coil index switches in A07. A06 provides one-direction switching, not guaranteed immediate braking, so reference stopping/coasting and one-packet release need validation. Faster nominal speed is not evidence of greater turning force. Check the 25 mm gearbox and actual shaft/coupling fit within the existing design; no support/mounting fit is established by the listing photo.\n\nObtain the selected-variant rated output torque/duty and running/stall current. Match them to the fully loaded coil and A06/diode/fuse/supply ratings. Prefer validating one suitably specified final-use unit before buying all three; retain that same unit in the finished machine. No separate practice motor is budgeted.\n\n## Inputs needed before choosing a basket motor',1)
p.write_text(t)

p=root/'docs/FRYER_ASSESSMENT.md';t=p.read_text().replace('Table A is PHP 10,497','Table A is PHP 9,639').replace('PHP 18,571.40','PHP 17,713.40').replace('PHP 17,377.40','PHP 16,519.40');p.write_text(t)

p=root/'PROGRESS.md';t=p.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 26');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 27 — A05 25GA-370 candidate linked/priced.** User confirms flavor-coil role. Selected 12 V/30 RPM PHP 214 each × three = PHP 642; torque/current/fit still pending. Screenshot says pre-order ships in five days. Table A PHP 9,639; Table B PHP 8,074.40; priced materials PHP 17,713.40 before quotes/fees. Final-use reuse, native clickable links, I2C LCD and timed cycle retained; no Phase 2 approval.'+t[end:]
t=current_totals(t)
log='''### A05 replacement candidate on 15 October 2026 (Step 27)

- User explicitly confirms A05 flavor-coil role, reports previous listing sold out and supplies different Shopee seller 156048989 listing. Screenshot selects 12V 30RPM 25GA-370 at PHP 214. Actual shipping panel says PRE-ORDER ships in 5 days, despite Ready Stock title; direct web access unavailable.
- Recorded replacement candidate in A05 with observed price and native clickable link; quantity three unchanged, PHP 642 subtotal. Removed old S6 source, added S19. GA12-N20 inquiry is superseded, not a parallel purchase. No claim the new motor is proven stronger or adequate solely because it is larger or named 370.
- Voltage/type fit the planned nominal 12 V brushed-DC architecture, but rated torque/duty, running/stall current, shaft/mounting and loaded-coil requirements remain open. A06 remains conditional on verified stall current; 30 RPM nominal two-second turn is not proven packet delivery or loaded speed. Keep index feedback and validate stopping/coasting.
- PHP 858 reduction from former three-at-PHP500 allowance: Table A PHP 9,639; Table B PHP 8,074.40; priced materials PHP 17,713.40 (without fryer PHP 16,519.40). Five material quotes and separate fees remain. Same selected motors will be reused in final product.
- Updated PROJECT, readable BOM, motor guide and fryer budget note. No purchase, physical test, firmware, install or phase transition performed.

'''
t=t.replace('### GA12-N20 candidate on 15 October 2026 (Step 26)',log+'### GA12-N20 candidate on 15 October 2026 (Step 26)',1);p.write_text(t)

with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    (root/'tmp/bom/before-a05-sheet.xml').write_bytes(z.read('xl/worksheets/sheet1.xml'))
    (root/'tmp/bom/before-a05-strings.xml').write_bytes(z.read('xl/sharedStrings.xml'))
print('A05 PHP214 x3=642; reduction PHP858; A PHP9639; priced materials PHP17713.40.')
