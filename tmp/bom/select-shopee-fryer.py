import json
from pathlib import Path

root = Path('/home/hans/repos/fries-machine')
data_path = root / 'tmp/bom/lean-bom-data.json'
data = json.loads(data_path.read_text())
fryer = next(item for item in data['b'] if item['id'] == 'B01')
assert fryer['price'] == 5325
fryer.update(
    category='User-selected fryer',
    name='Single-6L electric deep fryer with basket',
    spec='User-selected DALANDAN LIVING PH Shopee Single-6L; seller advertises 2500 W, 60-200 C dial control, W285 x D435 x H300 mm. Exact manufacturer model/voltage unknown; confirm nameplate, independent overheat cutoff, grounding and fit',
    price=1194,
    status='SCREENSHOT: selected Single-6L PHP 1194, 15 Oct 2026; delivery extra; nameplate/protection/fit pending',
    store='Shopee PH / DALANDAN LIVING PH',
    why='Supplies the cooking tank, heater, temperature control and basket. Replaces the Hanabishi allowance, not a second fryer. Preserve internal controls/protection; confirm basket clearance and allowed external switching. No loose heater is added.',
)
next(item for item in data['b'] if item['id'] == 'B08.1')['why'] = 'Allows the Arduino to switch K1 coil current. Its contacts carry low-voltage coil power, not heater mains current.'
source = next(item for item in data['sources'] if item['id'] == 'S10')
source.update(label='User screenshot 15 Oct 2026: DALANDAN LIVING PH selected Single-6L PHP 1194; advertised 2500 W, 60-200 C, W285 D435 H300 mm; nameplate/cutoff/earth unverified', url='https://shopee.ph/product/1303238794/40333822650')
data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

def edit(relative, changes):
    path = root / relative
    text = path.read_text()
    for old, new in changes:
        assert old in text, (relative, old)
        text = text.replace(old, new, 1)
    path.write_text(text)

path = root / 'docs/BOM.md'
text = path.read_text()
text = text.replace('Step 17. Updated', 'Step 20. Updated', 1)
text = text.replace('PHP 23,019.40', 'PHP 18,888.40', 1)
text = text.replace('PHP 12,205.40', 'PHP 8,074.40', 1)
lines = text.splitlines()
row = f"| B01 | {fryer['name']} | {fryer['spec']} | 1 | 1,194.00 | 1,194.00 | {fryer['store']}. {fryer['status']} [S10] | {fryer['why']} |"
for index, line in enumerate(lines):
    if line.startswith('| B01 |'):
        lines[index] = row
    elif line.startswith('- [S10]'):
        lines[index] = f"- [S10] [DALANDAN LIVING PH Shopee Single-6L](https://shopee.ph/product/1303238794/40333822650): user screenshots dated 15 October 2026 show selected variant PHP 1,194; advertised 2500 W, 60-200°C control and 28.5 cm W × 43.5 cm D × 30 cm H. Voltage, actual nameplate, independent cutoff and grounding remain unverified. Delivery belongs in Table C."
text = '\n'.join(lines) + '\n'
text = text.replace('not the 2400 W heater', 'not heater mains current')
text = text.replace('HFRY60SS is now the user-confirmed planning basis; actual protection/nameplate still require checking.', 'Single-6L from DALANDAN LIVING PH is now the user-confirmed candidate. Its PHP 1,194 selected price is evidenced by the screenshot; 2500 W is advertised, with nameplate/voltage/protection still requiring confirmation.')
heading = '## Compatibility and selection checks\n\n'
text = text.replace(heading, heading + '- Selected fryer replaces the former Hanabishi allowance at PHP 1,194, a PHP 4,131 reduction in that line. Seller-advertised 2500 W gives an illustrative heater current of 10.87 A **if rated 230 V**, or 11.36 A **if rated 220 V**. Neither voltage is established by the screenshots. Confirm actual nameplate before final B06-B09 ratings; do not use the former 2400 W load. Temperature dial control is advertised, but a separate safety cutoff and grounding are not established. Basket/heater/control-head clearance and the unchanged layout still need fit verification.\n\n', 1)
path.write_text(text)

project = root / 'PROJECT.md'
text = project.read_text()
text = text.replace('current priced-material subtotal PHP 23,019.40', 'current priced-material subtotal PHP 18,888.40 including the selected Shopee Single-6L fryer at screenshot-listed PHP 1,194', 1)
lines = text.splitlines()
for index, line in enumerate(lines):
    if line.startswith('- **Fryer/heater:**'):
        lines[index] = '- **Fryer/heater:** User selects **Single-6L (one tank)** from DALANDAN LIVING PH [Shopee listing](https://shopee.ph/product/1303238794/40333822650), replacing Hanabishi. New screenshot visibly selects Single-6L at PHP 1,194; delivery extra. Seller advertises 2500 W, 60-200°C dial control and W285 × D435 × H300 mm outer size. Exact manufacturer model/voltage/nameplate, independent overheat cutoff, grounding, basket/heater clearance and allowed external switching remain unverified. B01 now budgets this unit once. Former Hanabishi 2400 W specification is superseded. See `docs/FRYER_ASSESSMENT.md`.'
project.write_text('\n'.join(lines) + '\n')

edit('docs/POWER_CONTROL_PARTS.md', [
    ('**PHASE 1: MATERIALS BUYING, Step 14 — 15 October 2026.** The user will assemble the controls with guidance. HFRY60SS is the confirmed planning basis.', '**PHASE 1: MATERIALS BUYING, Step 20 — 15 October 2026.** The user will assemble the controls with guidance. The user-selected Shopee Single-6L fryer replaces HFRY60SS; seller advertises 2500 W, but actual voltage/nameplate remain unverified.'),
    ('not the 2400 W heater', 'not heater mains current'),
    ('The candidate fryer is listed as 230 V, 2400 W. The planning heater current is `2400 / 230 = 10.43 A`. Confirm the actual nameplate, minimum/maximum oil levels, independent overheat protection, grounding and external power-control compatibility. A common 10 A Arduino relay board is insufficient as the direct heater power switch. The small relay in B08.1 switches only a low-voltage contactor coil. [Fryer rating reference](https://winlanddepot.com/products/hanabishi-by-winland-quick-fry-6-liters-deep-fryer-stainless-steel-hfry-60ss).', 'The selected Shopee Single-6L is advertised as **2500 W** in the user-provided listing image. Its voltage is not shown. If rated 230 V, the approximate heater current is `2500 / 230 = 10.87 A`; if rated 220 V, it is `2500 / 220 = 11.36 A`. These are conditional calculations, not verified nameplate data. The former Hanabishi 2400 W load is superseded. Confirm nameplate, minimum/maximum oil levels, independent overheat protection, grounding and external switching compatibility before final ratings. A common 10 A Arduino relay board is insufficient as the direct heater switch for these illustrative loads. B08.1 switches only a low-voltage contactor coil. [User-selected product](https://shopee.ph/product/1303238794/40333822650); see [screenshot assessment](FRYER_ASSESSMENT.md).'),
    ('One switches a 2400 W fryer;', 'One switches a fryer advertised as 2500 W (actual nameplate voltage/watts pending);'),
])

progress = root / 'PROGRESS.md'
text = progress.read_text()
lines = text.splitlines()
for index, line in enumerate(lines):
    if line.startswith('**PHASE 1: MATERIALS BUYING, Step 19'):
        lines[index] = '**PHASE 1: MATERIALS BUYING, Step 20 — Shopee Single-6L screenshot price/specs recorded; BOM updated.** Selected price PHP 1,194; seller advertises 2500 W, 60-200°C and W285 D435 H300 mm. Nameplate voltage, independent cutoff, grounding and fit remain unverified. Priced materials PHP 18,888.40 before five unquoted material entries and fees. Final-use motors, I2C LCD and timed sequence retained. No Phase 2 approval.'
text = '\n'.join(lines) + '\n'
text = text.replace("exact variant, nameplate, accepted protected model/manual and fit remain required. The existing workbook still contains the previous Hanabishi planning allowance pending this confirmation.", 'variant now confirmed Single-6L, while actual nameplate, accepted protected model/manual and fit remain required. B01 now uses screenshot-listed PHP 1,194 with the unresolved protection/fit conditions.', 1)
text = text.replace('Table B priced subtotal: **PHP 12,205.40**', 'Table B priced subtotal: **PHP 8,074.40**', 1)
text = text.replace('Priced materials subtotal A+B: **PHP 23,019.40**, including the PHP 5,325 fryer planning candidate', 'Priced materials subtotal A+B: **PHP 18,888.40**, including the PHP 1,194 user-selected Single-6L fryer candidate', 1)
log = '''### Selected fryer screenshot details on 15 October 2026 (Step 20)

- Four new user screenshots show Single-6L visibly selected at PHP 1,194, outer size W28.5 × D43.5 × H30 cm, advertised 2500 W heater and 60-200°C temperature control. Treated as seller claims/observed listing price, not a verified nameplate, safety certification or physical fit test.
- Replaced B01 Hanabishi PHP 5,325 allowance with the selected Shopee unit once. Difference PHP 4,131; Table A unchanged PHP 10,814, Table B priced subtotal PHP 8,074.40, priced materials PHP 18,888.40. Five material quotes/conditions and separate fee quotes remain outstanding. Shipping not included in product price.
- Conditional current at advertised 2500 W: 10.87 A if rated 230 V; 11.36 A if rated 220 V. Actual voltage is not established. Corrected B06-B09 explanation/supplier draft to avoid inheriting the former 2400 W heater specification; no final switching/protection ratings asserted.
- Retained unchanged mechanical layout, final-use motor reuse, I2C LCD and timed warm-up/cooking. Check basket clearance from rear heater/control head, tank rim and handle path. Five-minute warm-up remains a trial, not verified readiness.
- Updated PROJECT, BOM, power-control guide, fryer assessment and workbook data/source. Remaining seller information needed is exact nameplate/manual, independent thermal cutoff/earthing, basket dimensions/mass and permitted power-restoration behavior. No supplier message sent, firmware or physical build performed.

'''
text = text.replace('### Shopee fryer feasibility on 15 October 2026 (Step 19)', log + '### Shopee fryer feasibility on 15 October 2026 (Step 19)', 1)
progress.write_text(text)

print(json.dumps({key: round(sum(x['qty']*x['price'] for x in data[key] if x['price'] is not None), 2) for key in ['a','b','c']}))
