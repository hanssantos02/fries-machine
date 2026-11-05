# The Fries-Machine BOM Explained

**Current requirements override — Step 12:** Keep the physical PDF design unchanged. A flavor-button press dispenses the selected packet and starts the fryer/cooking process; potato detection is no longer the start trigger. Remove that detector in the next buying revision, while retaining needed temperature/position feedback. Controller-operated heating permission must be specified; preheated start versus warm-up before the ten-minute cooking interval is pending clarification. A stepper is optional, not selected. See [current sequence and motor selection](MOTOR_SELECTION.md). Older tables/alternative totals below are historical unapproved estimates; the relocated-funnel partial budget does not apply to the unchanged design.

PHASE 1: MATERIALS BUYING, Step 8. Explanation date: 14 October 2026.

This explains **every line and price in the existing proposal**. It does not authorize buying everything, move the project to Phase 2, or create a revised cheaper quotation. The user has rejected the cost of the current proposal. Prices and totals below match the existing workbook snapshot so you can compare them directly; this is not a new current-price quote.

## What made the earlier version confusing

The proposal mixed ready-to-price components, unverified bundles, temporary equipment, final machinery parts and paid labor. It also described several engineering additions as if they were already confirmed user requirements. I should have identified these more clearly. A screen, packet-delivery confirmation, bag-holder sensing and motor-current readings are proposed features to review, not four independently requested functions. Choosing a different interface or supervision arrangement requires design review; it does not automatically remove the need for safe power handling and guarding.

Most importantly, the **PHP 30,701.86 total is not a verified amount that this machine necessarily costs**. The PHP 9,636.86 listed-price portion came from publicly visible listing prices; the other **PHP 21,065.00 consists of my unverified allowances**. Listed prices still need correct variants, availability, delivery and any taxes. A priced candidate motor is not automatically compatible with the real load.

## How the proposed machine works

1. An operator fills the accepted fryer to its marked oil level and deliberately starts preheating. Its own thermostat maintains the chosen temperature; a thermostat switches heat in response to temperature.
2. A separate temperature probe informs the controller when the oil is ready. A potato-drop sensor cannot tell whether the oil is hot enough.
3. You manually cut a measured batch. Potato strips interrupt a light beam in the chute. The first accepted drop while READY starts the requested configurable ten-minute timer. Later strips in the same batch do not restart it.
4. After cooking, the controller commands the basket lift, waits for its end-position signal, allows drainage over the tank, then commands the mechanically validated rotation/dump movement. The receiving funnel/bag remain mechanical-team parts.
5. Pressing a flavor button commands only that flavor motor. The spiral carries sachets forward. A position switch marks the intended full turn and a packet beam can confirm delivery. Coil spacing must physically prevent multiple packets.

The basket holds the food; the tank holds the oil. The basket moves, not the full tank of oil. Ten minutes is the requested initial setting, not a universally validated recipe. A dry demonstration verifies logic and movement; it does not verify actual cooking.

## How to read a price

- **Quantity:** how many pieces/pairs/sets are budgeted.
- **Unit price:** cost of one of those pieces/pairs/sets.
- **Subtotal:** quantity multiplied by unit price. For example, three motors at PHP 500 each give 3 x PHP 500 = PHP 1,500.
- **Listed:** a price was visible on a seller page during research. It is not a guaranteed delivered price or proof of compatibility.
- **Estimate/allowance:** I set aside this amount without a verified seller quote. It may be too high or too low. For bundle entries, I cannot honestly assign individual component prices until they are itemized.
- **HOLD:** do not order that selection yet; model, strength, power demand, safety feature or fit still needs checking.

An estimated range in the original BOM is also a planning assumption, not a market survey. The exact-looking two-decimal total comes from adding the chosen numbers; it does not make the estimates accurate.

## Why there are two buying tables

**Table A** contains the controller, sensors and drives used for the initial dry prototype, along with temporary test equipment. Most of its electronics are reused in the final machine.

**Table B** contains only additional final-build purchases plus a separately identified labor allowance. It does not mean buying another Arduino or another complete set of sensors.

Two deliberate replacements made the budget larger: two small A7 test motors plus two real B2 basket motors, and the A16 small test adapter plus the B3 final motor supply. These replacements can be avoided if final compatible parts are selected first and safely used for the dry tests. They are procurement choices, not a rule that a thesis needs duplicate motors and power supplies.

## All prices, regrouped by function

Each item appears once in the following groups. IDs match the original tables. These group totals reorganize the same budget; they are not extra amounts to add to Table A/B.

| Function | Existing proposal amount (PHP) |
| --- | ---: |
| Controller, temperature, sensing and controls | 4,633.86 |
| Three flavor-coil drives | 1,980.00 |
| Basket movement | 4,534.00 |
| Bench-only equipment | 1,229.00 |
| Complete fryer | 5,325.00 |
| Final motor power and mains control | 7,700.00 |
| Permanent low-voltage construction | 2,800.00 |
| Electrical labor | 2,500.00 |
| **Total** | **30,701.86** |

## Every component and price

All prices below are PHP. A1-A20 belong to the prototype table; B1-B11 are final additions/service. Listed prices are the workbook snapshot, with a recheck note where known to differ.

### Controller, temperature, sensing and controls

**A1: Mega 2560 R3 compatible board + data cable**

Small computer that runs the machine. It reads the potato sensor, keeps the cooking timer, commands motors and reads buttons. One controller serves the entire machine; you do not need a separate Arduino for each flavor. It does not produce the power that moves motors or heats oil. The selected full-size third-party Mega and USB cable were listed together at PHP 1,030 by e-Gizmo. This board model is a proposed choice; it is not the only possible controller.

**Price calculation:** 1 set x PHP 1,030.00 = **PHP 1,030.00**. **Basis:** Listed-price candidate. **Original status:** LISTED; confirm stock.

**Where the listed price came from:** [e-Gizmo, Manila](https://e-gizmo.net/gizmoshop/index.php?product_id=1395&route=product/product&tag=Arduino).

**A2: MAX6675 module with bench K-type probe**

Temperature-sensor reader board, sold with a basic test probe. A K-type probe produces a very small electrical signal when its temperature changes. The MAX6675 board translates that signal into a number the controller can read. PHP 199 was the price of the listed module/probe bundle, marked pre-order. The bundled probe has not been verified for long immersion in food oil. Keep it for room-temperature or suitable warm-water tests; do not assume the chip measurement range is the probe rating.

**Price calculation:** 1 set x PHP 199.00 = **PHP 199.00**. **Basis:** Listed-price candidate. **Original status:** LISTED; PRE-ORDER.

**Where the listed price came from:** [e-Gizmo](https://www.e-gizmo.net/gizmoshop/index.php?product_id=1295&route=product/product).

**A3: Oil-immersion K-type probe with clamp**

Probe suitable for measuring the actual cooking oil. This is the part immersed in the oil. It connects to the same A2 reader board, so A2 and A3 are not two separate oil-temperature systems. I allowed PHP 1,000 for a documented oil-immersion, food-contact K-type probe with suitable lead and mounting clamp. That was my allowance, not an actual supplier quote. A cheaper verified probe could replace it. If a module bundle includes a proven suitable probe, the extra probe purchase could be removed.

**Price calculation:** 1 set x PHP 1,000.00 = **PHP 1,000.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 800-1500; HOLD specification.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A4: IR through-beam emitter/receiver pairs**

Two light beams that detect falling objects. Each pair contains a light transmitter and receiver; the two devices together count as one pair. One pair crosses the potato chute and notices the first falling strips. The other crosses the flavor-packet exit and checks that a packet fell. Hence 2 pairs, not four independently priced sensors. The original budget uses PHP 277.43 per pair from DigiKey PH, excluding possible delivery/tax. Potato-drop detection is central to your request. Packet confirmation is an added feedback feature whose cost can be reviewed; it does not make an incorrectly spaced coil release exactly one sachet.

**Price calculation:** 2 pair x PHP 277.43 = **PHP 554.86**. **Basis:** Listed-price candidate. **Original status:** LISTED; tax/delivery may be extra.

**Where the listed price came from:** [DigiKey PH; element14 PH alternate](https://www.digikey.ph/en/products/detail/dfrobot/SEN0503/15283061).

**A5: 16x2 LCD with I2C backpack**

Small text screen. It can show PREHEAT, READY, the remaining time and a fault message. A 16-by-2 display has two rows of up to sixteen characters each. The adapter on its back lets it use only two communication wires. PHP 150 was a Makerlab listing. A screen improves the demonstration and troubleshooting, but it is not what makes potatoes cook. A simpler indicator scheme is possible if the user approves that change.

**Price calculation:** 1 pc x PHP 150.00 = **PHP 150.00**. **Basis:** Listed-price candidate. **Original status:** LISTED; confirm stock.

**Where the listed price came from:** [Makerlab PH](https://makerlab.ph/products/16x2-lcd-display-i2c-black-on-green).

**A10: Roller-lever microswitches**

Eight small position or engagement switches. The proposed count is 2 for lift top/bottom, 2 for basket upright/dump, 3 for flavor-coil indexes, and 1 for the bag holder: 2 + 2 + 3 + 1 = 8. A mechanism pushes the switch lever at a known position. This lets the program stop at an actual position instead of guessing from elapsed motor time. PHP 40 each was an estimate. A coil index switch is different from the A4 packet beam: it reports shaft position rather than proving a packet fell. The bag-holder switch is an added feature and needs a mechanism that genuinely checks bag installation.

**Price calculation:** 8 pc x PHP 40.00 = **PHP 320.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 30-70.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A11: Non-illuminated panel pushbuttons**

Five ordinary operator buttons. Three select the flavors. One arms/preheats the machine. One cancels/resets normal operation. The potato sensor still starts the cooking timer automatically when the machine is READY. PHP 35 per plain, non-illuminated panel button was an estimate. A normal cancel button acts through the program; it is not the same as the independent emergency stop.

**Price calculation:** 5 pc x PHP 35.00 = **PHP 175.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 25-60.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A12: Latching mushroom emergency stop**

One latching emergency-stop button. Pressing this button should remove heater and motor power through a separate hardware circuit, even if the program stops responding. Latching means it stays operated until deliberately released. PHP 500 was an estimate for a documented suitable component, not a verified exact model. The button itself is only one part of the stop system: B4 contains the power-switching/control arrangement it operates. Mechanical restraint must keep the basket from falling when power is removed.

**Price calculation:** 1 set x PHP 500.00 = **PHP 500.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 350-1000; HOLD documented component.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A13: Buzzer and status LED kit**

Sound alarm and red/green lights. The buzzer can sound when cooking finishes or a fault occurs; the LEDs show simple status. I allowed PHP 100 for the small parts together, including the resistors and buzzer switching transistor. This is a bundle allowance rather than a shop-priced kit. It helps the operator notice the machine state; it does not provide emergency power isolation.

**Price calculation:** 1 set x PHP 100.00 = **PHP 100.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 70-180.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A17: 12 V to 5 V buck converter**

Small board that reduces 12 V to 5 V. A buck converter reduces voltage. The proposed motors use 12 V, while the controller/display/sensors use 5 V. This board supplies the 5 V electronics from a suitable 12 V source. PHP 45 was a Makerlab listing. It does not power the fryer or make a small adapter capable of supplying a large motor. Its output must be measured and set before connecting 5 V devices.

**Price calculation:** 1 pc x PHP 45.00 = **PHP 45.00**. **Basis:** Listed-price candidate. **Original status:** LISTED.

**Where the listed price came from:** [Makerlab PH](https://makerlab.ph/collections/all?page=2).

**A19: Passive components and filtering kit**

Small electrical support parts. Resistors limit current or keep driver commands in a defined OFF state during startup. Capacitors store a little electrical energy and help reduce disturbances from motors. I allowed PHP 200 for assorted resistors and capacitors, not a single part. Their values and positions matter; they cannot be omitted simply because they are small. The precise shopping quantities remain to be finalized with the wiring design.

**Price calculation:** 1 set x PHP 200.00 = **PHP 200.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 150-350.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A20: DC motor branch current sensor modules**

Two sensors that measure basket motor current. One monitors the lift motor branch and one the rotation branch. A blocked motor can draw more current; these readings help the program detect a jam. PHP 180 each was an estimate. They are additional diagnostic/protection feedback, not a replacement for fuses, end switches or guarding. Their inclusion in a lean thesis design can be reviewed with the selected driver's current feedback and the actual risk assessment.

**Price calculation:** 2 pc x PHP 180.00 = **PHP 360.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 120-250; verify board rating.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Three flavor-coil drives

**A8: Slow geared DC motors for three flavor coils**

Three slow motors for the flavor spirals. Each flavor coil needs its own motor so its button can move only that flavor. The listed candidate is an SGM-370 12 V motor at 6 revolutions per minute, priced at PHP 500 in Makerlab's motor collection. At nominal speed one full turn takes about ten seconds. Motor strength and loaded current have not been established for your coil. The budget includes three eventual motors, but testing one candidate before buying the other two prevents three unsuitable purchases.

**Price calculation:** 3 pc x PHP 500.00 = **PHP 1,500.00**. **Basis:** Listed-price candidate. **Original status:** LISTED candidate; HOLD torque/stall data.

**Where the listed price came from:** [Makerlab PH Motors collection](https://makerlab.ph/collections/motors).

**A9: 5 V logic MOSFET motor driver assemblies**

Three electronic switches that power the flavor motors. These proposed assemblies use a MOSFET, an electronic power switch, plus small supporting parts. Each controller output tells a switch when to power its flavor motor. A diode controls the electrical kick from the motor when it turns off. I allowed PHP 160 per complete channel, not PHP 160 for a bare transistor. The proposed diode/current path only applies if the selected motor meets the current limit; exact parts and their individual prices still need checking.

**Price calculation:** 3 set x PHP 160.00 = **PHP 480.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 120-250; HOLD current match.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Basket movement

**A6: BTS7960 / IBT-2 bidirectional driver boards**

Two power-driver boards for reversing basket motors. The motor is the device that physically turns. A driver is the electronic circuit that supplies motor power under the controller's commands. One board controls up/down lift, the other controls rotation and return. Each board drives one reversible motor. The original allowance is 2 x PHP 267 = PHP 534. A recheck found PHP 268 per board, so the old total differs by PHP 2 if that current price is used. Final motor current and driver cooling still need verification.

**Price calculation:** 2 pc x PHP 267.00 = **PHP 534.00**. **Basis:** Listed-price candidate. **Original status:** LISTED; HOLD final motor match.

**Where the listed price came from:** [Circuitrocks PH](https://circuit.rocks/products/motor-large-current-driver-module-bts7960-43a).

**B2: Load-rated basket lift and rotation motors**

Two motors strong enough for the real basket. One is intended to lift and one to rotate the basket. I allowed PHP 2,000 per motor, but no exact model has been selected and this is not a supplier quote. These replace the A7 small test motors. The full load includes the basket, bracket, 300 g fries and retained oil. The distance from the weight to a rotating pivot matters too. A mechanically combined lift/tilt arrangement could change motor count, but only after it is demonstrated.

**Price calculation:** 2 pc x PHP 2,000.00 = **PHP 4,000.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 1500-4000 each; HOLD sizing.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Bench-only equipment

**A7: Small 12 V geared DC motion simulators**

Two small motors for a dry practice model. These were included to test lift and rotation commands with a lightweight model before choosing the real motors. PHP 200 each was an estimate, not a selected purchase. They are not intended to move a real hot basket. This is extra test equipment, not a second pair of motors needed in the final machine. If the final motors are selected first and safely tested unloaded, this separate purchase may be unnecessary.

**Price calculation:** 2 pc x PHP 200.00 = **PHP 400.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 150-300; verify variant.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A14: 830-point solderless breadboards**

Two temporary connection boards. A breadboard has holes with internal contacts that join inserted signal wires without solder. It is useful while learning and changing the circuit. Two boards were budgeted for space. PHP 91 each was a MakerPH listing. These are workshop/testing items; the permanent machine uses a soldered or terminal board. Motor power and household mains do not pass through these breadboards.

**Price calculation:** 2 pc x PHP 91.00 = **PHP 182.00**. **Basis:** Listed-price candidate. **Original status:** LISTED.

**Where the listed price came from:** [MakerPH](https://www.makerph.com/product/full-size-breadboard-830-holes/).

**A15: 40-pin jumper wire bundles**

Three bundles of temporary signal wires. The ends differ: male-male, male-female and female-female, so they can connect different module headers and sockets. Each bundle has forty separable conductors; three bundles were budgeted. Makerlab listed bundles from PHP 39, which may depend on variant. These thin removable connections are for bench signals, not full-size motor or heater power.

**Price calculation:** 3 bundle x PHP 39.00 = **PHP 117.00**. **Basis:** Listed-price candidate. **Original status:** LISTED FROM; variant price may differ.

**Where the listed price came from:** [Makerlab PH](https://makerlab.ph/collections/all).

**A16: Enclosed 12 V regulated wall adapter**

Small enclosed power adapter for testing. It changes household electricity into a low-voltage 12 V DC supply, similar in purpose to an external adapter used by many appliances. The proposed 3 A output is for small dry tests with limited loads. PHP 350 was an estimate. It is separate from B3 because the final basket motors may need more current. Borrowing a suitable current-limited supply or testing with the selected final supply could avoid this purchase.

**Price calculation:** 1 pc x PHP 350.00 = **PHP 350.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 250-500.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**A18: Bench fuse and terminal kit**

Small bench protection and connection set. A fuse breaks the circuit when excessive current flows, helping protect wires during a short or mistake. Terminals securely join wires. PHP 180 was an estimate for holders, fuses, covered terminals and reverse-polarity protection, not a price for one fuse. This set was reserved for the bench; B8 contains the separate full-size machine harness. The inventory can be consolidated if the same correctly rated parts are reused.

**Price calculation:** 1 set x PHP 180.00 = **PHP 180.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 120-300.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Complete fryer

**B1: Complete electric deep fryer with basket**

Complete manufactured electric fryer. The candidate price covers the fryer product, including its basket and temperature control, not just a bare heater. Hanabishi's HFRY60SS listing shows PHP 5,325. It should not be counted again as a separate tank, heater and ordinary basket purchase. A suitable basket attachment may still require mechanical fabrication. The public listing does not establish the independent overheat cutoff required by the proposal; the accepted model remains unconfirmed. It is included because you asked to budget a complete fryer, although another team could own the purchase.

**Price calculation:** 1 set x PHP 5,325.00 = **PHP 5,325.00**. **Basis:** Listed-price candidate. **Original status:** LISTED candidate; HOLD protection + fit.

**Where the listed price came from:** [Hanabishi official PH; Winland alternative](https://myhanabishi.com/products/deep-fryer-hfry-60ss).

### Final motor power and mains control

**B3: Genuine 12 V industrial power supply**

Larger supply for the final motors. The candidate supply converts mains into 12 V DC for the final machine; A17 then derives 5 V for the logic. PHP 1,500 was my unverified allowance for a genuine MEAN WELL LRS-150-12, not a current shop quote. Its output rating does not mean the machine always consumes that current. The correct supply depends on selected motors, startup demand and temperature. Its exposed terminals require professional enclosure/installation.

**Price calculation:** 1 pc x PHP 1,500.00 = **PHP 1,500.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 1200-2200; HOLD power budget.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B4: Enclosed heater and motion power-control assembly**

A proposed power-control box containing several parts. **That particular PHP 5,500 package is not established as necessary.** It was an allowance I created, not a quoted ready-made product. It combined optional controller-operated normal heater switching with independent stop/protection and their mounting/wiring. A contactor is a power switch controlled by an electrical coil. Exact quantity, ratings and individual prices are not established, so the bundle is not ready to order.

The complete fryer already has temperature control. A simpler proposed arrangement keeps the fryer intact: the operator turns it on and sets its temperature; its thermostat maintains preheat/cooking temperature; the controller detects potatoes, runs the timer and controls basket/flavor movement. This does not require a second temperature-control power system. If normal heater ON/OFF must also be automatic, specify that additional function explicitly and select a suitable power-switching interface. Do not silently drop automatic heater permission if the user requires it.

Some electrical functions remain necessary regardless of whether they occupy a separate box: independently stopping hazardous heater/motor power, adequate overload/leakage protection, protective grounding where required, insulated/covered terminals and secure cables. Existing suitable appliance/site protection may already perform some functions and must be verified rather than automatically bought again. A6/A9 motor drivers, B3 DC supply, B8 DC fuses/harness and A12 emergency-stop button are already priced separately. B4 is not a second motor driver or another motor supply, and these existing entries must not be counted twice. The right revision replaces this vague bundle with individually specified, actually priced parts; the replacement total is currently unknown.

**Price calculation:** 1 assembly x PHP 5,500.00 = **PHP 5,500.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 4000-8000; HOLD itemized quote.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B5: Safety guard interlock switch**

Switch that detects an opened access guard. A guard is a cover or barrier that keeps hands away from a moving mechanism or hot-oil hazard. The proposed interlock stops hazardous operation when an access guard opens. PHP 700 was an estimate for one suitable switch. This is not the same as a normal motor end-position microswitch. Whether a movable guard/interlock or a suitable fixed-guard arrangement is needed depends on the physical design; the exact component is not selected.

**Price calculation:** 1 set x PHP 700.00 = **PHP 700.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 500-1500; HOLD guard design.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Permanent low-voltage construction

**B6: Perfboard or Mega terminal carrier**

Permanent board or terminal carrier. After a circuit works, its signal wiring needs secure permanent connections. Perfboard is a board with holes/pads onto which parts or wires can be soldered. A terminal carrier uses screw connections. PHP 350 was an allowance for the board, headers and low-voltage terminals. It replaces the temporary breadboards rather than adding another controller.

**Price calculation:** 1 set x PHP 350.00 = **PHP 350.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 250-600.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B7: Separated electronics enclosure**

Protective box for the small electronics. This box protects the controller/low-voltage drivers from oil, steam, loose metal and accidental touch. PHP 1,000 was an estimate for the enclosure and mounting items. B4 also contains a box, but for mains power parts: two separate compartments/boxes were proposed. One suitably divided enclosure may be more economical if electrical separation, cooling and maintenance are properly addressed. Do not assume an unverified enclosure size already fits the actual components.

**Price calculation:** 1 set x PHP 1,000.00 = **PHP 1,000.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 700-1600.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B8: Permanent DC wire, connectors and branch fuses**

Permanent electrical harness and branch protection. A harness is the group of wires/connectors that joins the installed components. This allowance covers appropriately rated motor/logic wires, locking connectors, ferrules (metal sleeves on stranded wire ends), fuse holders and branch fuses. PHP 650 was an estimate for the set. These connections differ from thin temporary jumper wires. It excludes the mains wiring already allowed in B4.

**Price calculation:** 1 set x PHP 650.00 = **PHP 650.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 450-1000; HOLD final currents.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B9: Flex cable and strain-relief set**

Protection for wires near moving parts. A moving basket repeatedly bends or pulls nearby cables. Flexible cable, clamps and sleeving guide the wiring and prevent the moving mechanism from pulling wires out. This is called strain relief. PHP 500 was an estimate for the set. Ordinary fixed wires can break under repeated bending. B8/B9 inventories must be itemized together to avoid paying twice for the same cable or clamp.

**Price calculation:** 1 set x PHP 500.00 = **PHP 500.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 350-900.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

**B10: Panel hardware and identification kit**

Small mounting and identification materials. The allowance covers fasteners, labels, insulating heatshrink and sensor mounting hardware. Heatshrink is an insulating tube that becomes tight when heated. PHP 300 was an estimate for the set. Labels and secure mounting make a thesis demonstration and later fault-finding easier. Contents need to be checked against B6-B9 so shared mounting hardware is not counted twice.

**Price calculation:** 1 set x PHP 300.00 = **PHP 300.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 200-500.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

### Electrical labor

**B11: Electrical assembly and commissioning labor**

Payment for qualified electrical work and checking. This is labor, not a material. I allowed PHP 2,500 for installation/commissioning, but no electrician supplied a quote. It was separated from B4 materials/assembly to show the intended distinction; a future contractor's bundled quote might already include some labor and must be checked for overlap. School-provided qualified support could remove an external service payment, but the actual mains checks still need doing.

**Price calculation:** 1 service x PHP 2,500.00 = **PHP 2,500.00**. **Basis:** Unverified estimate. **Original status:** ESTIMATE 1500-4000; HOLD quote.

**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.

## Common questions answered

**Why not connect the motors directly to the Arduino?** Its pins send small control signals. A motor needs substantially more current, which is why it has a separate power supply and power driver. The heater uses household mains and has its own protected power path; it cannot be connected to an Arduino output.

**Are the driver boards and motors duplicates?** No. The motor moves the mechanism, while its driver supplies and switches motor power. A motor normally needs both.

**Why five final motors?** The proposed design has one basket lift, one basket rotation, and three independently selected flavor spirals: 1 + 1 + 3 = 5. The two practice motors make seven purchased motors in the original budget, but only five are intended for the final machine. A proven mechanical linkage can change the basket-motor count. A missing transfer movement could increase it. Neither change should be guessed from the drawing alone.

**Why two light-beam pairs rather than one sensor for every flavor?** One detects potatoes and one checks a shared packet exit. Three index switches identify the individual coil positions. Only one flavor motor runs at a time. This shared-beam arrangement assumes mechanics directs all flavor packets through the same sensing path.

**Why eight microswitches?** Four basket position signals, three coil index signals and one proposed bag-holder engagement signal. Their count follows the proposed mechanisms. They are different from the emergency stop and guard interlock.

**Does 300 g mean a cheap small motor is sufficient?** No conclusion yet. The motor also moves the basket and bracket. Strength depends on total load, lever distances, reduction gears and friction. Torque means turning strength; speed alone does not establish it. A motor family/model name without the exact gear ratio and ratings is not enough to buy confidently.

**Why a temperature probe if the fryer already has a thermostat?** The fryer's thermostat controls its own heating. The controller probe provides independent information for READY, display and fault logic. It could be unnecessary in a simpler manually supervised arrangement, but that changes the proposed automatic temperature verification. The probe does not replace the independent overheat cutoff.

**Why an external heater-control box if the fryer controls its own heat?** My proposal included controller-controlled heating permission and a hardware emergency disconnect. These are two functions. The thermostat can maintain oil temperature on its own; we should confirm whether the controller needs a separate heater-permission switch at all. The cost of the independent stop/protection arrangement still needs a real design and quote.

**Does the listed fryer price include the safety box?** No. B1 is the appliance. B4 is proposed external power control. A12 is the stop button. B5 is the guard switch. B11 is proposed labor. Their quoted scope must be checked to prevent duplicated parts/labor when a contractor provides a bundled service.

**Why did I say around PHP 5,300 for basic electronics earlier?** That was a specific subset: A1, A2, A4-A6, A8-A11, A13, A17 and A19, totaling PHP 5,287.86 at the old prices. It does not include the oil-rated probe, real basket motors, final supply, safe power assembly, enclosure/harness, labor or test equipment. It is not a complete working machine budget, and the subset still contains unverified allowances.

**What does 12 V / 5 V / 3 A mean?** V (volts) is the specified electrical supply level. A (amperes) is current. Different parts require the right voltage, and the supply/wires must support the current they draw. A 12 V adapter should not be connected to a 5 V sensor. A supply rated 3 A can provide up to its specified limit under its stated conditions; it does not force every load to draw 3 A. Motor startup can demand more current than normal rotation.

**What are the common pin names?** VCC is a module's positive supply connection at its specified voltage. GND is its low-voltage electrical reference/return. OUT or SIG carries information or a control signal. A switch's COM is its shared terminal, NO means open when not pressed, and NC means closed when not pressed. The actual board pin positions/order vary; these names are not a wiring instruction. Sensing/communication pins do not carry heater or motor power.

**What does the price omit?** Frame fabrication, manual cutter, chain/sprockets, shafts/bearings, food-contact brackets and chutes, motion restraint, guards themselves, bag holder, spiral racks/cams, consumable oil/potatoes/bags/packets, optional tools, shipping and possible taxes. Some required mechanical work is therefore outside this total, not free.

## Understanding the expensive portion

The biggest unquoted amounts are B4 external power/control assembly (PHP 5,500), B2 basket motors (PHP 4,000), B11 labor (PHP 2,500), B3 supply (PHP 1,500) and A3 oil probe (PHP 1,000). Those five entries total **PHP 14,500**, all unverified allowances. They should not be presented to the client as proven required prices.

Some of the required functions remain important, but the particular component choices, bundle structure, labor procurement and exact amounts are not settled. Seeking quotes or school-provided qualified support may lower cost. Using correctly selected final motors/supply in the prototype avoids buying redundant practice equipment. The full machine cost cannot be concluded from cheaper controller prices alone.

## Price recheck notes

On this explanation pass, e-Gizmo still displayed Mega PHP 1,030 and MAX6675 PHP 199 (pre-order); Makerlab's motor collection displayed the coil-motor candidate PHP 500; Hanabishi displayed HFRY60SS PHP 5,325. Circuitrocks displayed BTS7960 PHP 268 rather than the original PHP 267. The workbook snapshot and explanation totals are intentionally unchanged for comparison; using the rechecked driver price alone would add PHP 2, making the same-design total PHP 30,703.86. A proper cheaper revision should update all chosen parts together instead of mixing snapshots.

The remaining original listed-price references are documented in the main BOM; they have not all been independently refreshed during this explanation pass. Stock, variants and delivered prices still require checking. No electrician, motor-load or probe supplier quote has been received.

## Where the project stands

**Self-assembly clarification:** You can perform guided controller/sensor/motor-driver work on the isolated low-voltage side. Qualified school supervision or an electrician should handle/check household-mains installation, earthing and protective cutoffs before power-on; remote explanations cannot verify these physical protections. The PHP 2,500 labor entry can shrink or be replaced by no-charge qualified support, but this has not yet been priced. Removing that entire outside-payment allowance alone gives PHP 28,201.86 including the fryer; it does not remove the components in the PHP 5,500 power-control allowance. These are conditional cost scenarios, not a new approved BOM.

The existing BOM remains unapproved because of price and unsettled selections. This explanation is not a recommendation to purchase all thirty-one lines. Phase 1 continues. No hardware has been connected, no firmware written/flashed, and no packages installed. The next cost revision must clearly separate necessary functions, proposed convenience/feedback features, borrowed test equipment, actual final purchases and unquoted labor.
