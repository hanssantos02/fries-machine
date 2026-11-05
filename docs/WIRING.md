# Prototype wiring record

> **Current save, 6 November 2026:** [Concise assembly checkpoint](ASSEMBLY_CHECKPOINT.md) and the newest dated reports supersede earlier pending prompts below. **Step37 motor soldering has been issued but is not reported complete.** Firmware remains output-free simulation; no powered motor test or Phase3.

## Current Step37 — motor positive and flyback cathode, first joint

Steps35/36 expected continuity/isolation and DRIVER+retention passed by user report. Fuse OUT, all power unplugged. MotorA is chosen/labelled bench positive (use actual+mark if available, otherwise no factory polarity claim); B is future switched return. Direction unverified. Make onlyAjoint:

| Component | Destination | Purpose |
|---|---|---|
| LabelledMOTOR+ pigtail | MotorA | Fused positive feed |
| SR5100 **banded cathode** lead | Same motorA | Flyback cathode at positive |
| SR5100 unbanded anode | Free, isolated for now | Later motorB/LOAD connection |
| MotorB, driverLOAD/controlPWM/controlGND | Empty | Not connected by this step |

```text
fused junction -- DRIVER+ ------------------ driverPOWER+
              └- MOTOR+ -------------------- motorA
SR5100 cathode (BAND) ----------------------- motorA
SR5100 anode (UNBANDED) --------------------- free/isolated
motorB / driverLOAD / control: empty
connector− --18AWGreturn--------------------- driverPOWER−
```

Support diode/leads; no bare contact with motor case/shaft, no forced bending of motor pins. Cool/photo/retention checkpoint before insulation or second joint. Flyback is incomplete until laterBconnection; no power/fuse insertion/GPIO assignment. [Beginner steps](BUILD_PROTOTYPE.md#current-step37--motor-and-banded-diode-lead-to-motor-terminal-a).

## Current Step36 — reconnect driver positive; taped junction

User reports electrical tape already coversY-junction; actual tape coverage/retention not visually inspected. Preserve if secure/full coverage, no automatic unwrapping. Three Step35 results not explicitly confirmed; request beep/beep/no-beep confirmation with next report. All power unplugged/fuseout. Reconnect only labelledDRIVER+tail to driverPOWER+, one untinned conductor/clamp. Negative return unchanged; unusedMOTOR+tip insulated.

```text
connector+ -- holder[FUSE OUT] -- tapedY -- DRIVER+ -- driverPOWER+
                                      └-- MOTOR+ -- tip insulated, disconnected
connector− -- existing18AWG return ---------------- driverPOWER−
DriverLOAD/controlPWM/controlGND and motor/diode: disconnected.
```

Check no bare metal around tape (including two-lead exit), secure solder joint with supported wires/slack, no stray strands at screw, and gentle-pull retention. Black positive pigtails must stay labelled. No electrical/taped-joint pass or motor-power approval inferred from “done.” [Steps](BUILD_PROTOTYPE.md#current-step36--reconnect-driver-after-junction-insulation).

## Current Step35 — junction continuity and negative isolation

6November2026: Step34 soldered junction secured by user report, no photo/electrical result. All power unplugged, fuse OUT, both pigtail ends disconnected, driverPOWER+empty, motor/diode/control disconnected. Negative return remains as before. Sleeve stays back for cooled-joint access.

| Probe point1 | Probe point2 | Mega connection | Expected in continuity mode |
|---|---|---|---|
| Bare solder junction including incoming red stem | LabelledDRIVER+ far-end copper | None | Beep/lowresistance near probe baseline |
| Same red-stem junction | LabelledMOTOR+ far-end copper | None | Beep/lowresistance near baseline |
| Same junction | Verified DCconnector− terminal metal | None | No beep/open |

Meter blackCOM/redVΩ; colours can be swapped for passive conductor tests. Check tip-touch/separated baseline, expose only about4mm of each far end for contact, do not tin future screw-clamped end. Keep loose positive ends apart from negative; inspect for damaged insulation/strands. If joint already covered, report before removing insulation. Wait for three results before covering/reconnection. No load/current-rating qualification from this test. [Instructions](BUILD_PROTOTYPE.md#current-step35--check-the-soldered-positive-junction-before-insulating).

## Current Step 34 — fused-positive Y junction, preparation pending

User chooses existing wire/solder/heat-shrink, no junction connector purchase. Preserve existing circuit until manual preparation begins. With adapter/USB unplugged and fuse out, release red holder output from driver+ and join it to two short18AWGstranded-copper positive pigtails. Future DRIVER+/MOTOR+ destinations must be visibly labelled even if insulation is black. All three conductors at the junction are the same positive electrical node.

| Junction wire | Future destination | Current preparation state |
|---|---|---|
| Red stem | Fuse-holder output, downstream of fuse | Released from driver+ for soldering |
| DRIVER+ pigtail | DriverPOWER+ | Far end remains insulated/disconnected |
| MOTOR+ pigtail | Selected motor positive, terminal assignment later | Far end remains insulated/disconnected |

```text
connector+ -- holder[FUSE OUT] -- red -- Y joint -- DRIVER+ tail (not connected)
                                           └--- MOTOR+ tail (not connected)
connector− -- existing18AWG return -- driverPOWER− (unchanged)
driverPOWER+ / LOAD / controlPWM / controlGND: empty during preparation
Motor/diode: disconnected. All supplies unplugged.
```

Fit heat-shrink before joining, make mechanically engaged inline splice, solder/cool, inspect and gently pull each lead. Keep tubing back for a clear joint photo; no shrink/power/reconnection yet. No solder-tinning on future screw-clamped ends. [Full beginner steps and safety](BUILD_PROTOTYPE.md#current-step-34--solder-the-fused-positive-y-junction). Actual assembly not reported complete; no GPIO/firmware changes.

## Current Step 33 — motor terminal and positive-junction review pending

**Photos now received:** [09motor rear](assets/motor-review-2026-11-05/09-motor-rear-terminals.jpg), [10DCconnector](assets/motor-review-2026-11-05/10-dc-connector-wired.jpg), [11driver](assets/motor-review-2026-11-05/11-driver-supply-wired.jpg). Two bare motor contacts, polarity marks not established. Supply red/black at outer driver entries, middleLOAD/control empty, consistent with intended map. No multi-wire clamp rating inferred. Availability of an internally common3port junction connector is pending; otherwise plan an insulated soldered junction from existing materials. Do not add a second wire under driver+ or install the motor until the junction/attachment steps are prepared. Photos do not establish loaded or independent safety acceptance.

Step32 user confirms18AWG negative return secured. Present assembly by user report:

```text
DC connector+ ---- fuseholder [FUSE OUT] ---- driver POWER+
DC connector− ---- 18AWG return ----------- driver POWER−
Driver LOAD / controlPWM / controlGND ---- EMPTY
Motor and SR5100 ---- disconnected
Adapter out of connector/wall; MegaUSB unplugged for handling.
```

Request actual motor-rear contact photo and current connector/holder/driver wiring photo before adding motor/diode leads. Plan the secure shared fused-positive junction; module terminal multi-conductor capacity is not established. Conceptual intended low-side circuit has motor positive and driver+ on the same fused-positive node, motor return on LOAD; do not install from this description until actual attachment/topology is resolved. No new GPIO, energizing or extra conductor in an occupied terminal is directed. [Review checkpoint](BUILD_PROTOTYPE.md#current-step-33--inspect-motor-terminals-and-plan-fused-positive-junction).

## Current Step 32 — negative motor-power supply return, unpowered

**Gauge clarification:**18AWGrecommended; short genuine20AWGstranded copper is also suitable within this isolated one-motor bench scope (aim10–30cm, cool/unbundled, intact insulation and secure clamp fit; branch protection still pending). This is not approval for a shared three-motor return/full5Atrunk, long or final harness, basket or mains. No actual substitution/connection reported. Colour is a guide; label both ends if not black. [Sizing context](https://www.powerstream.com/Wire_Size.htm).

Step31 fused-positive feed secured by user report. USB/adapter unplugged, adapter output removed and fuse OUT. Add one wire:

| From | To | Suggested wire | Purpose |
|---|---|---|---|
| DC connector terminal− | Driver POWER− on three-way+, LOAD,− block |18AWGblack stranded copper recommended; short20AWGstranded copper alternative as above | Return path for future motor current in this single branch |

```text
DC connector+ ---- holder [FUSE OUT] ---- driver POWER+
DC connector− ---- short18AWG /20AWG --- driver POWER−
Driver LOAD / controlPWM / controlGND: EMPTY
Motor/diode/Mega: not connected to this power assembly.
USB unplugged; adapter disconnected from connector and wall.
```

POWER− is distinct from the controlGND terminal besidePWM; do not route motor current through control leads, DuPont jumpers or breadboard. Secure one conductor per screw, no stray strands and gentle-pull both ends. Stop if wire/terminal fit is unsuitable; no forced/tinned-wire workaround. Await result before further wiring; incomplete assembly must not be powered. [Build steps](BUILD_PROTOTYPE.md#current-step-32--dc-connector-negative-to-driver-power-negative).

## Current Step 31 — first branch positive supply to driver, unpowered

Step30 first holder lead→connector+ and retention complete by user report. No new photo/rating qualification. Fuse removed, adapter disconnected, USB unplugged. Make only the following additional connection:

| Component lead | Destination | Wire | Purpose |
|---|---|---|---|
| Remaining free fuse-holder tail | Selected module POWER terminal marked+ | Existing red holder wire, gauge/rating unverified | Future positive feed through branch fuse |

```text
DC connector+ ---- holder ---- [FUSE REMOVED] ---- driver POWER+
DC connector− ---- EMPTY
Driver LOAD / POWER− / controlPWM / controlGND ---- EMPTY
Motor, diode, Mega ---- not connected to this assembly
Adapter disconnected from connector and wall; USB unplugged.
```

Use actual+marking from previously photographed board; notPWM/GND/LOAD/−. Secure one conductor with no stray strands; verify gentle-pull retention and wait for user report. No two-wire terminal approval is implied: motor-positive branching remains to design/inspect before installation. No power, GPIO assignment, flash or safeOFF qualification from this step. [Instructions](BUILD_PROTOTYPE.md#current-step-31--remaining-fuse-holder-lead-to-driver-positive).

## Current Step 30 — first fused-positive lead, unpowered

**Loop status now confirmed by user:** prepare two tails by one manual cut approximately midway along the loose red loop, away from holder body, with all power disconnected and fuse removed. Strip one tail only for connector+; leave the other tail insulated and disconnected. This supersedes the earlier stop-for-loop-identification instruction below. [Preparation steps](BUILD_PROTOTYPE.md#latest-user-confirms-the-cable-is-still-one-loop). No cut/connection result supplied yet; diagram/connection destinations unchanged.

Step29 connector mapping passed by user report. Unplug USB/adapter, keep barrel plug out, remove fuse. Only proceed if holder already has two free ends; if still a continuous loop, stop/report before cutting.

| Component | Connection | Wire | Purpose |
|---|---|---|---|
| Either free fuse-holder lead | DC connector marked+ | Existing red holder lead, actual gauge unverified | Supply-side entry to planned branch fuse |
| Other holder lead | Unconnected, exposed tip insulated | Existing red holder lead | Future branch output |
| Connector− | Empty | None yet | Return wiring follows |
| Fuse | REMOVED | None | Keep branch open during assembly |

```text
Connector+ ---- holder lead ---- [FUSE REMOVED] ---- free lead insulated
Connector− ---- EMPTY
Adapter output and wall plug disconnected; USB unplugged.
No motor, module or Mega connection to this assembly.
```

Clamp conductor securely, no stray strands/excess bare metal, one conductor per terminal. Gentle-pull/photo report before continuing. No cut/power/GPIO assignment or approval of unknown current ratings. [Full steps](BUILD_PROTOTYPE.md#current-step-30--first-fuse-holder-lead-to-connector-positive-unpowered).

## Current Step 29 — disconnected DC connector mapping

User confirms diode SR5100 and reports expected forward direction (redunbanded/blackbanded) with none reversed; exact readings not supplied. Reverse must mean OL/open, not numerical0. Current next checkpoint tests only the loose barrel/screw connector with USB/adapter unplugged and no other connections.

| Connector connection | Mega pin | Continuity probe points (either colour order) | Expected |
|---|---|---|---|
| Moulded+ screw terminal | None | Terminal metal ↔ barrel centre contact | Beep/low resistance near probe baseline |
| Moulded− screw terminal | None | Terminal metal ↔ outer barrel contact | Beep/low resistance near probe baseline |
| + versus− | None | One terminal metal ↔ other terminal metal | No beep/open |

Meter blackCOM/redVΩ, continuity mode; first verify tip-touch beep and separated-tip open. Do not bridge barrel contacts or force access with a probe. Request an end-on connector photo if contacts cannot be identified/reached. In photo04 the moulded− is left and+right, but follow actual labels if rotated. Mapping pending, not passed. This is not an energized adapter test, current-rating qualification or motor wiring instruction. [Detailed steps](BUILD_PROTOTYPE.md#current-step-29--check-the-disconnected-dc-connectors-terminal-mapping).

## Current Step 28 — loose diode meter connections

Photo07 under [motor review](assets/motor-review-2026-11-05/manifest.json) shows an axial rectifier-style diode; pale cathode band is upper-right in the photo. Full code not reliably read; await transcription and electrical readings. No motor connection/GPIO is assigned by this step.

| Loose component lead | Mega connection | Meter probe / lead jack | Purpose |
|---|---|---|---|
| Unbanded anode, first test | None | Red / VΩ-diode jack | Forward direction, test current enters anode |
| Banded cathode, first test | None | Black / COM | Forward direction, record voltage-drop display |
| Banded cathode, second test | None | Red / VΩ-diode jack | Reversed direction, normally OL/open |
| Unbanded anode, second test | None | Black / COM | Reversed direction return |

```text
First:   red probe ---- anode [ diode |band ] cathode ---- black probe
Second: black probe --- anode [ diode |band ] cathode ----- red probe
Digital meter: diode mode; component disconnected from EVERYTHING else.
```

Never diode-test a powered circuit. Keep probe tips apart. Wait for readings before connecting the diode to a motor; no motor-terminal polarity assignment is issued here. [Detailed steps](BUILD_PROTOTYPE.md#current-step-28--isolated-flyback-diode-check-5-november-2026).

> **Latest photo review, 5 November 2026:** adapter label shows12VDC5A, centre-positive (MODEL1250); earlier missing-label questions are resolved. Connector moulding shows minus left/plus right in photo04 only; verify actual contact mapping/current suitability before powered wiring. Fuse appears marked2; voltage/curve not established. Photo05 is a red indicator LED and must not serve as motor flyback protection. Next select one owned black axial diode and read its code/band. Six originals: [manifest](assets/motor-review-2026-11-05/manifest.json). No new wiring/output GPIO or powered test.

> **Latest, 5 November 2026 — Step 27:** adapter store check accepted by user report; exact output current/polarity and test scope remain unspecified. Proceed only with electrically disconnected one-channel parts layout/marking review. No motor/power/control wiring or GPIO is assigned. Existing module photo20 establishes printed PWM/GND/+ /LOAD/− labels, not full topology or adapter polarity. Obtain actual fuse/diode markings and adapter OUTPUT/current/polarity as text or photos before preparing the protected channel diagram. Do not repeat the same voltage test solely to restart the workflow.

> **Latest, 5 November 2026:** user reports all reconnected inputs working after Step 26D. Preserve LCD GND/5V/SDA20/SCL21, buttons22/23/24 and indexNO26/28/30 with COM shared GND and NC unused. This is a user-reported restored logic result, not a new solder inspection or motor test. Earlier reconnection prompts below are superseded. Current Step 26 is unplugged adapter label/plug review and clarification of the prior 12 V measurement; no new motor wiring or output pins assigned.

## Current Step 26D — three index switches, 5 November 2026

Buttons connected by user report; no new solder/endpoint inspection or restored input pass. Preserve their D22/D23/D24 connections, working LCD and existing ground. Unplug USB and every supply before restoring the following inputs. Switch identifiers match flavor buttons.

| Component pin | Mega/shared connection | Suggested wire colour | Purpose |
|---|---|---|---|
| Index1 COM | Existing shared GND | Black | Common return for switch1 |
| Index1 NO | D26 | Blue | Closes to GND on actuation; index1 input LOW |
| Index2 COM | Existing shared GND | Black | Common return for switch2 |
| Index2 NO | D28 | Yellow | Closes to GND on actuation; index2 input LOW |
| Index3 COM | Existing shared GND | Black | Common return for switch3 |
| Index3 NO | D30 | White | Closes to GND on actuation; index3 input LOW |
| All three NC | Unconnected | None | Not used by this simulation; keep clear of other conductors |

```text
Mega D26 ---- NO [ index1 ] COM ---- shared GND
Mega D28 ---- NO [ index2 ] COM ---- shared GND
Mega D30 ---- NO [ index3 ] COM ---- shared GND
NC on each switch: unused.
USB unplugged; adapter/motors/drivers/fryer disconnected.
```

COM=common; NO=normally open (closes to COM when pressed); NC=normally closed (opens when pressed). Use actual terminal labels, never assumed middle/outer lug positions. INPUT_PULLUP in the retained sketch supplies the input bias; no 5V contact wire or extra resistor is required. Keep existing correct COM ground returns, and secure/insulate leads. Await user mapping/wiring report before the focused powered reconnection check. No new wiring/function pass is recorded for these indexes.

## Current Step 26C — flavor buttons, 5 November 2026

**Latest:** stranded 20 AWG wire and heat-shrink tubing confirmed. Immediate checkpoint is one soldered lead on one completely disconnected flavor1 contact; leave the far end insulated/disconnected. Inspect the cooled joint before covering or making the second lead. [First-joint instructions](BUILD_PROTOTYPE.md#first-physical-checkpoint--one-wire-on-one-button-contact) include soldering safety. The full route below is the future arrangement, not a completed assembly; GPIO map is unchanged.

**Retention update:** user reports loose jumper fit at buttons. 20 AWG may be used for low-current button leads; wire type and available insulation still need clarification. Proposed termination preserves proper male jumper pins at controller/rail sockets:

```text
Button contact A -- 20 AWG lead -- insulated splice -- male jumper pin -- D22/23/24
Button contact B -- 20 AWG lead -- insulated splice -- male jumper pin -- shared GND
```

Button-contact solder joints and wire splices must be individually insulated, with the insulated leads supported against pulling. Stranded wire is preferred for handled leads. No soldering directly to Mega, no forced bare-wire/solder-blob insertion into sockets, no 5V to contacts. No terminal/crimp size is inferred from the photograph. This is a proposed attachment method, not a completed wiring change or purchase; wait for wire-type/insulation information before a one-button physical assembly checkpoint. GPIO map and firmware remain unchanged.

User confirms shared connections already exist; preserve the common signal ground without duplicate construction. Exact return endpoints/continuity are not independently inspected. LCD is working and Mega simulation unchanged by user report. USB/all supplies must be unplugged while restoring these connections.

| Component terminal | Mega connection | Suggested wire colour | Purpose |
|---|---|---|---|
| Button1 contact A | D22 | Blue | Flavor1 selection input |
| Button1 contact B | Existing shared GND | Black | Pulls D22 LOW only while pressed |
| Button2 contact A | D23 | Yellow | Flavor2 selection input |
| Button2 contact B | Existing shared GND | Black | Pulls D23 LOW only while pressed |
| Button3 contact A | D24 | White | Flavor3 selection input |
| Button3 contact B | Existing shared GND | Black | Pulls D24 LOW only while pressed |

A/B are temporary identifiers for the two isolated contacts; they may be exchanged. Colours are suggestions. Internal pull-ups are configured by the retained sketch; do not add 5V wires to the contacts.

```text
Mega D22 ----[ button1 ]---- existing shared GND
Mega D23 ----[ button2 ]---- existing shared GND
Mega D24 ----[ button3 ]---- existing shared GND
LCD remains GND / 5V / SDA20 / SCL21.
USB and all other supplies unplugged during wiring.
```

Leave already-correct ground returns in place. Follow printed socket numbers on the double-row Mega header; 22/23/24 are not three consecutive sockets in one row. One wire per socket. Await the button wiring report before index signal wiring/powered checking. No new button pass is recorded. Earlier Step 26B rail-construction prompt below is superseded by the user's existing-ground report.

## Current Step 26B — shared signal ground, 5 November 2026

User reports Step 26A LCD reconnection working and confirms the Mega retained its simulation sketch. Keep GND/5V/SDA20/SCL21 LCD wiring intact. With USB and every supply unplugged, add only this ground feed:

| Component connection | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| One selected breadboard minus/blue rail section | Spare GND socket | Black, male-to-male jumper | Common electrical reference/return for the six future input contacts |

```text
Mega spare GND ---- black jumper ---- one selected ground-rail section
                                     o o o o o o ...
                                     six return connections follow later

LCD: retain GND / 5V / SDA20 / SCL21 direct connections.
USB and all external supplies unplugged.
```

Choose a section with at least seven free holes before adding the feed. Markings do not establish electrical continuity; a central break or opposite rail may be isolated. Keep all future input returns within the same section unless a bridge is deliberately checked later. Do not connect 5V to this rail. Use one wire per Mega socket, and do not route motor current through breadboard wiring. Await the user's ground-wire/rail-section report before adding buttons; no measured continuity or new input pass is recorded.

## Completed Step 26A — LCD reconnection map, 5 November 2026

**Result:** LCD connected and working, Mega sketch unchanged, by user report. Original pending text below is historical; Step 26B above is current.

User removed the breadboard connections for another project. The maps below remain the intended wiring; current reconnection is not yet confirmed. Last known sketch is the output-free simulation, but ask whether the Mega was reprogrammed before power. This checkpoint connects only the LCD, directly to the Mega, with USB and every supply unplugged.

| Component pin | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| LCD GND | GND | Black | Electrical return/reference shared with Mega |
| LCD VCC | 5V in POWER header | Red | Powers the previously tested LCD from the 5 V logic supply |
| LCD SDA | Digital 20 / SDA | Blue | I2C display data |
| LCD SCL | Digital 21 / SCL | Yellow | I2C communication clock |

```text
LCD rear backpack               Mega 2560
GND --------------------------- GND
VCC --------------------------- 5V (POWER)
SDA --------------------------- 20 / SDA
SCL --------------------------- 21 / SCL

USB unplugged; barrel jack empty; 12 V adapter disconnected.
Buttons, switches, drivers and motors: leave disconnected at this checkpoint.
```

Use the actual printed labels; rotation changes apparent pin order. Male-to-female jumpers connect these four pins directly without the breadboard. Check secure, correctly aligned endpoints and no bare-pin contact. Never put 12 V on these connections. Wait for the unpowered wiring report before proceeding. Full step instructions: [BUILD_PROTOTYPE.md](BUILD_PROTOTYPE.md#completed-step-26a--reconnect-the-lcd-with-all-power-off-5-november-2026).

> **Current state, 5 November 2026:** Step24 USB-only logic checks passed; Step25 procurement review saved. Step26 is pending adapter label/polarity review. Adapter is now owned and user reports measured12V; current/power rating, polarity and loaded suitability are not yet established. October missing-adapter/pending-test statements below are historical. Driver GPIO and motor-power wiring remain unassigned. See [current handoff](handoffs/2026-11-05-assembly-resume.md) and [USB checkpoint](USB_LOGIC_CHECKPOINT.md).


Updated: **28 October 2026**, Asia/Manila. **Phase 2, Step 24**.

## Completed test: isolated pushbutton continuity

There is **no Arduino wiring and no external power** in this checkpoint. Temporary terminal names A and B below are arbitrary labels for the two terminals on one loose pushbutton. They are not inferred manufacturer pin names.

| Component terminal | Arduino pin | Meter connection / colour | Purpose |
|---|---|---|---|
| Pushbutton terminal A | None | Black probe; meter lead plugged into COM | One end of the isolated contact measurement |
| Pushbutton terminal B | None | Red probe; meter lead plugged into V/Ω | Other end of the isolated contact measurement |

Black and red probe positions can be exchanged on this isolated mechanical switch without changing the expected result. Do not exchange the meter's voltage/resistance jack for a current jack.

```text
       Meter in continuity mode
     COM                    V/Ω
      |                      |
  black probe            red probe
      |                      |
  terminal A ---[ button ]--- terminal B

  No Arduino, USB, supply, motor or capacitor connected.
```

Expected: released = open; held pressed = connected; released again = open. User reports all three buttons passed. See TESTING.md for recorded results.

## Completed test: isolated microswitch contacts

Only use the terminal markings on the actual switch. The switch COM terminal and the meter COM jack are distinct things connected by the black probe.

| Component terminal | Arduino pin | Meter connection / colour | Purpose |
|---|---|---|---|
| Switch COM / C | None | Black probe; meter COM jack | Common contact for each measurement |
| Switch NC, first measurement | None | Red probe; meter V/Ω jack | Checks contact that opens when actuated |
| Switch NO, second measurement | None | Move same red probe from NC to NO | Checks contact that closes when actuated |

```text
Meter COM -- black probe -- switch COM
Meter V/Ω -- red probe   -- switch NC   [first measurement]
                         OR switch NO   [second measurement]
No power, Arduino or other component connected.
```

Expected COM–NC: beep / no beep / beep. Expected COM–NO: no beep / beep / no beep, for released / held actuated / released. If markings cannot be read, obtain a clear photo before assigning terminal positions.

## Current diagnostic connection: bare Mega USB only

The user reports all microswitches working as intended. See TESTING.md for the batch result and unconfirmed count.

| Component connection | Mega connection | Suggested cable / colour | Purpose |
|---|---|---|---|
| Computer USB port | Actual board USB socket (normally Type-B on full-size Mega) | Matching intact USB data cable; jacket colour irrelevant | Power bare board and later establish USB data communication |
| All external buttons, switches, drivers, LCD and motor supplies | No connection | None | Keep first board check isolated |

```text
Computer USB port ===== matching USB data cable ===== bare Mega USB socket
Mega header pins: empty. Barrel jack: empty. No other power or modules.
```

Inspect the unpowered board first. Put it on a clean nonconductive surface. Do not force a cable that does not fit. Power indication and USB data detection are separate checks; a charge-only cable can power a board without establishing programming communication. No soldering or Arduino pin assignment is needed for this checkpoint.

## Known diagnostic pin use — uploaded; serial passed

| Component | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| Already fitted L LED | LED_BUILTIN = digital 13 in Mega definition | None; onboard connection | Two short flashes per two-second frame |
| Onboard USB-to-serial interface | Existing Serial UART0 connection | None; onboard plus USB cable | Status messages at 115200 baud and ?/ACK receive check |
| All external devices | None | None | Remain disconnected |

Do not attach anything to digital 13 or the UART0 pins 0/1 during this bare-board test. Source: firmware/mega_diagnostic/mega_diagnostic.ino. This is not a machine-control pin map. USB power/enumeration, diagnostic upload and serial heartbeat/ACK have passed. User confirms the expected two-flash L pattern. Step 4 passed. Keep external parts disconnected.

## Completed checkpoint: unpowered LCD identification

User supplied the rear photo: attached HW-61 backpack and GND/VCC/SDA/SCL labels confirmed. Exact IC text and electrical operation remain unverified.

## Step 6 connection table — user reports connected

Photo evidence: `assets/inventory-2026-10-28/13-lcd-backpack.png`. The attached backpack is marked **HW-61**. The four male header pins are labelled **GND, VCC, SDA, SCL from top to bottom in that photo**. Always use the printed labels if the module is rotated. The chip text is not clear enough to assign an exact manufacturer/part number; the I2C address is not yet measured. The photo shows the adapter attached along the 16-pin row; it does not certify every solder joint.

The proposed system uses a 5 V LCD supply from the Mega's **5V** power header in a later USB-only powered test. This is the selected LCD1602 system design, not an independently verified rating for the generic HW-61 assembly. Step 6 issued unpowered connections; user now reports them complete without a photo. Step 7 requires an end-to-end user label check before USB-only power observation; no independent visual review is claimed.

| LCD backpack pin | Mega pin / header label | Suggested wire colour | Purpose |
|---|---|---|---|
| GND | Any GND | Black | Shared circuit return/reference |
| VCC | 5V in the POWER header | Red | Planned regulated 5 V supply for this logic display; never VIN or 12 V |
| SDA | Digital 20, marked SDA where provided | Blue | I2C communication data |
| SCL | Digital 21, marked SCL where provided | Yellow | I2C communication clock |

```text
LCD backpack                    Mega 2560
GND --------------------------  GND
VCC --------------------------  5V [POWER header]
SDA --------------------------  20 / SDA
SCL --------------------------  21 / SCL

USB unplugged; barrel jack empty; all other supplies disconnected.
No motors, drivers, buttons or other modules connected.
```

Mega pin mapping is verified against the [official Mega 2560 pinout](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf). Use the labelled digital 20 and 21 sockets for this table. The separate duplicated SDA/SCL header on an R3 board is the same bus, not another required pair. Do not use A4/A5 as if this were an Uno.

Use four **male-to-female jumper wires**: socket (female) end over each LCD male pin; pin (male) end into the Mega's labelled female socket. Wire colours are suggestions; labels determine the connection. A breadboard is not needed for these direct four wires. If the available ends do not fit securely, report the connector types; do not balance loose wires on pins or force an incompatible connector.

**Check before continuing:** with power still disconnected, trace each wire end-to-end against the table. Ensure each female socket covers one intended pin, no neighbouring pins touch, and Mega 5V/GND are not confused with adjacent VIN/RESET/3.3V. User reports the wires are connected; no photo received. Step 7 below uses a final user label check before power. Leave the blue trimmer and jumpers as delivered. No powered display result or address scan is claimed.

## LCD power/address/text results and current Step 9

With USB unplugged, recheck all four table endpoints. If correct and secure, reconnect USB **only**, barrel jack empty and no other modules/supplies. Observe the backlight; report its state before adjustments or new firmware. Power off before changing a wire. The existing double-flash diagnostic does not initialise the LCD.

User reports the first power check passed. Prepared scanner uploaded successfully; startup and r rescan each found one device at **0x27**. The next prepared text test uses that address and the same SDA20/SCL21 and 5V/GND wires. No wiring changes are requested. User approved the text-test library/install/upload. It is now running at address0x27 on the same wires; serial init/seconds updates passed. User now reports no visible text and provides a lit-screen photo. Connections remain unchanged. User now confirms contrast adjustment restored readable FRIES MACHINE / Seconds:23, shown in photo17. LCD test passed. Retain its wires and contrast setting; Step10 adds only input buttons with USB off.

## Step10 three-button map — connected per user; active test Step11

Keep the successful LCD wires unchanged: GND/5V/SDA20/SCL21, address0x27. **Unplug USB and every other supply before adding button wires.** No driver/motor connection is issued. The two-terminal buttons already passed normally-open momentary contact tests; either terminal can be chosen as A or B because these isolated contacts have no polarity.

| Component terminal | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| Button1 terminal A | Digital22 | Green | First flavour selection input |
| Button1 terminal B | Unused GND socket | Black | Connects input22 to ground only while pressed |
| Button2 terminal A | Digital23 | Yellow | Second flavour selection input |
| Button2 terminal B | Another unused GND socket | Black | Connects input23 to ground only while pressed |
| Button3 terminal A | Digital24 | White | Third flavour selection input |
| Button3 terminal B | Another unused GND socket | Black | Connects input24 to ground only while pressed |

```text
Mega22 ----[ normally-open button1 ]---- GND
Mega23 ----[ normally-open button2 ]---- GND
Mega24 ----[ normally-open button3 ]---- GND

LCD remains on GND / 5V / SDA20 / SCL21.
USB unplugged while adding/checking wires. No external supply or motors.
```

Use one wire per Mega socket and individually labelled unused GND sockets. All Mega GND sockets share the same circuit ground. Never use a socket merely because it is near GND; check the printed label. Colours are suggestions, not electrical proof. Do not connect any button terminal directly to 5V/VIN. This is the uploaded flavor_buttons_test `INPUT_PULLUP` arrangement: the Mega's internal weak pull-up holds an unpressed input HIGH; a press joins it to ground so it reads LOW. No separate resistor is needed for this basic short-wire logic test. The new input diagnostic enables that mode on22/23/24; the earlier LCD-only program has been replaced.

Connect through securely fitting insulated leads/terminals. If female jumper sockets do not fit the panel-button terminals, stop and show/describe the terminals before soldering or improvising. Do not wedge or balance bare wires where they can touch adjacent terminals. A breadboard is optional if later needed for ground distribution, but no unverified rail layout is assumed here.

### Keeping the prototype button leads attached

User says the jumpers can connect but asks how to prevent falling off. The earlier bag photo does not establish an exact terminal size/type; no spade size or locking connector is prescribed.

For this stationary low-current button test, an already **snug electrical contact** can be retained temporarily with electrical insulation tape: cover each connector/terminal separately, then anchor the insulated lead to the stationary button body/support with slack. This support is **strain relief**: pressing/pulling should not load the contact. Tape cannot fix loose/intermittent metal contact. Keep exposed conductors separate and leave the moving button/mounting thread usable.

At the Mega end, seat male pins fully in the correct sockets and anchor the cable bundle to a nearby nonconductive support with slack at the header. Do not solder into Mega sockets or put glue in contacts. Avoid anchoring to hot parts, sharp edges, the reset button or USB plug.

A durable alternative is short flexible **soldered pigtails** on suitable button solder terminals, with heat-shrink insulating each joint separately and wire support. Pigtails are short attached leads; retain a removable male connector at the Mega end. Do not solder a plastic female jumper socket onto a lug. No cutting/soldering steps are issued yet: confirm suitable terminals and insulation first. Matched crimp receptacles are another option if these are blade tabs; actual size is unmeasured and no purchase selected.

**One trial checkpoint:** USB and all supplies unplugged. If proper electrical tape is available and a jumper already seats snugly, secure just one button connector and anchor its wire. Apply a very gentle pull to the insulated lead and check the button moves freely. Report whether it stays attached before repetition. Stop if the contact moves/loosens; do not bury an intermittent contact in tape. If suitable insulation is unavailable, report that before improvising. No soldering, power or upload is issued here.

Reference: [SparkFun Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire/all), covering soldered connections, insulation and strain relief. This is low-current signal wiring, not a motor or mains termination.

**Check before continuing:** trace each button's input and ground lead against this table. Leave USB unplugged and report all three connected (or show a photo/describe a connector difficulty). Wait before power/new firmware. No soldering or new upload is issued in this wiring checkpoint. Actual named flavours have not been provided; labels1–3 are test identifiers.

References: [Mega official pinout](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf), [Arduino internal-pullup example](https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial/). The installed AVR1.8.8 Mega variant also maps D22–24 as GPIO, separate from SDA20/SCL21.

## Completed Step11 — button diagnostic, user report

User reports all three buttons connected/secured after retention advice. The tester uses the exact table above, built-in INPUT_PULLUP and35ms debounce; LCD remains0x27/SDA20/SCL21. Serial idle111/counts0,0,0 and lcd=OK observed. User subsequently reports all buttons working after correcting pin placement; exact changed sockets and separate held-press details not supplied. Use BUTTON_TEST.md to test each mapping and hold/release behaviour. Firmware/host tests do not prove each physical connection. No motors or new power source connected.

## Header-position reference and Step12 driver inspection

With the board oriented as in photo18 (header beside the board edge), the row toward the board centre contains even-numbered digital pins; the outer row contains odd-numbered pins. Starting at the header end near SDA20/SCL21 and the mounting hole:

```text
Toward board centre       Toward board edge
          5V                       5V   <- power pair: NOT button inputs
          22                       23   <- buttons1 and2
          24                       25   <- button3 uses24 only
          26                       27
          28                       29
          ...                      ...
```

Use printed labels rather than counting from an assumed first socket:22 and23 are opposite;24 is the next socket along22's row. Each button's other lead still goes to a labelled GND socket, never5V. Source: [official Mega pinout, page3](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf). Photo18 was supplied before the user self-corrected the wiring; obscured endpoints do not establish the precise fault.

**Step12:** unplug USB/all other supplies before handling. Photograph one disconnected soldered MOSFET module on both sides with terminal labels visible. Do not assign a module terminal or GPIO by analogy with another LR7843 board. No new connections are issued until the actual module is reviewed; successful LCD/button wiring remains unchanged. Motor/driver pins are still unassigned.

### Step12 photo review — 28 October 2026

Photos19–20 show one assembled module; total owned count remains unspecified. Green two-way connector: PWM above GND in the component-side photograph. In the **underside photo**, blue three-way connector is on the right: **+ / LOAD / − from top to bottom**. Turning the board over reverses left/right; always trace the actual printed labels. Exact power-MOSFET and optocoupler chip markings cannot be read reliably. There is no obvious bridge between adjacent terminal nets in these photographs; this is not a continuity, insulation, mechanical-strength or solder-quality pass. Multiple pads joined under one terminal can belong to the same net; do not order blanket resoldering merely because solder is rounded.

| Printed module terminal | Role in documented matching module family | Mega pin / wire colour | Current action |
|---|---|---|---|
| PWM | Control input: accepts the controller's on/off or pulse signal | Unassigned; future logic lead blue | Leave disconnected |
| GND beside PWM | Return/reference for the control input | Future Mega GND / black, not connected now | Leave disconnected |
| + | Motor-supply positive; also positive side of the load circuit | No Mega pin; future protected positive lead red | Meter probe only at this checkpoint |
| LOAD | Switched motor return; motor's other side goes to + in the matching circuit | No Mega pin; future motor return lead black, individually labelled LOAD | Leave disconnected |
| − | Motor-supply negative | No Mega pin; future supply-return lead black | Meter probe only at this checkpoint |

The terminal-role interpretation matches the [ProtoSupplies LR7843 module description](https://protosupplies.com/product/lr7843-mosfet-control-module/), retrieved in search results on28October2026; direct opening returned403. This supplier describes its own tested module, not the user's exact board. Do not transfer its current/voltage/isolation guarantees to this generic board. The matching family uses an optocoupler, a component that passes the control command using light internally. Actual control-GND to power-minus separation has not been measured; do not add a ground bridge or claim verified galvanic isolation. The small onboard diode's function/rating is not established from its appearance. Keep external motor flyback protection in the plan; no suitable motor-diode path is verified here.

### Current Step12 checkpoint — resistance across disconnected power terminals

**Before using resistance/continuity mode:** module must have no wires attached, no motor, no adapter and no Arduino connection. Unplug Mega USB before handling nearby wiring; keep successful LCD/button leads unchanged. Never use resistance mode on a powered circuit. This check concerns the loose driver only, not the power adapter or mains.

1. Black meter lead in **COM**; red in **V/Ω**, never the A/mA current jack. Select **Ω (resistance)**, with auto-range or a suitable range if available.
2. Touch the probe tips together briefly and note the near-zero lead reading; separate them. This gives a reference for a direct metal short.
3. Touch **red to the module's + terminal** and **black to its − terminal**. Use the underside markings to identify the corresponding top screw/terminal metal. Keep tips apart; do not bridge an adjacent terminal.
4. Wait a few seconds and report the displayed number **and unit/range**, or OL. Report if the reading starts low then rises. If the meter has only continuity, report whether the beep persists or is brief instead; no resistance value may be inferred from a beep alone.

```text
Meter COM -- black probe -------- module −
Meter V/Ω -- red probe ---------- module +
Module PWM / GND / LOAD: empty. Module entirely disconnected.
```

**Check before continuing:** request the measured reading and whether the regulated12V motor adapter is already in hand (label photo if present). A persistent reading near the shorted-probe baseline is suspicious: do not power the board; review the measurement and joint details first. A higher reading or OL only rules out an obvious direct short in this measurement; it does not verify driver switching, safe OFF/reset, current capacity, isolation or flyback protection. No exact nominal resistance is assumed without the actual circuit. Stop here for the user's result. No wiring to a GPIO, installation, upload or motor-power operation is issued.

## Step12 subsequent user result

User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned. The earlier resistance checkpoint is superseded by this report; no repeated meter check requested now.

## Completed Step13 — one roller microswitch connected, user report

The missing motor adapter does not prevent a controller-input test. Leave motor drivers and motors disconnected. A microswitch is a mechanically operated electrical contact. This first switch will represent **flavor-coil index1**: a reference position the coil will later reach once each turn. This test uses hand operation only; it does not prove one-packet dispensing or mechanical index placement.

**Before changing wires:** unplug Mega USB and all other supplies. Keep the successful LCD/button wiring unchanged. Use the switch's actual COM/NO/NC markings and the earlier contact checks; do not assume the middle physical lug is COM. If labels cannot be read, obtain a clear view before wiring.

| Component terminal | Mega pin | Suggested wire colour | Purpose |
|---|---|---|---|
| Microswitch COM (common) | An unused socket explicitly marked GND | Black | Circuit return when the NO contact closes |
| Microswitch NO (normally open) | Digital26 | Blue | Future index1 input; goes LOW when lever is actuated with INPUT_PULLUP enabled |
| Microswitch NC (normally closed) | No connection | None | Not used in this isolated NO-contact diagnostic; keep clear of other conductors |

```text
Mega D26 ---- NO  [roller microswitch]  COM ---- Mega GND
              NC: no wire
LCD remains GND/5V/SDA20/SCL21.
Buttons remain D22/GND, D23/GND, D24/GND.
USB and external supplies unplugged during wiring.
All motor/driver connections remain absent.
```

1. Select **one** previously contact-tested roller microswitch and identify COM and NO from its markings/known meter test. NC is the other labelled contact and stays empty.
2. Attach a snug, insulated signal lead from COM to an unused labelled Mega GND socket. If there is no free GND or the connector does not fit securely, report that before improvising a shared connection.
3. Attach NO to **D26**. In the pictured double-row header, D26 is in the same inner row as22 and24, immediately after24; opposite it is27. Skip the extra5V pair at the header end. Use printed numbers.
4. Ensure the NC lug and exposed lead metal cannot touch adjacent terminals. Lightly operate the lever without pulling on the leads.

**Check before continuing:** leave USB unplugged and report this one switch connected (or send a clear terminal/header photo if uncertain). Do not power or upload yet. D26 is now reserved for this next diagnostic, but the currently uploaded flavor_buttons_test only reads22/23/24 and will not display index events. Matching complete input/index firmware is the next software checkpoint after wiring confirmation, with the required upload permission handled then. No firmware/pin change has been made to the running button diagnostic.

The later input test will enable the Mega's internal pull-up on26: lever released = HIGH; lever actuated = LOW. Mechanical contact bounce will be filtered in software, just as for the red buttons. A broken wire can also read HIGH in this NO arrangement; this is a bench input test, not a fail-safe limit or emergency-stop circuit. Final homing/index timeout and any NC fault-detection arrangement must be designed and tested separately.

References: [Arduino internal pull-up example](https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial/) and [Mega pinout](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf). No new parts, packages or prices are introduced by this wiring step.

**User result:** “connected.” Recorded as completed wiring report; no physical index input event verified.

## Completed Step14 — index1 input passed by user report

User reports Step13 COM/GND–NO/D26–NCempty switch connected and subsequently explicitly approved the prepared diagnostic upload. Keep the existing buttons/LCD unchanged. Complete `firmware/inputs_index_test` now runs; exact commands and logs in [INDEX_TEST.md](INDEX_TEST.md).

Compile passed11922 flash/599RAM bytes; identical debounce-helper host tests passed. Pins22/23/24/26 use INPUT_PULLUP; LCD0x27/SDA20/SCL21 unchanged. No motor/driver/heater outputs configured.

User approved the prepared upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; source hashes matched compiled source. CLI upload --verify exited0. Serial INPUTS_INDEX_V1 READY plus 16 released-idle samples raw1111/counts0,0,0,0/lcdOK; no LCD error, held-at-boot tag or physical input press during capture. Unreadable startup bytes preceded clean tagged output. Monitor closed Ctrl+C exit0; inputs_index_test now runs on the board. No package install or wiring change. Physical lever test remains pending.

**Check before continuing — operate only the roller lever, do not move wires:** hold about2seconds; expect INDEX 1: ACTIVE and exactly one Count increment. Release: INDEX 1: READY with Count unchanged. Press/release again: one additional count. Ask user for actual visible states/count behaviour and wait. Do not infer physical contact closure from idle1111. No new installation/upload or connection needed for this observation.

**Step14 user result:** User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test.

## Superseded Step15 proposal — user already has common signal ground

Step14 first index-switch input passed by user report. Before adding two more switches, provide a shared GND connection without placing multiple wires into a single Mega socket. The existing direct LCD/button/index connections use several ground sockets. A **breadboard power rail** is a long connection strip for distributing one electrical connection; its printed colour is only a label, not proof of electrical continuity. Some rails are split.

**Safety before this check:** unplug Mega USB and every other supply. Use an otherwise empty breadboard rail; do not connect it to the Mega or change the successful wires yet. Resistance/continuity mode must never be used on a powered circuit.

1. Find one clearly marked long power rail, preferably beside a blue line or minus sign. Select **four nearby holes along that same rail**, calling them1–4 from one end. These will later accommodate MegaGND plus the three microswitch COM leads. Do not choose holes across the central breadboard gap or jump to the opposite rail.
2. Meter black lead in COM and red lead in V/Ω; select continuity/beeper mode. Verify the meter beeps when probe tips touch. Use snug male jumper pins in the chosen holes to make probe contact; do not force thick meter probes into breadboard sockets.
3. With one jumper in hole1 for the black probe, put a second jumper in hole2 and touch its free conductor to the red probe. Check for a steady beep. Move only that second jumper to hole3, then hole4, checking each against hole1.

```text
ISOLATED, UNPOWERED breadboard rail:
Chosen holes:      1    2    3    4
Meter black ------1
Meter red -------------2    (first check)
                        3    (second check, against1)
                             4 (third check, against1)

No Mega/switch/supply connected to this rail yet.
```

| Test | Expected | What it establishes |
|---|---|---|
| Hole1–hole2 | Steady continuity beep | Same electrical group |
| Hole1–hole3 | Steady continuity beep | Same electrical group |
| Hole1–hole4 | Steady continuity beep | Same electrical group |

**Check before continuing:** report whether all three pairs beep. If any fail, report which pair or show the breadboard before moving wires; a split rail or different connection group may be involved. Wait for this result before using that group as shared ground. Existing working LCD, three buttons and D26 switch remain unchanged and unplugged for this checkpoint. No new index GPIO, firmware, upload or motor-power operation is issued yet. The next step will connect the verified ground group and the remaining index switches, then prepare a matching diagnostic. Shared-ground rail is for low-current input signals only, not motor current.

**Step15 user clarification:** User states an existing common breadboard GND line is already made for everything and supplies photo21. Accept the existing signal-ground arrangement as user-reported; retain it instead of building a second rail or repeating the empty-rail procedure. Photo shows multiple jumpers near the blue marking but does not prove every endpoint or split-rail continuity. Earlier working LCD/buttons/index1 support those tested signal paths, not every unused rail hole. No numeric continuity reading or new meter pass is inferred.

## Completed Step16 — switches2/3 connected by user report

The user already has common ground; Step15's proposed empty-rail construction is superseded. Reuse the **same connected ground section** already used by the working input circuit. Printed colour and wire colour do not determine electrical identity. Do not connect a separate rail segment on the assumption it is internally continuous.

**Before moving/adding wires, unplug Mega USB and every other supply.** The photograph shows ON lit, so ensure USB is now actually disconnected. Preserve the LCD, three buttons and working index1 connection. Motor drivers/motors remain disconnected; breadboard ground is for these low-current control/input circuits, not motor-current routing.

| Component terminal | Mega / shared-ground connection | Suggested wire colour | Purpose |
|---|---|---|---|
| Index switch2 COM | Existing connected signal-GND rail | Black | Common return, linked to MegaGND |
| Index switch2 NO | Reserved digital28 | Yellow | Future flavor-coil2 reference-position input |
| Index switch2 NC | No connection | None | Unused in this NO-contact input diagnostic |
| Index switch3 COM | Existing connected signal-GND rail | Black | Common return, linked to MegaGND |
| Index switch3 NO | Reserved digital30 | White | Future flavor-coil3 reference-position input |
| Index switch3 NC | No connection | None | Unused in this NO-contact input diagnostic |

```text
Existing MegaGND ---- existing connected signal-GND rail
                         |---- COM index1, NO ---- D26 (already tested)
                         |---- COM index2, NO ---- D28 (new)
                         |---- COM index3, NO ---- D30 (new)
NC on each switch: unused. LCD/buttons unchanged.
```

1. Identify COM/NO/NC from each previously tested switch's actual markings. The middle physical lug is not assumed to be COM.
2. Add switch2 COM to an available hole on the existing connected GND section and NO to **D28**.
3. Add switch3 COM to that same connected GND section and NO to **D30**. Keep both NC terminals empty and exposed conductors separated; use snug, insulated leads as for the first switch.
4. D26, D28 and D30 are consecutive sockets along the same **inner/even-numbered** row. Their opposite sockets are27,29,31. Use printed labels, leaving existing D26 untouched.

**Check before continuing:** leave USB unplugged and report both new switches connected, or report a terminal/ground-section uncertainty before improvising. Do not change the working circuit or build another ground rail merely to follow earlier assumptions. Current uploaded inputs_index_test reads only22/23/24/26; **D28 andD30 are reserved for the next diagnostic and will not display events yet**. Matching all-three-index firmware follows the wiring report; no new firmware or upload is issued here. Final machine fault detection/homing mechanics and all motor-power tests remain separate.

**Step16 user result:** “done, connected.” Connection completion reported; switch2/3 physical input events not yet tested.

## Completed Step17 — all three flavor-index inputs passed by user report

User approved the prepared upload. IndexNO26/28/30 and COMexistingGND/NCempty, buttons22/23/24 and LCD0x27/SDA20/SCL21 unchanged. Complete `firmware/inputs_three_index_test` now runs. [THREE_INDEX_TEST.md](THREE_INDEX_TEST.md) has exact commands and manual checks.

User approved the prepared three-index diagnostic upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523, read/write access and unchanged source hashes. CLI upload --verify exited0. Serial INPUTS_3INDEX_V1 READY and15 released-idle samples raw111111/counts0,0,0,0,0,0/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical press during capture. Startup unreadable bytes preceded clean tags. Monitor closed Ctrl+C exit0; inputs_three_index_test now runs. No new library, wiring change or actuator output. Physical three-index mapping/hold/release and button regression remain pending.

Compile/host evidence remains PASS12054flash/619RAM, identical debounce helper; four supplied-core warnings only. All six inputs use INPUT_PULLUP. Current firmware now reads28/30; no further flash or connection required for manual testing.

**Check before continuing:** operate levers1,2,3 individually, keeping others released. Each should show its own INDEXnumber ACTIVE and exactly one increment during a2second hold; release shows same index READY with count unchanged; repress adds one. Then recheck buttons show matching FLAVOR1/2/3. Ask actual results and wait before adding anything else. Do not touch wiring while powered. No motor power or Phase3.

**Step17 user result:** User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing.

## Completed Step18 — only three microswitches owned

The three connected flavor-index inputs passed Step17 by user report. Preserve the working LCD/buttons/index wiring and inputs_three_index_test. The12V motor adapter is explicitly not yet owned, so no powered driver/motor test is issued.

The BOM provisionally plans **seven microswitches total**: three coil indexes plus four basket end-position inputs. Those four cover the two ends of the proposed lift and tilt axes; actual mechanical mounting, final function and any NC/fault-detection arrangement remain subject to the retained PDF mechanism. A future hand-operated input check would not authorise basket motion or determine safe mounting.

**Current missing information:** does the user have **four additional roller microswitches**, besides the three now connected? Ask for availability/remaining quantity; do not assume planned shopping quantity equals received count, declare them missing, or order duplicates. If available, next prepare an unpowered bench-input connection checkpoint using actual terminal labels and a matching diagnostic. If fewer, record the count and choose useful firmware/input work with present hardware before purchasing. No new GPIO assignment, firmware, connection or upload yet.

**Check before continuing:** wait for the user's quantity response before the basket-input wiring branch. No action on the working hardware is required now. All current driver and basket pins remain unassigned. Adapter purchase remains the already documented regulated12V5A enclosed unit on the physical-store list, with actual label/output/polarity/protection verification needed before motor power. No new price or purchase item is introduced.

**Step18 user answer:** no additional switches; only the three connected switches. Four provisional basket switches remain to buy; no basket GPIO assigned.

## Completed Step19 — first physical simulation passed by user report

Retain current six inputs/commonGND/LCD; no new wires. Complete `firmware/cycle_logic_test` now runs and has **no actuator output pins/API**. [CYCLE_LOGIC_TEST.md](CYCLE_LOGIC_TEST.md) contains exact commands and expected sequence.

User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed.

Host logic/debounce tests and build remain PASS13360flash/797RAM,4corewarningsonly. This is a software/input simulation, not a powered prototype or actual cooking recipe. Four basket switches and12Vadapter still missing.

**Check before continuing:** with all contacts released, press/release flavor2 then hand-operate index2/D28 within15seconds. Expect selected Flavor2, SIMWARMUP5s, SIMCOOK10s, then SIMTIMERSDONE/Basketpending. Ask for actual display sequence and wait before fault/busy/recovery tests or further hardware. All drivers/motors/heater/external supplies remain disconnected; no movement expected. If timeout, report actual display/contact before changing anything. Keep powered wiring untouched.

**Step19 user result:** User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement.

## Completed Step20 — busy-button selection lockout passed by user report

Step19 first manual simulation passed by user report. Keep the same uploaded cycle_logic_test and all existing wiring; no new firmware/connection or device command is needed. Drivers/motors/heater/external supplies remain disconnected, USB logic power only.

Read these steps before starting, so the short simulated cooking window is clear:

1. Release all buttons/levers, then press the Mega's small onboard **RESET** button once. Wait for **SIMULATION ONLY / Select flavor**. This is a bench simulation reset, not a real machine emergency stop.
2. Press/release **flavor button1**. Within15seconds press/release **index1/D26**, just as the prior test used flavor2/index2.
3. Wait through the5second SIMWARMUP until **SIM COOK** starts its10second countdown.
4. During SIMCOOK, press **flavor button2**, hold about2seconds, then release. Press/release **flavor button3** while the countdown is still active. Expect **Flavor1** to remain selected and remaining seconds to keep decreasing; no switch toFlavor2/3 or restart to10s/5s.
5. At **SIM TIMERS DONE / Basket: pending**, press/release button2 once. Expect the stopped completion view to remain; busy presses must not have queued another simulation, and this diagnostic needs an explicit reset for another run.

**Check before continuing:** ask whether Flavor1 remained selected, timers continued without restarting and the final view stayed stopped after the extra press. Wait for that physical result before wrong-index/timeout/reset tests or further code/hardware. Do not touch wiring while powered. If any selection/timer changes unexpectedly, report which button and LCD stage/countdown; do not rewire or reflash automatically. Host lockout tests passed previously, but this actual input/LCD lockout check is still pending.

**Step20 user result:** User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred.

## Completed Step21 — wrong-index rejection and flavor3 passed by user report

Step20 busy-button check passed by user report. Keep the existing uploaded cycle_logic_test, six input wires and LCD unchanged. This is still an output-free USB-only simulation; motors, drivers, external supplies and heater remain disconnected.

Read the sequence before starting: all index responses below must fit inside the same15-second response window.

1. Release every button/lever, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button3**. Expect SIM PRESS INDEX / Flavor3 with the response countdown.
3. Briefly press/release **index1/D26**, then **index2/D28**. These are roller levers, not flavor buttons. Expect the display to stay on SIM PRESS INDEX / Flavor3 while the countdown continues; neither wrong index may advance or restart it.
4. Before that same15-second window expires, press/release **index3/D30**. Only this matching index should advance to SIM WARMUP5s, then SIM COOK10s, then SIM TIMERS DONE / Basket: pending, retaining Flavor3.

**Check before continuing:** ask whether indexes1/2 were ignored and only index3 advanced the Flavor3 simulation through the timers. Wait for this physical result before timeout/recovery or initially-held-index tests. If the window expires, get the actual display and sequence rather than assuming wrong-index rejection failed. No reflash, serial monitor opening, wiring change or further part purchase is required for this observation. RESET is a bench reset, not an emergency stop.

**Step21 user result:** User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test.

## Completed Step22 — timeout/fault/reset passed by user report

Step21 wrong-index test passed by user report. Use the same cycle_logic_test and unchanged wiring with USB logic power only. All motors/drivers/heater/external supplies remain disconnected. This checks the software's missing-response path, not motor jam/stall protection or an emergency stop.

1. Release all buttons/levers, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button2**, then **do not operate any roller lever**. Allow its15-second index-response countdown to expire.
3. Expect **SIM FAULT / INDEX TIMEOUT**. No SIM WARMUP or SIM COOK stage should start.
4. While the fault is displayed, press/release **index2/D28**, then **flavor button1**. Expect the fault to remain: a late index or new selection must not resume/restart the simulation.
5. Release every control and press onboard **RESET** once. Expect **SIMULATION ONLY / Select flavor**, remaining idle without a new button press.

**Check before continuing:** ask whether the missing response produced the fault, the fault stayed after the extra switch/button presses, and RESET returned to idle. Wait for that result before initially-held-index/startup-input tests or any further code/hardware. No new upload, serial monitor opening or wiring change needed. If behavior differs, request the actual display/operation sequence; do not infer a defective switch or alter powered wiring. Reset here is a bench software reset and does not qualify a physical safety-stop circuit.

**Step22 user result:** User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop.

## Completed Step23 — initially-held selected-index check passed by user report

Step22 timeout/fault/reset test passed by user report. Preserve the uploaded cycle_logic_test and successful six-input/LCD wiring. Use USB logic power only; all motors/drivers/heater/external supplies stay disconnected.

Read the sequence before starting; release/re-actuation must occur within the15-second response window that begins at flavor selection.

1. Release all controls, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press and **hold index1/D26** for about1second before selecting a flavor, allowing its contact filter to settle.
3. Still holding that roller lever, press/release **flavor button1**. Expect **SIM RELEASE IDX** with Flavor1. Keep the lever held about2seconds: warm-up must not begin from the old active index state.
4. Release index1. Expect **SIM PRESS INDEX**, still Flavor1 and inside the same countdown; release alone must not start warm-up.
5. Press/release index1 again before the original15-second window expires. Only this fresh actuation should start SIM WARMUP, then the existing5s/10s simulation and Basket: pending.

**Check before continuing:** ask whether the held index was rejected, release changed the prompt without advancing, and only re-actuation started warm-up. Wait for the physical result before the startup-held-flavor test or further work. No code, flash, monitor opening or wiring changes. If the deadline expires, obtain actual displayed stages/operation order; do not infer a defective input. RESET remains a bench reset, not a hardware safety-stop function.

**Step23 user result:** User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred.

## Current checkpoint: Step24 complete — USB-only logic milestone passed

User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied.

All currently planned USB-only input/display/control-logic checks now pass. Current firmware and wires remain unchanged; no new build, flash, monitor session or device action. See [USB_LOGIC_CHECKPOINT.md](USB_LOGIC_CHECKPOINT.md) for the concise resume point and coverage limits.

**Full Phase2 prototype remains incomplete.** Next priority is the already planned regulated enclosed12V5A60W adapter; four additional basket-input switches remain to buy. Other power wiring/protection/mounting details are not automatically qualified. When the adapter arrives, request its label/plug photo before issuing a measured-output/polarity checkpoint or any motor wiring. Do not repeat passed USB checks absent new evidence; no Phase3 transition or powered motor/heater action.

## Pending connections

- LCD SDA20/SCL21 and three flavour-button inputs22/23/24 are now assigned. Future firmware must match these tables. D26 is active in the uploaded inputs_index_test together with buttons22/23/24; physical lever event/hold/release passed by user report; All three index inputs26/28/30 are now active in uploaded inputs_three_index_test with buttons22/23/24. Physical three-index mapping/hold/release passed by user report; latest button regression not separately confirmed. Driver and basket pins stay unassigned.
- LCD backpack and actual header labels are now confirmed from the rear photo; address is now measured as 0x27. Readable text now passes after contrast adjustment, with user confirmation/photo. Exact chip identity remains unverified.
- One soldered module is now photographed on both sides (photos19–20); PWM/GND and +/LOAD/− labels readable. Exact chip marks and total count unconfirmed. User reports all MOSFET modules already checked/working; do not repeat the earlier resistance request. No driver GPIO or power wiring assigned.
- The DC connector's moulded plus/minus marks do not independently establish the acquired adapter's polarity, current capability or mating size.
- Received motor labels support 12 V / 22 RPM identification, not powering them directly from the Mega or USB. No motor current through a breadboard or DuPont signal leads.
- Electrolytic capacitors have polarity. Keep them unconnected until a later verified diagram and discharge/polarity check. Do not use their 16 V/25 V ratings to infer the proper voltage for the Mega or LCD.
- Mains/fryer and final-machine wiring are not issued at this stage.
