const {chromium}=require('playwright');const fs=require('fs');
const F='file:///home/claude/as/fonts/';const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const css=`@font-face{font-family:AD;font-weight:700;src:url(${F}amenti-display-700.woff2)}@font-face{font-family:AD;font-weight:400;src:url(${F}amenti-display-400.woff2)}
@font-face{font-family:G;font-style:italic;src:url(${NM}/eb-garamond/files/eb-garamond-latin-400-italic.woff2)}
*{margin:0}body{width:1640px;height:924px;overflow:hidden;background:#0c1020}
.bg{position:absolute;inset:0;background:url(file:///tmp/claude-0/up/out2/${process.env.IMG}.jpg) ${process.env.POS}/cover}
.sh{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 55%,rgba(8,10,22,.15),rgba(8,10,22,.65) 75%),linear-gradient(180deg,rgba(8,10,22,0) 40%,rgba(8,10,22,.7))}
.t{position:absolute;left:0;right:0;top:50%;transform:translateY(-10%);text-align:center;color:#e0a53c}
.w{font:700 120px/1 AD;letter-spacing:.06em}.r{height:5px;background:#e0a53c;width:520px;margin:22px auto}
.s{font:400 52px/1 AD;letter-spacing:.32em;margin-left:.32em}.q{font:italic 40px G;color:#efe7d8;margin-top:30px}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1640,height:924}});
fs.writeFileSync('/tmp/claude-0/ig/_fb.html',`<style>${css}</style><div class=bg></div><div class=sh></div><div class=t><div class=w>AMENTI</div><div class=r></div><div class=s>STUDIOS</div><div class=q>Classic novels: Voiced by History.</div></div>`);
await p.goto('file:///tmp/claude-0/ig/_fb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:'/tmp/claude-0/ig/fbc-'+process.env.K+'.jpg',type:'jpeg',quality:92});await b.close()})();
