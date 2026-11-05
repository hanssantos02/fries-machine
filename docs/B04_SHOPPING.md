# B04 permanent DC harness and moving cables

PHASE 1: MATERIALS BUYING, Step 53 — 16 October 2026.

A harness is a group of wires routed and supported together. B04 replaces temporary jumper connections for permanent low-voltage wiring and provides suitable cable wherever the existing basket mechanism bends or twists it. It does not include fryer mains cable (B09.5) or a second set of A14 fuse holders.

## First listing to compare

Search `22 AWG stranded copper hookup wire multicolor` or `22AWG silicone wire tinned copper`.

- Intended role: fixed, low-current control wiring such as button/switch inputs and short controller signal connections. This is not a selected basket-motor cable size, a blanket rating for all 5 V supply wiring, or a claimed continuous-flex cable.
- Choose genuine copper or tinned copper; do not substitute copper-clad aluminum (CCA) based only on the same AWG label.
- Stranded wire contains many fine wires and is easier to route than solid conductor. AWG describes conductor size; insulation diameter alone does not establish conductor size or current capacity.
- User will buy per metre at a physical store. Initial allowance: 2 m each red, black, blue, yellow and white = 10 m total single-conductor wire. This is a practical initial purchasing quantity, not a measured final routing takeoff. Check terminal accepted wire size and intended insulation/environment ratings.
- Silicone insulation can be flexible but does not automatically establish oil resistance, repeated-flex life or suitability near fryer heat. Prefer protected, cool routes; keep exposed wiring out of hot oil/steam areas.

## Remaining B04 shopping categories

| Category | What to look for | Quantity/status |
|---|---|---|
| Fixed signal wire | Stranded copper hookup wire, initial 22 AWG candidate | 10 m total: red/black/blue/yellow/white, 2 m each; initial allowance |
| Motor supply cables | Copper wire sized for actual starting/stall current, length/voltage drop, fuse and installation | Pending A16/A17; no invented 16/18/22 AWG universal selection |
| Moving cables, where required | Cable documented for the actual repeated bend/twist, conductor count and environment | Pending basket travel/routes; ordinary stranded wire is not automatically rated for repeated motion |
| Removable connectors | Matching locking connector pairs with appropriate wire range, voltage/current rating and pin count | Actual interfaces/count pending; reuse existing suitable terminal points |
| Ferrules where terminal requires/allows them | Crimp sleeves sized to actual conductor and terminal | Tool/terminal compatibility first; avoid unnecessary large assortment |
| Insulation and support | Small heat-shrink assortment, cable sleeves, clamps and strain relief for DC harness | Actual sizes/counts after cable selection; avoid duplicate B03 gland and B05 label kits |

Ferrules are small sleeves crimped around fine wire strands for suitable terminals. Heat-shrink is insulating tubing that tightens when heated. A locking connector has a latch that helps keep it from pulling apart. These definitions are for shopping; wiring/crimping/assembly instructions remain later-phase work.

## Budget and references

B04 remains **PHP 1,150 estimated complete allowance**, not a verified current product quote or a cost for hookup wire alone. No extra line-item charges or new Excel supplier added until a specific listing is assessed. All PH seller prices/lengths remain to confirm.

- [Pololu 22 AWG stranded copper hookup-wire example](https://www.pololu.com/product/2645): product-category reference, not selected PH purchase or current price.
- [igus moving-cable guidance](https://www.igus.com/cables/control-cables): illustrates why stationary and repeated-motion cable requirements differ; no expensive branded cable purchase is mandated by this reference.


## Physical-store list

Ask for **22 AWG stranded copper or tinned-copper insulated hookup wire**, sold per metre:

| Color | Metres | Proposed fixed-control role |
|---|---:|---|
| Red | 2 | Low-current +5 V connections only; not automatically all logic distribution |
| Black | 2 | DC 0 V/common; not protective earth |
| Blue | 2 | Labeled button/signal connections |
| Yellow | 2 | Labeled position-switch/signal connections |
| White | 2 | Other labeled low-current control signals |
| **Total** | **10** | Sum of five individual wire lengths |

Colors are an identification convention for this DC harness, not proof of function; final labels/wiring tables determine every connection. Do not use these lengths/gauge for fryer mains, an unselected motor-power branch or automatically for repeatedly moving cables. No green/yellow protective-earth wire is included here; mains protective earth is separately specified in B09.5.

Per-metre price remains unquoted. Keep B04 PHP 1,150 as the complete harness estimate, not a price for ten metres of wire. Replace with itemized actual prices later without charging the same wire again. Final routing may need additional length or a different cable type; the initial quantity does not establish complete machine coverage.

## Step99 flavor power-wire purchase override

Userwillbuy18AWGstrandedcopperRED3m+BLACK3m(total6m), plusoneadapter-matchedDCinputconnectiondocumented>=5A atphysicalstore. UpdatedB04workbookwithinexisting1150estimate, noindividualquote. Separate22AWGsignalsare10mdeferredfullharness. SeePHYSICAL_STORE_LIST.md. Actualwire/terminal/fusecoordinationandfinalroutespending; nomains/basket/repeated-flexapproval.
