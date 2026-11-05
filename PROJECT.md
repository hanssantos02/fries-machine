# PROJECT.md: Automatic Fries Machine

Updated: 5 November 2026, Asia/Manila. Current phase: **Phase 2, Step 26 pending — adapter received/reported 12 V; label/polarity review before powered assembly**. The user explicitly asked to start prototyping with received materials. Outstanding selections remain conditional; this does not authorise Phase 3 or unverified powered tests.

## Basics
- **Project name:** Automatic Fries Machine.
- **What it should do:** Keep the physical PDF design unchanged. Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence.
- **Required user features:** Approx. 300 g fries, manual cutting, three flavor/start buttons, timer-based warm-up then cooking, powered basket lift/drain/flip and complete protected fryer. Initial proposed durations 5 minutes warm-up + 10 minutes cooking. No potato-start detector or external automatic oil-temperature gate; keep position feedback and independent protection. Keep one 16x2 I2C LCD for countdowns, flavor and status.
- **Nice-to-have features:** None confirmed. Wi-Fi, payment collection, automatic bag feeding and powder dosing are outside the stated scope.

## Usage
- **Where and how it will be used:** User confirms initial assembly/testing at home (16 October 2026, Step 78). Proposed indoor, stationary, supervised demonstration. Final demonstration site and whether food will be served to customers remain unconfirmed. Home outlet protection, earthing, circuit capacity and supply topology have not been verified; do not assume school facilities or existing leakage protection.
- **Power source:** Proposed Philippine 220-230 V AC wall supply for a complete electric deep fryer and isolated low-voltage supplies; qualified electrician to handle mains installation.
- **Connectivity needed:** None requested. Operate locally.

## Budget and constraints
- **Budget limit (PHP):** No fixed ceiling; economical thesis procurement. Retained user-requested I2C LCD, now selected ALLAN listing at PHP 120; current priced-material subtotal PHP 16,117.40 including the selected Shopee Single-6L fryer at screenshot-listed PHP 1,194, before outstanding electrical/fee quotes. No complete quotation yet.
- **Team scope:** Electronics only. Include a complete protected electric fryer allowance at the user's request; assign its purchasing owner with the mechanical team to avoid double buying.
- **Assembly preference:** User explicitly will assemble B06–B09 as well as the electronics, with guidance. No external assembly-labor fee is imposed. Plan guided low-voltage dry tests and qualified school/electrician supervision/review of mains installation before energizing. Only any actual paid review/inspection/help remains a separate fee; availability/cost is unknown.
- **Mechanical reference:** `drawing-fries (1).pdf`, ten pages showing frame, fryer/basket, manual cutter, three spiral dispensers, chain/sprockets, funnel and basket-related bracket.
- **Size / weight limits:** Drawing dimensions are references, not a confirmed manufactured assembly. Empty basket mass, retained-oil allowance, pivot geometry, actual travel and torque requirements are missing.
- **Deadline:** Not provided.

- **Confirmed design constraint:** The physical design in the PDF must remain unchanged; resolve the existing basket movement/transfer mechanism with the mechanical team.

## Platform
- **Preferred controller:** Full-size Mega 2560 R3 compatible board, 5 V logic. User screenshot confirms [Shopee SAMIORE.ph/SAMIROB](https://shopee.ph/product/580325202/15523024357) option **2560 R3 With Cable at PHP 699**, before shipping. A01 now uses this price, replacing PHP 1,030 reference. Pictured assembled headers and USB A-to-B cable; actual USB-serial chip and operation to verify on delivery. Compact PRO alternatives are not additional purchases. The Mega has now been received (28 October photo). User reports ON lit and L blinking on USB. Host detects /dev/ttyUSB0, VID:PID 1a86:7523, driver ch341-uart, with read/write access; approved known diagnostic upload and 115200-baud heartbeat/ACK now passed. CLI 1.5.1 and AVR Boards 1.8.8 installed project-locally; user confirms the new two-flash L pattern. Mega diagnostic passed.
- **Preferred language / framework:** Arduino C++ using Arduino CLI is planned for the authorised Phase 2 work. Complete diagnostic source and project-local setup scripts are prepared for CLI 1.5.1 / AVR Boards 1.8.8, hd447801.3.2 now installed project-locally for the LCD. User approved setup/upload with “proceed.” Setup, compile (3334 bytes flash / 196 bytes RAM), upload with verification and serial heartbeat/ACK succeeded. Exact commands/results in docs/ARDUINO_SETUP.md; future installations/flashes still follow AGENTS.md authorisation rules.
- **Motion architecture:** Budget two basket axes (lift and rotation) and three independently indexed flavor-coil motors. Any extra horizontal transfer axis remains unconfirmed and outside the current price total.
- **Withdrawn motion alternative:** User rejects changes to the PDF design. Do not relocate the funnel, shorten the frame or adopt the proposed custom cam/linkage. Its lower-cost partial estimate does not apply to the retained design. Stepper and geared DC basket motors remain candidates; motor count/type depends on the existing mechanism and measured loads.
- **Basket driver candidate:** A04 user-supplied [Shopee fulabs.ph IBT-2/BTS7960-type module](https://shopee.ph/product/1367148707/26183927355), PHP 275 each, quantity two provisionally for lift/tilt. One board drives one brushed-DC motor in both directions. Match to actual motor current/voltage and module cooling before buying; advertised 43 A is not a verified continuous board rating. If basket steppers are selected, replace with matching stepper drivers rather than buying both alternatives.
- **Flavor driver (A06):** User selects [fulabs.ph LR7843](https://shopee.ph/product/1367148707/41455009761) at **PHP 50 each × three = PHP 150**. Seller description documents 3 V/5 V input, HIGH=ON, LOW=OFF and PWM for DC devices. Suitable control architecture; actual input current/reset OFF, motor running/stall/thermal match and circuit protection still need validation. A06 is module-only; A06.1 separately quotes three suitable motor flyback diodes if the module lacks a verified path. Former PHP 160/channel complete-set allowance removed; no duplicate discrete MOSFET/gate parts. User confirms the MOSFET modules are received and already soldered (28 October 2026). One module front/back photographed: PWM/GND and +/LOAD/− labels readable; exact chip markings and total count unconfirmed. User now reports all modules already checked and working; method/readings unprovided. Adapter now owned with user-reported12V measurement on5November; label/current rating/polarity and loaded channel, safe-OFF/protection checks remain later.
- **Position switches (A07):** [SHOPOMATIC.ph SHOPO roller microswitch](https://shopee.ph/product/447511770/11436017124), screenshot PHP 22 **per piece**, quantity seven = PHP 154: four provisional basket endpoints plus three coil indexes. Confirm actual COM/NO/NC markings, low-current reliability, switch dimensions/travel and dry/cool mounting. Signal inputs only; not certified safety-stop or motor/heater power contacts. Final quantity depends on existing mechanism.
- **Heating architecture:** Manufactured fryer with its own thermostat and verified independent overheat protection. Proposed K1 normal fryer contactor and K0 independent hardwired heater/motor-power stop, low-voltage coil/control interfaces and manual restart. User assembles with qualified review before energizing; protection must function without firmware. Ordinary contactors alone do not certify safety performance.
- **Updated heater-control scope:** Button-operated heater permission remains. Controller advances through timed warm-up/cooking stages without measuring oil temperature. Retain fryer thermostat and verified independent cutoff. Five-minute warm-up is an initial adjustable proposal pending actual thermal/loading tests.

## Current purchase decisions — 28 October 2026

User chooses one HSK LA38 Emergency Stop (1NO+1NC, screenshotPHP98), not yet received; final safety acceptance remains pending documented opening mechanism/contact duty. Do not buy old STOP supplier additionally. Buzzer/LED kit A10 will be bought at a physical store; itemized list saved in `docs/PHYSICAL_STORE_LIST.md`, existing parts reused. No powered test or phase transition.

## Current assembly resume — 5 November 2026

**5 November 2026 update:** user now owns one 12 V adapter and reports measuring **12 V DC**. Exact model, label current/power rating, enclosure type, connector size/polarity, load during measurement and loaded regulation/protection are not supplied. Planned A17 is enclosed regulated 12 V / 5 A / 60 W, but those ratings are not established by the voltage reading. Do not rebuy it automatically. No motor connection/test is reported.

User requests continuation in a new chat and commit/push to `main` at `https://github.com/hanssantos02/fries-machine.git`. Persistent handoff: `docs/handoffs/2026-11-05-assembly-resume.md`. Keep the passed simulation/wiring; physical motor/basket/fryer prototype and Phase3 remain incomplete. No device operation requested in this save/handoff turn.

## What I already have
- **Step25 ownership update:** ceramic capacitors and 18 AWG black wire are present, per user. Capacitor value/voltage/count and wire length remain unreported; do not automatically rebuy them. Full procurement audit: `docs/REMAINING_PURCHASES.md`. Red wire, LM2596, STOP and buzzer/LED kit were not reported owned; four additional switches remain without a later receipt report. Adapter receipt now supersedes its October missing status.
- **Tools:** Multimeter(s), testing tools and soldering equipment ready, per user confirmation. Specific soldering equipment not itemised.
- **Parts received, 28 October 2026:** Mega 2560 board, LCD with attached HW-61 I2C-style backpack (rear photo now received), three red buttons, three JGB37-520 motors (visible labels DC 12 V / 22 RPM), diode strip/bag, microswitch bag, inline fuse holders, blade fuse bag, 1000 µF / 25 V and 470 µF / 16 V capacitor bags, one DC connector and one black cable. User separately confirms soldered MOSFET modules, breadboard and jumper wires. All three red buttons and the received microswitch batch passed the user-reported contact-action checks; user confirms exactly three microswitches owned; four additional basket switches remain. See `docs/INVENTORY.md` for evidence, counts and pending identification; receipt is not a test pass.
- **Fryer/heater:** User selects **Single-6L (one tank)** from DALANDAN LIVING PH [Shopee listing](https://shopee.ph/product/1303238794/40333822650), replacing Hanabishi. New screenshot visibly selects Single-6L at PHP 1,194; delivery extra. Seller advertises 2500 W, 60-200°C dial control and W285 × D435 × H300 mm outer size. Exact manufacturer model/voltage/nameplate, independent overheat cutoff, grounding, basket/heater clearance and allowed external switching remain unverified. B01 now budgets this unit once. Former Hanabishi 2400 W specification is superseded. See `docs/FRYER_ASSESSMENT.md`.

## Confirmed operating requirements and engineering qualifications
- 300 g means food weight, not the full moving basket assembly weight.
- Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence. Ignore repeated/held selection presses while busy; proposed button behavior remains one packet/cycle per selection.
- Ten minutes is the requested initial setting. It is not a universal cooking-time standard; actual cut size, oil temperature and batch conditions must be tested.
- Basket must drain over the oil tank before discharge. It needs a supported path from the fryer to the funnel and load restraint when power is removed.
- A rotating coil is a vending spiral, not necessarily an elastic spring to press. One-packet release depends on its mechanical pitch, packet dimensions and indexing geometry as well as motor control.

- Five minutes is a trial setting, not proof that cold oil is ready. Validate warm-up/cooking durations for the actual oil fill, starting conditions, 300 g batch and loading sequence. If potatoes are in the oil during warm-up, they also heat during that period. Keep the manufactured fryer thermostat and verified independent overheat protection; timers do not regulate oil temperature or replace hardware power switching/stop protection. Retain position switches and motor drivers for basket/coil motion.

- **LCD content:** Selected flavor, warm-up/cooking countdown, lift/drain/flip/return/completion and faults. Use elapsed-time wording for warm-up; no claim of measured oil readiness or temperature.

## Open engineering inputs
**Current A05 motors:** Three ZENG WHCD JGB37-520 motors received; visible labels read DC 12 V / 22 RPM. These supersede the earlier 25GA-370 candidates. The seller-listed rated 5.5 kgf·cm / 18 loaded RPM / 0.30 A and 1.2 A stall are not measured results. Actual coil fit, duty, loaded torque/current, mounting and driver/protection checks remain pending.

1. Mechanical team: measured basket/mounting mass; pivot-to-centre-of-mass distance; sprocket pitch radius; lift travel/speed; drain and dump angles; demonstrated basket-to-funnel trajectory; brakes/retention and guards.
2. Dispenser: packet dimensions/thickness, loaded-coil turning torque, coil pitch and end-of-revolution cam/switch arrangement.
3. Fryer: accepted model/manual, nameplate, independent overheat protection, oil fill limits, tank/basket fit and permissible external control arrangement.
4. Electrical suppliers: selected motor/driver/supply/coil ratings and itemized installation materials; probe is no longer a compulsory controller part.
5. Phase2 started with received parts on28October2026. Step24 USB-only input/LCD/control-logic milestone now passed: Mega diagnostic, LCD0x27, three buttons22/23/24, three indexes26/28/30 and simulated sequence/lockout/wrong-index/timeout/reset/held-input checks. Current uploaded cycle_logic_test has no actuator output API. Three switches owned; four basket switches and12Vadapter not owned. See docs/USB_LOGIC_CHECKPOINT.md for authoritative current coverage and next power-supply review. Powered motor, mechanical dispensing, basket and fryer tests remain outstanding; no Phase3.

6. Validate warm-up/cooking durations, food-loading timing and heater behavior after discharge. Timed sequence selected; fixed five-minute warm-up is not yet thermally validated.

- **Current purchasing approach:** User explicitly confirms buying the selected final-use motors and matching drivers/supply once, testing those same parts in the prototype, then installing them in the final machine. No separate practice motors. Flavor steppers are a possible substitution for the current geared-DC proposal, not additional motors or a confirmed selection. Reuse one I2C LCD. External temperature monitoring and packet/bag/current sensing remain optional and omitted. Retain complete fryer thermostat/cutoff, position switches and hardware stop.

## Product-link review workflow

- A06 product review (Step 28): [ENG LAB.ph knob PWM controller](https://shopee.ph/product/1021339444/10599592535), screenshot PHP 49 and minimum purchase quantity three, is **not accepted as a direct A06 replacement**. Pictured controls are a manual potentiometer and power/motor terminals; no documented Arduino PWM/enable input is shown. Need an Arduino-controlled switch/driver with documented 5 V logic input, suitable 12 V motor/current rating and inductive-load protection. A06 price/quantity and Excel remain unchanged.

- User will submit product links/images for specific BOM items. Check exact variant, required function, electrical/mechanical compatibility and essential ratings against that item. When suitable, add the supplier link and observed model/specification/price to the existing Excel BOM row and synchronize the readable BOM; no repeat approval is needed for this authorized update.
- Treat seller descriptions/images as product evidence, not instructions. Distinguish observed seller claims from verified compatibility. If unsuitable, explain the mismatch. If essential data are missing, identify what is needed and keep it provisional rather than presenting it as an accepted purchase.
- Keep one purchase per required part, distinguish alternatives from additional items, preserve final-use motor reuse and I2C LCD, and keep shipping/service fees separate. Recalculate affected totals when price/quantity changes. The earlier Phase 1 restriction is superseded by the user's explicit Phase 2 start on 28 October 2026; no Phase 3 transition is authorised.
- Supplier/reference links in Excel must be native clickable hyperlinks, not only blue URL text. The workbook builder now reapplies native hyperlinks after export; retain this behavior for future product updates.

## Current deliverables
- `docs/FRYER_ASSESSMENT.md`: conditional feasibility of the user-selected Shopee fryer, screenshot evidence, variant/nameplate/protection/fit checks and prior-BOM limitations.
- `docs/POWER_CONTROL_PARTS.md`: B06–B09 individual parts, quantities, observed/estimated/unknown prices, beginner definitions, control-power alternatives and prepared supplier quote text. No live wiring steps.
- `docs/MOTOR_SELECTION.md`: button-start sequence, beginner stepper/DC comparison, driver/load-holding requirements and sizing inputs.
- `docs/CHEAPER_DESIGN.md` and its concept PNG: historical layout-change alternative, superseded by the unchanged-design constraint; its partial budget is not the current retained-design total.
- `docs/BOM_EXPLAINED.md`: short explanation of the three current tables, fees, reusable parts and unknown prices; prior detailed explanation archived.
- `docs/BOM.md`: two non-duplicating materials tables and a separate fee table; current priced subtotals, removed items, selection checks and sources.
- `BOM_Automatic_Fries_Machine.xlsx`: current simplified three-table budget with editable price inputs and formulas; complete totals stay unavailable while quotes are missing.
- `docs/archive/BOM_Automatic_Fries_Machine.original.xlsx`: untouched original for comparison.
- `PROGRESS.md`: phase and continuation record.

Phase 2 documents now available: `docs/INVENTORY.md`, `docs/BUILD_PROTOTYPE.md`, `docs/WIRING.md` and `docs/TESTING.md`. All three pushbuttons and the received microswitch batch passed the reported tests; Mega USB power observation and host enumeration also pass; user confirms its uploaded diagnostic's two-flash L pattern; LCD power observation passes by user and address scanner upload/two scans pass with 0x27. LCD visual test now passes after contrast adjustment. The button/LCD diagnostic uses INPUT_PULLUP on22/23/24 and the unchanged LCD map. Software/idle passed; user now reports all buttons working after correcting their pin connections. Current Step12 is unpowered identification of one actual soldered MOSFET module; detailed physical hold observations remain unitemised. Later wiring and complete diagnostic firmware will be added as their hardware checkpoints are reached. Received input contacts, Mega USB power/enumeration and approved diagnostic build/upload/bidirectional serial checks passed. Project-local tools installed; no powered motor/fryer test performed. Read-only checks found no arduino-cli/pio/platformio command on PATH, hans already in dialout, and no matching serial device nodes before the USB checkpoint. After connection /dev/ttyUSB0 appeared with ch341-uart and read/write access. See docs/ARDUINO_SETUP.md for the prepared next steps.

- **Flavor/start buttons (A08):** GarageSale01 GS selected Model C normally-open momentary panel buttons, screenshot PHP 20 each × three = PHP 60. Mounting dimensions/contact operation pending; ordinary controller inputs, separate from the emergency stop.

- **A09 provisional purchase:** User elects LA38 STOP from liuma.ph at screenshot PHP 140 and inspection/testing on arrival. Add supplier link to BOM; price replaces PHP 500 allowance. Latching action, NC configuration, direct-opening documentation and selected control rating remain unresolved; bench tests do not certify safety function. Replacement/contact-block costs if required remain outside this candidate price.

- **A12 jumper supplier:** ENG LAB.ph user listing added. Screenshot-selected male-male 10 cm costs PHP 49; one bundle each M-M/M-F/F-F remains planned, preferably around 20 cm. PHP 49 per bundle × three = PHP 147 is a mixed-variant estimate pending exact prices/pack count. Temporary low-current signals only.

- **A13 logic converter:** User Zantop Fiber LM2596 adjustable module screenshot PHP 35 × one, replacing PHP 45 allowance. Proposed 12 V DC to 5.0 V, below 1 A logic planning load; check output/stability/temperature before connection, not a verified module continuous rating. Keep motor power separate. Controller power routing/USB backfeed prevention remains for Phase 2.

- **A14 protection candidates:** fulabs.ph five 5×20 mm holders screenshot PHP 68 with advertised 22 AWG leads; glass fuse listing PHP 35 with no size/current selected. Both links recorded provisionally, exact DC ratings/branch amperage/time curve unverified. Retain PHP 180 whole-row allowance; not an extra PHP 103 charge and not approval for basket/high-current/heater use. Remaining terminals/reverse-polarity and suitable high-current protection still need itemization.

- **A15 ceramics selected:** user Shopee 100nF/0.1µF 50 V through-hole option at PHP 3 each × ten = PHP 30, 16 October 2026 screenshot. Included inside existing PHP 200 A15 set allowance; remaining PHP 170 is unitemized estimate until other filters are selected. Native supplier link added; no total change.

- **A15 bulk capacitor candidate:** BCD Electronics Shop 20-piece 1000µF 25V pack, advertised 10×20 mm, screenshot PHP 69. Correct nominal value/voltage, but 105°C/low-ESR/ripple/manufacturer data pending; recorded as candidate source only. Whole-pack cost applies if selected; existing PHP 200 A15 allowance unchanged.

- **A15 current bulk decision (supersedes candidate-only status):** User elects one BCD 20-piece 1000µF 25V pack at PHP 69 provisionally. No verified 105°C/ESR/ripple claims; inspection and intended-load assessment remain. A15 PHP 200 now comprises PHP 30 ceramics + PHP 69 bulk pack + PHP 101 remaining estimate. No extra charge or three-pack purchase.

- **A15 current allocation, Step 47:** Add selected 16V 470µF 8×12mm twenty-piece pack at PHP 76 (one pack; one initial logic position). Current A15 PHP 200 = PHP 30 ceramics + PHP 69 bulk pack + PHP 76 logic pack + PHP 25 estimated remaining signal parts. Supersedes earlier PHP 99/PHP 101 allocation; no budget-total change. Electrolytic temperature/ESR/ripple data remain unverified.

- **A18 LCD source update (Step 49):** User ALLAN/allantimer LCD1602+I2C listing screenshot PHP 120, quantity one, replaces earlier Makerlab PHP 150 candidate. Complete display plus adapter advertised; verify inclusion/assembly, supplied ratings/address and actual operation. No second display/backpack. User defers A16 while fryer has not arrived/mechanical team unavailable; motor and dependent A17 supply selections remain pending, continue other Phase 1 items.

- **B02 selected:** [Aliex IC Store Mega terminal shield](https://shopee.ph/product/1391133201/29571601363), screenshot Welded Board PHP 270 × one, replacing PHP 350 perfboard/carrier kit allowance. Seller assembled variant, Mega2560/R3 compatibility advertised; actual fit/mapping/power routing pending checks. No duplicate whole perfboard/header set or extra Arduino.

- **B04 fixed signal wire (Step 53):** User buys at physical store by metre. Enter initial 22 AWG stranded copper/tinned copper allowance of 10 m total: red 2 m, black 2 m, blue 2 m, yellow 2 m, white 2 m. Fixed low-current controls only; final routes/lengths, motor-current and repeated-motion cables remain pending. Per-metre price unquoted; entire B04 PHP 1,150 allowance unchanged.

- **B05 label source (Step 55):** Yasen BrightPrint selected PP Matte A4 180gsm twenty-sheet pack PHP 158, order quantity one. Inside B05 PHP 300, remaining PHP 142 mounting estimate. Inkjet media; printed smudge/water resistance, adhesion and printer compatibility not tested. No label printer added; any paid printing/delivery fees separate.

- **Coil architecture clarification (Step 60):** 24 V DC coil/LS contactor is a proposal, not a user-required feature. User reports no accessible matching listings; compare locally available 220–230 V AC-coil alternatives with documented heater/contact/coil ratings and a revised reviewed B07/B08/reset/stop arrangement. Dedicated 24 V supply/accessories must be removed if made obsolete by that finalized arrangement; do not buy both. Current Excel pending coherent replacement, not a final mandatory DC24V design.

- **Current B06 candidate, Step62:** Screenshot-selected Jayson CJX2-1810(18A220V) PHP289, qty1; seller50–60Hz, oneNOaux, Ith32A. Heater AC1, exact coil operation and any needed auxiliary block unresolved. B07/B08 are procurement HOLD for coherent AC-coil/independent stop/interface revision. Prior priced24V supply and hobby interface are conditional references, not approved AC-coil purchases; remove/replace obsolete parts when finalized. No finished electrical circuit implied.

- **B08.1 current source Step66:** ENG LAB 1-channel5V relay screenshot PHP49 qty1 replaces Circuitrocks65. SellerLOW-trigger andmaximumAC250V10A/DC30V10A claims. Provisional low-voltage test choice; exactdriver/input/startupOFF, mainsboard separation and B06 ACcoil inductive/pickup match unverified. No optocoupler claim, directheater use or final mains approval. B07/B08.2 remainpending.

- **B08.3 selected Step70:** Jayson LA38-11BN listing green +Self-reset screenshotPHP62 qtyone; seller22mm,1NO+1NC,springreturn, nonilluminated appearance. LabelRESET. Actual contact voltage/utilization rating, markings and final independentstop/reset arrangement pending; noautomatic cooking restart. No extra ordinary startbutton or contactblock assumed.

- **First-order priority (Step87):** User requests essential reusable prototype purchases first. docs/PROTOTYPE_FIRST_ORDER.md lists controller/LCD/buttons/three initial microswitches/breadboard/jumpers at PHP1183 planning subtotal before shipping/tools. This supports logic/input tests only. Actual dispensing, basket motion and heating require deferred matched motors, power/protection and mechanics; do not claim complete functional prototype or exact final specifications. MasterBOM unchanged.

- **Step88 motor purchasing direction:** User prefers conservative oversizing to select flavor motors now. Compare documented12V20–40rpm geared motors around10kgf.cm rated torque, not a calculated guarantee. CytronSPG30-GR270 is a manufacturer-backed benchmark; local price/fit and LR7843/protection matching pending. Original25GA370 quote is not a price for the stronger candidate. No basket design change or second alternative motor purchase.

- **Current A05 replacement (Step92, supersedes25GA370 choice):** User confirms12V22RPM JGB37-520 listing1412288706/26828465072 remainsPHP352 each, quantitythree=PHP1056 conditional on voucher/checkout terms. Seller table5.5kgf.cm at18rpm0.30A, stall1.2A. Three motors replace642 priorcandidate, raising priced materials by414 toPHP17520.40. Actual fit/torque/duty/driver/protection untested; no second motor alternative purchase.

- **A06.1 selected diode pack(Step95):** KILIMA10pcsSR5100 PHP64 qtyonepack, nominal5A100V,3conditionalpositions+7spares. Replacesunquoted3loosediodes; noadditionalSB560. Actualidentity/thermal/circuitandmissingonboardpathchecksremain. PricedmaterialsPHP17584.40,3unquotedmaterialsplusfees.

- **Current supply architecture override(Step97):** User will buy one regulatedfactory-enclosed12V5A60W flavor/control adapter at their physicalstore, actualpricepending; reuse in finalflavor/control branch. A17nowthisadapter; A17.1separatebasket supply unquoted/deferredpendingA16. Supersedes earlieronesharedsupply rule; no temporaryadapter. WithdrawoldPHP1500sharedestimate ratherthanassignwithoutquote to eithernewunit. PricedmaterialsPHP16084.40exclude5unquotedmaterials+fees, not a saving. Independentstopandloadbudgetmustcoverbothbranches.

- **Step99 physical-store harness:** User confirms18AWGstrandedcopperred3m+black3m plusone5AratedDCinputconnector matchedtoA17adapter. SavedphysicalstorelistandB04Exceltext, individualquotespendinginside1150wholeharnessestimate. Signals22AWG10mremainseparatedeferredpurchase. No poweredtestornewmotorprotectionapproval.

- **A14candidateupdate(Step101):** InlineATO/ATCholderlisting599754496/15005730338atPHP49,provisional3=147inside180estimate. Replacesactiveglassholdercandidateforthese3branches; no duplicatepack. Seller16/14AWGconflict, fusesexcluded, DCvoltage/current/temperaturequalificationpending. Matching2Astandardbladefusesandotherprotectionunquoted.

- **A14selectedpack/remainingprotection(Step103):**2Astandard10pcbladefusepackPHP66plus3holdersPHP147=PHP213conditionalpricedbranchparts,replaces180estimate. DCratings/curve/qualityandadaptercoordinationpending. A14.1nowseparatelyquotesremainingmain/logic/basketDCprotection, nohiddenleftoverorcompletepackageclaim. PricedmaterialsPHP16117.40exclude6unquotedmaterials+fees.

- **Step104 consolidated prototype shopping:** docs/PROTOTYPE_FIRST_ORDER.md rewrittenforcontroller+3flavormotorprototype. Selectedpricedsubset2876plusunquotedphysicalstoreadapter/18AWGwire/DCconnectorandremainingprotection/mounting/tools/shipping. Threeinitialswitches, remaining4basketonesdeferred. Fullbasket/fryingprototypecannotbecompletedwiththissubset; masterBOMunchanged.


### Phase2 Step13 current update — 28 October2026

User reports all MOSFET modules were already checked and are working. Accept this as a user-reported functional check; test method, readings and total count were not supplied. Do not repeat the requested resistance test or claim measured current, safe OFF/reset, thermal or loaded-motor qualification. User explicitly confirms the 12 V motor adapter is not yet owned. Current checkpoint: USB off, connect one previously tested microswitch COM to labelledGND and NO to reservedD26; NC empty. Current uploaded button tester still only reads22/23/24; matching index diagnostic follows wiring confirmation. No driver power, extra purchase, upload or Phase3 transition.


### Phase2 Step14 — index input firmware prepared, 28 October2026

User reports the Step13 microswitch connected: COM/GND, NO/D26, NCempty; no independent endpoint photo. Complete inputs_index_test prepared/compiled with existing tools/libraries (11922 flash/599RAM); identical debounce helper host checks passed. Current board still has flavor_buttons_test; no new upload or input event observed. Ask for USB-only reconnection and approval of the concrete upload documented in docs/INDEX_TEST.md under AGENTS.md:30. No motor adapter owned or powered motor test.


### Phase2 Step14 upload executed — 28 October2026

User approved the prepared upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; source hashes matched compiled source. CLI upload --verify exited0. Serial INPUTS_INDEX_V1 READY plus 16 released-idle samples raw1111/counts0,0,0,0/lcdOK; no LCD error, held-at-boot tag or physical input press during capture. Unreadable startup bytes preceded clean tagged output. Monitor closed Ctrl+C exit0; inputs_index_test now runs on the board. No package install or wiring change. Physical lever test remains pending.


### Phase2 Step15 — first index input passed, 28 October2026

User replies “working as intended” to the explicit Step14 lever-hold/release/repress checklist. Record INDEX1 onD26 ACTIVE/READY display, one count per hold, unchanged count on release and another count on repress as PASS by user report. Numeric final count and a serial capture of these manual events were not supplied; do not invent them. This is an input test, not mechanical dispensing or a motor test. Next checkpoint: with USB/all supplies off, identify four connected holes in one empty breadboard rail by continuity1–2,1–3,1–4 before shared-ground/additional-switch wiring. Preserve successful LCD/button/D26 wires; current inputs_index_test remains uploaded. Adapter not owned, no motor power or Phase3.


### Phase2 Step16 — existing common ground reported, 28 October2026

User states an existing common breadboard GND line is already made for everything and supplies photo21. Accept the existing signal-ground arrangement as user-reported; retain it instead of building a second rail or repeating the empty-rail procedure. Photo shows multiple jumpers near the blue marking but does not prove every endpoint or split-rail continuity. Earlier working LCD/buttons/index1 support those tested signal paths, not every unused rail hole. No numeric continuity reading or new meter pass is inferred. Next: USB/all supplies off; index2 COM→same existingGNDsection/NO→reservedD28, index3 COM→sameGNDsection/NO→reservedD30; NCempty. Current input/index1 firmware unchanged. Wait for wiring report before matching all-three-index firmware/upload. No motor power or Phase3.


### Phase2 Step17 — switches2/3 wiring reported complete, 28 October2026

User says “done, connected” to Step16 NO28/30, COMexistingGND, NCempty. Prepared complete inputs_three_index_test for22/23/24/26/28/30 and existingLCD. Mega compile12054 flash/619RAM passed; identical helper host tests passed. Current Mega still runs previous one-index diagnostic; no new upload. Request USB-only reconnect and explicit upload approval; exact command and expected tests in docs/THREE_INDEX_TEST.md. No adapter owned, motors disconnected, no Phase3.


### Phase2 Step17 upload executed — 28 October2026

User approved the prepared three-index diagnostic upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523, read/write access and unchanged source hashes. CLI upload --verify exited0. Serial INPUTS_3INDEX_V1 READY and15 released-idle samples raw111111/counts0,0,0,0,0,0/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical press during capture. Startup unreadable bytes preceded clean tags. Monitor closed Ctrl+C exit0; inputs_three_index_test now runs. No new library, wiring change or actuator output. Physical three-index mapping/hold/release and button regression remain pending.


### Phase2 Step18 — three index inputs passed, 28 October2026

User reports “all microswitches working as intended” after the Step17 three-lever mapping/ACTIVE/READY/hold/release/repress checklist. Record all three connected flavor-index inputs26/28/30 as PASS by user report. Exact final counts and manual-event serial traces were not supplied. The user did not separately confirm the requested three-button regression on this latest six-input upload; earlier button checks remain passed. Do not extend this report to unconnected basket switches or powered/mechanical indexing. Next clarify whether four further roller switches are in hand before basket-input bench wiring. Existing sketch/wires unchanged; no motor adapter or powered test, no Phase3.


### Phase2 Step19 — three switches owned; logic dry run prepared, 28 October2026

User confirms no additional roller switches:3owned and4remaining of provisional7total. Adapter also not owned. Complete output-free cycle_logic_test prepared and verified (13360flash/797RAM; host controller/debounce testsPASS), waiting for explicit upload approval. Uses current six inputs/LCD;15s selected-index response then simulated5s/10s timers, busy lockout/timeout latch, ends Basket:pending. No powered dispensing/heating/basket success claimed; real300s/600s proposal and PDFmechanism unchanged. Details docs/CYCLE_LOGIC_TEST.md.


### Phase2 Step19 simulation upload executed — 28 October2026

User approved the prepared control-logic simulation upload with “proceed.” Rechecked /dev/ttyUSB0 USB1a86:7523 and read/write access; all source hashes unchanged. CLI upload --verify exited0. Serial CYCLE_SIM_V1 READY and17 idle samples phaseIDLE/flavor0/seconds0/raw111111/lcdOK; no LCD_ERROR, HELD_AT_BOOT or physical contact event during capture. Partial/duplicate boot text preceded stable tagged startup/status. Monitor closed Ctrl+C exit0; cycle_logic_test now runs on the Mega. No library install, wiring change, motor/heater outputs or manual simulated sequence performed. Next ask one flavor2/manualindex2/5s/10s/Basketpending sequence, then wait for visible result. Still missing4basket-switches and12Vadapter; fullprototype incomplete/noPhase3.


### Phase2 Step20 — first software dry run passed, 28 October2026

User replies “yes, working as intended” to the first Step19 manual flavor2→index2/D28→SIMWARMUP5s→SIMCOOK10s→SIMTIMERSDONE/Basketpending checklist, retainingFlavor2. Record PASS by user report; no stopwatch measurements or manual-event serial capture supplied. This validates the software/input simulation only, not physical dispensing, heating or basket movement. Next physical checkpoint: resetbenchsimulation, flavor1/index1, press otherflavorbuttons duringSIMCOOK, verifyFlavor1/timerunchanged andDONEremainslatched. Samewiring/code; no poweredactuators/Phase3.


### Phase2 Step21 — busy selection lockout passed, 28 October2026

User confirms “yes, working as intended” to Step20: flavor1/index1 starts the simulation; button2 held and button3 pressed during SIM COOK do not change Flavor1 or restart the countdown; the final Basket: pending view remains latched after another button2 press. Record busy-selection lockout and no queued restart as PASS by user report. No manual-event serial capture or stopwatch timing supplied; no physical motor/heater test inferred. Next test flavor3 with wrong index1/2 then correct index3 within the same15s window. Same software/wires; full prototype and powered/basket scope remain incomplete.


### Phase2 Step22 — wrong-index result passed, 28 October2026

User reports “working as intended” after Step21: flavor3 stays waiting when index1/D26 and index2/D28 are operated, then only matching index3/D30 advances through the simulated timers to Basket: pending. Record wrong-index rejection and Flavor3 sequence as PASS by user report. No independent timing measurement or manual-event serial capture supplied; this remains a software/input test. Next simulate missing index2 response, verify INDEX TIMEOUT stays latched after late index/new button, then explicit RESET returns idle. Same code/wires; no powered prototype or Phase3 transition.


### Phase2 Step23 — timeout/fault/reset passed, 28 October2026

User confirms “yes, working as intended” to Step22: omitting the selected index response produces SIM FAULT / INDEX TIMEOUT; a late index2 actuation and new flavor1 press leave the fault latched; releasing controls and pressing RESET returns to idle. Record timeout, fault latch and explicit-reset recovery as PASS by user report. No stopwatch or manual-event serial measurement supplied; this does not qualify motor jam protection or a physical safety stop. Next verify index1 already held at flavor1 selection requires release and a fresh actuation before warm-up. Same program/wires; no powered motor/heater/basket validation or Phase3.


### Phase2 Step24 — selected-index release check passed, 28 October2026

User reports “working as intended” after Step23: index1 held before flavor1 selection produces SIM RELEASE IDX and does not start warm-up; release changes to SIM PRESS INDEX without advancing; a fresh index1 actuation advances the simulation. Record selected-index release/re-actuation qualification as PASS by user report. No independently measured timing or manual serial trace supplied; no mechanical homing or motor protection qualification inferred. Next final current USB-logic check: button3 held through onboardRESET must remainidle, release remainsidle, onlyfreshpress selectsFlavor3. Sameprogram/wires; fullpoweredprototype incomplete, noPhase3.


### Phase2 Step24 complete — 28 October2026

User reports “working as intended” after Step24: flavor3 held through onboard RESET stays idle after startup, releasing it also leaves idle, and only a fresh press selects Flavor3. The matching index3 permits the simulated sequence. Record startup-held flavor suppression as PASS by user report. No manual-event serial capture or precise timing readings supplied. Planned USB logic checks complete; do not repeat without new issue/change. Full prototype incomplete. Next priority adapter label/plug review when acquired, plus outstanding4basket switches and remaining power/mechanical checks. Concise checkpoint docs/USB_LOGIC_CHECKPOINT.md.
