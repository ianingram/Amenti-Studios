const {chromium}=require('playwright');
const fs=require('fs');const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const A='/tmp/claude-0/up/out2/';
// [file, painting, focusX(0-1), overlay]
const posts=JSON.parse(fs.readFileSync('/tmp/claude-0/ig/posts.json'));
const css=`@font-face{font-family:G;font-style:italic;src:url(${NM}/eb-garamond/files/eb-garamond-latin-400-italic.woff2)}
@font-face{font-family:C;src:url(${NM}/cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2)}
@font-face{font-family:M;src:url(${NM}/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;background:#0c1020}
.bg{position:absolute;inset:0;background-size:cover;}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,22,.0) 45%,rgba(8,10,22,.82) 100%)}
.sig{position:absolute;bottom:44px;left:0;right:0;text-align:center;font:13px M;letter-spacing:.5em;text-transform:uppercase;color:#e0a53c;opacity:.85}
.t{position:absolute;left:0;right:0;text-align:center;color:#f1e9da}
.k{font:15px M;letter-spacing:.45em;text-transform:uppercase;color:#e0a53c}
.big{font:300 138px/1 C;letter-spacing:.12em;margin:18px 0 14px}
small{display:block;font-size:.42em;letter-spacing:.14em;margin-bottom:6px}.fit{white-space:nowrap;display:inline-block}.sig2{position:absolute;bottom:44px;left:0;right:0;text-align:center;font:12px M;letter-spacing:.5em;text-transform:uppercase;color:#e0a53c;opacity:.6}
.q{font:italic 34px/1.35 G;color:#efe7d8;padding:0 110px}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const [out,img,fx,ov] of posts){
 const html=`<style>${css}</style><div class=bg style="background-image:url(file://${A}${img}.jpg);background-position:${fx*100}% 50%"></div>${ov?'<div class=shade></div>'+ov:'<div class=shade style="opacity:.45"></div><div class=sig>Amenti Studios · Dracula</div>'}`;
 fs.writeFileSync('/tmp/claude-0/ig/_p.html',html);await p.goto('file:///tmp/claude-0/ig/_p.html',{waitUntil:'load'});await p.evaluate(async()=>{await document.fonts.ready;document.querySelectorAll('.fit').forEach(e=>{let f=parseFloat(getComputedStyle(e).fontSize);while(e.scrollWidth>860&&f>40){f-=4;e.style.fontSize=f+'px'}});});
 await p.screenshot({path:`/tmp/claude-0/ig/posts/${out}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
