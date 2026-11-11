const {chromium}=require('playwright');const fs=require('fs');
const slug=process.argv[2];const CFG=JSON.parse(fs.readFileSync('/tmp/claude-0/books/books.json'))[slug];const O='/tmp/claude-0/books/'+slug+'/';
const D=JSON.parse(fs.readFileSync(O+'data.json'));
const NM='file:///tmp/claude-0/card/node_modules/@fontsource';
const base=`@font-face{font-family:G;font-style:italic;src:url(${NM}/eb-garamond/files/eb-garamond-latin-400-italic.woff2)}
@font-face{font-family:C;src:url(${NM}/cormorant-garamond/files/cormorant-garamond-latin-300-normal.woff2)}
@font-face{font-family:M;src:url(${NM}/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2)}
*{margin:0;box-sizing:border-box}body{overflow:hidden}.k{font:28px M;letter-spacing:.42em;text-transform:uppercase;color:#d9a441}`;
const M={
laurel:w=>`<svg width="${w}" height="${w*.5}" viewBox="0 0 120 60"><g fill="none" stroke="#b08a3e" stroke-width="2.2"><path d="M58 52 C38 48 26 34 24 14"/><path d="M62 52 C82 48 94 34 96 14"/></g><g fill="#b08a3e">${[0,1,2,3,4].map(i=>{const t=i/4,x=24+t*(58-24)*1.0,y=14+t*38;return `<ellipse cx="${x-4}" cy="${y-2}" rx="6" ry="2.6" transform="rotate(-40 ${x-4} ${y-2})"/><ellipse cx="${120-x+4}" cy="${y-2}" rx="6" ry="2.6" transform="rotate(40 ${120-x+4} ${y-2})"/>`}).join('')}</g></svg>`,
rose:w=>`<svg width="${w}" height="${w*.5}" viewBox="0 0 120 60"><path d="M60 46 C46 54 36 50 30 44 C42 42 50 44 60 46Z" fill="#2f5d3a"/><circle cx="60" cy="30" r="15" fill="#9a1c2a"/><path d="M60 18 C68 22 70 32 60 38 C52 34 52 24 60 18Z" fill="#c03246"/><path d="M52 26 C58 22 66 26 64 32" fill="none" stroke="#6e101c" stroke-width="2"/></svg>`,
anchor:w=>`<svg width="${w}" height="${w*.5}" viewBox="0 0 120 60"><g fill="none" stroke="#2f4560" stroke-width="3.4" stroke-linecap="round"><circle cx="60" cy="9" r="5"/><path d="M60 14 V54"/><path d="M48 22 H72"/><path d="M38 40 C42 52 52 55 60 55 C68 55 78 52 82 40"/><path d="M38 40 l-4 6 M38 40 l6 2 M82 40 l4 6 M82 40 l-6 2"/></g></svg>`,
fish:w=>`<svg width="${w}" height="${w*.5}" viewBox="0 0 120 60"><path d="M28 18 C48 52 80 52 98 30 C80 8 48 8 28 42" fill="none" stroke="#8a2a1a" stroke-width="3.4" stroke-linecap="round"/></svg>`,
};
const mot=M[CFG.motif];
const jobs=[
 CFG.titleImage?['title-flat.jpg',2200,1700,`body{background:#0b0606}.t{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#f1e9da}`,
 `<div class=t><img src="file://${CFG.hero}" style="width:2200px;margin-top:-60px;-webkit-mask-image:radial-gradient(ellipse 60% 62% at 50% 50%,#000 60%,transparent 100%)"><div class=k style="margin-top:10px">${CFG.author}</div><div style="font:italic 36px G;color:#e8dcc6;margin:22px 0 0">${CFG.tagline}</div><div class=k style="font-size:22px;margin-top:40px">Amenti Studios</div></div>`]:
 ['title-flat.jpg',2200,1700,`body{background:#0d1222}.bg{position:absolute;inset:0;background:url(file://${CFG.hero}) center/cover;filter:brightness(.5)}.t{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#f1e9da;text-align:center}`,
 `<div class=bg></div><div class=t><div style="font:300 150px/1.02 C;letter-spacing:.08em;margin:0 0 34px">${CFG.title.join('<br>')}</div><div class=k>${CFG.author}</div>${CFG.tagline?`<div style="font:italic 36px G;color:#e8dcc6;margin:22px 0 0">${CFG.tagline}</div>`:''}<div class=k style="font-size:22px;margin-top:50px">Amenti Studios</div></div>`],
 ['orn-flat.jpg',3600,360,`body{background:#fff;display:flex;align-items:center;justify-content:center}`,`<div style="height:4px;width:1500px;background:#a8823f"></div><div style="margin:0 40px">${mot(300)}</div><div style="height:4px;width:1500px;background:#a8823f"></div>`]];
D.chapters.forEach((c,i)=>jobs.push([`cards/card${c.n}.jpg`,2200,1238,`body{background:#141a2e;display:flex;align-items:center;justify-content:center;text-align:center;color:#efe7d8;padding:0 120px}`,
 `<div><div class=k>${c.num?D.unit+' '+c.num:'Prologue'}</div><div style="margin:40px auto">${mot(220)}</div><div style="font:300 ${c.sub.length>34?78:100}px/1.1 C;letter-spacing:.08em;text-transform:uppercase">${c.sub}</div></div>`]));
(async()=>{const b=await chromium.launch();const p=await b.newPage();for(const [out,w,h,css,html] of jobs){await p.setViewportSize({width:w,height:h});
fs.writeFileSync(O+'_a.html',`<style>${base}${css}</style>${html}`);await p.goto('file://'+O+'_a.html');await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:O+out,type:'jpeg',quality:90})}await b.close()})();
