# Mega diagnostic setup and first upload

28 October 2026, Asia/Manila. **Phase 2, Step 4. User approved execution; setup, compile, upload and serial checks passed. User confirms the expected LED pattern; this diagnostic checkpoint is complete.**

## Confirmed so far

- User: bare board ON LED lights and L LED blinks with USB power.
- Read-only host inspection: a new `/dev/ttyUSB0`, USB VID:PID `1a86:7523`, product `USB Serial`, kernel driver `ch341-uart`. Port is readable and writable by the current process. Initial enumeration was followed by a successful approved diagnostic upload and serial heartbeat/ACK check.
- User `hans` already has `dialout` in the current process's groups. No group change or extra USB driver is indicated. Initially no Arduino CLI, `pio` or `platformio` executable was found on PATH. Project-local CLI 1.5.1 and AVR Boards 1.8.8 are now installed using the approved scripts; an IDE elsewhere has not been inventoried.

Keep the board bare, USB only. Do not attach drivers, motors, LCD, switches, header wires or another supply during this diagnostic. Confirm the port still belongs to the Mega before upload; device numbers can change. A device label from a clone USB interface may be generic, so select the photographed full-size Mega 2560 target explicitly.

## Tool versions and locations

- Arduino CLI **1.5.1**, Linux x86_64 archive.
- Arduino AVR Boards **1.8.8** (`arduino:avr@1.8.8`), from Arduino's official package index. Its dependent compiler/uploader/discovery tools are installed by the core/CLI, not invented manual driver packages.
- Target/FQBN: **`arduino:avr:mega:cpu=atmega2560`**. FQBN is the CLI's exact board identifier.
- Sketch: `firmware/mega_diagnostic/mega_diagnostic.ino`. No third-party libraries.
- Serial speed: **115200 baud**, the number of serial signalling symbols per second for this link.
- CLI archive SHA-256: `28a8e119c498a25607821c36cb2dc49e8463941b261a0d99091baa7bc692dd2b`, checked against the official release checksum list before extracting. A checksum detects a mismatched download.

The scripts keep tools, downloaded packages, temporary files and compilation cache under `.tools/arduino/` inside this project; compiled outputs go under `.build/mega_diagnostic/`. They do not use sudo, change groups, edit shell startup files or install system packages. Directory environment variables override default Arduino locations; `TMPDIR` is a project-local temporary directory. No HOME variable is changed.

## Exact commands — approved and executed for this diagnostic

The scripts are plain text and can be reviewed in `tools/`. Their full installation/download/build/upload commands are saved there. The user approved the installation, compilation, diagnostic upload and serial check with “proceed.” AGENTS.md still requires permission for any future installation/flash action that is not covered by existing authorisation.

```bash
cd /home/hans/repos/fries-machine
bash /home/hans/repos/fries-machine/tools/setup-arduino.sh
bash /home/hans/repos/fries-machine/tools/mega-diagnostic.sh compile
bash /home/hans/repos/fries-machine/tools/mega-diagnostic.sh list
```

Continue only if setup and compilation succeed and the listed port is still the intended Mega. The following upload replaces the existing application that currently blinks L; it does not intentionally burn a bootloader or change fuses. It uses the standard core uploader and verifies the application write.

```bash
bash /home/hans/repos/fries-machine/tools/mega-diagnostic.sh upload /dev/ttyUSB0
bash /home/hans/repos/fries-machine/tools/mega-diagnostic.sh monitor /dev/ttyUSB0
```

Opening the monitor can reset the Mega. Close other IDE serial monitors first to avoid competing for the port. Stop this monitor with Ctrl+C. Do not continue to external wiring until the observed diagnostic result is recorded.

### Serial permissions

Read-only check already performed: `id -nG`, with `dialout` present, and direct port read/write access confirmed. **No permission-changing command is needed now.** If a later actual error establishes missing membership, the command for this user would be `sudo usermod -a -G dialout hans`, followed by a new login/restart. This is a conditional explanation, **not** a current instruction or permission to run sudo. Check the actual port's group first; never use a blanket world-writable port workaround.

## Expected diagnostic result

1. Compile succeeds for Mega 2560; memory usage is reported. Exact sizes are not claimed before compilation.
2. Upload/verification succeeds. A successful USB power check alone does not establish this.
3. L changes to **two short flashes, a pause, repeating every two seconds**.
4. At 115200 baud, the monitor shows startup lines when caught and repeated lines resembling:

```text
FRIES_MEGA_DIAGNOSTIC_V1 heartbeat=1 uptime_ms=1000
FRIES_MEGA_DIAGNOSTIC_V1 heartbeat=2 uptime_ms=2000
```

Actual uptime can vary slightly. Missing a startup line is acceptable if the repeated diagnostic heartbeat is present. Sending `?` should produce:

```text
FRIES_MEGA_DIAGNOSTIC_V1 ACK: USB serial receive OK
```

The code uses `millis()` (elapsed milliseconds) instead of a long blocking delay, so serial input is handled between LED updates. It controls only the onboard LED (digital pin 13) and serial interface; it contains no machine actuation logic.

**Result:** serial heartbeat/ACK captured successfully, and the user confirms the two-flash pattern. Diagnostic checkpoint passed. Record compilation/upload evidence separately from user-observed LED behaviour.

## If something fails

- Download/checksum/core install failure: stop, retain the actual error, and check source/network or dependency issue. Do not bypass checksum verification.
- Compile failure: stop before upload; review the exact first compiler error and board/core versions.
- Port absent/busy/denied: recheck enumeration, cable, ownership and another open monitor. Do not kill processes or change permissions blindly.
- Upload signature/synchronisation failure: check target, port and reset/cable before concluding the bootloader is broken. Never force an AVR signature or burn the bootloader as an automatic fallback.
- Readable serial missing/garbled: check 115200 baud, correct port and known diagnostic tag; existing factory blinking is not a substitute for this result.

## Sources checked for the prepared commands

- [Arduino CLI 1.5.1 release](https://github.com/arduino/arduino-cli/releases/tag/v1.5.1) and [published checksums](https://github.com/arduino/arduino-cli/releases/download/v1.5.1/1.5.1-checksums.txt).
- [Official package index](https://downloads.arduino.cc/packages/package_index.json), [AVR 1.8.8 board definitions](https://github.com/arduino/ArduinoCore-avr/blob/1.8.8/boards.txt) and [Mega pin definitions](https://github.com/arduino/ArduinoCore-avr/blob/1.8.8/variants/mega/pins_arduino.h).
- [CLI installation](https://arduino.github.io/arduino-cli/1.5/installation/), [configuration](https://arduino.github.io/arduino-cli/1.5/configuration/), [compile](https://arduino.github.io/arduino-cli/1.5/commands/arduino-cli_compile/) and [upload](https://arduino.github.io/arduino-cli/1.5/commands/arduino-cli_upload/).
- [Arduino Linux port access guidance](https://support.arduino.cc/hc/en-us/articles/360016495679-Fix-port-access-on-Linux).

## Current validation limits

Approved execution completed successfully:

- CLI archive checksum passed; CLI 1.5.1 and AVR Boards 1.8.8 installed in the project.
- Target compilation passed: 3334 bytes program storage, 196 bytes RAM. Four unused-parameter warnings come from the supplied core new.cpp; no diagnostic-source warnings were reported.
- Board list showed /dev/ttyUSB0 as a generic Unknown USB serial board, consistent with a clone interface; the explicitly selected Mega target compiled/uploaded successfully. Upload used --verify and exited 0.
- At 115200 baud captured the diagnostic boot tag, 27 consecutive heartbeat lines (uptime 1000 through 27000 ms) and the expected ?/ACK response. A few unreadable bytes appeared before the clean boot tag; subsequent diagnostic lines were readable.
- Monitor closed cleanly with Ctrl+C. No external wiring or motor/fryer operation was performed.
- The user confirms the expected two-flash L LED pattern (28 October 2026). T04 passed. This does not qualify every GPIO or connected machinery.

Logs and machine-readable results: `.build/logs/mega-setup.log`, `mega-compile.log`, `mega-board-list.log`, `mega-upload.log`, `mega-serial.log`, `mega-diagnostic-result.json` (all in the same log directory).
