# One index-switch and three-button diagnostic

28 October 2026, Asia/Manila. **Phase2 Step14: verified upload/idle and physical lever test passed by user report.**

## Wiring and power

User reports Step13 connected. This is a completion report, not independent endpoint/continuity verification. Retain LCD GND/5V/SDA20/SCL21, measured address0x27; buttons22/23/24 toGND. Index1 microswitch: **COM→GND, NO→D26, NC empty**. Internal pull-up on26 is enabled only by this new sketch after upload. The previous button-only sketch has now been replaced by inputs_index_test; D26 pull-up/readout is active.

Reconnect USB only when requested for upload; leave motor drivers/motors/supply/fryer disconnected. Release all buttons and the roller lever. Never move wiring while powered. NO contact released gives HIGH/1; actuated gives LOW/0. A broken wire also reads HIGH, so this is a manual input diagnostic, not a proven fail-safe limit or complete dispenser/indexing control.

## Complete source and behaviour

`firmware/inputs_index_test/inputs_index_test.ino` and its local `ButtonInput.h` form a standalone ready-to-build sketch. Reuses installed **Arduino CLI1.5.1, Arduino AVR Boards1.8.8, hd44780 by Bill Perry1.3.2**, plus core Wire. No install or system change required; hans already has dialout and prior /dev/ttyUSB0 read/write access. See ARDUINO_SETUP.md for recorded setup/permissions; do not run sudo or change groups unnecessarily.

All four inputs have35ms stable debounce, independent counters, release-to-rearm and held-at-startup count suppression. Index1 is input4 in serial records, array position3 in code. Its real state is shown at boot, even if held, but a startup-held lever needs release before the first counted actuation. LCD rows are padded to16characters to erase old text. I2C25ms timeout and init/write failures produce serial LCD_ERROR and stop later LCD writes while continuing input logs. No actuator output is configured; only onboard LED13 and the usual LCD/serial interface outputs.

Buttons keep FLAVOR 1/2/3 plus their own Count display on presses. An index transition restores INDEX1 view. The latest event owns the LCD view; status serial still reports all four raw pins/counters. This is not final busy-cycle or cooking software.

## Exact commands

Compilation was shown to the user before execution and passed:

```bash
cd /home/hans/repos/fries-machine
source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/inputs_index_test" "$FRIES_PROJECT_ROOT/firmware/inputs_index_test"
```

**Upload completed after explicit approval:** the user replied “proceed” to the concrete upload/serial-check request. Rechecked intended port USB1a86:7523 and read/write access; verified upload exited0. Commands below are the executed procedure, not a request to flash again.

```bash
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" board list --format json
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload --fqbn arduino:avr:mega:cpu=atmega2560 --port /dev/ttyUSB0 --input-dir "$FRIES_PROJECT_ROOT/.build/inputs_index_test" --verify "$FRIES_PROJECT_ROOT/firmware/inputs_index_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor --port /dev/ttyUSB0 --config baudrate=115200
```

Monitor opening may reset the board and clears diagnostic counts. Ctrl+C closes the monitor. No serial input synthesises switch events: ? prints actual pin status only. Preserve logs for real init/idle/physical observations separately.

## Expected after approved upload

With all contacts released, LCD:

```text
INDEX 1: READY
Count:         0
```

Serial includes:

```text
INPUTS_INDEX_V1 READY: 35ms debounce, hold counts once.
INPUTS_INDEX_V1 STATUS raw=1111 counts=0,0,0,0 lcd=OK
```

Idle1111 alone can also mean disconnected wires, so it is not a switch pass.

After successful upload/idle check, issue one physical checkpoint and wait for the result:

1. Press and hold the roller lever roughly2seconds. After35ms stable closure the LCD should read **INDEX 1: ACTIVE** and Count increase by1 only. Serial logs `PRESS input=4 pin=26 count=1` (or the next count), raw1110 while other contacts are released.
2. Release: LCD returns **INDEX 1: READY**, Count unchanged; serial RELEASE input=4 and raw1111.
3. Press/release again: one additional count. Test only this one switch first; don't add the other switches until results reviewed.

If pressed at boot, display starts ACTIVE/count0, serial HELD_AT_BOOT input=4. Release then actuate normally. If reversed behaviour, unplug and check NO/NC against markings. If always READY, unplug and trace both leads/check contact closure. If always ACTIVE, release lever then inspect possible short/NC mix-up unpowered. If display is blank, report backlight/serial results; preserve previously successful contrast/wires until evidence indicates otherwise. No new powered test is implied by these troubleshooting branches.

## Actual validation so far

- User reports one microswitch connected; no hardware input event observed yet.
- Mega compile PASS: **11922 flash bytes /599 RAM bytes**. Four unused-parameter warnings solely in supplied AVR core new.cpp; no sketch warnings.
- Reused debounce helper is byte-identical to the prior tested helper. Existing host tests run with this new sketch's header pre-included passed debounce, held/no-repeat, release/repress, startup-held and32bit timer rollover. They verify timing logic, not physical pins or LCD output.
- Verified upload PASS/exit0; serial READY and16 idle samples raw1111/counts0,0,0,0/lcdOK; no HELD_AT_BOOT/LCD_ERROR/press events. Monitor closed Ctrl+C exit0. The new input/index program remains running.
- Initial unreadable bytes preceded clean tagged startup/status lines. Physical index/LCD actuation test remains pending user observation; idle alone does not prove contact closure.
- Logs: `.build/logs/inputs-index-compile.log`, `inputs-index-host-test.log`, `inputs-index-result.json`.


### Execution record — 28 October2026

User approved the prepared upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; source hashes matched compiled source. CLI upload --verify exited0. Serial INPUTS_INDEX_V1 READY plus 16 released-idle samples raw1111/counts0,0,0,0/lcdOK; no LCD error, held-at-boot tag or physical input press during capture. Unreadable startup bytes preceded clean tagged output. Monitor closed Ctrl+C exit0; inputs_index_test now runs on the board. No package install or wiring change. Physical lever test remains pending.


## Physical user result — 28 October2026

User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test. Current Step15 verifies an empty breadboard rail for later shared input ground; the uploaded index1 diagnostic is retained.
