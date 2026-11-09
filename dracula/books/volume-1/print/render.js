//BLEED
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:900}});
p.on('console',m=>console.log('console',m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file:///tmp/claude-0/vol1/book-built.html'+(process.env.BLEED?'#bleed':''));await p.waitForFunction(()=>document.title==='done',{timeout:600000});await p.waitForTimeout(800);
const n=await p.evaluate(()=>document.querySelectorAll('.pg').length);console.log('pages',n);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.pg')].map((x,i)=>(i+1)+':'+(x.dataset.im||x.className)).join(' | ')));
await p.emulateMedia({media:'print'});await p.pdf({path:'/tmp/claude-0/vol1/Dracula-Volume-One'+(process.env.BLEED?'-Lulu':'')+'.pdf',width:process.env.BLEED?'11.25in':'11in',height:process.env.BLEED?'8.75in':'8.5in',printBackground:true,preferCSSPageSize:true});
await b.close()})()
