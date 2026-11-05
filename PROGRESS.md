# Project Progress

Updated: 5 November 2026 (Asia/Manila).

## Current phase and step

**PHASE 2: PROTOTYPING, Step26 pending — adapter received with user-reported12V; label/polarity review before motor wiring. Step25 procurement and Step24 USB logic milestone complete; powered motor/basket/fryer work remains.** Current uploaded firmware is cycle_logic_test: output-free simulation on buttons22/23/24, index26/28/30, LCD0x27/SDA20/SCL21 and existing signalGND. Planned input/display/selection/countdown/lockout/fault/reset/held-input checks passed; tool evidence and user reports are recorded separately. Three microswitches owned; four additional basket switches remain without a later receipt report. Adapter now owned; user reports measured12V on5November, other ratings/polarity/load conditions unknown. No powered actuator test, full prototype completion or Phase3 approval. See docs/USB_LOGIC_CHECKPOINT.md for the concise handoff.

## Step 25 — remaining purchases audited

User confirms ceramic capacitors and 18 AWG black wire are owned. Values/voltage/count and wire length remain unknown; no automatic replacement pack or 3 m black-wire order. Red wire, LM2596, STOP and buzzer/LED set were not reported owned. Full audit saved in `docs/REMAINING_PURCHASES.md`: all 37 materials and 3 fees covered; adapter and four additional switches explicitly missing, partial receipts/top-ups separated from unconfirmed ownership and purchase holds. Updated BOM inventory note, inventory and physical-store list. No repricing, remaining-total claim, Excel edit, firmware change, flash or physical test. Phase 2 remains incomplete.

## Step 25 follow-up — STOP candidate review

Reviewed user Lead-HG XB2-ES542 screenshots: PHP81, 22mm, red40mm head, push-lock/twist-release, explicitly1NC/two terminals. Basic form matches; preferred2NC and documented positive opening/control duty not established. Candidate only, not final safety acceptance or replacement selection. A singleNC is not inherently invalid for every design; final stop contact arrangement remains unresolved. Shopee direct access failed; screenshot evidence used. Saved detail in POWER_CONTROL_PARTS and BOM note; no new purchase, table-price/workbook/wiring/firmware change.

## Step 25 follow-up — Jayson LA38 red STOP

Reviewed selected red STOP screenshot PHP116: advertised22mm press-to-disconnect/rotate-to-reset; mixed self-reset title does not identify this variant. Contact count, documented positive opening and voltage/inductive duty absent. Generic10A/CCC claims do not resolve those gaps. Direct page inaccessible; screenshot evidence used. Candidate only; seller datasheet/contact-block details needed before acceptance. Saved BOM note and POWER_CONTROL_PARTS review; no purchase, price/workbook/wiring/firmware change.

## Step 25 follow-up — HSK LA38 STOP

User screenshot HSK Emergency Stop selected PHP98:22mm, non-illuminated,1NO+1NC, pushdownlock/turnrelease. More explicit contact/action evidence; exact manufacturer, positive opening and applicable contact duty still absent. Clarify2NC preferred rather than mandatory for all designs; singleNC can serve a suitable single-loop design subject to final safety review. Candidate only; BOM review note and detailed POWER_CONTROL_PARTS record added, no selection/price/workbook/wiring/firmware change.

## Step 25 follow-up — STOP choice and A10 physical-store order

User chooses HSK LA38 Emergency Stop1NO+1NC, screenshotPHP98, one unit; purchasing choice recorded, not receipt or final safety acceptance. Do not rebuy old A09 alternative. Positive-opening/control-duty evidence still unresolved. Itemized A10 physical-store kit:5Vactivebuzzer<=30mA, red/green5mmLEDoneeach,330ohm1/4Wtwo,BC337one,1kohm1/4Wone,10kohm1/4Wone;1N4007onlyif needed/no suitable owned diode spare. Own breadboard/jumpers/soldergear reused. No new price estimates beyond existing historical kit allowance, no workbook repricing, pin/wiring/firmware/device change. Full list in PHYSICAL_STORE_LIST; BOM/audit/control notes updated.

## Completed context review

- Read the complete `AGENTS.md`, the original blank `PROJECT.md`, all populated cells/formulas in `BOM_Automatic_Fries_Machine.xlsx`, and all ten pages of `drawing-fries (1).pdf` (text and rendered images).
- There was no previous `PROGRESS.md`, firmware, software or other project document in the folder.
- Obtained five clarifications: electronics-only team assignment; approx. 300 g fries per batch; electrical buttons turn the three coils; no fixed budget but economical working choices; no electronics owned, multimeters/testing tools available; include a complete protected fryer allowance.
- Populated `PROJECT.md` with confirmed requirements, qualified assumptions and missing mechanical/electrical inputs.

## Decisions and corrected assumptions

- Proposed full-size Mega 2560 R3 compatible controller, 5 V logic, in place of the earlier ESP32. No Wi-Fi requirement. This is a recommendation awaiting BOM approval, not a user-mandated controller.
- Maintain temperature regulation using the manufactured fryer thermostat. Current cycle start is a flavor-button press, replacing potato-drop start; timed warm-up followed by timed cooking is selected, with actual durations pending validation.
- A flavor-button press requests one packet and one cooking cycle. Proposed busy lockout prevents repeated selections from restarting it. Ten minutes is requested, not a universal cooking standard.
- Provisionally budget two geared DC basket axes and reusable drivers; select actual motors for cold tests/final reuse. Separate bench-only simulators are removed. Final sizing and the existing trajectory remain unresolved.
- Three flavor coils need geared motors, drivers and index switches. Optional packet-delivery detector is removed; operator observes delivery. Ordinary positional servos are not selected as direct full-turn coil drives.
- Potato/packet/bag/current sensing are omitted. Keep position feedback and fryer internal temperature regulation, independent power stop/protection, mechanical guarding/load retention and qualified mains inspection. Movable-guard interlock need/type is conditional on the actual guard.
- No unverified claim that either fryer already meets the independent overheat requirement. User's new Shopee choice supersedes the Hanabishi preference; variant now confirmed Single-6L, while actual nameplate, accepted protected model/manual and fit remain required. B01 now uses screenshot-listed PHP 1,194 with the unresolved protection/fit conditions.
- Mechanical fabrication, food/packaging and optional tools are excluded from the electronics totals. Fryer allowance is shown once and can be assigned to the mechanical team without rebuying.

## Current deliverables and budget

- `docs/BOM.md` and `BOM_Automatic_Fries_Machine.xlsx`: simplified Table A prototype/reusable materials, Table B additional permanent materials and Table C fees. No reusable item charged twice and no fee mixed into material prices.
- Last planning budget (16 October 2026, not receipt prices or refreshed quotations): Table A **PHP 7,779.00**; Table B **PHP 8,338.40**; priced materials **PHP 16,117.40**, including the PHP 1,194 fryer candidate. Without fryer: **PHP 14,923.40**. Six material entries and two fee entries remain unquoted/conditional. Ownership updates do not change these historical planning prices; actual amounts paid were not supplied.
- Table C: **PHP 0 user assembly outside labor**, plus any actually paid qualified review/inspection/help and delivery. No outside panel-building fee is imposed; free professional service is not assumed.
- Complete materials/fees/grand totals: **Quote needed**, not zero. These partial subtotals include estimates and are not a final complete quotation or guaranteed savings claim.
- Earlier workbook, BOM and explanation preserved in `docs/archive/`; original PDF unchanged. Existing price references rechecked where accessible; previous unlocated jumper/buck prices explicitly estimates.

## Earlier validation status (before cleanup)

- Source workbook rendered before editing; source values/formulas inspected.
- Revised workbook totals independently reconciled to line-item quantity x unit price calculations; no formula-error matches in the revised ranges.
- A temporary PHP 100 unit-price change updated the dependent grand total correctly; the original input was restored before saving.
- Revised Table A/B, totals, price sources, operating notes and purchase holds rendered and visually checked. All item descriptions and amounts are readable; row heights adjusted to fit.
- Reopened the exported Excel file and verified cached totals, the corrected automatic first-drop timer wording, single-sheet structure and original backup contents. Excel desktop execution has not been tested; the formulas use ordinary multiplication and SUM.
- No hardware currents, basket torque, cooking recipe, actual probe ratings or final safety circuit have been physically verified.

## Open purchase holds

1. Empty basket/mounting mass, retained-oil allowance, sprocket pitch radius, tilt lever arm, travel, target speed and load-holding/brake design.
2. A working mechanical path from the raised basket to the distant receiving funnel. An extra transfer axis, if necessary, must be added explicitly to the BOM and power/pin budgets.
3. Packet dimensions, coil pitch, loaded torque, exact motor current/stall data and cam/index design; buy/test one candidate before all three.
4. Access to an appropriate reference thermometer for validation; no compulsory external controller-temperature probe. Validate warm-up and recipe with actual loading conditions.
5. Protected fryer model/manual/nameplate, independent overheat cutoff, grounding, oil limits, basket/tank fit and allowed external control.
6. Final basket motors, compatible driver continuous/peak ratings, PSU/transient margin, fuses, wire/connector ratings and itemized licensed-electrical panel/commissioning quote.
7. Actual fixed/movable guarding and load retention; quote an interlock if the accepted guard requires it. Operator bag placement replaces proposed bag sensing.

## Next action

User will resume assembly in a **new chat**. Persistent resume source: `docs/handoffs/2026-11-05-assembly-resume.md`. Adapter is now owned and user reports measured12V; first pending Step26 checkpoint is a clear adapter label/plug photo plus how polarity/voltage were measured, current rating and power connector details. Do not repeat identical voltage measurement merely to reset the workflow. A12V reading is not proof of5A capacity or loaded performance.

USB logic checks passed; preserve source and working inputs/LCD/common signalGND. Before a protected single flavor-channel test, actual module terminal topology, power wiring/connector ratings, fuse/diode suitability, safe-OFF/reset, secure unloaded mounting and independent disconnect still need review. Driver GPIO is not assigned. No motor current through breadboard/DuPont leads or12V on Mega5V/LCD rails. STOP selection is not safety acceptance; no new STOP/A10/LM2596/redwire/switch receipt reported. No device operation, flash, install or Phase3 authorization from this handoff.

The GitHub destination supplied by user is `https://github.com/hanssantos02/fries-machine.git`, branch `main`. Folder initially had no.git; initialized/fetched remote and based localmain on original README commit2e5c478 without changing existing project files. User explicitly requests commit/push main; preserve history, no force push or new PR. Publication status is recorded in the save log below; checkpoint18ebf34 was pushed and remote-verified on5November.

## Historical work log

Earlier statements below about no received parts or no Phase 2 approval apply to their dated entries, not the current state.

### A08 flavor/start buttons on 15 October 2026 (Step 32)

- Reviewed screenshot: GarageSale01 GS normally-open momentary pushbutton, Model C visibly selected, PHP 20 per piece; two terminals pictured. Direct product page unavailable. Exact mounting diameter/thread, environmental rating and delivered contact operation unverified.
- Added A08 supplier and native clickable link; quantity three retained, one per flavor. Replaces PHP 105 allowance with PHP 60, reducing priced materials by PHP 45. No extra ordinary start buttons or duplicate prototype buttons added. Signal controls only; A09 emergency stop remains separate.
- Recalculated and visually reviewed A08; saved XLSX validates PHP 20 × three = PHP 60, PHP 17,212.40 priced subtotal, 32 native clickable links including A08, no formula-error cells and retained unknown-cost totals.
- Current Table A PHP 9,138; Table B PHP 8,074.40; priced materials PHP 17,212.40 (without fryer PHP 16,018.40). Six material quotes/conditions and separate fees remain. Updated PROJECT, BOM and fryer budget note. No purchase, installation, physical wiring or phase transition.

### A07 roller microswitch on 15 October 2026 (Step 31)

- Reviewed user SHOPOMATIC.ph SHOPO listing/screenshot: roller lever, three terminals pictured, PHP 22 and explicit 1 piece per order. Direct product page inaccessible. No exact manufacturer model, terminal ordering, environmental or low-current ratings inferred from photo.
- Added candidate supplier/link and observed price to A07. Quantity seven retained: four provisional basket endpoints and three coil indexes. Correct sensing form, subject to actual mounting/travel/contact reliability and protected dry/cool placement. These are signal switches, not motor/heater power contacts or safety-rated emergency-stop devices.
- Omron primary contact-selection guidance supports checking low-current contact reliability/minimum applicable load; manufacturer ratings not assigned to seller switch. COM/NC/NO definitions saved without guessing physical pin order or starting wiring/firmware.
- A07 PHP 154 replaces PHP 280 allowance, PHP 126 reduction. Table A PHP 9,183; Table B PHP 8,074.40; priced materials PHP 17,257.40 (without fryer PHP 16,063.40). Six material quotes/conditions and separate fees remain. No duplicate prototype switches or spare quantity added.
- Updated PROJECT, readable BOM, motor guide and fryer budget note. No purchase, physical test, firmware, package install or phase transition.
- Recalculated/exported and reviewed A07/summary/source views. Saved-file validation confirms PHP 22 × seven = PHP 154, PHP 17,257.40 priced subtotal, 30 native clickable links including A07, unchanged unrelated inputs/formulas, retained diode quote and no cell errors. Complete totals still expose outstanding quotes.

### LR7843 selected price and description on 15 October 2026 (Step 30)

- New screenshots select LR7843 at PHP 50 and provide seller text: 3 V/5 V inputs, high-level start, low-level stop, PWM and DC motor switching. This resolves the previous selected-price and advertised signal-interface gaps. Treat as seller documentation, not tested isolation/current/thermal/safe-OFF performance.
- Replaced A06 complete-set PHP 160/channel allowance with module-only PHP 50 × three = PHP 150. Added A06.1 quantity three suitable flyback diodes if no valid onboard path is established, price/model Quote needed. No duplicated discrete MOSFET/gate assembly; A15 exclusions updated to avoid rebuying diode/gate pieces.
- Priced subtotal decreases PHP 330: Table A PHP 9,309; Table B PHP 8,074.40; priced materials PHP 17,383.40 (without fryer PHP 16,189.40). This is not a guaranteed PHP 330 complete-channel saving because diode cost is now separately unquoted. Six material entries and two fee entries remain unquoted/conditional.
- Actual input current/reset OFF, selected motor running/stall load, module heating and suitable flyback path remain later acceptance checks. Loose connectors may need soldering. No unsupported assumption that body diode/opto provides motor protection or that 161 A applies to this board.
- Updated PROJECT, BOM, motor/fryer guides and source S20. Builder unknown-cost count now includes both material tables; native hyperlink assertions resolve item rows by ID to accommodate the added row. No firmware, physical tests, package install or phase transition.
- Exported/recalculated after correcting the quote-completion check to account for quantities greater than one. Reviewed changed module/diode/passive rows, summary and sources. Saved-file verification checks every material/fee input and subtotal against source, six unquoted material entries, retained missing-total markers, 28 correctly positioned native hyperlinks and no cell/ZIP errors. Removed stale managed link anchors when rows move.

### A06 control-input MOSFET module on 15 October 2026 (Step 29)

- User supplies fulabs.ph module link/screenshot with LR7843, AOD4184 and FR120N options, PHP 49 and no selected variant. Boards show separate control pads; terminal blocks/headers pictured loose. Direct page inaccessible. No assertion that input thresholds, isolation, current capacity or motor protection are established by the photo.
- Added LR7843 as provisional A06 candidate and clickable supplier/source links. Infineon genuine IRLR7843 primary data supports logic-level gate operation at 4.5 V; explicitly distinguishes MOSFET gate characteristics from the module's optocoupler-input requirements. No transfer of 161 A IC number to whole-board current rating.
- Need 5 V logic input/current and safe OFF behavior, 12 V load compatibility, actual motor running/stall current/thermal margin and suitable flyback path. External rated motor diode remains needed if not already supplied by the actual circuit. Do not assume MOSFET body diode/opto is sufficient; retain existing sub-2 A stall screening until design revised.
- A06 keeps three complete-channel sets at PHP 160 estimated each (PHP 480), now explicitly module plus any missing protection. PHP 49 is not booked as the full-channel cost or as a confirmed selected LR7843 price. No old discrete MOSFET/gate assembly bought additionally; actual module/protection costs must replace the estimate when known. No total change.
- Updated PROJECT, BOM and motor guide; no purchase, wiring, firmware, installation or phase transition.
- Recalculated/exported and visually checked A06 and source notes. Saved-file validation confirms candidate URL and complete-channel price caveat, 28 native clickable links, unchanged prices/quantities/formulas/totals, retained LCD and no cell errors. Current priced subtotal stays PHP 17,713.40; complete total still exposes missing quotes.

### A06 manual PWM controller review on 15 October 2026 (Step 28)

- User supplies ENG LAB.ph Shopee motor PWM/dimming controller link/screenshot. PHP 49 and minimum purchase quantity three observed. Photo shows manual potentiometer and four power/motor terminals; no documented external Arduino PWM/enable input supplied. Max 5 A is advertised, not verified continuous module capacity. Direct Shopee access unavailable.
- Assessed for A06 based on ongoing item sequence. Not accepted as a direct replacement: manual internally generated PWM does not establish Arduino-commanded start/stop at the coil index. No blanket claim that the board cannot be adapted, but adaptation/additional switch would add unverified work/parts and is not selected.
- Explained required module features: documented 5 V logic signal interface, 12 V motor/load match, current/thermal capacity and inductive-load protection. DFRobot primary documentation used as a functional example only, not a selected priced PH product or specs for the submitted board.
- Recorded decision in PROJECT/MOTOR_SELECTION. A06 remains the existing provisional three-channel MOSFET/diode allowance; workbook/links/prices unchanged. No claimed PHP 333 saving or minimum-order purchase. No firmware, wiring, test, package install or phase transition.

### A05 replacement candidate on 15 October 2026 (Step 27)

- User explicitly confirms A05 flavor-coil role, reports previous listing sold out and supplies different Shopee seller 156048989 listing. Screenshot selects 12V 30RPM 25GA-370 at PHP 214. Actual shipping panel says PRE-ORDER ships in 5 days, despite Ready Stock title; direct web access unavailable.
- Recorded replacement candidate in A05 with observed price and native clickable link; quantity three unchanged, PHP 642 subtotal. Removed old S6 source, added S19. GA12-N20 inquiry is superseded, not a parallel purchase. No claim the new motor is proven stronger or adequate solely because it is larger or named 370.
- Voltage/type fit the planned nominal 12 V brushed-DC architecture, but rated torque/duty, running/stall current, shaft/mounting and loaded-coil requirements remain open. A06 remains conditional on verified stall current; 30 RPM nominal two-second turn is not proven packet delivery or loaded speed. Keep index feedback and validate stopping/coasting.
- PHP 858 reduction from former three-at-PHP500 allowance: Table A PHP 9,639; Table B PHP 8,074.40; priced materials PHP 17,713.40 (without fryer PHP 16,519.40). Five material quotes and separate fees remain. Same selected motors will be reused in final product.
- Updated PROJECT, readable BOM, motor guide and fryer budget note. No purchase, physical test, firmware, install or phase transition performed.
- Recalculated/exported workbook; reviewed updated A05, summary and source notes. Saved-file check confirms selected variant and pre-order caveat, PHP 214 × three = PHP 642, PHP 17,713.40 priced subtotal, 25 native clickable links including new G18 target, retained unrelated inputs/formulas and no cell errors. Complete total remains “Quote needed.”

### GA12-N20 candidate on 15 October 2026 (Step 26)

- User supplied fulabs.ph Shopee GA12-N20 link/screenshot. No voltage or speed selected; family price PHP 163-165, variants 3/6/12 V and 15-1000 rev/min. No rated torque, current, shaft dimensions or loaded-coil fit established; direct product page inaccessible.
- Assessing as possible A05 flavor-coil alternative based on sequence/context, not treating it as a stepper or a demonstrated basket actuator. No blanket claim that all N20 motors cannot move a basket; this listing lacks sufficient evidence for that role.
- Need selected-variant rated running torque/duty, running/stall current, shaft/coupling data and actual loaded-coil turning requirement. Suggested inspecting the 12 V/15 rev/min data first for the existing supply/slow-motion plan; not an approval to buy. No imported Pololu numerical ratings assigned to the generic seller motor.
- Saved pending review in PROJECT/MOTOR_SELECTION. Per the user's suitability-first workflow, workbook/A05 price/quantity/links remain unchanged until this candidate is adequately specified; no claimed savings or duplicate practice motor. No firmware, physical tests or phase transition.

### Basket DC driver product on 15 October 2026 (Step 25)

- Reviewed user fulabs.ph/FU LABS Shopee link and screenshot: IBT-2 marking, two power IC packages, one motor terminal pair and PHP 275 displayed. Direct page inaccessible; price/product evidence is the screenshot, not independently verified delivered hardware.
- A04 is the correct candidate architecture for the proposed brushed-DC lift/tilt motors, conditional on actual motor voltage/current/stall demand and board cooling/ratings. One module powers one reversible DC motor. “Double” is two half-bridges, not two independently driven motors. A single module is not the matched bipolar-stepper driver.
- Checked Infineon primary datasheet: BTS7960 IC is a half-bridge with a typical 43 A current-limitation level. This does not establish the marketplace module's continuous current capability, IC authenticity or thermal performance. Do not buy on the advertised current number alone.
- Replaced A04 supplier link/reference price with PHP 275 each, quantity two provisionally; subtotal PHP 550. Removed unused Circuitrocks S5 source, added S17 seller/S18 IC reference. Native clickable links must be reapplied after export.
- PHP 14 increase: Table A PHP 10,497; Table B PHP 8,074.40; priced materials PHP 18,571.40 (without fryer PHP 17,377.40). Five unquoted material entries and separate fee quotes remain. No additional duplicate driver set or practice motors.
- Updated PROJECT, BOM and fryer budget note. No physical purchase/test, firmware, package install or phase transition.
- Exported/recalculated and reviewed driver/summary/source views. Saved Excel check confirms PHP 275 × two = PHP 550, PHP 18,571.40 priced subtotal, 25 native clickable links including new driver and retained controller/fryer targets, unchanged unrelated inputs/formulas and no cell errors. All complete-total fields still expose missing quotes.

### Clickable Excel links on 15 October 2026 (Step 24)

- User explicitly requests clickable links. Added 24 native Excel external hyperlink relationships: 11 matching material supplier/reference cells plus 13 source URL entries. Applied blue underlined font styles; existing labels, prices, formulas, cached values and layout preserved.
- Artifact HYPERLINK evaluation was already known to return unsupported text, and targeted native API help returned no match. Used bundled lxml/ZIP only for the missing native hyperlink capability, adding SpreadsheetML hyperlink nodes/relationship targets and link styles. No HYPERLINK formulas, package installs or outside-project writes.
- Integrated the native-link helper into the existing canonical workbook builder after export, so subsequent product updates retain clickable links. References resolve from item/source IDs, not fixed row assumptions. Unknown supplier URLs were not invented.
- Verified ZIP integrity, all relationship targets and external modes, controller/fryer links, unchanged cell texts/formulas/cached amounts and summary values. Rendered and visually reviewed controller and source-link styles. Actual desktop Excel click-through has not been exercised.
- Updated PROJECT/BOM notes; prices and current PHP 18,557.40 priced subtotal unchanged. No phase transition or hardware work.

### Selected controller price on 15 October 2026 (Step 23)

- New user screenshot visibly selects **2560 R3 With Cable** at **PHP 699**; full-size board, assembled headers and USB A-to-B cable pictured. This resolves Step 22's variant-price uncertainty; PHP 199 headline is not used.
- Replaced A01 PHP 1,030 original supplier reference with PHP 699; kept supplier URL and quantity one. Removed unused original source S1 from current workbook source list; updated S16 with selected-price evidence. No additional board or cable budgeted.
- PHP 331 reduction: Table A PHP 10,483; Table B unchanged PHP 8,074.40; priced materials PHP 18,557.40, or PHP 17,363.40 excluding the fryer. Five unquoted material entries and separate fees still prevent a complete quotation.
- Updated PROJECT, BOM, fryer-assessment budget note and workbook inputs. Actual delivered board/USB-serial chip will be checked later. No physical purchase, firmware, installation or phase transition performed.
- Recalculated/exported workbook and reviewed the updated controller row, summary and source notes. Saved-file check confirms PHP 699 row price, PHP 331 reduction, PHP 18,557.40 priced subtotal, preserved formulas/unrelated material and fee inputs, retained LCD/URL and no cell errors. Complete totals remain “Quote needed.”

### Controller product link on 15 October 2026 (Step 22)

- Reviewed user Shopee link/screenshot: listing mixes full-size 2560 R3 With Cable, MEGA2560-CH340G, compact MEGA2560 PRO and PRO TYPE-C. Recommend full-size With Cable to match the existing controller/layout and minimize beginner header soldering. No unsupported claim that compact PRO cannot operate the machine.
- Arduino primary Mega documentation confirms the ATmega2560 platform's 54 digital pins, 16 analog inputs and I2C capability for the proposed controls/LCD. This is a platform comparison, not proof of this clone's exact USB chip, supplied accessories, build quality or shipping condition. Direct Shopee access unavailable; user screenshot used for listing evidence.
- Added the supplier URL to A01's Where-to-buy cell plus source S16 and exact option instruction. Screenshot PHP 199 is explicitly after voucher with no variant selected; do not assume it is the full-size With Cable price. A01 retains original e-Gizmo PHP 1,030 reference, clearly labeled; no claimed savings or total change. One board only, reused in final machine.
- Synchronized PROJECT and readable BOM. No new purchase, firmware, installation or physical build performed. Selected variant price and delivered-board checks remain pending; no phase transition.
- Exported and visually checked controller row/source notes; verified saved URL, exact option, price caveat, retained totals/formulas and LCD. Artifact engine's HYPERLINK function returned unsupported-function text, so removed it and stored the full supplier URL as cell text before delivery; no unsupported formula output remains. Existing prices and calculations unchanged.

### Product-link workflow on 15 October 2026 (Step 21)

- User explicitly authorizes reviewing incoming product links/images and adding suitable products' links to the Excel BOM for the matching item. Check the selected variant, function and required ratings/fit before accepting; identify gaps instead of guessing.
- Suitable links/details can be added directly within this ongoing authorization. Preserve quantities/reuse, avoid buying both alternatives, synchronize docs/BOM.md and update dependent totals if price/quantity changes. Delivery/services stay separate.
- No new product was submitted in this instruction, so the Excel workbook is unchanged. Recorded workflow in PROJECT; remain in Phase 1.

### Selected fryer screenshot details on 15 October 2026 (Step 20)

- Four new user screenshots show Single-6L visibly selected at PHP 1,194, outer size W28.5 × D43.5 × H30 cm, advertised 2500 W heater and 60-200°C temperature control. Treated as seller claims/observed listing price, not a verified nameplate, safety certification or physical fit test.
- Replaced B01 Hanabishi PHP 5,325 allowance with the selected Shopee unit once. Difference PHP 4,131; Table A unchanged PHP 10,814, Table B priced subtotal PHP 8,074.40, priced materials PHP 18,888.40. Five material quotes/conditions and separate fee quotes remain outstanding. Shipping not included in product price.
- Conditional current at advertised 2500 W: 10.87 A if rated 230 V; 11.36 A if rated 220 V. Actual voltage is not established. Corrected B06-B09 explanation/supplier draft to avoid inheriting the former 2400 W heater specification; no final switching/protection ratings asserted.
- Retained unchanged mechanical layout, final-use motor reuse, I2C LCD and timed warm-up/cooking. Check basket clearance from rear heater/control head, tank rim and handle path. Five-minute warm-up remains a trial, not verified readiness.
- Updated PROJECT, BOM, power-control guide, fryer assessment and workbook data/source. Remaining seller information needed is exact nameplate/manual, independent thermal cutoff/earthing, basket dimensions/mass and permitted power-restoration behavior. No supplier message sent, firmware or physical build performed.
- Exported and visually checked changed summary, fryer/control rows and source notes. Reopened the saved workbook: only intended fryer/input/source text and dependent totals changed; all formulas preserved, no Excel cell errors, LCD retained once and fees separate. Price-change recalculation checked; complete total still exposes outstanding quotes.

### Shopee fryer feasibility on 15 October 2026 (Step 19)

- User provides a product link and screenshot, identifies it as the fryer to use and asks whether it is doable. Recorded the new preference in PROJECT and saved FRYER_ASSESSMENT. No screenshot marketing text treated as instructions or verified specifications.
- Screenshot shows DALANDAN LIVING PH, Single-6L/Double-12L choices and PHP 1,194; no variant visibly selected. Web tool could not access the actual Shopee page. No exact model, power, independent cutoff, grounding or dimensions established.
- Conditional feasibility: intact thermostatic fryer with documented suitable external power-control behavior can support existing timed cycle. External basket linkage/motors remain necessary; verify clearance of heater/control head/rim and fit within unchanged PDF design. Single-tank option is the first economical candidate for one basket, not a confirmed variant or performance claim.
- User confirms Single-6L (one tank). Need seller nameplate/manual, thermostat/overheat/earth evidence, power-restore behavior, dimensions/basket mass and confirmed selected price. Prior 2400 W load and PHP 5,325 allowance are not inherited by the new fryer.
- Workbook unchanged for question-only review and unknown selected price/specs; accepted fryer will replace B01, not add a second unit. Prior priced subtotal remains historical planning for the old fryer. No firmware, live wiring, physical tests, installations or phase transition.

### Basket-motor wording clarification on 15 October 2026 (Step 18)

- User asks why A16 says “do not buy yet” despite using final motors in the prototype. Clarified that reuse and selecting a suitable product are separate decisions: the chosen final units will be bought once and tested, but no exact A16 model has been selected.
- PHP 2,000 each / PHP 4,000 for two is an unverified planning allowance, not a confirmed market quotation, guaranteed sufficient budget or proof of lifting ability. These are the proposed basket lift/tilt motors, distinct from three flavor-coil motors.
- Selection needs full moving basket/support/food/oil mass, existing transmission geometry, speed/travel, mounting and power-off retention; 300 g food alone does not establish required turning force. The phrase protects against an unsuitable purchase and does not mean postponing motor tests until final assembly.
- Read current project/BOM/motor context; workbook unchanged because the request is an explanation. No firmware, physical tests, installations, flashing or phase transition.

### Final motor reuse and flavor coil clarification on 15 October 2026 (Step 17)

- User explicitly confirms that motors purchased for testing must be the selected final-use units. The BOM/workbook already removes separate practice motors and charges actual motors/drivers/supply only once in Table A, with final reuse noted; no further motor-price reduction or duplicate purchase was introduced.
- Explained that the flavor spiral is a mechanical part: either a suitable stepper with matched driver/reference handling or a geared DC motor with index switch can turn it. Current A05/A06 remain the latter proposal; user asked about steppers but did not mandate a substitution. Do not buy both alternatives.
- Expanded MOTOR_SELECTION with beginner definitions, DC index sequence, stepper-driver distinction and one-turn/one-packet validation. Corrected old warm-up-clarification and external-temperature statements to match the accepted timed cycle.
- Rechecked Pololu stepper-driver compatibility and Makerlab SGM-370 PHP 500 listing (sold out; inconsistent speed description). No unsupported stepper price or final torque rating assigned. Exact flavor/basket selections remain pending loaded mechanism inputs.
- Updated PROJECT, BOM and motor guide. Workbook quantities/prices already reflect the requested reuse rule and were not changed. No firmware, physical tests, installs, flashing or phase transition.

### LCD restoration on 15 October 2026 (Step 16)

- User explicitly requires retaining the I2C LCD. Restored one 16x2 PCF8574-backpack candidate as A18, bought once and reused; other item IDs retained.
- Rechecked Makerlab MLE00659 PHP 150. Listing shows sold out; confirm stock before purchasing. Candidate 5 V logic/backpack and I2C address must be verified during approved testing.
- Display planned for selected flavor, adjustable warm-up/cooking countdowns, basket/cycle status and faults. No temperature display or measured-ready claim without a sensor. Timed warm-up/cooking and unchanged PDF design retained.
- Table A priced subtotal PHP 10,814; Table B priced subtotal unchanged PHP 12,205.40; priced materials PHP 23,019.40 (PHP 17,694.40 without fryer). Five unresolved electrical entries and separate unquoted fees remain; complete total unavailable.
- Updated BOM/workbook, current explanation and PROJECT. Checked recalculation, saved values/formulas and changed display/summary/removal-note views. No firmware, wiring, physical build, installs, flashing or phase transition.

### Timed sequence on 15 October 2026 (Step 15)

- User asks to enable heating on the flavor-button press, wait an initial proposed five minutes, then advance automatically by time. Interpret the next job as the existing ten-minute cooking interval; durations configurable. Initial elapsed time before lift is fifteen minutes, plus draining/motion.
- Controller performs elapsed-time sequencing. Intact manufactured fryer thermostat regulates heat; verified independent thermal cutoff and hardwired stop remain required. No extra timer module, separate temperature controller, firmware or physical build is needed/started in Phase 1.
- Removed A02 MAX6675 and A03 oil probe from compulsory purchases, making external temperature monitoring optional. Basket/coil position switches and drivers remain. Historical IDs retained to avoid changing other references.
- Five-minute warm-up is unverified. Check actual oil fill, starting temperature, 300 g batch, loading and repeat-cycle conditions during approved testing. If food is already in oil during warm-up, it is heating then too. No new automatic loading mechanism or frame change assumed.
- Priced Table A subtotal now PHP 10,664; priced materials PHP 22,869.40 with fryer, or PHP 17,544.40 excluding fryer. Reduced by the former PHP 1,199 temperature-reader/probe allowance; estimates and outstanding electrical/fee costs still prevent a complete total.
- Updated current sequence and BOM; worksheet calculations, missing-quote markers and saved line prices checked after changes. Physical cooking/motion and oil readiness remain untested. No packages installed, sudo, flashing or outside-project writes.

### B06–B09 parts listing on 15 October 2026 (Step 14)

- User will assemble these controls personally. Retained qualified mains supervision/review/inspection before energizing, as AGENTS.md recommends, without assuming paid outside assembly. C01 changed to review/inspection/help only if hired; C03 user labor remains zero.
- Asked fryer planning basis and received explicit HFRY60SS confirmation. Use seller-listed 230 V/2400 W (~10.43 A) for provisional selection, not evidence of delivered nameplate/cutoff. Oil preheat/timer question remains unresolved.
- B06 K1 handles normal heating; B07 K0 independently removes heater/motor-supply power through hardwired E-stop/manual restart. Candidate genuine LS Metasol low-voltage DC coil family; exact variant, AC-1 and power-supply inrush ratings/local price still need supplier confirmation. No certified safety-system claim.
- Expanded B08 into single-channel 5 V interface (Circuitrocks SKU 2833 PHP 65, sold out), proposed MEAN WELL HDR-15-24 (RS PHP 1765.40 inc. VAT), hardware RESET, supplier-compatible suppression and additional control-wire/fuse pieces. Dedicated 24 V supply is conditional on coil/load/stop design; verified 12 V coil alternatives might reuse A17 but must not compromise power removal or holding.
- Expanded B09 into conditional Type A/30 mA RCBO candidate (CHINT NB4LE 2P C16 code 292721, quote/site check), enclosure, DIN rail, covered terminals/earth bar, rated mains cord/plug/socket and strain relief. Reuse verified existing protection/kit contents, keep factory fryer cord; no duplicate DC items.
- Corrected interface candidate after inspecting the PHP 150 listing's inconsistent DC/board ratings; did not use its advertised 30 A as heater suitability evidence. Even the selected small interface's actual DC/inductive rating and trigger behavior need verification before connection to a 24 V coil.
- Verified primary LS catalog, MEAN WELL specs and CHINT device catalog; retained unknown correct-variant prices rather than treating mixed marketplace variants as confirmed quotes. Material estimates are labeled, not quotations.
- Saved docs/POWER_CONTROL_PARTS.md with listing, definitions, current price references and unsent supplier quote text. Updated BOM, spreadsheet and PROJECT; current unchanged PDF and Table A costs preserved. Qualified review fee separate; no supplier contacted or physical work performed.
- Validated recalculating subtotals and missing-quote propagation after expanded rows; inspected saved formulas and changed views. No installation, package changes, sudo, flashing or writes outside project.

### BOM cleanup on 15 October 2026 (Step 13)

- Applied spreadsheet skill to the authorized restructuring; one current worksheet with three clearly named tables and an opening subtotal/unknown-cost summary.
- Removed two IR detector pairs, LCD, two current sensors, two practice basket motors, separate bench supply, two extra ordinary buttons, bag switch and spare breadboard. Removed unquoted PHP 5,500 bundle/2,500 labor allowance and automatic 700 guard-interlock purchase. Guarding remains required and a movable-guard interlock must be quoted if necessary.
- Moved actual basket motors and final suitable factory-enclosed supply into Table A for cold-test/final reuse. Retained full-size Mega/cable for familiar connectors. Two basket DC axes remain provisional, not an approved mechanism or mandatory stepper rejection.
- Replaced bundled electrical assembly with B06 normal fryer contactor, B07 independent power disconnect, B08 coil/restart interfaces and B09 protected mains installation materials. All four sets unquoted, material-only. Qualified work and shipping are separately unquoted C01/C02; DIY low-voltage outside fee C03 is zero.
- Combined fixed/moving DC harness allowances and removed duplicate fuse/terminal, driver-resistor/diode and enclosure/mounting kit scope. Updated references to new item numbers.
- Independently reconciled JSON/document/workbook subtotals. Tested price-edit recalculation, one supplied quote with other quotes still missing, complete temporary quotes and restoration to blank unknown prices. No formula errors found. Rendered/reviewed all changed table sections and summary; saved file retains formulas and unknown-cost markers. Excel desktop execution is not tested.
- Updated PROJECT and replaced BOM_EXPLAINED with a short current guide; preserved prior documents/workbook in archive. No work outside project, installations, sudo, flashing or physical build.
- Preheat/timer clarification, load/trajectory/motor/driver/supply sizing, accepted probe/fryer and actual electrical/fee quotes remain before purchasing approval. No budget ceiling inferred and no Phase 2 transition.

### Updated user requirements on 14 October 2026 (Step 12)

- User explicitly rejects changing the drawn design. The closer-funnel/shorter-frame/custom-guide concept and PHP 14,254.43 partial alternative are superseded; they must not be used as the retained-design budget.
- Any of three flavor buttons now requests its packet and starts the fryer/cooking process. Potato-start detection is removed. Controller-operated heating permission must be specified; manual-only normal fryer ON/OFF is not adopted as accepted scope.
- Asked whether oil is already preheated or button initiates warm-up before the ten-minute cooking interval. No answer assumed. Heated-from-cold elapsed time cannot be represented as ten minutes at cooking temperature.
- Explained that steppers are optional. Geared DC motors with position switches remain economic candidates; actual motor choice needs total basket/support/food/oil mass, geometry, speed, running/stall or phase current, compatible driver, position feedback and power-off retention. Neither step counting nor NEMA frame designation establishes a safe lift.
- Recommended ignoring held/repeated flavor-button presses while busy to avoid duplicate packets/cycles; this is proposed logic, not a confirmed separate packet-only feature.
- Saved docs/MOTOR_SELECTION.md; updated PROJECT and current-override notices in BOM, BOM_EXPLAINED and CHEAPER_DESIGN. Historical worksheet retained; no replacement grand total or motor price invented.
- Checked primary Oriental Motor torque/frame/brake documentation and Pololu stepper configuration guidance. No firmware, wiring/build guide, installation, flashing or physical build performed. Phase 1 continues.

### Cheaper design explanation on 14 October 2026

- Revisited the PDF overview, fryer, cutter, spirals, chain, funnel and bracket images. The remote right-hand funnel is not reached by a demonstrated basket trajectory in the supplied drawing. Proposed bringing it alongside the fryer, retaining right-hand discharge through a short chute and shortening the frame only if mechanical fabrication permits.
- Applied the brainstorming skill's non-software route to compare alternatives. No subagents, physical prototype or firmware work.
- Proposed a conditional guided, hinged carriage: cook upright, chain-lift to drain, lift farther through a captive guide to tip, reverse to straighten/lower. Three basket positions plus three coil index switches. Full dumping, forces, clearances, retention and power-off holding remain unverified. A published curved-guide tilt principle is supporting context, not proof of this complete dumping design.
- Keep two basket motors as fallback if guide fabrication outweighs the saved motor/driver cost. Do not silently replace automatic discharge with manual tipping.
- Proposed operator preheat/normal fryer ON/OFF with intact thermostat, while controller monitors temperature, senses potato drops, times and controls motion. This removes proposed normal Arduino heater permission only if accepted; independent thermal protection and hardware emergency disconnection remain required.
- Rechecked listed Mega2560 Pro Mini PHP 495 (preorder, unsoldered headers), BTS7960 PHP 268, LCD PHP 150 and HFRY60SS PHP 5,325. Smaller coil motors at PHP 200 each are explicitly unverified variant/torque allowances, not approved purchases. One final basket motor remains an unverified PHP 2,000 allowance; supply PHP 1,500 and simpler permanent low-voltage construction PHP 1,200 remain estimates.
- Candidate control/sensing subtotal PHP 4,229.43; adding one basket motor, supply and low-voltage permanent assembly gives PHP 8,929.43; adding the listed fryer gives PHP 14,254.43. Independent stop/protection, inspection, USB/header/temporary supplies are unpriced; mechanical fabrication, delivery, tools and food/packaging are excluded. None is a complete final total or verified savings claim.
- Saved `docs/CHEAPER_DESIGN.md` with full explanations and provenance, plus `docs/CHEAPER_DESIGN_CONCEPT.png`. Visually reviewed the 1600x1200 concept image and corrected text overlap. Added proposal links/limitations to BOM and PROJECT; retained old workbook totals so an incomplete estimate is not substituted as a finalized purchase list.
- Next decision is whether mechanical layout/linkage changes are allowed. No approval of the new architecture or move to Phase 2 inferred from the request for explanation.

### B4 clarification on 14 October 2026

- Explained that B4 is not a specific necessary PHP 5,500 product and not a second motor driver/supply. It combined several functions without a verified design/price.
- Distinguish the fryer's internal thermostat, optional controller-operated normal heater ON/OFF, and independent hardware stop/protection. A thermostatic fryer does not need another temperature-regulating power controller merely because the cooking timer and basket are automated.
- Proposed cheaper architecture for discussion: operator enables/sets intact fryer; its thermostat maintains heat; controller senses drop, times cooking and moves basket/flavor coils. Normal automatic heater switching would be omitted under that alternative, so obtain confirmation before adopting it. Independent emergency disconnect, verified thermal protection, appropriate electrical protection and guarded/load-retained motion remain accounted for.
- A6/A9 drivers, B3 supply, B8 DC protection/harness and A12 E-stop are already priced; any replacement electrical BOM must avoid counting these again within B4. Reuse suitable existing appliance/site protection only after verification.
- No new replacement prices invented, no blanket PHP 5,500 savings asserted, no controller/firmware/wiring changes and no live work. Historical spreadsheet totals retained and explanatory documents updated with the clarification.

### Guided self-assembly preference on 14 October 2026

- User asked to do electrical work personally with guidance. Offer full beginner guidance for isolated low-voltage electronics and stepwise dry testing, requesting observations/readings before progressing.
- Recommend qualified electrical instructor/licensed electrician supervision and inspection for household-mains installation, protective earthing, disconnects and thermal protection before energizing. Guidance via chat cannot establish those physical protections. Do not characterize UK HSE guidance as Philippine law.
- B11 PHP 2,500 is an unverified paid-service allowance. It may be reduced by DIY low-voltage labor or replaced by actual no-charge qualified school support. No inspection-service price or availability has been verified.
- If all outside paid B11 service is genuinely replaced, same-design arithmetic is PHP 28,201.86 with fryer or PHP 22,876.86 without fryer, before replacement inspection costs if any. This is not a new finalized quote; spreadsheet baseline retained.
- B4 hardware is not removed by doing labor personally. Its bundled scope needs itemization and simpler design review; do not claim PHP 8,000 savings by deleting B4+B11.
- Prefer an intact manufactured fryer and enclosed low-voltage adapters for early tests; keep the fryer's thermostat and thermal protection. Any external heater-run permission change is a design proposal requiring scope confirmation, not a silently removed user function.
- Updated project/BOM explanation notes; no wiring, flashing, installation or physical build performed.

### Explanation completed on 14 October 2026

- Added `docs/BOM_EXPLAINED.md`: plain-language machine sequence; price/quantity/estimate definitions; all 31 lines with calculations and price provenance; functional groups whose totals exactly reconcile; motor/driver, two-probe, practice/final motor and power-supply distinctions; power/pin vocabulary; required versus proposed feedback/convenience features; cost exclusions and procurement-overlap risks.
- Marked the existing proposal's listed-price portion as PHP 9,636.86 and its unverified allowance portion as PHP 21,065.00. Neither amount implies final compatibility or guaranteed delivered prices.
- Explicitly identified the large B4 power-control bundle as an unquoted design allowance, not a ready-made product with known component prices. Labor and kit contents need itemization to avoid overlap.
- Rechecked original supplier references for controller, temperature reader, coil candidate and fryer; prices still displayed PHP 1,030 / 199 / 500 / 5,325. BTS7960 listing now displays PHP 268 rather than snapshot PHP 267. Explanation retains the old workbook totals for comparison and discloses the PHP 2 two-board difference. No spreadsheet price/quantity changes made during this explanation request.
- Added a link to the explanation at the start of `docs/BOM.md`. Reconciled all functional groups and confirmed every original line is explained once.
- User has not yet answered the budget-ceiling question; no answer assumed. Current user request is explanation, not phase approval or a selected reduced-function design.

### Cost review on 14 October 2026

- User asked whether PHP 30,701.86 is too expensive for student-thesis clients. Agreed the proposal did not adequately prioritize economical thesis procurement.
- B4 panel materials/assembly allowance (PHP 5,500) plus B11 labor (PHP 2,500) account for **PHP 8,000 of unquoted allowances**. These are not verified contractor prices.
- B2 basket actuators add another **PHP 4,000 unverified allowance**; basket load/geometry remain unknown.
- B1 complete fryer allowance is **PHP 5,325**, included at the user's request, with independent protection still unverified.
- Existing controller/sensor/display/coil-drive/control subset (A1, A2, A4, A5, A6, A8-A11, A13, A17, A19) sums to **PHP 5,287.86**. This excludes final basket motors, oil-rated probe, power/protection assembly, installation/harness and test equipment. It is not a complete machine quote.
- Requested budget ceiling through the user-input tool. No answer assumed, no replacement price or reduced-function design selected. Workbook quantities/prices remain unchanged pending an actual revision; BOM notes now identify the cost objection.

## Environment and permissions

- Only files inside this project have been created/modified; original PDF and `AGENTS.md` unchanged.
- Existing bundled Python, Node, spreadsheet and PDF tools used; no packages installed, no sudo, no device flashing.
- Temporary context renders/build scripts are under `tmp/`; these are support files, not physical build steps or firmware.
- Before any later package install, sudo use, flashing or write outside this project, show exact Linux commands and ask permission per `AGENTS.md`. Physical steps require user observations before continuing. No Phase 2/3 wiring/code/build guide has been started.

### A09 LA38 candidate on 15 October 2026 (Step 34)

- User listing: https://shopee.ph/product/459134338/12816027599 (liuma.ph). Screenshot advertises multiple switch types, including LA38 STOP, and PHP 98–140 range; no selected variant-specific price visible. Direct page inaccessible.
- LA38 STOP is the candidate option to inspect, not an approved A09 selection. Need exact manufacturer/model/contact block, latching/twist or pull release, documented positive opening and NC configuration (preferably two NC). LA38 Reset R/Lock R labels alone do not establish emergency-stop suitability.
- Requested selected STOP variant and rear/contact-block/specification evidence. No price or approved supplier substituted in Excel; existing A09 PHP 500 estimate and totals retained.

### A09 selected LA38 STOP screenshots (Step 35)

- New screenshots visibly select LA38 STOP at PHP 140, resolving variant/price uncertainty. Seller description says LA38 22 mm, 10 A and CCC; these generic listing claims do not establish the emergency-stop operating mechanism, NC contact count, direct-opening function or control-circuit utilization rating.
- Candidate price recorded here, not substituted for the qualified A09 budget. Ask seller for exact manufacturer/model, rear contact-block markings/datasheet, latching release method and documented direct opening. No unsupported claim that two NC contacts are mandatory for every design; two NC remain preferred for the provisional arrangement.
- Existing BOM and totals retained pending essential compatibility evidence. No physical test, purchase or phase transition.

### A09 provisional purchase accepted for later inspection (Step 36)

- User elects to test selected LA38 STOP after receipt. Added provisional A09 supplier link and PHP 140 screenshot price in place of PHP 500 allowance; PHP 360 reduction in priced subtotal. No claim that latch/continuity testing establishes positive-opening certification.
- Required latching action, NC contacts (preferably two), exact manufacturer/model, direct-opening documentation and control-circuit rating remain unresolved. Do not accept for safety service on appearance/continuity alone; replacement/contact-block costs may be necessary and are unquoted.
- Table A PHP 8,778; Table B PHP 8,074.40; priced materials PHP 16,852.40, without fryer PHP 15,658.40. Six existing unknown material entries and separate fees retained. No physical test performed, firmware/build phase not started.
- Saved XLSX validated: A09 PHP 140, Table A PHP 8,778, priced materials PHP 16,852.40, 34 native clickable links including A09, complete totals still Quote needed, no formula-error cells. Changed row rendered and reviewed.

### A12 jumper listing (Step 37)

- User screenshots: ENG LAB.ph selected male-male 10 cm PHP 49; other end combinations and lengths offered. Direct page inaccessible. One M-M, one M-F and one F-F bundle retained, approximately 20 cm preferred; 40 leads/bundle and other variant prices need confirmation.
- Supplier link added; A12 updated from PHP 39 × three = PHP 117 to mixed-variant planning estimate PHP 49 × three = PHP 147. Only selected male-male 10 cm price is screenshot-verified. Old S8 supplier reference removed.
- Table A PHP 8,808; Table B PHP 8,074.40; priced materials PHP 16,882.40, without fryer PHP 15,688.40. Signal use only, no motor/heater or permanent safety-stop current. No duplicate final harness purchase.
- Recalculated/exported and reviewed A12: saved values PHP 49 × three = PHP 147, PHP 16,882.40 priced materials, estimate label preserved, correct native supplier link, 34 links total and no formula-error cells. Complete totals remain Quote needed.

### A13 LM2596 module (Step 38)

- User screenshot Zantop Fiber adjustable LM2596 module PHP 35; direct Shopee page inaccessible. TI primary reference supports adjustable step-down architecture but does not verify seller board authenticity/current capacity.
- A13 replaces PHP 45 allowance with PHP 35 × one; native supplier link and manufacturer source added. Proposed 12 V to 5.0 V logic supply, below 1 A planning load. Output setting/stability/thermal test and final controller power/USB isolation routing remain later-phase work. Not a direct AC supply or motor/heater driver.
- Table A PHP 8,798; Table B PHP 8,074.40; priced materials PHP 16,872.40, without fryer PHP 15,678.40. Existing six unknown material entries and separate fees remain. No build, purchase, installation or physical test performed.
- Workbook recalculated/exported and A13 visually reviewed. Saved XLSX confirms A13 PHP 35, Table A PHP 8,798, priced subtotal PHP 16,872.40, native A13 supplier link (35 links total), no formula-error cells, and retained Quote needed complete totals.

### A14 fuse/holder candidate links (Step 39)

- Holder screenshot selects 5pcs 5x20 Fuse Holder at PHP 68; title advertises 22 AWG leads. Fuse screenshot shows PHP 35, current options and two sizes, no selection. Do not infer exact-current purchase price, mixed assortment, supplied fuses with holders, or actual DC/current/interrupting ratings. Both direct pages inaccessible.
- Added S28 holder, S29 fuse and S30 Littelfuse selection reference. Record as provisional low-current protection candidates; do not approve for basket motors/heater. Match physical fuse size and branch startup/current/time curve plus lead/holder rating and fault breaking capacity; exact values remain pending motor/supply data.
- Retained complete A14 PHP 180 estimate covering remaining rated branch holders/fuses, terminals and reverse-polarity protection. No duplicate PHP 68/35 charges added, no exact pack quantity ordered. Table A PHP 8,798; Table B PHP 8,074.40; priced materials PHP 16,872.40.
- Workbook recalculated/exported and A14 rendered/reviewed. Saved A14 allowance PHP 180 and PHP 16,872.40 subtotal unchanged, both supplier links native-clickable (fuse link in sources), 39 links total, no formula-error cells and complete totals still Quote needed.

### XH-M609 low-voltage disconnect (Step 41)

- User screenshot/link https://shopee.ph/product/421779283/16193894719 advertises XH-M609 12–36 V low-voltage battery disconnect at PHP 103. Direct page inaccessible; no further undocumented ratings assumed.
- Not needed for currently planned factory-enclosed DC supply with no battery. Advertised undervoltage-disconnect function is not evidence of reverse-polarity/short-circuit protection and does not replace A14 fuse parts or A17 supply. Not added to Excel or totals. If seeking A14 reverse-polarity item, search 12 V DC MOSFET reverse polarity protection module, then match current/voltage/thermal ratings after load data.

### A15 shopping breakdown (Step 43, 16 October 2026)

- Saved docs/A15_SHOPPING.md with search terms, proposed quantities, purpose, through-hole preference, polarity explanation and explicit unverified PHP 45–140 loose-part estimate before delivery. No confirmed seller prices or component purchases inferred.
- Ceramic 100 nF × ten initial pack allocation: five provisional motor positions and local logic/signal filtering; up to three 1000 uF 25 V bulk positions for current 12 V driver groups, one 470 uF 16 V logic buffer. Check existing capacitors and final ripple/stability/inrush/thermal requirements before additions. Not a validated final filter or regenerative clamp.
- Resistor values/counts pending input/module circuit; no unnecessary assortment. Do not duplicate A06 MOSFET modules, A06.1 diodes or A10 indicator/buzzer parts. Existing A15 PHP 200 allowance retained, not replaced or supplemented by this estimate. No Excel edit, build phase or physical installation.

### A15 selected 104 ceramics (Step 44, 16 October 2026)

- Screenshot visibly selects 100nF/0.1µF, PHP 3 each and quantity ten; listing advertises 50 V, sold per piece, MOQ six. Ten satisfies shown minimum. Direct Shopee page inaccessible; screenshot is price/variant evidence, not tested quality.
- Added S31/native link to A15. PHP 30 ceramic allocation inside unchanged PHP 200 set allowance; remaining PHP 170 clearly unitemized estimate until electrolytics and signal needs sourced. No duplicate extra charge or claim all A15 parts cost PHP 30.
- Updated BOM, PROJECT and A15 shopping detail (partly sourced PHP 65–120 capacitor range, electrolytics still estimates). Worksheet review date updated to 16 October; historical source dates preserved. No purchases, tests or phase transition.
- Recalculated/exported and visually reviewed A15. Saved XLSX retains PHP 200 set/total PHP 16,872.40, clearly records 10 × PHP 3 ceramic allocation, native supplier link (41 links total), no formula-error cells and Quote needed complete totals.

### A15 1000µF bulk candidate (Step 45, 16 October 2026)

- Screenshot BCD Electronics Shop 20PCS/SET 1000µF 25V 10×20 mm PHP 69; direct page inaccessible. Nominal value/form/voltage match proposed 12 V branch but temperature, ESR, ripple rating and series/data unverified. Do not infer qualification from sleeve appearance.
- Added S32 candidate source link; A15 main supplier link remains selected S31 ceramics. Up to three bulk positions proposed, not twenty required; any pack purchase costs full PHP 69, not prorated PHP 10.35. No three-pack quantity or extra charge added.
- A15 PHP 200 remains PHP 30 selected ceramics plus PHP 170 unitemized remaining estimate. Updated shopping note, PROJECT and readable BOM. No purchased hardware, physical testing or phase change.
- Workbook recalculated/exported and A15 rendered/reviewed: PHP 200 set allowance and PHP 16,872.40 priced subtotal unchanged, no reported formula errors; S32 candidate has native clickable source link (42 links total), selected ceramic main link preserved.

### A15 bulk pack selected provisionally (Step 46, 16 October 2026)

- User cannot locate requested temperature/ESR specifications and elects previous BCD listing for now. Set provisional purchase quantity ONE pack of twenty at PHP 69, with up to three initial placements. Do not claim 105°C, low ESR or verified ripple rating. Received-part inspection/load assessment may require replacement; basic checks do not establish missing manufacturer ratings.
- A15 now allocates PHP 30 ceramics + PHP 69 pack = PHP 99 selected purchases, PHP 101 estimated remaining parts, unchanged PHP 200 total. Supplier source/link retained and status changed from candidate-only to provisional selection. No physical test, purchase report or phase transition.
- Recalculated/exported and visually reviewed A15. Saved XLSX verifies PHP 99 selected allocation plus PHP 101 estimate within PHP 200, total PHP 16,872.40 unchanged, 42 native links including bulk listing and no formula-error cells. Shopping note now budgets whole pack: capacitor-only PHP 104–114 including estimated remaining logic capacitor.

### A15 selected 470µF 16V pack (Step 47, 16 October 2026)

- Screenshot selects 16V 470UF 8x12mm 20PCS at PHP 76, quantity one. Direct page inaccessible. Nominal capacitance/voltage match 5 V buffer; manufacturer/temperature/ESR/ripple ratings not established. Do not assume generic image depicts selected part markings.
- Added S33 native source link, full PHP 76 pack cost within A15. One initial position only; smaller verified offer can replace if cheaper delivered. A15 now PHP 175 selected capacitor purchases + PHP 25 unitemized signal-parts estimate, total PHP 200 unchanged; remove remainder if not needed after circuit review.
- Refreshed shopping note with current quantities/prices instead of stale candidate estimates. BOM/PROJECT synchronized. No purchase, wiring, physical check or phase transition.
- Export/recalculation and changed A15 rendering checked: saved PHP 175 capacitor allocation plus PHP 25 estimate inside PHP 200, subtotal PHP 16,872.40 unchanged, no formula-error cells and 43 native links including S33.

### A16 shopping opened (Step 48, 16 October 2026)

- User proceeds to A16. Saved search categories and required seller/mechanical evidence in docs/MOTOR_SELECTION.md. No motor model, RPM, load capacity or PH quote invented. Existing PHP 2,000 × two estimate is not a selected product.
- Request basket/moving-support mass and existing driven-shaft/linkage dimensions/description from mechanical team; food mass alone insufficient. Compare geared DC first; stepper needs changed drivers and separate power-off retention assessment. No extra practice motors or layout redesign.

### A18 LCD source and A16 deferral (Step 49, 16 October 2026)

- User cannot contact mechanical team before fryer arrives; proceed with independent shopping, do not guess basket motors or dependent supply. Phase remains materials buying.
- Screenshot ALLAN/allantimer LCD1602+I2C PHP 120, blue display with rear backpack thumbnails. Direct page inaccessible. Matches display/interface category; verify complete adapter included/assembly, ratings/address/pins and functionality later. No specific PCF chip or delivered performance inferred from thumbnail.
- Replaced A18 PHP 150 with PHP 120, quantity one, S34 supplier link; obsolete S4 source removed. Table A PHP 8,768; Table B PHP 8,074.40; priced materials PHP 16,842.40 (without fryer PHP 15,648.40). No additional display/backpack or fee.
- Saved XLSX validated: LCD PHP 120, Table A PHP 8,768, priced subtotal PHP 16,842.40, native A18 supplier link and 43 links overall, no formula-error cells, complete totals Quote needed. Actual A18 row rendered/reviewed after adjusting focused LCD preview range.

### B02 shopping opened (Step 50, 16 October 2026)

- Saved docs/B02_SHOPPING.md: search terms, terminal/shield/perfboard definitions, full-size Mega compatibility and included assembly/pin access checks. DFRobot manufacturer category reference, not a PH quote or ratings for another listing.
- Compare one Mega screw-terminal shield; FR4 2.54 mm perfboard/header/terminal kit alternative requires more custom soldering. Do not buy both complete alternatives or duplicate A14 terminals. No motor power or mains on this signal board. Existing PHP 350 estimated allowance unchanged pending actual listing.
- Phase 1 purchasing only; no physical build instructions, install, firmware or phase transition.

### B02 Welded Board selected (Step 51, 16 October 2026)

- User screenshot Aliex IC Store MEGA2560 screw-terminal prototype shield; Welded Board selected PHP 270, quantity one. Direct page inaccessible. Assembled terminals/headers/prototype area pictured; seller claims full-size Mega2560/R3 fit. Actual assembly/underside headers, fit/clearance, pin continuity and power routing remain checks; no invented schematic or current rating.
- B02 now one assembled terminal/prototype shield, replaces PHP 350 perfboard/carrier kit allowance. No second whole perfboard/header set, no Arduino duplication, no mains or motor-power routing through board.
- Table A PHP 8,768; Table B PHP 7,994.40; priced materials PHP 16,762.40, without fryer PHP 15,568.40, PHP 80 reduction. Existing six unquoted materials/fees remain. No installation, physical test or phase transition.
- Recalculated/exported and visually checked B02 and summary: saved quantity one × PHP 270, B subtotal PHP 7,994.40, priced materials PHP 16,762.40, complete totals Quote needed, no formula-error cells, and native B02 link (45 links overall).

### B04 shopping opened (Step 52, 16 October 2026)

- Saved docs/B04_SHOPPING.md with first wire search terms, low-current scope, copper vs CCA, ordinary stranded vs repeated-flex distinction and remaining harness categories. No unverified gauge/current limit, length, exact connector count or PH price invented.
- Motor cable sizing remains dependent on A16/A17 and route/fuse coordination. Fixed signal wire can be compared now; no requirement to purchase expensive branded cable. Retain B04 PHP 1,150 complete estimate, not hookup-wire-only cost. Reuse appropriate A14/B02 terminals and avoid duplicating B03/B05/B09 items.
- No Excel change, physical assembly, package installation or phase transition.

### B04 wire quantity/colors entered (Step 53, 16 October 2026)

- User requests Excel shopping details for physical-store per-metre purchase. Added 22 AWG stranded copper/tinned copper, red/black/blue/yellow/white each 2 m, 10 m summed conductor length, as initial shopping allowance rather than measured final cable route.
- Roles red low-current +5 V, black DC0V, other colors labeled signals; not mains protective-earth convention. Motor cables/current sizing and moving cables not assigned this gauge or quantity.
- Wire price unknown, retained B04 complete harness PHP 1,150 estimate without duplicate wire fee. Updated shopping note, readable BOM and PROJECT. No hardware purchase reported, installation or phase transition.
- Saved workbook verified and B04 visually reviewed: all five colors at 2 m each/10 m total in C41, complete allowance PHP 1,150 and subtotal PHP 16,762.40 unchanged, no formula-error cells; existing 45 native hyperlinks preserved.

### B05 shopping opened (Step 54, 16 October 2026)

- Saved docs/B05_SHOPPING.md: one self-adhesive label sheet/local-print option, three flavor labels and emergency-stop identification; no label printer purchase. Actual label size/flavor wording to confirm. No new PH price quote assumed.
- Seven A07 switches may need rigid fixtures/fasteners, but not seven automatically purchased brackets. Exact screw diameter/length/fixture count awaits delivered switch holes and existing mounts; check mechanical-team provisions first. No guessed screw assortment or food-contact fabrication added.
- B05 PHP 300 complete estimate unchanged; excludes existing B03 enclosure, B04 harness and B09 mains hardware/labels. No Excel edit or phase transition.

### B05 Yasen label pack (Step 55, 16 October 2026)

- Screenshot selected PP Matte A4 180gsm at PHP 158, twenty sheets, quantity one. Direct page inaccessible. Record actual PP option despite title vinyl language; no invented waterproof-ink, oil/heat or printer compatibility claim. Inkjet media; check actual intended printer and printed sample.
- Added S36 native supplier link; selected material appropriate for label role with environment/print checks pending. B05 whole allowance PHP 300 retained: label pack158 + remaining hardware estimate142. Do not prorate one sheet price as actual pack purchase, buy twenty packs, buy a label printer or bundle printing fees into materials.
- Updated PROJECT/BOM/shopping note, no total change or build phase. One sheet may suffice; local smaller offer can save if lower delivered cost.
- Workbook recalculated/exported and B05 rendered/reviewed: PHP 158 selected label allocation + PHP 142 estimate inside PHP 300, total PHP 16,762.40 unchanged, no formula-error cells, native B05 supplier link and 47 links overall.

### B06 shopping opened (Step 56, 16 October 2026)

- Added focused search terms/spec explanation to docs/POWER_CONTROL_PARTS.md. One K1 normal fryer contactor, existing proposed 24 V DC coil architecture. 20 A AC-1 is a provisional selection target, not a verified rating assigned to every LS family listing. Exact order code, nameplate, coil consumption and contact arrangement needed.
- Clarify control-coil voltage vs heater main-contact voltage, AC-1 heater vs AC-3 motor headline rating, and no direct Arduino coil drive. Existing internal fryer thermostat/cutoff retained. No actual matching PH supplier quote, no invented price or purchase. B06 remains Quote needed.
- No Excel edit, wiring, installation or phase transition.

### B06 broader search (Step 57, 16 October 2026)

- Web search found Shopee leads 750550293/26089306360 and 1201429789/25283305784; provided shorter CJX2Z 24V DC coil search terms. Brand LS is not mandatory. Saved links/limitations in power-control procurement note.
- No exact variant selected or price/rating assumed. Need coil label, manufacturer AC-1/load rating and required auxiliary contacts; do not infer NC auxiliary from 3210 title. Do not substitute AC-coil or DC-main-only device based on ambiguous listing title. No Excel changes or supplier messaging.

### B06 simple.ph CJX2-1810 review (Step 58, 16 October 2026)

- User screenshot listing 1253203453/27004405033 has contactor/overload/set options, no selected variant, PHP210–408 range. Direct page inaccessible. Pictured coil appears mains AC with 50 Hz marking; not the proposed DC24V control coil. Exact supplied-part data needed; do not overread unclear coil voltage.
- Visible auxiliary13NO/14NO, no NC established. AC-1/manufacturer/exact price unverified. Do not add JR28-25 overload or set automatically. Request suitable24VDC variant and rating evidence; AC-coil adoption requires explicit architecture review. No Excel edit, purchase, physical test or phase transition.

### CJX2 220 V AC options (Step 59, 16 October 2026)

- User Jayson Electric one link777946608/42206576962 shows220V AC options and PHP259–529 family range, no selected option. Direct page inaccessible. No exact coil frequency, AC1 heater rating/manufacturer or auxiliary configuration verified.
- Explain coilAC is not inherently unusable, but requires deliberate revision/review of associated control/stop/interface parts; current24VDC plan not automatically changed. No highest-current option recommended merely on headline. No Excel edit, purchase or physical work.

### Why B06 / coil flexibility (Step 60, 16 October 2026)

- User challenges repeated difficult DC24V searches. Clarified exact coil voltage/brand is engineering choice, not feature requirement; previous search instruction too restrictive. Low-voltage coil rationale is control-wiring voltage, not cooking requirement. Manufacturer AC-coil contactor evidence confirms alternative architecture is possible.
- Broaden next review to documented available AC-coil device with heaterAC1, voltage/frequency/auxiliary data and whole control/stop/interface review. Do not falsely declare current generic220V candidate qualified or automatically deleteB08.2 without replacing dependent arrangement. Avoid buying both alternatives; qualified mains review retained without imposed labor contractor.
- No Excel mutation or user approval request; work remains Phase1 selecting concrete parts, not energized build.

### CJX2 option comparison (Step 61, 16 October 2026)

- User asks which option. Identify CJX2-1810(18A220V) as first provisional comparison variant, not a verified sufficient purchase. Neither accept18A nor reject12A by AC3headline alone. No exact supplier price available.
- Explicit60Hz coil check needed for PH supply; manufacturer guidance cautions against assuming50Hzcoil suits60Hz samevoltage. Need heaterAC1>=20A and exact auxiliary contacts; visibleNO does not proveNC. No Excel mutation, control redesign completion or wiring.

### B06 selected-price/spec evidence (Step62, 16 October2026)

- New screenshots select CJX2-1810(18A220V) PHP289 and seller text50–60Hz, Ith32A, three main poles, oneNOaux. Frequency claim resolves seller-information gap, not tested hardware; noNCaux claimed. Ith32A/Ui690V not assigned as operational heater orcoil ratings.
- Added provisional B06 supplier/price. Explicit procurement HOLD on B07/B08 while AC-coil interface/control/stop/reset/suppression arrangement reviewed; no unsafe mains qualification for prior65PHP relay or automatic24V supply purchase. Keep conditional existing costs until replacement design concretely specifies what is removed/replaced; no savings invented.
- TableA8768, TableB8283.40, priced17051.40, withoutfryer15857.40; five material unknowns (fourB + oneA). No physical testing, final mains design or phase transition.
- Recalculated/exported and reviewed changed B06/B07/B08 rows. Saved XLSX validates B06 PHP289, B subtotal8283.40, priced17051.40, five unknown material entries, explicit HOLD statuses, no formula-error cells and native B06 supplier link (49 total links). Complete totals remain Quote needed.

### B07 shopping review (Step63, 16 October2026)

- Explained B06 normal fryer switching vs B07 independent heater/motor power removal. Same availableCJX2-1810 listing is a comparison candidate, not automatic duplicate purchase or certified safety function. Previous289 screenshot is reference only, no B07 price inserted.
- B07 cannot be finalized from heater load alone: pendingA17 input/inrush, contactor making capacity, coil/control voltage, aux contacts/manualreset and actualA09 ratings. Do not automatically choose32A, route mains through unverifiedEStop or delete24Vsupply without complete arrangement. Saved focused procurement note with MEANWELL inrush reference.
- No Excel edit, purchase, construction or phase transition.

### B08.1 shopping focus (Step64, 16 October2026)

- Saved relay-module search terms, quantityone and distinction between5V supply/logic vs ACcoil contact path. Need integrated transistor driver, low GPIO input current, suitable coil inductive/pickup contact capacity, wholeboard separation/covers and safeOFF. No bare relay directGPIO or generic10A heater switching recommendation.
- DFR0017 primary example shows architecture only, not a PH selection or ratings for marketplace module. Interposingrelay/socket/driver alternative only if necessary; no duplicate assemblies. ExactB06 coil and independentstop arrangement pending; noExcel edit or approvedmains wiring.

### B08.1 ENG LAB candidate (Step65, 16 October2026)

- User screenshots listing1021339444/22577819886, 1/2/4channels and5/12/24V, noselectedvariant, PHP49–199 range. DescriptionLOW-trigger,maxAC250V10A/DC30V10A. Directpage inaccessible.
- Targetonechannel5V qtyone; no exactprice or guaranteedopto assumed. Needexactfront/backphotos, coilinductive/pickup match, wholeboardmains separation/driver and startupOFF. Multichannelphoto features notassignedtoonechannel. Request selectedoptionprice/photo; noExcelmutation until candidate details resolved. No wiring/purchase/phasechange.

### B08.1 selected relay price (Step66, 16 October2026)

- User now selects1-Channels +5V atPHP49, qty1. AdvertisedLOW-trigger from prior description. Exactboardphoto not treated as proof ofopto, creepage/clearance, ACinductive contact rating, safeGPIOcurrent/resetOFF or B06coilmatch.
- AddedS38/native link, removedobsoleteS11 active reference. Oneprovisional lowvoltage-test candidate replacesold65, notextra relay; mainsacceptanceHOLD. B07/B08.2 architecturepending. UpdatedPROJECT/BOM/fryer budget and powerparts currentoverride; historicalnotes remainhistorical.
- TableA8768, TableB8267.40, priced17035.40, withoutfryer15841.40; reduction16. Five existingunknownmaterials andseparatefees retained. No purchase reported, physicaltest or phasechange.
- Workbook recalculated/exported and B08.1 visually reviewed: saved1×PHP49, TableB8267.40, priced17035.40, explicitmainsHOLD, noformulaerrorcells, completeQuoteNeeded totals and nativeB08.1link (49 links overall).

### B08.2 review (Step67, 16 October2026)

- User proceedsB08.2; no new part needed for currentB06ACcoil/B08.1 5V. Recommendskip purchase; not same asA17motor PSU/A13buck. B07 lowvoltage independentstop requirement remainsunknown, so nofalsefinaldeletion/guaranteedsavings.
- ExistingB08.2HOLD alreadyexplicit inExcel; unchangedPHP1765.40 conditionalprice inplanning subtotal. Savedcurrent purchasingdecision, no newsourcing or physicalwork.

### B08.3 RESET search (Step68, 16 October2026)

- Userproceeds; providedLA38 genericsearch, momentary1NO completebutton+block, quantityone, noLED supplyneeded. Preferblue labeledRESET; notlatching, extra mushroom or headonly. PrimarySchneider examplecategoryonly, notbrandmandate/price.
- Resetrestorespermission deliberately, notautomaticcooking/motion; actualhardwiredcircuit/controlvoltage/contactinductiveduty stillpending. No guessedcurrentrating or B08.2deletion. NoExcelmutation or Phase2work.

### B08.3 Jayson LA38 candidate (Step69, 16 October2026)

- User777946608/42354881235 screenshot sellerstates1NO+1NC,22mm, below10A generic, self-reset immediate springreturn vs self-locking retained untilrepress. No optionsselected, PHP62–81 range. Directpage inaccessible.
- Targetgreen +Self-reset qtyone withRESETlabel; blue unavailable notmandatory. Exact price/contactvoltageduty notestablished; no mains/safetyacceptance from generic10A. Askselectedvariantprice, keepExcelQuoteNeeded unchanged. Nophysicalwork orphasechange.

### B08.3 selected greenSelf-reset (Step70, 16 October2026)

- Screenshot nowselectsgreen +Self-reset PHP62 qtyone. Earlierdescription provides22mm,1NO+1NC and immediate springreturn. AddedS39/native supplierlink, price replacesunknown, no directmains acceptance or safetycertification claimed.
- TableA8768, TableB8329.40, priced17097.40, withoutfryer15903.40; four unknownmaterialentries (threeB +oneA), separatefees unchanged. Existing24Vcontrol allowance remainsconditional, B07/interface/reset compatibilityreviewpending. No purchase reported, wiring orphasechange.
- Recalculated/exported and visually reviewedresetrow: saved1×PHP62, TableB8329.40, priced17097.40, fourunquotedmaterialentries, noformulaerrorcells, QuoteNeeded complete totals and nativeB08.3link (51 total).

### B08.4 suppression procurement (Step71, 16 October2026)

- SavedACcoilRC searchterms, resistor-capacitor definition, documentedMOV alternative and exactcontactor compatibility/need checks. Schneiderprimaryexample illustratescategory, notCjx2fit or PHquote.
- Buyonlymissing compatibleaccessories; finalcountdependsB07. Do notsubstitute plainDCflybackdiode orA15lowvoltagecaps, inferMOVvalues, mandatebothRCandMOV, or assumeexposedmodulemains safety. Dropouttime affectsstopreview. NoExcelmutation orphysicalconnection.

### B08.4 duplicate search clarification (Step72, 16 October2026)

- Userreportssearchshowspriorcontactor. ClarifiedB06switch vsB08.4accessory; do notbuysecondcontactor asB08.4. Previoussearchwording unhelpful; noverifiedPHaccessorylink identified.
- LeaveB08.4pending actualsupplier/coil evidence, notclaimunnecessary or deleteprotection blindly. Preparedsame-seller compatible/built-in question withoutsending. NoExcelmutation, shoppingduplication orphasechange.

### B08.5 duplication/controlbranch check (Step73, 16 October2026)

- UserproceedsB08.5. ExistingrowconditionalHOLD, notanotherautomaticwire/fusepack. B04signalwire andA14DCparts alreadyplanned; ACcoil wiring/protection requiresactualratings/coilpickup/fault andstoparrangement review.
- Noexactwiregauge/fusevalue guessed, noDC holderapprovedforAC, noautomaticprotectiondeletion. Keep150conditionalestimate untilmissingparts itemized. NoExcelmutation orphysicalwork; nextB09.1requiresoutletprotectioncheck.

### B09.1 protection shopping (Step74, 16 October2026)

- ExplainedRCBOcombinedfunction andsearchcriteria, notmandatoryC16installation. Needactualsitecircuit/load/supplytopology/earthing/faultlevel andexistingprotection checkedbyschoolstaff; avoidsduplicatepurchase. No livepanelopening instructions. TypeA,30mA andC16differentmeanings; no100/300mAsubstitution.
- CHINTprimaryfamily page/catalogconfirmcandidatecategory; noPHprice ormarketplacevariant approval. FoundS14 lowercasecatalogURL404, updatedcorrectcapitalizedreference inpowernote; nativeExcelS14linkrepairpendingnextauthorizedexport. NoExcelmutation orphasechange.

### B09.1 TX63LE candidate (Step75, 16 October2026)

- User277704323/14295512771screenshots showRCBOcategoryclaims30mA6kA230V/2P, mainphoto16A50/60Hz, noselectedcurrent andPHP347–388range. ModelTX63LE isnotTypeAleakageproof. Noindependentrating/testapprovalinferredfromCE/IECtext.
- RequestTypeAdatasheet andselected16Aprice forcomparison; sitewiring/topology/actualload andexistingprotectionstillpending. L/Nmarking requiresactualpole/neutralcompatibilityreview. Noautomatic63A, TypeACsubstitution orpricingupdate.
- Directpage inaccessible; noExceledit orphysicalwork. S14catalogURLrepairremainspendingnextauthorizedexport (correctcapitalizedURLinpowernote).

- Manufacturer reference verified: https://www.taxnele.com/product/product-91-932.html repeats TX63LE 2P/30mA/6kA and combined-protection claims but omits Type A. Exact variant acceptance and price remain pending; workbook unchanged.

### B09.1 CHINT price range (Step 76, 16 October 2026)

- Reviewed user listing 615190079/29421243173: PHP798–1865 unselected range, advertised Type A/30mA; not a confirmed exact quote or typical market price. Manufacturer catalogue confirms Type A variants exist in NXBLE-63 family, not seller authenticity or exact variant acceptance.
- Request 16A + 2P Type A selection for comparison only; actual load/site/pole arrangement and existing school protection remain unresolved. No requirement to buy the maximum-price/multi-pole unit or EV-specific hardware. No workbook edits or purchases reported.

### Home testing location (Steps 77–78, 16 October 2026)

- Corrected unsupported school-outlet assumption. User confirms initial testing at home and personally builds the machine. PROJECT.md updated. Home outlet protection, earthing, circuit capacity and supply topology remain unknown.
- Retain B09.1 as planned machine protection pending exact selection; do not remove based on assumed upstream protection or imply an on-machine breaker makes any home outlet adequate. Licensed electrician review applies to mains installation and home circuit suitability; no physical wiring/test requested or performed. Current CHINT 16A/2P Type A option is only a comparison candidate, not final approval. No workbook edit or budget change.

### B09.3 DIN rail (Step 79, 16 October 2026)

- Explained mounting role/search terms; provisional one 1m 35×7.5mm slotted steel rail cut to layout, four end stops for possible two rows. Avoid rail/mounting duplication with enclosure/B05. Exact quantities depend on final layout. Manufacturer profile reference saved in power notes; no verified local quote.
- B09.1 purchasing deferred at user request, not declared unnecessary. Workbook unchanged, no phase transition or physical work.

### B09.3 ChaoMai candidate (Step 80, 16 October 2026)

- Saved user screenshot selected50cm/PHP49 and supplier URL in power notes. Looks like slotted top-hat rail but 35×7.5mm dimensions not established. Two pieces = PHP98 for provisional1m stock; count remains layout-dependent. End stops/fixings not included by evidence, so do not call existing PHP100 whole-kit estimate a confirmed quote. No workbook edit or phase change.

### B09.4 connection hardware (Step 81, 16 October 2026)

- Saved practical covered-terminal and earth-bar search terms, provisional one six-way strip + one six-way bar, no model/rating acceptance from search text. Actual conductor range/ratings/layout and enclosure inclusion must match; avoid duplicate B04 connectors.
- Explained protective-earth function and manufacturer category references in power notes. Existing PHP200 estimate unchanged, no verified quote, workbook mutation or physical work.

### B09.4 Anigo/SDE terminal listing (Step 82, 16 October 2026)

- Screenshot source 732230948/23570358234 shows covered TB-series terminals, seller600V claim; TB2506 greyed out and TB2503 available. Suggested selecting TB2503/25A for exact price, provisional two strips instead of unavailable six-pair unit. PHP49 unselected price not accepted as exact quote.
- Six pairs = six isolated positions, not twelve circuits; earth bar remains separate. Actual cable acceptance/cover inclusion/ratings require confirmation. No Excel mutation, phase change or physical wiring.

### B09.4 selected TB-2503 price (Step 83, 16 October 2026)

- Selected screenshot confirms PHP10 each. Recorded two provisional strips/PHP20 within existing PHP200 set allowance, PHP180 still unquoted remainder, S40 and native clickable supplier link. Earth bar and actual conductor compatibility remain pending.
- Export recalculation passed, zero formula error matches, priced subtotal PHP17097.40 unchanged, complete totals still Quote needed. Native hyperlink verification passed53 links with cell text/formulas preserved. Corrected S14 catalogue capitalization. Reviewed B09.4 rendered row; no physical work or purchase reported.
- Also corrected the remaining workbook B09.1 location wording to home test outlet. Re-export checks passed with unchanged totals and53 native links.

### B09.4 Wixim earth bar (Step 84, 16 October 2026)

- Saved JDS/Wixim268117918/15457423948 candidate and seller copper/8mm/up-to8AWG claims. Request6way selectedprice, qtyone provisional. Maximum wire size alone does not establish smaller earth-wire compatibility.
- Bar must serve dedicated protective earth; blue feet do not imply neutral use or bond enclosure automatically. Actual PE installation review remains pending. PHP200 set allowance unchanged, no selected exact quote/Excel edit or physical work.

### B09.4 Wixim selected price (Step 85, 16 October 2026)

- Screenshot confirms6ways/PHP189/qty1. AddedS41/native link and retainedS40 strip link. Replaced PHP200 estimate with PHP209 selected parts subtotal, no artificial accessory remainder. Mounting pieces still to check without duplication; actual wire acceptance/PE suitability remains pending.
- Recalculated/exported Excel, verified zero formula error matches, A8768/B8338.40/materials17106.40, complete totals Quote needed. Native hyperlink check passed54 links with prices/text/formulas preserved; rendered B09.4 reviewed for legibility. PROJECT/BOM/power notes synchronized. No purchase or physical work reported.

### B09.5 mains connection materials (Step 86, 16 October 2026)

- Saved shopping terms and roles in power notes. One incoming plug and one controlled fryer socket provisional; cable length to measure, factory fryer cord retained. Exact plug/socket shape deferred until factory plug/home outlet known, no adapter assumption. OMNI manufacturer16A250V example verified as category reference only, not a selected purchase or quote.
- Keep PHP850 estimate unchanged; B0422AWG is not mains cable. Qualified mains review required before energizing, no physical instructions or phase transition.

### Minimal first order (Step87,16October2026)

- User asks essentials only for first prototype order. Saved docs/PROTOTYPE_FIRST_ORDER.md and linked from BOM; controller699+LCD120+buttons60+three microswitches66+breadboard91+jumpers147=PHP1183, before shipping/tools. Breadboard PHP91 reverified on MakerPH; jumper mixed variants remain estimates.
- Clearly limited to logic/input/timer-state tests. Three switches are partial order from existing seven, not additional/removed master quantities. Deferred actual motors/drivers/supply/protection, four basket switches and permanent/mains hardware; full functional prototype cannot be finalized without actual mechanical/electrical inputs. No throwaway practice motors/supply. No workbook edits, installation, firmware or phase transition.

### Conservative flavor motors (Step88,16October2026)

- User proposes higher torque to enable purchasing now. Saved conservative comparison targets, mechanical envelope/shaft caveat and jam-damage implications without demanding complete force measurements before candidate search. ManufacturerCytron SPG30-GR270 data verified; not assigned to generic37GB520. Local price unverified, no invented PHPquote or existing642price applied to upgrade.
- LR7843 remains a board-level qualification question. SB5605A60V manufacturer-backed flyback candidate for documented1.2A-stall low-side motor only if suitable path absent; thermal/transient/circuit acceptance pending. No duplicate motor alternative, purchase, physical test or workbook mutation.

###25GA370 torque-table distinction(Step89,16October2026)

- Reviewed user93948225/1829351870screenshots.30rpm load770gf.cm=0.77kgf.cm, stall12kgf.cm; slow5rpm row1.15kgf.cm load. Poorly formatted table and repeatedratio/currentclaims not independentlyverified. No definitive insufficiency for unknownrealcoil, but no evidence of requested running-torque margin.
- No selectedvariant, PHP193–246range not exact quote. Savedassessment inMOTOR_SELECTION.md, noExcelchange or purchase/physicalwork.

### JGB37-520 variant review(Step90,16October2026)

- Saveduser1412288706/26828465072candidate:6/12/24V7–960rpmfamily, unspecifiedmaximum21kg.cm, no-load0.05–0.3A,6mmDshaft. Neither selectedvariant nor actualoperatingtorque/stallcurrent shown; no claimed21kg.cm ratedperformance. PHP352 conditionalvoucher not exactquote.
- Nextcomparison12VMotor35RPM and exactparameter-tablephoto. Noautomaticmanualcontroller/bracketpurchase ordriver/diodequalification. Tenkgf.cm remains conservativeproposal, not calculatedminimum. NoExcelmutation/phasechange.

### JGB37 rated-data comparison(Step91,16October2026)

- Userselected12V35RPMshowsPHP352 AfterVoucher, not unqualifiedbasequote. Table35no-load/28ratedrpm,3.4kgf.cm0.3Aload,1.2Astall;22no-load/18ratedrpm,5.5kgf.cm0.3Aload,1.2Astall. Read as sellerclaims only.
- Recommend22RPM for extraforce/slowdispense,~2.7s free/3.3s rated revolution; deliveryangle/timing unvalidated. No demandtochasearbitrary10minimum. MatchLR7843/protectionandsupplybeforepoweredtest; newvariantpriceandfitpending. NoExcelmutation orphysicalwork.

### Selected JGB37 flavor motor replacement(Step92,16October2026)

- User confirms12V22RPM same352price. ReplacedA05 prior25GA3703x214 withJGB37-5203x352=1056, delta414; savedS42/nativeproductlink and sellerlisted5.5kgf.cm18ratedrpm0.3A/1.2Astall. Price retainsAfterVoucher/quantityeligibility caveat; no purchase reported or guaranteedtorquemargin.
- ThreeLR7843modules150 =>1206motor/driver subtotal. Added to1183logic firstorder gives2389beforeunquoteddiodes/supply/protection/connectors/mounting/tools/shipping; no claim completepoweredkit. Docs/PROJECT/BOM updated, no duplicatedalternativepurchase.
- Export/recalculation checks pass, zeroformulaerrormatches. A9182/B8338.40/materials17520.40, fourmaterialquotes+twofeesunknown, complete totalsQuoteNeeded. Native55links verified withcelltext/formulas preserved. Motorrowrender reviewed. NoPhase2/physicalwork.

### Motorcompletionparts(Step93,16October2026)

- Saved electrical/mechanical checklist inMOTOR_SELECTION/PROTOTYPE_FIRST_ORDER. Existing3switches/3LR7843s/A15filters reused;3SB5605A60V candidateifverifiedonboardpathabsent. A17supply,A14protection,powerwire andmechanical3mounts/3cams/3couplingsstillneedmatch. No universal6to6coupling or 22AWGmotorwireapproval.
- No secondtemporaryPSUorcapacitorpack added, noexactfuse/wirepriceguess. MotoronlyLR7843cannotreverseautomatically; noextraencoder/manualPWM needed. NoExcelmutation,purchase/physicalworkorphasechange.

### SR5100 candidate(Step94,16October2026)

- User487295469/11536801341listingcontainsinconsistenttitle, exactdescriptionSR51005A100V vsSR31003A100V. Prefer10pcsSR5100, qtyonepack,3neededplus7spares. Noexactvariantselectedpriceorverifiedsellerdiodeauthenticity.
- Candidate5A100VSchottkysuitablecategoryfor1.2Astall12Vlow-side motor asSB560alternative, thermal/circuit/identityandmissingonboardpathchecksremain. Do notorderbothalternativesor3packs. Nextselectedpackprice; noExcelmutationorphysicalwork.

### SR5100 selectedpack(Step95,16October2026)

- Screenshotconfirms10pcsSR5100PHP64qty1. A06.1changedfrom3unquotedlooseto1packfull64cost, nativeS43supplierlink, noSB560duplicate. Threepositionsifneeded/sevenspares; deliveredidentity/thermal/circuitandmissingonboardpathchecksremain. No purchase reported.
- Saved/exported/recalculated, zeroformulaerrormatches. A9246/B8338.40/materials17584.40, withoutfryer16390.40; complete totalsQuoteNeededfor3materialentries+2fees. Native57linksverifiedwithvalues/formulaspreserved; diode-rowrenderreviewed. Docs/PROJECT/firstorder synchronized. No physicalwork/phasechange.

### Flavor supply proposal(Step96,16October2026)

- Suggested12V5A60Wenclosedadaptercomparisonfrom3x1.2Aclaimedstallpluslogicallowance, manufacturerGST60A12-P1Jreferenceverified. Localpriceunquoted, actualcurrentlimits/transients/connectorandcordpending.
- Explicitlyflaggedproposalchangesprioronesharedsupplyplan: adaptercanbereusedasfinalflavor/logicwithseparatebasketsupplylater; notautomaticduplicate/temporarypurchase, noBOMmutationuntilselection/reconciliation. No5Afullmachineapprovalorphysicalwork.

### Physical-store12Vadapter(Step97,16October2026)

- Userknowsphysicalstoreandrequestslistitem. ExcelA17now12V5A60Wenclosedadapterqty1priceunknownphysicalstore, no newonlinequote. Agreedpurchasecontextimpliesretainedfinalflavor/controlbranch, basketA17.1deferredunquoted. Reconciledold1500sharedestimatebywithdrawingit, notassigningunsupportedpriceorclaimingsaving.
- PROJECT/BOM/motor/power/first-ordernotesupdated. Export/recalculationpass, zeroformulaerrormatches, A7746/B8338.40/materials16084.40, completeQuoteNeededfor5materialentries+2fees. Native57linksverifiedunchangedcelltext/formulas; shiftedrowsrebuiltandbothsupplyrendersreviewed. No purchase/physicalworkorphasechange.

### DC motor wire/adapter connection(Step98,16October2026)

- Proposedinitial6m18AWGcopper(red3/black3)forshortfixedflavorpowerwiring, distinctfromexisting22AWGsignals; notfinalroute/basket/mainsapproval. Needdocumented5Aconnectorwithactualadapterfit/polarity, no2Abarrelsubstitution.
- ExactDCfuse/holdermustmatchwireandactualadapterfaultresponsebeforepower, noextrapriceorB04/A14duplicate. Notesonly, noExcelmutationorphysicalwork.

### PhysicalstorewireconfirmationandDCfusecandidates(Step99,16October2026)

- User approveswire/connectorphysicalstorelisting. Addeddocs/PHYSICAL_STORE_LIST.md, synchronizedB04/firstorder/PROJECT/BOM.6m18AWGred3+black3,1rated5ADCmatchedconnection, noextraquoteor1150duplicate. Separate22AWG10msignalsdeferred.
- Nextcandidates3standardATO/ATC32VDCholders18/16AWGleads+6matching2A32VDCfuses(3used/3spares). Exactadapterfaultresponse/fusecurve/wirematchrequired; fusesnotjamprotectorsandmain/logicprotectionstillpending. Noautomaticnewholderpurchaseoroldglasspackduplication.
- Exportrecalculationpass/zeroformulaerrors, pricedtotalsunchanged7746/8338.40/16084.40,5materialquotes+2feesunknown, completetotalsQuoteNeeded. Native57linksandcellvalue/formulapreservationverified, B04renderreviewed. No purchase/physicalworkorphasechange.

### Inlinebladeholder review(Steps100–101,16October2026)

- User599754496/15005730338screenshots confirm49/unit,30cm,copperclaimed,standardATO/ATCfitandfusesexcluded.16AWGspecvs14AWGfeatureconflict; noDCvoltage/currentratingand30Ctemperatureambiguous. Saved3holders147ascandidateinside180setestimate, noqualified30Aclaimorfinalpoweredapproval.
- AddedS44nativeURL,replacedactiveglassholdercandidateforthesamebranches, remainder33unquotednotcompleteprotectionquote. Nextsearch2AATO/ATCstandard32Vfuses6individualpieces, main/logicandadapterfaultcoordinationpending.
- Export/recalculationpass, zeroformulaerrors, unchangedA7746/B8338.40/materials16084.40,5materialquotes+2feesunknown. Native58linksverifiedwithvalues/formulaspreserved, A14renderreviewed. No purchase/physicalworkorphasechange.

### Standardfuselistingwithout2A(Step102,16October2026)

- Revieweduser212420707/6261291722screenshot:Standard/Mini/Micro,3Aminimum,no2A,PHP75unselected. Correctfamilyoptiondoesnotestablishrequestedrating/DCvoltage/timecurve. Do notincreasefuseampstomatchavailability. NoExcelmutationorpurchase/physicalwork.

### Standard2Apackselection(Step103,16October2026)

- Screenshot1218437594/26470926816selected2A+10pcsPHP66qty1. Fullpackpriced,3positions+7spares. No32VDC/timecurve/manufacturerdataestablished; sourceS45andnativeURLrecordedascandidate, actualfitholder/adapterwirecoordinationpending.
- A14holder147+pack66=213replaces180(+33); remainingmain/logic/basketDCprotectionnowA14.1unquotedratherthanhiddenremainder. Avoidduplicateoldglassholderor6loosefusepurchases. Pricedfirstsubset2666beforeadapterandotherpendingitems, notcompleteprototype.
- Exportrecalculationpasszeroformulaerrors,A7779/B8338.40/materials16117.40/withoutfryer14923.40,completeQuoteNeededfor6materialentries+2fees. Native59linksverifiedwithvalues/formulasretained, shiftedrowsandA14renderreviewed. No purchase/physicalworkorphasechange.

### Consolidatedprototypeorder(Step104,16October2026)

- Userrequestslistagain. Rewrotedocs/PROTOTYPE_FIRST_ORDER.mdclearlywith15selectedpartsrows,sum2876,physicalstoreadapter/red3mblack3m18AWG/DCconnector, remainingprotectionandmechanicalrequirements/tools, anddeferredpermanent/basketitems. No duplicateA14/A15allowanceor20packs,3initialswitchesfrom7total.
- Currentmotorprice352vouchercaveat,jumper147estimate, actualfuse/holderDCratingsandadaptercoordinationpendingexplicit. Listnotclaimedcompleteworkingfullmachineorready-poweredkit. LinkedcurrentlistfromBOM, PROJECTupdated,noExcelprice/quantitychange orPhase2/physicalwork.


### Phase 2 authorised and received inventory recorded — 28 October 2026

- User explicitly requests prototyping with received materials. Recorded twelve photographs and cautious counts in `docs/INVENTORY.md`; preserved originals and a SHA-256 manifest in `docs/assets/inventory-2026-10-28/`.
- Separately incorporated user confirmation that MOSFET modules are present and already soldered. Intended modules are LR7843, three channels; exact delivered count/labels and solder quality remain to inspect. They are not missing purchases.
- Received evidence includes one Mega, one LCD front, three red buttons, three JGB37-520 motors with visible DC12V22RPM labels, diode and microswitch bags, inline holders, blade fuses, both electrolytic capacitor bags, a DC connector and a black cable. Bag counts, fuse ratings, cable ends and LCD backpack remain unverified. Receipt does not imply a test pass.
- Created beginner prototype, wiring and testing documents. T01 is one disconnected pushbutton continuity check with probe verification and released / held / released readings. Await user result before any further physical step.
- Updated PROJECT and BOM receipt status; shopping list is now a historical reference to check against inventory. No workbook prices/quantities changed and no new purchase instructed.
- No package installation, sudo, serial permission change, compilation, flashing, external power/motor test, mains work or Phase 3 transition performed.


### Phase 2 Step 2 — buttons passed; additional equipment confirmed, 28 October 2026

- User reports all buttons checked and all expected outcomes obtained. Recorded PASS for all three red buttons: open at rest, connected while held, open on release. No numeric contact resistance supplied; no extrapolation to other components.
- Added user-confirmed breadboard, jumper wires and soldering equipment to inventory and PROJECT; removed breadboard/jumpers from unconfirmed ownership list. Sizes/counts/types remain unitemised. No BOM price or workbook change.
- Issued one disconnected microswitch terminal/contact check, with actual COM/NC/NO identification, definitions, meter-only pin table, expected two sequences and stop-for-result checkpoint. No physical pin order guessed. If markings unreadable, obtain a photo before wiring/probing assigned terminals.
- No powered circuit, installation, sudo, flashing, mains or soldering work performed. Wait for first microswitch result.


### Phase 2 Step 3 — microswitch batch passed; bare Mega USB checkpoint, 28 October 2026

- User reports all switches working as intended following the issued COM–NC and COM–NO procedure. Recorded batch PASS; no invented count or numeric contact resistance. Buttons and received microswitch contact checks now complete by user report.
- Read-only PATH/group/port checks were announced before running. No command paths returned for arduino-cli, pio or platformio; not an exhaustive installation inventory. Current hans process includes dialout. No matching ttyACM/ttyUSB/by-id nodes before the connection checkpoint; missing-glob listing exit status is not a board failure.
- Prepared and issued bare Mega inspection and USB-only power observation with no external modules, header wires or barrel supply. Explain data cable vs power-only and that existing L LED behaviour does not establish known firmware. Wait for user result before any further physical step.
- Arduino official detection and Linux permission references consulted. No arbitrary clone driver choice, sudo/group change, installation, compilation, flashing or motor/mains power operation performed.


### Phase 2 Step 4 — Mega USB detected; diagnostic prepared, 28 October 2026

- User reports ON LED lit and L blinking. Recorded power observation, not a known-program pass or full-board qualification.
- Read-only /dev and sysfs checks find newly present /dev/ttyUSB0, USB 1a86:7523/product USB Serial, driver ch341-uart. Port readable and writable. No serial port opened, no new driver installed, no group change needed.
- Verified official CLI release 1.5.1 with published Linux x86_64 archive checksum; official package index and matching AVR core 1.8.8 board/Mega pin definitions verified. Prepared source target arduino:avr:mega:cpu=atmega2560, onboard LED13 and Serial115200, no third-party libraries.
- Saved complete commented firmware/mega_diagnostic sketch, project-local setup/environment/config/checksum and compile/list/upload/monitor scripts in tools/, plus beginner setup and expected-result guide docs/ARDUINO_SETUP.md. Diagnostic: two short LED flashes per two-second frame, periodic heartbeat, ?/ACK serial receive check.
- Exact commands prepared for review. Installation and flashing explicitly require user permission per AGENTS.md. No setup script, Arduino build/upload/monitor, system package, sudo, outside-project write or powered actuator work run. Shell syntax validation only; target compilation and physical diagnostic result remain pending.


### Phase 2 Step 4 execution authorised — 28 October 2026

- User replied “proceed” to the concrete request to install project-local Arduino tools, compile/upload the bare-board diagnostic and check serial output. This authorises those steps without a second permission request.
- Exact commands remain in docs/ARDUINO_SETUP.md. Keep USB-only/bare board; no actuator wiring or mains work. Installation, build and upload results will be recorded after execution.


### Phase 2 Step 4 diagnostic executed successfully — 28 October 2026

- Executed user-approved project-local setup. CLI 1.5.1 archive SHA-256 matched published checksum. Arduino AVR Boards 1.8.8 installed with its managed tools. No sudo, Linux group change, system package or extra USB driver required.
- Compiled arduino:avr:mega:cpu=atmega2560 successfully: 3334 bytes flash / 253952 available, 196 bytes RAM / 8192 available. Four unused-parameter warnings are in Arduino core new.cpp, none in the diagnostic source; no vendor-core edits made.
- Verified port still /dev/ttyUSB0 USB 1a86:7523 with read/write access. CLI board list labels clone interface Unknown; actual Mega target explicitly selected. Approved upload with --verify exited 0, then running diagnostic boot tag captured.
- CLI serial monitor at 115200 captured 27 consecutive heartbeat messages with 1000 ms increments and expected ?/ACK response. A few unreadable bytes preceded clean startup text; subsequent diagnostic lines readable. Ctrl+C closed monitor with exit 0. Board left running diagnostic.
- Evidence logs and JSON results in .build/logs/. Updated setup/build/wiring/inventory/test/project records. **Await user observation of two short L flashes and a pause before any next physical wiring step.** No motor, driver, LCD, mains or heater test issued/performed.


### Phase 2 Step 5 — user confirms Mega diagnostic; LCD inspection requested, 28 October 2026

- User confirms the diagnostic LED pattern works as intended. T04 now passes with user observation plus tool-observed compile/upload/bidirectional serial evidence. Marked the Mega diagnostic success checklist item complete, not the full prototype.
- Updated inventory, PROJECT, setup guide, wiring/build/test records and BOM phase status. No part quantities or budget prices changed; no new upload/install performed this turn.
- Next one physical checkpoint: unplug Mega USB and inspect the unpowered LCD rear. Request a clear photo showing any I2C backpack, actual connector labels/order, chip marking and solder attachment before issuing LCD wiring. No assumed PCF8574 type, address, pin order or voltage from the front photograph.
- No LCD power, new wiring, soldering or firmware upload issued. Await photo; no Phase 3 transition.


### Phase 2 Step 6 — LCD rear photo and unpowered wiring, 28 October 2026

- User supplied rear LCD photo. Saved original as docs/assets/inventory-2026-10-28/13-lcd-backpack.png, appended checksum/observation to manifest. Attached board marked HW-61, header GND/VCC/SDA/SCL top-to-bottom in this view and blue trimmer visible. Exact IC marking not reliably legible; do not invent PCF8574 variant, address, manufacturer rating or test pass.
- Official Arduino Mega pinout verified SDA20/SCL21. Issued complete four-wire table/ASCII diagram and beginner male-to-female jumper instructions in WIRING/BUILD_PROTOTYPE. Planned 5 V LCD rail from Mega5V; this step remains unpowered, not independent qualification of generic module voltage.
- Await a photo of four wires at both ends, USB unplugged and all other supplies/modules disconnected. No powered LCD action, new upload, library installation, soldering or contrast adjustment performed/issued. No second backpack purchase. No BOM price or quantity change.


### Phase 2 Step 7 — user reports LCD wired; first power observation issued, 28 October 2026

- User says “done, wires connected, proceed.” Recorded completion by user report; no wired photo received or independent visual check claimed. Do not repeatedly demand a photo as a blocker for this low-voltage step; require a final actual-label check before USB power, and leave off if uncertain.
- Issued one next physical checkpoint: verify LCD GND/VCC/SDA/SCL to Mega GND/5V/20/21 while unpowered, reconnect USB only, report backlight/appearance. Existing diagnostic does not initialise display text. No contrast/backlight-jumper change, motor power or additional supply instructed.
- Prepared complete commented firmware/lcd_i2c_scan/lcd_i2c_scan.ino using installed Wire APIs checked in AVR1.8.8 source; uses the documented SDA20/SCL21 pins, 100kHz, 25ms timeout and explicit scan errors. Compile-only passed; log .build/logs/lcd-i2c-scan-compile.log. No package/library installation and no scanner upload or I2C result claimed.
- Await user physical power observation before the next firmware/address test; later uploads follow existing project authorisation requirements. No Phase 3 transition.


### Phase 2 Step 8 started — 28 October 2026

- User reports LCD working as intended after the USB-only power check and says proceed. Record the reported power/appearance check as passed, not known displayed text. Their instruction advances to the already prepared address scanner discussed in Step 7.
- Run the prepared scanner upload and serial capture using existing tools; no extra package/library install, motor operation or wiring change. Current port rechecked against USB1a86:7523 with read/write access.


### Phase 2 Step 8 — LCD responds at 0x27; concrete text test prepared, 28 October 2026

- User reports LCD working as intended after the issued USB power check and asks to proceed to the already prepared address scanner. Power/backlight check passes by user report; no known text pass inferred from that message.
- Rechecked /dev/ttyUSB0 USB1a86:7523 with read/write access. Scanner upload --verify exited0. At115200 baud both startup and commanded r scans reported FOUND0x27 / SCAN_COMPLETE devices=1, no scanner timeout/transaction errors. Monitor closed Ctrl+C exit0. Startup transient unreadable bytes followed by clean tagged text retained in log.
- Saved scan evidence/result JSON in .build/logs/, measured address0x27 assigned to next source/config/wiring records. No actuator, extra supply or wire change.
- Researched maintainer hd44780 library primary documentation and official local Arduino index: Bill Perry1.3.2, no extra library dependencies; I2Cexp supports autoconfiguration of the internal backpack mapping at a specified measured address. This does not prove exact generic backpack IC.
- Prepared complete firmware/lcd_text_test and docs/LCD_TEST.md with exact new-library install/build/upload commands, expected title/advancingseconds and error handling. **Library not installed, new sketch not target-compiled/uploaded. Request permission for this newly proposed installation/upload per AGENTS.md; do not repeat permission for the scanner already authorised/executed.** Await user approval, then user-visible text confirmation after execution. No Phase3 transition.


### Phase 2 Step 9 execution approved — 28 October 2026

- User replies proceed to the concrete hd44780 1.3.2 project-local installation, compile/upload and serial-check request. Execute prepared commands in docs/LCD_TEST.md, using unchanged USB-only Mega/LCD wiring. No second permission request required for these authorised steps.
- Await actual command results and user-readable title/seconds observation before advancing. No motors/heater or additional wiring authorised by this checkpoint.


### Phase 2 Step 9 — LCD text program executed; visible result pending, 28 October 2026

- Executed explicitly approved project-local hd44780@1.3.2 install; no sudo/system package/extra driver. Same measured0x27 address and SDA20/SCL21, 5V/GND wiring. No hardware changes.
- Mega compile passed: 10574 bytes program/253952 available;511 RAM/8192. Four unused-parameter warnings in supplied Arduino core new.cpp, no diagnostic or LCD-library warnings. No code changes needed after target compilation.
- Rechecked intended /dev/ttyUSB0 identity/read/write access. CLI board list still generic Unknown; explicit Mega target used. Upload --verify exited0.
- Captured LCD_TEXT_TEST_V1 READY and 27 increasing seconds values1–27 at115200 baud, no reported LCD error. Initial partial/duplicate boot line on monitor opening then stable captured updates; do not claim no startup reset. Monitor closed Ctrl+C exit0; LCD text program remains running.
- Logs/results in .build/logs/lcd-text-* including result JSON with source hash. Updated all current phase/wiring/inventory/setup/test notes. **Await user confirmation of readable FRIES MACHINE first row and advancing Seconds: second row before next physical step.** Do not mark full display visual test or prototype complete yet. No new contrast adjustment/motor/heater operation issued.


### Phase 2 Step 9 troubleshooting — lit LCD with no text, 28 October 2026

- User reports nothing appears. Three photos saved as inventory14–16 with manifest checksums. LCD backlight visibly on, character area blank; Mega header photos provide partial wiring visibility but do not prove end-to-end continuity or voltages. Do not mark LCD visual test passed from earlier serial READY.
- First hypothesis contrast setting, based on lit display and prior address/init results. Issued one gentle rear blue-trimmer check, existing USB-only program, no wire/jumper changes, no new firmware. Reposition unpowered if needed; proper small tool clear of adjacent conductors, no forced end stop. Ask whether letters/filled rectangles/no change appear and wait.
- General Adafruit primary contrast guidance checked; does not establish exact generic HW-61 specifications. Maintainer I2CexpDiag is a possible later check if contrast fails, not run or flashed now. No package install, reflash, resoldering, replacement purchase or actuator operation.


### Phase2 Step10 — LCD contrast fix verified; three-button wiring issued, 28 October2026

- User confirms LCD now working and supplies photo17, saved with manifest checksum. FRIES MACHINE / Seconds:23 readable. Previous serial updates plus user confirmation support counter operation; photo alone is a single instant. Marked T09/T09a passed after contrast adjustment, no code/replacement/wire change reported. No further LCD diagnostics warranted.
- Kept LCD address0x27, SDA20/SCL21, 5V/GND and installed hd447801.3.2 unchanged. No new firmware flash/install this turn.
- Issued next low-voltage physical checkpoint: unplug USB, connect three previously continuity-tested buttons to digital22/23/24 and unused GND sockets. All button terminals are isolated non-polarised contact pairs; future test uses INPUT_PULLUP, not external5V button wiring. Documented six-endpoint table/ASCII diagram, individual ground sockets and secure lead guidance. Do not assume panel lugs accept DuPont sockets; if they do not fit, get terminal details before soldering/improvising.
- Await user wiring report with USB still unplugged. Current LCD-only sketch does not read buttons; complete matching input diagnostic/upload comes after wiring confirmation. No motor/index/basket power or Phase3 transition.


### Step10 button connector retention advice — 28 October2026

- User asks how fitting jumper wires can be secured. Reviewed earlier bag photo; exact terminal size/type still insufficient for a specific spade recommendation.
- Recommended temporary individual electrical tape plus wire anchoring for already snug low-current contacts. Tape cannot repair intermittent/loose metal contact. One unpowered connector trial/gentle pull/free-button-action result requested if tape available, before repetition.
- Durable alternative: suitable solder-terminal pigtails with each joint insulated by heat-shrink, Mega end removable. No solder/cut step issued. Matched crimp terminals require actual terminal identification/measurement. No new purchase, price/quantity change, upload or power-on operation.
- Updated build/wiring/test records; secure button input wiring still awaits user completion. LCD remains passed.


### Phase2 Step11 started — 28 October2026

- User reports all buttons connected after retention guidance and says proceed. This advances to the discussed input/LCD test on22/23/24 without new libraries or repeated setup approval. User completion is not independent electrical verification.
- Prepared complete commented flavor_buttons_test and debounce helper, matching WIRING.md; no actuator pin output configured. Host debounce/hold/startup/rollover checks passed and AVR compilation passed. Exact commands and operator checks in docs/BUTTON_TEST.md.
- /dev/ttyUSB0 present, USB1a86:7523 read/write; next run verified diagnostic upload then idle serial check before asking for manual button mapping/hold results. No motor/heater test.


### Phase2 Step11 — button/LCD tester running; manual tests pending, 28 October2026

- User says all buttons connected and proceed after retention advice. Connection/securement reported; exact retention method and independent full endpoint photo not supplied. This advances to discussed input diagnostic with existing libraries, no repeated install/setup request.
- Saved complete commented firmware/flavor_buttons_test and ButtonInput.h with pin22/23/24 INPUT_PULLUP,35ms stable contact timing, one event per held press, release rearming and held-at-boot suppression. LCD0x27/SDA20/SCL21 unchanged. No driver/motor/heater output configured; not final busy/cooking logic.
- Host tests on the same helper passed contact bounce, stable interval, hold/no repeat, release/repress, held-at-boot and uint32 rollover. AVR compile passed11692 flash/584 RAM bytes; four supplied Arduino-core unused-parameter warnings, no test/helper warnings. No code changes after successful build.
- Rechecked /dev/ttyUSB0 USB1a86:7523/read/write. Verified upload exit0. Serial READY and14 idle samples raw111/counts0,0,0/lcdOK; no held-at-boot/LCD error/physical press during capture. Startup unreadable bytes precede clean tag. Monitor closed Ctrl+C exit0. Program left running.
- Saved docs/BUTTON_TEST.md exact commands and operator expectations, test/compile/port/upload/serial logs and result JSON in .build/logs/. Await user mapping/count/hold result before any next physical step. No new libraries, wiring, motor power or Phase3 transition.


### Phase2 Step12 — button connection corrected by user; module identification issued, 28 October2026

- User initially questioned the double-row header positions, then reports: “nevermind, fixed it myself, all buttons working as intended, proceed.” Record the three-button input test as passed by user report after a self-corrected connection. Exact changed sockets, individual count values and a separately itemised physical held-button result were not supplied; do not invent them. Recheck held-input behaviour during later integration.
- Preserved pre-correction header photo18 with checksum; wire bodies obscure exact endpoints, so no specific miswired socket or correction was inferred. Clarified physical paired header numbering in WIRING.md from the official Mega pinout. No pin/code changes.
- Issued one unpowered driver-identification checkpoint: USB/all supplies off, one loose module, label-side and solder-side photographs. Module terminals/GPIO and motor-power diagram remain unassigned pending actual board review. No install, flash, motor power or Phase3 transition.


### Phase2 Step12 — module photos received, 28 October2026

- Saved original front/back photos19–20 with manifest hashes. Readable rear PWM/GND and +/LOAD/− positions documented. Exact MOSFET/optocoupler marks unreadable; only one pictured, no assumed total. No obvious adjacent-terminal bridge seen; solder integrity/continuity untested.
- Checked matching ProtoSupplies supplier module description via web search (direct page403); terminal roles align, but do not transfer ratings/isolation guarantees to this board. No verified motor flyback diode path from component appearance.
- Issued disconnected +/− resistance check with safe meter jacks/mode and requested settled reading/unit orOL; motor-adapter availability/label still unanswered. No motor wiring/GPIO, flash/install or powered test. Wait for user result.


### Phase2 Step13 — MOSFET test report accepted; adapter absent, 28 October2026

- User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned.
- Advanced to one unpowered roller-switch input connection: COM→GND, NO→reservedD26, NC empty. Updated wiring/build/testing/inventory and adapter receipt status; no full input firmware claimed, no upload or powered actuator work. Wait for physical wiring report.


### Phase2 Step14 — one switch connected; matching diagnostic compiled, 28 October2026

- User “connected” accepted as Step13 wiring report. No direct endpoint verification or index input pass inferred.
- Prepared complete inputs_index_test (22/23/24/26, LCD0x27), independent counts,35ms debounce, startup-held protection, READY/ACTIVE index display, retained flavor-button display, LCD timeout/error logging and actual-input serial status. No actuator outputs.
- Compiled Mega11922 flash/599RAM; four core new.cpp warnings only. Identical helper passes existing timing tests with new header pre-included. Compile/host/result logs saved; exact source hashes recorded. No flash/install/system modification or port-monitor opening performed.
- Request USB-only reconnect and approval of the documented upload per AGENTS.md:30, then run within approval without repeat prompt. Old button-only program remains on board. Manual index test follows successful upload/idle.


### Phase2 Step14 — approved index upload/idle passed, 28 October2026

- User approved the prepared upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; source hashes matched compiled source. CLI upload --verify exited0. Serial INPUTS_INDEX_V1 READY plus 16 released-idle samples raw1111/counts0,0,0,0/lcdOK; no LCD error, held-at-boot tag or physical input press during capture. Unreadable startup bytes preceded clean tagged output. Monitor closed Ctrl+C exit0; inputs_index_test now runs on the board. No package install or wiring change. Physical lever test remains pending.
- Ask actual lever hold/release/repress result and visible LCD state; stable idle does not prove contact closure. Keep current firmware/wires. No further actuator or Phase3 step until physical result.


### Phase2 Step15 — physical index1 pass reported, 28 October2026

- User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test.
- Issued empty unpowered breadboard rail continuity check for four future signal-GND holes, before moving any successful wiring or adding switch inputs. Each chosen hole must connect to first; no split-rail assumption. No code/flash/new pins or motor power. Wait for result.


### Phase2 Step16 — existing common ground retained, 28 October2026

- User states an existing common breadboard GND line is already made for everything and supplies photo21. Accept the existing signal-ground arrangement as user-reported; retain it instead of building a second rail or repeating the empty-rail procedure. Photo shows multiple jumpers near the blue marking but does not prove every endpoint or split-rail continuity. Earlier working LCD/buttons/index1 support those tested signal paths, not every unused rail hole. No numeric continuity reading or new meter pass is inferred.
- Saved original photo21 with hash. Step15 proposed new empty rail superseded; do not require duplicate construction. Issued unpowered switch2/3 COM to existing connectedGND, NO28/30, NCempty; index1 remains26. Current firmware does not yet read28/30. Wait for wiring completion; no flash/install/motor power.


### Phase2 Step17 — six-input diagnostic prepared, 28 October2026

- User reports switch2/3 connections complete. Prepared separate complete inputs_three_index_test retaining original uploaded source. Six INPUT_PULLUP contacts,35ms stable debounce, held-at-boot protection, per-input count and correct index1/2/3 display on each press/release. No actuator outputs.
- Mega compile passed12054flash/619RAM, four Arduino-core unused-parameter warnings only. Byte-identical helper tested using existing tests with the new header pre-included; passed. No new installation or flash/port opening.
- Saved exact upload/test guide, compile/host logs and result hashes. Ask USB-only reconnect and concrete-upload approval before executing; current single-index program unchanged.


### Phase2 Step17 — approved three-index upload and idle passed, 28 October2026

- User approved the prepared three-index diagnostic upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523, read/write access and unchanged source hashes. CLI upload --verify exited0. Serial INPUTS_3INDEX_V1 READY and15 released-idle samples raw111111/counts0,0,0,0,0,0/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical press during capture. Startup unreadable bytes preceded clean tags. Monitor closed Ctrl+C exit0; inputs_three_index_test now runs. No new library, wiring change or actuator output. Physical three-index mapping/hold/release and button regression remain pending.
- Next ask actual individual lever index/state/count and three-button regression results. Stable idle alone does not prove signal closure or correct assignment. No new wiring or Phase3 advancement.


### Phase2 Step18 — all three connected index switches pass, 28 October2026

- User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing.
- Requested availability of four further roller switches for provisional basket endpoint bench inputs. No planned-vs-delivered count assumption, new pins, device operation or duplicate purchase. Existing hardware/firmware preserved; wait for response.


### Phase2 Step19 — output-free cycle logic prepared, 28 October2026

- User confirms3switchesonly;4remaining ofexisting7plan and12Vadapter notowned. Updated ownership/missingitems without duplicate charge or newprice.
- Prepared standalone CycleLogic.h, full Mega/LCD wrapper and identical tested contact filter; no actuator output interfaces. Scope is manual index response plusshorttimer/busy/fault simulation; basket stageexplicitlypending.
- Added host tests before core implementation; initialcompilefailedmissingheader, thenallpassed with implementation. Mega13360flash/797RAM, fourcorewarningsonly. Scope-only simplification checks returned nochanges. Dedicatedcecodereviewscopingfailednogitbase; manualfile/outputscan recorded instead. Userfile-deliverable workflow retained; noGitinit/commit/publish.
- Newfirmware notuploaded; exactcommands/firstoperatorcheckpoint saved. Ask approval only forconcreteflash underAGENTS30, thenhonourwithoutrepeat. Fullprototypeincomplete/noPhase3.


### Phase2 Step19 — simulation verified-upload and idle passed, 28 October2026

- User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed.
- Actual manual selection/index/timer sequence remains pending; issue only firstcheckpoint and wait. No poweredactuator or prototype-complete claim. New files/tests/sourcehashes unchanged since successful build; no repeatcode-review/compile needed for this upload.


### Phase2 Step20 — manual happy-path simulation passed, 28 October2026

- User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement.
- Issued onebusy-button physicalcheckpoint usingflavor1/index1 thenbuttons2/3duringSIMCOOK andextraafterDONE. No newcode/flash/install/serialmonitor orwirechanges. Waitforresult;hostpassdoesnotreplaceuserobservation.


### Phase2 Step21 — busy lockout physical result accepted, 28 October2026

- User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred.
- Issued wrong-index checkpoint using flavor3: wrong index1/2 ignored; matching index3 advances within same15s window. No device commands, code or wiring changes; await physical report.


### Phase2 Step22 — physical wrong-index rejection passed, 28 October2026

- User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test.
- Issued missing-index timeout/fault-latch/reset checkpoint. No device commands, source changes, uploads or wiring. Wait for actual result.


### Phase2 Step23 — physical timeout/reset recovery passed, 28 October2026

- User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop.
- Issued initially-held selected-index checkpoint, requiring release then fresh actuation inside same15s window. No source/device/wiring operation; wait for user result.


### Phase2 Step24 — held selected-index qualification passed, 28 October2026

- User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred.
- Issued final current USBlogic check for flavor3 held through reset: idleuntilreleaseandfreshpress. Existing output-free simulation untouched; no device commands or wireschanged. Awaituserresult, thenrecordlimitedUSBlogicmilestonewithoutclaimingfullprototypecomplete.


### Phase2 Step24 completed — USB-only logic milestone, 28 October2026

- User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied.
- Planned USBinput/display/software sequence/lockout/fault/held-input checks now passed. Saved concise checkpoint; keep current wiring/firmware, no repeated tests. No device operations or source changes.
- Outstanding adapter+4basket switches and power/mechanical qualification prevent fullprototype completion. Next checkpoint is adapter label/plug review when part arrives; no motor power or Phase3 issued.


## Save and handoff — 5 November 2026

**5 November 2026 update:** user now owns one 12 V adapter and reports measuring **12 V DC**. Exact model, label current/power rating, enclosure type, connector size/polarity, load during measurement and loaded regulation/protection are not supplied. Planned A17 is enclosed regulated 12 V / 5 A / 60 W, but those ratings are not established by the voltage reading. Do not rebuy it automatically. No motor connection/test is reported.

Prepared a project-local persistent handoff and README entry, corrected active inventory/BOM/shopping/resume state, retained dated records as history, and copied original small bench evidence from ignored `.build/logs` to `docs/evidence/2026-10-28`. Toolchain/downloads/build binaries and generated scratch renders are excluded from Git. Source firmware is unchanged. Pre-commit validation passed: uploaded simulation source matches all3original hashes, all40BOM rows remain covered, README links resolve, and archived logs are byte-identical. Sources/docs/assets/evidence are being saved onmain, preserving original README history. Final push success must be verified against remoteHEAD; no new hardware test or setup performed.


### Git publication verified — 5 November 2026

Checkpoint commit `18ebf34f3c15451fd46daa7cf6be663c035dcd86` (`docs: preserve prototype progress and adapter assembly handoff`) was pushed to `main`. `git ls-remote origin refs/heads/main` matched that full hash and the working tree was clean. HTTPS push initially lacked credentials; existing SSH authentication as hanssantos02 succeeded, so the same repository uses HTTPS fetch and SSH push locally. No credentials installed, no force push, no PR, no hardware operation. Original root commit2e5c478 is retained.

This publication note is a small follow-up documentation commit; the subsequent final HEAD and remote equality can be checked with Git. Persistent resume file: `docs/handoffs/2026-11-05-assembly-resume.md`, also linked from README. It captures passed USB tests, exact pins/current firmware, latest adapter receipt, current purchasing decisions, and Step26 label/polarity/current-rating checkpoint. Local tool/build caches are intentionally ignored; portable original evidence is committed under `docs/evidence`.
