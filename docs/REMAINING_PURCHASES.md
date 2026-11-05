# Remaining purchases — inventory audit

Updated: **5 November 2026, Phase 2, Step 26 pending**. Compared every current row of `BOM.md` against confirmed receipts and user reports in `INVENTORY.md`. “Not reported owned” means check before ordering; it is not proof of absence. Received parts still require their applicable electrical/mechanical checks.

**Latest ownership correction:** ceramic capacitors and 18 AWG black wire are in hand. Their values/count and available wire length are unknown. Do not order replacement packs or another automatic 3 metres of black wire.

## Latest purchasing decision

User selects HSK LA38 Emergency Stop, 1NO+1NC, screenshotPHP98, one unit. Not yet received; final positive-opening/contact-duty acceptance still pending. Replaces old STOP supplier for procurement, not an extra STOP purchase. A10 physical-store parts are now itemized in [PHYSICAL_STORE_LIST.md](PHYSICAL_STORE_LIST.md); quantities specify one working set and no automatic duplicate diode pack. Historical master cost table/Excel snapshot remain unrepriced.

## Adapter receipt supersedes the earlier purchase priority

**5 November 2026 update:** user now owns one 12 V adapter and reports measuring **12 V DC**. Exact model, label current/power rating, enclosure type, connector size/polarity, load during measurement and loaded regulation/protection are not supplied. Planned A17 is enclosed regulated 12 V / 5 A / 60 W, but those ratings are not established by the voltage reading. Do not rebuy it automatically. No motor connection/test is reported.

## Purchase priority

1. **A17 adapter now received; no additional adapter purchase planned.** User reports 12 V measured. Next task is actual label/plug/current rating and polarity review, not reordering or assuming 5 A capability.
2. **Red 18 AWG stranded copper wire, initial allowance 3 m (part of B04): not reported owned.** Black wire is already owned; only top up any measured shortfall against the initial 3 m black allowance. These are short fixed DC motor-power wires, not mains or repeatedly flexing basket leads.
3. **Four additional roller microswitches (A07): explicitly missing.** Three of seven planned switches are already connected and tested. The four are for provisional basket endpoints; confirm mounting/travel before ordering. They do not block the next single flavor-channel bench test.
4. **LM2596 buck converter, one (A13), and suitable STOP actuator, one (A09): not reported owned.** The converter later supplies standalone 5 V logic; USB already powers current logic tests. STOP selection requires the documented contacts and final hardwired circuit described below. An independent motor-power disconnect and secured mounting must be defined before motor operation.
5. **Buzzer/LED set (A10): not reported owned; may defer for the current LCD-based bench tests.** Buy only the missing signal parts once the circuit is settled.

This is a purchase audit, not authorization to energize motors or mains. Motor current must not run through the breadboard or DuPont jumper leads. Existing signal ground is retained; motor return wiring needs its own suitable power path.

## Table A — every prototype/reusable BOM row

| BOM | Planned quantity / item | Receipt status | Remaining purchase or decision |
|---|---|---|---|
| A01 | 1 Mega 2560 + data cable | Owned; USB diagnostic passed | None. Reuse controller and working cable. |
| A04 | 2 BTS7960/IBT-2 basket drivers | Not reported owned | **Hold.** Match to selected basket motor voltage/current first. If steppers are selected, replace these with matching stepper drivers; do not buy both types. |
| A05 | 3 JGB37-520 12 V / 22 RPM flavor motors | 3 received | None to buy. Loaded fit/current/torque testing remains. |
| A06 | 3 LR7843 MOSFET modules | Received, soldered and reported working; total not explicitly counted | Do not reorder a set. Count available channels before any top-up; loaded qualification remains separate. |
| A06.1 | 1 ten-piece SR5100 diode pack | Strip/bag received; count/identity to check | No automatic replacement pack or duplicate SB560. Confirm at least 3 suitable flyback diodes if required by actual module circuit. |
| A07 | 7 roller microswitches | Exactly 3 owned, connected and tested | **4 remaining**, for provisional basket endpoints. Check physical fit. |
| A08 | 3 momentary flavor buttons | Owned and tested | None. These are signal controls, not emergency stops. |
| A09 | 1 LA38 STOP mushroom actuator | Not reported owned | Remaining if absent, but provisional candidate is not yet qualified. Require latching action and documented positive-opening normally-closed contacts, preferably 2 NC, matched to the independent stop circuit. Do not buy a generic button solely by appearance. |
| A10 | 1 active-buzzer/red-green LED set | Not reported owned | Remaining if absent; can defer. Include appropriate buzzer transistor/base resistor and individual LED resistors only as needed; avoid duplicating A15 parts. |
| A11 | 1 breadboard | Owned and used | None. Keep motor current off it. |
| A12 | 3 planned jumper bundles | Jumpers owned; quantities/types not counted | No automatic three-bundle order. Top up only an actual connector/length shortage. |
| A13 | 1 LM2596 adjustable buck converter | Not reported owned | Remaining if absent, for standalone logic power. Set and measure 5 V before connecting logic. Not required for present USB-only operation. |
| A14 | 3 inline holders + 1 ten-piece 2 A fuse pack | Holders and fuse bag received | Do not rebuy the set. Check actual holder count, lead gauge, DC ratings, fuse size/current markings and suitability. A received fuse is not automatically accepted protection. |
| A14.1 | 1 additional DC protection/distribution set | Not reported owned; exact pieces unresolved | Select/itemize main, logic and basket protection, distribution and polarity protection after current/supply/wire/stop review. Buy only additions to A14/B04. |
| A15 | 1 passive/filtering kit | Ceramic capacitors now confirmed; 1000 µF / 25 V and 470 µF / 16 V bags already received | Check ceramics against planned 100 nF (0.1 µF, often marked 104), 50 V, quantity 10. Existing electrolytic counts unknown. Do not reorder whole bags; only actual shortfalls or circuit-specific missing passives. The old miscellaneous allowance is not a separate shopping item. |
| A16 | 2 provisional basket actuators | Not reported owned | **Hold.** Resolve mechanism, torque, speed, travel and power-off load retention before choosing motors. |
| A17 | 1 planned enclosed regulated 12 V / 5 A / 60 W adapter | **One adapter owned**, user reports measured 12 V on 5 November | No automatic repeat purchase. Exact label/current rating, enclosure, connector/polarity and load-test conditions remain unverified; planned 5 A / 60 W is not established. |
| A17.1 | 1 basket motor supply | Not reported owned | **Hold** until A16 and stop/current requirements are known. Not a second automatic flavor adapter. |
| A18 | 1 LCD1602 with I2C backpack | Owned; readable and tested | None. Backpack already attached; no second backpack. |

## Table B — every additional/permanent-material BOM row

These are outstanding integration/permanent-build entries, not an instruction to start Phase 3. Some protection/fryer items will also be required before completing powered/hot Phase 2 integration. They are not all needed for the next cold single flavor-channel bench test.

| BOM | Planned quantity / item | Receipt status | Remaining purchase or decision |
|---|---|---|---|
| B01 | 1 complete Single-6L fryer with basket | Candidate selected; receipt not reported | Check purchasing ownership with mechanical team. Verify actual nameplate, independent overheat cutoff, earth connection and fit before acceptance; no duplicate fryer order. |
| B02 | 1 assembled Mega screw-terminal shield | Not reported owned | Later permanent signal connections; not needed for current breadboard work. |
| B03 | 1 low-voltage enclosure set | Not reported owned | Later; confirm layout, standoffs, cable entries and cooling before exact size/order. |
| B04 | 1 permanent DC/moving harness set | **18 AWG black wire and 1 DC connector owned**, lengths/connector rating unknown | Red 18 AWG initial allowance 3 m if absent; black top-up only against 3 m allowance. Existing DC connector: verify plug fit/polarity and documented 5 A suitability; replace only if unsuitable. Later 22 AWG fixed signal wire: 2 m each red/black/blue/yellow/white, 10 m total. Basket/flex leads require final takeoff. Do not add the whole kit allowance again on top of its individual wires. |
| B05 | 1 labels/mounting hardware set | Not reported owned | Later, actual missing fasteners/sensor mounts and labels. Existing selected label pack does not imply a label-printer purchase. Avoid hardware already supplied with mounts/enclosures. |
| B06 | 1 K1 fryer run contactor | Not reported owned | **Hold.** Candidate CJX2-1810 18 A / 220 V AC coil must match actual heater and complete coil/interface/stop design. |
| B07 | 1 K0 independent power-stop contactor | Not reported owned | **Hold.** Final contacts, coil voltage, combined load/inrush and manual-restart circuit unresolved. |
| B08.1 | 1 Arduino-to-contactor relay interface | Not reported owned | **Hold acceptance/order with coil scheme.** Generic 5 V/10 A relay advertising does not establish suitability for the final mains coil circuit. |
| B08.2 | 1 conditional HDR-15-24 control supply | Not reported owned | **Hold; may be removed.** Legacy 24 V DC-coil allowance is not automatically needed by the B06 220 V AC coil. Buy only if the finalized whole control scheme requires it; do not buy incompatible alternative schemes. |
| B08.3 | 1 spring-return panel RESET button | Not reported owned | Later hardwired reset control; verify contact block/duty. Mega onboard RESET is not its permanent substitute. |
| B08.4 | 1 coil-suppression allowance/set | Exact parts/count unresolved | **Hold.** Match to actual AC/DC coils and release requirements; check built-in suppression first. A plain DC flyback diode is not an AC-coil suppression choice. |
| B08.5 | 1 additional control-wire/fuse set | Exact voltages/lengths unresolved | **Hold.** Additional pieces only, not duplicates of A14/B04. |
| B09.1 | 1 conditional RCBO | Existing site protection not assessed | Buy only if qualified assessment finds existing protection inadequate. Candidate ratings must match actual circuit. An RCBO combines overcurrent and earth-leakage protection. |
| B09.2 | 1 covered mains enclosure + mounting plate | Not reported owned | Later; confirm actual component layout, clearances and metal bonding. Separate from B03 low-voltage box. |
| B09.3 | 1 DIN rail/end-stop mounting set | Not reported owned | Later; omit rail/mounting parts already included with enclosure. |
| B09.4 | 2 covered TB-2503 strips + 1 six-way earth bar | Listings selected; receipt not reported | Later, if absent. Verify terminal conductor/current ratings and protective-earth suitability; do not infer ownership from product screenshots. |
| B09.5 | 1 mains cord/grounded plug/controlled outlet set | Not reported owned | Later; finalize cable type/length and load/protection match. Retain factory fryer cord. Qualified mains review before energizing. |
| B09.6 | 1 mains glands/ferrules/identification set | Not reported owned | Later; only additional sizes/pieces not supplied with other kits. |

## Table C — fees, not parts to buy

| BOM | Entry | Remaining action |
|---|---|---|
| C01 | Qualified electrical review/inspection | Arrange before mains energizing. Pay only if actually hired; school support availability/cost not confirmed. |
| C02 | Shipping/delivery | Record actual charges after orders are grouped. |
| C03 | User assembly labor | PHP 0 outside assembly fee in the existing DIY plan. Do not add an automatic panel-building charge. |

## Mechanical-team and small-consumable coordination

Before powered flavor tests, confirm provision of **3 secure 37 mm-class motor brackets/fixtures with matching screws, 3 shaft couplings/hubs, and 3 index cams/tabs with switch mounts**, plus suitable guarding. Motor-only purchases do not establish these are included. Measure both shaft ends before choosing couplings; advertised 6 mm D-shaft does not establish a 6-to-6 mm coupling fits the coil.

Confirm suitable motor-lead terminations, insulation/heat-shrink and strain relief as needed, and an accessible independent power disconnect. These are mechanical-team scope or existing B04/B05 provisions unless an actual additional purchase is identified; no new duplicate budget lines are charged. Computer, multimeter and soldering equipment are already available. Borrow any additional crimp/strip tools actually needed instead of automatically buying a whole toolkit.

## Cost and scope of this audit

All **37 material rows and 3 fee rows** are covered once above. No current market-price research was requested/performed, and actual receipt costs were not supplied. Existing BOM prices are historical observations/estimates, not a remaining-to-pay total. Unconfirmed ownership, conditional items and unquoted items prevent an accurate remaining total. Master quantities/prices and the Excel workbook are unchanged; this audit and inventory records provide the current procurement status.

USB logic checks remain passed. This review does not complete the full prototype or start Phase 3.
