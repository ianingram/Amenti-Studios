const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file:///tmp/claude-0/carol/book-built.html'+(process.env.BLEED?'#bleed':''));await p.waitForFunction(()=>document.title==='done',{timeout:600000});
const n=await p.evaluate(()=>document.querySelectorAll('.pg').length);console.log('pages',n);
fs.writeFileSync('/tmp/claude-0/carol/spreads.json',JSON.stringify(await p.evaluate(()=>window.SPREADS)));
if(process.env.PDF){await p.emulateMedia({media:'print'});await p.pdf({path:'/tmp/claude-0/carol/A-Christmas-Carol'+(process.env.BLEED?'-Lulu':'')+'.pdf',width:process.env.BLEED?'11.25in':'11in',height:process.env.BLEED?'8.75in':'8.5in',printBackground:true,preferCSSPageSize:true});}
await b.close()})()
