# Three index switches and three flavor buttons — diagnostic

28 October2026, Asia/Manila. **Phase2 Step17: verified upload/startup/idle and user-reported three-index tests passed.**

## Hardware and software map

Keep the successful LCD and button connections and existing common signalGND unchanged. Index1 was already physically tested with the previous one-index sketch; the user now reports index2/3 connected too. These reports are not independent inspection of every endpoint. No motor adapter owned; drivers/motors/fryer remain disconnected.

| Input | Mega pin | Contact return | Serial input number |
|---|---|---|---|
| Flavor button1 |22|GND|1|
| Flavor button2 |23|GND|2|
| Flavor button3 |24|GND|3|
| Index1 NO |26|COM→existing commonGND, NCempty|4|
| Index2 NO |28|COM→existing commonGND, NCempty|5|
| Index3 NO |30|COM→existing commonGND, NCempty|6|

LCD GND/5V/SDA20/SCL21, measured address0x27. All six contacts use INPUT_PULLUP after the new upload: releasedHIGH/1, actuatedLOW/0. No external5V contact wire or resistor is required. The previous inputs_index_test has now been replaced by inputs_three_index_test; all six pins22/23/24/26/28/30 are active. Breadboard common ground is for low-current signals, not motor current. Power off before changing wires.

Complete source: `firmware/inputs_three_index_test/inputs_three_index_test.ino` and local `ButtonInput.h`. Reuses installed CLI1.5.1, AVR Boards1.8.8, hd44780 by Bill Perry1.3.2 and core Wire; no package or system setup change. User hans previously confirmed in dialout with read/write access on /dev/ttyUSB0. See ARDUINO_SETUP.md, not a new sudo/group instruction.

## What the program does

Each input has its own35ms stable-contact filter and counter. A held input counts once; release rearms it. Held-at-boot inputs must be released before a first counted actuation. Serial actual raw pin readings are not debounced; LCD event/state changes are. Every status lists six inputs/counters in table order. Counters reset on startup; opening serial may reset the board.

LCD initially displays **INDEX 1: READY** and Count0 if index1 is released (ACTIVE if held). Operating another index selects its own **INDEX 2** or **INDEX 3** view and its own Count. Release shows that same index READY without incrementing. The initial view is only index1; all six actual raw inputs appear in serial regardless of which input is on screen. A button press still shows FLAVOR1/2/3 and that button's own count. The last processed event selects the LCD view; operate contacts one at a time for mapping tests.

READY refers only to a released lever, not oil temperature or machine readiness. This diagnostic drives no motor/relay/heater pins; outputLED13 plus LCD/serial are used. It is not homing, dispensing, busy-lockout or full-cycle firmware. A broken NO wire can readHIGH; later index timeout/fault handling is separate.

LCD rows padded to16characters. I2C runs100kHz with25ms timeout; LCD init/cursor/write/timeout errors log LCD_ERROR and stop subsequent display writes while input events continue logging. Stop physical testing and report an error before changing powered wiring.

## Exact build/upload commands

Compilation was shown to the user before execution and passed:

```bash
cd /home/hans/repos/fries-machine
source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/inputs_three_index_test" "$FRIES_PROJECT_ROOT/firmware/inputs_three_index_test"
```

**Upload executed after explicit approval:** user replied “proceed” to the prepared upload/startup-check request. Intended port USB1a86:7523/read-write and source hashes rechecked; upload --verify exited0. Commands below document the completed procedure; no repeated upload/approval needed.

```bash
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" board list --format json
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload --fqbn arduino:avr:mega:cpu=atmega2560 --port /dev/ttyUSB0 --input-dir "$FRIES_PROJECT_ROOT/.build/inputs_three_index_test" --verify "$FRIES_PROJECT_ROOT/firmware/inputs_three_index_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor --port /dev/ttyUSB0 --config baudrate=115200
```

Check tagged INPUTS_3INDEX_V1 READY and with all contacts released:

```text
INPUTS_3INDEX_V1 STATUS raw=111111 counts=0,0,0,0,0,0 lcd=OK
```

Ctrl+C closes monitor. ? prints real input status, never fabricates events. Preserve actual startup/idle log and any errors; do not mark any switch passed from released readings alone.

## Physical checkpoint after approved upload and idle check

Do not issue manual testing until upload/init results are known. Then ask user to operate each lever separately, with other contacts released:

| Lever | Held LCD | Released LCD | Held serial raw |
|---|---|---|---|
| Index1, D26 |INDEX 1: ACTIVE|INDEX 1: READY|111011|
| Index2, D28 |INDEX 2: ACTIVE|INDEX 2: READY|111101|
| Index3, D30 |INDEX 3: ACTIVE|INDEX 3: READY|111110|

For each: press/hold about2seconds adds one to its own count only; release leaves count unchanged; another press adds one more. First unused counter begins0, but compare increments if already exercised. Others' counters must not change. Release returns raw111111. Each lever must select its own index number, not a different one. Recheck flavor buttons separately afterward if the index mapping is correct; final input integration requires all six contacts.

If no event, power off before checking commonGND section, both wire endpoints and NO/COM contact action. If inverted, inspect NO/NC selection unpowered. If two index inputs change together, inspect shared signal wiring/bridges; commonGND is intentional but NO signal lines must stay separate. If a held lever repeats, report counts/serial before edits. Do not infer mechanical indexing or packet-delivery success from hand tests.

**Wait for user mapping/state/count results before further switch, motor or full-cycle steps.**

## Validation already performed

- Mega compilation PASS: **12054 bytes flash,619bytes RAM**. Four supplied Arduino core new.cpp unused-parameter warnings only, none in sketch.
- Local debounce helper is byte-identical to the previously tested helper. Existing host tests forced to include this sketch's header passed debounce/bounce, hold/no-repeat, release/repress, held-at-startup and32bit rollover. Tests do not prove physical pins or LCD operation.
- Compile-time assertions enforce index26/28/30 and Mega SDA20/SCL21; review confirmed each index's press and release calls display its own state/count.
- Verified upload PASS/exit0; INPUTS_3INDEX_V1 READY and15 idle111111/counts0,0,0,0,0,0/lcdOK samples. No held-at-boot, LCD error or press event during capture. Initial unreadable bytes preceded clean tagged startup/status. Monitor closed exit0; new sketch remains running.
- **All-three-index physical mapping/hold/release and button regression still pending user observation.** No physical pass inferred from idle.
- Evidence: `.build/logs/inputs-three-index-compile.log`, `inputs-three-index-host-test.log`, `inputs-three-index-result.json`.


### Execution record — 28 October2026

User approved the prepared three-index diagnostic upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523, read/write access and unchanged source hashes. CLI upload --verify exited0. Serial INPUTS_3INDEX_V1 READY and15 released-idle samples raw111111/counts0,0,0,0,0,0/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical press during capture. Startup unreadable bytes preceded clean tags. Monitor closed Ctrl+C exit0; inputs_three_index_test now runs. No new library, wiring change or actuator output. Physical three-index mapping/hold/release and button regression remain pending.


## Physical user result — 28 October2026

User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing. Next Step18 checks remaining basket-switch availability; no device/wiring/code change.
