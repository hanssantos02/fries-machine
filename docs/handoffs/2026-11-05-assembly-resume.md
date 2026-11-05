---
artifact_contract: "ce-handoff/v1"
created_at: "2026-11-05T09:14:42+00:00"
title: "Resume fries-machine assembly after adapter receipt"
summary: "USB logic passed; 12 V adapter received and user-measured; review label and polarity before the first motor channel."
keywords: ["fries-machine", "assembly", "adapter", "phase-2", "handoff"]
cwd: "/home/hans/repos/fries-machine"
resume_focus: "Continue beginner-guided Phase 2 assembly with the received 12 V adapter"
repository: "github.com/hanssantos02/fries-machine"
branch: "main"
---

# Phase 2 assembly handoff — 5 November 2026

## User intent and current boundary

The user explicitly wants to continue assembly **in a new chat**, save all progress, and commit/push this project to **main** at the repository above. The user now owns the 12 V adapter and reports testing that it is **12 V**. No label/photo, current rating, exact voltage trace, probe polarity/placement or measurement load was supplied today. Planned A17 is factory-enclosed regulated12V5A60W; do not assume the acquired adapter meets every planned rating. This handoff does not report motor operation or complete the prototype.

User's project instructions require beginner explanations, phase/step prefix on every reply, one physical checkpoint at a time with their result before proceeding, and permission before installs/flashing/sudo/outside-project writes. Future device actions are not automatically authorized by today's commit/push request. Physical PDF design stays unchanged. Three flavor dispensers, about300g fries and manufactured thermostatic fryer remain intended. No extra automatic temperature probe; thermostat/independent overheat protection remain required. Phase3 has not started.

## Read first — authoritative references

1. `AGENTS.md`: project working rules and physical-result gates; runtime/model identity comes from the active host, not the old model note.
2. `PROJECT.md`: user requirements, unchanged mechanical design, ownership and purchase decisions. `PROGRESS.md`: latest state at top, dated history below.
3. `docs/USB_LOGIC_CHECKPOINT.md`: actual passed USB tests, wiring, known limitations. `docs/evidence/2026-10-28/cycle-logic-result.json`: original source hashes, build/upload results and recorded physical user reports. Logs in that directory are historical and unmodified, including old missing-adapter field.
4. `docs/INVENTORY.md`: receipts and uncertain counts/ratings. `docs/assets/inventory-2026-10-28/manifest.json`: evidence-photo map; photos19/20 show actual module labels, photo21 existing signalGND. Do not infer motor power topology solely from terminal names or colors.
5. `docs/WIRING.md` and `docs/BUILD_PROTOTYPE.md`: small-step build history and pin tables; top November banner supersedes old missing-adapter/pending-test wording. Driver and basket output pins remain unassigned.
6. `docs/REMAINING_PURCHASES.md`, `docs/PHYSICAL_STORE_LIST.md`, `docs/BOM.md`: complete40-row audit, exact A10 store list, STOP choice and purchase holds. Excel and master pricing tables remain historical planning snapshots, not actual remaining-to-pay totals.
7. `docs/POWER_CONTROL_PARTS.md`: STOP candidate reviews and unresolved contactor/control supply scheme. `drawing-fries (1).pdf`: original retained mechanical reference; basket path/torque/load retention unresolved.

## What passed — do not repeat without cause

- Bare Mega/USB diagnostic verified upload, serial heartbeat/ACK and user-observed LED pattern.
- LCD1602/HW-61 backpack measured at0x27; readable after contrast adjustment. Blank-screen contrast issue is solved.
- Three flavor buttons and three microswitches pass contact/mapping tests. User fixed earlier header placement; don't re-diagnose that old photo.
- Output-free cycle simulation passed all planned manual checks by user: selected index, busy lockout/no queue, wrong-index rejection, missing-index timeout and latched fault/reset, initially-held index release/re-actuation, and startup-held flavor suppression.
- Host tests cover controller/debounce, timing boundaries and rollover. Exact earlier tool results are in evidence. Manual events/timing were not independently captured/calibrated.
- User says all soldered MOSFET modules already checked/working; method/count not supplied. This does not prove loaded current/thermal/stop suitability. Don't repeat the superseded loose-module resistance request solely because it appears earlier in the build guide.

## Firmware and exact working signal wiring

Current uploaded source: `firmware/cycle_logic_test/cycle_logic_test.ino`, `CycleLogic.h`, `ButtonInput.h`. Source unchanged since approved upload. No motor/relay/heater output commands, no basket motion or physical emergency-stop function. Last observed board firmware is this simulation, not a full machine controller.

| Function | Mega connection |
|---|---|
| Flavor buttons1/2/3 | D22/D23/D24, other side to existing signalGND |
| Index switches1/2/3 | NO toD26/D28/D30; COM to existing signalGND; NC unused |
| LCD | GND,5V,SDA20,SCL21; address0x27 |

Inputs use INPUT_PULLUP (closed toGND meansLOW). Existing common breadboard ground works for signals. **Motor power and return current do not belong on breadboard/DuPont wiring.** No new motor GPIO assignment exists. USB remains logic power; no12V on Mega5V or LCD rails. Simulation:15s index deadline,5s warm-up,10s cook, terminal `SIM TIMERS DONE / Basket: pending`. Real proposed300s/600s settings are separate and thermally unvalidated.

Machine-local tooling at capture: `.tools/arduino/`, ArduinoCLI1.5.1, AVRBoards1.8.8, hd44780byBillPerry1.3.2. Target`arduino:avr:mega:cpu=atmega2560`; historical build13360flash/797RAM. Last port`/dev/ttyUSB0`, USB1a86:7523/ch341; re-enumerate only when a future authorized device action needs it. Tool downloads/build artifacts are ignored, not published. `docs/ARDUINO_SETUP.md` and `tools/` preserve setup commands; a fresh clone needs authorized setup, not copied binaries. Do not rerun setup on the existing machine automatically.

## Ownership and procurement

- Owned: Mega/cable, LCD/backpack,3flavor buttons, **exactly3microswitches** (all used for coil indexes),3JGB37-520motors with readable12V/22RPM labels, soldered MOSFET modules, diode/fuse-holder/fuse bags, capacitor bags1000uF25V/470uF16V, ceramics,18AWGblackwire, oneDCbarrel/screw adapter, breadboard/jumpers, multimeter/computer/soldering gear.
- **New:** one12Vadapter, voltage user-tested; other actual ratings/plug details pending.
- Four additional provisional basket microswitches still needed unless user reports later receipt; don't buy7more.
- Ceramic value/voltage/count and black18AWG length unknown. Redwire,LM2596 and A10 components not reported received. Do not automatically rebuy bags/blackwire/connector; inspect only relevant shortfalls.
- User selected **one HSK LA38 Emergency Stop** (22mm, non-illuminated, push-lock/turn-release,1NO+1NC), screenshotPHP98; chose to buy it despite absent positive-opening/contact-duty evidence. **Not yet reported received or safety-qualified.** 2NC was a preference, not a universal mandatory count. Do not force another identical supplier-search loop or falsely accept safety function. Final hardwired stop circuit/contact needs remain unresolved.
- A10 store list: one5Vactive/self-oscillating2pinbuzzer<=30mA; one eachred/green5mmLED; two330ohm1/4W; oneBC337; one1kohm1/4W; one10kohm1/4W. Suitable spareSR5100 may cover magnetic-buzzer protection; otherwise one1N4007, no extra whole pack. Pins/firmware for these not yet assigned.
- Basket actuators/drivers/supply, power-off retention and mechanical transfer path remain on hold. Contactors/relay duty/suppression/control voltages unresolved. Legacy24Vcontrol supply is conditional, not automatic with220VACcoil. Fryer model/nameplate/independent cutoff/earth/fit and qualified mains review remain required. Full BOM coverage in linked audit.

## Next assembly checkpoint — Step26 pending

A reasonable next step, subject to the new chat's current user instruction, is **adapter qualification before any motor connection**: request a clear label and connector photo, establish printed continuous current rating and connector polarity from markings/probe placement, and ask whether the reported12V was measured unloaded. Credit the voltage result already supplied; repeat only if polarity/conditions or a changed connection needs checking.

Then review one actual driver channel's terminal topology, suitable power wiring/DCconnector ratings, branch fuse/holder and flyback diode identity/orientation, secure unloaded motor mount and independent accessible disconnect. A future safe-OFF/reset/power sequencing test requires an explicitly prepared matching sketch/wiring and appropriate upload permission. Only after that progression is a protected single-channel motor test plausible. Do not jump straight from voltage report to connecting all motors or a cooking cycle. No hardware step was issued/performed in today's save turn.

## Repository continuity and verification limits

This directory initially had no.git. User supplied the remote; it has an original README commit`2e5c478`. Localmain was based on that commit; history is retained, no force push intended. The handoff exists before the save commit, so its final commit hash is deliberately not embedded. `PROGRESS.md` and final response report publication outcome; verify `git log/status` and remote when resuming if needed. Git remote itself is local metadata; a new clone uses the repository URL above.

Published source/docs/PDF/workbook/photo evidence and small logs are intended to persist in Git. Ignored machine-local `.tools`, `.build` and generated scratch renders are not prerequisites for understanding the build. Historical BOM generation source under`tmp/bom` is retained where relevant; it is archival, with original path assumptions, not an instruction to regenerate prices. No credentials or tool download caches belong in the commit.
