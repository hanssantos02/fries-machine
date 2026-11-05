from pathlib import Path
import shutil

root=Path('/home/hans/repos/fries-machine')
p=root/'docs/BOM_EXPLAINED.md'
backup=root/'docs/archive/BOM_EXPLAINED.before-cleanup.md'
if not backup.exists(): shutil.copy2(p,backup)
p.write_text('''# How to read the simplified BOM

**PHASE 1: MATERIALS BUYING, Step 13 — 15 October 2026.** The current [BOM](BOM.md) and spreadsheet replace the earlier proposal. The PDF physical design remains unchanged; each flavor button requests its packet and the cooking process.

## Three tables with separate purposes

- **Table A — Prototype materials:** Parts bought once for learning/cold testing and reused in the final machine. It now includes the actual proposed basket motors and suitable enclosed supply, so a higher Table A subtotal does not mean duplicate purchases. Their exact models stay on hold until sizing is established.
- **Table B — Additional permanent materials:** The complete fryer, permanent circuit board, enclosure, final cables/mounting and required heater/stop switching parts. None of the reusable Table A items is charged again.
- **Table C — Fees:** Qualified mains assembly/inspection and delivery. Student low-voltage assembly has no outside labor fee budgeted because you plan to do it yourself. Professional inspection is not assumed free.

## Prices and unknown costs

**Quantity × unit price = row subtotal.** Material subtotals exclude fees. LISTED means a seller price was observed, not that compatibility has passed. ESTIMATE means an unverified planning allowance. QUOTE NEEDED means an unknown cost, not zero.

The headline is a **priced materials subtotal**. It includes the estimated real-motor and supply allowances. Required electrical materials and fees still awaiting quotations are visibly separate. The spreadsheet's complete total remains “Quote needed” until the remaining price cells are filled; entering one quote cannot hide the others. A genuine zero for DIY labor is allowed.

The old PHP 5,500 combined assembly and PHP 2,500 labor allowance were unquoted. They are no longer imposed as fixed costs. B06–B09 identify actual required electrical-material functions, and C01 records the separately quoted skilled work. Quotes must identify exact parts and avoid repeated charges for existing supplies, drivers, fuses, terminals or enclosures.

## Why some sensors and motors remain

Potato detection is removed because the flavor button starts the cycle. Optional packet/bag/current sensing and the LCD are also removed. The operator observes packet delivery and bag readiness; automatic verification of these is omitted.

Temperature feedback distinguishes oil readiness from warm-up. Position switches identify basket endpoints and coil indexes. Motor drivers supply current that an Arduino pin cannot provide. Three coil motors operate the three dispensers; two provisional basket motors represent lift and rotation, pending the existing mechanism's requirements. A stepper remains a possible alternative, with different matched drivers; it is not an extra purchase.

No separate practice motors or second adapter are budgeted. Initially test logic through USB, then use the selected real motors and suitably enclosed supply in cold testing. Oil/mains work follows the later approved phase with qualified support.

The earlier detailed explanation is preserved in `docs/archive/BOM_EXPLAINED.before-cleanup.md`. It describes historical IDs/prices and should not be used as the current shopping list.
''')
p=root/'PROJECT.md'; text=p.read_text().replace('Updated: 14 October 2026','Updated: 15 October 2026')
start=text.index('- **Budget limit (PHP):**');end=text.index('\n',start)
text=text[:start]+'- **Budget limit (PHP):** No fixed ceiling confirmed; economical thesis procurement required. Current simplified priced-material subtotal is PHP 19,988 including fryer, before four unquoted electrical-material sets and separately unquoted fees. This is not a complete machine quotation.'+text[end:]
text=text.replace('- `docs/BOM_EXPLAINED.md`: plain-language explanation of every existing BOM item and price, with proposed-feature and unverified-price distinctions.','- `docs/BOM_EXPLAINED.md`: short explanation of the three current tables, fees, reusable parts and unknown prices; prior detailed explanation archived.')
text=text.replace('- `docs/BOM.md`: two non-duplicating buying tables, architecture, audit, compatibility/pin and power budgets, alternatives, mechanical interfaces, tool list and sources.','- `docs/BOM.md`: two non-duplicating material tables plus a separate fee table, current requirements, removal list, compatibility checks and sources.')
text=text.replace('- `docs/BOM.md`: two non-duplicating buying tables, architecture, audit, compatibility/pin and power budget, sources and purchase holds.','- `docs/BOM.md`: two non-duplicating material tables plus a separate fee table, current requirements, removal list, compatibility checks and sources.')
text=text.replace('- `docs/BOM.md`: two non-duplicating buying tables, architecture, audit, compatibility/pin and power budgets, alternatives, mechanical interfaces, tool list and sources.','- `docs/BOM.md`: two material tables plus a separate fee table, removal list, compatibility checks and sources.')
text=text.replace('- `docs/BOM.md`: two non-duplicating buying tables, architecture, audit, compatibility/pin and power budget, sources and purchase holds.','- `docs/BOM.md`: two material tables plus a separate fee table, removal list, compatibility checks and sources.')
text=text.replace('- `docs/BOM.md`: two non-duplicating buying tables, architecture, audit, compatibility/pin and power budget, sources and purchase holds.','- `docs/BOM.md`: two material tables plus a separate fee table, removal list, compatibility checks and sources.')
# Existing wording varies between earlier project updates; replace the authoritative entry by prefix.
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- `docs/BOM.md`:'): lines[i]='- `docs/BOM.md`: two non-duplicating materials tables and a separate fee table; current priced subtotals, removed items, selection checks and sources.'
    elif line.startswith('- `BOM_Automatic_Fries_Machine.xlsx`:'): lines[i]='- `BOM_Automatic_Fries_Machine.xlsx`: current simplified three-table budget with editable price inputs and formulas; complete totals stay unavailable while quotes are missing.'
lines.insert(lines.index('## Current deliverables'),'- **Current purchasing approach:** Buy selected actual motors/supply once for cold testing and reuse in final build. Optional LCD, packet/bag/current sensors, practice motors, separate bench supply and extra ordinary controls are omitted; protection/temperature/position requirements remain.\n')
p.write_text('\n'.join(lines)+'\n')
p=root/'PROGRESS.md';text=p.read_text().replace('Updated: 14 October 2026','Updated: 15 October 2026',1)
a=text.index('**PHASE 1: MATERIALS BUYING, Step 12');b=text.index('\n',a)
text=text[:a]+'**PHASE 1: MATERIALS BUYING, Step 13 — simplified current BOM into two materials tables and one fee table.** Updated document and workbook for unchanged PDF design and flavor-button start. Priced materials total PHP 19,988; complete total unavailable while four electrical-material sets and two fees lack quotes. Motor/probe/fryer selection holds remain; no Phase 2 approval.'+text[b:]
a=text.index('## Deliverables and budget');b=text.index('## Validation status',a)
text=text[:a]+'''## Current deliverables and budget

- `docs/BOM.md` and `BOM_Automatic_Fries_Machine.xlsx`: simplified Table A prototype/reusable materials, Table B additional permanent materials and Table C fees. No reusable item charged twice and no fee mixed into material prices.
- Table A priced subtotal: **PHP 11,863**. Includes estimated real basket motors/supply once; exact selections not yet approved.
- Table B priced subtotal: **PHP 8,125**, plus four unquoted required electrical-material sets.
- Priced materials subtotal A+B: **PHP 19,988**, including the PHP 5,325 fryer candidate. Without that allowance: **PHP 14,663**.
- Table C: **PHP 0 DIY low-voltage outside labor**, plus unquoted qualified mains service and delivery. Fee total is unknown; no free professional service assumed.
- Complete materials/fees/grand totals: **Quote needed**, not zero. These partial subtotals include estimates and are not a final complete quotation or guaranteed savings claim.
- Earlier workbook, BOM and explanation preserved in `docs/archive/`; original PDF unchanged. Existing price references rechecked where accessible; previous unlocated jumper/buck prices explicitly estimates.

'''+text[b:]
text=text.replace('- Budget two basket axes (lift and rotation), two reusable reversible drivers, and two small bench-only simulator motors. Final basket actuators remain unselected until load/geometry data exists.','- Provisionally budget two geared DC basket axes and reusable drivers; select actual motors for cold tests/final reuse. Separate bench-only simulators are removed. Final sizing and the existing trajectory remain unresolved.')
text=text.replace('- Three flavor coils need geared continuous-rotation motors, drivers, index/home switches and packet-delivery feedback. Generic positional 180-degree servos are not chosen as direct coil drives.','- Three flavor coils need geared motors, drivers and index switches. Optional packet-delivery detector is removed; operator observes delivery. Ordinary positional servos are not selected as direct full-turn coil drives.')
text=text.replace('- Constrained sensing chutes, bag-holder sensing, motor current feedback, independent hardware stop/guard protection, load retention and qualified mains commissioning are included or assigned to the mechanical team.','- Potato/packet/bag/current sensing are omitted. Keep position/temperature feedback, independent power stop/protection, mechanical guarding/load retention and qualified mains inspection. Movable-guard interlock need/type is conditional on the actual guard.')
entry='''### BOM cleanup on 15 October 2026 (Step 13)

- Applied spreadsheet skill to the authorized restructuring; one current worksheet with three clearly named tables and an opening subtotal/unknown-cost summary.
- Removed two IR detector pairs, LCD, two current sensors, two practice basket motors, separate bench supply, two extra ordinary buttons, bag switch and spare breadboard. Removed unquoted PHP 5,500 bundle/2,500 labor allowance and automatic 700 guard-interlock purchase. Guarding remains required and a movable-guard interlock must be quoted if necessary.
- Moved actual basket motors and final suitable factory-enclosed supply into Table A for cold-test/final reuse. Retained full-size Mega/cable for familiar connectors. Two basket DC axes remain provisional, not an approved mechanism or mandatory stepper rejection.
- Replaced bundled electrical assembly with B06 normal fryer contactor, B07 independent power disconnect, B08 coil/restart interfaces and B09 protected mains installation materials. All four sets unquoted, material-only. Qualified work and shipping are separately unquoted C01/C02; DIY low-voltage outside fee C03 is zero.
- Combined fixed/moving DC harness allowances and removed duplicate fuse/terminal, driver-resistor/diode and enclosure/mounting kit scope. Updated references to new item numbers.
- Independently reconciled JSON/document/workbook subtotals. Tested price-edit recalculation, one supplied quote with other quotes still missing, complete temporary quotes and restoration to blank unknown prices. No formula errors found. Rendered/reviewed all changed table sections and summary; saved file retains formulas and unknown-cost markers. Excel desktop execution is not tested.
- Updated PROJECT and replaced BOM_EXPLAINED with a short current guide; preserved prior documents/workbook in archive. No work outside project, installations, sudo, flashing or physical build.
- Preheat/timer clarification, load/trajectory/motor/driver/supply sizing, accepted probe/fryer and actual electrical/fee quotes remain before purchasing approval. No budget ceiling inferred and no Phase 2 transition.

'''
text=text.replace('### Updated user requirements on 14 October 2026',entry+'### Updated user requirements on 14 October 2026')
text=text.replace('7. Guard arrangement and truthful bag-holder engagement sensing.','7. Actual fixed/movable guarding and load retention; quote an interlock if the accepted guard requires it. Operator bag placement replaces proposed bag sensing.')
p.write_text(text)
print('Updated current explanation, PROJECT and PROGRESS; archived prior explanation.')
