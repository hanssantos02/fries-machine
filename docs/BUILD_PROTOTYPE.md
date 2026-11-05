# Prototype build — work with received materials

> **Current state, 5 November 2026:** Step24 USB-only logic checks passed; Step25 procurement review saved. Step26 is pending adapter label/polarity review. Adapter is now owned and user reports measured12V; current/power rating, polarity and loaded suitability are not yet established. October missing-adapter/pending-test statements below are historical. Driver GPIO and motor-power wiring remain unassigned. See [current handoff](handoffs/2026-11-05-assembly-resume.md) and [USB checkpoint](USB_LOGIC_CHECKPOINT.md).


Updated: **28 October 2026**, Asia/Manila.

The user explicitly authorised **Phase 2** with available materials. Outstanding purchases remain in the BOM; they do not prevent isolated unpowered input tests. We will complete one physical checkpoint at a time and wait for the user's observations before advancing. This guide does not authorise Phase 3.

## Completed Step 1 — three disconnected pushbuttons

### What this checks

A pushbutton is a manually operated electrical contact. Our intended flavour button is **normally open**: its two terminals are disconnected at rest. It is **momentary**: pressing connects them, and releasing disconnects them again. The red cap does not prove either behaviour; this test checks the delivered part.

**Continuity** means there is an electrical path between the meter probes. The meter supplies its own small test signal. A typical continuity setting beeps for a low-resistance path; the exact beep threshold depends on the meter. `OL` or an open-circuit indicator means no conducting path in this test.

### Safety before touching the probes

- Test **one loose pushbutton only**, disconnected from every other part.
- No USB, adapter, motor, capacitor or wall power is connected to this test.
- Put the black lead in **COM** and the red lead in the jack marked **V/Ω** or its meter-specific voltage/resistance equivalent. Do not use an A, mA or 10 A current jack.
- If the meter jack/mode labels are unclear, stop and ask for help identifying them rather than guessing.
- Do not perform resistance/continuity checks on powered circuits. Do not use this test on a household outlet or on a capacitor.

### Do this one component test

1. Take one red button out of its bag. Set it on a clean non-conductive surface. Its two metal terminals must be accessible and unconnected.
2. Select the meter's continuity/beeper setting. Some meters share this with diode/ohms mode and require a SELECT button; follow its actual labels. If there is no beeper function, resistance mode can show the same contact change.
3. Touch the probe tips together briefly. Note the beep and displayed resistance. This establishes that the meter/probes work and gives the shorted-probe baseline. Separate them; the meter should return to its open indication.
4. Touch one probe to each button terminal. Probe polarity does not matter for this isolated mechanical contact. Avoid letting the probe tips touch each other, which would create a false pass.
5. Observe with the button **released**, **held pressed**, then **released again**. Keep the probes in contact with the two separate terminals throughout. If convenient, repeat slowly to confirm the change is repeatable.

| Button state | Expected for the selected normally-open momentary type |
|---|---|
| Released | No beep; open indication such as OL |
| Held pressed | Beep; resistance close to the shorted-probe baseline |
| Released again | No beep; returns to open |

**Check before continuing:** Report the three states and the shorted-probe check. If readings are unstable, first check probe contact and mode. If it stays connected after release or conducts only while released, report the actual behaviour; do not assume the ordered contact type was delivered. Result recorded 28 October 2026: user confirms all three buttons matched the expected outcomes. All three pass this contact-action check; numeric resistance values were not supplied.

**Step 1 complete by user report.** No firmware or power supply was required.

Reference for the powered-off continuity method: [Fluke continuity testing guide](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity). This is measurement guidance, not certification of the delivered parts.

## Completed Step 2 — disconnected microswitches

A microswitch is a small snap-action contact operated by a lever or roller. Here it will later signal a mechanism position to the Mega. A click alone does not prove an electrical connection.

### Identify the actual terminals

- **COM** or **C**: the common contact that switches between the other two.
- **NC**: normally closed, connected to COM when the lever is released.
- **NO**: normally open, disconnected from COM when the lever is released.

Read the markings moulded or printed beside the terminals; do not assign them by physical position or a generic diagram. If labels are unreadable, stop and send a clear close photo of the switch's marked sides and terminals.

### Safety and procedure

Keep the switch completely disconnected. No Arduino, USB, adapter, motor or capacitor connects to this test. Use the meter's black COM jack and red V/Ω jack, continuity mode; never a current jack. Only actuate the lever through its normal click/travel without bending or forcing it.

1. Take **one** loose microswitch. Confirm its COM, NC and NO labels.
2. Verify the meter by touching the probe tips together, then separating them.
3. Place the black probe on switch COM and red probe on switch NC. Keep tips separate. Observe released, gently held actuated, then released again: expected **beep → no beep → beep**.
4. Keep the black probe on COM and move the red probe to NO. Repeat: expected **no beep → beep → no beep**.
5. Record both sequences. A connected contact should read close to the shorted-probe resistance; exact meter beeper thresholds vary. Avoid resting fingers on exposed tips/contact surfaces if interpreting high-resistance readings.

**Result, 28 October 2026:** user confirms all switches work as intended following the issued check. Record the received microswitch batch as passing the reported COM–NC and COM–NO action checks. Exact switch count, individual labels and numeric resistance values were not supplied; do not substitute the planned quantity of seven for a counted quantity.

## Completed Step 3 — bare Mega USB power and detection

### What this checks

The Mega is the controller that will read switches, run the sequence and command driver signals. A USB connection can power the bare board and also carry programming/serial data. A lit power LED establishes only that power reaches the board; it does not prove data communication or our firmware.

### Check before applying power

1. Keep the board disconnected while inspecting it. Remove all jumper wires, shields and other modules from its headers. Look for loose wire strands, solder bridges between pins, debris, damaged connectors or obvious damage. If any is present, stop and send a photo.
2. Place the board on a clean, dry, nonconductive surface such as cardboard or a plastic stand. Keep it off metal and the outside of antistatic bags. Do not attach motors, drivers, the LCD, a barrel adapter or a bench supply.
3. Use a USB **data** cable that matches the actual board connector. The full-size Mega-style board normally has a square USB Type-B socket with two bevelled corners; the computer end must fit the computer directly. Do not force a plug. If the cable ends are unclear or do not match, send a photo of both ends before trying another connection. A cable supplying power alone is not proof it carries data.

### One physical checkpoint

Connect the bare board directly to the computer over USB only. Observe the ON/power indicator and any other LEDs. A preloaded L LED may blink or remain steady; do not require a particular blink pattern before our diagnostic is uploaded. Disconnect immediately if there is smoke, a burning smell or obvious abnormal heating; do not touch components to test their temperature.

**Result:** user reports ON lit and L blinking. Read-only host inspection now detects /dev/ttyUSB0, VID:PID 1a86:7523, product USB Serial, driver ch341-uart, readable and writable. Basic power/enumeration pass; no known-sketch upload or functional GPIO claim. Unpowered visual inspection was instructed but not explicitly reported separately.

### Linux baseline already checked (read-only)

On 28 October 2026, the agent ran:

```bash
command -v arduino-cli
command -v pio
command -v platformio
id -nG
ls -l /dev/ttyACM* /dev/ttyUSB* /dev/serial/by-id/* 2>/dev/null
```

No CLI executable path was returned for those three command names; this is a PATH check, not an exhaustive search for every installed IDE/tool. The current hans process already includes dialout. No matching serial device nodes were returned before this USB checkpoint. The listing's nonzero exit status reflected missing matches, not a diagnosed board failure. This baseline does not establish that a connected board is recognised.

After the user's USB result, read-only detection and port access checks succeeded as recorded above. No installation is needed for the initial power-light observation. Do not run sudo/usermod, install packages/cores or flash a device without presenting the exact commands and obtaining the user permission required by AGENTS.md. No dialout change is currently indicated. The complete diagnostic and build/upload instructions are now available and executed in Step 4; a power LED alone is not its success criterion.

References: [Arduino connection checks](https://support.arduino.cc/hc/en-us/articles/4412955149586-If-your-board-is-not-detected-by-Arduino-IDE), [Linux serial permissions](https://support.arduino.cc/hc/en-us/articles/360016495679-Fix-port-access-on-Linux). These support the method, not identification of the actual clone USB interface.

## Completed Step 4 — known diagnostic passed

The complete diagnostic source is saved in `firmware/mega_diagnostic/mega_diagnostic.ino`. Read [ARDUINO_SETUP.md](ARDUINO_SETUP.md) for exact proposed installation, compilation, port listing, upload and monitor commands, expected output, pinned versions and troubleshooting.

It uses only the built-in LED on pin 13 and USB serial: two short flashes every two seconds, a status line every second at 115200 baud, and an ACK when ? is received. Keep the board bare and USB-only. No external part is wired in this checkpoint.

User approved setup, compilation, diagnostic upload and serial capture. All completed successfully: checksum verified, 3334-byte program / 196-byte RAM build, verified upload exit 0, 27 consecutive heartbeat messages and ?/ACK reply. The serial monitor is closed; the program remains running. **Result:** user confirms the two short flashes and pause work as intended (28 October 2026). T04 complete; this checks the diagnostic and USB interface, not every GPIO or the entire machine. No external wiring yet. Logs/results are in .build/logs/; see TESTING.md.

## Completed Step 5 — LCD rear identified

The LCD is the screen for later countdowns and status. An **I2C backpack** is a small adapter board on the rear of some displays that lets the controller communicate through a four-pin connector. The received front photo does not show whether this adapter is installed or how its connector is labelled.

1. Unplug the Mega USB cable before any new handling or wiring. Leave all other supplies disconnected. The LCD must remain unpowered.
2. Turn the LCD over without removing or unsoldering anything.
3. Send a clear photograph of the **entire back**, especially any small adapter board, the pin labels beside its connector, the chip's printed marking and the soldered row joining the adapter to the display. If one photo cannot show the labels, add a close-up of that area.

Typical labels to look for are GND, VCC, SDA and SCL; these are examples only, not an instruction to assign positions or connect them. GND is the circuit return, VCC is the supply input, SDA carries communication data and SCL carries its clock. Actual labels, module identity and intended voltage must be reviewed before a pin table is issued. Do not infer voltage from VCC alone.

**Result:** rear photo now shows an attached HW-61 backpack, four-pin male header labelled GND/VCC/SDA/SCL from top to bottom in this view, and a blue trimmer. Chip text is not sufficiently legible to assign a precise IC, and no address/powered operation is yet checked. No additional backpack purchase is needed.

## Completed Step 6 — LCD wires connected, user report

An I2C link uses SDA (data) and SCL (clock); the display also needs supply and ground. The Mega uses digital **20 for SDA** and **21 for SCL**, verified against its official pinout. Use the complete pin table and diagram in [WIRING.md](WIRING.md), Step 6.

### Before connecting

**Unplug Mega USB and keep the barrel jack and every other supply disconnected.** Do not connect a 12 V adapter to this display or put its VCC on VIN. Keep motors, drivers and other modules disconnected. Leave the supplied trimmer and jumpers alone for this checkpoint.

1. Lay the LCD and Mega on a dry nonconductive surface, with their connector labels visible.
2. Take four male-to-female jumper wires. The female socket ends fit over the LCD pins; the male pin ends fit into the Mega's labelled sockets. Colours only help identify wires; actual endpoints matter.
3. Connect **LCD GND → Mega GND** (black suggested).
4. Connect **LCD VCC → Mega 5V** in the POWER header (red suggested). This is the planned 5 V LCD supply; keep it unpowered now. Do not use 3.3V, VIN, RESET or a numbered digital pin.
5. Connect **LCD SDA → Mega digital 20** (blue suggested).
6. Connect **LCD SCL → Mega digital 21** (yellow suggested).
7. Trace all four wires against WIRING.md; check each end seats securely on just one intended pin/socket. A breadboard is unnecessary for this direct connection.

**Result:** user reports “done, wires connected, proceed.” No wired photo was supplied, so do not claim an independent visual inspection. Use a final user-performed end-to-end label check before the next USB-only power observation. The existing diagnostic only drives the L LED and serial link; it cannot display countdown text.

No LCD power, I2C scan, library install, firmware flash or contrast adjustment has been performed. The generic display's exact electrical rating/IC is not independently established by its HW-61 marking; later powered-test acceptance will be kept distinct from this unpowered wiring step.

## Completed Step 7 — LCD USB-only first power observation

1. With USB still unplugged, trace the actual endpoints one last time: **GND → GND, VCC → Mega 5V, SDA → 20, SCL → 21**. Ensure sockets are not shifted by one pin and no adjacent exposed pins touch. Colours alone do not establish the connection. If an endpoint is uncertain, leave power off and ask for help/photo review.
2. Keep the barrel jack and every other supply disconnected; only the Mega and LCD are connected. Place both boards on a dry nonconductive surface.
3. Reconnect the Mega's USB cable to the computer. Observe whether the LCD backlight comes on. Disconnect immediately if there is smoke, a burning smell, abnormal heating or repeated power cycling; do not feel components to test their temperature or move wires while powered.

**Check before continuing:** report whether the LCD backlight illuminates, and whether you see blank space, dark blocks or any characters. No readable text is required yet: the currently uploaded Mega diagnostic does not initialise the LCD. A missing backlight is a symptom to investigate, not proof the whole LCD is faulty. Leave the contrast trimmer and backpack jumpers unchanged until the observation is reviewed.

**Result:** user reports “lcd working as intended, proceed.” The first power observation passes by user report; exact screen appearance was not specified and readable test text is not inferred. User directs continuation to the prepared address scan. Do not operate motors or connect another supply. The user requested proceeding after wiring; no extra permission is needed for this instructed low-voltage power observation.

### Address scanner — uploaded and passed in Step 8

`firmware/lcd_i2c_scan/lcd_i2c_scan.ino` is a complete, commented diagnostic for Mega SDA20/SCL21. It compiles with installed AVR Boards 1.8.8 and bundled Wire; no additional library installation. It performs an address-only scan at 100 kHz, reports responding addresses over serial at 115200 baud, has a 25 ms Wire timeout and stops on a held-low bus/transaction fault. Send r to repeat. It does not initialise LCD text or claim an address before measurement.

Compile-only command already run:

```bash
cd /home/hans/repos/fries-machine
bash -c 'source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/lcd_i2c_scan" "$FRIES_PROJECT_ROOT/firmware/lcd_i2c_scan"'
```

Compile log: `.build/logs/lcd-i2c-scan-compile.log`. Compilation alone did not communicate with the board. Following the user's power confirmation/proceed instruction, the prepared scanner was uploaded with --verify (exit 0); two scans each found 0x27, one device, no scanner error. Serial log/result are in .build/logs/.

## Completed Step 8 — address confirmed; text test prepared

Scanner startup and r rescan both reported **FOUND 0x27 / SCAN_COMPLETE devices=1** at 115200 baud. The monitor is closed. This confirms the backpack responds at that address, not that LCD characters render correctly.

The complete next sketch is `firmware/lcd_text_test/lcd_text_test.ino`; [LCD_TEST.md](LCD_TEST.md) contains exact proposed commands and expected output. It will show FRIES MACHINE and advancing Seconds: using the same wiring. It uses **hd44780 by Bill Perry 1.3.2**, which is not yet installed; this library configures the expander-to-LCD mapping at the measured address. It handles init/write/timeout errors and drives no actuators.

The user explicitly approved the concrete library/text-test execution with “proceed.” It has now been installed/compiled/uploaded and serial-checked in Step9; no further permission for that completed action is pending. No hardware connection change needed. See LCD_TEST.md for exact commands and evidence.

## Completed Step 9 — LCD text and contrast check passed

Approved execution passed: hd44780 1.3.2 installed project-locally; Mega compilation succeeded (10574 bytes flash /511 bytes RAM); upload with verification exited0. Serial reported LCD_TEXT_TEST_V1 READY and 27 increasing seconds values without a reported LCD error. Monitor is closed; text diagnostic remains running.

Keep the same USB-only Mega/LCD wiring. **Actual observation:** user reports nothing appears; photos show a lit blue screen without readable characters. Visual text check has not passed. Successful API/serial output is not independent proof of visible characters.

Next one physical check: adjust the blue rear contrast trimmer gently while running the existing USB-only text test. Full beginner procedure and short-circuit precautions are in LCD_TEST.md, current Step9 troubleshooting. Watch for letters or filled character rectangles. Keep wiring/jumpers unchanged, do not force the trimmer, and report the result before any further step.

**Result:** user confirms “now working as intended” after the contrast check. Photo17 clearly shows FRIES MACHINE and Seconds:23. The reported contrast adjustment resolved visibility without a new code upload. LCD text test passed; retain its setting. This is not cooking firmware or a Phase3 transition.

## Completed Step 10 — three flavour-button connections reported

Each red pushbutton is a normally-open momentary contact: it connects its two terminals only while held. We will use the Mega's internal pull-up resistors in the next input-test program, so each button connects a digital input to GND. A pull-up is a weak internal connection that holds the unpressed input HIGH; pressing makes it LOW. No added resistor or 5V wire goes to these button contacts.

1. Unplug USB and every other supply. Leave the four working LCD wires in place; no driver or motor is connected.
2. Identify the Mega's **digital22,23,24** labels. They are in the double-row digital connector, not the numbered analog header. The exact printed numbers determine the socket, not a guessed left/right row.
3. Connect one terminal of button1 to **22**, the other to an unused **GND** socket.
4. Connect button2 similarly to **23** and another unused **GND** socket.
5. Connect button3 similarly to **24** and another unused **GND** socket.
6. Use one secure wire per Mega socket. Each button's two contact terminals can be exchanged; these switches have no polarity. Do not put a button terminal directly on5V/VIN. See WIRING.md Step10 for colours, purposes and full ASCII diagram.

**Check before continuing:** trace all six endpoints and report the three buttons connected, leaving USB unplugged. A photo is useful if connector positions are unclear. If jumper ends do not fit the button terminals, stop and show/describe them before soldering or improvising. Keep motors and their supplies disconnected.

### Connector retention question — current Step10 sub-check

User asks how to keep fitting jumpers attached. Keep USB unplugged. If a jumper seats snugly and proper electrical tape is available, retain each connector separately and anchor its insulated wire to the stationary button body/support with slack. This strain relief prevents button presses pulling on the contact. Tape is not a fix for loose/intermittent electrical contact. Try one unpowered lead first and report gentle-pull retention/free-button action; full advice and durable alternatives are in WIRING.md, Keeping the prototype button leads attached.

Suitable solder-terminal pigtails with individual heat-shrink are the durable alternative, after confirming terminals/insulation. No cutting/soldering or new purchase directed now. Keep Mega-side connections removable; anchor cables instead of soldering/gluing sockets.

User now reports all buttons connected and says proceed. Matching input diagnostic has been prepared/compiled/uploaded in Step11 using already installed Wire/hd447801.3.2. No independent photo of all six endpoints was supplied; do not infer physical input passes from the completion report.

## Completed Step 11 — flavor-button input test, user report

The user requested proceeding after connecting all buttons. Uploaded complete firmware/flavor_buttons_test with 35ms software debounce and startup-held protection. Host timing tests and Mega compilation passed (11692 flash /584 RAM bytes); verified upload exited0. Serial READY and14 idle samples show raw111, counts0,0,0, lcd=OK, no errors/held inputs. Monitor closed; tester running. Existing libraries reused; no new installation.

Read [BUTTON_TEST.md](BUTTON_TEST.md) for complete expected output, commands and limits. LCD initially shows BUTTON TEST / Press1,2or3 (with normal spaces).

1. With USB-only power and unchanged secure wiring, press/release **button1**: expect FLAVOR 1 and its Count increasing by1.
2. Press/release **button2**, then **button3**, separately: expect FLAVOR 2 and FLAVOR 3 respectively, each with its own count.
3. Hold any one button for about2seconds: its count increases once, not continuously. Release, wait a moment, and press again: it increases once more. The last selection remains on screen after release.

**Check before continuing:** report whether each button selects the matching number and whether holding counts only once. Do not change wires while powered. If a mapping/contact is wrong, record which input and what LCD shows; unplug before corrections. Do not add index switches or motor drivers until these results are reviewed. These are test identifiers, not assigned real flavour names or active dispensing/cooking commands.

**User result, 28 October 2026:** User initially questioned the double-row header positions, then reports: “nevermind, fixed it myself, all buttons working as intended, proceed.” Record the three-button input test as passed by user report after a self-corrected connection. Exact changed sockets, individual count values and a separately itemised physical held-button result were not supplied; do not invent them. Recheck held-input behaviour during later integration.

## Completed Step12 — module identification and user test report

A MOSFET module is an electronic switch: a small controller signal controls a separate motor-power circuit. The selected BOM family is LR7843, but actual terminal labels and board layout must be inspected before assigning wires. A component name alone does not establish a module pinout or an adequate flyback-current path.

1. Unplug Mega USB and disconnect every external supply before handling or moving connections. Keep the successful LCD/button wiring in place.
2. Set **one loose soldered MOSFET module** on a nonconductive surface. Do not connect it to the Mega, a motor or a power supply yet.
3. Supply clear photographs of its component/label side and underside/solder joints. Include the whole module and all terminal markings. If a marking is unreadable, report that rather than assigning a terminal by position.

**Check before continuing:** review the user's actual module labels, connector assembly and visible solder joints before issuing its connection table. A photograph can reveal obvious bridges or loose joints but cannot certify electrical operation. Ask whether the regulated 12 V motor adapter is already in hand; obtain its label and measured output/polarity at a later power-supply checkpoint. No driver GPIO is assigned and no wiring, installation, flash or motor-power test is issued at Step12. The current button tester stays uploaded; no software change is needed for this identification step.

**Photo review received:** one module shown on both sides, labels PWM/GND and +/LOAD/− readable. See WIRING.md Step12 photo review for orientation, terminal roles and limits. No obvious adjacent-net solder bridge visible; electrical condition untested.

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

**Subsequent user result:** User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned. The earlier requested resistance reading is not repeated.

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

## Subsequent checkpoints — not instructions to perform yet

| Stage | Evidence needed before issuing its physical instructions |
|---|---|
| Bare Mega USB checkpoint | Basic power and enumeration passed; retain no-external-wiring arrangement |
| Onboard-LED/serial diagnostic | Step 4 complete: setup/build/upload/serial and user LED observation passed |
| LCD check | LCD text/contrast passed; keep same wires/address0x27 |
| Button input firmware | Step11 uploaded; all buttons working per user after pin correction; separate hold details not itemised |
| Index input firmware | D26 index1 diagnostic uploaded and physical test passed by user; two other inputs follow shared-ground rail verification |
| MOSFET/motor channel test | Actual soldered board/pin labels, safe OFF/reset handling, validated DC supply/protection, measured polarity, secured unloaded motor and disconnect arrangement |
| Three-channel dispenser test | Individual channel passes, mounts/couplings/cams and packet/coil fit, then jam/index fault handling |
| Basket/fryer integration | Separate mechanical/power/stop/protection requirements met; qualified mains review and later explicit test steps |

User approved Step 4 execution. Project-local CLI 1.5.1 / AVR Boards 1.8.8 setup, diagnostic compilation/upload and serial heartbeat/ACK have now passed; exact commands and evidence are in ARDUINO_SETUP.md and .build/logs/. hd447801.3.2 was subsequently installed after approval for Step9; no new USB driver installed. The user has now confirmed the expected LED pattern. LCD four-wire connection and first USB-only power observation now issued; no actuator operation.
