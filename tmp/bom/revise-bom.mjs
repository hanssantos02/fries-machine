import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';

const root='/home/hans/repos/fries-machine';
const target=`${root}/BOM_Automatic_Fries_Machine.xlsx`;
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(target));
const sh=wb.worksheets.getItem('BOM');
const data=JSON.parse(await fs.readFile(`${root}/tmp/bom/lean-bom-data.json`,'utf8'));
if(process.argv[2]==='inspect') {
  console.log((await wb.inspect({kind:'table',range:'BOM!A5:H11',include:'values,formulas',maxChars:3500})).ndjson);
  process.exit(0);
}
const applyNativeLinks=()=>console.log(execFileSync('/home/hans/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',[`${root}/tmp/bom/native-hyperlinks.py`],{encoding:'utf8'}).trim());
if(process.argv[2]==='links') {
  wb.recalculate();
  console.log((await wb.inspect({kind:'table',range:'BOM!A5:H11',include:'values,formulas',maxChars:2200})).ndjson);
  applyNativeLinks();
  const linked=await SpreadsheetFile.importXlsx(await FileBlob.load(target));
  for(const [name,range] of [['clean-a-1','A14:H19'],['clean-notes','A73:H88']]){
    const png=await linked.render({sheetName:'BOM',range,scale:1});
    await fs.writeFile(`${root}/tmp/bom/${name}.png`,new Uint8Array(await png.arrayBuffer()));
  }
  process.exit(0);
}
sh.getRange('A1:J200').unmerge();
sh.getRange('A1:J200').clear({applyTo:'all'});
sh.showGridLines=false;
const rows=[],bands=[],entries=[],sections=[];
function note(text,type='note') {
  const row=rows.length+1;
  rows.push([text,null,null,null,null,null,null,null]);bands.push({row,type});return row;
}
note('AUTOMATIC FRIES MACHINE: MATERIALS AND FEES','title');
note('Unchanged PDF layout. Flavor button: dispense packet, enable fryer, timed warm-up 5 min, timed cook 10 min, then basket lift/drain/flip. Durations need validation.');
note('PHP prices reviewed 16 October 2026. ESTIMATE = unverified allowance; QUOTE NEEDED = unknown cost.');
rows.push(Array(8).fill(null));
for(const label of ['Table A: priced prototype materials','Table B: priced additional materials','Priced materials subtotal (A + B)','Priced fees (C; unquoted fees additional)','Complete materials planning total','Complete fees total','Complete grand planning total']) {
  const row=note(label,'summary');
}
note(`${[...data.a,...data.b].filter(x=>x.price===null).length} material entries and ${data.c.filter(x=>x.price===null).length} fees are unquoted. Priced figures include estimates; coil/control-power and protective-device selections need checking.`);
rows.push(Array(8).fill(null));
const header=['#','Item name','Exact model / specification','Qty','Unit price (PHP)','Subtotal (PHP)','Where to buy / price status','Why it is needed'];
for(const [key,title] of [['a','TABLE A: PROTOTYPE MATERIALS — REUSE IN FINAL'],['b','TABLE B: ADDITIONAL PERMANENT MATERIALS'],['c','TABLE C: SERVICE AND DELIVERY FEES']]) {
  const section=note(title,'section'); const head=rows.length+1; rows.push(header);
  const first=rows.length+1;
  for(const item of data[key]) {
    const row=rows.length+1;entries.push({row,item,key});
    rows.push([item.id,item.name,item.spec,item.qty,item.price,null,`${item.store}\n${item.status}${item.source?` [${item.source}]`:''}${item.product_url?`\n${item.product_url}`:''}`,item.why]);
  }
  const last=rows.length;const total=note(`TABLE ${key.toUpperCase()}: PRICED SUBTOTAL`,'subtotal');
  sections.push({key,section,head,first,last,total});
  note(key==='a'?'Cold tests use selected real motors and a factory-enclosed suitable supply. No separate practice motors or bench adapter. Initial logic tests use USB.':key==='b'?'Reuse suitable Table A parts. B06–B09 list the additional power-control components. Dedicated 24 V control supply is conditional on the selected coil arrangement; do not buy both alternatives.':'User assembly labor is budgeted at PHP 0. Any paid qualified review/inspection/help and delivery remain separate fees; no outside panel-building labor is imposed.');
  rows.push(Array(8).fill(null));
}
note('REMOVED PURCHASES','section');
note('Potato and packet IR detectors, external temperature reader/probe, two current sensors, practice motors, separate bench adapter, extra ordinary buttons, bag switch and spare breadboard are omitted. I2C LCD, position switches and indicators remain.');
note('The PHP 5,500 unitemized assembly and PHP 2,500 unquoted labor allowance are removed. B06–B09 identify required electrical materials; C01 identifies labor separately.');
note('GUARD / MECHANISM CONDITIONS','section');
note('Keep the drawn layout. Verify basket mass, torque/speed, existing lift/flip/transfer path and power-off retention before purchasing actuators. Two geared DC axes are provisional; steppers need different matched drivers.');
note('The mechanical team provides guards and load retention. A movable access guard may require a separately quoted interlock. No blanket PHP 700 interlock purchase is included before its need/type is established.');
note('Selected Single-6L seller advertises 2500 W and 60-200 C control; confirm nameplate voltage, independent cutoff, earth and fit. No Arduino temperature gate: 5-minute warm-up is a trial setting; validate actual oil fill/batch/loading timing.');
note('PRICE SOURCES','section');
for(const source of data.sources)note(`[${source.id}] ${source.label}\n${source.url}`);
note('EXCLUSIONS','section');
note('Frame/cutter/chain/coil/funnel fabrication, food/oil/packaging and tools are excluded. User owns multimeters/testing tools. Extra transfer axes, if required by the unchanged mechanism, need explicit additional pricing.');
sh.getRange(`A1:H${rows.length}`).values=rows;
sh.getRange(`A1:H${rows.length}`).format={font:{name:'Arial',size:10},verticalAlignment:'top',wrapText:true};
const widths=[7,30,43,6,18,20,29,57];
for(let i=0;i<widths.length;i++)sh.getRange(`${String.fromCharCode(65+i)}1:${String.fromCharCode(65+i)}${rows.length}`).format.columnWidth=widths[i];
for(const x of entries) {
  const r=x.row,it=x.item;
  sh.getRange(`F${r}`).formulas=[[`=IF(ISNUMBER(E${r}),D${r}*E${r},"Quote needed")`]];
  if(it.product_url){
    sh.getRange(`G${r}`).format.font.color='#0563C1';
  }
  const strings=[it.id,it.name,it.spec,String(it.qty),'','',`${it.store}\n${it.status}${it.source?` [${it.source}]`:''}${it.product_url?`\n${it.product_url}`:''}`,it.why];
  const lines=Math.max(...strings.map((s,i)=>s.split('\n').reduce((n,t)=>n+Math.ceil(t.length/Math.max(4,widths[i]*0.93)),0)));
  sh.getRange(`A${r}:H${r}`).format.rowHeight=Math.max(58,lines*13+14);
  if(x.key==='b')sh.getRange(`A${r}:H${r}`).format.fill='#EAF2E3';
  if(x.key==='c')sh.getRange(`A${r}:H${r}`).format.fill='#F3F0E9';
  sh.getRange(`D${r}:F${r}`).format.horizontalAlignment='right';
  sh.getRange(`D${r}:E${r}`).format.font.color='#0000FF';
  sh.getRange(`E${r}:F${r}`).setNumberFormat('"PHP "#,##0.00');
  if(it.price===null){sh.getRange(`E${r}`).format.fill='#FFF2CC';sh.getRange(`G${r}`).format.font.color='#9C5700';}
}
for(const section of sections) {
  const h=section.head;
  sh.getRange(`A${h}:H${h}`).format={fill:'#2E5597',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,horizontalAlignment:'center',verticalAlignment:'center',rowHeight:35};
  sh.getRange(`F${section.total}`).formulas=[[`=SUM(F${section.first}:F${section.last})`]];
}
for(const band of bands) {
  const r=band.row;const numeric=['summary','subtotal'].includes(band.type);
  sh.mergeCells(`A${r}:${numeric?'E':'H'}${r}`);
  sh.getRange(`A${r}:H${r}`).format.rowHeight=band.type==='note'?46:27;
  if(band.type==='title')sh.getRange(`A${r}:H${r}`).format={fill:'#1B2F4A',font:{name:'Arial',size:14,bold:true,color:'#FFFFFF'},rowHeight:30};
  if(band.type==='section')sh.getRange(`A${r}:H${r}`).format={fill:'#2E5597',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:28};
  if(numeric){sh.getRange(`A${r}:F${r}`).format.fill='#E7E6E6';sh.getRange(`A${r}:F${r}`).format.font.bold=true;sh.getRange(`F${r}`).format.horizontalAlignment='right';sh.getRange(`F${r}`).setNumberFormat('"PHP "#,##0.00');}
}
const [a,b,c]=sections;
sh.getRange('F5').formulas=[[`=F${a.total}`]];
sh.getRange('F6').formulas=[[`=F${b.total}`]];
sh.getRange('F7').formulas=[['=F5+F6']];
sh.getRange('F8').formulas=[[`=F${c.total}`]];
sh.getRange('F9').formulas=[[`=IF(AND(COUNT(E${a.first}:E${a.last})=ROWS(E${a.first}:E${a.last}),COUNT(E${b.first}:E${b.last})=ROWS(E${b.first}:E${b.last})),F7,"Quote needed")`]];
sh.getRange('F10').formulas=[[`=IF(COUNT(E${c.first}:E${c.last})=ROWS(E${c.first}:E${c.last}),F8,"Quote needed")`]];
sh.getRange('F11').formulas=[['=IF(AND(ISNUMBER(F9),ISNUMBER(F10)),F9+F10,"Quote needed")']];
sh.freezePanes.unfreeze();sh.freezePanes.freezeRows(3);
const expected=Object.fromEntries(['a','b','c'].map(k=>[k,data[k].reduce((s,it)=>s+(typeof it.price==='number'?it.qty*it.price:0),0)]));
function assertTotals(){for(const s of sections)if(Math.abs(sh.getRange(`F${s.total}`).values[0][0]-expected[s.key])>0.001)throw new Error(`Subtotal mismatch ${s.key}`);}
wb.recalculate();assertTotals();
if(sh.getRange('F11').values[0][0]!=='Quote needed')throw new Error('Missing quotes were hidden');
const one=process.argv[2]==='fryer'?entries.find(x=>x.item.id==='B01'):entries[0];sh.getRange(`E${one.row}`).values=[[one.item.price+100]];wb.recalculate();
if(sh.getRange('F7').values[0][0]!==expected.a+expected.b+100)throw new Error('Input recalculation failed');
sh.getRange(`E${one.row}`).values=[[one.item.price]];
const unknown=entries.filter(x=>x.item.price===null);
sh.getRange(`E${unknown[0].row}`).values=[[100]];wb.recalculate();
if(sh.getRange('F11').values[0][0]!=='Quote needed')throw new Error('One quote hid other missing costs');
for(const x of unknown)sh.getRange(`E${x.row}`).values=[[100]];
wb.recalculate();
if(Math.abs(sh.getRange('F11').values[0][0]-(expected.a+expected.b+unknown.reduce((sum,x)=>sum+x.item.qty*100,0)))>0.001)throw new Error('Completed quote recalculation failed');
for(const x of unknown)sh.getRange(`E${x.row}`).values=[[null]];
wb.recalculate();assertTotals();
console.log((await wb.inspect({kind:'table',range:'BOM!A5:H11',include:'values,formulas',maxChars:3500})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:1000})).ndjson);
const renderRanges=[{name:'clean-summary',range:'A1:H12'}];
for(const s of sections)for(let start=s.first,n=1;start<=s.last;start+=4,n++)renderRanges.push({name:`clean-${s.key}-${n}`,range:`A${start===s.first?s.section:start}:H${Math.min(start+3,s.last)}`});
renderRanges.push({name:'clean-notes',range:`A${c.total+3}:H${rows.length}`});
const views=process.argv[2]==='reset'?renderRanges.filter(v=>['clean-summary','clean-b-3','clean-notes'].includes(v.name)):process.argv[2]==='b05'?renderRanges.filter(v=>['clean-summary','clean-b-2','clean-notes'].includes(v.name)):process.argv[2]==='b02'?renderRanges.filter(v=>['clean-summary','clean-b-1','clean-notes'].includes(v.name)):process.argv[2]==='protection'?renderRanges.filter(v=>['clean-summary','clean-a-4','clean-a-5','clean-notes'].includes(v.name)):process.argv[2]==='jumpers'?renderRanges.filter(v=>['clean-summary','clean-a-3','clean-notes'].includes(v.name)):process.argv[2]==='switch'?renderRanges.filter(v=>['clean-summary','clean-a-2','clean-notes'].includes(v.name)):process.argv[2]==='controller'?renderRanges.filter(v=>['clean-summary','clean-a-1','clean-a-2','clean-a-4','clean-notes'].includes(v.name)):process.argv[2]==='fryer'?renderRanges.filter(v=>['clean-summary','clean-b-1','clean-b-2','clean-notes'].includes(v.name)):process.argv[2]==='lcd'?renderRanges.filter(v=>['clean-summary','clean-a-5','clean-notes'].includes(v.name)):process.argv[2]==='power'?renderRanges.filter(v=>v.name==='clean-summary'||v.name.startsWith('clean-b-')||v.name.startsWith('clean-c-')||v.name==='clean-notes'):process.argv[2]==='repair'?renderRanges.filter(v=>['clean-a-2','clean-a-4','clean-b-1','clean-b-2'].includes(v.name)):renderRanges;
for(const view of views){const png=await wb.render({sheetName:'BOM',range:view.range,scale:1});await fs.writeFile(`${root}/tmp/bom/${view.name}.png`,new Uint8Array(await png.arrayBuffer()));}
await (await SpreadsheetFile.exportXlsx(wb)).save(target);
applyNativeLinks();
await fs.writeFile(`${root}/tmp/bom/lean-layout.json`,JSON.stringify({sections,rows:rows.length,expected,unpriced:unknown.length},null,2));
console.log(JSON.stringify({expected,pricedMaterials:expected.a+expected.b,completeTotal:sh.getRange('F11').values[0][0],rows:rows.length,sections}));
