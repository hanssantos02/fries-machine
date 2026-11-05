# Current prototype purchasing list

Current phase: **Phase2, Step24 complete — USB-only logic milestone**, 28 October 2026. The shopping list below is the historical 16 October planning list. **Check [current received inventory](INVENTORY.md) before ordering; do not buy received items again.**

## What this order covers

Controller, three flavor/start buttons, LCD, three position/index inputs and the selected three-flavor-motor prototype. Suitable parts will be reused in the final machine. This is not yet a complete frying/basket-motion prototype: actual basket motors, power supply, independent stop/mains controls and mechanics remain unresolved. This document is a clean consolidated list replacing the earlier logic-only first-order list. The list itself originally authorised no physical work. The user has since explicitly started Phase 2, supplied receipt photographs and confirmed soldered MOSFET modules; that newer state is recorded in INVENTORY.md. Mega/LCD/input and USB-only software-simulation tests have now passed; see USB_LOGIC_CHECKPOINT.md. Powered motor/basket/fryer tests remain outstanding.

## Online/electronics-store selected items

| BOM | Item/specification | Quantity to order | Planning subtotal PHP | Source |
|---|---|---:|---:|---|
| A01 | Full-size Mega2560 R3, 2560 R3 With Cable | 1 set | 699 | https://shopee.ph/product/580325202/15523024357 |
| A18 | ALLAN LCD1602 with complete I2C backpack | 1 | 120 | https://shopee.ph/product/211037329/9786615418 |
| A08 | GS Model C normally-open momentary flavor buttons | 3 | 60 | https://shopee.ph/product/8710520/22680277060 |
| A07 | SHOPO roller-lever microswitches, initial flavor indexes | 3 | 66 | https://shopee.ph/product/447511770/11436017124 |
| A11 | Full-size 830-point solderless breadboard, low-current logic only | 1 | 91 | https://www.makerph.com/product/full-size-breadboard-830-holes/ |
| A12 | DuPont jumpers: one M-M, one M-F, one F-F bundle, about20cm, ideally40leads/bundle | 3 bundles | 147 estimated | https://shopee.ph/product/1021339444/22577819873 |
| A05 | ZENG WHCD JGB37-520,12V Motor /22RPM, motor-only | 3 | 1056 conditional voucher price | https://shopee.ph/product/1412288706/26828465072 |
| A06 | LR7843 MOSFET driver modules | 3 | 150 | https://shopee.ph/product/1367148707/41455009761 |
| A06.1 | SR5100 nominal5A100V Schottky diodes,10pcs | 1 pack | 64 | https://shopee.ph/product/487295469/11536801341 |
| A13 | LM2596 adjustable buck converter,12Vto5V logic | 1 | 35 | https://shopee.ph/product/682614836/23339687631 |
| A14 | Standard ATO/ATC inline blade fuse holders | 3 | 147 | https://shopee.ph/product/599754496/15005730338 |
| A14 | Standard2A blade fuses,10pcs | 1 pack | 66 | https://shopee.ph/product/1218437594/26470926816 |
| A15 | 100nF/0.1uF50V ceramic capacitors | 10 pieces | 30 | https://shopee.ph/product/172443349/5245020841 |
| A15 | 1000uF25V electrolytics,20pcs | 1 pack | 69 | https://shopee.ph/product/284375565/4543014643 |
| A15 | 470uF16V electrolytics,20pcs | 1 pack | 76 | https://shopee.ph/product/487295469/10833769858 |
| | Priced subset before physical-store items, other missing parts/tools/shipping | | 2876 | |

The fifteen subtotals above sum2876. Do not add master A14set213 or master A15allowance200 on top: their selected parts are already counted individually here. A15selectedpacks175, excluding unitemized25estimate. Firstlogic subset1183 +motor/driver/diode1270 +holder/fuse213 +buck35 +filterpacks175=2876.

Three motors1056 assumes PHP352 each applies to quantitythree at checkout; prior screenshot wasAfterVoucher. Jumper147 is mixed-variant estimate, onlyMM10cm49was screenshot-confirmed. Breadboard91 reverifiedMakerPH16Oct. Other prices from user screenshots, not guaranteed currentcart prices. Actualparts untested.

## Physical-store list, prices pending

| BOM | Item | Quantity |
|---|---|---:|
| A17 | Regulated factory-enclosed12VDC5A60W adapter with overload/short-circuit protection and suitableACcord | 1 |
| B04 | 18AWG insulated stranded copper/tinned copper, RED | 3m |
| B04 | Same wire, BLACK | 3m |
| B04 | Secure insulated DCinputsocket/connector matched to actualadapterplug/polarity, documented>=5A and appropriatewiretermination | 1 |

See PHYSICAL_STORE_LIST.md. Sixmetres initialshortfixedflavorbenchallowance, notfinalroute/basket/mains/flexapproval. Do not add B04whole1150allowance to this pricedsubset as if it were a quote for these pieces. Separate later22AWGsignalwire10m remains deferred; DuPontjumperscoverinitiallogicconnections.

## Needed before actual motor operation or coil dispensing

- A14.1remaininginput/logicprotection and distribution/insulatedconnections, exactparts/priceafteractualadapterlabel/currentlimiting andwire/fusecoordination. Branch2Afuse/holder32VDCratings, actualleadgauge/temperature andfusecurve remain unverified. Threebranchholders/fuses are not the entireprotectionpackage; do not substitute largerfusessolelyavailability. No poweringmotorsthroughUSB/Arduino/breadboard/DuPontsignaljumpers.
- Independentmotor-power stop/accessible disconnect and safe securedtestarrangement definedbeforepoweredtests; movingloadedmechanismrequiresappropriatehardwarestop/guarding. CurrentLA38STOPcandidateA09notdocumentedqualified; do not assume140priceprovescompleteemergencystopcircuit.
- Three secure37mm-motor mounting brackets/fixtures withcorrectscrews, unlessmechanicalteamprovides. Motor-onlyvariantdoesnotestablishincludedbrackets.
- Three shaftcouplings/hubs: motor side6mmDshaft, coilsideactualmeasurementpending. Do notblindorder6-to-6mmcouplings. FitwithinunchangedPDFdesign.
- Threeindexcams/actuatingtabs plussecuremountsforexistingthree microswitches, unlessalreadyprovided. Actualcamgeometry/packetreleaseandjamtimeoutstobevalidated. No secondsetofswitchesorduplicatedmountallowances.
- Driverheaders/terminalblocksandmotorleadterminationsmayneedsoldering. Verifywhat'ssupplied beforeextraconnectororders. Actualmotor/drivercurrent/reset/OFFandflybackcircuitchecksremain; sellerperformanceisnotverifiedtestresult.

Capacitors are existingselectedfilteringcandidates, not instructiontoinstalltwentyofeach; actualaddedvalues/positions dependoncircuitchecks. Threeceramicmotorpositions, up-to-three1000uFrailpositions andone470uFlogicposition wereinitialproposals, notallautomaticallynecessary. ElectrolyticESR/ripple/temperatureunverified. Diodepack:3positionsifonboardpathmissing+7spares. Fusepack:3positions+7spares. NoSB560orotherduplicateflybackpack. Smallremainingpartsnotquotedareexcludedfrom2876.

## Tools to check, not automatically buy again

Ownedmultimeterandcomputer, includedUSBdatacable. Check solderingiron/stand, electronics-suitable solder, wirestripper/cutter, smallscrewdrivers andheatshrink/insulation. Additionaltools dependonactualterminations; no newtoolkitpriceinvented. Noinstallation/flashingstepsperformed.

## Defer from this first order

Basketmotors/drivers(A16/A04), fouradditionalprovisionalbasketswitches(A07remaining), basketsupplyA17.1, completefryerinstallationandB06–B09mains/controlhardware, permanentenclosures/shield/fullharness/labels. FryerB01andmechanicalpartsremainnecessaryforfullmachineandpurchasingownerstatusunconfirmed; do notduplicateorder. Noextrapotato/packet/temp/currentdetectors, encoders, manualPWMknobsorstepperdriversforthecurrentflavorplan. A10buzzer/statusLEDsoptionalforinitialdisplay-ledtests. Existingselectedfinalpartsarenotcancelledbydeferral.

BeforePhase2, finalizecompletepoweredtestpartsandgetuserPhase1approval. Beforefinalmainproductphase, usermustconfirmsuccessfulprototypeandactualfinal-loadcompatibility. This listcannotguaranteeexactfinalbasket/supply/installationpartswithoutmissinginputs.
