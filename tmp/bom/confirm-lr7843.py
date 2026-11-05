from pathlib import Path
import json
from zipfile import ZipFile

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';data=json.loads(p.read_text())
driver=next(x for x in data['a'] if x['id']=='A06')
assert driver['price']==160 and not any(x['id']=='A06.1' for x in data['a'])
driver.update(name='LR7843 MOSFET flavor-motor driver modules',unit='pc',price=50,spec='Selected LR7843 module. Seller documents 3 V/5 V signal input, HIGH=ON, LOW=OFF, PWM and DC motor start/stop. Verify actual input current, safe reset/OFF, motor-current/thermal suitability and circuit before final acceptance. Loose terminals/headers pictured',status='SCREENSHOT: selected LR7843 PHP 50 each, 15 Oct 2026; delivery extra. Seller documents 5 V control. Motor-current/protection validation pending',store='Shopee PH / fulabs.ph',why='One Arduino-commanded module switches each flavor motor. Replaces the old discrete MOSFET/gate assembly, not an additional driver. Buy three once and reuse in final build. Any missing motor flyback protection is listed separately in A06.1.')
diodes={'id':'A06.1','category':'Flavor-motor protection','name':'Motor flyback diodes if missing from module circuit','spec':'One correctly rated motor freewheeling diode per coil motor if no suitable onboard path is established. Select reverse-voltage, current/surge and switching ratings from actual 12 V motor/PWM data; exact part pending. Existing sub-2 A stall screening retained until revised','qty':3,'unit':'pc','price':None,'status':'QUOTE NEEDED; verify module protection first and buy only missing diodes','source':None,'store':'PH electronics supplier / Alexan / Raon; exact rated part/price pending','why':'Provides the motor turn-off current path to limit voltage spikes. Module description does not establish a suitable onboard flyback path; do not assume the MOSFET body diode is sufficient. This replaces the protection formerly included in A06 allowance; no duplicate set.'}
data['a'].insert(data['a'].index(driver)+1,diodes)
caps=next(x for x in data['a'] if x['id']=='A15')
caps['spec']='Signal-filter and decoupling capacitors, 100 nF motor-noise caps, 470-1000 uF 25 V motor bulk caps and 470 uF 10 V logic bulk cap; excludes module gate circuitry in A06, motor flyback diodes in A06.1 and indicator resistors in A10'
source=next(x for x in data['sources'] if x['id']=='S20')
source['label']='User screenshots 15 Oct 2026: fulabs.ph selected LR7843 PHP 50; description supports 3 V/5 V signals, HIGH=ON, LOW=OFF, PWM and DC motors. Terminals/headers loose. Motor-current rating, actual safe OFF and suitable flyback path still need validation.'
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

p=root/'docs/BOM.md';t=p.read_text().replace('Step 29. Updated','Step 30. Updated',1)
t=t.replace('PHP 17,713.40','PHP 17,383.40',1).replace('PHP 16,519.40','PHP 16,189.40',1).replace('PHP 9,639.00','PHP 9,309.00',1)
t=t.replace('excludes 5 unquoted electrical-material entries','excludes 6 unquoted material entries',1)
t=t.replace('**Table A priced subtotal: PHP 9,309.00.** All prices are populated, but estimated selections are not approved purchases.', '**Table A priced subtotal: PHP 9,309.00, plus A06.1 diode pricing/need check.** Estimated selections and load-dependent parts are not approved purchases.')
lines=t.splitlines();out=[]
for line in lines:
    if line.startswith('| A06 |'):
        out.append(f"| A06 | {driver['name']} | {driver['spec']} | 3 | 50.00 | 150.00 | [Shopee: selected LR7843]({driver['product_url']}); {driver['status']} [S20, S21] | {driver['why']} |")
        out.append(f"| A06.1 | {diodes['name']} | {diodes['spec']} | 3 | Quote needed | Quote needed | {diodes['store']}. {diodes['status']} | {diodes['why']} |")
    elif line.startswith('| A15 |'):
        parts=line.split('|');parts[3]=' '+caps['spec']+' ';out.append('|'.join(parts))
    elif line.startswith('- **A06 module candidate:**'):
        out.append('- **A06 selected module:** New screenshots select LR7843 at PHP 50 and explicitly advertise 3 V/5 V signal input, high-level start, low-level stop and PWM control for DC devices. This supports the required Mega control interface, subject to actual input current and reset/OFF checks. Three modules cost PHP 150. The former PHP 160/channel DIY/protection allowance is removed. Any missing rated motor flyback diodes are separately quoted in A06.1; they are not assumed included or free. Actual motor running/stall current, board thermal performance and suitable flyback path remain acceptance checks. Loose terminal/header pieces may need soldering. No duplicated discrete MOSFET/gate circuit is budgeted. IC current figures are not whole-board ratings or proof of system isolation.')
    elif line.startswith('- [S20]'):
        out.append('- [S20] [Shopee fulabs.ph LR7843 module](https://shopee.ph/product/1367148707/41455009761): user screenshots 15 October 2026 select **LR7843, PHP 50** and document **3 V/5 V control, HIGH=ON, LOW=OFF, PWM and DC motor switching**. Loose connectors pictured; motor-current/thermal and protection checks remain. Diodes are separately listed if absent; shipping separate.')
    else:out.append(line)
t='\n'.join(out)+'\n';p.write_text(t)

p=root/'PROJECT.md';t=p.read_text().replace('PHP 17,713.40','PHP 17,383.40',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- **Flavor driver candidate (A06):**'):
        lines[i]='- **Flavor driver (A06):** User selects [fulabs.ph LR7843](https://shopee.ph/product/1367148707/41455009761) at **PHP 50 each × three = PHP 150**. Seller description documents 3 V/5 V input, HIGH=ON, LOW=OFF and PWM for DC devices. Suitable control architecture; actual input current/reset OFF, motor running/stall/thermal match and circuit protection still need validation. A06 is module-only; A06.1 separately quotes three suitable motor flyback diodes if the module lacks a verified path. Former PHP 160/channel complete-set allowance removed; no duplicate discrete MOSFET/gate parts. Loose connectors may need soldering.'
p.write_text('\n'.join(lines)+'\n')

p=root/'docs/MOTOR_SELECTION.md';t=p.read_text().replace('Step 29 — 15 October 2026.**','Step 30 — 15 October 2026.**',1)
t=t.replace('A06 estimated PHP 160 per channel (PHP 480 total) stays conditional on motor-current compatibility.', 'A06 now prices three selected LR7843 modules at PHP 50 each (PHP 150); any missing motor flyback diodes are separately quoted in A06.1. Motor-current/protection suitability remains pending.')
start=t.index('## A06 control-input MOSFET module candidate (Step 29)');end=t.index('## Inputs needed before choosing a basket motor',start)
t=t[:start]+'''## A06 selected LR7843 module (Step 30)

New user screenshots visibly select **LR7843 at PHP 50** and provide seller text documenting **3 V/5 V signal inputs, high-level start, low-level stop, PWM regulation and DC motor start/stop**. This resolves the previous missing selected price and advertised signal-compatibility information. Three modules cost **PHP 150**, before delivery; each operates one flavor motor through the existing index-switch control sequence.

The seller's optocoupler-isolation claim is not independent proof of the complete circuit's isolation. [Infineon's IRLR7843 specification](https://www.infineon.com/part/IRLR7843) describes the chip, not a tested current capacity for the whole seller board. Verify actual input current within the Mega pin budget, OFF behavior during reset/disconnection, motor running/stall current, module heating and suitable turn-off protection during the approved later phase. No high-frequency PWM performance or motor-current capability is established by the text alone. Terminal blocks and headers appear loose and may need soldering.

**Protection is separate:** The screenshots do not establish a suitable onboard motor flyback path. A06.1 therefore reserves one appropriately rated external diode per motor if missing, quantity three, with price/model pending real motor/current/circuit data. Do not treat a MOSFET body diode or input optocoupler as proof of motor flyback protection. Do not buy duplicate external diodes if a suitable onboard path is verified. No wiring or physical test has begun.

**Budget treatment:** A06 now lists module-only PHP 50 × three = PHP 150. The former PHP 160/channel complete assembly allowance is removed, including its discrete MOSFET/gate parts. A06.1 keeps the remaining conditional protection visible as **Quote needed**, not zero. Priced subtotal falls by PHP 330, but this is not a guaranteed full-channel saving because the diode cost is still unquoted. No additional prototype-only drivers are bought.

'''+t[end:];p.write_text(t)

p=root/'docs/FRYER_ASSESSMENT.md';t=p.read_text().replace('Table A is PHP 9,639','Table A is PHP 9,309').replace('PHP 17,713.40','PHP 17,383.40').replace('PHP 16,519.40','PHP 16,189.40').replace('Five material entries and separate fees still need quotes/need checks','Six material entries (including conditional motor flyback diodes) and separate fees still need quotes/need checks');p.write_text(t)

p=root/'PROGRESS.md';t=p.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 29');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 30 — LR7843 selected price/control specs recorded.** A06 PHP 50 each × three = PHP 150; seller documents 3 V/5 V input, high ON/low OFF and PWM. A06.1 separately lists three rated motor flyback diodes if absent, quote needed. Former PHP 160/channel allowance removed. Table A PHP 9,309; Table B PHP 8,074.40; priced materials PHP 17,383.40 before six unquoted materials/fees. Actual motor/current/protection validation pending; clickable links/LCD/reuse retained; no Phase 2 approval.'+t[end:]
t=t.replace('Table A priced subtotal: **PHP 9,639.00**. Includes estimated real basket motors/supply once; exact selections not yet approved.', 'Table A priced subtotal: **PHP 9,309.00**, plus A06.1 diode pricing/need check. Includes estimated real basket motors/supply once; exact selections not yet approved.',1)
t=t.replace('Priced materials subtotal A+B: **PHP 17,713.40**','Priced materials subtotal A+B: **PHP 17,383.40**',1).replace('Without fryer allowance: **PHP 16,519.40**','Without fryer allowance: **PHP 16,189.40**',1)
log='''### LR7843 selected price and description on 15 October 2026 (Step 30)

- New screenshots select LR7843 at PHP 50 and provide seller text: 3 V/5 V inputs, high-level start, low-level stop, PWM and DC motor switching. This resolves the previous selected-price and advertised signal-interface gaps. Treat as seller documentation, not tested isolation/current/thermal/safe-OFF performance.
- Replaced A06 complete-set PHP 160/channel allowance with module-only PHP 50 × three = PHP 150. Added A06.1 quantity three suitable flyback diodes if no valid onboard path is established, price/model Quote needed. No duplicated discrete MOSFET/gate assembly; A15 exclusions updated to avoid rebuying diode/gate pieces.
- Priced subtotal decreases PHP 330: Table A PHP 9,309; Table B PHP 8,074.40; priced materials PHP 17,383.40 (without fryer PHP 16,189.40). This is not a guaranteed PHP 330 complete-channel saving because diode cost is now separately unquoted. Six material entries and two fee entries remain unquoted/conditional.
- Actual input current/reset OFF, selected motor running/stall load, module heating and suitable flyback path remain later acceptance checks. Loose connectors may need soldering. No unsupported assumption that body diode/opto provides motor protection or that 161 A applies to this board.
- Updated PROJECT, BOM, motor/fryer guides and source S20. Builder unknown-cost count now includes both material tables; native hyperlink assertions resolve item rows by ID to accommodate the added row. No firmware, physical tests, package install or phase transition.

'''
t=t.replace('### A06 control-input MOSFET module on 15 October 2026 (Step 29)',log+'### A06 control-input MOSFET module on 15 October 2026 (Step 29)',1);p.write_text(t)
print('A06 PHP50 x3=150; A06.1 diodes quoted separately. A PHP9309; B PHP8074.40; priced materials PHP17383.40; six material quotes pending.')
