const {chromium}=require('playwright');const fs=require('fs');
const F='file:///home/claude/as/fonts/';const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const css=`@font-face{font-family:AD;font-weight:700;src:url(${F}amenti-display-700.woff2)}@font-face{font-family:AD;font-weight:400;src:url(${F}amenti-display-400.woff2)}
@font-face{font-family:G;font-style:italic;src:url(${NM}/eb-garamond/files/eb-garamond-latin-400-italic.woff2)}
*{margin:0}html,body{width:1920px;height:1080px;overflow:hidden;background:transparent}
.sh{position:absolute;inset:0;background:radial-gradient(ellipse 60% 55% at 50% 52%,rgba(8,10,22,.55),rgba(8,10,22,.15) 70%,rgba(8,10,22,.45))}
.t{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;color:#e0a53c}
.w{font:700 150px/1 AD;letter-spacing:.06em}.r{height:6px;background:#e0a53c;width:650px;margin:26px auto}
.s{font:400 64px/1 AD;letter-spacing:.32em;margin-left:.32em}.q{font:italic 48px G;color:#efe7d8;margin-top:34px}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
fs.writeFileSync('/tmp/claude-0/ig/_ov.html',`<style>${css}</style><div class=sh></div><div class=t><div class=w>AMENTI</div><div class=r></div><div class=s>STUDIOS</div><div class=q>Classic novels: Voiced by History.</div></div>`);
await p.goto('file:///tmp/claude-0/ig/_ov.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:'/tmp/claude-0/ig/fbv/overlay.png',omitBackground:true});await b.close()})();
