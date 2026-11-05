from pathlib import Path
import json

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';d=json.loads(p.read_text())
d['a']=[x for x in d['a'] if x['id'] not in ['A02','A03']]
for x in d['a']:
    if x['id']=='A10':x['why']='Signals warm-up completion, timed cooking, cycle completion and faults. Warm-up completion is an elapsed-time signal, not a measured oil-temperature indication.'
d['sources']=[s for s in d['sources'] if s['id']!='S2']
p.write_text(json.dumps(d,indent=2))
a=sum(x['qty']*x['price'] for x in d['a']);b=sum(x['qty']*x['price'] for x in d['b'] if x['price'] is not None);total=a+b
seq='Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence.'
caveat='Five minutes is a trial setting, not proof that cold oil is ready. Validate warm-up/cooking durations for the actual oil fill, starting conditions, 300 g batch and loading sequence. If potatoes are in the oil during warm-up, they also heat during that period. Keep the manufactured fryer thermostat and verified independent overheat protection; timers do not regulate oil temperature or replace hardware power switching/stop protection. Retain position switches and motor drivers for basket/coil motion.'
p=root/'docs/BOM.md';text=p.read_text().replace('Step 14. Updated','Step 15. Updated',1)
old='One flavor-button press dispenses its packet and starts the fryer/cooking process. After the requested ten-minute cooking interval, operate the existing basket lift/flip mechanism. Oil-preheat/timer timing remains pending clarification.'
text=text.replace(old,seq)
text=text.replace('Shows ready/busy/fault states and sounds completion or fault alerts. This provides basic operating feedback without an LCD.','Signals warm-up completion, timed cooking, completion and faults. Warm-up completion is elapsed time, not measured oil readiness.')
lines=[line for line in text.splitlines() if not line.startswith('| A02 |') and not line.startswith('| A03 |') and not line.startswith('- [S2]')]
text='\n'.join(lines)+'\n'
text=text.replace('PHP 24,068.40',f'PHP {total:,.2f}').replace('PHP 18,743.40',f'PHP {total-5325:,.2f}').replace('PHP 11,863.00',f'PHP {a:,.2f}')
text=text.replace('Motor/probe/fryer selections','Motor/fryer selections').replace('Controller/cable, temperature reader and suitable probe,','Controller/cable,')
text=text.replace('- Plan 5 V logic, nominal 12 V motors and separate motor/logic power branches. The MAX6675 is used at 5 V with a compatible ungrounded K-type probe. The final power-input arrangement and regulator output must be verified in Phase 2.','- Plan 5 V logic, nominal 12 V motors and separate motor/logic power branches. Temperature regulation stays inside the complete fryer; the controller runs timed stages. Verify the actual regulator/board/driver power inputs in Phase 2.')
text=text.replace('- Reserve roughly 28 signals: temperature 3, basket drivers 8, coil outputs 3, position switches 7, flavor buttons 3, indicators 2 and stop/guard status up to 2.','- Reserve roughly 25 signals: basket drivers 8, coil outputs 3, position switches 7, flavor buttons 3, indicators 2 and stop/guard status up to 2.')
text=text.replace('- Preheated start versus warming cold oil before the ten-minute cooking interval remains an open question. Temperature monitoring is retained so this can be implemented without guessing.','- '+caveat+' Borrow an appropriate oil-rated reference thermometer for validation rather than purchasing an automatic temperature-monitoring module as a compulsory item.')
text=text.replace('## What was removed','## What was removed\n\n- External MAX6675 temperature reader and oil probe: the new controller sequence uses elapsed time. This does not remove the fryer’s internal thermostat or thermal protection. Historical price allowance removed: PHP 1,199. IDs A02/A03 are retired so existing part references remain stable.')
text=text.replace('## Table A:', '**Timer sequence:** '+caveat+'\n\n## Table A:',1)
p.write_text(text)
p=root/'PROJECT.md';text=p.read_text()
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- **What it should do:**'):lines[i]='- **What it should do:** Keep the physical PDF design unchanged. '+seq
    elif line.startswith('- **Required user features:**'):lines[i]='- **Required user features:** Approx. 300 g fries, manual cutting, three flavor/start buttons, timer-based warm-up then cooking, powered basket lift/drain/flip and complete protected fryer. Initial proposed durations 5 minutes warm-up + 10 minutes cooking. No potato-start detector or external automatic oil-temperature gate; keep position feedback and independent protection.'
    elif line.startswith('- **Updated heater-control scope:**'):lines[i]='- **Updated heater-control scope:** Button-operated heater permission remains. Controller advances through timed warm-up/cooking stages without measuring oil temperature. Retain fryer thermostat and verified independent cutoff. Five-minute warm-up is an initial adjustable proposal pending actual thermal/loading tests.'
    elif line.startswith('- **Budget limit (PHP):**'):lines[i]=f'- **Budget limit (PHP):** Economical thesis procurement; no fixed ceiling. Removing A02/A03 reduces the priced-material subtotal by PHP 1,199 to PHP {total:,.2f}, including fryer and estimates but excluding unresolved electrical/fee costs. Complete quotation remains unavailable.'
    elif line.startswith('- A valid flavor-button press'):lines[i]='- '+seq+' Ignore repeated/held selection presses while busy; proposed button behavior remains one packet/cycle per selection.'
    elif line.startswith('4. Electrical suppliers:'):lines[i]='4. Electrical suppliers: selected motor/driver/supply/coil ratings and itemized installation materials; probe is no longer a compulsory controller part.'
    elif line.startswith('6. Oil preheat state'):lines[i]='6. Validate warm-up/cooking durations, food-loading timing and heater behavior after discharge. Timed sequence selected; fixed five-minute warm-up is not yet thermally validated.'
    elif line.startswith('- **Current purchasing approach:**'):lines[i]='- **Current purchasing approach:** Reuse actual motors/supply. Optional external temperature monitoring, LCD and packet/bag/current sensing are omitted. Retain complete fryer thermostat/independent cutoff, position switches and hardware power stop.'
text='\n'.join(lines)+'\n';text=text.replace('## Open engineering inputs','- '+caveat+'\n\n## Open engineering inputs',1);p.write_text(text)
p=root/'PROGRESS.md';text=p.read_text();start=text.index('**PHASE 1: MATERIALS BUYING, Step 14');end=text.index('\n',start)
text=text[:start]+'**PHASE 1: MATERIALS BUYING, Step 15 — simplified to timed warm-up/cooking stages.** Flavor-button start, initial adjustable 5-minute warm-up then 10-minute cooking interval; thermostat/protection stays inside fryer. Removed compulsory external temperature reader/probe from controller BOM. No physical verification or Phase 2 approval.'+text[end:]
text=text.replace('**PHP 11,863**',f'**PHP {a:,.2f}**').replace('**PHP 24,068.40**',f'**PHP {total:,.2f}**').replace('**PHP 18,743.40**',f'**PHP {total-5325:,.2f}**')
text=text.replace('Keep position/temperature feedback,','Keep position feedback and fryer internal temperature regulation,').replace('preheat/timing is pending clarification.','timed warm-up followed by timed cooking is selected, with actual durations pending validation.')
text=text.replace('4. Exact oil-immersion food-contact ungrounded K-type probe and cable rating.','4. Access to an appropriate reference thermometer for validation; no compulsory external controller-temperature probe. Validate warm-up and recipe with actual loading conditions.')
entry='''### Timed sequence on 15 October 2026 (Step 15)

- User asks to enable heating on the flavor-button press, wait an initial proposed five minutes, then advance automatically by time. Interpret the next job as the existing ten-minute cooking interval; durations configurable. Initial elapsed time before lift is fifteen minutes, plus draining/motion.
- Controller performs elapsed-time sequencing. Intact manufactured fryer thermostat regulates heat; verified independent thermal cutoff and hardwired stop remain required. No extra timer module, separate temperature controller, firmware or physical build is needed/started in Phase 1.
- Removed A02 MAX6675 and A03 oil probe from compulsory purchases, making external temperature monitoring optional. Basket/coil position switches and drivers remain. Historical IDs retained to avoid changing other references.
- Five-minute warm-up is unverified. Check actual oil fill, starting temperature, 300 g batch, loading and repeat-cycle conditions during approved testing. If food is already in oil during warm-up, it is heating then too. No new automatic loading mechanism or frame change assumed.
- Priced Table A subtotal now PHP 10,664; priced materials PHP 22,869.40 with fryer, or PHP 17,544.40 excluding fryer. Reduced by the former PHP 1,199 temperature-reader/probe allowance; estimates and outstanding electrical/fee costs still prevent a complete total.
- Updated current sequence and BOM; worksheet calculations, missing-quote markers and saved line prices checked after changes. Physical cooking/motion and oil readiness remain untested. No packages installed, sudo, flashing or outside-project writes.

'''
text=text.replace('### B06–B09 parts listing',entry+'### B06–B09 parts listing',1)
text=text.replace('Clarify oil preheat state/timer timing, then obtain','Validate the proposed timed warm-up/cooking and loading sequence, then obtain')
p.write_text(text)
for name in ['docs/POWER_CONTROL_PARTS.md','docs/MOTOR_SELECTION.md','docs/BOM_EXPLAINED.md']:
    p=root/name;text=p.read_text();h,body=text.split('\n',1)
    note='**Current sequence override — Step 15:** '+seq+' '+caveat+' External MAX6675/probe purchases are removed from the current compulsory BOM; earlier references to a temperature gate are superseded.\n\n'
    p.write_text(h+'\n\n'+note+body.lstrip('\n'))
print(json.dumps({'tableA':a,'tableB_priced':b,'materials_priced':total,'removed_temperature_allowance':1199,'warmup_seconds':300,'cook_seconds':600}))
