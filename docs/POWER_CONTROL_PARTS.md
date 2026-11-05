**Current B08.1 source override — Step 66, 16 October 2026:** ENG LAB 1-channel 5V selected screenshot PHP49, one module. Replaces the prior Circuitrocks PHP65 reference in the table/BOM. LOW-trigger seller claim; exact board driver/input/reset OFF, insulation and B06 AC-coil inductive/pickup match unverified. Provisional low-voltage test candidate only; HOLD for mains use. Historical Circuitrocks descriptions below are superseded, not extra purchases.

# B06–B09: Power-control parts to list and source

**Current sequence override — Step 15:** Press one flavor button: dispense that packet and enable the thermostatic fryer; wait a configurable warm-up time (initial proposal 300 seconds); run a configurable cooking interval (initial 600 seconds); then lift, drain and flip using position switches, and return. The initial timed sequence reaches basket discharge commands after 15 minutes plus movement/drain time. No extra temperature sensor is required for this timer sequence. Five minutes is a trial setting, not proof that cold oil is ready. Validate warm-up/cooking durations for the actual oil fill, starting conditions, 300 g batch and loading sequence. If potatoes are in the oil during warm-up, they also heat during that period. Keep the manufactured fryer thermostat and verified independent overheat protection; timers do not regulate oil temperature or replace hardware power switching/stop protection. Retain position switches and motor drivers for basket/coil motion. External MAX6675/probe purchases are removed from the current compulsory BOM; earlier references to a temperature gate are superseded.

**PHASE 1: MATERIALS BUYING, Step 20 — 15 October 2026.** The user will assemble the controls with guidance. The user-selected Shopee Single-6L fryer replaces HFRY60SS; seller advertises 2500 W, but actual voltage/nameplate remain unverified. This is a procurement list and functional explanation, not instructions to energize mains wiring. Keep the machine layout unchanged.

**Current procurement override — Step 62, 16 October 2026:** B06 provisional selection is Jayson Electric one CJX2-1810(18A220V), PHP 289, AC-coil advertised 220 V. Seller description now states 50–60 Hz, Ith32 A and one NO auxiliary. This supersedes the DC24V-only B06 selection below. Ith32 A is not established AC-1 switching current; delivered coil rating and heater suitability remain pending. B07/B08/interface/reset/suppression are HOLD for a coherent control/stop revision. The old priced 24 V supply/interface references are conditional, not purchase instructions. No mains layout or final circuit approved.

## What the four groups mean

- **B06 — Normal fryer switching:** One power contactor K1. A contactor is an electrically operated power switch; its coil receives a small control-power supply, and its separate main contacts switch the heater circuit.
- **B07 — Independent emergency power removal:** One power-stop contactor K0 and the reused A09 emergency-stop button. K0 stops heater and motor-supply power through a hardwired circuit. K1 manages normal cooking. These two functions are separate; neither ordinary contactor alone establishes certified safety performance.
- **B08 — Low-voltage control parts:** Interface relay, compatible coil supply, hardware RESET, suppression and control-branch wiring/protection.
- **B09 — Mains installation materials:** Suitable protection, enclosure, DIN rail, covered terminals/earth bar, rated cord/plug/socket and strain relief.

## Detailed listing

LISTED prices were observed. ESTIMATE figures are unverified small-material allowances and must be checked locally. Quote needed means no reliable price for the correct variant was verified. Fees are excluded.

| ID | Item / specification | Qty | PHP price | Role / selection condition |
| --- | --- | ---: | --- | --- |
| B06 | Fryer run contactor K1. Provisional CJX2-1810(18A220V), Jayson Electric one; advertised 220 V AC coil, seller states 50-60 Hz and single/three-phase use. Three main poles, ONE NO auxiliary only. Seller Ith32 A is thermal current, not verified AC-1 heater switching rating. Verify exact coil label/voltage range, heater duty and any needed auxiliary block; dimensions advertised 47x87x76 mm | 1 | PHP 289.00. SCREENSHOT: selected CJX2-1810(18A220V) PHP 289, 16 Oct 2026; delivery extra. PROVISIONAL B06 AC-coil choice, not final heater/control-circuit acceptance | Candidate normal fryer power switch; internal fryer thermostat/cutoff remain. Replaces the old LS/DC24V-only B06 candidate, not an extra contactor. Coil needs a suitable isolated AC-rated interface, not direct Arduino drive. B07/B08 and reset/stop arrangement must be reconciled before purchasing their dependent parts. |
| B07 | Independent power-stop contactor K0. Independent power-stop contactor: exact coil/contacts pending review with provisional B06 AC-coil choice; cover fryer and motor-supply input including inrush. Hardwired emergency stop and deliberate reset; verify auxiliary/load-holding arrangement. Do not assume B06 one-NO auxiliary suffices | 1 | Quote needed. QUOTE NEEDED; HOLD final coil/stop architecture and combined-load match | Removes heater and motor-supply power independently of the Arduino. Mechanical load holding is still required when the basket motor loses power. |
| B08.1 | Arduino-to-contactor relay interface. ENG LAB selected 1-Channels + 5V relay module; seller LOW-trigger, maximum AC250V10A/DC30V10A claims. One-channel board pictured; optocoupler not established. Verify actual driver/input current, startup/reset OFF and mains-to-logic clearances/insulation, AC inductive duty and B06 coil pickup/holding match before any mains use | 1 | PHP49.00. SCREENSHOT: selected 1-Channels + 5V PHP49, 16 Oct 2026; delivery extra. PROVISIONAL low-voltage test candidate; HOLD mains-coil acceptance until board/contact/load checks | Candidate Arduino-controlled switch for B06 contactor coil only, not direct fryer heater switching. Buy one module, replacing old Circuitrocks reference, not both. Relay coil power comes from module supply/driver, not Arduino GPIO. Generic 10A marking and seller LOW-trigger statement do not qualify whole board or guarantee safe OFF. |
| B08.2 | 24 V contactor control supply. Candidate genuine MEAN WELL HDR-15-24, 24 V DC 0.63 A / 15.2 W, DIN rail; capacity conditional on actual two-coil pickup/holding loads and temperature derating | 1 | PHP 1,765.40. PRIOR LISTED price inc VAT; HOLD: only for retained 24 V control arrangement, not automatic purchase with B06 AC coil | Conditional control-supply allowance from previous DC-coil plan. An AC-coil contactor does not require this supply for its own coil. Retain only if finalized independent low-voltage stop/control arrangement needs it; remove/replace once whole B07/B08 design settled. Do not buy both alternative schemes. |
| B08.3 | Hardwired RESET pushbutton. LA38-11BN series, selected green + Self-reset, non-illuminated complete panel pushbutton. Seller advertises 22 mm, 1 NO + 1 NC, spring return on release. Label RESET; use appropriate contact after exact block markings, control-voltage/inductive duty and mounting verified. Generic below10A claim is not a verified mains control rating | 1 | PHP62.00. SCREENSHOT: selected green + Self-reset PHP62, 16 Oct 2026; delivery extra. PROVISIONAL reset-button selection; actual contacts/duty and final stop/reset circuit pending | Provides a deliberate reset request after a cleared stop/power interruption. One button, not an extra flavor/start input or emergency mushroom. Reset must not itself start cooking/motion; final hardwired arrangement provides that behavior. No extra contact block or indicator lamp purchased without need. |
| B08.4 | Contactor coil suppression accessories. Manufacturer-compatible suppression for final AC/DC coil types; check built-in parts first. B06 AC coil needs suitable AC suppression if required, not a plain DC flyback diode. Exact parts/number depend on finalized coil/stop release behavior | 1 | Quote needed. QUOTE NEEDED; buy only missing accessories | Limits coil switch-off voltage spikes. Suppression type affects contactor release time, so a generic diode must not be selected blindly for an emergency-stop circuit. |
| B08.5 | Additional control-circuit wire and fuse parts. Conditional additional control-branch protection/wire; exact control voltages, ratings and lengths after revised coil/interface/stop design. Mains-rated wiring for any AC-coil branch; do not assume A14 low-current holders suitable; reuse rated parts without duplicates | 1 | PHP 150.00. ESTIMATE PHP150; HOLD final control-circuit materials, additional pieces only | Protects and connects the new control-power branch. This is separate from high-current motor wiring already in A14/B04. |
| B09.1 | RCBO if existing supply protection is inadequate. Candidate CHINT NB4LE 2P C16, Type A, 30 mA, 230/240 V, 6 kA, manufacturer code 292721; current/curve/breaking capacity/frequency and isolation suitability depend on actual circuit | 1 | Quote needed. QUOTE NEEDED; need/type to verify at school outlet | Combines overload/short-circuit and earth-leakage protection. If a suitable verified device already protects this circuit, do not buy another automatically. |
| B09.2 | Covered mains enclosure with mounting plate. Candidate approx. 300 x 300 x 150 mm suitable metal/plastic electrical enclosure; confirm component clearances, insulation, splash location and metal bonding | 1 | 800.00. ESTIMATE PHP 500-1200; exact enclosure quote needed | Houses contactors, control supply and protected mains terminals. This is the mains compartment; B03 already budgets the separate low-voltage electronics box. |
| B09.3 | DIN rail and mounting/end-stop kit. 35 mm DIN rail, lengths determined by layout, end stops and mounting hardware; omit rail supplied with enclosure | 1 | 100.00. ESTIMATE PHP 50-150; additional pieces only | Secures contactors/supply/protection in the enclosure. Do not charge for the same mounting hardware again in B05. |
| B09.4 | Two SDE TB-2503 covered 3-pair strips, seller-rated 25 A / 600 V (PHP10 each), plus one Wixim 6-way grounding bar (PHP189). Final conductor acceptance, markings, PE suitability and connection count pending. | 1 set | PHP209 screenshot subtotal before shipping | Connects incoming power and appliance branches securely and bonds exposed metal. Protective earth is never switched by the Arduino, a relay or an emergency stop. |
| B09.5 | Mains cord, matching grounded plug and controlled outlet. Provisional 3G2.5 mm2 flexible copper cable allowance plus genuine matching grounded 250 V plug/socket rated at least 16 A; actual type, length, ampacity and protection must be checked; retain factory fryer cord | 1 | 850.00. ESTIMATE PHP 500-1200; lengths and outlet type pending | Provides a controlled connection for the intact fryer and supply. This is mains wiring, separate from B04 DC harness; no cheap ungrounded or universal adapter is presumed suitable. |
| B09.6 | Mains cable glands, ferrules and identification. Mains-compartment strain relief, appropriately sized ferrules/sleeves and wire labels; only pieces not included with enclosure/other kits | 1 | 150.00. ESTIMATE PHP 100-250; avoid duplicate kits | Keeps cables from pulling out and makes connections identifiable. B04/B05 already cover DC/external sensor pieces; these are additional mains-only parts. |

**Priced B06–B09 component subtotal: PHP 4,424.40, plus 3 unquoted entries.** This includes a proposed dedicated 24 V control supply at the observed RS price; it is not a complete panel price. No outside assembly labor is added.

## Why these ratings matter

The selected Shopee Single-6L is advertised as **2500 W** in the user-provided listing image. Its voltage is not shown. If rated 230 V, the approximate heater current is `2500 / 230 = 10.87 A`; if rated 220 V, it is `2500 / 220 = 11.36 A`. These are conditional calculations, not verified nameplate data. The former Hanabishi 2400 W load is superseded. Confirm nameplate, minimum/maximum oil levels, independent overheat protection, grounding and external switching compatibility before final ratings. A common 10 A Arduino relay board is insufficient as the direct heater switch for these illustrative loads. B08.1 switches only a low-voltage contactor coil. [User-selected product](https://shopee.ph/product/1303238794/40333822650); see [screenshot assessment](FRYER_ASSESSMENT.md).

**AC-1** is a switching category for resistive/low-inductance loads such as a heater. **AC-3** is a motor-switching category. A contactor advertised as “9 A” for a motor can have a different heater rating. Obtain the exact AC-1 rating for the coil variant supplied; do not buy using the large current number alone. K0 also switches a motor power supply with startup inrush, so its suitability requires that load information.

The proposed low-voltage coil is **24 V DC**, not 24 V AC, 220 V AC or a 5 V relay coil. The actual contactor coil voltage determines the required control supply. The LS manufacturer catalog confirms several DC variants; sellers must supply the requested variant and identify the genuine exact order code. [LS manufacturer catalog](https://www.ls-electric.com/upload/customer/download/1416/Metasol_MC_E_1310.pdf).

HDR-15-24 provides 24 V, 0.63 A / 15.2 W. Select it only if the sum of actual coil pickup/holding demand and other connected control loads fits its rating with margin at enclosure temperature. The catalog coil-consumption example is not a measurement of the delivered 24 V variant. Increase supply size if needed. A17 powers the motors; this proposed control supply remains available while K0 has removed motor power. The finalized design must also prevent motion from residual stored energy and safely hold the basket. [MEAN WELL specifications](https://www.meanwell.com/Upload/PDF/HDR-15/HDR-15-SPEC.PDF).

The interface relay candidate is listed at PHP 65 and currently sold out. Verify its actual DC/inductive contact rating and fail-off trigger behavior before using it for a 24 V coil. The earlier PHP 150 module is not selected: its seller text has conflicting contact ratings. Its “30 A” label is not evidence of safe heater switching. [Current interface candidate](https://circuit.rocks/products/5v-10a-1-channel-relay-module-with-optocoupler-no-nc).

**RCBO** means residual-current circuit breaker with overcurrent protection: it covers leakage plus overload/short circuit. **30 mA** is its leakage sensitivity; **16 A** is a separate load-current rating. A normal MCB handles overcurrent but is not a leakage protector. Do not replace 30 mA with 100/300 mA solely for price. The actual outlet supply, frequency, wire/plug ratings and fault level determine the accepted device; C16 is a candidate, not an unconditional prescription. A verified existing suitable protected outlet may eliminate a duplicate RCBO purchase. A separate isolator is additional only if the accepted protection/plug arrangement does not provide suitable isolation. [CHINT manufacturer model/code reference](https://www.chintglobal.com/content/dam/chint/global/product-center/low-voltage/iec/final-power-distribution/rcbo/nb4le/catalog/NB4LE-RCBO-catalog.pdf).

DIN rail is the metal mounting strip for contactors/breakers/supplies. Ferrules are crimped sleeves for stranded wire ends. Glands grip cables where they enter the enclosure. Protective earth connects exposed conductive parts to the installation earth; it must remain continuous during switching. Grounding, covers, strain relief and correct conductor/plug ratings are physical requirements, not firmware settings.

## Economical sourcing without duplicate purchases

Request quotes from a PH industrial electrical supplier for the LS 24 V DC variants and compatible accessories. Marketplace prices mix coil options and do not verify authenticity, so no cheap listing is represented as a confirmed exact-part quote. Avoid premium imported Schneider prices unless the actual local quote is competitive.

A genuine 12 V DC coil alternative might reuse the existing A17 supply and reduce cost, but it requires a checked arrangement that preserves control power during emergency stopping and correctly interrupts motor energy. It is an alternative, not an automatic deletion of B08.2. Do not buy both control-power arrangements.

Reuse A09 E-stop, suitable A14 components and any verified existing school outlet protection. Do not buy two mounting kits if the enclosure includes the rail/plate, two gland sets for the same cable, or new appliance cord when the factory cord is retained. Low-voltage B03/B04/B05 parts and mains B09 parts have distinct scopes.

## Text you can send to suppliers

> Please quote two genuine LS Metasol contactors with 24 V DC coils, three normally-open main poles and one NO plus one NC auxiliary contact. Candidate family MC-9b/MC-12b; supply the exact order code and datasheet showing heater AC-1 rating of at least 20 A at 230 V. One switches a fryer advertised as 2500 W (actual nameplate voltage/watts pending); the other removes the fryer and motor-power-supply input power, so please identify relevant inrush/load limitations. Include compatible coil suppression only if not built in. Quote a suitable manual RESET control and any needed auxiliary blocks separately. No panel-building labor in the materials quote.

This is prepared quotation text; no supplier has been contacted. Do not buy before confirming the actual appliance and motor-supply ratings and reviewing the stop arrangement.

## Your assembly role

You can assemble low-voltage controls with step-by-step guidance in the approved prototype phase and report multimeter/behavior results after each step. Mains mounting/wiring and protective-earth/stop arrangements should be supervised and checked by a qualified electrical instructor or electrician before energizing. This follows the project safety instruction in AGENTS.md; it does not impose a paid assembly contractor. C01 now covers any actually paid review/inspection/help only, and C03 user labor remains PHP 0.

Terminal-by-terminal wiring, software and live tests wait for their approved phases and actual selected part pinouts. No live wiring, installation or flashing has been performed.

## Observed prices

- [Circuitrocks interface board](https://circuit.rocks/products/5v-10a-1-channel-relay-module-with-optocoupler-no-nc): PHP 65, sold out, exact relay/DC rating still to verify.
- [RS Philippines HDR-15-24](https://ph.rs-online.com/web/p/din-rail-power-supplies/1457862): PHP 1,576.25 excluding VAT / PHP 1,765.40 including VAT. Delivery is separate. This is an available price reference, not a claim that it is the cheapest local source.
- Enclosure, rail, terminals, cord/connector, gland and control-wire figures above are explicitly unverified estimates. No exact correct-variant local contactor/RCBO/reset/suppression prices have been verified.


## B06 shopping focus — Step 56, 16 October 2026

Search `LS Metasol MC-9b contactor 24V DC coil` or `contactor 24V DC coil AC1 20A heater`. These are comparison searches, not exact approved order codes. Quantity one for B06 K1; B07 is a separate stop function and its selection remains pending.

Verify the exact supplied coil is **24 V DC**, not 24 V AC/220 V AC. Ask for the nameplate/datasheet with main contacts rated at least 20 A **AC-1 at 220–230 V** for the proposed heater switching, three normally-open main poles and preferably the planned one NO plus one NC auxiliary arrangement (or compatible blocks if required). Existing candidate family is not a guarantee that every similarly named listing has these ratings. Confirm actual fryer nameplate when received; currently 2500 W is seller-advertised only.

A contactor has separate control and power ratings: 24 V DC operates its electromagnetic coil, while rated main contacts switch the fryer's AC supply. It does not convert 24 V into mains power. Arduino signals need the separate B08 interface, not a direct coil connection. Keep the manufactured fryer thermostat/overheat protection intact; K1 provides normal cycle permission, not temperature regulation.

Do not reject or accept a product solely on an advertised 9 A/18 A headline; distinguish motor AC-3 from heater AC-1 ratings. Seller current claims, exact variant, coil consumption, suppression and authenticity need evidence. No current PH price verified for the requested variant; B06 remains Quote needed. No terminal wiring or mains energizing instructions provided in Phase 1.


## B06 broader marketplace searches — Step 57, 16 October 2026

The user found no results for the LS-specific search. LS is a candidate brand, not mandatory. Try `CJX2Z 24V DC coil contactor` or `CJX2 3210Z DC24V` as shorter searches. Search results surfaced these Shopee PH comparison leads:

- https://shopee.ph/product/750550293/26089306360 — title CJX2-3210Z DC Magnetic Contactor Coil 12V 24V.
- https://shopee.ph/product/1201429789/25283305784 — title DC Contactor CJX2-3210 / LP1-3210, multiple coil-voltage options.

These are discovery leads only: no current selected-variant price, actual 24 V DC coil, genuine manufacturer rating, AC-1 heater capability, complete-contactor supply or required auxiliary contacts verified. Titles mixing AC/DC are ambiguous; read the coil label, not just title. Do not presume 3210 provides the planned NC auxiliary contact. A missing auxiliary block must be specified/quoted if required by the final circuit.

No replacement has been added to the approved purchase BOM, and B06 stays Quote needed. Ask for selected DC24V variant and complete device label/datasheet. Proposed AC-1/load, control supply/interface and stop arrangement still require the same compatibility checks.


## CJX2-1810 listing review — Step 58, 16 October 2026

User listing https://shopee.ph/product/1253203453/27004405033 (simple.ph) shows CJX2-1810, JR28-25 overload relay 9–13 A, and set options. Screenshot price PHP 210–408 is a range with no variant selected; not a verified contactor price. Shipping says pre-order ships in 20 days despite stock text.

Pictured coil label appears to show mains voltage with 50 Hz marking, indicating an AC-coil pictured version, not evidence of the planned 24 V DC coil. Exact voltage/coil/50–60 Hz compatibility needs clearer supplied-part data. Do not assign DC24V based on the CJX2 model family. Visible 13NO/14NO identifies an auxiliary NO pair; no NC auxiliary confirmed by this photo. Exact AC-1 rating/manufacturer/datasheet not established.

Not accepted as current B06 without a documented suitable DC24V variant and main/auxiliary/load ratings. Do not order the JR28-25 overload relay or the combined set solely because grouped in this listing; that does not establish the fryer safety/protection requirements. An AC-coil architecture would need a deliberate redesign and review of B08/stop/power arrangements, not merely a coil substitution.

B06 remains Quote needed; no supplier/price inserted in purchasing Excel.


## CJX2 220 V AC listing — Step 59, 16 October 2026

User link https://shopee.ph/product/777946608/42206576962, seller Jayson Electric one, advertises 220 V AC contactors: options CJX2-1210(12A220V), CJX2-1810(18A220V), CJX2-3210(32A220V). No option is selected; PHP 259–529 is a family range, not an exact quoted price. One disabled variant label conflicts with pictured model; do not infer exact product rating from it.

This is not a drop-in match for the current B06 DC24V coil arrangement. A documented correctly rated 220 V AC coil contactor can switch the fryer in an alternative reviewed mains-coil architecture; it is not inherently unsuitable merely because its coil is AC. That change would affect B08 interface contact ratings/insulation and control-power design plus B07/A09/reset/stop arrangements. Do not retain/buy the dedicated 24 V coil supply automatically if it is removed by a finalized alternative. No architecture change approved/implemented by this product inquiry alone.

Exact manufacturer, coil label/frequency, heater AC-1 rating, necessary auxiliary contacts, genuine supplied product and fryer nameplate still need confirmation. Headline 12/18/32 A may be a motor rating. Do not select 32 A solely because it is the highest number. Current BOM remains DC24V and B06 Quote needed; no price/link entered as accepted material.


## Clarification: 24 V DC coil is a proposal, not a feature requirement — Step 60

User challenges availability and need. The automatic-cycle requirement is an appropriately rated controller-operated power switch for the fryer. A contactor is a practical implementation; an exact LS brand or DC24V coil is not mandatory. The original low-voltage coil proposal kept contactor control wiring at low voltage, but its sourcing difficulty justifies comparing a documented locally available AC-coil arrangement.

A 220–230 V AC-coil contactor is a legitimate alternative when its voltage/frequency and heater main-contact ratings match actual supplies/loads. Example manufacturer evidence: https://www.se.com/au/en/product/LC1D09P7/contactor-tesys-d-3p3-no-ac3-ac3e-0-to-440v-9a-230vac-50-60hz-coil/ . This is architectural evidence, not a requirement to buy that brand or assign its ratings to generic CJX2 listings.

The coil voltage does not change how hot the fryer cooks. It determines the voltage required to operate the contactor's magnetic switch. The controller still needs a suitable isolated interface; no direct mains/coil connection to Arduino. Keep internal fryer thermostat/cutoff.

Next procurement review can use common AC-coil candidates rather than requiring further searches for DC24V. Obtain exact supplied device data, selected price, AC-1 rating, coil frequency/voltage and auxiliary arrangement; review B07/B08/reset/E-stop ratings together. If the complete selected arrangement no longer uses a dedicated 24 V coil supply, remove B08.2 and its obsolete accessories instead of purchasing both architectures. Do not promise savings or remove control-power parts until the alternative is concretely specified. Mains control components remain enclosed and reviewed by qualified school/electrical support; firmware cannot replace stop/protection functions.

No wiring details or physical energizing here. Existing Excel is unchanged pending a coherent replacement architecture; the previous mandatory-sounding DC24V shopping restriction is withdrawn.


## Variant to inspect first — Step 61, 16 October 2026

For the Jayson Electric one listing, **CJX2-1810(18A220V)** is a provisional comparison candidate, not an approved purchase or demonstrated sufficient rating. No supplied model datasheet is available; 18 A headline alone does not establish heater rating. Do not claim 12 A is too small based on comparing an AC-3 headline to heater current, or that 32 A is automatically required.

Before checkout ask for the actual coil label documenting suitability for the intended 220–230 V **60 Hz** supply (or appropriate 50/60 Hz voltage ratings), AC-1 rating at least 20 A for proposed heater switching, and exact auxiliary arrangement. Visible 13NO/14NO suggests only NO is shown; a needed NC block must be separately identified, not assumed present. Philippine frequency guidance: https://corporatepartners.meralco.com.ph/media/download/2704 . Manufacturer coil-frequency guidance: https://www.se.com/es/es/faqs/FA137683/ . A coil with only a 50 Hz label is not automatically approved for 60 Hz at the same voltage.

Select the option to obtain its exact price and send nameplate/specification evidence. No exact price or completed AC-coil control design available; B06 and dependent control BOM remain unresolved. Quantity one for B06 only; do not order B07 or extra auxiliary parts without matching the complete arrangement.

### Newly supplied evidence, Step 62

Selected CJX2-1810 price289 replaces B06 unknown; dimensions seller47×87×76mm. Description states18A threephase motor figures, Ith32A, oneNOaux, Ui690VAC and50–60Hz; do not recast these as verified20A AC1 orNCaux. Current price planning adds289, but prior24V supply/interface allowances are held until complete reviewed revision. No automatic same-model B07 purchase, AC suppression parts or mains-control buttons assumed suitable.


## B07 shopping focus — Step 63, 16 October 2026

B07 K0 is the independent contactor removing the fryer's and motor supply's AC input power through the hardwired stop/manual-restart arrangement. B06 K1 provides normal fryer cycle permission. Different functions are budgeted separately; a second ordinary contactor alone does not establish certified safety performance, monitored contacts or a validated stop function.

For comparison, reuse the Jayson Electric one listing https://shopee.ph/product/777946608/42206576962 and inspect CJX2-1810(18A220V) as a possible additional unit; do not assume it is sufficient because provisionally recorded in B06. B06's PHP289 screenshot is a reference for the identical variant only, not a finalized B07 quote/selection. No need to search a rare DC24V coil just for this comparison. Exact B07 coil/control-voltage arrangement remains subject to the whole A09/B08/reset review.

B07 has a different load: fryer plus motor-supply input current and startup surge. A17 supply remains unselected pending basket motors. Its input/inrush data and contactor making/breaking capacity are needed before choosing B07; do not compare the supply's 12V output amps directly to AC mains contactor current or automatically choose32A to compensate for missing data. A supply's momentary inrush is not its continuous input rating.

[MEAN WELL manufacturer guidance](https://www.meanwell.com/qa.aspx?c=9) documents switching-supply startup inrush; it does not give the unselected A17's current or establish a particular CJX2's suitability. Necessary auxiliary contacts/blocks, manual reset and supplied E-stop's ratings remain unresolved. No blanket approval to route mains through A09. Mechanical basket retention and stored DC energy require separate attention; opening AC input is not instant proof that all motor energy has vanished.

Keep B07 **Quote needed / procurement HOLD** until motor-supply and stop arrangement selected. No additional unit added or ordered by opening this shopping step, and no changes to B08.2 conditional supply allowance yet.


## B08.1 search for current AC-coil candidate — Step 64, 16 October 2026

First compare `5V 1 channel relay module optocoupler Arduino` or `5V relay module 1 channel 250VAC`. Quantity one module initially for normal K1 permission. No exact marketplace board approved by this search. An assembled module with a transistor driver avoids buying an unrelated bare relay/socket and trying to operate its coil from an Arduino pin.

Needed: 5 V module power, compatible low-current 5 V logic input (VCC/GND/IN typically, confirm actual board), and main relay contacts documented for the contactor's AC inductive coil load, including pickup demand. Verify whole-board mains-to-logic insulation/clearance, covered installation, terminal ratings and OFF behavior during reset. Optocoupler text or a 10 A/250 VAC relay stamp alone does not establish complete module suitability or galvanic isolation after grounds/jumpers are connected.

The module does **not** switch the roughly 2500 W heater directly. Its contacts operate only the provisional 220 V AC contactor coil; the contactor's power contacts carry heater current. Coil voltage remains separate from module control power. Module relay coil current comes from its supply/transistor circuit, not an Arduino GPIO directly.

[DFRobot DFR0017 manufacturer example](https://wiki.dfrobot.com/dfr0017/) illustrates 5 V logic-controlled relay architecture with AC-rated contacts. It is not a selected PH quote, not an inductive rating assigned to any blue marketplace relay and not the different low-voltage-only DFR0473 product. Exact supplied B06 coil pickup/holding data and final independent stop/reset architecture remain pending.

Prefer a documented suitable module in a covered mains compartment. If the available board lacks adequate ratings/separation evidence, compare a documented interposing relay plus finger-safe socket and matched low-voltage driver instead; do not buy both architectures. B08.1 old PHP65 sold-out reference remains HOLD until an actual candidate is assessed. No price/part changes or wiring steps from this shopping discussion.


## B08.1 ENG LAB candidate — Step 65, 16 October 2026

User listing https://shopee.ph/product/1021339444/22577819886, ENG LAB.ph, offers 1/2/4 channels and5/12/24V supply/coil choices. Neither channel norvoltage is selected in screenshot; PHP49–199 is a family range, not a confirmed exact5Vsinglechannel price. Inspect **1-Channels +5V**, quantityone.

Seller description advertises low-level trigger and maximumAC250V10A/DC30V10A. Low-trigger means commandedLOW energizes relay; actual input-current/threshold, startup/reset behavior and fail-OFF remain to test. Claimedmaximum contact figures do not establish an ACinductive coil duty or board mains-to-logic separation.

Family photo shows different1/2/4channel layouts. Do not transfer optocoupler or jumper features from a multi-channel version to the one-channel board. Exactvariant front/back photographs and circuit/relay identification are needed to review driver/insulation/contacts. No optocoupler claimed for the selected-but-not-yet-shown exact version. NeedB06 actualcoil pickup/holding load and suppression before approving mains-coil service.

This is a comparison candidate only. Does not directly switch the fryer heater. B08.1 priorPHP65 reference remains HOLD; no selected-price replacement or accepted purchase in Excel yet.

### B08.1 selected screenshot Step66

Source https://shopee.ph/product/1021339444/22577819886 . Selected1-Channels and5V PHP49. No optocoupler established from exactonechannel photo. Budget reductionPHP16, not proof of board suitability. Board may require replacement if mains ratings/separation inadequate. B07/B08.2 stop/control architecture still pending.


## B08.2 purchasing decision — Step 67, 16 October 2026

**Skip buying B08.2 now.** It is the previous dedicated24VDC contactor-control supply, not A17 motor power or A13 5V converter. Current B06 candidate is220VAC coil; B08.1 candidate is5V module. Neither calls for this24V supply. No other finalized24V load has been selected.

B07 emergency-stop/reset architecture is not finalized, so keep B08.2 HOLD rather than pretending its possible independent low-voltage control need is resolved. ExistingPHP1765.40 remains a conditional planning allowance inside the subtotal, not a purchase recommendation or current mandatory requirement. Remove it when the finalized B07/B08 arrangement confirms no24V control circuit; replace rather than duplicate if a different supply is chosen.

A17 proposed12V supply plus A13 5V converter still serve the motor/controller arrangement; deferringB08.2 does not remove them. No new supplier search or purchase needed forB08.2. Next independent procurement discussion can beB08.3 reset button, with final contact duty/voltage dependent on stop circuit.


## B08.3 manual RESET shopping — Step 68, 16 October 2026

Search `LA38 22mm momentary push button 1NO blue non illuminated` or `22mm spring return push button normally open`. Quantity one complete panel button including contact block, not head only. Blue is suggested to distinguish RESET from the red emergency-stop and flavor controls; label clearly RESET. Green/white can be compared if blue unavailable; color does not establish electrical function/rating.

Required mechanical form: momentary/spring return (releases when finger removed), at least one normally-open contact, non-illuminated to avoid a lamp supply requirement. A complete1NO+1NC assembly can be acceptable if exact block ratings/fit match, but do not buy extra blocks without need. No latching/selector/emergency-mushroom substitute just because a title says reset.

Purpose is deliberate restoration of operating permission after a cleared stop/power interruption; reset must not itself initiate cooking/motion or bypass a still-active stop. Exact hardware circuit, monitoring and behavior remain for the finalized reviewed stop arrangement. No assertion that a button alone implements this behavior.

Actual contact duty depends on selected control voltage and load. For AC-coil switching/control seek a documented appropriateAC15/inductive rating; a generic10A resistive claim is not enough. If the final reset loop is low-voltage, use corresponding documented rating/minimum load. Do not presume the earlier20PHP flavor button or unverifiedA09 block qualified for mains. Actual panel hole/grip dimensions, rear clearance and protected installation must fit.

[Manufacturer example of a22mm spring-return1NO complete button](https://www.se.com/us/en/product/XB5AA31/push-button-harmony-xb5-plastic-flush-green-22mm-spring-return-unmarked-1no/) illustrates the type only, not a mandated brand/color or verifiedPH quote. B08.3 remains Quote needed until a specific complete unit and price are assessed. No supply/wiring instructions, physical steps or phase transition.


## B08.3 LA38 candidate — Step 69, 16 October 2026

User listing https://shopee.ph/product/777946608/42354881235, Jayson Electric one. Screenshot has red/green/yellow choices and Self-reset/Self-locking options, none selected; PHP62–81 family range, not an exact chosen price. Seller describes22mm and oneNO+oneNC contacts, generic below10A claim, and explicitly defines self-reset as spring return on finger release.

Inspect **green + Self-reset**, quantityone completebutton. Blue is not offered in the screenshot; green is acceptable for the proposed mechanical form when clearly labeled RESET. Do not choose Self-locking, which stays pressed until another press. Seller oneNO+oneNC satisfies the proposed contact-form category, not final electrical approval. Actual contact markings, suppliedassembly, mountinghole/grip/clearance and control-circuit duty need confirmation. Generic10A claim lacks voltage/utilization information and does not establish AC15/inductive mainscontrol rating. Do not claim safety positive-opening from this reset listing.

Pending selected exactprice and whole stop/reset voltage/load arrangement, B08.3 remains Quote needed and currentExcel unchanged. Candidate link saved here; no additional head/contactblock or duplicated ordinary startbutton added.

### B08.3 selected-price update Step70

User selectedgreen +Self-reset PHP62 qtyone, source https://shopee.ph/product/777946608/42354881235 . This supersedes B08.3 QuoteNeeded status in earlier discussion; exact electrical contact duty and complete reset circuit remain provisional. No latchingbutton, lamp or extra block added.


## B08.4 AC-coil suppression shopping — Step 71, 16 October 2026

B08.4 reduces switch-off voltage spikes from contactor coils. For provisional B06's AC coil, search `CJX2 220V AC coil surge suppressor` or `contactor RC suppressor 220 240V AC`. Compare a documented complete accessory compatible with the exact contactor/coil; a physically similar snap-on part for another brand is not automatically interchangeable.

RC means resistor plus capacitor in a suppression network. A documented appropriately rated varistor/MOV accessory can be another option; choose one validated arrangement, not both automatically. Manufacturer reference https://www.se.com/in/en/product/LA4DA1U/tesys-d-suppressor-module-rc-circuit-110-240-v-ac/ illustrates ACcoilRC use, not a part verified to fit this genericCJX2 or a PH price quote.

Initial counting: one appropriate accessory for B06 only if a required suitable suppression network is not already incorporated. B07 remains unselected, so its accessory type/quantity cannot be finalized; existing B08.4 quantityone set is an allowance, not exactlyone generic module guaranteed to cover both coils. Ask seller whether built-in suppression exists and request a compatible accessory/datasheet. Do not guess resistor/capacitor/MOV values, clamping voltage, coil energy or continuous rating from the220V title.

A plain DCflybackdiode is not the chosen suppressor for an ACcoil. A15's lowvoltage ceramic/electrolytic capacitors are not direct mains suppressor replacements. Prefer an appropriately insulated enclosed accessory rated for this coil application, not an exposed generic snubber board whose mains safety is unknown. Suppression can alter dropout time; B07 stop behavior requires review. [Schneider explanation](https://www.se.com/ca/en/faqs/FA102916/) shows this tradeoff without assigning exact timings to the generic device.

B08.4 remains Quote needed until a compatible exact accessory and need are established; no new price or Excel purchase item inferred. No connection instructions or live testing in Phase1.


## B08.4 search clarification — Step 72, 16 October 2026

User reports searches show the same contactor. Do not buy another contactor for B08.4: B06 is the switching device, B08.4 is a separate compatible coil-suppression accessory only if needed. Earlier search wording returned the main device and was not sufficient to identify an accessory. No working exactPH accessory listing established.

Stop the current accessory search rather than substitute an unverified generic part or duplicate B06. Keep B08.4 pending supplier/actual-coil information. Ask the contactor supplier whether this exact product already includes suppression and, if not, whether it has a documented compatible220VAC coil accessory. This prepared question is not a sent message. No paid inspection/supplier contact or new safety hardware automatically added.

Pending is not an engineering decision that suppression is unnecessary; it prevents an unsupported shopping instruction. Existing QuoteNeeded allowance and final coil/stop review remain. Subsequent Phase1 B08.5 procurement can continue independently within its conditional scope.


## B08.5 additional control wire/protection — Step 73, 16 October 2026

B08.5 is a conditional allowance for **additional control-branch** fuse/holder and wire not already provided by other items. It is not a requirement to buy another22AWG bundle or repeatA14 fuse packs. User B04 already specifies10m of22AWG fixed low-current signal wire. A14 holds conditionalDC protection/terminals. B09 covers mainAC wiring/protection.

Under the developing ACcoil option, control-branch wiring/protection must be rated for the actualAC circuit, coil pickup/holding current, conductor installation and availablefault current. Do not extend the22AWG low-current shopping instruction to ACcoil wiring automatically, or assume the advertised22AWG glass-fuse-holder candidate is appropriate. No exactgauge/fuseamperage/curve can be finalized without the coil/control andB07 arrangement. Existing fuses in properly rated supplies/other devices do not automatically establish controlbranch protection.

**Purchasing decision: no additionalB08.5 item to buy now.** KeepPHP150 as a labeledconditional planning allowance until a complete circuit/cable takeoff identifies missing parts. Reuse only suitable rated existingpieces and removeoverlap when itemized. Do not report this allowance as a verified quote or savings. NoExcel mutation required becauseB08.5 alreadyHOLD. NextgroupB09.1 is supply/outlet protection; actualschooloutlet protection should be assessed before buyinganotherdevice.


## B09.1 supply protection shopping — Step 74, 16 October 2026

RCBO means residual-current circuit breaker with overcurrent protection. It combines overload/short-circuit protection with earth-leakage detection; a plain MCB lacks leakage detection and a plain RCCB/RCD does not by itself provide the same combined overcurrent function.

For comparison only, search `RCBO 2P C16 30mA Type A 230V 60Hz` or `CHINT NB4LE 2P C16 Type A 30mA`. Initial candidate criteria remain230/240VAC,60Hz or50/60Hz, TypeA residual detection,30mA sensitivity and suitable short-circuit breaking capacity (existing6kA planning target), quantityone **only if needed**. C16 is a preliminary comparison rating, not an approved breaker rating for unverified site wiring, supply topology, plugs, actual fryer+PSU load or fault level.

Do not choose a higheramp rating to avoidtripping. TypeA leakage waveform category is different from curveC or16A rating;30mA is leakage sensitivity, not load capacity. Do not substitute100/300mA because cheaper. Verified existing suitable outlet/circuit protection may eliminate duplicate purchase. Have school electrical staff identify actual circuit protection, earthing and supply arrangement before deciding; do not open a live panel or assume a TESTbutton alone establishes all suitability.

Current manufacturer primaryreference: https://www.chintglobal.com/in/en/products/low-voltage/iec/final-power-distribution/nb4le.html . RefreshedcatalogURL https://www.chintglobal.com/content/dam/chint/global/product-center/low-voltage/iec/final-power-distribution/rcbo/nb4le/catalog/NB4LE-RCBO-Catalog.pdf . Earlier lowercasecatalogURL currently404; updateS14 nativeworkbooklink on nextauthorizedexport. Manufacturer family data do not establish actualmarketplace variant/current price or the old exactordercode's currentavailability.

B09.1 remains QuoteNeeded and conditional. No currentPHprice verified, no specificunit accepted, no construction or physicaltest. Sendcandidate listing/nameplate for review; no automaticneed to buy thisifverifiedschoolprotectionadequate.


## B09.1 TAXNELE TX63LE candidate — Step 75, 16 October 2026

User https://shopee.ph/product/277704323/14295512771, sellernewtaxnele.ph. Screenshots showTX63LE, claimed2P230V30mA,6kA, combined residual/overcurrent/short-circuit protection, IEC/EN61009-1 andCE claim. Mainphoto displays16A and50/60Hz but no currentoption selected; PHP347–388 family range, not confirmed16Aprice. Description currentlist omits16A despite option/photo; actualselectedunit documentation needed.

The leakage waveform category **TypeA** is not established. Seller fieldType:TX63LE is a model field, not TypeA proof. Do not infer TypeA or TypeAC from unreadable tiny symbol or generictitle. CE/standardtext is a seller claim, not independently verified approval/performance. Need exactvariantdatasheet/nameplate confirming category, tripcurve,60Hz, suitable voltage/breaking capacity and intended supplyconnections.

Pictured L/N terminal markings mean exactpole/neutral behavior must fit actualsite topology; do not assume all productsadvertised2P are equivalent two-protected-poledevices. Schoolqualifiedreview of outletprotection/earthing/site needed beforebuying; suitableexistingprotection may eliminate purchase. Select16Aonly forcomparison, not finalapproval; neverchoose63A merelytitle says63A. Do notsubstituteTypeAC or100/300mA to getacheaper/foundlisting.

B09.1 remainsQuoteNeeded/currentCHINTcandidate unchanged, not acceptedreplacement orcurrentprice. Candidate evidence saved. Shopee direct page inaccessible. Manufacturer page https://www.taxnele.com/product/product-91-932.html independently located and read: it repeats the TX63LE 2P, 30mA, 6kA and combined-protection specifications, but does not identify Type A residual-current detection. This corroborates published specifications, not independent product testing. No Excel mutation or physical test.


## B09.1 CHINT NXBLE price comparison — Step 76, 16 October 2026

User screenshot https://shopee.ph/product/615190079/29421243173 advertises Type A, 30mA and PHP798–1865 across current and pole options, with none selected. This is a family price range, not a confirmed 16A/2P quote or a verified typical Philippine market price. Main image shows a multi-pole unit and cannot establish the price or ratings of the required candidate. Select 16A + 2P Type A only for a comparison quote; final current/pole selection still requires actual load, site topology and existing protection review. Do not buy a 3P/4P variant for the pictured appearance or choose a larger current for availability.

CHINT manufacturer NXBLE-63 catalogue explicitly includes Type A variants, but this does not authenticate this seller's delivered unit or confirm this exact listing variant: https://www.chintglobal.com/content/dam/chint/global/product-center/low-voltage/iec/final-power-distribution/rcbo/nxble-63/catalog/NXBLE-63-RCBO-catalog.pdf . Direct Shopee page inaccessible. A charging-station marketing title does not establish that EV-specific hardware is required for this machine. Avoid treating PHP1865 as a mandatory project expense. Existing suitable school circuit protection may remove the need for a duplicate device, subject to qualified review. B09.1 and workbook remain unchanged/Quote needed until a specific variant and need are confirmed.


## B09.3 mounting rail shopping — Step 79, 16 October 2026

User elects to defer B09.1 purchasing and continue to B09.3. This defers selection, not a finding that electrical protection is unnecessary; retain B09.1 conditional/Quote needed.

B09.3 is the metal mounting rail that holds compatible contactors, breakers and terminal blocks inside the mains enclosure. Search `DIN rail 35mm 7.5mm slotted steel` (TS35/TH35 top-hat profile), plus `DIN rail end stop 35mm`. Provisional shopping quantity: one 1-metre rail to cut into enclosure-sized sections, and four compatible end stops for a possible two-row arrangement. Actual rail length, end-stop count, fixing screws and component clip compatibility depend on the enclosure/layout; do not order duplicates if supplied with enclosure. One metre is stock length, not one metre to fit uncut inside the planned box. Generic suitable rail is acceptable; Phoenix Contact manufacturer reference verifies profile category only, not a required brand or Philippine price: https://www.phoenixcontact.com/en-us/products/din-rail-ns-35-75-perf-1950mm-5406365 .

Existing PHP100 whole kit allowance remains an estimate, not a quote for the provisional quantity. No workbook edits, purchases, cutting or assembly performed.


## B09.3 ChaoMai rail candidate — Step 80, 16 October 2026

User screenshot https://shopee.ph/product/1575869610/41015518424 selects 50cm at PHP49, quantity one, seller ChaoMai. Image resembles slotted top-hat DIN rail, but visible screenshot does not confirm 35mm width or 7.5mm height, material or thickness. C45 guide-rail thumbnail is not a dimensional specification. Accept as a candidate pending 35×7.5mm dimensional evidence and component clip compatibility.

Two 50cm pieces would provide the earlier provisional 1m stock allowance at PHP98 before shipping. This is not a final measured requirement or instruction to buy two before enclosure layout/included rails are checked. Four end stops and fixing screws remain separately unquoted/not shown included. The existing PHP100 complete-kit estimate cannot be represented as a confirmed rail-plus-end-stop price; no workbook change until dimensions/quantity and remaining accessory costs are settled. No new exact supplier price for the complete kit, no purchase reported or physical work.


## B09.4 covered terminals and earth bar — Step 81, 16 October 2026

User proceeds after rail candidate; dimensions/rail end-stop pricing still pending. B09.4 provides secure mains conductor connections and protective-earth distribution. Practical search candidates: `covered terminal block 25A 600V 6 way` (one strip provisionally) and `earth ground terminal bar 6 way` (one bar provisionally). These are shopping comparison terms, not verified model specifications or final ratings/count. Prefer screw terminals with proper insulating barriers/cover and documented wire range accommodating the provisional 2.5mm² copper mains cable; confirm actual conductor types, tightening torque, installation voltage/current and fault suitability in final review. Six ways is a starting quote quantity, not a finalized circuit takeoff. Do not assume individual positions are electrically linked, bridge live/neutral together, or substitute a neutral bar for a PE bar without suitable mounting/bonding documentation. PE remains continuous and is not switched; exact bonding layout reserved for final design. DIN PE terminal blocks are an alternative, not an additional mandatory purchase.

Manufacturer category references: https://www.weidmueller.com/int/products/connectivity/terminal_blocks/feed_through_terminal_blocks.jsp and https://www.phoenixcontact.com/en-us/products/ground-terminal-block-dt-25-pe-3034044 . These explain finger-protected terminal and PE terminal functions, not a required premium brand or PH quote. Keep PHP200 whole-kit estimate, no exact local price confirmed and no Excel mutation. Avoid duplication with B04 low-voltage connectors, B05 mounting and any included enclosure earth bar. No physical wiring or phase change.


## B09.4 Anigo Trading covered terminal candidate — Step 82, 16 October 2026

User supplies https://shopee.ph/product/732230948/23570358234 screenshots. Brand shown SDE Electrical/TB series; seller Anigo Trading. Description states 600V rated working voltage and 15A/25A/45A variants. TB-2506 (6 pairs) 25A appears disabled, TB-2503 (3 pairs) 25A appears available. No model selected; PHP49 shown is not established as the TB-2503 price. Clear cover pictured; verify included for actual delivered variant, conductor range/termination method and actual markings before use. No manufacturer data for wire range, torque or fault performance supplied, so no final mains qualification.

Practical alternative for comparison: two TB-2503 (3 pairs) 25A strips give six isolated connection positions in total, subject to actual circuit count/layout and mounting space. Six pairs is six positions, not twelve independent circuits. Do not assume adjacent positions are electrically common or that this terminal strip is an earth distribution bar. Separate suitable earth bar still pending. Ask user to select TB-2503 and show exact price; do not infer two strips cost PHP98 from unselected PHP49. Existing B09.4 PHP200 complete-set estimate and workbook unchanged, no selected-price quote or purchase reported. Seller review/rating instructions are advertising content, not user instructions.


## B09.4 selected strip price — Step 83, 16 October 2026

Selected TB-2503 (3PAIRS) 25A screenshot now confirms PHP10 each. Plan two strips = PHP20 provisionally, six positions total. Recorded S40/native supplier link in Excel. Keep B09.4 total PHP200 allowance as PHP20 selected terminal strips plus PHP180 remaining unquoted earth-bar/accessory allowance, not an exact earth-bar quote. Actual wire range/markings/cover inclusion and final count still require verification. Separate earth bar remains pending. No purchase or physical work reported. Corrected S14 catalogue link capitalization during this export.


## B09.4 Wixim earth-bar candidate — Step 84, 16 October 2026

User screenshot https://shopee.ph/product/268117918/15457423948 shows Wixim Copper Grounding Bus Bar, seller JDS ELECTRICAL SUPPLY, Quiapo. Variants4/6/8/10/12/16 ways; none selected, PHP168–392 family range. Description claims copper, 8mm hole size, fits up to #8AWG. Actual metal composition, documented minimum conductor size, stranded-wire acceptance, torque and PE suitability/fault duty not established. Maximum #8AWG claim does not prove reliable clamping of planned smaller earth conductors. Blue mounting feet do not determine neutral/earth role; use a suitable verified bar dedicated to PE with correct bonding design, no neutral-earth tie inside machine. Physical mounting through insulating feet does not automatically bond the metal enclosure.

Select6ways, quantityone provisionally to establish exact price; final count depends PE takeoff and any enclosure-included bar. Candidate matches intended category, not unconditional mains acceptance. Do not assign PHP168 to6way from unselected range, and do not assume it fits remaining PHP180 allowance. Keep B09.4 PHP200 planning allowance including PHP20 terminal strips and unquoted remainder until exact earth-bar price available; workbook unchanged. No purchases, physical wiring or Phase2 work reported.


## B09.4 selected earth bar — Step 85, 16 October 2026

Wixim6ways selected screenshot confirms PHP189, quantityone. Two TB2503 strips PHP20 plus earthbar PHP189 = PHP209 before shipping. Replaces prior PHP200 whole-set estimate and removes its artificial PHP180 remainder. Actual supplied mounting pieces/any missing hardware remain to itemize without duplicating B05/B09.6. S41 source and native link added; S40 terminal link retained. Earth conductor range/clamping and actual PE suitability/bonding still pending; no neutral-earth link implied, no purchase/physical installation. Updated priced totals: A PHP8768, B PHP8338.40, materials PHP17106.40, without fryer PHP15912.40. Four material quotes plus two fees remain unknown.


## B09.5 mains connection shopping — Step 86, 16 October 2026

User proceeds to B09.5 after selected B09.4. Plan machine incoming flexible cable and one grounded plug plus one controlled grounded socket for the intact fryer; retain fryer factory cord/plug. Search `3 core 2.5mm2 flexible copper cable with earth` (3G2.5), `grounded plug 16A 250V`, and `grounded socket outlet 16A 250V`. These are provisional comparison specifications, not acceptance for unknown total input current, installation conditions or plug shape. Three cores means two supply conductors plus protective earth. B04 22AWG low-current wire is not substituted for mains cable. Actual cable length measured from placement, no invented per-metre quote or mandatory stock length; socket must mate properly with factory fryer plug and machine plug with home outlet while preserving earth. Fryer has not arrived, so plug/socket geometry selection can wait. No universal adapter/ground-pin removal or household extension-strip substitution.

Manufacturer reference example only: OMNI WGD-402 is published as grounded duplex16A250V at https://www.omniphilippines.com.ph/product/wgd-402/ . Not selected: unknown fryer plug geometry, no matching enclosure/plate acceptance, no need for duplex specifically. Do not infer manufacturer endorsement of unrelated sellers. Mains work needs qualified electrician review before energizing; higher marked cable/plug ratings do not establish home circuit suitability. B09.5 PHP850 set allowance remains estimate; no workbook update or physical work. Next B09.6 covers only additional strain relief/termination/identification pieces.


## A17 physical-store purchase — Step97,16October2026

User explicitly says to list12V5A60Wadapterforphysicalstorepurchase andknowswheretobuy. Qtyone, no price/store name invented, no furtheronlinelisting needed. Regulated12VDC5Acontinuous60Wfactory-enclosed withproperACinput/protection andmatchedratedDCconnector/polarity; suitableACcordincludedorpricedseparatelyifneeded. It remainsfinalflavor/control supply, notbasketorheaterpower. Checklabelandlaterloadresponse; userinstructionisnotaconfirmedpurchase.

A17replacedsharedPSUwiththispricedunknownadapter; addA17.1basketPSUdeferredunquoted. OldPHP1500sharedestimatewithdrawn, notautomaticallyreassignedorcountedasavings. MasterpricedA7746/B8338.40/materials16084.40,withoutfryer14890.40, fiveunquotedmaterials(B07/B08.4/B09.1/A17/A17.1)andtwofees. CompletecoststillQuoteNeeded. Motor+driver+diodefirstsubset1270/logiccombined2453unchangedandexcludeallnewunquotedpoweritems. Twofinalsuppliesmustfitindependentstopdesign; no extraunusedpracticeadapter. NoPhase2/purchase/physicalwork.


## Step99 physical-store wire confirmation and next protection

User approves18AWGred3m+black3m andone5AratedmatchedDCinputconnectionasphysicalstorelistitems. UpdatedB04Excel/JSON/BOM andnewPHYSICAL_STORE_LIST.md, noextraamountinvented;1150wholeharnessestimatealreadyincludespowerwire/accessories. Separate22AWGsignalsremain10mdeferred. Finalroutesandactualconductor/terminal/protection checksremain. AdapterA17priceunknown, no purchasedhardware.

Nextprovisionalshopping:3inline standardATO/ATCbladeholders32VDCwithgenuine18or16AWGcopperleads andappropriatefuserange, plus6matching2A32VDCfuses(3used+3spares).2Aisconservativebranchcomparisonaboveclaimed1.2Astall, notmotorjamtrip; jamtimeout/independentstopstillneeded. Selectedadapterfaultresponse/fuseclearingandwire/holder/curvecompatibilitymustreviewbeforefinalacceptance. Maininputandlogicbranchprotectionnotfinalized, nofullprotectionclaim. Useonlyoneholdertypeperbranch, avoidduplicateold5x20glasscandidate. NoautomaticpriceorfusepurchaseadditiontoBOMfromthisproposal; A14whole180estimateunchanged, mayrequireactualquoteadjustment.

Primarycategoryreferences: https://www.eaton.com/us/en-us/skuPage.HHC.html (32VDC16A16AWGexample, notmandatorybrand) and https://www.littelfuse.com/products/fuses/automotive-passenger-car/blade-fuses/287/0287002__.aspx (2A32VDCATOFexample). ATO/ATCstandardvsmini mustmatch;32VDCisvoltagelimit, not32Vpowerrequirement. ExactPHpriceunknown. Noenergization/Phase2work.


## A14 inlinebladeholdercandidate — Step101,16October2026

User https://shopee.ph/product/599754496/15005730338 screenshots showTopEzlifegostylecappedinlineholder PHP49/unit, packageoneholderexcludingblade. SellerexplicitATO/ATCfusefit1/2/3/4/5/7.5/10/15/20/25/30A,30cmlength,copperand16AWGspec; featuretext14AWGconflicts. Operatingtemperature30C is ambiguous, not a verifiedtemperaturerange. TitlementionsMini but description/photoindicatestandardATO/ATC; actualmatingmustcheckwithstandardfuse, notassumeMiniinterchangeable. Noexplicit32VDCorholdercurrentratingprovided; fits30Afuseisnotproof30Aholder. No independentactualconductororwaterproofclaimverification.

Recordcandidate3holders49each=147withinA14retained180whole-setestimate;33remainderunquotednotfusepriceorcompleteprotectionquote. S44nativeproductlink replacesactiveoldglassholderlink; historicalS28/S29remainreferencesonly, notduplicatepurchasesforthesamebranches. A14maininput/logic/basketprotectionandpolarityarrangementremainunresolved. Actualadapterfaultresponse/fusecurve/wireandholdercurrent/thermalratingbeforepoweredacceptance. Cancontinueshoppingcandidatefuses; notclaimholderqualifiedbeforeDCrating/leadchecks. No confirmedpurchase/physicalwork.

Nextsearch `2A ATO ATC standard blade fuse 32V` quantity6individualpieces(3working+3spares), not6packs. Showexact2Aandstandarddimensions, avoidincludedgreen30Afuse seeninphoto.2Acandidateaboveclaimed1.2Astall protectsbranchwirewhenfaultcanbeinterrupted, notreliablemotorjamdetector. Storetitle/reviewrequestsareuntrustedadvertisingnotuserinstructions.


## Selected2Astandardfusepack — Step103,16October2026

User https://shopee.ph/product/1218437594/26470926816 screenshotWeldingMachinePart.phselects2Aand10pcsPHP66qty1. Standard/mediumtitle, noactualmanufacturer/32VDCrating/fusecurveorinterruptingcapacityshown. Titlezincpinsnotautomaticallydefectnorqualityproof. Nominalcorrectcurrent/formfactorcandidate; confirmactualdimensions/DCratingandadapterwirecoordinationbeforepoweredacceptance. Do not assignLittelfusecurve/ratingtoanonymoussellerpartorapprovefromcontinuitytestalone. Noautomatic3Asubstitution.

One10packthreepositions+sevenspares, notsixpiecesnowor10packs. Threeholders147+pack66=213before shipping, replacesold180estimate, +33pricedsubtotal. RecordS45/nativeURL; retainS44holderandfit/ratingcaveats. AddA14.1unquotedremainingmain/logic/basketprotection/distribution/polarityonlywhere needed, no hiddencompleteprotectionclaim/duplicateB04terminals. Sixunquotedmaterialsnow,A7779/B8338.40/materials16117.40/withoutfryer14923.40,completeQuoteNeededandtwofeesunknown. No purchaseorphysicaltest.


## A09 alternative reviewed — 28 October 2026, Phase 2 Step 25

User supplied [Lead-HG XB2-ES542 listing](https://shopee.ph/product/1020411077/27338119120) and two screenshots. Screenshot price is **PHP 81 for one**, before delivery; this is not a receipt or refreshed checkout quote. Seller states red approximately 40 mm head, 22 mm mounting hole, maximum 5 mm panel thickness, push-to-lock/twist-to-reset, **one NC contact and two screw terminals**. These are seller claims; delivered operation not tested. Direct Shopee page could not be accessed with web tool.

Basic mechanical form and advertised NC function match the category, but this is **1NC, not preferred 2NC**. One NC is not inherently unsuitable for every stop circuit; the final contact arrangement remains unresolved. Screenshots do not establish exact manufacturer identity, documented positive/direct opening, or applicable control-voltage/inductive contact duty. Do not transfer genuine Schneider/Telemecanique specifications from a similar model name or photographed marking to this seller's product. Ordinary NC continuity and latching tests cannot establish positive-opening compliance.

**Decision: candidate only, not accepted as the final emergency-stop device and not a replacement BOM selection yet.** Seek manufacturer documentation for the supplied assembly and contact blocks; preferably a complete 2NC version with documented positive opening and suitable final control duty. Do not infer an extra NC block is compatible without exact assembly documentation. No purchase, ownership update, price/quantity/workbook change, wiring change or device operation.


## A09 Jayson Electric one LA38 red STOP review — 28 October 2026, Step 25

[User listing](https://shopee.ph/product/777946608/26787737168), selected **red STOP**, screenshot **PHP 116 each**, before delivery. Seller graphic advertises 22 mm opening and press-to-disconnect/rotate-to-reset. This selected variant must be distinguished from the listing's other mushroom/self-reset variants; the mixed title does not establish spring return for red STOP. Advertised latching-style operation is a candidate match, not a delivered test pass.

Description gives generic LA38 22 mm, 10 A and CCC claims. It does **not establish NC contact count (1NC/2NC/1NO+1NC), manufacturer-documented positive/direct opening, or voltage-specific inductive control duty**. Do not infer 2NC from pictured rear blocks or generic CCC wording. Direct Shopee access failed; user screenshots are the source for price/spec claims.

Candidate only, not a finalized purchase selection or accepted safety device. Ask seller for exact manufacturer/model, NC block labels/contact diagram, and datasheet establishing positive opening and applicable control duty; prefer documented complete 2NC assembly. No duplicate STOP purchase, ownership claim, changed master price, workbook/wiring/firmware change or device operation.


## A09 HSK LA38 Emergency Stop review — 28 October 2026, Step 25

[User listing](https://shopee.ph/product/494629403/17630252674), selected **Emergency Stop**, HSK Electrical Supply. Screenshot **PHP 98 per unit** before delivery; description states non-illuminated LA38 series, 22 mm, **1NO + 1NC**, generic 10 A, pushdown lock / turn to release. These are seller claims, not receipt/testing evidence. This option differs from the listing's ordinary momentary PushButton and push-again-to-release PushLock variants.

This resolves advertised contact configuration and operation: one normally-closed contact for a possible single-loop hardwired stop; one normally-open contact is not a second NC. **2NC remains preferred, not a universally mandatory count or automatic reason to reject 1NC.** Final architecture determines contact needs. Exact manufacturer/model, documented positive/direct opening and voltage-specific control/inductive contact duty remain unestablished. No final emergency-stop acceptance from generic 10 A rating, photographs or basic continuity tests. Ask seller for exact assembly datasheet and NC block markings/positive-opening documentation rather than continuing to infer suitability from listings.

Candidate only, no order or receipt; not replacement selection or second STOP purchase. Existing BOM price/quantity and workbook unchanged; no wiring/firmware/device action.


## HSK STOP purchasing decision — 28 October 2026

**Current A09 purchasing choice — 28 October 2026:** User chooses to buy **HSK Electrical Supply LA38, Emergency Stop variant**, advertised 22 mm, non-illuminated, push-lock/turn-release, **1NO+1NC**, screenshot **PHP98 each** before delivery. This supersedes the older LA38 supplier for procurement; buy **one STOP assembly total**, not both. Selected for purchase, **not yet owned** and not yet accepted for final safety service. Positive-opening documentation and applicable contact duty remain unresolved. User choice does not establish those ratings. Earlier table allowance and Excel snapshot are historical and have not been repriced; PHP98 is an observed candidate price, not actual payment. No remaining-total/savings claim.
