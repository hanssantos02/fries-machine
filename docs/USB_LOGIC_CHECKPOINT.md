# USB-only control-logic checkpoint

**28 October 2026, Asia/Manila — PHASE 2, Step24 complete.**

The planned USB-only input/display/software checks passed. **The full working machine prototype is not complete, and Phase3 has not started.** Do not repeat these checks unless a change, failure or unresolved concern justifies it.

## Confirmed results

| Check | Evidence/result |
|---|---|
| Mega/USB | Verified diagnostic upload, serial heartbeat/ACK and user-observed LED pattern passed |
| I2C LCD | Address0x27 measured; readable text passed after contrast adjustment |
| Three buttons | Individual mappings22/23/24 and normal selections passed by user |
| Three coil-index inputs | Individual mappings26/28/30, ACTIVE/READY, held/no-repeat and release/repress passed by user |
| Simulation sequence | Selected manual index advances to SIM warm-up5s, SIM cooking10s, then Basket:pending; flavors1–3 exercised across tests |
| Busy lockout | Other buttons do not change selection/restart timers/queue a new cycle; completion remains latched |
| Wrong-index rejection | Flavor3 ignores indexes1/2 and accepts index3 only |
| Missing-index timeout | Missing response produces INDEX TIMEOUT; late index/new button cannot resume; explicit RESET returns idle |
| Already-held selected index | Requires release and fresh actuation after selection |
| Startup-held flavor button | Remains idle while held and upon release; fresh press required |

Physical test results are user reports; no stopwatch calibration, loaded motor measurement or manual-event serial trace was supplied. Host tests cover the same controller/contact helpers, including timer rollover, timing boundaries, invalid timings and debounce/controller integration.

## Current uploaded firmware and wiring

`firmware/cycle_logic_test/cycle_logic_test.ino`, `CycleLogic.h`, `ButtonInput.h`. Mega target `arduino:avr:mega:cpu=atmega2560`; CLI1.5.1/AVR1.8.8/hd44780 BillPerry1.3.2. Build13360flash/797RAM bytes; four supplied-core warnings only. Verified upload passed; captured17 idleIDLE/flavor0/raw111111/lcdOK samples. Later manual checks above passed by user. No firmware change after upload.

- Buttons1/2/3: D22/D23/D24 to signalGND.
- Index1/2/3: NO to D26/D28/D30; COM to existing connected signalGND; NC unused.
- LCD: GND/5V/SDA20/SCL21, address0x27.
- Existing breadboard commonGND retained. Wire colours alone do not identify signals or guarantee split-rail continuity.

**SIMULATION ONLY:** no motor/relay/heater GPIO outputs or physical-stop function. USB logic power only; drivers, motors, external supplies and fryer circuitry disconnected.15s response window,5s/10s simulation durations do not replace or validate the project's real300s/600s proposal. Basket stage stops explicitly as pending. No independent thermal, mains, mechanical or emergency-stop validation has occurred.

## Ownership and purchase priorities

**5 November 2026 update:** user now owns one 12 V adapter and reports measuring **12 V DC**. Exact model, label current/power rating, enclosure type, connector size/polarity, load during measurement and loaded regulation/protection are not supplied. Planned A17 is enclosed regulated 12 V / 5 A / 60 W, but those ratings are not established by the voltage reading. Do not rebuy it automatically. No motor connection/test is reported.

- **3 microswitches owned**, already used as coil-index inputs; **4 additional switches** remain of provisional7total for basket inputs. Do not buy7more or duplicate the3owned. Final basket fit/function remains conditional on the retained PDF mechanism.
- **Adapter now owned**, user reports measured12V on5November. Actual label/current rating, connector/polarity and measurement conditions still need review; planned5A60W is not established by the voltage reading.
- DC connector, fuse holders/fuses, diodes, motors and MOSFET modules are received/reported; do not automatically rebuy them. Existing connector rating, delivered fuse markings, diode identity/orientation, power-wire ownership/gauge and motor mounting/disconnect still require review. See INVENTORY.md and PHYSICAL_STORE_LIST.md. Prices have not been refreshed or quoted.

## Next checkpoint — Step26 adapter review, part now available

Keep successful signal wiring intact. Adapter is in hand and the user already reports12V measured. Obtain a clear label/plug photograph and ask how probes were placed to establish polarity and conditions; avoid repeating an identical voltage check without a reason. Do not energise a raw open mains supply or connect12V to the breadboard/Mega5V rail. The selected supply is a factory-enclosed adapter; no mains opening/wiring step is issued.

Before motor-power wiring: review actual driver terminals (photo19/20), rated power wiring/connectors, branch protection/flyback diode, safe OFF/reset behavior, secured unloaded motor and accessible independent disconnect. These checks are not already passed by MOSFET ownership or the software simulation. Only then issue the first protected single-channel motor test. Four basket switches, basket motor/driver sizing, mechanical path/retention/guards and protected fryer/mains installation remain later Phase2 work.

No new upload, purchase/order, wiring or motor operation is authorised by this checkpoint document. Existing per-action permissions and step-by-step physical-result gates remain in force.


Full handoff for the new chat: [5 November assembly resume](handoffs/2026-11-05-assembly-resume.md). Original tool records are preserved under `docs/evidence/2026-10-28/`; their old inventory fields are historical.
