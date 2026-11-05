import copy
import json
import shutil
from pathlib import Path

root = Path('/home/hans/repos/fries-machine')
archive = root / 'docs/archive'
archive.mkdir(exist_ok=True)
for name, dest in [('BOM_Automatic_Fries_Machine.xlsx', 'BOM_Automatic_Fries_Machine.before-cleanup.xlsx'), ('docs/BOM.md', 'BOM.before-cleanup.md')]:
    target = archive / dest
    if not target.exists():
        shutil.copy2(root / name, target)
old = json.loads((root / 'tmp/bom/bom-data.json').read_text())
by_id = {x['id']: copy.deepcopy(x) for k in ['a', 'b'] for x in old[k]}
a = [by_id[i] for i in ['A1','A2','A3','A6','A8','A9','A10','A11','A12','A13','A14','A15','A17','A18','A19','B2','B3']]
for x in a:
    x['old_id'] = x['id']
    x['id'] = f'A{a.index(x)+1:02d}'
    x['why'] = {
        'A1': 'Reads the three flavor buttons and runs the cooking timer and motors. Without it, the automatic sequence cannot run.',
        'A2': 'Converts the temperature probe reading into data for the controller. Its bundled probe is for bench tests until oil suitability is documented.',
        'A3': 'Measures oil readiness with a documented oil/food-compatible probe. Without it, the controller cannot reliably distinguish warm-up from cooking temperature.',
        'A6': 'Runs the two proposed basket DC motors forward and reverse. Controller pins cannot supply motor power or reverse motors directly.',
        'A8': 'One motor rotates each flavor coil. Packet spacing and motor strength must be tested to dispense one packet per selection.',
        'A9': 'One power-switch circuit runs each flavor motor; its diode absorbs turn-off voltage spikes. Without suitable switching, motor current can damage the controller.',
        'A10': 'Four proposed basket end positions and three coil indexes tell the controller where motion should stop. These remain needed after removing potato detection.',
        'A11': 'One button per flavor dispenses the selected packet and requests cooking. The same buttons replace a separate ordinary start button.',
        'A12': 'Provides a latching emergency-stop input for the hardwired disconnect. It is reused in the final build; a button alone does not disconnect power.',
        'A13': 'Shows ready/busy/fault states and sounds completion or fault alerts. This provides basic operating feedback without an LCD.',
        'A14': 'Allows temporary low-current signal connections while learning and testing. It must not carry motor current or mains power.',
        'A15': 'Connects controller pins, buttons and module signals during testing. These thin wires are unsuitable for motor/heater power.',
        'A17': 'Reduces the selected DC supply to a regulated 5 V logic supply. Motors require their own power branch so they do not overload the controller.',
        'A18': 'Provides low-voltage branch fuses, holders and secure bench power terminals. Reuse rated parts in the final harness rather than buying them twice.',
        'A19': 'Provides filtering capacitors and required signal resistors. These help prevent motor noise from resetting or falsely triggering controls.',
        'B2': 'Two provisional actuators lift and rotate the real basket. Use them for cold tests and the final machine instead of buying separate practice motors.',
        'B3': 'One suitable supply powers motors and the 5 V converter in testing and the final machine. Its capacity must match starting/stall loads; no second bench adapter is budgeted.'
    }[x['old_id']]
by_old = {x['old_id']: x for x in a}
by_old['A6']['price'] = 268
by_old['A10']['qty'] = 7
by_old['A10']['spec'] = 'KW11-style roller microswitch candidate; 4 basket stops + 3 coil indexes; final mounting/quantity depends on existing mechanism'
by_old['A11']['qty'] = 3
by_old['A11']['name'] = 'Three flavor/start pushbuttons'
by_old['A11']['spec'] = 'Three normally-open momentary panel buttons, one per flavor; software accepts one selection per cooking cycle'
by_old['A14']['qty'] = 1
by_old['A18']['name'] = 'Reusable DC branch fuses and terminals'
by_old['B2']['spec'] = 'Provisional two 12 V geared DC actuators, one lift and one tilt; exact models depend on existing mechanism torque/speed and power-off retention; do not buy yet'
by_old['B2']['status'] = 'ESTIMATE; motor type/count and sizing pending'
by_old['B3']['name'] = 'Reusable enclosed DC motor power supply'
by_old['B3']['spec'] = 'Factory-wired enclosed 12 V DC supply/adapter with protected mains input; exact current/output connectors pending motor selection; ready-to-use housing required for beginner bench tests'
by_old['B3']['status'] = 'ESTIMATE; capacity/model pending'
by_old['B3']['store'] = 'Authorized PH power-supply supplier'
by_old['A8']['status'] = 'LISTED candidate; stock, 6/16 rpm discrepancy and stall current to confirm'
by_old['A17']['status'] = 'ESTIMATE at previous PHP 45 snapshot; current price not verified'
by_old['A15']['status'] = 'ESTIMATE at previous PHP 39 snapshot; mixed variants not rechecked'
by_old['A8']['spec'] = 'Candidate SGM-370, nominal 12 V, continuous rotation; listing disagrees between 6 and 16 rpm, so confirm variant, torque and stall current before loaded testing/purchase'
by_old['A19']['spec'] = 'Signal-filter and decoupling capacitors, 100 nF motor-noise caps, 470-1000 uF 25 V motor bulk caps and 470 uF 10 V logic bulk cap; excludes gate/diode parts already in A06 and indicator resistors in A10'

b = [by_id[i] for i in ['B1','B6','B7','B8','B10']]
for n,x in enumerate(b,1):
    x['old_id']=x['id']; x['id']=f'B{n:02d}'
    if x['old_id']=='B8':
        x['name']='Permanent DC wiring and moving cables'
        x['price']=1150
        x['spec']='Rated fixed/locking DC connectors and flexible moving sensor cables, ferrules, sleeves, clamps and strain relief; reuse A14 fuse holders/terminals where suitably rated'
        x['why']='Connects permanent electronics and supports repeated basket movement without pulling or breaking sensor wires. This replaces temporary jumpers for final power/moving connections.'
        x['status']='ESTIMATE: previous fixed harness 650 + moving cable 500'
    elif x['old_id']=='B10':
        x['spec']='Labels and external sensor mounting fixtures/hardware; excludes enclosure standoffs/glands in B03 and wiring sleeves/strain relief in B04; food-contact brackets belong to mechanical team'
        x['why']='Secures sensors and labels controls/wiring. Stable mounting and identification prevent misalignment and maintenance mistakes.'
    elif x['old_id']=='B6':
        x['spec']='FR4 solder board/terminal carrier and socket headers; reuse suitable A14 terminal blocks; motor power stays on driver terminals, no mains on this board'
        x['why']='Makes permanent soldered/terminal signal connections that resist vibration. Breadboard connections are only for the prototype.'
    elif x['old_id']=='B7':
        x['spec']='Approx. 250 x 200 x 100 mm flame-retardant low-voltage box, mounting plate, standoffs and glands; confirm fit/cooling; separate from B09 mains enclosure'
        x['why']='Protects low-voltage controls from oil splash and accidental contact. Driver cooling and separation from mains wiring must be maintained.'
    elif x['old_id']=='B1':
        x['why']='Provides the cooking tank, heater, thermostat and basket. Confirm independent overheat protection and fit before buying; an extra loose heater/thermostat is not needed.'

pending = [
('Fryer ON/OFF power contactor', 'Suitably rated appliance-load contactor; isolated low-voltage coil preferred; exact rating/model after fryer nameplate and external-control review', 'Lets a flavor-button request enable the fryer while its thermostat still regulates heat. No controller pin directly switches heater power.'),
('Hardwired heater/motor power disconnect', 'Independent contactor/disconnect arrangement operated by the reused E-stop, with deliberate restart; poles/quantity/load ratings pending electrical design', 'Removes hazardous heat/motion power independently of firmware. It is separate from normal heater-run switching.'),
('Contactor control/interface parts', 'Correctly rated low-voltage coil drivers, suppression and restart parts; reuse the selected DC supply where compatible; exact parts/quantity pending', 'Connects controller signals to power-switch coils without exceeding controller current limits. No duplicate DC supply is automatically added.'),
('Mains protection and installation materials', 'Covered mains enclosure/terminals, protective-earth connections, rated cord/glands and any missing isolator/overcurrent/leakage protection; verify existing appliance/site provision first', 'Contains and protects mains connections for the fryer and its power switches. Quote physical parts only here; all installation/inspection labor belongs in Table C.')]
for name,spec,why in pending:
    b.append(dict(id=f'B{len(b)+1:02d}',category='Required electrical materials',name=name,spec=spec,qty=1,unit='set',price=None,status='QUOTE NEEDED; not zero',source=None,store='PH electrical supplier; qualified school/electrician specification',why=why))
c=[
dict(id='C01',name='Qualified mains assembly and inspection',spec='Actual installation/earthing/protection/stop/restart and fryer-cutoff checks; no material cost included',qty=1,price=None,status='QUOTE NEEDED; school support may replace paid service if available',store='Qualified school supervisor / licensed electrician',why='Covers skilled work and physical inspection. The earlier PHP 2,500 was an unquoted allowance, not a mandatory fee.'),
dict(id='C02',name='Delivery/shipping',spec='Actual seller delivery charges after orders are grouped',qty=1,price=None,status='QUOTE NEEDED',store='Chosen suppliers/couriers',why='Delivery is a fee, not an electronic part. Do not charge it inside material unit prices again.'),
dict(id='C03',name='Student low-voltage assembly labor',spec='User plans to assemble low-voltage electronics personally',qty=1,price=0,status='DIY: no outside assembly fee budgeted',store='User',why='No paid low-voltage assembly service is being purchased. This does not assume professional mains work or inspection is free.')]

source_ids={x['source'] for x in a+b if x.get('source')}
sources=[copy.deepcopy(s) for s in old['sources'] if s['id'] in source_ids]
for s in sources:
    if s['id']=='S5': s['label']='Circuitrocks BTS7960, PHP 268 per board, rechecked 15 October 2026'
    if s['id']=='S6': s['url']='https://makerlab.ph/products/dc-worm-gear-motor-sgm-370-12v-16rpm'; s['label']='Makerlab SGM370, PHP 500 displayed; 6/16 rpm inconsistency and stock/current must be confirmed'
    if s['id']=='S8': s['label']='Earlier jumper-wire snapshot PHP 39; now treated as ESTIMATE because exact variants not rechecked'
    if s['id']=='S9': s['label']='Earlier LM2596 snapshot PHP 45; now treated as ESTIMATE because current listing not located'
data=dict(date='15 October 2026',a=a,b=b,c=c,sources=sources)
(root/'tmp/bom/lean-bom-data.json').write_text(json.dumps(data,indent=2))
totals={k:sum(x['qty']*x['price'] for x in data[k] if isinstance(x['price'],(int,float))) for k in ['a','b','c']}
partial=totals['a']+totals['b']
out=['# Automatic Fries Machine: Materials and Fees','', '**PHASE 1: MATERIALS BUYING, Step 13. Updated 15 October 2026.** Keep the PDF physical design unchanged. One flavor-button press dispenses its packet and starts the fryer/cooking process. After the requested ten-minute cooking interval, operate the existing basket lift/flip mechanism. Oil-preheat/timer timing remains pending clarification.','',
    'The three tables separate prototype materials, additional permanent materials and service fees. LISTED prices were observed from the linked sellers; ESTIMATE prices are unverified allowances. QUOTE NEEDED means the cost is unknown, not free. Motor/probe/fryer selections still need the checks below.','',
    f'**Priced materials subtotal: PHP {partial:,.2f}.** This includes the fryer and estimated motor/supply prices, but excludes four unquoted required electrical-material sets and unquoted fees. **Complete materials total and grand total: not yet available.** Without the fryer allowance, the priced materials subtotal is PHP {partial-5325:,.2f}.','',
    '## Table A: Prototype materials — reusable parts bought once','',
    'Initial logic tests use USB power. Reuse the selected real motors and factory-enclosed supply for subsequent cold tests; no hot oil or exposed mains connections in the breadboard prototype. Basket motors and the supply stay on purchase hold until sizing is established.','']
header='| # | Item name | Exact model/spec | Qty | Est. unit price (PHP) | Subtotal (PHP) | Where to buy (PH) | Why it is needed and how it makes the project work |'
def table(key):
    out.extend([header,'| --- | --- | --- | ---: | ---: | ---: | --- | --- |'])
    for x in data[key]:
        cost='Quote needed' if x['price'] is None else f"{x['price']:,.2f}"
        subtotal='Quote needed' if x['price'] is None else f"{x['qty']*x['price']:,.2f}"
        source=f" [{x['source']}]" if x.get('source') else ''
        out.append(f"| {x['id']} | {x['name']} | {x['spec']} | {x['qty']} | {cost} | {subtotal} | {x['store']}. {x['status']}{source} | {x['why']} |")
table('a')
out += ['',f"**Table A priced subtotal: PHP {totals['a']:,.2f}.** All prices are populated, but estimated selections are not approved purchases.",'', '## Table B: Additional permanent materials','', 'Buy these in addition to Table A; no reusable Table A item is charged again.','']
table('b')
out += ['',f"**Table B priced subtotal: PHP {totals['b']:,.2f}, plus four required material sets awaiting quotation.** Complete Table B total is unavailable.",'', '**Reused from prototype:** Controller/cable, temperature reader and suitable probe, two basket drivers/motors if validated, three coil motors/drivers, seven position switches, three flavor buttons, E-stop, indicators, DC supply, regulator, suitable fuses/terminals and support components. Breadboard/jumpers remain test equipment; permanent connections use Table B materials.','', '## Table C: Service and delivery fees','']
table('c')
out += ['', '**Priced fees: PHP 0.00 for DIY low-voltage labor, plus unquoted qualified service and delivery.** Total fees remain unknown. School help may reduce paid service costs; availability has not been confirmed.','', '## What was removed','',
'- Both infrared pairs: potato detection is no longer required; automatic packet-delivery confirmation is an optional extra. Coil index switches remain.',
'- LCD: no display was requested; LEDs/buzzer provide basic status. Remaining-time display is omitted.',
'- Two ACS712 current sensors: optional diagnostics. Retain position checks, timeouts, properly sized drivers/fuses and independent stop protection; timeouts do not directly measure a jam.',
'- Two practice basket motors and separate bench adapter: test and reuse the selected final parts instead.',
'- Extra ordinary ARM/start and cancel buttons: three flavor/start buttons cover normal selection; emergency stop remains separate. Any required hardwired restart control is part of the B08 quote, not assumed to be replaced safely by software.',
'- One spare breadboard and the proposed bag-detection switch: supervise loading and bag placement; automatic bag verification is omitted.',
'- The unitemized PHP 5,500 assembly: replaced by B06–B09 physical material requirements with actual quotes needed.',
'- The unquoted PHP 2,500 labor allowance: replaced by Table C qualified service, separately quoted. It is not moved into material prices.',
'- Automatic purchase of a PHP 700 guard interlock: determine whether the unchanged mechanism uses fixed guards or movable access. A movable guard may require a separately quoted interlock; guarding itself remains necessary.','',
'## Compatibility and selection checks','',
'- Retain the full-size 5 V Mega candidate for common headers and included USB cable; no Wi-Fi or extra I/O board. A cheaper Pro Mini is an optional substitution, not another purchase; verify headers/cable and delivered cost first.',
'- Plan 5 V logic, nominal 12 V motors and separate motor/logic power branches. The MAX6675 is used at 5 V with a compatible ungrounded K-type probe. The final power-input arrangement and regulator output must be verified in Phase 2.',
'- Reserve roughly 28 signals: temperature 3, basket drivers 8, coil outputs 3, position switches 7, flavor buttons 3, indicators 2 and stop/guard status up to 2. Exact wiring/pin assignment waits for selection. Controller pins carry signals only.',
'- Budget two geared DC basket axes provisionally; stepper motors are optional alternatives requiring matched stepper drivers. The existing chain/pivot/trajectory must establish actual motor count, output torque and speed. The PDF does not by itself prove transfer to the distant receiving area. An extra transfer axis is not priced; flag it explicitly if the existing mechanism needs one.',
'- 300 g is food only. Include basket/support mass, retained oil, friction and pivot/sprocket geometry. Require power-off load retention and appropriate guards; neither ordinary stepper holding torque nor a generic worm-drive claim establishes it.',
'- Match supply, motor drivers, fuses, wires/connectors and flavor flyback diodes to actual running/start/stall current. The BTS7960 label does not establish 43 A continuous module capability. IRLZ44N-style logic-level switching is provisional; diode/resistor ratings need motor data.',
'- Accept the complete fryer only after verifying basket/tank fit, nameplate, independent overheat protection and allowed external switching. Its thermostat still regulates heat; button start does not mean continuous full-power heating for ten minutes.',
'- Mains work requires qualified supervision/inspection. Table B contactor/disconnect/interface/protection sets contain materials only; Table C contains their labor. Reuse verified existing appliance/site protection and the selected DC supply without duplicate purchases.',
'- Preheated start versus warming cold oil before the ten-minute cooking interval remains an open question. Temperature monitoring is retained so this can be implemented without guessing.',
'', '## Excluded mechanical items and tools','',
'Frame, cutter, chain/sprockets, coils, funnel/bag holder, food-contact support, load retention and guards are the mechanical team scope. Food, oil and packaging are excluded. Borrow tools where available: soldering iron/stand, solder, cutter/stripper, screwdrivers and appropriate crimp tool. The user already owns multimeters/testing tools; no tool fee is silently added.','',
'## Price references','']
for s in sources: out.append(f"- [{s['id']}] [{s['label']}]({s['url']}).")
out += ['', 'The earlier spreadsheet and detailed BOM are preserved in `docs/archive/`. This revision replaces them as the current planning list. No physical build, firmware or phase transition has been performed. Review the remaining selections and quotes before approving Phase 2.','']
(root/'docs/BOM.md').write_text('\n'.join(out))
print(json.dumps({'tableA':totals['a'],'tableB_priced':totals['b'],'materials_priced':partial,'fees_priced':totals['c'],'unpriced_material_sets':4,'unpriced_fees':2}))
