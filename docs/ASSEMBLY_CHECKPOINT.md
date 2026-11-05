# Assembly checkpoint — 6 November 2026

**PHASE 2: PROTOTYPING, Step 37 issued; motor soldering result pending.**

This is the short current-state reference. Earlier entries in build/wiring/testing/progress files retain their dated prompts and intermediate states. Use this checkpoint and the newest dated results to resolve those older pending statements. The original mechanical design remains unchanged; no Phase 3 approval or complete machine prototype.

## Confirmed progress and evidence limits

| Work | Current evidence |
|---|---|
| USB logic restoration | User removed breadboard wiring for another project, then reported LCD/buttons/three indexes reconnected and working. User confirms Mega was not reprogrammed. Original 28 October full simulation checks remain historical passes; not all repeated during restoration. |
| Adapter identification | New photo shows generic MODEL 1250, INPUT AC100–240V50/60Hz, OUTPUT12VDC5A, centre-positive. 60W is calculated from its label. Earlier12V/store check is user-reported; no loaded/current-limit/thermal/certification test supplied. |
| Motor identity | Selected ZENG WHCD JGB37-520 label12V22RPM; two bare rear electrical contacts photographed. No reliable polarity mark, direction, load/current or motor operation confirmed. |
| Fuse | Planned2Astandard ATO/ATC branch fuse; installed-fuse image appears marked2. Actual DC voltage/time curve/interrupting and holder-wire ratings remain unverified. Fuse was removed for wiring and remains out per issued steps. |
| Diode | User confirms SR5100 and reports forward reading redunbanded/blackbanded, no reading reversed. Qualitatively consistent with normal behavior if reverse meansOL/open; no exact displays/manufacturer supplied. Earlier red component is a status LED, not this motor rectifier. |
| DC screw connector | +to barrel centre continuity, −to outer continuity and no+to−short passed by user report. Contact mapping is not a current-capacity or loaded-fit qualification. |
| Power leads | Holder loop cut/prepared and connector+feed/driver+supply secured by user report. Connector−to driverPOWER− return uses18AWG, secured by user report. Photos09–11 show supply leads at outer power terminals and LOAD/control empty. |
| Positive split | User has no3port junction connector and chose a solderedYjunction with existing wire/solder. Two short18AWGpigtails were instructed, labelledDRIVER+/MOTOR+; exact lengths not supplied. User reports soldering/retention complete and electrical tape covering joint, replacing planned heat-shrink. No joint photo supplied. |
| Junction tests and DRIVER+reconnection | User confirmed expected beep/beep/no-beep (two positive paths, isolation from negative, tested before reconnecting module) and secured DRIVER+reconnection. Exact numeric resistance not supplied. |

User-reported tests are distinguished from tool-observed evidence. No new install, flash, serial session or firmware edit occurred during this reconnection/motor-wiring chat.

## Last confirmed assembly

```text
DC connector + -- holder [FUSE REMOVED] -- taped solder junction -- DRIVER+ -- driver POWER+
                                                               └- MOTOR+ -- insulated free end
DC connector − -- existing18AWG black return ------------------------------- driver POWER−

Driver LOAD: empty
Driver control PWM / control GND: empty
Selected motor and SR5100: not yet reported attached
Adapter: disconnected from wall AND DC connector per issued steps
Mega USB: unplugged for handling per issued steps
```

“Disconnected” describes the instructed/latest reported state, not live visual verification. The MOTOR+tail can have black insulation and must remain labelled positive. ControlGND besidePWM is distinct from the POWER− terminal used for motor return; no motor current through breadboard/DuPont wiring.

No second conductor is assumed approved under a module screw: the externalYjunction keeps one conductor at driver+. Electrical tape was accepted conditionally for the dry low-voltage bench joint when fully covering metal and supported against pulling. It does not certify final heat/moisture protection or fix a bad solder joint.

## Immediate physical checkpoint — Step 37, not reported complete

The last hardware guidance asked the user to identify motor terminalA as bench positive (follow actual+mark if available, otherwise label the chosen contact), leavingB as futureLOAD. Attach the labelledMOTOR+wire and the **banded SR5100 cathode** together atA. The unbanded lead andBremain disconnected at this first joint. Support wire/diode, avoid contact with metal motor case and avoid damaging thin contacts/plastic through force or heat. Wait for a cooled-joint photo/retention/band-position report before covering or the second motor joint.

The user then requested saving and pushing; **there is no Step37 completion report or photo**. Resume by establishing whether that joint was actually made. See [build instructions](BUILD_PROTOTYPE.md#current-step37--motor-and-banded-diode-lead-to-motor-terminal-a) and [wiring table](WIRING.md#current-step37--motor-positive-and-flyback-cathode-first-joint).

Later intended connections remain unfinished: motorBto LOAD and unbanded diode anode atB, contact insulation/support, actual module/input topology and electrical matching, controlled safeOFF/reset handling, secured unloaded motor/clear shaft and independently accessible disconnect. Motor direction is unverified. A diode already placed across a motor cannot be assessed as a loose diode by the same directional meter test because the winding is in parallel. No powered motor test or full cooking sequence is authorized by this checkpoint.

## Existing Mega firmware and signal map

Current sketch by user report: [cycle_logic_test](../firmware/cycle_logic_test/cycle_logic_test.ino), unchanged from the approved historical upload. This is **output-free simulation**, not motor-control firmware and not a physical stop function. No motor GPIO is assigned.

| Function | Connection |
|---|---|
| Flavor buttons1/2/3 | D22/D23/D24; other contact shared signalGND |
| Coil indexes1/2/3 | NOtoD26/D28/D30; COMsharedGND; NCunused |
| LCD | GND,5V,SDA20,SCL21; measured address0x27 |

INPUT_PULLUP makes grounded inputs activeLOW. Simulated index deadline15s, warm-up5s, cooking10s; ends SIM TIMERS DONE / Basket: pending. Real proposed300s/600s timers remain separate and unvalidated for actual thermal operation.

Local toolchain from prior approved setup: CLI1.5.1, AVRBoards1.8.8, hd44780BillPerry1.3.2, targetarduino:avr:mega:cpu=atmega2560. Ignored.tools/.build are machine-local caches, not Git deliverables; no automatic reinstall/flash or serial-port reuse. [Setup instructions](ARDUINO_SETUP.md) and [historical logs](evidence/2026-10-28/) retain exact prior commands/results.

## Ownership and scope reminders

- Three flavor motors, MOSFET modules, diodes, fuses/holders and DC connector already received; no automatic duplicate purchases. Actual module count and some delivered ratings remain uncertain.
- 18AWGblack wire,20AWGstranded wire, heat-shrink, electrical tape and soldering gear are reported available.18AWGis actually reported used for negative return.20AWGwas discussed as a conditional short one-motor alternative, not installed in that path or approved for every shared/final cable.
- Only3microswitches owned, all coil indexes;4additional provisional basket switches remain without a receipt report. Basket motor sizing/mechanism/retention/guarding, complete protected fryer/mains/independent stop remain unfinished.
- One red indicatorLED is now photographed; exact dimensions/electrical specs unmeasured. Avoid automatic duplicate redLED purchase if suitable forA10. Other A10 parts remain unconfirmed. [Store list](PHYSICAL_STORE_LIST.md), [inventory](INVENTORY.md) and [remaining audit](REMAINING_PURCHASES.md) retain purchase holds.
- BOM/workbook prices are historical planning figures, not refreshed quotations or actual costs. No budget/table quantities or workbook were repriced in this session.

## Durable references

- [New 6 November handoff](handoffs/2026-11-06-motor-wiring-resume.md): next-chat orientation and save boundary.
- [Progress](../PROGRESS.md): chronological user reports and pending checkpoints; newest entries first.
- [Photo manifest](assets/motor-review-2026-11-05/manifest.json): all11original session photos, observations and SHA256hashes;09motor contacts,10connector,11driver assembly. No solderedY/motor-joint photo yet.
- [Tool guide](TOOLS.md): photographed multifunction stripper, gentle strand gathering and uncertain die compatibility.
- [Project requirements](../PROJECT.md) and [project rules](../AGENTS.md): phase gates, beginner explanations and per-action permissions.
