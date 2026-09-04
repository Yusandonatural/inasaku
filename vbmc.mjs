import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium' });
for (const f of ['index.html','sagyou.html','hinshu.html','nouki.html','genjou.html','rekishi.html']) {
  const p = await b.newPage({viewport:{width:430,height:900}});
  await p.goto('http://127.0.0.1:8899/'+f, {waitUntil:'domcontentloaded'});
  const a = await p.$('.bmc');
  console.log(f.padEnd(14), a ? (await a.getAttribute('href')) + '  [' + (await a.innerText()).replace(/\n/g,' ') + ']' : 'ボタン未検出');
  await p.close();
}
await b.close();
