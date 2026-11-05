import json
from pathlib import Path

root = Path('/home/hans/repos/fries-machine')
d = json.loads((root/'tmp/bom/bom-data.json').read_text())
items = {x['id']: x for x in d['a']+d['b']}
src = {x['id']: x for x in d['sources']}

explanations = {
'A1': ('Small computer that runs the machine.', 'It reads the potato sensor, keeps the cooking timer, commands motors and reads buttons. One controller serves the entire machine; you do not need a separate Arduino for each flavor. It does not produce the power that moves motors or heats oil. The selected full-size third-party Mega and USB cable were listed together at PHP 1,030 by e-Gizmo. This board model is a proposed choice; it is not the only possible controller.'),
'A2': ('Temperature-sensor reader board, sold with a basic test probe.', 'A K-type probe produces a very small electrical signal when its temperature changes. The MAX6675 board translates that signal into a number the controller can read. PHP 199 was the price of the listed module/probe bundle, marked pre-order. The bundled probe has not been verified for long immersion in food oil. Keep it for room-temperature or suitable warm-water tests; do not assume the chip measurement range is the probe rating.'),
'A3': ('Probe suitable for measuring the actual cooking oil.', 'This is the part immersed in the oil. It connects to the same A2 reader board, so A2 and A3 are not two separate oil-temperature systems. I allowed PHP 1,000 for a documented oil-immersion, food-contact K-type probe with suitable lead and mounting clamp. That was my allowance, not an actual supplier quote. A cheaper verified probe could replace it. If a module bundle includes a proven suitable probe, the extra probe purchase could be removed.'),
'A4': ('Two light beams that detect falling objects.', 'Each pair contains a light transmitter and receiver; the two devices together count as one pair. One pair crosses the potato chute and notices the first falling strips. The other crosses the flavor-packet exit and checks that a packet fell. Hence 2 pairs, not four independently priced sensors. The original budget uses PHP 277.43 per pair from DigiKey PH, excluding possible delivery/tax. Potato-drop detection is central to your request. Packet confirmation is an added feedback feature whose cost can be reviewed; it does not make an incorrectly spaced coil release exactly one sachet.'),
'A5': ('Small text screen.', 'It can show PREHEAT, READY, the remaining time and a fault message. A 16-by-2 display has two rows of up to sixteen characters each. The adapter on its back lets it use only two communication wires. PHP 150 was a Makerlab listing. A screen improves the demonstration and troubleshooting, but it is not what makes potatoes cook. A simpler indicator scheme is possible if the user approves that change.'),
'A6': ('Two power-driver boards for reversing basket motors.', 'The motor is the device that physically turns. A driver is the electronic circuit that supplies motor power under the controller\'s commands. One board controls up/down lift, the other controls rotation and return. Each board drives one reversible motor. The original allowance is 2 x PHP 267 = PHP 534. A recheck found PHP 268 per board, so the old total differs by PHP 2 if that current price is used. Final motor current and driver cooling still need verification.'),
'A7': ('Two small motors for a dry practice model.', 'These were included to test lift and rotation commands with a lightweight model before choosing the real motors. PHP 200 each was an estimate, not a selected purchase. They are not intended to move a real hot basket. This is extra test equipment, not a second pair of motors needed in the final machine. If the final motors are selected first and safely tested unloaded, this separate purchase may be unnecessary.'),
'A8': ('Three slow motors for the flavor spirals.', 'Each flavor coil needs its own motor so its button can move only that flavor. The listed candidate is an SGM-370 12 V motor at 6 revolutions per minute, priced at PHP 500 in Makerlab\'s motor collection. At nominal speed one full turn takes about ten seconds. Motor strength and loaded current have not been established for your coil. The budget includes three eventual motors, but testing one candidate before buying the other two prevents three unsuitable purchases.'),
'A9': ('Three electronic switches that power the flavor motors.', 'These proposed assemblies use a MOSFET, an electronic power switch, plus small supporting parts. Each controller output tells a switch when to power its flavor motor. A diode controls the electrical kick from the motor when it turns off. I allowed PHP 160 per complete channel, not PHP 160 for a bare transistor. The proposed diode/current path only applies if the selected motor meets the current limit; exact parts and their individual prices still need checking.'),
'A10': ('Eight small position or engagement switches.', 'The proposed count is 2 for lift top/bottom, 2 for basket upright/dump, 3 for flavor-coil indexes, and 1 for the bag holder: 2 + 2 + 3 + 1 = 8. A mechanism pushes the switch lever at a known position. This lets the program stop at an actual position instead of guessing from elapsed motor time. PHP 40 each was an estimate. A coil index switch is different from the A4 packet beam: it reports shaft position rather than proving a packet fell. The bag-holder switch is an added feature and needs a mechanism that genuinely checks bag installation.'),
'A11': ('Five ordinary operator buttons.', 'Three select the flavors. One arms/preheats the machine. One cancels/resets normal operation. The potato sensor still starts the cooking timer automatically when the machine is READY. PHP 35 per plain, non-illuminated panel button was an estimate. A normal cancel button acts through the program; it is not the same as the independent emergency stop.'),
'A12': ('One latching emergency-stop button.', 'Pressing this button should remove heater and motor power through a separate hardware circuit, even if the program stops responding. Latching means it stays operated until deliberately released. PHP 500 was an estimate for a documented suitable component, not a verified exact model. The button itself is only one part of the stop system: B4 contains the power-switching/control arrangement it operates. Mechanical restraint must keep the basket from falling when power is removed.'),
'A13': ('Sound alarm and red/green lights.', 'The buzzer can sound when cooking finishes or a fault occurs; the LEDs show simple status. I allowed PHP 100 for the small parts together, including the resistors and buzzer switching transistor. This is a bundle allowance rather than a shop-priced kit. It helps the operator notice the machine state; it does not provide emergency power isolation.'),
'A14': ('Two temporary connection boards.', 'A breadboard has holes with internal contacts that join inserted signal wires without solder. It is useful while learning and changing the circuit. Two boards were budgeted for space. PHP 91 each was a MakerPH listing. These are workshop/testing items; the permanent machine uses a soldered or terminal board. Motor power and household mains do not pass through these breadboards.'),
'A15': ('Three bundles of temporary signal wires.', 'The ends differ: male-male, male-female and female-female, so they can connect different module headers and sockets. Each bundle has forty separable conductors; three bundles were budgeted. Makerlab listed bundles from PHP 39, which may depend on variant. These thin removable connections are for bench signals, not full-size motor or heater power.'),
'A16': ('Small enclosed power adapter for testing.', 'It changes household electricity into a low-voltage 12 V DC supply, similar in purpose to an external adapter used by many appliances. The proposed 3 A output is for small dry tests with limited loads. PHP 350 was an estimate. It is separate from B3 because the final basket motors may need more current. Borrowing a suitable current-limited supply or testing with the selected final supply could avoid this purchase.'),
'A17': ('Small board that reduces 12 V to 5 V.', 'A buck converter reduces voltage. The proposed motors use 12 V, while the controller/display/sensors use 5 V. This board supplies the 5 V electronics from a suitable 12 V source. PHP 45 was a Makerlab listing. It does not power the fryer or make a small adapter capable of supplying a large motor. Its output must be measured and set before connecting 5 V devices.'),
'A18': ('Small bench protection and connection set.', 'A fuse breaks the circuit when excessive current flows, helping protect wires during a short or mistake. Terminals securely join wires. PHP 180 was an estimate for holders, fuses, covered terminals and reverse-polarity protection, not a price for one fuse. This set was reserved for the bench; B8 contains the separate full-size machine harness. The inventory can be consolidated if the same correctly rated parts are reused.'),
'A19': ('Small electrical support parts.', 'Resistors limit current or keep driver commands in a defined OFF state during startup. Capacitors store a little electrical energy and help reduce disturbances from motors. I allowed PHP 200 for assorted resistors and capacitors, not a single part. Their values and positions matter; they cannot be omitted simply because they are small. The precise shopping quantities remain to be finalized with the wiring design.'),
'A20': ('Two sensors that measure basket motor current.', 'One monitors the lift motor branch and one the rotation branch. A blocked motor can draw more current; these readings help the program detect a jam. PHP 180 each was an estimate. They are additional diagnostic/protection feedback, not a replacement for fuses, end switches or guarding. Their inclusion in a lean thesis design can be reviewed with the selected driver\'s current feedback and the actual risk assessment.'),
'B1': ('Complete manufactured electric fryer.', 'The candidate price covers the fryer product, including its basket and temperature control, not just a bare heater. Hanabishi\'s HFRY60SS listing shows PHP 5,325. It should not be counted again as a separate tank, heater and ordinary basket purchase. A suitable basket attachment may still require mechanical fabrication. The public listing does not establish the independent overheat cutoff required by the proposal; the accepted model remains unconfirmed. It is included because you asked to budget a complete fryer, although another team could own the purchase.'),
'B2': ('Two motors strong enough for the real basket.', 'One is intended to lift and one to rotate the basket. I allowed PHP 2,000 per motor, but no exact model has been selected and this is not a supplier quote. These replace the A7 small test motors. The full load includes the basket, bracket, 300 g fries and retained oil. The distance from the weight to a rotating pivot matters too. A mechanically combined lift/tilt arrangement could change motor count, but only after it is demonstrated.'),
'B3': ('Larger supply for the final motors.', 'The candidate supply converts mains into 12 V DC for the final machine; A17 then derives 5 V for the logic. PHP 1,500 was my unverified allowance for a genuine MEAN WELL LRS-150-12, not a current shop quote. Its output rating does not mean the machine always consumes that current. The correct supply depends on selected motors, startup demand and temperature. Its exposed terminals require professional enclosure/installation.'),
'B4': ('A proposed power-control box containing several parts.', 'This is the most confusing bundle in the original revision. PHP 5,500 was an allowance I created; it is not a quoted ready-made product. It was intended to cover power switches/contactors, an independent stop/restart arrangement, an isolated low-voltage control interface/supply, electrical protective devices, earthing terminals, mains wiring and their enclosure. A contactor is a power switch controlled by an electrical coil. Exact quantity, ratings and individual prices are not established. The estimate must be replaced by an itemized design/quote. Fryer thermostat control can remain internal to the fryer; an extra external heater-run control is a proposed feature that may be simplified after confirming the intended behavior. Safe emergency disconnection still needs provision.'),
'B5': ('Switch that detects an opened access guard.', 'A guard is a cover or barrier that keeps hands away from a moving mechanism or hot-oil hazard. The proposed interlock stops hazardous operation when an access guard opens. PHP 700 was an estimate for one suitable switch. This is not the same as a normal motor end-position microswitch. Whether a movable guard/interlock or a suitable fixed-guard arrangement is needed depends on the physical design; the exact component is not selected.'),
'B6': ('Permanent board or terminal carrier.', 'After a circuit works, its signal wiring needs secure permanent connections. Perfboard is a board with holes/pads onto which parts or wires can be soldered. A terminal carrier uses screw connections. PHP 350 was an allowance for the board, headers and low-voltage terminals. It replaces the temporary breadboards rather than adding another controller.'),
'B7': ('Protective box for the small electronics.', 'This box protects the controller/low-voltage drivers from oil, steam, loose metal and accidental touch. PHP 1,000 was an estimate for the enclosure and mounting items. B4 also contains a box, but for mains power parts: two separate compartments/boxes were proposed. One suitably divided enclosure may be more economical if electrical separation, cooling and maintenance are properly addressed. Do not assume an unverified enclosure size already fits the actual components.'),
'B8': ('Permanent electrical harness and branch protection.', 'A harness is the group of wires/connectors that joins the installed components. This allowance covers appropriately rated motor/logic wires, locking connectors, ferrules (metal sleeves on stranded wire ends), fuse holders and branch fuses. PHP 650 was an estimate for the set. These connections differ from thin temporary jumper wires. It excludes the mains wiring already allowed in B4.'),
'B9': ('Protection for wires near moving parts.', 'A moving basket repeatedly bends or pulls nearby cables. Flexible cable, clamps and sleeving guide the wiring and prevent the moving mechanism from pulling wires out. This is called strain relief. PHP 500 was an estimate for the set. Ordinary fixed wires can break under repeated bending. B8/B9 inventories must be itemized together to avoid paying twice for the same cable or clamp.'),
'B10': ('Small mounting and identification materials.', 'The allowance covers fasteners, labels, insulating heatshrink and sensor mounting hardware. Heatshrink is an insulating tube that becomes tight when heated. PHP 300 was an estimate for the set. Labels and secure mounting make a thesis demonstration and later fault-finding easier. Contents need to be checked against B6-B9 so shared mounting hardware is not counted twice.'),
'B11': ('Payment for qualified electrical work and checking.', 'This is labor, not a material. I allowed PHP 2,500 for installation/commissioning, but no electrician supplied a quote. It was separated from B4 materials/assembly to show the intended distinction; a future contractor\'s bundled quote might already include some labor and must be checked for overlap. School-provided qualified support could remove an external service payment, but the actual mains checks still need doing.')
}

groups = [
 ('Controller, temperature, sensing and controls', ['A1','A2','A3','A4','A5','A10','A11','A12','A13','A17','A19','A20']),
 ('Three flavor-coil drives', ['A8','A9']),
 ('Basket movement', ['A6','B2']),
 ('Bench-only equipment', ['A7','A14','A15','A16','A18']),
 ('Complete fryer', ['B1']),
 ('Final motor power and mains control', ['B3','B4','B5']),
 ('Permanent low-voltage construction', ['B6','B7','B8','B9','B10']),
 ('Electrical labor', ['B11'])
]

lines = ['''# The Fries-Machine BOM Explained

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
''']

for title, ids in groups:
    subtotal = sum(items[i]['qty']*items[i]['price'] for i in ids)
    lines.append(f'| {title} | {subtotal:,.2f} |\n')
lines.append('''| **Total** | **30,701.86** |

## Every component and price

All prices below are PHP. A1-A20 belong to the prototype table; B1-B11 are final additions/service. Listed prices are the workbook snapshot, with a recheck note where known to differ.

''')

for title, ids in groups:
    lines.append(f'### {title}\n\n')
    for id in ids:
        x=items[id]
        heading,body=explanations[id]
        total=x['qty']*x['price']
        pricekind='Listed-price candidate' if x['source'] else 'Unverified estimate'
        lines.append(f'**{id}: {x["name"]}**\n\n')
        lines.append(f'{heading} {body}\n\n')
        lines.append(f'**Price calculation:** {x["qty"]} {x["unit"]} x PHP {x["price"]:,.2f} = **PHP {total:,.2f}**. **Basis:** {pricekind}. **Original status:** {x["status"]}.\n\n')
        if x['source']:
            s=src[x['source']]
            lines.append(f'**Where the listed price came from:** [{x["store"]}]({s["url"]}).\n\n')
        else:
            lines.append('**Where the price came from:** my budgeting allowance. A store/supplier category in the BOM is a place to seek a quote, not evidence that the stated price is sold there.\n\n')

lines.append('''## Common questions answered

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

The existing BOM remains unapproved because of price and unsettled selections. This explanation is not a recommendation to purchase all thirty-one lines. Phase 1 continues. No hardware has been connected, no firmware written/flashed, and no packages installed. The next cost revision must clearly separate necessary functions, proposed convenience/feedback features, borrowed test equipment, actual final purchases and unquoted labor.
''')

assert len(explanations)==len(items)==31
seen=[i for _,ids in groups for i in ids]
assert len(seen)==len(set(seen))==31
assert round(sum(items[i]['qty']*items[i]['price'] for i in seen),2)==30701.86
(root/'docs/BOM_EXPLAINED.md').write_text(''.join(lines))
print('Saved plain-language explanation of all 31 items; functional totals reconcile to PHP 30,701.86.')
