import json
from pathlib import Path

root = Path('/home/hans/repos/fries-machine')
path = root / 'tmp/bom/lean-bom-data.json'
data = json.loads(path.read_text())
item = next(x for x in data['a'] if x['id'] == 'A08')
assert item['price'] == 35
url = 'https://shopee.ph/product/8710520/22680277060'
item.update(
    spec='GS normally-open momentary panel pushbutton, selected Model C; two terminals pictured. One per flavor; software accepts one selection per cooking cycle. Confirm mounting-hole/thread dimensions and press/release operation; exact manufacturer model/environmental ratings unverified',
    price=20,
    status='SCREENSHOT: selected Model C PHP 20 per piece, 15 Oct 2026; delivery extra. Confirm mounting dimensions and momentary normally-open contacts',
    source='S23', store='Shopee PH / GarageSale01', product_url=url,
    why='One button per flavor requests one packet and starts the timed cooking cycle. Momentary means contacts close only while pressed and release afterward; normally open means disconnected at rest. Reuse all three in final build. Controller signal inputs only; not the A09 emergency stop.'
)
source = {'id':'S23', 'label':'User screenshot 15 Oct 2026: GarageSale01 GS normally-open momentary pushbutton, selected Model C PHP 20 per piece. Two terminals pictured; mounting dimensions, actual contact operation and environmental ratings unverified. Shipping extra.', 'url':url}
assert not any(s['id'] == 'S23' for s in data['sources'])
data['sources'].append(source)
path.write_text(json.dumps(data, indent=2) + '\n')

bom = root / 'docs/BOM.md'
text = bom.read_text().replace('Step 31. Updated', 'Step 32. Updated')
old = next(line for line in text.splitlines() if line.startswith('| A08 |'))
new = f"| A08 | {item['name']} | {item['spec']} | 3 | 20.00 | 60.00 | [Shopee GarageSale01]({url}); {item['status']} [S23] | {item['why']} |"
text = text.replace(old, new)
text += f"\n- [S23] [Shopee GarageSale01 GS momentary button]({url}): screenshot dated 15 October 2026, selected **Model C, PHP 20 per piece**. Two terminals pictured. Confirm mounting dimensions and normally-open momentary operation; no exact diameter or protection rating inferred.\n"
bom.write_text(text)

for name in ['docs/BOM.md','PROJECT.md','docs/FRYER_ASSESSMENT.md']:
    p = root / name
    s = p.read_text().replace('9,183', '9,138').replace('17,257.40','17,212.40').replace('16,063.40','16,018.40')
    p.write_text(s)

p = root / 'PROJECT.md'
p.write_text(p.read_text() + '\n- **Flavor/start buttons (A08):** GarageSale01 GS selected Model C normally-open momentary panel buttons, screenshot PHP 20 each × three = PHP 60. Mounting dimensions/contact operation pending; ordinary controller inputs, separate from the emergency stop.\n')
p = root / 'PROGRESS.md'
s = p.read_text()
old = next(line for line in s.splitlines() if line.startswith('**PHASE 1:'))
new = '**PHASE 1: MATERIALS BUYING, Step 32 — A08 flavor/start button supplier and price added.** GarageSale01 GS selected Model C normally-open momentary button PHP 20 per piece × three = PHP 60. Mounting dimensions/contact operation remain to confirm. Table A PHP 9,138; Table B PHP 8,074.40; priced materials PHP 17,212.40 before six unquoted material entries and separate fees. Final-use reuse, clickable links, LCD and timed sequence retained; no Phase 2 approval.'
s = s.replace(old,new)
# Update current budget only; preserve historical step logs.
head, tail = s.split('### A07 roller microswitch',1)
head = head.replace('9,183','9,138').replace('17,257.40','17,212.40').replace('16,063.40','16,018.40')
log = '''### A08 flavor/start buttons on 15 October 2026 (Step 32)

- Reviewed screenshot: GarageSale01 GS normally-open momentary pushbutton, Model C visibly selected, PHP 20 per piece; two terminals pictured. Direct product page unavailable. Exact mounting diameter/thread, environmental rating and delivered contact operation unverified.
- Added A08 supplier and native clickable link; quantity three retained, one per flavor. Replaces PHP 105 allowance with PHP 60, reducing priced materials by PHP 45. No extra ordinary start buttons or duplicate prototype buttons added. Signal controls only; A09 emergency stop remains separate.
- Current Table A PHP 9,138; Table B PHP 8,074.40; priced materials PHP 17,212.40 (without fryer PHP 16,018.40). Six material quotes/conditions and separate fees remain. Updated PROJECT, BOM and fryer budget note. No purchase, installation, physical wiring or phase transition.

'''
p.write_text(head + log + '### A07 roller microswitch' + tail)
