# LCD communication and text diagnostic

28 October 2026, Asia/Manila. **LCD diagnostic complete: upload/serial and readable text passed after contrast adjustment. Current project stage: Phase2 Step10 button wiring.**

## Actual results

The user reports the first LCD power check worked as intended. This records the requested power/backlight observation, not successful known text. Wiring was reported connected by the user; no complete wired photo was reviewed. Rear module photo confirms the GND/VCC/SDA/SCL labels.

The user said to proceed to the prepared scanner. Its approved next-step upload used the existing CLI/core and `/dev/ttyUSB0`, with `--verify`, and exited 0. Read-only port identity remained USB 1a86:7523 with read/write access. Serial at 115200 baud showed both a startup scan and a deliberate `r` rescan:

```text
FOUND 0x27
SCAN_COMPLETE devices=1
```

Both found one device at **0x27**, with no scanner timeout or transaction error. This measures an address acknowledgement, not the LCD panel's text rendering or an exact expander part number. A few unreadable bytes preceded the clean boot tag; scanner lines were readable. Monitor closed with Ctrl+C, exit 0.

Evidence: `.build/logs/lcd-i2c-scan-compile.log`, `lcd-i2c-scan-upload.log`, `lcd-i2c-scan-serial.log`, `lcd-scan-port-before-upload.json` and `lcd-i2c-scan-result.json` in the same log directory. Scanner has now been replaced by the approved text diagnostic below.

## Current test: readable title and advancing seconds

Source: `firmware/lcd_text_test/lcd_text_test.ino`. It uses the measured address **0x27**, 16 columns / 2 rows, Mega SDA20/SCL21 and 115200-baud serial. Keep LCD GND→GND and VCC→5V, USB-only power, no other devices or supplies.

Approved and installed library: **hd44780 by Bill Perry, version 1.3.2**, installed under this project's `.tools/arduino/user/libraries/`. The `hd44780_I2Cexp` class checks and automatically configures supported expander-to-LCD pin mappings at the specified address. This avoids assuming a generic LiquidCrystal_I2C fork or backpack mapping. It supports PCF8574/MCP23008 backpacks, but the scanner does not prove which chip is fitted here.

The official Arduino library index lists 1.3.2 with SHA-256 `c1408b8129a225fa4e2f3e2e3bef709c1f98ca53dadedfcc9b071f083e504f89`. No additional library dependencies are listed; Wire is supplied by the installed AVR core. CLI checks the downloaded library against index metadata.

### Exact commands — approved and executed

No sudo, new driver or board-core update is needed. The following shell uses the existing project environment to keep data/cache/temporary files inside the project. The user explicitly approved this concrete library installation, compilation, upload and serial test with “proceed.” These commands were then executed. Future installations/uploads continue to follow AGENTS.md authorisation rules.

```bash
cd /home/hans/repos/fries-machine
source tools/arduino-env.sh
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" lib install hd44780@1.3.2
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile --fqbn arduino:avr:mega:cpu=atmega2560 --warnings all --build-path "$FRIES_PROJECT_ROOT/.build/lcd_text_test" "$FRIES_PROJECT_ROOT/firmware/lcd_text_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" board list
```

Only after a successful build and rechecking the intended Mega's port:

```bash
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload --fqbn arduino:avr:mega:cpu=atmega2560 --port /dev/ttyUSB0 --input-dir "$FRIES_PROJECT_ROOT/.build/lcd_text_test" --verify "$FRIES_PROJECT_ROOT/firmware/lcd_text_test"
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor --port /dev/ttyUSB0 --config baudrate=115200
```

Execution results:

- hd44780 **1.3.2** installed inside the project; no sudo/system package or new driver required.
- Target compilation passed: **10574 bytes program storage / 511 bytes RAM**. Four unused-parameter warnings were in the supplied Arduino core new.cpp; no sketch/library warnings reported.
- Port rechecked as /dev/ttyUSB0, USB1a86:7523, read/write available. Upload with --verify exited0.
- Serial at115200 baud reported **LCD_TEXT_TEST_V1 READY** and 27 consecutive increasing seconds values (1–27), no LCD error line. An initial partial/duplicate boot line preceded READY while opening the monitor; the captured updates after READY did not restart.
- Monitor closed cleanly with Ctrl+C, exit0. The text diagnostic remains running. **Initial visual check showed a blank blue backlight; after contrast adjustment the user confirms success and photo17 shows FRIES MACHINE / Seconds:23. The visual text test now passes.**

Evidence: .build/logs/lcd-text-library-install.log, lcd-text-compile.log, lcd-text-port-before-upload.json, lcd-text-board-list.log, lcd-text-upload.log, lcd-text-serial.log, lcd-text-result.json.

### What success will look like

```text
FRIES MACHINE
Seconds:       0
```

The seconds value advances. Serial reports `LCD_TEXT_TEST_V1 READY` after successful initialisation, followed by increasing seconds. The library may briefly change the backlight during automatic configuration. L will toggle once per second instead of the earlier double flash. This is an elapsed-time display test, not a cooking timer or a claim that oil is ready.

Code handles nonzero initialisation/cursor status, short writes and Wire timeouts by reporting the failure and stopping further LCD writes. It does not retry a failed bus indefinitely or actuate machinery. Hardware text confirmation remains necessary even if library calls return success.

**Observed after upload:** no visible text, backlight on. Use the single contrast check below, then wait for its result. Power off before changing any wiring. Do not infer readable text from address ACK or API return codes.

## Resolved Step9 troubleshooting — contrast adjustment

User reports **nothing is appearing** and provides three photos: LCD backlight blue with no readable characters, Mega signal header, and power-header connections. Originals saved as assets/inventory-2026-10-28/14-lcd-lit-no-text.png through 16-lcd-mega-power-wires.png. Earlier serial READY/seconds remained valid evidence of API results while the initial visual display test was incomplete. It has since passed after contrast adjustment.

**First hypothesis: contrast setting.** Contrast controls how strongly character pixels stand out from the background. The blue square trimmer on the rear HW-61 adapter, identified in photo13, is the first adjustment to check. A lit backlight does not establish readable contrast. Successful software initialisation does not eliminate a contrast problem. This is a hypothesis, not proof of a bad or good display.

### One physical check now

1. If you need to reposition/turn over the module to reach the trimmer, unplug USB first; support the boards on a dry nonconductive surface without straining the four wires. Do not change the connections or remove jumpers.
2. Reconnect USB only so the already uploaded text diagnostic runs. Keep every other supply and device disconnected.
3. With a small suitable screwdriver (preferably an insulated adjustment tool), engage **only the centre slot of the blue rear trimmer**. Keep the tip clear of adjacent pins, solder joints and chip leads. Do not use a large tool that can slip across the board.
4. Turn gently in small increments (about one-eighth turn), watching the front after each movement. Try the other direction if necessary, sweeping gently through the available range. Some adjustments require several small movements; never force a mechanical stop.
5. If characters appear, adjust for clear FRIES MACHINE and an advancing Seconds: line. If only filled character rectangles appear, report that too; it distinguishes a contrast response from no visible change.

**Check before continuing:** report whether readable text, rectangles, or no change appears as the trimmer turns. Stop after this one test and wait for review. No wiring change, extra voltage, resoldering, replacement purchase or new flash is issued. If the proper small tool is unavailable or access is awkward, stop and report that rather than risking a short.

General manufacturer guidance: [Adafruit backpack Arduino I2C use](https://learn.adafruit.com/i2c-spi-lcd-backpack/arduino-i2c-use) recommends contrast-trimmer adjustment when characters are not visible. Its board is a different product; it supports this general check, not specifications for this generic HW-61 assembly. If contrast does not change visibility, later checks can measure actual supply/contrast voltage and use the installed library's I2CexpDiag; those are not yet physical instructions or upload authorisation.

## Resolution evidence

User reports **now working as intended** after the issued contrast check. Photo `assets/inventory-2026-10-28/17-lcd-readable-after-contrast.png` shows `FRIES MACHINE` and `Seconds:23` clearly. No software, wire or replacement part change was reported between blank and readable states. Contrast adjustment resolved the symptom in this build; retain its setting. The single still image does not independently measure time progression, which is supported by user confirmation and earlier serial updates.

No extra voltage measurement or vendor diagnostic upload is needed for this resolved symptom. The next project step is unpowered flavour-button wiring; the currently uploaded LCD-only sketch remains unchanged.

## Sources checked

- [Maintainer's hd44780 repository](https://github.com/duinoWitchery/hd44780), [version metadata](https://raw.githubusercontent.com/duinoWitchery/hd44780/master/library.properties), [official HelloWorld example](https://github.com/duinoWitchery/hd44780/blob/master/examples/ioClass/hd44780_I2Cexp/HelloWorld/HelloWorld.ino) and [I2Cexp implementation](https://github.com/duinoWitchery/hd44780/blob/master/hd44780ioClass/hd44780_I2Cexp.h).
- Arduino's local official `library_index.json` entry for hd44780 1.3.2 (under `.tools/arduino/data/`).
- [Official Mega pinout](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf): SDA20/SCL21 and 5V/GND headers.
