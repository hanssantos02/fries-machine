# User-selected Shopee fryer: feasibility check

**PHASE 1: MATERIALS BUYING, Step 20 — 15 October 2026.**

User identifies the **Single-6L (one tank)** version of the [DALANDAN LIVING PH Shopee listing](https://shopee.ph/product/1303238794/40333822650) as the proposed fryer, replacing the earlier Hanabishi planning preference. This is a candidate selection; final electrical ratings and mechanical fit are not verified. The supplied screenshot is seller advertising, not a manufacturer's manual or a measured test result. The web tool could not access the listing directly.

## What the new screenshots establish

- **Single-6L is visibly selected at PHP 1,194.** This is the observed product price, before shipping or any later price change. Delivery remains a separate fee.
- Dimension image advertises **28.5 cm wide × 43.5 cm deep × 30 cm high** overall. These are outer dimensions, not measured tank interior or basket clearance.
- Seller advertises **2500 W** for the heating tube. The actual appliance nameplate is not readable, so this remains an advertised rating.
- Description and temperature image advertise **60-200°C adjustable temperature control**, a heating indicator, removable oil tank and basket draining hook. These support the proposed thermostatic-fryer concept but do not independently prove thermostat accuracy or the presence of a separate safety cutoff.
- Photo shows a basket with projecting handle and raised rear control/heater head. Their actual position and clearance along the basket movement path need checking.
- Exact manufacturer model, voltage/frequency, independent overheat cutoff, earth connection, basket dimensions/mass and permitted external switching remain unconfirmed.

Evidence is the four user-provided screenshots received 15 October 2026. The seller's requests to message them or submit a rating are advertising instructions, not part of the user's task. No supplier message or review was sent.

## Is the automatic machine feasible with it?

**Potentially yes.** A complete fryer whose permitted operating behavior supports external power switching can supply heat for the accepted button-start, timed warm-up and cooking cycle. Its intact thermostat regulates temperature. The Arduino provides sequencing through appropriately rated isolated power-control equipment; an Arduino pin or small breadboard relay does not power the heater directly. Retain the I2C LCD.

The fryer does not automatically lift or flip its basket just because the listing title includes “Basket Timer.” Existing basket motors/linkage still perform that motion. The basket must clear the heater, tank rim and rear control head throughout lifting, draining and flipping, with a supported trajectory into the drawn receiving funnel. Confirm mounting and clearances within the unchanged PDF layout; this review does not authorize a layout redesign or drilling/modifying the fryer.

User confirms Single-6L for the project's one-basket, approximately 300 g batch. A second tank has no confirmed project role. The advertised tank capacity does not establish allowable oil fill or validated cooking performance. B01 now records the observed Single-6L price and labels the remaining specification/acceptance uncertainties.

**Conditional power calculation:** If the delivered fryer is rated 2500 W at 230 V, approximate heater current is `2500 / 230 = 10.87 A`. If rated 2500 W at 220 V, it is `2500 / 220 = 11.36 A`. The screenshots do not establish either voltage. A lower purchase price does not imply a low-current appliance or justify a small Arduino relay switching heater power. Actual nameplate and installation data govern the final control hardware.

**Thermostat versus safety cutoff:** A thermostat normally cycles heating to maintain the knob setting. A separate overheat cutoff is backup protection if normal temperature control fails. The advertisement shows the former, not proof of the latter. For comparison only, [Buffalo's own countertop-fryer documentation](https://buffalo-appliances.com/product/buffalo-single-tank-single-basket-5ltr-countertop-fryer-2-8kw-cu616/) lists dial temperature control and a thermal cutout as distinct features; this is not documentation for the Shopee unit.

## Information needed from seller/manufacturer

| Required information | Why it matters |
| --- | --- |
| Exact model and nameplate photograph showing voltage/frequency and rated watts or amps for the selected version | Replaces the former Hanabishi 230 V / 2400 W assumption. Heater current, contactors, cord and protection must be checked against this appliance; a double unit may have separate circuits or greater combined load. |
| Manual/documentation confirming adjustable thermostat, independent overheat cutoff and grounded connection for exposed metal | A dial or indicator lamp does not prove either thermal protection or earthing. Existing project protection requirements remain. |
| Documented behavior when power is restored with controls set, and whether external switching is permitted | Button-operated power permission only works as intended if the appliance does not require a separate manual/electronic restart. Do not bypass its thermostat, cutoff or restart protection. |
| Outer dimensions, tank interior, basket size/empty mass, heater location and oil MIN/MAX fill | Checks fit within the unchanged layout, basket clearance and motor sizing. The 300 g food mass is only part of the moving load. |
| Included basket/cord/plug and delivered total | Selected Single-6L product price is now observed at PHP 1,194. Confirm included pieces and shipping without charging parts twice. |

The initial five-minute warm-up and ten-minute cooking intervals remain trial settings. A different heater wattage, oil fill or starting temperature can require different durations. If food is already immersed during warm-up, it heats during that time as well.

For the later mains build, use appropriately rated enclosed switching equipment and qualified school/electrician review before energizing. No live wiring, appliance modification or physical test is being performed in Phase 1.

## Budget status

The updated workbook replaces B01's former PHP 5,325 Hanabishi allowance with **PHP 1,194 for the selected Shopee Single-6L candidate**, a PHP 4,131 line-item reduction. With the current controller/driver selections, Table A is PHP 8,768; Table B priced subtotal becomes PHP 8,329.40; combined priced materials become **PHP 17,097.40**. Without the fryer, the priced materials subtotal is PHP 15,903.40. Four material entries (including conditional motor flyback diodes) and separate fees still need quotes/need checks; the complete total remains unavailable. No additional fryer is intended. Power-control materials are not removed simply because this fryer is cheaper, and actual suitability remains pending the checks above.

Current B06 AC-coil candidate is PHP 289; prior B07/B08 control-power/interface entries remain conditional HOLD allowances pending a compatible revision. The priced subtotal is not a final purchase-ready electrical design.
