# A15 filtering parts: current shopping list

PHASE 1: MATERIALS BUYING, Step 47 — 16 October 2026.

A capacitor stores a small electrical charge. Ceramic capacitors help suppress fast interference; larger electrolytics buffer brief supply disturbances. These do not replace fuses, flyback diodes, a suitable supply or correct wiring. This is a purchasing list, not installation instructions.

| Selected part | Purchase quantity | Screenshot cost (PHP) | Initial intended use |
|---|---:|---:|---|
| 100 nF / 0.1 µF (104), advertised 50 V ceramic, wire leads | 10 individual pieces | 30 (3 each) | Up to five motor positions plus local logic/signal filtering as needed |
| 1000 µF 25 V radial electrolytic, advertised 10×20 mm | 1 pack of 20 | 69 | Up to three local 12 V driver-group buffers; provisional selection at user request |
| 470 µF 16 V radial electrolytic, selected 8×12 mm | 1 pack of 20 | 76 | One initial 5 V logic-rail buffer |
| **Selected capacitor purchases** | | **175** | Full pack costs, not prorated installed-piece costs |

**A15 remains PHP 200: PHP 175 selected capacitors + PHP 25 estimated remaining signal parts**, before shipping. The PHP 25 is not a supplier quote or an instruction to spend it; final resistor/filter needs depend on actual interfaces. If unnecessary, remove that remainder when the circuit is settled. No second PHP 175 charge is added.

Only up to three 1000 µF and one 470 µF capacitors are initially intended; twenty of each are not functional requirements. Buy only one of each selected pack. A smaller pack or single 470 µF capacitor can save money if its delivered cost is lower. The surplus pieces are simply included in the seller's pack.

## Compatibility and pending checks

- 16 V is the 470 µF capacitor's voltage limit, not an output voltage. It is intended for the 5 V rail here. The 25 V capacitors are scoped to the proposed 12 V motor supply, not an eventual 24 V motor design.
- Generic listing images do not establish exact manufacturer/series, 105°C rating, low ESR or ripple-current capacity. Neither electrolytic listing is claimed to meet those undocumented specifications.
- Inspect delivered markings and evaluate intended load, converter stability, inrush and temperature before permanent use; replace if unsuitable. Basic tests do not establish missing manufacturer ratings. Large capacitors cannot absorb unlimited regenerative energy.
- Check whether delivered motors/modules already contain suitable capacitors before duplicating them. Final filtering positions/quantities are provisional.
- Electrolytics have positive/negative terminals and can fail if reversed. Ceramic capacitors are generally non-polarized. Installation and measurement steps belong in Phase 2.
- Do not duplicate A06 MOSFET modules, A06.1 flyback diodes or A10 LED/buzzer parts. No large resistor assortment required now.

## Clickable selected listings

- [100nF ceramic, PHP 3 each](https://shopee.ph/product/172443349/5245020841): selected 100nF/0.1µF, quantity ten; MOQ six shown.
- [1000µF 25V, twenty-piece pack PHP 69](https://shopee.ph/product/284375565/4543014643): user elects provisional selection despite missing temperature/ESR data.
- [470µF 16V, twenty-piece pack PHP 76](https://shopee.ph/product/487295469/10833769858): selected 16V 470UF 8x12mm 20PCS, order quantity one.

All three prices are from user screenshots dated 16 October 2026; shipping extra. No purchased or tested parts inferred.

[Pololu motor-noise guidance](https://www.pololu.com/docs/0J15/9) supports 0.1 µF ceramic suppression, but does not validate this machine's final filter design.
