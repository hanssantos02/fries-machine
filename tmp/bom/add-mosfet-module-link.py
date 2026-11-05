from pathlib import Path
from zipfile import ZipFile
import json

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';data=json.loads(p.read_text())
item=next(x for x in data['a'] if x['id']=='A06')
assert item['price']==160 and item['qty']==3
url='https://shopee.ph/product/1367148707/41455009761'
item.update(
    name='Arduino-controlled MOSFET flavor-motor driver sets',
    spec='Candidate LR7843 control-input module replacing the discrete MOSFET/gate circuit, plus one suitable motor flyback diode per channel if missing. Verify 5 V input thresholds/current, 12 V load switching, safe OFF, motor stall current and thermal limits. Retain sub-2 A stall screening until revised',
    store='Shopee PH / fulabs.ph module candidate; protection parts separately sourced',
    status='PHP 160 per COMPLETE CHANNEL is retained ESTIMATE, not module price. Screenshot headline PHP 49, no variant selected. LR7843 price/input/protection and motor match pending',
    source='S20; S21',
    product_url=url,
    why='One Arduino-commanded switch runs each flavor motor until its coil index is reached. Module replaces the old discrete MOSFET/gate parts, not an additional driver. Keep correctly rated inductive turn-off protection; MOSFET body diode alone does not establish motor flyback protection.',
)
data['sources'].extend([
    {'id':'S20','label':'User screenshot 15 Oct 2026: fulabs.ph LR7843/AOD4184/FR120N control-input modules, PHP 49 headline with no variant selected. LR7843 is candidate only; 5 V input behavior, assembled accessories and motor protection unverified. A06 retains PHP 160 complete-channel allowance.','url':url},
    {'id':'S21','label':'Infineon IRLR7843 manufacturer reference: 30 V logic-level MOSFET, low on-resistance characterized at 4.5 V gate drive. IC specification does not prove seller-module input threshold, continuous current or isolation/protection.','url':'https://www.infineon.com/part/IRLR7843'},
])
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

p=root/'docs/BOM.md';t=p.read_text().replace('Step 27. Updated','Step 29. Updated',1)
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A06 |'):
        lines[i]=f"| A06 | {item['name']} | {item['spec']} | 3 | 160.00 | 480.00 | [Shopee: LR7843 candidate]({url}); {item['status']} [S20, S21] | {item['why']} |"
t='\n'.join(lines)+'\n'
t=t.replace('## Compatibility and selection checks\n\n','## Compatibility and selection checks\n\n- **A06 module candidate:** Added user LR7843/AOD4184/FR120N listing; nominate LR7843 for further checking because the genuine IRLR7843 is a logic-level part specified at 4.5 V gate drive. This does not prove the optocoupler/module input threshold or isolation. Confirm documented 5 V Arduino control, input current/polarity/fail-off behavior, 12 V motor operation, motor stall current, thermal capacity and actual assembly. The screenshot shows loose terminals/headers; do not assume pre-soldered delivery. Verify a suitable flyback path and add one rated external diode per motor if absent; a MOSFET body diode or optocoupler alone is not proof of motor protection. No separate old discrete MOSFET/gate circuit is bought alongside a validated module. The retained **PHP 160/channel is a complete driver/protection estimate**, while PHP 49 is an unselected module headline; no price reduction is claimed yet.\n\n',1)
t=t.replace('IRLZ44N-style logic-level switching is provisional; diode/resistor ratings need motor data.', 'LR7843-module logic input and switching/protection are provisional; diode and driver ratings still need actual module/motor data.')
t=t.replace('The earlier spreadsheet and detailed BOM are preserved',f'- [S20] [Shopee fulabs.ph MOSFET modules]({url}): user screenshot 15 October 2026, PHP 49 headline with LR7843/AOD4184/FR120N variants unselected. Candidate LR7843; selected price, input and protection pending. PHP 160 remains the complete-channel estimate, not this module\'s quote.\n- [S21] [Infineon IRLR7843](https://www.infineon.com/part/IRLR7843): logic-level IC / 4.5 V gate-drive reference; not proof of seller module ratings, isolation or input compatibility.\n\nThe earlier spreadsheet and detailed BOM are preserved',1)
p.write_text(t)

p=root/'PROJECT.md';t=p.read_text();t=t.replace('- **Heating architecture:**','- **Flavor driver candidate (A06):** [fulabs.ph MOSFET module listing](https://shopee.ph/product/1367148707/41455009761), nominate LR7843 provisionally. Screenshot PHP 49 has no variant selected. Retain PHP 160 per complete channel (module and any missing suitable flyback/protection pieces) as an estimate until prices/specs are confirmed. Need documented 5 V signal input/safe OFF, 12 V motor operation, load/current/thermal compatibility and flyback path. Module replaces discrete MOSFET/gate parts; no duplicate driver purchase. Loose connectors pictured may need soldering.\n- **Heating architecture:**',1);p.write_text(t)

p=root/'docs/MOTOR_SELECTION.md';t=p.read_text().replace('Step 28 — 15 October 2026.**','Step 29 — 15 October 2026.**',1)
t=t.replace('This uses A05 motors, A06 DC switching circuits and the three coil switches included in A07.', 'This uses A05 motors, A06 Arduino-controlled switching sets (now a candidate module plus necessary protection) and the three coil switches included in A07.',1)
t=t.replace('## Inputs needed before choosing a basket motor','## A06 control-input MOSFET module candidate (Step 29)\n\nThe new [fulabs.ph listing](https://shopee.ph/product/1367148707/41455009761) has LR7843, AOD4184 and FR120N options. Unlike the preceding knob controller, the pictured boards expose separate control-input pads, so this is a relevant module architecture for A06. Nominate **LR7843** as a candidate, subject to the actual module schematic/specifications and load checks. [Infineon](https://www.infineon.com/part/IRLR7843) characterizes the genuine IRLR7843 MOSFET at 4.5 V gate drive; that does not establish the marketplace optocoupler-input thresholds or current requirements. Nor does the IC\'s 161 A headline establish a safe current for the whole board, terminals, PCB or wiring.\n\nConfirm the control input accepts the Mega\'s 5 V output within its pin-current budget, turns reliably OFF at reset/no signal and supports the required switching behavior. Check actual 12 V motor compatibility, running/start/stall current and thermal margins. Seller claims of isolation must be checked against the actual circuit; an optocoupler does not by itself establish complete system isolation or mains suitability. This is for low-voltage motors only. Loose terminal/header parts are pictured, so confirm whether soldering is required.\n\n**Retain motor turn-off protection:** A suitable flyback path is required for each motor. Do not assume the MOSFET body diode, an input optocoupler or a diode visible elsewhere on the board supplies the required motor flyback path. Verify schematic/continuity in the approved later phase and buy only any missing correctly rated external diode(s). Match the diode and driver to the real motor data. See the [manufacturer functional example](https://wiki.dfrobot.com/dfr0457), which separately calls for a freewheeling diode on inductive loads.\n\n**Price and BOM:** A06 now includes the clickable candidate link; three final-use channels remain. PHP 49 is an unselected listing headline. PHP 160 per channel / PHP 480 total is explicitly retained as the estimated **complete channel** budget including necessary protection, not presented as the board price. Confirm selected LR7843 price and any missing protection parts before replacing that estimate with itemized observed costs. A validated module replaces the old discrete MOSFET/gate circuit, rather than being bought in addition. No savings are booked yet.\n\n## Inputs needed before choosing a basket motor',1)
p.write_text(t)

p=root/'PROGRESS.md';t=p.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 28');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 29 — A06 control-input MOSFET module candidate linked.** LR7843 nominated provisionally; module 5 V input/current/safe OFF, motor stall current and flyback protection need verification. PHP 49 is an unselected module headline; retain PHP 160 estimated complete channel × three. Priced materials unchanged PHP 17,713.40 before quotes/fees. Native clickable links, final-use reuse, I2C LCD and timed cycle retained; no Phase 2 approval.'+t[end:]
log='''### A06 control-input MOSFET module on 15 October 2026 (Step 29)

- User supplies fulabs.ph module link/screenshot with LR7843, AOD4184 and FR120N options, PHP 49 and no selected variant. Boards show separate control pads; terminal blocks/headers pictured loose. Direct page inaccessible. No assertion that input thresholds, isolation, current capacity or motor protection are established by the photo.
- Added LR7843 as provisional A06 candidate and clickable supplier/source links. Infineon genuine IRLR7843 primary data supports logic-level gate operation at 4.5 V; explicitly distinguishes MOSFET gate characteristics from the module's optocoupler-input requirements. No transfer of 161 A IC number to whole-board current rating.
- Need 5 V logic input/current and safe OFF behavior, 12 V load compatibility, actual motor running/stall current/thermal margin and suitable flyback path. External rated motor diode remains needed if not already supplied by the actual circuit. Do not assume MOSFET body diode/opto is sufficient; retain existing sub-2 A stall screening until design revised.
- A06 keeps three complete-channel sets at PHP 160 estimated each (PHP 480), now explicitly module plus any missing protection. PHP 49 is not booked as the full-channel cost or as a confirmed selected LR7843 price. No old discrete MOSFET/gate assembly bought additionally; actual module/protection costs must replace the estimate when known. No total change.
- Updated PROJECT, BOM and motor guide; no purchase, wiring, firmware, installation or phase transition.

'''
t=t.replace('### A06 manual PWM controller review on 15 October 2026 (Step 28)',log+'### A06 manual PWM controller review on 15 October 2026 (Step 28)',1);p.write_text(t)

with ZipFile(root/'BOM_Automatic_Fries_Machine.xlsx') as z:
    (root/'tmp/bom/before-a06-sheet.xml').write_bytes(z.read('xl/worksheets/sheet1.xml'))
    (root/'tmp/bom/before-a06-strings.xml').write_bytes(z.read('xl/sharedStrings.xml'))
print('A06 candidate link added; original PHP160 complete-channel estimate retained, totals unchanged.')
