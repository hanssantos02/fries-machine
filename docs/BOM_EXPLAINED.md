# How to read the simplified BOM

**Current sequence override — Step 15:** Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence. Five minutes is a trial setting, not proof that cold oil is ready. Validate warm-up/cooking durations for the actual oil fill, starting conditions, 300 g batch and loading sequence. If potatoes are in the oil during warm-up, they also heat during that period. Keep the manufactured fryer thermostat and verified independent overheat protection; timers do not regulate oil temperature or replace hardware power switching/stop protection. Retain position switches and motor drivers for basket/coil motion. External MAX6675/probe purchases are removed from the current compulsory BOM; earlier references to a temperature gate are superseded.

**PHASE 1: MATERIALS BUYING, Step 16 — 15 October 2026.** The current [BOM](BOM.md) and spreadsheet replace the earlier proposal. The PDF physical design remains unchanged; each flavor button requests its packet and the cooking process.

## Three tables with separate purposes

- **Table A — Prototype materials:** Parts bought once for learning/cold testing and reused in the final machine. It now includes the actual proposed basket motors and suitable enclosed supply, so a higher Table A subtotal does not mean duplicate purchases. Their exact models stay on hold until sizing is established.
- **Table B — Additional permanent materials:** The complete fryer, permanent circuit board, enclosure, final cables/mounting and required heater/stop switching parts. None of the reusable Table A items is charged again.
- **Table C — Fees:** Qualified mains assembly/inspection and delivery. Student low-voltage assembly has no outside labor fee budgeted because you plan to do it yourself. Professional inspection is not assumed free.

## Prices and unknown costs

**Quantity × unit price = row subtotal.** Material subtotals exclude fees. LISTED means a seller price was observed, not that compatibility has passed. ESTIMATE means an unverified planning allowance. QUOTE NEEDED means an unknown cost, not zero.

The headline is a **priced materials subtotal**. It includes the estimated real-motor and supply allowances. Required electrical materials and fees still awaiting quotations are visibly separate. The spreadsheet's complete total remains “Quote needed” until the remaining price cells are filled; entering one quote cannot hide the others. A genuine zero for DIY labor is allowed.

The old PHP 5,500 combined assembly and PHP 2,500 labor allowance were unquoted. They are no longer imposed as fixed costs. B06–B09 now list individual physical components. See [power-control parts](POWER_CONTROL_PARTS.md) for models, prices and sourcing conditions. C01 covers any actually paid qualified review/inspection/help; user assembly labor is zero. Quotes must identify exact parts and avoid repeated charges for existing supplies, drivers, fuses, terminals or enclosures.

## Why some sensors and motors remain

Potato detection is removed because the flavor button starts the cycle. Optional packet/bag/current sensing is removed. The I2C LCD is retained by explicit user request and shows selected flavor, warm-up/cooking countdowns and status. The operator observes packet delivery and bag readiness; automatic verification of these is omitted.

The fryer’s own thermostat controls oil temperature. The Arduino advances using elapsed time; the LCD shows that countdown without claiming measured oil readiness. Position switches identify basket endpoints and coil indexes. Motor drivers supply current that an Arduino pin cannot provide. Three coil motors operate the three dispensers; two provisional basket motors represent lift and rotation, pending the existing mechanism's requirements. A stepper remains a possible alternative, with different matched drivers; it is not an extra purchase.

No separate practice motors or second adapter are budgeted. Initially test logic through USB, then use the selected real motors and suitably enclosed supply in cold testing. Oil/mains work follows the later approved phase with qualified support.

The earlier detailed explanation is preserved in `docs/archive/BOM_EXPLAINED.before-cleanup.md`. It describes historical IDs/prices and should not be used as the current shopping list.
