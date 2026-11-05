import json
from pathlib import Path

root = Path('/home/hans/repos/fries-machine')
data = json.loads((root / 'tmp/bom/bom-data.json').read_text())
sources = {s['id']: s for s in data['sources']}
a = sum(x['qty'] * x['price'] for x in data['a'])
b = sum(x['qty'] * x['price'] for x in data['b'])
money = lambda n: f'{n:,.2f}'

intro = '''# Phase 1: Materials Buying - Automatic Fries Machine

**Review date:** 14 October 2026 (Philippines). **Status:** revised planning BOM for approval, with explicitly identified purchase holds. **Batch:** approximately 300 g fries. **Scope:** electronics, electrical actuators, protection and a complete-fryer allowance requested by the user. Mechanical fabrication is excluded.

The existing Excel BOM has been revised in place. The unmodified original is saved under `docs/archive/BOM_Automatic_Fries_Machine.original.xlsx`. The reference drawing and `AGENTS.md` are unchanged. This document supplies the beginner explanations and limitations behind the spreadsheet; it is not a hot-oil assembly guide.

## What the machine needs to do

The manual cutter on the left remains manual. Strips pass through a **through-beam sensor**: one device sends invisible infrared light across a narrow chute, and a receiver detects when a potato interrupts it. The strips fall into a perforated **basket** in preheated oil. The basket, not the tank containing the oil, is raised and rotated. Moving or tipping the whole oil tank is not part of this design.

The controller starts the requested 600-second cook timer on the first valid drop while READY. Several strips from the same potato must count as one batch, not several starts. The later strips must not reset the timer. A short loading window must be established for the actual cutter, and another potato must not be added mid-cycle. A sensor does not weigh the batch: the operator still measures approximately 300 g. No load cell has been added without a weighing requirement.

Preheating must happen **before** the first potato is loaded. ARM/PREHEAT grants heater permission; the fryer's thermostat automatically cycles its heater to maintain temperature. Detecting a drop starts the cooking sequence, not ten minutes of uncontrolled continuous heater power. The controller must reject starts below the validated ready temperature or during movement/faults.

At the end of cooking, remove heater permission, lift the basket, pause to drain over the tank, then rotate along a mechanically verified path to the right funnel and paper bag. Check that the bag holder is engaged before dumping. Return the basket to its upright/home position before lowering it. The emergency stop and guard protection must remove heater/motor energy independently of the program, with deliberate manual restart. Stopping power must not allow the basket to fall.

Each flavor button turns one **vending spiral** (the spring-shaped coil in the drawing) through one indexed revolution. A cam and home switch identify a completed turn. A beam across the shared packet exit checks for delivery. The coil spacing and packet supports must physically separate sachets; electronics cannot guarantee one packet if the mechanical design lets two fall together. A held button must not keep vending. One flavor motor operates at a time. A missed packet, unexpected extra packet or index timeout produces a fault; an already released extra packet cannot be retrieved electronically.

**Ten minutes is your requested starting setting, not a universal standard fry time.** It must be adjustable and validated for cut size, potato preparation, 300 g batch and actual oil temperature. Manufacturer fry recipes vary; for example, a Frymaster manual includes different fry timings. The example is evidence of variation, not a recipe for this machine. [Frymaster operator manual](https://fm-xweb.frymaster.com/service/udocs/manuals/819-6465%20APRIL%2009.pdf).

## What was wrong or incomplete in the previous BOM

| Previous choice or claim | Assessment | Correction |
| --- | --- | --- |
| 12 V motor with DRV8833 | Definite electrical mismatch: its recommended motor supply is 2.7-10.8 V. | Use a 12 V-capable driver and match actual motor current; two reusable BTS7960 boards are provisional candidates. [TI datasheet](https://www.ti.com/lit/ds/symlink/drv8833.pdf). |
| E18-D80NK described as a beam-break detector | It is commonly a reflective proximity device, not a separate emitter/receiver through-beam pair. Detection depends on target reflectivity and geometry. Exact clone output circuitry was not verified. | Use a specified through-beam pair and a chute that forces all strips through the light path. Do not assume an arbitrary sensor's output voltage is safe for an ESP32. |
| Three SG90/MG90S servos as direct vending-coil drives | Ordinary positional versions rotate through a limited angle, not repeated full turns. A pusher could work with a different mechanically designed mechanism, but that is not the drawn spiral indexing arrangement. | Budget three slow continuously rotating geared DC motors, three switching drivers and three index/home switches. |
| MG996R described as a 10 kg basket actuator | Torque in kgf.cm is not a 10 kg lifting capacity. The basket mass and pivot distance were unknown. | Use calculated load-rated basket actuators. Do not promise that a hobby servo can rotate the full basket over hot oil. |
| Three prototype SG90s said to simulate three flavor pushers plus tilt | Three devices cannot independently represent four actuators. | Budget two separate basket-motion simulator motors and three coil motors. |
| One basket driver plus two extra horizontal-transfer switches | A powered transfer axis was implied but its motor and driver were missing. The drawing does not prove it is needed or how transfer works. | Budget lift and rotation only; list the unresolved basket-to-funnel path and price an extra axis only if the mechanical design requires it. |
| 180 C thermostat + 184 C fuse asserted to protect 180 C oil | These component temperatures do not establish oil temperature or correct protection. Mounting, thermal lag, tolerances, heater current and certified assembly matter. | Require a protected manufactured fryer and verified independent overheat cutoff. Do not select random cutoff values from the oil setpoint. |
| SSR signal removal called an emergency stop | A solid-state relay can fail conducting; firmware or signal removal alone is not a reliable energy disconnect. A cheap generic SSR's label does not prove its rating or authenticity. | Budget an independent hardwired power disconnect and qualified electrical assembly. Let the existing fryer thermostat regulate temperature. |
| 220 V desk lamp called a safe low-voltage simulation | A mains lamp still exposes the prototype to mains wiring hazards. | Simulate heater permission using a low-voltage LED. No AC load on a breadboard. |
| Generic threaded thermocouple described as oil-proof/food-grade | Metal construction and temperature range do not prove food contact suitability, continuous immersion rating or cable insulation. | Require a documented food-contact oil-immersion probe, with an ungrounded junction and appropriate lead rating. |
| LRS-100-12 described as 12 V 10 A / 120 W | A genuine LRS-100-12 is 12 V 8.5 A / 102 W. A clone must not be represented as an equivalent certified supply. | A genuine LRS-150-12 (12 V 12.5 A / 150 W) is a provisional allowance; verify measured loads before purchase. [MEAN WELL LRS-100 specifications](https://www.meanwell.com/Upload/PDF/LRS-100/LRS-100-SPEC.PDF). |
| DS18B20 bench reference | It was explicitly intended for water, so it was not inherently wrong. It is unnecessary for the final oil function and its chip stops at 125 C. | Remove it to save money; test the K-type system with a suitable reference thermometer instead. Never substitute a DS18B20 in frying oil. [Analog Devices datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf). |
| All prices called PH benchmarks without item-specific links | They could not be treated as verified current quotes. | Distinguish observed online prices from unverified estimates; record sources, stock qualifications and purchase holds. |

## Proposed system architecture and controller choice

Use a **Mega 2560 R3 compatible board**: a microcontroller is a small computer that repeatedly reads sensors and changes its output pins to run the machine. Its 5 V signals match the proposed display, sensor outputs and driver inputs. It also has enough pins for five motors, position switches and controls without an additional expansion board. A compatible board is a third-party implementation, not an official Arduino-manufactured product. [Arduino Mega technical specifications](https://store.arduino.cc/products/arduino-mega-2560-rev3).

The ESP32 in the old BOM is capable, and its board can cost less. But its 3.3 V pins need careful interfacing to 5 V modules, and a 30-pin board is tight once all feedback is included. Wi-Fi/Bluetooth are not required here. An Uno is simple but has too few pins for the complete arrangement without expansion; a Raspberry Pi adds cost and operating-system complexity without a requested camera, network or payment feature. The Mega is chosen for straightforward wiring, not because the others cannot work.

An **H-bridge** is a motor driver that can reverse current through a motor, making it turn both ways. Two BTS7960/IBT-2 boards are budgeted, one per basket axis. A **MOSFET** is an electronic power switch: three one-direction driver assemblies run the flavor motors. Coil motors need only one rotation direction for normal vending. The two small motion motors are inexpensive dry test devices; they do not establish the final basket's ability to lift or dump.

The **MAX6675** converts the small electrical signal from a K-type thermocouple into digital temperature readings. **SPI** is the clock/data communication used by that interface. **I2C** is a two-signal communication bus used by the display. USB serial communication is used for computer upload/debugging later; there is no network dependency. An **ACS712** provides an analog voltage representing DC motor current, helping detect a jam. None of these parts replaces independent electrical or thermal protection.

```text
Manual cutter -> constrained potato chute -> drop beam -> basket in fryer
                                                        |
                 Mega reads temperature, switches, current and buttons
                    |              |                    |
                 lift driver    tilt driver        three coil drivers
                    |              |                    |
                 lift motor     tilt motor         flavor motors 1/2/3
                    |              |                    |
                 raised/drained basket -> right funnel   -> packet exit beam
                                            |                    |
                                      fitted paper bag <---------+

Mega heater-permission output -> isolated low-voltage interface
    -> professionally enclosed mains control -> complete thermostatic fryer
Independent E-stop / guard circuit -> heater AND motor power removal
Mechanical restraint -> prevents basket falling when power is removed
```

This is an architecture diagram only. It is not a mains wiring diagram or permission to connect the machine.

## Price labels and table scope

- **LISTED:** a price was visible in a store page or search-indexed listing during this review. It is not a checkout quote or a guarantee of stock. Confirm the exact variant and landed price. Some pages had inconsistent stock banners; MAX6675 was explicitly pre-order.
- **ESTIMATE:** an unverified planning allowance. Typical ranges are shown beside the chosen unit allowance. Obtain a PH supplier quote before ordering; do not treat the range as measured market data.
- **HOLD:** part compatibility, exact model, protection, geometry or current is unresolved. Its allowance is included so the budget does not hide it, but it is not ready to buy.
- All table amounts are PHP. Shipping, possible import taxes and optional tools are excluded. Two suppliers listing a similar item do not guarantee identical circuitry.
- Table A covers a **dry, low-voltage prototype**. Actual hot-oil integration requires Table B protection and qualified commissioning in the approved final phase. A dry prototype cannot demonstrate cooking performance.

'''

parts = [intro]
for key, title in [('a', 'Table A: Prototype Phase Materials'), ('b', 'Table B: Main Product Phase Materials - additions only')]:
    parts.append(f'## {title}\n\n')
    if key == 'b':
        parts.append('The complete fryer is included once at your request, even though your assignment is electronics. B11 is a service allowance, shown separately to avoid presenting labor as a physical component. All other B items are additional materials/assemblies.\n\n')
    parts.append('| # | Item name | Exact model/spec | Qty | Est. unit price (PHP) | Subtotal (PHP) | Where to buy (PH) | Why it\'s needed and how it makes the project work |\n')
    parts.append('| --- | --- | --- | ---: | --- | ---: | --- | --- |\n')
    for x in data[key]:
        source = sources.get(x['source'])
        where = x['store'] + (f' ([{x["source"]}]({source["url"]}))' if source else '')
        price = f'{money(x["price"])}; **{x["status"]}**'
        fields = [x['id'], x['name'], x['spec'], str(x['qty'])+' '+x['unit'], price, money(x['qty']*x['price']), where, x['why']]
        parts.append('| ' + ' | '.join(f.replace('|', '/') for f in fields) + ' |\n')
    total = a if key == 'a' else b
    parts.append(f'\n**Table {key.upper()} total: PHP {money(total)}.**\n\n')
    if key == 'a':
        parts.append('A7 motors, A14 breadboards, A15 jumpers, A16 small adapter and the bench portion of A18 remain testbench equipment. The stock A2 probe remains a bench spare. They are not claimed to become full-size final components.\n\n')
    else:
        parts.append('**Reused from Prototype:** A1 controller/cable, A2 MAX6675 converter, A3 verified oil probe, A4 beam pairs, A5 display, A6 basket drivers **if final current/thermal tests pass**, A8 three coil motors **if loaded-coil tests pass**, A9 coil drivers **if current tests pass**, A10 eight switches, A11 five buttons, A12 emergency stop, A13 indicators, A17 logic buck, A19 filtering parts and A20 current sensors. Do not buy these again. A7 bench motors are replaced by the different, load-rated B2 basket actuators. The B8 permanent harness/fuses serve the real machine; the A18 small bench kit remains test equipment. If a candidate fails compatibility tests, update this BOM and total before buying a replacement.\n\n')

parts.append(f'''## Budget totals

| Cost | PHP |
| --- | ---: |
| Table A, dry prototype purchases | {money(a)} |
| Table B, additional final materials/assemblies | {money(b - data['b'][-1]['price'])} |
| Table B, electrical commissioning labor (B11) | {money(data['b'][-1]['price'])} |
| Table B total, including labor | {money(b)} |
| **Grand total, A + B** | **{money(a+b)}** |
| Assignment total if another team buys the fryer | {money(a+b-data['b'][0]['price'])} |

These are planning totals, not a fixed quotation or a complete mechanical machine price. The electrician panel and labor, two basket actuators and probe are substantial unverified estimates. Final compatible choices can change the total. The old spreadsheet's low total omitted or under-specified several of these functions; a cheaper incomplete total is not directly comparable.

## Electrical compatibility and pin budget

| Group | Power / signal interface | Controller signals reserved | Compatibility and purchasing requirement |
| --- | --- | ---: | --- |
| Mega controller | 5 V logic; USB or separately regulated supply arrangement | USB serial pins reserved for debugging | Use one verified power path; do not parallel USB 5 V and buck 5 V without a documented isolation arrangement. Phase 2 selects the board-specific power connection. |
| MAX6675 | Powered at 5 V; SPI-compatible read-only digital output | 3 digital: clock, chip select, data | Mega accepts this 5 V logic. Verify the exact breakout does not require a different supply. The probe sheath/lead ratings, not the converter's maximum measurement range, determine oil suitability. [MAX6675 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max6675.pdf). |
| LCD/PCF8574 | 5 V; I2C SDA/SCL | 2 digital shared bus lines | No ESP32-style 3.3-to-5 V level converter is required in this proposed 5 V system. Determine backpack address during the later bench test. |
| Two SEN0503 pairs | 5 V, NPN output with pullup; approx. 25 mA per specified sensor pair | 2 digital inputs | Use a pullup to controller 5 V; confirm installed behavior. Protect alignment and place outside hot steam/oil splash. Documented maximum ambient is 60 C and it is not waterproof. [DFRobot documentation](https://www.dfrobot.com/product-2388.html). |
| Two basket drivers | 12 V motor power, 5 V logic supply/control | 6 digital: two PWM directions and one combined enable per axis | One IBT-2 drives one reversible motor. Tie each board's R_EN/L_EN together only in the later reviewed wiring design. Driver inputs need boot-time pulldowns. The chip's large current limit is not a safe module continuous rating. [Infineon BTS7960 datasheet](https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf). |
| Three flavor drivers | 12 V motors, 5 V MOSFET gate command | 3 digital outputs | Genuine IRLZ44N specifies low on-resistance at 4.5 V gate drive. Verify stall below 2 A for the proposed 3 A diode/current path, and fit thermal management as needed. This exact assembly is not automatically suitable for an ESP32's 3.3 V output. [Infineon IRLZ44N](https://www.infineon.com/part/IRLZ44N). |
| Eight position/bag switches | Dry contacts: no external powered output | 8 digital inputs | Four basket end states, three coil indexes, one bag-holder engagement. Use pullups, debouncing and wire-break checks where appropriate. Bag-holder geometry must ensure an empty closed holder cannot falsely prove a bag is installed. |
| Five operator buttons | Dry contacts | 5 digital inputs | Three flavors, ARM/PREHEAT, CANCEL/RESET. Ordinary reset must not bypass a guard/stop fault or restart motion automatically. |
| Heater permission / safety status | Isolated low-voltage interface, maximum 5 V at controller | 3 digital: permission, E-stop status, guard status | Never connect 12/24 V contactor coils or mains to Mega pins. The hardware stop chain works without these status inputs or firmware. Exact interface belongs in the B4 supplier design. |
| Buzzer + two status LEDs | 5 V buzzer transistor driver; individual LED resistors | 3 digital outputs | Keep GPIO current small; no motor/coil/relay supply current through the controller pins. |
| Two ACS712-20A sensors | 5 V supply, analog outputs within compatible range | 2 analog inputs | Use DC motor branches only. Calibrate zero and thresholds; module conductor/terminal ratings may be less than chip range. A sensor chip's insulation rating is not approval to use a hobby board on mains. [Allegro documentation](https://www.allegromicro.com/-/media/files/datasheets/acs712-datasheet.pdf). |
| **Total** | **35 digital + 2 analog signals** | **37** | Mega provides 54 digital and 16 analog inputs. Four PWM outputs are needed for basket motors; up to seven if coil speed modulation is added. No assignment conflict is apparent; exact pin mapping is deferred to Phase 2. |

PWM means rapidly switching a driver command to control average motor power. The main basket power path still needs real startup/stall capability. The 5 V **logic** supply powers the controller, display and sensing, not motors. The 12 V **motor** supply powers the motors. Their low-voltage reference grounds are connected in a reviewed layout, while mains is separated by the isolated supply/interface and safety enclosure. Protective earth is a separate safety conductor; never disconnect it to fix sensor noise.

### Power budget: verified ratings versus unresolved loads

| Load / rail | Planning calculation | What is still needed |
| --- | --- | --- |
| Fryer candidate | 2400 W / 230 V = **10.43 A** nominal; approximately 10.91 A if the same 2400 W were specified at 220 V | Use actual nameplate rating; current changes with voltage and heater resistance, so the latter is only an arithmetic comparison. Qualified electrician selects circuit, protection, switches and cables, including supply currents and margins. The 10 A relay suggested previously has inadequate margin for this candidate. [Winland HFRY-60SS specifications](https://winlanddepot.com/products/hanabishi-by-winland-quick-fry-6-liters-deep-fryer-stainless-steel-hfry-60ss). |
| 5 V logic | Reserve **up to 1 A (5 W)** as a design envelope, not a measured draw | Measure total board, LCD, two beams, MAX6675, drivers and sensors, including buzzer. Keep cheap LM2596 module loading conservative and check temperature/ripple. |
| Logic load referred to 12 V | At an assumed 85% buck efficiency: 5 W / (12 V x 0.85) = **0.49 A** | Efficiency is an estimate; verify under actual load. |
| Motor operation | Lift OR tilt OR one flavor motor, with deliberate sequencing; standby loads also present | Obtain running and startup/stall current for each actual motor. A firmware promise of one-at-a-time is not independent short-circuit protection. |
| Main 12 V candidate | LRS-150-12 is **12.5 A / 150 W**. At a provisional 80% design-use target, keep expected operating demand at or below **10 A** | Verify temperature derating, startup transient behavior, fuse/current limiting and loads. If a motor needs more current or 24 V, update supply/driver choices rather than silently using this one. [MEAN WELL specifications](https://www.meanwell.com/Upload/PDF/LRS-150/LRS-150-SPEC.PDF). |
| Bench 12 V supply | 3 A enclosed adapter; small test motors one at a time | Only accept simulator/coil tests within the adapter's rating. If candidate motor startup exceeds it, obtain a suitable current-limited bench supply before testing. |

Final compatibility is therefore **partly verified, not complete**: controller logic levels, bus choice and pin capacity fit the proposed architecture. Full-load motors, drivers, supply, protection and fryer acceptance remain purchase holds. No measured running/stall currents or physical tests have been obtained.

### Protection and components that must not be omitted

- Coil-driver **flyback diodes** provide a safe path for the motor's stored magnetic energy when switched off. Match their current and voltage to the actual motor. A plain diode cannot simply be placed across a reversing basket motor: that would short one direction. H-bridge recirculation and transient protection must follow the actual driver design.
- Gate resistors and pulldowns keep coil switches off while the controller boots. Driver-enable pulldowns serve the same purpose for the basket motors. A reset, unplugged controller or corrupt reading must not cause automatic movement or heating.
- Bulk electrolytic capacitors absorb short current surges; ceramic capacitors reduce fast electrical noise. Polarized capacitors have a positive and negative terminal and must be installed correctly. Exact placement is part of later wiring.
- DC branch fuses protect each conductor/driver branch. Select ratings from actual current, start duration, wire rating and fuse behavior, not from the advertised driver maximum. A larger fuse is not a repair for repeated faults.
- The enclosed mains assembly must have separate run control and independent stop capability, proper earthing of accessible metal, covered terminals, strain relief, suitable residual-current/overcurrent protection and no automatic restart after power returns. A **contactor** is an electrically operated power switch. An **RCBO** combines leakage-current and overcurrent protection. The electrician chooses exact ratings and topology; this BOM does not assert a safety category or certify the finished machine.
- Retain the fryer's thermostat and independently verified overheat protection. Temperature-probe failure must remove software heater permission and latch a fault, while independent protection still works if the controller or run switch fails. Protection against heating with insufficient oil must follow the accepted fryer design; never infer dry-fire protection from an oil temperature reading. Oil level must be checked to the marked limits before arming, and staff supervision does not make a tank safe to run dry.

## Mechanical interfaces needed from the other team

The drawings are reference geometry, not proof that the automatic path works. Pages 1-3 show the overall assembly; page 4 shows the fryer/basket; page 5 the manual cutter; page 6 the spirals; page 7 the chain/sprockets; page 8 the funnel; page 9 a basket-related bracket; page 10 the frame. Most dimension values appear millimetre-scale, but units and as-built dimensions must be confirmed.

| Mechanical-team deliverable | Why electronics depends on it |
| --- | --- |
| Empty basket plus attached bracket mass, retained-oil allowance, 300 g food mass | The motor moves all of this, not just the food. Torque and brake capacity depend on total load. |
| Chain sprocket pitch radius, lift travel, target speed and efficiency estimate | Required lift torque is approximately mass x 9.81 x pitch radius / efficiency, then allowance for friction/acceleration and a justified design margin. |
| Tilt pivot, maximum horizontal distance to the loaded centre of mass, dump angle and reduction ratio | Rotation torque depends on the weight's distance from the pivot. A direct-drive 2 kg load 0.12 m away already creates about 2.35 N.m before friction/margin; these are example values, not measurements of your basket. |
| A demonstrated basket trajectory or transfer chute to the right funnel | The fryer and funnel are separated. A simple vertical lift plus local tip may spill onto the frame unless the linkage or chute bridges that distance. If translation is needed, another motor/driver/end switches/harness must be priced. |
| Chain guides, tensioner, shaft bearings, guards and brake/anti-drop restraint | A worm gearbox is not automatically a certified load-holding brake. Cutting motor power must not drop hot contents. |
| Packet size/thickness, coil pitch, loaded turning force, coupler dimensions and indexing cam | One turn produces one sachet only with matching mechanical spacing. Thin sachets can slip, overlap or jam. A6/A9 driver compatibility requires motor current data. |
| Narrow potato sensing chute and common sachet exit chute | A lone beam only sees objects that cross it. Without constrained paths some strips or packets may bypass detection. Sensors stay below their ambient rating and away from steam/oil. |
| Paper-bag holder/clamp, basket drain path, splash barriers and hygienic food-contact surfaces | The engagement switch must correspond to a genuinely installed open bag; the chute must keep hot oil away from paper. Mechanisms and lubricated chains must not contaminate food. |

The mechanical team's shopping/fabrication list includes frame, manual cutter, food-contact basket/brackets, chain/sprockets, shafts/bearings, motor brackets/couplers, motion restraint, guards, food-safe drain/transfer chute, receiving funnel, bag holder and spiral racks/indexing cams. These are **required interfaces but excluded from your electronics price total**. No fabricated stainless structure price has been invented. Food oil, potatoes, bags and flavor packets are also excluded.

## Ways to reduce cost without losing the required functions

1. Get a local Mega clone quote and compare complete landed prices. The chosen full-size e-Gizmo board at PHP 1,030 includes a data cable. Circuitrocks lists a CH340-compatible Mega at PHP 745 but it was marked sold out and its page has inconsistent product details; verify the exact board first. A matching replacement could save PHP 285 before a separate cable/shipping. [Circuitrocks candidate](https://circuit.rocks/products/arduino-mega-adk-r3).
2. Prototype one actual coil before purchasing all three A8 motors/A9 drivers. If that exact motor fails the torque/current/spacing test, this prevents buying three unsuitable units. The budget still includes three eventual channels; tests do not reduce required channel count.
3. If mechanics can prove one motor plus a cam achieves lift, drain and dump safely, recalculate the actuator count, end stops and drivers. Do not assume the chain shown already performs every motion. Conversely, do not buy a third transfer motor until it is shown necessary.
4. Ask the school whether qualified electrical commissioning can be provided. B11 is a service allowance and can be removed only if an actual qualified service replaces it. The required checks and protection still apply.
5. Share the fryer purchase with the mechanical team; do not count it twice. Lower-price generic 6 L listings exist, but a low price does not establish grounding, protective cutoffs, food contact or actual power. No unverified protected model is recommended as ready to buy.
6. Continue reusing prototype sensors, buttons, controller and accepted drivers. Avoid display upgrades, Wi-Fi modules, illuminated buttons, payment hardware and unnecessary temperature sensors until there is a requirement.

The safety assembly is a quotation allowance, not a fixed design with every component already selected. Request an itemized quote listing the power enclosure, run/safety switches, independent control supply, restart circuit, wiring, protective devices and ratings before ordering it. This can reveal genuine savings or missing components.

## Tools you may still need

You already have multimeters/testing tools, so no multimeter is included in either BOM. The other tools below are **unverified PHP estimates**, outside the totals. Borrowing school equipment is often cheapest.

| Tool | Est. PHP | Purpose |
| --- | --- | --- |
| Linux computer with USB port | Existing/borrowed; no price assumed | Firmware compilation, upload and serial logs in Phase 2. |
| Temperature-controlled soldering iron/station | 800-2,000 | Permanent low-voltage board assembly; soldering is a later-phase step. |
| Electronics solder, flux and cleaning materials | 200-500 | Sound joints and removal of residue; keep these away from food-contact surfaces. |
| Wire stripper, cutters and small screwdrivers | 250-700 | Correct conductor preparation and covered-terminal assembly. |
| Ferrule/connector crimper | 400-1,200 | Secure permanent stranded-wire and locking-connector termination. |
| Third-hand holder, eye protection and fume ventilation | 300-900 | Holds small boards and reduces soldering exposure. |
| Reference cooking thermometer, continuous rating at least 250 C | 400-1,200 | Checks the installed oil probe independently. Verify accuracy and immersion instructions. |
| Adjustable current-limited DC bench supply | Borrow, or estimate 1,500-3,500 | Controlled motor characterization; needed if a candidate exceeds the small adapter's startup capability. |
| Suitable clamp meter and electrical insulation/earth test equipment | Qualified electrician supplies; quote with B11 | Commissioning checks; a beginner multimeter is not a substitute for all installation tests. |

No installations, sudo commands or flashing were performed. Existing PDF/rendering, Python and spreadsheet tools were used. Exact Arduino CLI setup commands, board/library versions and Linux serial-group permissions will be provided in Phase 2, with permission before installation, sudo, device flashing or writes outside this project.

## Price sources checked during this review

''')
for s in data['sources']:
    parts.append(f'- **{s["id"]}:** {s["label"]}. [Source]({s["url"]}).\n')
parts.append('''
Additional comparisons: [element14 PH SEN0503, PHP 270.75 before possible charges](https://ph.element14.com/dfrobot/sen0503/ir-break-beam-sensor-through-beam/dp/4308278); [Winland fryer candidate, PHP 5,055](https://winlanddepot.com/products/hanabishi-by-winland-quick-fry-6-liters-deep-fryer-stainless-steel-hfry-60ss); [Imarflex 6 L IDF-6000S candidate, PHP 5,598](https://imarflex.ph/shop/product/imarflex-idf-6000s-deep-fryer-idf-6000s/). The public fryer listings confirm thermostatic products but did not establish the independent cutoff requirement. Stock probe temperature/immersion limits could not be established from the retailer bundle; the stock probe stays bench-only.

## Phase 1 approval and next step

The revision is ready for budget/architecture review. It is **not a finalized exact-part order for the items marked HOLD**. Resolve the mechanical trajectory and actuator data, oil-probe specification, fryer protection and supplier quotations before releasing those purchases. Phase 2 can begin with a dry logic prototype once you approve the BOM scope; it does not authorize a live-oil demonstration.

**Are you happy with this BOM? Should I proceed to Phase 2?**
''')

(root/'docs').mkdir(exist_ok=True)
(root/'docs/BOM.md').write_text(''.join(parts))
print(f'Wrote docs/BOM.md: A={money(a)}, B={money(b)}, total={money(a+b)}')
