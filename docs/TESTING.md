# Prototype tests and results

> **Current state, 5 November 2026:** Step24 USB-only logic checks passed; Step25 procurement review saved. Step26 is pending adapter label/polarity review. Adapter is now owned and user reports measured12V; current/power rating, polarity and loaded suitability are not yet established. October missing-adapter/pending-test statements below are historical. Driver GPIO and motor-power wiring remain unassigned. See [current handoff](handoffs/2026-11-05-assembly-resume.md) and [USB checkpoint](USB_LOGIC_CHECKPOINT.md).


Updated: **28 October 2026**, Asia/Manila. Current checkpoint: **Phase 2, Step 24**.

Receiving a part is not a functional test pass. User-reported observations record manual hardware checks; tool-observed upload/serial results are recorded separately with logs. Never infer an unobserved physical LED pattern from serial output.

## T01 — three disconnected flavour/start pushbuttons: PASS, user report

Procedure: BUILD_PROTOTYPE.md, Step 1. Wiring: WIRING.md, isolated meter-only diagram.

| Observation | Expected | Actual / status |
|---|---|---|
| Probes together, then apart | Beep/low resistance together, open apart | User states all expected outcomes occurred; no numeric resistance supplied |
| Button released | Open / no beep | PASS for all three, user report |
| Button held pressed | Connected / beep, resistance near shorted-probe baseline | PASS for all three, user report; no numeric resistance supplied |
| Button released again | Open / no beep | PASS for all three, user report |

If the probe check fails, correct the lead jack/mode and probe contact first; do not conclude the switch is faulty. If the contact result differs, record whether it appears normally closed, latching, intermittent or not changing; confirm delivered terminals/type before proceeding. Do not test a powered circuit in continuity mode.

## T02 — received microswitch batch: PASS, user report

Read the actual COM/C, NO and NC markings first; no terminal order is assumed. If unreadable, request a close photo before assigning terminals. Procedure: BUILD_PROTOTYPE.md, Step 2; meter-only connections in WIRING.md.

| Pair | Lever released | Lever held actuated | After release | Actual |
|---|---|---|---|---|
| COM–NC | Beep / low resistance | Open / no beep | Beep / low resistance | PASS, user reports all switches working as intended |
| COM–NO | Open / no beep | Beep / low resistance | Open / no beep | PASS, user reports all switches working as intended |

Observe electrical change, not just a mechanical click. If there is no change, first check probe contact, terminal labels and meter mode. Report actual readings; do not assume all switches match one tested sample. The user reports all switches checked and working as intended. Exact tested count and numeric resistance values were not supplied. This contact-action check does not establish environmental ratings or long-term mechanical reliability.

## T03 — bare Mega USB power/enumeration: PASS for reported observations

Procedure: BUILD_PROTOTYPE.md, Step 3. Board bare, USB only, no header wiring or external power.

| Observation | Expected / interpretation | Actual |
|---|---|---|
| Unpowered visual inspection | No loose conductive debris, obvious damage or unintended pin bridges | Pending |
| ON/power LED after USB connection | Power indication; this alone does not prove USB data or firmware operation | PASS: user reports ON lit |
| Other LEDs | Record actual labels/pattern; factory program unknown | User reports L blinking; existing program not identified |
| Computer USB/serial detection | Device/port enumerates; actual port/interface to identify, no fixed tty name assumed | PASS: /dev/ttyUSB0, USB 1a86:7523, product USB Serial, ch341-uart; read/write access true |

If no power indication appears, disconnect and check cable/USB port/connector fit before interpreting it as a damaged board. If power appears without a detected port, investigate data cable and USB interface; do not install arbitrary drivers or reflash a bootloader. Smoke, burning smell or abnormal heating requires immediate disconnection. Known-sketch upload is recorded separately in T04 below.

## T04 — known Mega diagnostic: PASS

Procedure and exact commands: ARDUINO_SETUP.md. Source: `firmware/mega_diagnostic/mega_diagnostic.ino`. CLI 1.5.1 / Arduino AVR Boards 1.8.8; target `arduino:avr:mega:cpu=atmega2560`; no third-party libraries.

| Check | Expected | Actual |
|---|---|---|
| Project-local CLI/core setup | Checksum verified, pinned core/tool installation succeeds | PASS: CLI 1.5.1 checksum OK; Arduino AVR Boards 1.8.8 installed project-locally |
| Target compilation | Mega target builds successfully; memory use recorded | PASS: 3334 bytes flash, 196 bytes RAM. Four unused-parameter warnings in Arduino core new.cpp; none from sketch |
| Upload and verification | Diagnostic application writes and verifies on intended Mega | PASS: approved upload with --verify to /dev/ttyUSB0, exit 0; uploaded diagnostic boot tag subsequently captured |
| L LED | Two short flashes then pause, repeating every two seconds | PASS: user confirms expected double-flash pattern, 28 October 2026 |
| Serial heartbeat | Diagnostic tag, increasing heartbeat and uptime at 115200 baud | PASS: 27 consecutive heartbeats, 1–27, uptime 1000–27000 ms in 1000 ms increments |
| Serial receive | Sending ? produces diagnostic ACK | PASS: expected USB serial receive OK acknowledgement |

User explicitly approved execution with “proceed.” Evidence: .build/logs/mega-setup.log, mega-compile.log, mega-board-list.log, mega-upload.log, mega-serial.log and mega-diagnostic-result.json. Monitor closed cleanly with Ctrl+C; board remains running. A few unreadable bytes preceded the clean diagnostic boot text; all subsequent captured diagnostic lines were readable. Do not describe the entire capture as free of initial noise.

Opening a serial monitor can reset the board; this is expected. These are separate from T03's existing-program blink. If upload or compilation fails, stop and retain the error; no automatic forced signature, bootloader burn or package/permission change.

## T05 — LCD rear identification: photo received; connector identification PASS

Current instruction: disconnect Mega USB, keep LCD unpowered, inspect and photograph its back. Identify whether an adapter board (I2C backpack) is fitted and soldered to the LCD. Read actual header labels and chip markings; no connector order, supply voltage, I2C address or working display is inferred from the front photo.

| Check | Actual |
|---|---|
| Entire rear and connector visible | PASS: rear photo saved as assets/inventory-2026-10-28/13-lcd-backpack.png |
| Backpack fitted / solder joints visible | Attached HW-61 adapter and soldered 16-pin row visible; not an electrical continuity or workmanship certification |
| Header labels and pin order | PASS: GND / VCC / SDA / SCL, top-to-bottom in supplied rear photo |
| Adapter IC marking and display board identification | HW-61 board marking visible; exact IC text not reliably legible. LCD address and voltage not measured |
| Ready for a specific wiring diagram | Unpowered four-wire diagram issued in WIRING.md; no power or address-scan pass claimed |

If there is no backpack, do not buy one automatically; review the received display and existing parts first. Do not remove a fitted adapter or solder/connect anything for this inspection.

## T06 — LCD wiring: user reports connected; no wired photo supplied

| Connection | Expected | Actual |
|---|---|---|
| LCD GND | Mega GND | User reports wiring complete; no independent photo review |
| LCD VCC | Mega 5V power header; no supply connected yet | User reports wiring complete; final label check instructed before power |
| LCD SDA | Mega digital 20 / SDA | User reports wiring complete; no independent photo review |
| LCD SCL | Mega digital 21 / SCL | User reports wiring complete; no independent photo review |
| Power isolation | USB unplugged during wiring; later USB-only supply | Procedure instructed; no measured voltage or independent visual review |

Review actual endpoints; colours alone do not verify connections. If unclear or shifted by a pin, keep power disconnected and correct that specific connection before continuing. This is an assembly review, not a successful powered LCD test. No electrical measurements or code upload are claimed.

## T07 — first LCD power/backlight observation: PASS by user report

Procedure: BUILD_PROTOTYPE.md, Step 7. Final user label check with power off, then reconnect USB only. No motors/other supply connected. Observe LCD illumination and appearance. Existing Mega diagnostic does not send LCD text.

| Observation | Actual |
|---|---|
| LCD backlight | User reports LCD working as intended after requested power check |
| Blank / dark blocks / characters | Exact appearance not specified; no known text-rendering pass inferred |
| Stable board power / abnormal symptoms | User reports working as intended; no voltage/current/temperature measurement supplied |

If abnormal smell/heat/smoke or power cycling occurs, disconnect USB immediately. If no backlight, investigate power/polarity, connector seating and backlight circuitry/jumper with power disconnected; do not assume failure or raise the supply voltage. No contrast/jumper adjustment issued before the first observation.

Scanner now uploaded/tested in T08 below. Successful displayed text remains a separate future test.

## T08 — I2C backpack address scan: PASS, tool-observed

- Prepared scanner uploaded with --verify to the rechecked /dev/ttyUSB0 port; exit 0.
- At 115200 baud, startup scan and r rescan each found **0x27**, exactly one device, no reported timeout or transaction error.
- Monitor closed with Ctrl+C, exit 0. A few unreadable startup bytes preceded readable tagged diagnostic output.
- Evidence: .build/logs/lcd-i2c-scan-result.json and accompanying upload/serial logs. Address ACK establishes backpack response, not readable LCD text or exact expander identity.

## T09 — LCD text test: PASS after contrast adjustment

Complete source: firmware/lcd_text_test/lcd_text_test.ino. Exact commands/expected output: docs/LCD_TEST.md. Uses measured 0x27 and the same 5V/GND/SDA20/SCL21 wires. Approved hd44780 by Bill Perry1.3.2 installed project-locally. Target compile passed (10574 flash /511 RAM bytes); verified upload to /dev/ttyUSB0 exited0.

Tool-observed result: LCD_TEXT_TEST_V1 READY plus 27 consecutive seconds updates (1–27), no reported LCD init/write/timeout error. Initial partial/duplicate startup line occurred before READY; no restart in subsequent captured seconds. Monitor closed cleanly. Four compile warnings were from Arduino core new.cpp, none from diagnostic/library. Evidence: .build/logs/lcd-text-result.json and associated logs.

**User observation:** “Nothing is appearing.” Photos14–16 saved in inventory evidence; LCD backlight lit blue, no readable characters. Visual test has not passed. Serial/API results above do not override this observation.

### T09a — contrast adjustment: PASS

Hypothesis: contrast too low/high for readable characters. Use the blue rear trimmer, existing USB-only text firmware and unchanged wires; full procedure in docs/LCD_TEST.md. Small gentle movements, proper tool clear of adjacent conductors, never force a stop. If repositioning the boards, unplug USB first. Observe while powered and report readable text / filled rectangles / no change. No new flash or wiring was needed for this correction. **Result:** user now confirms working as intended; photo17 shows readable FRIES MACHINE and Seconds:23. Counter operation is confirmed by the user report and earlier serial updates, not inferred solely from a still photo. No later voltage/RAM diagnostic is necessary for the resolved symptom.

## T10 — three flavour-button connections: completed by user report

Unpowered wiring: button1→22/GND, button2→23/GND, button3→24/GND; working LCD unchanged on20/21 and5V/GND. Full beginner procedure and table in BUILD_PROTOTYPE.md / WIRING.md, Step10.

| Check | Actual |
|---|---|
| Button1 at22 and GND | User reports all buttons connected after retention guidance; no independent photo/continuity check |
| Button2 at23 and GND | User reports connected; method/endpoint photo not provided |
| Button3 at24 and GND | User reports connected; method/endpoint photo not provided |
| USB unplugged during changes; no driver/motor power | Instructed, awaiting result |
| Firmware enables INPUT_PULLUP and matches22/23/24 | Matching input diagnostic now compiled/uploaded; initial raw111 captured |

No button-to-Mega input pass is inferred from earlier meter continuity checks. Each press/release, held press and mapping will be tested with matching input firmware later. Connector difficulty should be resolved before powering; do not assume every panel lug fits a DuPont socket.

## T11 — flavor-button LCD/input diagnostic: PASS by user report after pin correction

Source: firmware/flavor_buttons_test/flavor_buttons_test.ino, ButtonInput.h; operator procedure and exact commands in docs/BUTTON_TEST.md. Pins22/23/24 use INPUT_PULLUP, LCD unchanged at0x27/SDA20/SCL21. No actuator output configured.

| Check | Actual |
|---|---|
| Host helper tests | PASS: 35ms debounce, held press, release/repress, held-at-startup lockout and timer rollover |
| Mega compile | PASS:11692 flash /584 RAM bytes; four Arduino-core unused-parameter warnings |
| Verified upload | PASS: /dev/ttyUSB0, exit0 |
| Serial READY/LCD init | PASS: READY and lcd=OK |
| All released idle |14 status samples raw111, counts0,0,0; no held-at-boot or press events during capture |
| Button1→FLAVOR 1 |PASS by general user report: all buttons working after pin correction; individual count values not supplied |
| Button2→FLAVOR 2 |PASS by general user report: all buttons working after pin correction; individual count values not supplied |
| Button3→FLAVOR 3 |PASS by general user report: all buttons working after pin correction; individual count values not supplied |
| Hold counts once; release/repress adds one |Host timing logic passed; physical hold result not separately itemised; retain later integration recheck |

A HIGH input alone does not rule out a broken/open contact wire. Ask user to press/release each separately and verify matching LCD title/count, then hold one for roughly2seconds to check a single increment. No synthetic serial press can satisfy these tests. Monitor closed cleanly; program remains running. Opening a monitor later may reset counters, so do not infer prior manual counts after a reset. User now reports all buttons working as intended after fixing the connections. No exact endpoint change is inferred from the partly obscured prior photo. Proceed to unpowered driver identification only.

## T12 — module identification reviewed; functional check PASS by user report

Expected: clear component-side and solder-side images of one disconnected module, readable terminal labels and review for visible solder bridges/loose joints. If labels or joints are hidden, request a clearer view before assigning wires. Photographs alone cannot prove electrical function, safe OFF behaviour or current capability. USB and every supply disconnected while handling. No driver GPIO/connection or powered motor test yet.

### T12 photo result and short-screen checkpoint

Photos19–20 received: one module, terminal labels PWM/GND and +/LOAD/− readable. No obvious adjacent-terminal solder bridge visible; exact semiconductor markings not readable and electrical quality untested. Visual identification complete to the terminal-label level only.

**Next measurement pending:** disconnected module + to −, red/black respectively, meter in Ω, leads V/Ω and COM. Record settled value/unit or OL; note changing values. Near the touched-probe baseline is suspicious and prevents power-up pending review. Higher resistance/OL is not a full driver pass. Actual short check, input-ground separation, safe OFF/reset, switching, flyback and powered-current tests remain open. Motor adapter ownership/label still unanswered.

### T12 subsequent result

User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned. Treat prior resistance-reading request as superseded; do not invent an ohmic value or repeat it. Powered-channel integration is separate.

## T13 — one index-switch input: connected by user report; input event not tested

USB/all supplies off; COM→labelled MegaGND, NO→D26, NC empty. Await user wiring report before enabling pull-up/test firmware. Expected later physical diagnostic: released HIGH, actuated LOW, repeatable debounced events. If inverted check actual NO/NC labels unpowered; if stuckHIGH check contact/wire continuity before assuming defective GPIO. Current uploaded button program does not read26. No index input or dispensing test pass yet.

## T14 — one index-switch diagnostic: compile/upload/idle and user physical test PASS

User reports T13 wiring connected. Complete firmware/inputs_index_test matches22/23/24/26 and LCD0x27/SDA20/SCL21. Mega build PASS11922 flash/599RAM; four supplied-core unused-parameter warnings only. Debounce helper byte-identical to prior; existing tests forced to include the new header passed35ms filtering, hold/no-repeat, release/repress, held-at-boot and rollover. Logs .build/logs/inputs-index-*; procedure docs/INDEX_TEST.md.

**User approved upload with “proceed”; verified upload and serial init/idle passed. User subsequently reports the requested physical actuation checklist working as intended.** Captured16 idle1111/counts0,0,0,0/lcdOK samples, no press/held-at-boot/LCD-error tags. Monitor closed exit0; startup unreadable bytes preceded clean tags. Idle is not proof of switch closure. Actual held lever should show ACTIVE/raw1110 and one count, release READY/raw1111 unchanged count, next press one additional count. Input4 in logs means index1 on26. No motor/driver/heater output configured.

**T14 physical result:** User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test.

## T15 — proposed new ground rail superseded by existing user arrangement

USB/all supplies off; otherwise empty rail not connected to Mega/switches. Choose four nearby same-rail holes1–4, use male jumper contacts and meter continuity to test1–2,1–3,1–4. Expect steady beep on each. If any fail, review chosen holes/split rail before wiring. Wait for user result; existing circuit unchanged. No ground distribution or additional switch connection is yet reported.

**T15 clarification:** User states an existing common breadboard GND line is already made for everything and supplies photo21. Accept the existing signal-ground arrangement as user-reported; retain it instead of building a second rail or repeating the empty-rail procedure. Photo shows multiple jumpers near the blue marking but does not prove every endpoint or split-rail continuity. Earlier working LCD/buttons/index1 support those tested signal paths, not every unused rail hole. No numeric continuity reading or new meter pass is inferred. Do not label the earlier suggested three continuity measurements PASS without readings; no repeated/duplicate rail requested.

## T16 — switches2/3 connected by user report; functional test pending

USB/all supplies off; retain existing signalGND and all working wiring. Index2 COM→existingGND/NO→D28; index3 COM→existingGND/NO→D30; NCempty. Wait for both-connected report before preparing/uploading matching diagnostic. Current firmware still reads only22/23/24/26, so no28/30 event or pass expected yet.

**T16 user result:** “done, connected.” No independently observed switch2/3 event or electrical measurement.

## T17 — six-input diagnostic: three-index physical test PASS by user report

Complete inputs_three_index_test matches22/23/24/26/28/30, sameLCD. Mega compile12054flash/619RAM PASS; four supplied-core warnings only. Existing debounce tests forced to use identical new-sketch helper PASS. Exact procedure docs/THREE_INDEX_TEST.md.

User approved with “proceed”; verified upload exit0. Serial READY and15 idle111111/counts0,0,0,0,0,0/lcdOK samples captured, no LCD_ERROR/HELD_AT_BOOT/press events; monitor closed exit0. Startup unreadable bytes before clean tags. Three-index physical events not yet captured/confirmed. After approved upload, idle should be111111, counts0,0,0,0,0,0/lcdOK with all released; this alone is not closure proof. Individually held index1/2/3 should select its own ACTIVE/count and raw111011/111101/111110 respectively; release READY unchanged count, repress one additional count. Verify independent counters and retain button regression test.

**T17 user result:** User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing.

## T18 — remaining basket-switch inventory: three owned, four still needed

Ask whether four additional switches exist beyond three connected index switches; no numerical received count assumed. Await answer before further input wiring or procurement. Actual basket motion/mounting/NC fault strategy remains conditional; no new GPIO, firmware or test executed.

**T18 user answer:** only the3connected switches, no additional ones. Four of the provisional7planned total remain to purchase. Basket endpoints and motion tests deferred; no electrical pass claimed for missing parts.

## T19 — output-free logic simulation: first manual sequence PASS by user report

Source firmware/cycle_logic_test and firmware/tests/cycle_logic_test.cpp. Host tests cover all selections, wrong-index rejection, fresh selected-index requirement,35ms debounce integration, busy-lockout/noqueue, timer boundaries, timeout precedence/latch/explicitreset, invalidconfig and32bitrollover. Initial preimplementation build failed missingheader; no false assertion-red claim. FinalhostPASS. Mega13360flash/797RAM PASS; only4suppliedcorewarnings. Exactcommands docs/CYCLE_LOGIC_TEST.md.

User approved upload; verified flash exit0 and17 idleIDLE/flavor0/seconds0/raw111111/lcdOK samples, taggedREADY, no LCD_ERROR/HELD_AT_BOOT/contact events. Monitor closed exit0; startup partial/duplicate boot text before stable tags. Manual simulation sequence not yet performed/confirmed. Expect selectedmanualindex within15s, thenSIM5swarmup/SIM10scook, thenSIMTIMERSDONE/Basketpending. No actuator pins, no basket or heat/dispensing pass. Test firsthappy-path after approved upload/init; wait before individual busy/wrongindex/timeout/recovery physical checks. No motion/stop qualification from pure software tests.

**T19 manual result:** User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement.

## T20 — physical busy-button lockout and latched completion: PASS by user report

Sameuploadedsketch/wiring. OnboardRESETwithallcontactsreleased, startflavor1→manualindex1/D26within15s, waitSIMCOOK. Press/holdbutton2about2s/release thenpressbutton3beforecountdownends:expectFlavor1unchanged,norestart. AtDONE/Basketpending pressbutton2once:remainstopped,noqueuedcycle. Getuserselection/timer/final-viewresultsandwait. Hostlogiclockoutpassalreadyrecorded;actualtestnotyetconfirmed. No motor/heat/stop qualification.

**T20 user result:** User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred.

## T21 — wrong-index rejection and flavor3 sequence: PASS by user report

Same program/wires, USB logic only. RESET with controls released; select flavor3. Inside same15s response window actuate/release wrong index1/D26 and index2/D28: expect no advancement or restart, Flavor3 unchanged. Matching index3/D30 before deadline should advance to SIM5s/SIM10s/Basketpending. Ask actual result and wait. No physical timeout/recovery/held-index pass inferred from this check.

**T21 user result:** User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test.

## T22 — physical missing-index timeout, fault latch and reset: PASS by user report

Same program/wires, USB-only logic. RESET with controls released; select flavor2, omit all index actuation for15s. Expect SIM FAULT/INDEX TIMEOUT and no timer stages. Late index2/D28 then flavor1 must leave fault latched. Release all and RESET; expect idle without automatic start. Ask actual fault/latch/reset results and wait. No motor jam/stall/emergency-stop qualification inferred.

**T22 user result:** User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop.

## T23 — selected index held before selection: PASS by user report

RESET/release controls; hold index1/D26 for1s, press flavor1 while holding lever. Expect SIM RELEASE IDX, no advancement during2s hold. Release: SIM PRESS INDEX without warm-up. Fresh index1 actuation before same15s deadline should start warm-up. Ask all three observed transitions and wait; code/wires unchanged. No startup-held-button or motor behavior pass inferred.

**T23 user result:** User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred.

## T24 — startup-held flavor-button suppression: PASS by user report

Holdflavor3throughonboardRESETwithothersreleased. Remainidle3safterboot; release3andwait1sremainidle; onlyfreshpressselectsFlavor3. Manualindex3/D30thenallowsnormal5s/10s/Basketpending. Askactualidle/selectionresultandwait. LastcurrentUSBlogiccheck; no newcode/flash/wires, no physicalpower-stopqualification. Wholeprototype/Phase3gates remain open.

**T24 user result:** User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied.

## USB-only logic milestone — planned checks complete

All current input/display/manual simulated-sequence, busy/wrong-index, timeout/reset and held-input checks passed. See USB_LOGIC_CHECKPOINT.md. No further routine repetition without a new change/failure. Actual power/driver/motor/basket/fryer qualification below remains incomplete.

## Later test coverage — gated, not completed

| Test group | Required outcome / what must be investigated if it fails | Status |
|---|---|---|
| All three buttons | Open at rest, connected while held, open again on release | PASS, user report 28 October 2026 |
| Microswitches | Identify COM/NO/NC from labels and isolated measurements; check repeatable actuation without assuming terminal order | PASS, three owned/connected coil-index switches tested; four additional basket switches not owned |
| Bare Mega / USB | Stable USB-only operation and host detection; check data cable, board and interface before driver/software changes | USB power and enumeration PASS; known diagnostic remains T04 |
| Diagnostic LED/serial | Known uploaded sketch behaviour and serial heartbeat; no existing factory blink is accepted as proof of our firmware | PASS: build/upload/serial observed by tools, double-flash L pattern confirmed by user |
| LCD | Verified backpack/pins/address, legible known text; resolve supply, contrast and address before assuming a broken LCD | PASS: power/address/software plus user-readable text after contrast adjustment |
| Controller inputs | Button/index events match the documented pin map, debounce and held-input behaviour | Buttons22/23/24 and indexes26/28/30 passed individual and simulated-selection/lockout/held-input checks; basket inputs and real machine integration pending |
| DC supply / driver | Correct measured voltage/polarity, suitable protection and safe driver OFF on reset/disconnect | Not issued |
| Single secured motor | Controlled start/index stop and jam timeout; validate current/temperature and stop/disconnect before extra channels | Not issued |
| Three coils | Exactly one selected channel per request, repeatable indexed dispensing and safe interrupted-cycle recovery | Not issued |
| Basket/fryer | Appropriate hardware and separate qualified mains/mechanical checks, then controlled full-sequence validation | Deferred |

## Prototype success checklist

- [x] Three red buttons and three owned microswitches passed user-reported contact/input checks; four further basket switches not owned.
- [x] Mega and USB interface tested with known diagnostic firmware: verified upload, heartbeat, receive ACK and user-observed LED pattern.
- [x] LCD test text readable after contrast adjustment; address0x27 and serial/software checks passed.
- [x] Three flavor-button and three coil-index inputs tested individually and in the software simulation; basket input coverage remains open.
- [ ] Actual supply/driver/protection/polarity and safe motor shutdown checked.
- [ ] Each final-use flavour motor/channel and coil index tested.
- [x] USB-only simulated selection/countdowns, busy lockout, wrong-index rejection, missing-response fault/reset and held-input suppression tested.
- [ ] Real dispensing, physical jams/interrupted motion, motor shutdown and mechanism recovery tested.
- [ ] Remaining intended basket/heater prototype scope completed with required mechanical and electrical protection, or an explicitly agreed limited-scope milestone recorded without calling the whole machine complete.
- [ ] User confirms the prototype worked before Phase 3 begins.

No checklist item is complete merely because a component appears in a receipt photograph. Phase 3 has not been authorised.


**T19 execution record:** User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed.
