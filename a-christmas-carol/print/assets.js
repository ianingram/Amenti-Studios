const {chromium}=require('playwright');const fs=require('fs');
const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const base=`@font-face{font-family:G;font-style:italic;src:url(${NM}/eb-garamond/files/eb-garamond-latin-400-italic.woff2)}
@font-face{font-family:C;src:url(${NM}/cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2)}
@font-face{font-family:M;src:url(${NM}/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2)}
*{margin:0;box-sizing:border-box}body{overflow:hidden}
.k{font:28px M;letter-spacing:.42em;text-transform:uppercase;color:#d9a441}`;
const holly=(w)=>`<svg width="${w}" height="${w*0.5}" viewBox="0 0 120 60"><g fill="#2f5d3a"><path d="M60 30 C48 18 36 22 28 14 C30 24 22 30 30 36 C38 38 50 34 60 30Z"/><path d="M60 30 C72 18 84 22 92 14 C90 24 98 30 90 36 C82 38 70 34 60 30Z"/></g><g fill="#a3201c"><circle cx="56" cy="34" r="5"/><circle cx="64" cy="34" r="5"/><circle cx="60" cy="27" r="5"/></g></svg>`;
const jobs=[
 ['title-flat.jpg',2200,1700,`body{background:#0d1222}.bg{position:absolute;inset:0;background:url(file:///home/claude/as/a-christmas-carol/carol-hero.jpg) center/cover;filter:brightness(.55)}
 .t{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#f1e9da;text-align:center}`,
 `<div class=bg></div><div class=t><div class=k>Charles Dickens</div><div style="font:300 190px/1 C;letter-spacing:.08em;margin:50px 0 10px">A CHRISTMAS<br>CAROL</div><div style="font:italic 46px G;color:#e8dcc6;margin:20px 0 60px">in Prose · Being a Ghost Story of Christmas</div><div class=k style="font-size:22px">Amenti Studios</div></div>`],
 ['orn-flat.jpg',3600,360,`body{background:#fff;display:flex;align-items:center;justify-content:center}`,`<div style="height:4px;width:1500px;background:#a8823f"></div><div style="margin:0 40px">${holly(300)}</div><div style="height:4px;width:1500px;background:#a8823f"></div>`],
];
const st=['One','Two','Three','Four','Five'];const D=JSON.parse(fs.readFileSync('data.json'));
D.chapters.forEach((c,i)=>jobs.push([`cards/stave${i+1}.jpg`,2200,1238,`body{background:#141a2e;display:flex;align-items:center;justify-content:center;text-align:center;color:#efe7d8}`,
 `<div><div class=k>Stave ${st[i]}</div><div style="margin:40px auto">${holly(220)}</div><div style="font:300 100px/1.05 C;letter-spacing:.08em;text-transform:uppercase">${c.sub}</div></div>`]));
(async()=>{const b=await chromium.launch();for(const [out,w,h,css,html] of jobs){const p=await b.newPage({viewport:{width:w,height:h}});
fs.writeFileSync('/tmp/claude-0/carol/_a.html',`<style>${base}${css}</style>${html}`);await p.goto('file:///tmp/claude-0/carol/_a.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:'/tmp/claude-0/carol/'+out,type:'jpeg',quality:92});await p.close()}await b.close()})();
