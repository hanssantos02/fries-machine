# Three flavor-button and LCD input test

28 October 2026, Asia/Manila. **Phase2 Step11.** User reports all three button connections completed/secured and says proceed to the next input test. No new library installation is required. Existing CLI1.5.1 / AVR Boards1.8.8 / hd447801.3.2 reused.

## Wiring and scope

Keep LCD address0x27, SDA20/SCL21 and5V/GND unchanged. Button1 joins digital22 toGND, button2 digital23 toGND, button3 digital24 toGND. USB-only power; no motor, driver, relay or heater connected. User completion report is not independent continuity verification of these six wires. See WIRING.md for terminal table.

Source: firmware/flavor_buttons_test/flavor_buttons_test.ino and ButtonInput.h. This is an input diagnostic, not dispensing/cooking firmware. It reads the actual physical buttons; serial ? reports status and cannot simulate presses. INPUT_PULLUP means HIGH/1 released, LOW/0 pressed. Debouncing requires35ms stable contact. Held buttons count once and need release before another press; buttons held at startup need release before their first counted press. Each counter belongs to its own button. Independent test events are not the final machine busy-lockout/interlock design.

## Exact commands

The user instruction to proceed after completing the requested wiring advances to this input diagnostic; no repeated package/setup approval needed. No install/sudo/group/bootloader action. Target compilation only, first:

```bash
cd /home/hans/repos/fries-machine
source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/flavor_buttons_test" "$FRIES_PROJECT_ROOT/firmware/flavor_buttons_test"
```

After successful compilation and rechecking the intended Mega port, upload/read using:

```bash
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload --fqbn arduino:avr:mega:cpu=atmega2560 --port /dev/ttyUSB0 --input-dir "$FRIES_PROJECT_ROOT/.build/flavor_buttons_test" --verify "$FRIES_PROJECT_ROOT/firmware/flavor_buttons_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor --port /dev/ttyUSB0 --config baudrate=115200
```

Execution completed after the user instructed proceeding with the connected buttons; results recorded below. If the port is absent because USB is unplugged, ask the user to reconnect USB only; do not select a different device automatically. Opening the monitor may reset the Mega and clears these diagnostic counters; this is not persistent machine state.

## Expected before manual presses

LCD row1 BUTTON TEST; row2 Press 1, 2 or 3. Serial tagged READY, raw=111 with all buttons released, counts=0,0,0 and lcd=OK. HELD_AT_BOOT means a pin is LOW: release that button and investigate wiring if it stays LOW with no press. The title remains at the last selection after release.

## User physical input checkpoint

After successful upload/idle checks, press and release one button at a time:

| Button | Expected LCD title | Expected first count | Input |
|---|---|---|---|
|1|FLAVOR1 (with space before digit)|Count:1|22 LOW while pressed|
|2|FLAVOR2 (with space before digit)|Count:1|23 LOW while pressed|
|3|FLAVOR3 (with space before digit)|Count:1|24 LOW while pressed|

Display strings are actually FLAVOR 1 / FLAVOR 2 / FLAVOR 3, padded to16columns. Then hold button1 for about2seconds: its count should increase by one only; release and press again adds one more. If the initial count is already nonzero, compare increments instead of expecting a particular absolute value. Do not touch or move wires while powered. Power off before any connection change.

**Check before continuing:** user reports whether each button selects the correct number, and whether holding gives one increment. Stop/wait for this report before adding index switches or motor drivers. Counts/mapping must not be declared physically passed merely from software tests or idle raw=111.

## Validation limits and evidence

Host test firmware/tests/button_input_test.cpp exercises the same debounce helper: contact bounce filtering, minimum stable interval, held press without repeat, release/repress, held-at-boot lockout and uint32 timer rollover. It passed; log .build/logs/button-input-host-test.log. This is timing logic evidence, not hardware input proof.

AVR compilation passed: **11692 bytes flash /584 bytes RAM**. Four unused-parameter warnings from the supplied Arduino core new.cpp, none in the test/helper. The verified upload to rechecked /dev/ttyUSB0 exited0. Serial showed READY and **14 idle status samples** with raw=111, counts=0,0,0, lcd=OK; no held-at-boot or LCD error line, no press events during capture. Initial unreadable bytes preceded clean boot/status output. Ctrl+C closed the monitor (exit0); the tester remains running.

An unpressed HIGH input can also result from a disconnected wire: idle111 is not proof each switch closes correctly. User subsequently reports correcting the pin connections and all buttons working as intended. Record the input test as passed by user report, distinct from earlier continuity/idle results. Individual count values and a separate physical held-button observation were not itemised; recheck held-input behaviour during later integration.

Evidence: .build/logs/button-input-host-test.log, flavor-buttons-compile.log, flavor-buttons-port-check.json, flavor-buttons-upload.log, flavor-buttons-serial.log and flavor-buttons-result.json. No new library/install or actuator pin output required.


## User result and next checkpoint

User initially questioned the double-row header positions, then reports: “nevermind, fixed it myself, all buttons working as intended, proceed.” Record the three-button input test as passed by user report after a self-corrected connection. Exact changed sockets, individual count values and a separately itemised physical held-button result were not supplied; do not invent them. Recheck held-input behaviour during later integration.

Current phase is Step12: identify one disconnected soldered driver from front/back photos before any new wiring. Keep this firmware uploaded; no reflash needed.
