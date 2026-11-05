# Control-logic dry run with existing parts

> **Current state, 5 November 2026:** Step24 USB-only logic checks passed; Step25 procurement review saved. Step26 is pending adapter label/polarity review. Adapter is now owned and user reports measured12V; current/power rating, polarity and loaded suitability are not yet established. October missing-adapter/pending-test statements below are historical. Driver GPIO and motor-power wiring remain unassigned. See [current handoff](handoffs/2026-11-05-assembly-resume.md) and [USB checkpoint](USB_LOGIC_CHECKPOINT.md).


28 October2026, Asia/Manila. **Phase2 Step19: all planned USB-only manual logic checks passed by user report; full powered prototype remains incomplete.**

## Purpose and limits

The user confirms **only three roller microswitches**, all already connected and input-tested. Four additional basket-position switches and the12V motor adapter are not owned. This test uses existing buttons/LCD/index switches to check selection, selected-index response, busy lockout, short countdowns and timeout handling without those parts.

**SIMULATION ONLY: keep all MOSFET driver inputs, motors, external supplies and fryer/heater circuitry disconnected.** No actuator output pins, physical-stop function, basket-position handling or real dispensing/heating commands exist in this sketch. Only onboard LED13, existing I2C LCD and USB serial are outputs. It ends at **SIM TIMERS DONE / Basket: pending**; that is not a complete machine or food-cooking test. The original physical PDF design and proposed300s warm-up/600s cooking recipe remain unchanged and unvalidated; the5s/10s timings below are bench-only.

## Existing wiring — no changes

| Component | Mega pin | Other connection | Suggested colour / purpose |
|---|---|---|---|
| Flavor button1 |22|GND|Green, first selection|
| Flavor button2 |23|GND|Yellow, second selection|
| Flavor button3 |24|GND|White, third selection|
| Index1 NO |26|COM→existing commonGND, NCempty|Blue, selected index1 response|
| Index2 NO |28|COM→existing commonGND, NCempty|Yellow, selected index2 response|
| Index3 NO |30|COM→existing commonGND, NCempty|White, selected index3 response|
| LCD GND |GND|Existing signal-ground system|Black, return/reference|
| LCD VCC |5V|No external supply|Red, logic power|
| LCD SDA |20|LCD SDA|Data; same working lead|
| LCD SCL |21|LCD SCL|Clock; same working lead|

All contacts use INPUT_PULLUP: releasedHIGH/1, closed toGND LOW/0. The internal resistor makes a separate5V contact wire unnecessary. Retain actual successful wire colours if different; labels determine connections. Power off before any wiring change. No new GPIO is assigned. Breadboard carries logic/input returns only.

Complete sources in `firmware/cycle_logic_test/`: `cycle_logic_test.ino` handles real contacts/LCD/serial; `CycleLogic.h` handles the state sequence; `ButtonInput.h` filters contact bounce. A **state** is the current stage, such as waiting for an index or showing a cooking countdown. The controller advances one stage at a time using elapsed time, without a blocking delay. Previous inputs_three_index_test source is preserved unchanged; the board now runs approved cycle_logic_test.

## Expected sequence

1. Idle LCD: **SIMULATION ONLY / Select flavor**. Release every lever/button before starting.
2. A new flavor-button press selects that number. If several arrive together, lowest-numbered new press wins deterministically. A button held during startup needs release/repress before it can select.
3. LCD shows **SIM PRESS INDEX / Flavor N 15s**, counting down the response window. Hand-operate the matching indexNO switch; a wrong index cannot advance the sequence. If the matching index is already held when selection starts, LCD instead says **SIM RELEASE IDX**; release then actuate it within that same15s window. This verifies a fresh release/actuation sequence, not a real coil revolution.
4. Once the matching switch is actuated, **SIM WARMUP** counts5seconds, then **SIM COOK** counts10seconds. The selected flavor remains fixed. New button presses while busy are logged IGNORED_BUSY and discarded, never queued or allowed to restart a timer.
5. LCD stops at **SIM TIMERS DONE / Basket: pending**. Buttons cannot start another simulation from this latched view. Press the Mega's onboard RESET button for another test, or send lowercase **r** in serial. Reset is a bench software function, not an emergency-stop circuit.
6. If the selected fresh index response is missing at15seconds, LCD latches **SIM FAULT / INDEX TIMEOUT**. At the exact deadline, timeout wins over a late response. A wrong/stuck index or open wire cannot be qualified from this message alone. Inspect wiring only after USB is unplugged. Reset explicitly before retrying.

Counts in the earlier individual-input diagnostic are replaced by stage/seconds displays in this sketch. All six physical inputs are still logged. I2C errors produce LCD_ERROR with stage/status, stop further LCD writes and leave serial logging available; the simulation may continue in serial, so report any display fault before proceeding. Rows are padded to16characters and only changed rows are sent to the LCD. Timer arithmetic handles32bit millis rollover.

## Tool setup and exact commands

Reuses already installed project-local **CLI1.5.1, AVR Boards1.8.8 and hd44780 by Bill Perry1.3.2**, plus core Wire. No install, sudo, group change or extra driver needed; hans was already in dialout with prior readable/writable /dev/ttyUSB0. ARDUINO_SETUP.md records the setup. All build/cache/temp files stay inside this project.

Executed host tests and target build:

```bash
cd /home/hans/repos/fries-machine
source tools/arduino-env.sh
g++ -std=c++11 -Wall -Wextra -Werror firmware/tests/cycle_logic_test.cpp -o .build/cycle-logic-host-test
.build/cycle-logic-host-test
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/cycle_logic_test" "$FRIES_PROJECT_ROOT/firmware/cycle_logic_test"
```

**Upload executed after explicit approval:** user replied “proceed” to the concrete simulation-upload/startup-check request. Intended port identity/readwrite and unchanged source hashes confirmed; upload --verify exited0. Commands below document the completed operation; no repeated upload/approval needed.

```bash
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" board list --format json
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload --fqbn arduino:avr:mega:cpu=atmega2560 --port /dev/ttyUSB0 --input-dir "$FRIES_PROJECT_ROOT/.build/cycle_logic_test" --verify "$FRIES_PROJECT_ROOT/firmware/cycle_logic_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor --port /dev/ttyUSB0 --config baudrate=115200
```

Expected startup includes `CYCLE_SIM_V1 READY` and `STATUS phase=IDLE flavor=0 seconds=0 raw=111111 lcd=OK` with all contacts released. Opening serial may reset the Mega. Ctrl+C closes monitor; ? reads actual status, r explicitly resets the bench controller. No serial command fabricates a physical index response.

## First physical checkpoint — only after approved upload/startup check

1. With all contacts released, press/release **flavor button2**. Expect SIM PRESS INDEX, Flavor2 and15s response countdown.
2. Within that15seconds, press/release **index switch2 onD28** by hand. Expect SIM WARMUP with Flavor2 and5s, then SIM COOK with Flavor2 and10s.
3. Wait for SIM TIMERS DONE / Basket: pending. Report the observed sequence. This tests no physical motor or cooking action.

**Wait for this user result before issuing more manual fault/lockout tests.** If it times out, record what was pressed and shown; do not claim a bad switch or change powered wiring. A reset returns to idle for a later attempt.

Later checkpoints, issued individually after the first result: choose each other flavor; operate a wrong index first and verify no advancement; press other flavor buttons while busy and check selection/time is unchanged; deliberately omit the selected index and observe timeout/latching; start with selected index already held and verify release/re-actuation is required; verify explicit reset clears fault and held buttons cannot auto-restart. These are software/input checks only, not final jam/stall/thermal or physical-stop validation.

## Evidence and pending work

- Host tests PASS for all3flavors, wrong index, selected-index release requirement, busy-button discard, exact timing boundaries/ceil countdown, timeout precedence/latch/reset, invalid timing configuration,32bit rollover and the real debounce-to-controller chain. First pre-implementation build failed because CycleLogic.h did not yet exist; this is recorded as missing-implementation evidence, not a witnessed behavior assertion failure.
- Mega build PASS **13360 flash bytes /797 RAM bytes**. Four unused-parameter warnings only in supplied core new.cpp; no sketch warnings.
- Three scope-limited simplification checks found no actionable changes; standalone copies of tested diagnostics intentionally retained. Full git-based ce-code-review could not resolve a base because this folder has no Git repository; manual source/output-pin scan performed and limitation recorded in `.build/logs/cycle-logic-review.md`. No Git initialization, commit or PR attempted.
- New sketch verified-uploaded; CYCLE_SIM_V1 READY and17 idleIDLE/flavor0/seconds0/raw111111/lcdOK samples captured. No LCD_ERROR/HELD_AT_BOOT/contact events; partial/duplicate startup text before stable tags. Monitor closed exit0.
- **First manual dry-run sequence not yet performed/confirmed.** The output-free simulation remains running; source unchanged.
- Missing basket switches:4 beyond the3owned; master BOM planned total7 unchanged. Motor adapter missing. Complete prototype and Phase3 gates remain unmet.


### Execution record — 28 October2026

User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed.


## First physical result — 28 October2026

User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement.

## Completed Step20 — busy-button selection lockout passed by user report

Step19 first manual simulation passed by user report. Keep the same uploaded cycle_logic_test and all existing wiring; no new firmware/connection or device command is needed. Drivers/motors/heater/external supplies remain disconnected, USB logic power only.

Read these steps before starting, so the short simulated cooking window is clear:

1. Release all buttons/levers, then press the Mega's small onboard **RESET** button once. Wait for **SIMULATION ONLY / Select flavor**. This is a bench simulation reset, not a real machine emergency stop.
2. Press/release **flavor button1**. Within15seconds press/release **index1/D26**, just as the prior test used flavor2/index2.
3. Wait through the5second SIMWARMUP until **SIM COOK** starts its10second countdown.
4. During SIMCOOK, press **flavor button2**, hold about2seconds, then release. Press/release **flavor button3** while the countdown is still active. Expect **Flavor1** to remain selected and remaining seconds to keep decreasing; no switch toFlavor2/3 or restart to10s/5s.
5. At **SIM TIMERS DONE / Basket: pending**, press/release button2 once. Expect the stopped completion view to remain; busy presses must not have queued another simulation, and this diagnostic needs an explicit reset for another run.

**Check before continuing:** ask whether Flavor1 remained selected, timers continued without restarting and the final view stayed stopped after the extra press. Wait for that physical result before wrong-index/timeout/reset tests or further code/hardware. Do not touch wiring while powered. If any selection/timer changes unexpectedly, report which button and LCD stage/countdown; do not rewire or reflash automatically. Host lockout tests passed previously, but this actual input/LCD lockout check is still pending.



## Busy-button physical result — 28 October2026

User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred.

## Completed Step21 — wrong-index rejection and flavor3 passed by user report

Step20 busy-button check passed by user report. Keep the existing uploaded cycle_logic_test, six input wires and LCD unchanged. This is still an output-free USB-only simulation; motors, drivers, external supplies and heater remain disconnected.

Read the sequence before starting: all index responses below must fit inside the same15-second response window.

1. Release every button/lever, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button3**. Expect SIM PRESS INDEX / Flavor3 with the response countdown.
3. Briefly press/release **index1/D26**, then **index2/D28**. These are roller levers, not flavor buttons. Expect the display to stay on SIM PRESS INDEX / Flavor3 while the countdown continues; neither wrong index may advance or restart it.
4. Before that same15-second window expires, press/release **index3/D30**. Only this matching index should advance to SIM WARMUP5s, then SIM COOK10s, then SIM TIMERS DONE / Basket: pending, retaining Flavor3.

**Check before continuing:** ask whether indexes1/2 were ignored and only index3 advanced the Flavor3 simulation through the timers. Wait for this physical result before timeout/recovery or initially-held-index tests. If the window expires, get the actual display and sequence rather than assuming wrong-index rejection failed. No reflash, serial monitor opening, wiring change or further part purchase is required for this observation. RESET is a bench reset, not an emergency stop.



## Wrong-index physical result — 28 October2026

User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test.

## Completed Step22 — timeout/fault/reset passed by user report

Step21 wrong-index test passed by user report. Use the same cycle_logic_test and unchanged wiring with USB logic power only. All motors/drivers/heater/external supplies remain disconnected. This checks the software's missing-response path, not motor jam/stall protection or an emergency stop.

1. Release all buttons/levers, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press/release **flavor button2**, then **do not operate any roller lever**. Allow its15-second index-response countdown to expire.
3. Expect **SIM FAULT / INDEX TIMEOUT**. No SIM WARMUP or SIM COOK stage should start.
4. While the fault is displayed, press/release **index2/D28**, then **flavor button1**. Expect the fault to remain: a late index or new selection must not resume/restart the simulation.
5. Release every control and press onboard **RESET** once. Expect **SIMULATION ONLY / Select flavor**, remaining idle without a new button press.

**Check before continuing:** ask whether the missing response produced the fault, the fault stayed after the extra switch/button presses, and RESET returned to idle. Wait for that result before initially-held-index/startup-input tests or any further code/hardware. No new upload, serial monitor opening or wiring change needed. If behavior differs, request the actual display/operation sequence; do not infer a defective switch or alter powered wiring. Reset here is a bench software reset and does not qualify a physical safety-stop circuit.



## Timeout/fault/reset physical result — 28 October2026

User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop.

## Completed Step23 — initially-held selected-index check passed by user report

Step22 timeout/fault/reset test passed by user report. Preserve the uploaded cycle_logic_test and successful six-input/LCD wiring. Use USB logic power only; all motors/drivers/heater/external supplies stay disconnected.

Read the sequence before starting; release/re-actuation must occur within the15-second response window that begins at flavor selection.

1. Release all controls, press the Mega's small onboard RESET button once, and wait for SIMULATION ONLY / Select flavor.
2. Press and **hold index1/D26** for about1second before selecting a flavor, allowing its contact filter to settle.
3. Still holding that roller lever, press/release **flavor button1**. Expect **SIM RELEASE IDX** with Flavor1. Keep the lever held about2seconds: warm-up must not begin from the old active index state.
4. Release index1. Expect **SIM PRESS INDEX**, still Flavor1 and inside the same countdown; release alone must not start warm-up.
5. Press/release index1 again before the original15-second window expires. Only this fresh actuation should start SIM WARMUP, then the existing5s/10s simulation and Basket: pending.

**Check before continuing:** ask whether the held index was rejected, release changed the prompt without advancing, and only re-actuation started warm-up. Wait for the physical result before the startup-held-flavor test or further work. No code, flash, monitor opening or wiring changes. If the deadline expires, obtain actual displayed stages/operation order; do not infer a defective input. RESET remains a bench reset, not a hardware safety-stop function.



## Initially-held index physical result — 28 October2026

User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred.

## Completed Step24 — startup-held flavor suppression passed by user report

Step23 initially-held-index test passed by user report. This is the last currently planned manual check for the USB-only control-logic milestone, not completion of the whole machine prototype. Keep cycle_logic_test and all working wires unchanged; all driver/motor/heater/external-supply connections remain absent.

1. Release all roller levers and flavor buttons1/2. Press and **hold flavor button3**.
2. Still holding button3, tap the Mega's small onboard **RESET** button. Keep button3 held while the board restarts and for about3seconds after the LCD returns to **SIMULATION ONLY / Select flavor**. It must remain idle: no selection/index countdown may begin automatically.
3. Release button3 and wait about1second. The display must stay idle; releasing an input held at startup is not a new selection.
4. Press/release button3 again. This fresh press should select **Flavor3** and show **SIM PRESS INDEX**.
5. Within15seconds, hand-operate **index3/D30** to finish the normal5s/10s simulated sequence and Basket: pending.

**Check before continuing:** ask whether the startup-held button and its release left the board idle, and only the new press selectedFlavor3. Wait for that physical result. No new flash, code, serial-monitor session or wire change. If anything starts while the button is held after reset or on release, report the actual display/operation order before modifications. RESET is a bench reset, not an emergency-stop circuit.

After a pass, record the USB logic milestone only: all input mappings and these simulated selection/timer/fault checks passed by user report. Do not advance Phase3 or call dispensing/heating/basket motion tested. Four basket switches and12Vadapter remain missing; supply/protection/mounting/driver-current/stop checks are required before any real motor test. Do not invent more routine tests or repeat passed checks without a new failure/change/uncertainty.



## Final current USB-only logic result — 28 October2026

User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied. No further routine repetition needed. Current resume point and remaining parts/power checks: [USB_LOGIC_CHECKPOINT.md](USB_LOGIC_CHECKPOINT.md). Full functional prototype remains incomplete; no Phase3.
