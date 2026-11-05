# Flavor-button start and motor selection

**Current sequence override — Step 15:** Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence. Five minutes is a trial setting, not proof that cold oil is ready. Validate warm-up/cooking durations for the actual oil fill, starting conditions, 300 g batch and loading sequence. If potatoes are in the oil during warm-up, they also heat during that period. Keep the manufactured fryer thermostat and verified independent overheat protection; timers do not regulate oil temperature or replace hardware power switching/stop protection. Retain position switches and motor drivers for basket/coil motion. External MAX6675/probe purchases are removed from the current compulsory BOM; earlier references to a temperature gate are superseded.

**PHASE 1: MATERIALS BUYING, Step 31 — 15 October 2026.** Keep the physical PDF design unchanged. Button start replaces potato-sensor start. The closer-funnel/custom-guide redesign is rejected. No basket motor has been approved for purchase. User confirms that selected final-use motors, drivers and supply must be bought once and reused from prototype to final machine.

## New sequence

1. Operator prepares the food/bag and machine; the precise loading/preheating sequence remains to be agreed.
2. Pressing one flavor button selects its packet, runs that coil to its dispensing index and starts/authorizes the fryer and cooking process.
3. The manufactured fryer's thermostat regulates heat. Specify a compatible controller-operated heating permission interface with qualified electrical support. Heater mains current must never pass through Arduino pins or a breadboard. Independent stop and thermal protection remain necessary.
4. Wait the user-requested initial 300-second warm-up interval, then time the initial 600-second cooking interval. Both are adjustable trial settings needing actual thermal/loading validation. The timer does not measure oil temperature.
5. At completion, operate the existing mechanism to lift, drain over the tank, flip/discharge into the existing receiving area and return safely. Confirm the existing linkage/trajectory with the mechanical team without relocating parts.

Recommended logic accepts one selection per batch and ignores held/repeated flavor-button presses while busy, preventing duplicate packets or timer resets. This is proposed logic, not confirmation of a separate packet-only mode. A coil index indicates position; successful one-packet release also depends on packet spacing, coil pitch and end geometry.

## Does it need a stepper?

**No; a stepper is an option.** A stepper rotates in commanded angular increments. A geared DC motor rotates while powered; its gearbox trades speed for turning force. **Torque** means shaft turning force, normally measured in newton-metres (N·m), not a basket weight rating.

| Choice | How it works here | Requirements |
| --- | --- | --- |
| Geared DC basket motor | A reversible driver runs it up/down or clockwise/counterclockwise; position switches identify stops. | Suitable output torque/speed, running/stall current, gearbox rating and power-off load retention. A worm gearbox is not automatically a verified brake. |
| Stepper basket motor | A dedicated driver receives step/direction commands to rotate a controlled amount. | Running torque at intended speed, suitable phase current/driver/supply, home/end feedback, acceleration and power-off load retention. Missed movement under overload can invalidate the assumed position. |
| Geared DC flavor motors | Each button selects its coil motor; an index switch/cam identifies the next dispensing position. | Loaded torque/current and packet-release geometry. Straightforward candidate for this application. |
| Stepper flavor motors | Each button commands a defined number of steps for that coil. | Three compatible stepper drivers and reference/position handling. Shaft rotation does not guarantee packet delivery. |

For economy, compare **geared DC motors with position switches first**. This is a project recommendation, not a universal price claim. A stepper can work if the complete motor/driver/transmission/holding arrangement is suitable and economical.

## The flavor spiral and its motor are different parts

The spiral is the mechanical coil that holds and advances packets. A motor is attached to its shaft through a suitable coupling and mounting arrangement within the existing design. The spiral does not require a particular motor technology just because it is shaped like a coil. Its pitch means the distance between successive loops. Packet size, pitch and front-end geometry determine when a packet falls.

- **Stepper option:** The controller commands small angle increments, called steps, to turn the spiral by the calibrated dispensing amount. If the motor has a gearbox or the driver subdivides steps, calculate the command count for the spiral output, not just the motor shaft. A jam can cause missed movement. Retain reference/index handling so power-up or an interrupted turn does not silently create a wrong starting position. Each of the three motors needs a compatible driver; the A06 single-MOSFET DC circuits cannot run bipolar steppers. [Pololu manufacturer explanation of stepper winding/driver compatibility](https://www.pololu.com/docs/0J88/all).
- **Geared DC option currently priced:** A conventional DC motor with a gearbox turns slowly with increased output torque. Each selected motor runs until a cam on its coil shaft reaches the next index-switch position. A cam is a small shaped piece that operates the switch; an index is a repeatable reference position. Starting at that position, the control must first see the switch release and then operate again, rather than stopping immediately on the initial signal. Stopping accuracy/coasting and jam timeouts need validation later. This uses A05 motors, A06 Arduino-controlled switching sets (now a candidate module plus necessary protection) and the three coil switches included in A07.

For either option, one full spiral revolution is an initial mechanical candidate for one packet, not a proven guarantee. Confirm the release angle with the actual loaded packets and coil. These are the final-use motors being tested; no small demonstration motors are purchased. A successful first selected unit can be retained and the other two identical units bought afterward, avoiding three unsuitable purchases at once. This is a staged purchase of the same final parts, not a separate prototype motor allowance.

**Current prices and choice status:** A05 now budgets three candidate **25GA-370 12 V/30 RPM** motors at **PHP 214 each (PHP 642)** from the user-supplied [Shopee listing](https://shopee.ph/product/156048989/2380743022). Selected variant/price are visible in the screenshot; shipping panel says **pre-order, ships in 5 days**, despite the “Ready Stock” title. This replaces the unavailable SGM-370 candidate and the superseded N20 inquiry; neither is bought alongside it. Rated torque/duty, running/stall current, shaft/mounting and loaded-coil turning requirement remain unverified. A06 now prices three selected LR7843 modules at PHP 50 each (PHP 150); any missing motor flyback diodes are separately quoted in A06.1. Motor-current/protection suitability remains pending. No stepper set added in parallel.

NEMA 17 and NEMA 23 are frame/mounting sizes; the names alone do not establish sufficient torque. [Manufacturer frame-size reference](https://www.orientalmotor.com/stepper-motors/stepper-motor-frame-sizes.html).

Stepper holding torque describes a stopped, energized motor. Available running torque changes with speed and driver conditions; load, acceleration and current settings affect reliable motion. [Manufacturer torque reference](https://www.orientalmotor.com/products/pdfs/2018-2019/technical-reference/Technical_Reference_Stepper_Motors.pdf), [Pololu configuration guide](https://www.pololu.com/docs/0J71/4.3).

Power loss removes electrical holding force. Residual magnetic resistance must not be treated as a brake for a suspended basket. Both stepper and DC arrangements need appropriate load holding/retention. [Manufacturer vertical-load guidance](https://www.orientalmotor.com/applications/load-elevator.html), [brake reference](https://www.orientalmotor.com/products/pdfs/2018-2019/A/Product-Line-of-Stepper-Motors-and-Overview.pdf).

## Superseded GA12-N20 review (Step 26, 15 October 2026)

**Step 27 update:** User confirms this inquiry was for A05 and reports the earlier listing unavailable. The current candidate is now the 25GA-370 described above; the following N20 review is historical and is not the shopping instruction.

User supplied the [fulabs.ph GA12-N20 Shopee listing](https://shopee.ph/product/1367148707/41273875158). Screenshot shows brushed DC micro gearmotors, 3 V / 6 V / 12 V variants and speed choices from 15 to 1000 rev/min. No variant is selected. PHP 163-165 is the listing family range, not a confirmed price for a particular voltage/speed pair. Direct Shopee access is unavailable.

This is a **geared DC motor, not a stepper**. It may be a lower-cost A05 flavor-coil candidate if the loaded spiral turns within its rated output torque and gearbox/shaft limits. It is not selected for basket lifting/flipping: no sufficient load/holding/gearbox evidence is supplied for that application. Size, voltage and RPM alone cannot establish either role's suitability.

For further comparison with the planned 12 V supply, inspect the **12 V, 15 rev/min** variant's specifications first. This is an evaluation target, not an approved purchase or measured torque choice. Nominally 15 rev/min corresponds to four seconds per revolution; actual loaded speed is unverified. A higher gear reduction does not make an unknown micro gearbox suitable for arbitrary loads. The 3 V and 6 V options are different rated versions and must not be presumed suitable for a 12 V motor branch.

Required before accepting a substitution:

- Exact selected voltage/speed, price and motor/gearbox data, including **rated running output torque** and its duty limits. Stall torque is not a usable continuous operating rating.
- Running and **stall current** (current when the shaft cannot turn), so A06 driver/diode/fuse/supply suitability can be checked. Do not infer current ratings from other similarly shaped N20 motors.
- Shaft dimensions/flat, mounting and coupling fit. The coil should have appropriate independent support rather than assuming a tiny output shaft can carry its entire weight; resolve within the unchanged mechanism.
- Turning requirement of the actual fully loaded coil and its reference/index arrangement. A DC motor still uses position feedback to reach the dispensing stop; elapsed motor-on time alone is not proof of one complete turn or one packet.

[Pololu's manufacturer specifications for its own micro metal gearmotor family](https://www.pololu.com/category/60/micro-metal-gearmotors) illustrate that windings/gear ratio, no-load speed, torque and stall current are distinct selection data. Its numerical specifications are **not** assigned to this Shopee motor.

**BOM decision:** Keep A05 and its existing allowance unchanged. Record this link as pending review here, not as an accepted replacement or an additional prototype motor. If accepted later, the same selected motor(s) are reused in the final machine. No sample-only extra motor purchase is added.

## Current A05 acceptance checks (Step 27)

The selected 12 V rating matches the proposed nominal motor branch, subject to actual supplied ratings. Nominal 30 RPM corresponds to one revolution in two seconds; that does not prove packet dispensing time or loaded speed. A05 is still a brushed DC motor using the three coil index switches in A07. A06 provides one-direction switching, not guaranteed immediate braking, so reference stopping/coasting and one-packet release need validation. Faster nominal speed is not evidence of greater turning force. Check the 25 mm gearbox and actual shaft/coupling fit within the existing design; no support/mounting fit is established by the listing photo.

Obtain the selected-variant rated output torque/duty and running/stall current. Match them to the fully loaded coil and A06/diode/fuse/supply ratings. Prefer validating one suitably specified final-use unit before buying all three; retain that same unit in the finished machine. No separate practice motor is budgeted.

## A06 manual PWM controller review (Step 28)

User supplies the [ENG LAB.ph Shopee knob controller](https://shopee.ph/product/1021339444/10599592535). Screenshot shows PHP 49, minimum purchase quantity three, a rotary potentiometer and a four-position power/motor terminal block. The title advertises PWM, max 5 A and Arduino use, but no documented external Arduino PWM/enable input or suitable motor-current/thermal test data are supplied. Direct product-page access was unavailable.

**Not accepted as a direct A06 replacement.** PWM means pulse-width modulation: varying the proportion of time power is switched on to control average motor power. A manual knob controller can generate PWM internally without accepting any PWM command from an Arduino. Our controller must start the selected coil on a flavor-button press and stop at its index switch; a manually set knob alone does not implement that automatic operation.

This does not establish that adaptation is impossible. An additional suitable switch or a documented external-control modification could enable automatic operation, but neither is established by the screenshot, and buying both a manual regulator and an A06 switch would add scope/cost. Do not assume the potentiometer terminals are safe 5 V Arduino inputs or modify the board on that assumption.

For A06, search for a **5 V logic-controlled MOSFET trigger/switch module** or a documented brushed-DC motor driver. Verify a signal/enable input, 12 V motor compatibility, usable continuous/start/stall current, fail-off behavior and motor turn-off protection. A board marked SIG/IN/PWM still needs its actual pinout and input thresholds verified. A generic advertised 5 A number is not a tested continuous or stall-current capability.

[DFRobot's manufacturer documentation for a logic-controlled MOSFET power controller](https://wiki.dfrobot.com/dfr0457) illustrates a separate control interface and the requirement for a freewheeling diode with inductive loads. It is a functional reference, not a selected purchase, PH price quote or specifications for this seller's board. A06's current DIY MOSFET/diode allowance remains unchanged; any accepted module would replace its included parts rather than being added on top.

**BOM decision:** Do not add this product as A06 or reduce the budget using PHP 49. Need evidence of a suitable external control input and load compatibility before reconsidering. No minimum-order purchase is authorized/performed.

## A06 selected LR7843 module (Step 30)

New user screenshots visibly select **LR7843 at PHP 50** and provide seller text documenting **3 V/5 V signal inputs, high-level start, low-level stop, PWM regulation and DC motor start/stop**. This resolves the previous missing selected price and advertised signal-compatibility information. Three modules cost **PHP 150**, before delivery; each operates one flavor motor through the existing index-switch control sequence.

The seller's optocoupler-isolation claim is not independent proof of the complete circuit's isolation. [Infineon's IRLR7843 specification](https://www.infineon.com/part/IRLR7843) describes the chip, not a tested current capacity for the whole seller board. Verify actual input current within the Mega pin budget, OFF behavior during reset/disconnection, motor running/stall current, module heating and suitable turn-off protection during the approved later phase. No high-frequency PWM performance or motor-current capability is established by the text alone. Terminal blocks and headers appear loose and may need soldering.

**Protection is separate:** The screenshots do not establish a suitable onboard motor flyback path. A06.1 therefore reserves one appropriately rated external diode per motor if missing, quantity three, with price/model pending real motor/current/circuit data. Do not treat a MOSFET body diode or input optocoupler as proof of motor flyback protection. Do not buy duplicate external diodes if a suitable onboard path is verified. No wiring or physical test has begun.

**Budget treatment:** A06 now lists module-only PHP 50 × three = PHP 150. The former PHP 160/channel complete assembly allowance is removed, including its discrete MOSFET/gate parts. A06.1 keeps the remaining conditional protection visible as **Quote needed**, not zero. Priced subtotal falls by PHP 330, but this is not a guaranteed full-channel saving because the diode cost is still unquoted. No additional prototype-only drivers are bought.

## A07 roller-switch source (Step 31)

The user-supplied [SHOPOMATIC.ph SHOPO roller microswitch](https://shopee.ph/product/447511770/11436017124) matches the proposed contact-actuated position-sensing form. Screenshot price is **PHP 22 for one piece**; seven provisionally cost PHP 154. Four detect proposed basket endpoints and three mark coil reference positions. Final placement/count still depends on the existing mechanism. No basket/coil layout is redesigned by choosing this listing.

Three terminals are pictured; do not infer a particular manufacturer model or terminal order from appearance. **COM** is the common contact; **NC** means normally closed (connected to COM while unpressed); **NO** means normally open (connects to COM when pressed). Confirm markings/contact behavior on the delivered part during the approved phase. These signal switches do not directly switch motor/heater power, stop a moving assembly mechanically or replace the separate hardwired emergency-stop controls.

Confirm switch body size, mounting-hole spacing, lever/roller travel and mounting rigidity. Use a cam/stop that actuates without overdriving the lever, and locate the switch away from hot oil, steam/splash and excessive heat; no sealing or heat rating is established. For low-current digital inputs, verify stable contact operation and applicable minimum load. [Omron manufacturer guidance](https://www.ia.omron.com/product/cautions/29/safety_precautions.html) notes possible contact faults when general-load switches are used at microloads; its product ratings are not assigned to this generic switch. Any eventual pull-up/interface choice and debounce behavior belong to the later wiring/firmware phase.

## Inputs needed before choosing a basket motor

- Total moving mass: basket, supports, 300 g food and retained oil.
- Existing lift sprocket pitch radius, transmission ratio, friction, travel and speed.
- Existing rotation pivot, loaded centre-of-mass distance, dump angle and linkage ratio.
- How the existing mechanism creates lifting/rotation and reaches the receiving area. One motor can do both only if the existing linkage converts its motion accordingly; choosing a stepper does not create that linkage.
- Load retention when power is removed, guarding and position feedback.

Example only: a 1 kg moving assembly lifted through a 20 mm effective sprocket radius needs about `1 × 9.81 × 0.02 = 0.196 N·m` ideal torque before friction, acceleration and margin. Tipping a 1 kg assembly with its centre of mass 100 mm horizontally from its pivot can require `1 × 9.81 × 0.10 = 0.981 N·m` at that pivot before other effects. These are illustrative values, not measured machine dimensions or a motor specification.

A selected stepper needs its compatible current-regulated driver and supply. The previously proposed single BTS7960 DC module is not a drop-in bipolar-stepper driver. Do not select A4988/DRV8825/TB6600 solely by name before motor phase current, actual module ratings and cooling are known. DC drivers/supplies likewise need starting/stall-current compatibility.

## BOM consequences

- Remove the potato-start detector and its logic. Keep the fryer's internal thermostat/thermal protection and basket/coil position feedback. An external controller-temperature reader is not required for the selected timed sequence.
- Three flavor buttons/motors were already required. Their new start role can avoid a separate ordinary start button, subject to the chosen control interface. Hardware emergency stop remains separate.
- Specify actual controller-operated normal heating permission; the manual-only fryer ON/OFF alternative is not the accepted new behavior.
- The PHP 14,254.43 closer-funnel/single-motor partial estimate is superseded and does not apply to the unchanged PDF design.
- The current simplified spreadsheet and BOM now contain two materials tables and a separate fee table. Actuator/driver/supply selections and itemized electrical-material/fee quotes remain unresolved; the priced subtotal is not a complete quotation. See [current BOM](BOM.md).

No construction, firmware, installation or flashing has been performed. Remain in Phase 1 pending mechanical inputs, validated motor/driver/supply selection, outstanding prices and revised BOM review. Timer-based sequencing and one I2C LCD are confirmed requirements.


## A16 shopping stage — Step 48, 16 October 2026

A16 covers the real basket actuation, provisionally two axes: lift and tilt. This is separate from the three A05 flavor motors. Two motors are not a confirmed mechanical requirement until the existing lift/flip linkage is established. Keep the PDF layout and buy final-use motors only.

For finding comparison listings, search `12V DC worm gear motor high torque reversible` or `12V DC geared motor high torque rated torque`. This is a search category, not a selected motor/model, guaranteed load capacity, RPM or price. A worm gearbox is not automatically a verified power-off brake. The proposed A04 BTS7960 boards suit brushed DC architecture only after voltage/current/thermal compatibility checks.

Before choosing speed/torque and a purchase variant, obtain:

1. Basket plus moving supports mass, in addition to the confirmed 300 g food and retained-oil allowance.
2. Lift sprocket pitch diameter/transmission and intended travel/time, and flip pivot location relative to loaded basket centre of mass. Ask the mechanical team to mark both driven shafts on the existing drawing and explain whether a linkage couples lifting/flipping.
3. Existing brake/counterbalance/other power-off load retention.

Listing evidence: rated running output torque (not just stall torque), rated speed at load, rated/duty limits, running/start/stall current, shaft dimensions and mounting. Do not assign a 300 g motor label to the whole basket or select two identical units solely because A16 has quantity two.

Current PHP 2,000 each × two = PHP 4,000 is an unverified planning allowance, not an actual product quotation. No new supplier or variant is selected by this step.

[Pololu gearmotor manufacturer guidance](https://www.pololu.com/category/271/12v-37d-metal-gearmotors) distinguishes loaded operation from stall conditions and warns that stalling can quickly damage motors. Its product ratings are not assigned to marketplace motors.


## Conservative flavor-motor option — Step 88, 16 October 2026

User proposes overdesigning flavor motors so they can be purchased now. Accept the intent to choose an explicit conservative torque target without waiting for every load measurement. Oversizing cannot establish mechanical fit or guarantee sufficient margin against an unknown load; do not claim a quantified safety factor or that a 37mm frame is always stronger than25mm. A candidate with documented rated running output torque is more useful than a generic high-torque/stall-only claim. Keep the fixed PDF layout.

Practical screening target:12V brushed DC geared motor, roughly20–40rpm output, documented rated torque around10kgf.cm (~0.98Nm) as a conservative comparison target, not calculated project requirement. Search `12V 37mm gear motor 30RPM rated torque` or `37GB520 12V 30RPM`; model families alone do not establish torque/current/shaft/rating. Prefer documented start/stall current within2A for the existing conservative flavor-channel screening, but size actual driver/supply/protection from selected actual motor. Check37mm body envelope and shaft/coupling dimensions before ordering three. Stronger motor can damage packets/coil/coupling during jam; retains guarding, timeout, stop and fault protection.

Manufacturer-backed benchmark: Cytron OEM SPG30-GR270 without encoder, https://sg.cytron.io/p-12v-37mm-dc-geared-motor-spg30-gr270 . Published12V,37mm,270:1, rated10kg.cm at29rpm/400mA, no-load37rpm/120mA, stall1.2A, shaft6mmD15mm long. Use rated10 figure, not stall40 figure as operating torque. Encoder not required by current three cam/index-switch arrangement. This is a documented candidate, not an accepted price/fit or a claim that all generic37GB520 units share these data. Philippine checkout price/shipping and local availability unverified; no foreign price converted or invented.

Existing three LR7843modules remain candidates (PHP50each screenshot), not proof of board continuous/pulse current merely from chip161A advertising. No need to automatically upgrade driver solely for motor frame diameter; verify actual motor current, board terminals/traces/thermal behavior, input/reset/OFF and motor protection. Board current limit not established. The Cytron1.2A stall example is within prior2A screening but does not independently qualify board.

Flyback definition: motor turn-off current needs a safe recirculation path. For a12V low-side one-direction channel with the documented1.2A-stall candidate, a genuine axial SB560 Schottky5A60V is a conservative diode candidate, one per motor if suitable onboard path absent. Vishay https://www.vishay.com/docs/88721/sb520.pdf and https://www.vishay.com/en/product/88721/tab/designtools-ppg/ verify ratings/freewheeling category. Thermal mounting, actual operating current/transients and circuit still need check;5A headline rating has datasheet conditions, not unlimited current. Do not assign this diode to future unspecified higher-current motors, bidirectional basket drivers or AC contactor coils. Flyback diode is not a fuse, current limiter or guaranteed jam brake. No wiring steps provided. Exact local price/selected supplier pending; do not duplicate verified onboard diode.

Procurement path can advance now by choosing a motor meeting these targets with actual shaft/envelope evidence, then matching3drivers/3missing diodes/supply as one motor group. MasterBOM retains original25GA370 price as provisional until a replacement listing is actually selected; never add both motor alternatives or call PHP642 a quote for stronger units. Step87 first-order list is expanded only after actual candidate selection; this discussion does not prohibit progressing with a conservative selection. No purchases/physical tests/Phase2 approval.


## Supergoodsales25GA370 torque-table review — Step89,16October2026

User screenshots https://shopee.ph/product/93948225/1829351870 show GA25YN370/25GA37025mm brushed motor,4mm shaft10mm long, generic ratedpower3.5W/voltage5–12V/current0.06A, variant range12V5–1000rpm, PHP193–246 with none selected. No exact30rpm price. Seller text shippingoverseas1–2weeks despite ReadyStocktitle; not verified delivery promise.

Poorly formatted table appears to list30rpm row: no-load30rpm, loaded25rpm, loadtorque770gf.cm, stalltorque12.0kgf.cm and stallcurrent<=2.1A. 770gf.cm=0.77kgf.cm (~0.0755Nm), well below Step88 conservative10kgf.cm (~0.98Nm) running-torque screening target. Do not treat12kgf.cm stall figure as usable continuous operating torque. Table has suspect repeated1:150 ratio for10rpm/30rpm and current headings/values require clarification; do not call this manufacturer-verified rated continuous performance. 5rpm row load1150gf.cm=1.15kgf.cm, so slowest variant also does not document10kgf.cm running torque. Atno-load5rpm,12s/rev, but no reason to prescribe slowerdispense to chase stallfigure.

Decision: candidate may or may not drive actual small flavorcoil, unknown actual requirement, but this evidence does not establish requested conservative upgrade. Do not claim it is stronger than previoussame25GAfamily or qualifiesdriver. Vendorclaims stall<=2.1A not prior<=2A screening, actualmodule/circuitmatch stillpending; no categorical rejection on0.1A difference alone. Maintain37mm20–40rpm/documentedaround10kgf.cm operating target or CytronSPG30-GR270 reference, actualfit/localpricepending. No mandatorygeneric37GB520 performance assumed.

No replacementselected, no motor/diode/driverprice accepted from this listing. OriginalA05candidate642 and masterBOM totals unchanged. No purchase/physicalwork/phase transition.


## ZENG WHCD JGB37-520 candidate — Step90,16October2026

User https://shopee.ph/product/1412288706/26828465072 screenshots show ZENG WHCD JGB37-520 family6V/12V/24V,7–960rpm,6mmDshaft, generic3.6–10.8W, no-load0.05–0.3A, maximum21KG.CM. Neither speed nor voltage option selected. PHP352 explicitly AfterVoucher is not a verified12V35rpm unit price. 35rpm lies inside20–40rpm screening range, 22rpm alternative also inside;35rpm is comparison preference, not calibrated release time. No-load current cannot size driver/supply against jams/startup.

21kg.cm is unspecified maximum for a family, not a documented rated operating torque for12V35rpm. Do not assert stall vs rated classification without data, nor assign the maximum to every speed/voltage. Need parameter-table image for exact12V35rpm rated/load torque and current, stallcurrent and shaft/envelope/mounting. Mainimage video includes additional controller/wiring, but do not assumeincluded orArduino-compatible; motor-only versusMotor+Bracket are listed options, no extra manualPWMcontroller needed. Bracket can be chosen only if actualfit/need, not automaticadditional expense.

Candidate is worth pursuing as requested37mm class, not approvedcomplete motor-driver package. Next select12VMotor+35RPM for comparison price and read parameter-table thumbnail (or request seller datasheet if absent). Prior10kgf.cm running target is discretionaryconservative screening, not a proven minimum for flavorcoil; do not reject actualadequate smaller loads solely because this target was invented beforemeasurements. Usercan choose documentedcandidate with explicitmechanicalrisk, but don't falselycall knownmargin. Keep3LR7843driver/protection matching pending actualstall/current/boardacceptance, no finaldiode basedsolelygenericmotorname.

No workbook/source substitution or budgetchange because noselectedvariantprice/data. No purchases, wiring orPhase2 transition. ExistingA05 quote remains prior25GA370candidate, not a quote for JGB37upgrade.


## JGB37-520 variant table received — Step91,16October2026

User selected35RPM +12VMotor screenshot showsPHP352 AfterVoucher, qty1; baseprice/vouchereligibility/shipping not established. Table header12V JGB37-520-1260. Read169:1 row: no-load35rpm0.1A, ratedload28rpm0.30A3.40kg.cm, stall13.6kg.cm1.2A, gearbox26.5mm.270:1 row: no-load22rpm0.1A, rated18rpm0.30A5.50kg.cm, stall22kg.cm1.2A, gearbox26.5mm. Values are seller table, not measured/manufacturer-independentverification. Listed3.6W column does not necessarily equal shaftmechanicalpower; do not claim outputpower from it. Noencoder required currentindexswitchplan.

For user's extra-torque preference, recommend12V22RPM comparisoncandidate:5.5kgf.cm≈0.54Nm running vs3.4≈0.33Nm35rpm; ~62% more sellerlisted runningtorque, about2.7s no-load revolution/3.3s rated18rpm. Times are nominalshaftrotation, not calibratedpacketdelivery. Do not interpret stalls13.6/22 as continuous. 10kgf.cm earlier target was arbitraryconservativebenchmark, not calculatedminimum, so this candidate is not rejected solely below10. Evidence permits provisional flavorprototype candidate selection now, actualcoil/coupling/shaft/bodyfit and jamdamage/requiredtorqueremainuncertain. Same37mm6mmshaftenvelopepending. Bracketnotincludedmotor-only; selectonlyactualneededmounting.

Bothtablevariants1.2Astall are within earlier screening; threeLR7843modules remain candidates, boardtrace/terminal/thermalinput/reset andactualsupplyprotectionstillverify. OneSB5605A60V perlow-side motor conditionalifnoverifiedonboardpath remainsappropriatecandidateforstatedcurrents, datasheetthermalconditionsapply. Supply/branchwire/fuse selectionmustprecedepoweredtest, nomotorpowerbreadboard/Arduino. NoautomaticdrivercurrentprooffromICrating.

Pendingnext: user choose12V22RPM and selectedprice; current35RPM voucherprice is not22RPMquote. NoExcelreplacementyet or finaltorqueguarantee. Original25GAquote retainedprovisional until replacementchoice/price recorded. Nophysicalwork/phasechange.


## Current A05 selection override — Step92,16October2026

User confirms samePHP352 price for12VMotor22RPM JGB37-520 after previous35RPM screenshot. Record as selected provisional candidate:3x352=PHP1056 replaces25GA3703x214=642, delta414, neverbuyboth. NativeS42supplierlink added. Seller12Vtable22RPM no-load0.1A, rated18RPM5.5kgf.cm0.30A, stall1.2A; advertised37mm/6mmDshaft. Actualfit/duty/current, coilperformance and LR7843board/protection matching untested. Indexswitches remain, noencoder/manualspeedcontrolleradded. Motor-only option no includedbracketassumed.

PHP352 display wasAfterVoucher. Followupconfirmsvariantprice, not eligibility forthreeunits, baseprice or shipping. BudgetPHP1056conditional quotedsubtotal, check actualcart beforepayment; no confirmedpurchase. A05pricechange yieldsA9182/B8338.40/materials17520.40/withoutfryer16326.40. Fourunquotedmaterialentries andtwofees remain, completetotalQuoteNeeded. Motors+LR7843modules priced1056+150=1206 beforemissingdiodes/supply/protection/shipping. No claim complete powered-motor kit or approvedphysicaltest. Nophysicalwork orPhase2approval.


## Flavor-motor completion checklist — Step93,16October2026

User asks what else selectedthreeJGB37-52012V22RPMmotors need. They require more than3LR7843boards. ExistingBOM purchases reused, no extra motors/controllers/indexswitchsets automaticallyadded.

Electrical:3LR7843boards alreadybudgeted;3SB5605A60V axialSchottkyflybackdiodes as candidate one per12Vlow-side motor onlyifmodulelacksverifiedsuitablepath; sellerstates1.2Astall, diodeactualthermal/transientlimitsapply. Flybackprovidesoffcurrentpath notfuse/jamcurrentlimiter. Manufacturerreference https://www.vishay.com/en/product/88721/tab/designtools-ppg/ . Onefactoryenclosed12Vsupply is needed, pluscorrectDCbranchprotection, motorpowerwire/connections andlogicinterface supply. A17singlefinalsupply remainsunselectedbecausebasketloadunknown; no automatictemporaryflavoradapterpurchase. Flavor-only allthreeclaimedstall3x1.2=3.6A beforelogic/loadmargin, notfullmachinePSUsizing. AvoidpoweringmotorsfromMegaUSB/pins,breadboardorDuPontsignaljumpers. Exactfuses,wiregauge/length/connectors pending chosenpowersupply/installation; noapprovalof22AWGglassholderormainsoperation. ExistingA13buck candidate retainedfor5Vlogic when12Vsupplyused, USBbackfeedrouting inPhase2.

Filtering: existingA15ten100nF50Vceramicpurchase includes3potentialmotorpositions; existing1000uF25Vpackcoverspotentialrailbufferingifneeded. No duplicatecapacitorpacks; actualplacement/value/need andelectrolyticratingscheckedinwiringphase. LR7843looseheaders/screwterminals mayrequiresoldering; motorleads/terminaltypeconfirmondelivery, appropriatesoldering/insulationtoolsifnotowned.

Mechanical: three indexswitches alreadyinfirstorder; needonecam/actuatingfeaturepermotor/coilshaft, threebrackets/securemountsappropriate37mmmotorandactualframe, andthreecouplings/hubsconnectingmotor6mmDshafttoactualspiralshaft. Couplingotherside, shaftlength,mount-holepatternandscrewdepthpending; don'tblindorder6to6couplersorassumeMotor-onlyincludesbracket/coupling. Mechanicalteamcanprovideexistingcomponents; buyonlymissingones, finalreuse.B05mountingallowancealreadycoversswitchfixtures, notautomaticnewduplicatefee. Poweroffcoasting/indexprecision, jampacketdamageandguardingneedtest. Motoronlyone-directionviaLR7843; reverseabilityofmotorisnotautomaticreversingdriver. No needencoders/manualPWMknobs/relays/stepperdriversoradditionalArduino forcurrentplan.

Purchasingnextconcreteitem:SB5605A60Vthrough-holelisting, qty3conditionalonmissingonboardpath. Motor-power supply/protection completebeforepoweredtests; mechanicalfit beforeassumingfinalreuse. NoExcelpricechangeorphysicaltests/Phase2approval.


## A06.1 SR5100 alternative — Step94,16October2026

User listing https://shopee.ph/product/487295469/11536801341 KILIMA.ph shows10pcsSR5100 and10pcsSR3100 options, neitherselected, PHP64–72range. Description specificallystatesSR5100DO201A5A100V andSR3100DO273A100V; title/introcontainsinconsistent3A/5A40/80/100/200Vtext, so relyonexactvariantlabelandinspectdeliveredpart, nottitle. Originalclaimnotauthenticityverification. One10piecepack sufficientfor3motorpositionsplus7spares; don'tbuy3or10packs. NoexactSR5100packpriceyet.

SR5100nominal5A100VSchottky is a reasonablealternativecandidate toSB5605A60V forselected12Vlow-sideone-direction1.2Astall flavor motors, subjectactualdatasheetthermal/circuitchecks anddeliveredpartidentity. Higherreversevoltage is ratingnotappliedmotorvoltage andnotuniversalbetterforwardloss. Don'tdeclareallSR5100manufacturersidenticalorhousebranddataprovesKILIMAauthenticity. Primaryhousebrandcatalogue https://tw.element14.com/en-TW/multicomp-pro/sr5100/schottky-rectifier-5a-100v-do/dp/2675129 publishesSR5100Schottky5A100V. Exactmanufacturerunknown. Boardflybackpathstillnotverified; useonlymissingappropriateprotection, notduplicatebothSB560andSR5100. SR3100notselectedaspreferredlowercurrentalternative; do notfalselyclaimcannotfunctionat1.2A.

Requestselect10pcsSR5100qty1andshowprice. Onceacceptedpricebudgetfullpack, replaceA06.1qty3looseunquoteddiodeswithonepack(3used) ratherthanprice-perdiodeproportion. NoExcelpricechangeuntilselectedpackprice, noadditionalA06MOSFETs, powerorphysicaltest. RemainPhase1.


## A06.1 selected diode pack override — Step95,16October2026

User selected10pcsSR5100 option PHP64,qtyonepack atKILIMA https://shopee.ph/product/487295469/11536801341 . ReplaceA06.1threeunquotedlooselypriceddiodeswithone10piecepack/fullPHP64cost. Threeconditionalpositions, sevenspares. Nominal5A100VSchottky and alternativeSB560, neverbuyboth. Deliveredidentity,manufacturer,thermal/circuitadequacy andabsenceofsuitableonboardpathstillcheck. SellerOriginalclaimnotverification. No purchase/physicalwiringperformed.

A9246/B8338.40/materialspriced17584.40,withoutfryer16390.40. Threeunquotedmaterials(B07/B08.4/B09.1)plus2feesremain; completetotalsQuoteNeeded. Motors1056+drivers150+diodepack64=PHP1270 before supply/protection/wires/mounting/shipping. Firstlogicorder1183+1270=PHP2453 before remainingparts/tools/shipping, notcompletepoweredprototypecost.


## Next motor power-supply comparison — Step96,16October2026

User asksnextafterdiodes. Recommend evaluating a factory-enclosed regulated12V5A60W adapter for flavor+logic branch now. Three sellerlisted1.2Astall motors total3.6A;5Vlogicbranchbelow1Athroughbuck addsroughlyunder0.6A at12Vdependingefficiency, leavingplanningheadroomin5A. Actualstart/loadtransients/temperature/currentlimitingandratingsmustcheck; nominal5A is a comparison target, not testedguaranteeorprotectionrating. Oneflavormotorpercycleexpected, but conservative comparison includesallthreeclaimedstall. ExamplemanufacturerMEANWELLGST60A12-P1J datasheet https://www.meanwell.com/Upload/PDF/GST60A/GST60A-SPEC.PDF confirms12V5A60Wfamilyvariant and wideACinput; noPHpricequoted. No mandatorypremiumbrand; avoidunknownfalse-ratedsupply. NeedsmatchingratedDCconnector/polarityandACcord; includedcordnotassumed, noexposedACscrewterminalbenchunit recommended.

IMPORTANT: this is a PROPOSED purchasing architecture adjustment, not confirmed userdecision. PriorA17planonefinalsharedsupplycannotbesizedbeforebasketselection. Buying12V5A now onlymakesreusesenseifretainedasfinalflavor/control supplywithseparatelysizedbasket supplylater. Explicitlypresenttradeoff, do notsilentlycall5Awhole-machineadequateoraddsecondPSUtomasterBOMwithoutselection/reconciliation. AlternativewaittochooseonecombinedPSUwhenbasketknown. No disposabletemporaryadapter recommended. KeepA17PHP1500provisionalwholeoldallowanceunchangeduntiluserchoice/productquote; extraeventualsupplycostnotzeroandneeditemizedifretaineddualbranchplan. Controls/independentstoparrangementmustcoverbothmotorsuppliesappropriatelywithresidualenergyconsidered.12Vadapterdoesnotpowerfryer. No purchaseorphysicaltest/Phase2approval.

Search `12V 5A 60W regulated power adapter` or `Mean Well GST60A12-P1J`. Sendratinglabelandconnector. Exactdiode/driver/cap/USBbackfeed wiring deferredapprovedPhase2.


## A17 physical-store purchase — Step97,16October2026

User explicitly says to list12V5A60Wadapterforphysicalstorepurchase andknowswheretobuy. Qtyone, no price/store name invented, no furtheronlinelisting needed. Regulated12VDC5Acontinuous60Wfactory-enclosed withproperACinput/protection andmatchedratedDCconnector/polarity; suitableACcordincludedorpricedseparatelyifneeded. It remainsfinalflavor/control supply, notbasketorheaterpower. Checklabelandlaterloadresponse; userinstructionisnotaconfirmedpurchase.

A17replacedsharedPSUwiththispricedunknownadapter; addA17.1basketPSUdeferredunquoted. OldPHP1500sharedestimatewithdrawn, notautomaticallyreassignedorcountedasavings. MasterpricedA7746/B8338.40/materials16084.40,withoutfryer14890.40, fiveunquotedmaterials(B07/B08.4/B09.1/A17/A17.1)andtwofees. CompletecoststillQuoteNeeded. Motor+driver+diodefirstsubset1270/logiccombined2453unchangedandexcludeallnewunquotedpoweritems. Twofinalsuppliesmustfitindependentstopdesign; no extraunusedpracticeadapter. NoPhase2/purchase/physicalwork.


## Next DC power wiring — Step98,16October2026

User asksnextafterphysical-storeadapter. Proposedshortfixed12Vflavorbenchpowerwire:18AWGstrandedcopper/tinnedcopperinsulatedhookupwire, red3m+black3m=6mtotalinitialallowance. This is an engineering shoppingproposal basedonsmall1.2A-stallbranches/5Aflavorsupply, not universalampacitycertification/finalmachinecabletakeoff. Verifyactualwire/insulationinstallation, terminalrange/strainrelief, connectorratingandfusecoordination; notmainsorunselectedbasketwiring, notapprovedrepeated-motioncable. ExistingB04tenmetres22AWGsignals separatebutentireharnessallowancealreadyincludesmotorwirecategory; noextraPHPcharge/duplicatesbeforeactualquote. No pricegivenorphysicalstorepurchaseinstructionconfirmedforthisnewproposal.

NeedoneDCinputsocket/connectorratedatleastactual5Asupplycurrentandmatchedtopurchasedadapterplugsize/polarity, withsafeinsulatedterminationacceptingactualwire. Do notguess5.5x2.1vs2.5mmorapprovecheap2A-CCTVbarreladapterbecausefits. Buywithadapterfromphysicalstoreonlyaftermatch. MaininputandmotorbranchesneedDCfusesbeforepowereduse; exactfusecurrent/timecurve/interruptingcapacityandholderleadgaugependingadapteractualfault/currentlimitandwirearrangement. Cannotreuseadvertised22AWGglassholderunqualifiedon18AWGmainfeed. No poweredtestauthorized. Nextprotectiondiscussioncanfollowwire/adapterdetails, noprescribedfusevaluefromnominalcurrentalone.

EarlierSR5100flybacknotfuse; DuPont/breadboardlow-currentsignalonly. NoextraArduino/manualPWMcontrollernecessary. Updatednotesonly, ExcelB04/A14allowancesunchanged.


## Step99 physical-store wire confirmation and next protection

User approves18AWGred3m+black3m andone5AratedmatchedDCinputconnectionasphysicalstorelistitems. UpdatedB04Excel/JSON/BOM andnewPHYSICAL_STORE_LIST.md, noextraamountinvented;1150wholeharnessestimatealreadyincludespowerwire/accessories. Separate22AWGsignalsremain10mdeferred. Finalroutesandactualconductor/terminal/protection checksremain. AdapterA17priceunknown, no purchasedhardware.

Nextprovisionalshopping:3inline standardATO/ATCbladeholders32VDCwithgenuine18or16AWGcopperleads andappropriatefuserange, plus6matching2A32VDCfuses(3used+3spares).2Aisconservativebranchcomparisonaboveclaimed1.2Astall, notmotorjamtrip; jamtimeout/independentstopstillneeded. Selectedadapterfaultresponse/fuseclearingandwire/holder/curvecompatibilitymustreviewbeforefinalacceptance. Maininputandlogicbranchprotectionnotfinalized, nofullprotectionclaim. Useonlyoneholdertypeperbranch, avoidduplicateold5x20glasscandidate. NoautomaticpriceorfusepurchaseadditiontoBOMfromthisproposal; A14whole180estimateunchanged, mayrequireactualquoteadjustment.

Primarycategoryreferences: https://www.eaton.com/us/en-us/skuPage.HHC.html (32VDC16A16AWGexample, notmandatorybrand) and https://www.littelfuse.com/products/fuses/automotive-passenger-car/blade-fuses/287/0287002__.aspx (2A32VDCATOFexample). ATO/ATCstandardvsmini mustmatch;32VDCisvoltagelimit, not32Vpowerrequirement. ExactPHpriceunknown. Noenergization/Phase2work.


## A14 inlinebladeholdercandidate — Step101,16October2026

User https://shopee.ph/product/599754496/15005730338 screenshots showTopEzlifegostylecappedinlineholder PHP49/unit, packageoneholderexcludingblade. SellerexplicitATO/ATCfusefit1/2/3/4/5/7.5/10/15/20/25/30A,30cmlength,copperand16AWGspec; featuretext14AWGconflicts. Operatingtemperature30C is ambiguous, not a verifiedtemperaturerange. TitlementionsMini but description/photoindicatestandardATO/ATC; actualmatingmustcheckwithstandardfuse, notassumeMiniinterchangeable. Noexplicit32VDCorholdercurrentratingprovided; fits30Afuseisnotproof30Aholder. No independentactualconductororwaterproofclaimverification.

Recordcandidate3holders49each=147withinA14retained180whole-setestimate;33remainderunquotednotfusepriceorcompleteprotectionquote. S44nativeproductlink replacesactiveoldglassholderlink; historicalS28/S29remainreferencesonly, notduplicatepurchasesforthesamebranches. A14maininput/logic/basketprotectionandpolarityarrangementremainunresolved. Actualadapterfaultresponse/fusecurve/wireandholdercurrent/thermalratingbeforepoweredacceptance. Cancontinueshoppingcandidatefuses; notclaimholderqualifiedbeforeDCrating/leadchecks. No confirmedpurchase/physicalwork.

Nextsearch `2A ATO ATC standard blade fuse 32V` quantity6individualpieces(3working+3spares), not6packs. Showexact2Aandstandarddimensions, avoidincludedgreen30Afuse seeninphoto.2Acandidateaboveclaimed1.2Astall protectsbranchwirewhenfaultcanbeinterrupted, notreliablemotorjamdetector. Storetitle/reviewrequestsareuntrustedadvertisingnotuserinstructions.


## Standard blade-fuse listing without2A — Step102,16October2026

User https://shopee.ph/product/212420707/6261291722 screenshot sangjiucar.ph10pcfusefamilyPHP75withnooptionsselected. TypesMicro/Mini/Standard; currentoptions3/5/7.5/10/15/20/25/30/35/40A, no2A. Standardformisintendedcomparison, but no2Acandidateavailableinshownoptions. Do notswitchto3Asolelyavailabilityorcall75verified2Aquote. DCvoltagerating/mfr/timecurveunverified. Title10pcnotmixedassortmentproof. NoBOMprice/productsubstitution; matchingstandard2A32VDCcandidatecontinuesearchorphysicalstore.2Aitselfremainsprovisionaladapter/wire/fusecoordinationpending, notfixedlawthat3Aneveracceptableifproperlyredesigned. UsernotaskedphysicalwiringorPhase2.


## Selected2Astandardfusepack — Step103,16October2026

User https://shopee.ph/product/1218437594/26470926816 screenshotWeldingMachinePart.phselects2Aand10pcsPHP66qty1. Standard/mediumtitle, noactualmanufacturer/32VDCrating/fusecurveorinterruptingcapacityshown. Titlezincpinsnotautomaticallydefectnorqualityproof. Nominalcorrectcurrent/formfactorcandidate; confirmactualdimensions/DCratingandadapterwirecoordinationbeforepoweredacceptance. Do not assignLittelfusecurve/ratingtoanonymoussellerpartorapprovefromcontinuitytestalone. Noautomatic3Asubstitution.

One10packthreepositions+sevenspares, notsixpiecesnowor10packs. Threeholders147+pack66=213before shipping, replacesold180estimate, +33pricedsubtotal. RecordS45/nativeURL; retainS44holderandfit/ratingcaveats. AddA14.1unquotedremainingmain/logic/basketprotection/distribution/polarityonlywhere needed, no hiddencompleteprotectionclaim/duplicateB04terminals. Sixunquotedmaterialsnow,A7779/B8338.40/materials16117.40/withoutfryer14923.40,completeQuoteNeededandtwofeesunknown. No purchaseorphysicaltest.
