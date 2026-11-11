const {chromium}=require('playwright');const fs=require('fs');
const F='file:///home/claude/as/fonts/';const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const css=`@font-face{font-family:AD;font-weight:700;src:url(${F}amenti-display-700.woff2)}@font-face{font-family:AD;font-weight:400;src:url(${F}amenti-display-400.woff2)}
@font-face{font-family:C;src:url(${NM}/cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2)}
*{margin:0}body{width:1080px;height:1080px;background:radial-gradient(circle at 50% 45%,#141a33,#0a0d1c 70%);display:grid;place-items:center;overflow:hidden}`;
const G='#e0a53c';
const V={
A:`<svg width=1080 height=1080 viewBox="0 0 1080 1080"><g stroke="${G}" stroke-width="22" fill="none"><line x1=540 y1=250 x2=540 y2=840/><line x1=360 y1=430 x2=720 y2=430/><circle cx=540 cy=430 r=82/></g></svg>`,
B:`<svg width=1080 height=1080 viewBox="0 0 1080 1080"><g stroke="${G}" fill="none"><circle cx=540 cy=540 r=300 stroke-width="26"/><line x1=540 y1=240 x2=540 y2=840 stroke-width="26"/><line x1=240 y1=540 x2=840 y2=540 stroke-width="26"/></g></svg>`,
C:`<div style="position:relative;width:760px;height:760px;border:10px solid ${G};border-radius:50%;display:grid;place-items:center"><div style="font:700 520px/1 AD;color:${G};margin-top:40px">A</div></div>`,
D:`<div style="text-align:center;color:${G}"><div style="font:700 190px/1 AD;letter-spacing:.06em">AMENTI</div><div style="height:8px;background:${G};width:520px;margin:34px auto"></div><div style="font:400 92px/1 AD;letter-spacing:.32em;margin-left:.32em">STUDIOS</div></div>`,
};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});
for(const [k,h] of Object.entries(V)){fs.writeFileSync('/tmp/claude-0/ig/pp/_'+k+'.html',`<style>${css}</style>${h}`);
await p.goto('file:///tmp/claude-0/ig/pp/_'+k+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:'/tmp/claude-0/ig/pp/'+k+'.png'});}await b.close()})();
