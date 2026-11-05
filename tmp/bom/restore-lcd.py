import json
from pathlib import Path

root=Path('/home/hans/repos/fries-machine')
p=root/'tmp/bom/lean-bom-data.json';d=json.loads(p.read_text())
x=dict(id='A18',category='Display',name='16x2 LCD with I2C backpack',spec='Makerlab MLE00659 candidate, HD44780-compatible 16x2 LCD with PCF8574 I2C adapter; intended 5 V logic supply; confirm actual backpack voltage/address before wiring',qty=1,unit='pc',price=150,status='LISTED PHP 150; listing shows sold out, confirm stock',source='S4',store='Makerlab PH',why='Shows selected flavor, warm-up and cooking countdowns, basket/cycle status and faults. Reuse this same display in the final machine; elapsed warm-up is not a measured temperature reading.')
assert not any(r['id']=='A18' for r in d['a'])
d['a'].append(x)
s=dict(id='S4',label='Makerlab MLE00659 16x2 LCD with I2C adapter, PHP 150, rechecked 15 October 2026; confirm stock',url='https://makerlab.ph/products/16x2-lcd-display-i2c-black-on-green')
d['sources'].append(s);p.write_text(json.dumps(d,indent=2))
a=sum(r['qty']*r['price'] for r in d['a']);b=sum(r['qty']*r['price'] for r in d['b'] if r['price'] is not None);material=a+b
p=root/'docs/BOM.md';t=p.read_text().replace('Step 15. Updated','Step 16. Updated',1)
row=f"| {x['id']} | {x['name']} | {x['spec']} | 1 | 150.00 | 150.00 | {x['store']}. {x['status']} [S4] | {x['why']} |"
anchor='**Table A priced subtotal:';i=t.index(anchor);t=t[:i]+row+'\n\n'+t[i:]
t=t.replace('PHP 10,664.00',f'PHP {a:,.2f}').replace('PHP 22,869.40',f'PHP {material:,.2f}').replace('PHP 17,544.40',f'PHP {material-5325:,.2f}')
t=t.replace('**Reused from prototype:** Controller/cable,','**Reused from prototype:** I2C LCD, controller/cable,')
t=t.replace('- LCD: no display was requested; LEDs/buzzer provide basic status. Remaining-time display is omitted.','- **LCD retained by explicit user request:** A18 provides warm-up/cooking countdown, selected flavor and status. It is included once in Table A and reused in the final build.')
t=t.replace('- Reserve roughly 25 signals: basket drivers 8, coil outputs 3, position switches 7, flavor buttons 3, indicators 2 and stop/guard status up to 2.','- Reserve roughly 27 signals: LCD I2C 2, basket drivers 8, coil outputs 3, position switches 7, flavor buttons 3, indicators 2 and stop/guard status up to 2.')
t=t.replace('## Compatibility and selection checks','## Compatibility and selection checks\n\n- The LCD uses two I2C signal lines (SDA and SCL), plus supply and ground. Use a verified 5 V backpack with the 5 V Mega; no separate level shifter is required for that combination. Scan its actual address and include backlight current in the logic power budget during approved testing. No temperature value is displayed without a temperature sensor.')
t=t.replace('The earlier spreadsheet and detailed BOM are preserved',f"- [S4] [{s['label']}]({s['url']}).\n\nThe earlier spreadsheet and detailed BOM are preserved",1)
p.write_text(t)
p=root/'PROJECT.md';t=p.read_text();lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- **Required user features:**'):lines[i]=line+' Keep one 16x2 I2C LCD for countdowns, flavor and status.'
    elif line.startswith('- **Budget limit (PHP):**'):lines[i]=f'- **Budget limit (PHP):** No fixed ceiling; economical thesis procurement. Restored user-requested I2C LCD at PHP 150; current priced-material subtotal PHP {material:,.2f}, before outstanding electrical/fee quotes. No complete quotation yet.'
    elif line.startswith('- **Current purchasing approach:**'):lines[i]='- **Current purchasing approach:** Reuse actual motors/supply and one I2C LCD. External temperature monitoring and packet/bag/current sensing remain optional and omitted. Retain complete fryer thermostat/cutoff, position switches and hardware stop.'
lines.insert(lines.index('## Open engineering inputs'),'- **LCD content:** Selected flavor, warm-up/cooking countdown, lift/drain/flip/return/completion and faults. Use elapsed-time wording for warm-up; no claim of measured oil readiness or temperature.\n')
p.write_text('\n'.join(lines)+'\n')
p=root/'PROGRESS.md';t=p.read_text();start=t.index('**PHASE 1: MATERIALS BUYING, Step 15');end=t.index('\n',start)
t=t[:start]+'**PHASE 1: MATERIALS BUYING, Step 16 — I2C LCD restored at explicit user request.** One 16x2 I2C display in Table A, reused in final machine. Timed sequence retained; external temperature reader/probe omitted. Priced materials PHP 23,019.40 before outstanding quotes/fees. No Phase 2 approval.'+t[end:]
t=t.replace('**PHP 10,664.00**',f'**PHP {a:,.2f}**').replace('**PHP 22,869.40**',f'**PHP {material:,.2f}**').replace('**PHP 17,544.40**',f'**PHP {material-5325:,.2f}**')
entry='''### LCD restoration on 15 October 2026 (Step 16)

- User explicitly requires retaining the I2C LCD. Restored one 16x2 PCF8574-backpack candidate as A18, bought once and reused; other item IDs retained.
- Rechecked Makerlab MLE00659 PHP 150. Listing shows sold out; confirm stock before purchasing. Candidate 5 V logic/backpack and I2C address must be verified during approved testing.
- Display planned for selected flavor, adjustable warm-up/cooking countdowns, basket/cycle status and faults. No temperature display or measured-ready claim without a sensor. Timed warm-up/cooking and unchanged PDF design retained.
- Table A priced subtotal PHP 10,814; Table B priced subtotal unchanged PHP 12,205.40; priced materials PHP 23,019.40 (PHP 17,694.40 without fryer). Five unresolved electrical entries and separate unquoted fees remain; complete total unavailable.
- Updated BOM/workbook, current explanation and PROJECT. Checked recalculation, saved values/formulas and changed display/summary/removal-note views. No firmware, wiring, physical build, installs, flashing or phase transition.

'''
t=t.replace('### Timed sequence on',entry+'### Timed sequence on',1)
p.write_text(t)
p=root/'docs/BOM_EXPLAINED.md';t=p.read_text().replace('Optional packet/bag/current sensing and the LCD are also removed.','Optional packet/bag/current sensing is removed. The I2C LCD is retained by explicit user request and shows selected flavor, warm-up/cooking countdowns and status.').replace('**PHASE 1: MATERIALS BUYING, Step 13','**PHASE 1: MATERIALS BUYING, Step 16');p.write_text(t)
print(json.dumps({'LCD_qty':1,'LCD_unit':150,'tableA':a,'tableB':b,'priced_materials':material}))
