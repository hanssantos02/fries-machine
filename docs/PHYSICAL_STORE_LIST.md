# Physical-store purchases

> **Current save, 6 November 2026:** [Concise assembly checkpoint](ASSEMBLY_CHECKPOINT.md) and the newest dated reports supersede earlier pending prompts below. **Step37 motor soldering has been issued but is not reported complete.** Firmware remains output-free simulation; no powered motor test or Phase3.

**Latest receipt evidence, 5 November 2026:** adapter label now confirmed12VDC5A/centre-positive, MODEL1250 (60W nameplate-implied); no duplicate adapter or repeated label request. One red two-lead indicator LED also photographed: check its dimensions/specification for A10 reuse before buying another red LED. Green LED/buzzer/resistors/transistor ownership remains unreported. Red LED is not the motor flyback diode; existing black axial diode stock remains to identify. No fresh quote, added purchase or revised budget.

Updated 5 November 2026, Phase 2 Step 26 pending. User knows a physical supplier. Adapter now owned with user-reported 12 V measurement; other received items tracked in INVENTORY.md. Prices pending actual store quote/receipt.

## First flavor-motor prototype order

| BOM | Item | Quantity | Check when buying |
|---|---|---:|---|
| A17 | 12 V adapter — **received, no automatic repeat purchase** | 0 additional | User reports 12 V measured on 5 November. Compare actual label/plug/current rating against planned enclosed regulated 12 V / 5 A / 60 W; no loaded qualification inferred. |
| B04 | 18AWG insulated stranded copper/tinned-copper wire, RED | 3metres | Actualcoppergauge, insulation and terminalfit; shortfixed12Vflavorpower wiring. |
| B04 | Same wire, BLACK | **Top-up only, if needed** | User owns 18 AWG black wire; length unknown. Compare available usable length with initial 3 m allowance. Do not buy another automatic 3 m. |
| B04 | Matching DCinputsocket/connector with secure insulated connections | **Replacement only if unsuitable** | One connector already owned; Documentedcurrent>=5A, actualadapterplugsizeandpolarity, wireacceptance/strainrelief. Don'tsubstitute2ACCTVconnector merelybecausefits. |

Sixmetres is initialbenchallowance, not completefinalmachinecabletakeoff. Notmains/basket/repeatedmotionapproval. Wire/connectoralreadywithinB04PHP1150wholeharnessestimate, noadditionalpriceinvented. AdapterA17priceunknown. Supplybranchfuses/holderselectionrequiredbeforepoweringmotors.

## Existing later physical-store purchase

22AWGstrandedcopperlow-currentsignalwire: RED2m,BLACK2m,BLUE2m,YELLOW2m,WHITE2m =10m total. Deferredfullharnesspurchase, notnecessaryinadditiontoDuPontjumpersforinitiallogicbenchtest. Notmotorpower/mains/earthwire. PriceunknownwithinB04, notextra1150forwirealone.

## Next candidates, not yet confirmed purchases

Three inline standard-size ATO/ATC blade fuse holders,documented32VDCandappropriatefuserange, genuine18AWGor16AWGcopperleads; six2A32VDCmatchingbladefuses(3positions+3spares) as provisionalshortflavorbranchproposal. Exactadaptercurrentlimit/faultresponse,wire/holderratingsandfusecurvecompatibilitybeforeacceptance. Maininput/logicprotectionseparatelypending; notclaimfullDCprotectioncomplete. No automatic additiontoalreadyselectedphysicalstorebasketwithoutuserrequest. Avoidbuyingboththeseandunqualifiedpreviousglassholdercandidateforthesamebranches.

## Step103 sourcing update

Sixloose2Afuses are superseded byonlinecandidateone10pc2AstandardpackPHP66. ThreeholdersonlinecandidatePHP49each; noautomaticduplicatephysicalstorefusepurchase. DCratings/fusecurveandholderleadchecksremain; main/logic/basketprotectionA14.1stillunquoted.


## Remaining basket-input switches — do not duplicate the three owned

| BOM | Item | Remaining quantity | Check when buying |
|---|---|---:|---|
| A07 | Roller-lever microswitch, COM/NO/NC contacts, compatible with actual basket mounting/travel and low-current input use | **4** | User owns only3connected flavor-index switches. Planned7totalalreadyincludes these4; do not buy7more or addduplicatebudget. Actualfinalbasketmounting/environmentalfitneedschecking. Physicalstorequoteorsameonlinefamilyifavailable; nofreshpriceverified. |

The earlierPHP22/pieceShopee screenshot is a historical15October2026reference, not an updated storequote. No purchase or order placed. These switches are signal contacts, not emergency-stop or motor/heater-power switches.


## Current priority after USB logic checks — 28 October2026

Superseded on 5 November: adapter now owned and user reports 12 V measured. Next review its label/plug/current rating and polarity before any motor hookup. Four additional roller switches remain for basket inputs. Existing received diodes/fuses/holders/DCconnector are not automatic repeat purchases: verify their delivered markings/ratings first. Black 18 AWG wire is owned; usable length and suitability remain to confirm. Red 18 AWG wire is not reported owned. Secure motor mounting and independent disconnect remain to confirm. No motor power step issued by this shopping list.

## Step 25 ownership correction

Ceramic capacitors and 18 AWG black wire are in hand. Confirm capacitor values/count and black-wire length before any top-up. Red wire, LM2596, STOP actuator and buzzer/LED set are not reported owned; check the [full BOM audit](REMAINING_PURCHASES.md) before ordering. Existing diode/fuse/holder/capacitor bags and the DC connector are not automatic repeat purchases. Old sourcing notes above are historical; current inventory takes precedence. No prices refreshed or orders placed.


## A10 buzzer and LEDs — physical-store list, 28 October 2026

User requests these parts from a physical store. This itemizes the existing A10 kit, not an additional duplicate kit or A15 charge. Prices need an actual store quote; existing PHP100 kit allowance is an estimate, not a confirmed total.

| Part | Exact shopping specification | Qty | Purpose |
|---|---|---:|---|
| Active buzzer | **5 V DC active/self-oscillating buzzer**, two pins, rated current **30 mA or less**, documented polarity. Sounds continuously when rated DC is applied; not a passive transducer or 12 V buzzer. | 1 | Audible status/fault signal; switched through a transistor. |
| Red LED | Ordinary **5 mm red indicator LED**, two leads, non-flashing; not a mains/panel indicator or high-power LED | 1 | Red status indication. |
| Green LED | Ordinary **5 mm green indicator LED**, two leads, non-flashing | 1 | Green status indication. |
| LED resistors | **330 ohm, 1/4 W**, 5% or better | 2 | One separate current-limiting resistor per LED. |
| NPN transistor | **BC337**, through-hole TO-92; ask for exact manufacturer/datasheet | 1 | Switches buzzer current without putting its load directly on a Mega GPIO. Retains the existing A10 transistor-driver architecture. |
| Base resistor | **1 kilohm, 1/4 W**, 5% or better | 1 | Limits current into the transistor control terminal (base). Selected for a buzzer no greater than 30 mA. |
| Base pull-down resistor | **10 kilohm, 1/4 W**, 5% or better | 1 | Keeps the transistor off while the controller output is not actively driving it. |
| Buzzer protection diode | **1N4007**, through-hole | 1 **only if no suitable spare** | Protection provision for a magnetic buzzer. A suitable spare SR5100 from the received bag can be reused after confirming identity and retaining any needed motor diodes; do not buy another whole diode pack. A confirmed piezo buzzer may not require it. |

Quantities above are working quantities, not compulsory spare packs. Breadboard, jumper wires and soldering equipment already owned. No additional buzzer module/MOSFET board required for this discrete circuit. Check actual buzzer current/type and transistor manufacturer pinout before a later wiring step; TO-92 appearance alone does not identify its pins. Current firmware/wiring unchanged; no output pin assignments issued in this purchase step.

Technical references: [onsemi BC337 datasheet](https://www.onsemi.com/pdf/datasheet/bc337-fsc-d.pdf), [Arduino external LED/resistor explanation](https://docs.arduino.cc/built-in-examples/basics/Blink), [PUI Audio 5 V/30 mA internally driven indicator example](https://api.puiaudio.com/file/35fae081-9ae1-4652-8032-67880d16eb26.pdf). These establish component categories/examples, not local-shop authenticity or price. 330 ohm is the retained BOM design choice; actual LED forward voltage/brightness checked later.
