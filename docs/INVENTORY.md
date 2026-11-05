# Materials in hand

Updated: **5 November 2026**, Asia/Manila. Current phase: **Phase 2, Step 26 pending — adapter label/polarity review**.

The user explicitly asked to begin prototyping with the materials already received. Receipt is separate from electrical testing, final compatibility and actual purchase price. Counts hidden by bags are not assumed to equal the earlier shopping quantities.

## Latest receipt

**5 November 2026 update:** user now owns one 12 V adapter and reports measuring **12 V DC**. Exact model, label current/power rating, enclosure type, connector size/polarity, load during measurement and loaded regulation/protection are not supplied. Planned A17 is enclosed regulated 12 V / 5 A / 60 W, but those ratings are not established by the voltage reading. Do not rebuy it automatically. No motor connection/test is reported.

## Received items

| BOM | Item | Quantity supported by evidence | What is confirmed / still needs checking |
|---|---|---|---|
| A17 | 12 V DC adapter | **1 owned**, user confirmation 5 November 2026 | User reports measured 12 V DC; no exact reading trace/conditions or label/plug photo supplied. Current rating, polarity, connector fit and loaded suitability remain unverified. Planned 5 A / 60 W is not a measured rating. |
| A08 | Red panel pushbuttons | **3 visible** | User reports all three passed: released = open, held pressed = connected, released again = open (28 October 2026). Normally-open momentary action confirmed by user continuity checks. User now reports all three connected after retention advice; matching input tester uploaded; user now reports all buttons working after correcting pin placement. Separate physical hold details not itemised. Not emergency-stop buttons. |
| B04 | DC barrel-to-screw-terminal connector | **1 visible** | Plus/minus moulding visible. Exact barrel size, centre polarity mapping and 5 A current suitability not yet verified. Ownership does not qualify it for the full adapter current. |
| A06.1 | Axial Schottky diodes | **1 strip/bag**; individual count unconfirmed | Markings appear consistent with SR5100. Planned pack was ten, but do not mark ten counted from this photo. Delivered manufacturer/current/voltage performance remains untested. |
| A07 | Lever/roller microswitches | **3 owned total**, user confirmation28October2026 | User reports all switches working as intended after the COM–NC / COM–NO continuity procedure (28 October 2026). User confirms only these three are owned. All three connected index inputs pass mapping/state/count checks by user report. Four additional provisional basket switches remain to buy; numeric readings not supplied. Actual terminal labels remain the wiring reference. |
| A18 | Blue 1602-style LCD | **1 visible** | Rear photo confirms an attached HW-61 I2C-style backpack and header GND/VCC/SDA/SCL (top-to-bottom in photo), with blue trimmer. User reports four wires connected and the first power check working as intended. Tool-observed scanner found one device at 0x27 twice without errors. Approved text diagnostic now initialises successfully and logs advancing seconds. Initial blank text resolved after contrast adjustment; user confirms working and photo17 shows FRIES MACHINE / Seconds:23. LCD visual test passed; exact IC/manufacturer ratings still not independently established. No extra backpack purchase needed. |
| A01 | Full-size Mega 2560 compatible board | **1 visible** | User reports ON lit and L blinking on bare USB power. Host now detects readable/writable /dev/ttyUSB0, USB 1a86:7523, driver ch341-uart. Approved diagnostic build/upload and 115200-baud heartbeat/ACK now passed. User confirms the expected two-flash L pattern. Basic board diagnostic and USB link pass; not all GPIO or external functions have been tested. |
| A01/B04 | Coiled black cable | **1 visible** | Original photo ends remain unclear. The cable used for the Mega now powers it and allows host USB serial enumeration; user has not explicitly identified whether it is this photographed cable. Do not assign this coil a wire gauge or infer a known-sketch transfer pass. |
| A05 | ZENG WHCD JGB37-520 geared motors | **3 visible** | Readable labels show DC 12 V / 22 RPM on visible faces. Treat as the received selected motor family; inspect each label. No loaded torque/current/shaft measurement yet. |
| A14 | Capped inline blade-fuse holders | **At least 3 appear visible**; exact total unconfirmed | Actual lead gauge, voltage/current rating, fuse size and contacts not tested. |
| A14 | Standard-looking blade fuses | **1 bag**, exact count unconfirmed | Current and voltage markings are not reliably readable. Earlier order was 2 A, ten pieces; that is not proof the delivered fuses are 2 A. |
| A15 | Ceramic capacitors | Present, user confirmation 28 October 2026; count unknown | Value and voltage rating not supplied. Check markings against planned 100 nF / 0.1 µF (often 104), 50 V, ten pieces before any top-up. Do not rebuy a whole pack automatically. |
| B04 | 18 AWG black power wire | Present, user confirmation 28 October 2026; length unknown | Ownership and stated gauge confirmed by user; available length, conductor material and suitability still to check. Initial allowance is 3 m black: buy only a shortfall, not another automatic 3 m. Red wire not reported owned. |
| A15 | Electrolytic capacitors | **1 bag**, exact count unconfirmed | Visible sleeves read **1000 µF, 25 V**; some show 105 °C. Printed sleeve data are not independent verification of capacitance, ESR, ripple current or authenticity. |
| A15 | Electrolytic capacitors | **1 bag**, exact count unconfirmed | Visible sleeves read **470 µF, 16 V**. Same electrical/quality checks remain. |
| A06 | MOSFET driver modules | **Received, per user confirmation**; exact count not explicitly given | User says they are all soldered. Intended BOM modules are LR7843, three channels. One assembled module now photographed front/back (photos19–20); PWM/GND and +/LOAD/− terminal labels readable. Exact semiconductor markings and total owned count unconfirmed. User now reports all modules already checked and working; exact method/readings unprovided. Loaded channel, safe-OFF/protection and current/thermal tests remain separate. Do not describe them as missing. |
| A11 | Solderless breadboard | Present, user confirmation | User confirms an existing commonGND line, photo21 shows occupied rail near blue marking. Retain existing working signal ground; endpoints/unused-hole continuity not independently established. No duplicate rail required. Signal currents only. |
| A12 | Jumper wires | Present, user confirmation | Quantities, lengths and connector combinations not yet counted. For low-current signals. |
| Tools | Soldering equipment | Ready, user confirmation | Exact equipment not itemised. No further soldering step currently issued. |

Original photographs are copied under `docs/assets/inventory-2026-10-28/`. The photo index is in `manifest.json`; these are evidence photographs, not instructions or proof that parts pass tests.

## Not confirmed in this photo batch

- Adapter label/current rating, plug size/polarity and measurement conditions remain unconfirmed; ownership and reported 12 V are now recorded above.
- LM2596 buck converter, LA38 STOP actuator and buzzer/LED set are not reported owned.
- Ceramic capacitor value/voltage/count and available black 18 AWG wire length need checking; both materials are owned.
- Red 18 AWG wire is not reported owned.
- Motor mounts, couplings, index cams, secured guards and hardware stop/disconnect arrangement.
- The photographed coiled cable's actual connector ends/purpose. LCD rear backpack is now confirmed present.

Apart from the four additional switches explicitly confirmed missing as of 28 October (no later receipt reported), other entries are **not confirmed**, not declarations that the user does not own them. A computer and multimeter were previously reported available; approved project-local Arduino CLI/core installation is now complete; no system package or group change was required. The user reports successful continuity checks on all three buttons; numeric contact resistances were not supplied.

## Current tested milestone and next work

- Mega/USB diagnostics and known verified firmware/serial operation passed.
- LCD0x27 readable after contrast adjustment; three flavor inputs22/23/24 and three index inputs26/28/30 passed by user.
- Uploaded output-free cycle_logic_test passed planned manual sequence, lockout, wrong-index, timeout/reset and held-input checks. This is a USB-only logic milestone, not real motor/heater/basket validation.
- Preserve successful common signalGND and existing wires. Do not repeat passed checks without new evidence. Adapter is now in hand with reported 12 V; next review is label/plug/current rating and polarity; actual power/protection/driver/mounting checks remain required before motor operation.

Concise resume point: [USB_LOGIC_CHECKPOINT.md](USB_LOGIC_CHECKPOINT.md). Full prototype remains incomplete; Phase3 has not started.

## Confirmed missing items affecting next tests — 28 October2026

- Four additional roller microswitches for provisional basket endpoints (masterBOMA07total7,3owned,4remaining). Exact mechanical suitability remains conditional.
- Adapter is now owned; remove it from remaining-to-buy items. Current rating/polarity and loaded acceptance remain pending.

Step19 software dryrun is uploaded and uses current parts only; it does not remove these outstanding powered/basket prototype requirements.

## Step 25 procurement review

Full row-by-row audit: [REMAINING_PURCHASES.md](REMAINING_PURCHASES.md). Ceramic capacitors and black 18 AWG wire are now recorded as owned; values/count/length remain unreported. No duplicate purchase assumed, no new price or device test claimed.
