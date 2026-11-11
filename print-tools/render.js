const {chromium}=require('playwright');const fs=require('fs');const slug=process.argv[2];const O='/tmp/claude-0/books/'+slug+'/';
(async()=>{const b=await chromium.launch();const p=await b.newPage();p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+O+'book-built.html'+(process.env.BLEED?'#bleed':''));await p.waitForFunction(()=>document.title==='done',{timeout:1200000});
const n=await p.evaluate(()=>document.querySelectorAll('.pg').length);
fs.writeFileSync(O+'spreads.json',JSON.stringify(await p.evaluate(()=>window.SPREADS)));
if(process.env.PDF){await p.emulateMedia({media:'print'});await p.pdf({path:O+(process.env.NAME||slug)+(process.env.BLEED?'-Lulu':'')+'.pdf',width:process.env.BLEED?'11.25in':'11in',height:process.env.BLEED?'8.75in':'8.5in',printBackground:true,preferCSSPageSize:true,timeout:0});}
console.log(slug,'pages',n);await b.close()})()
