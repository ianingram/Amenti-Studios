const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:900}});
p.on('console',m=>console.log('console',m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file:///tmp/claude-0/print/book-built.html');await p.waitForFunction(()=>document.title==='done',{timeout:60000});await p.waitForTimeout(800);
const n=await p.evaluate(()=>document.querySelectorAll('.pg').length);console.log('pages',n);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.pg')].map((x,i)=>(i+1)+':'+(x.dataset.im||x.className)).join(' | ')));
await p.emulateMedia({media:'print'});await p.pdf({path:'/tmp/claude-0/print/Dracula-Book-I-sample.pdf',width:'11in',height:'8.5in',printBackground:true,preferCSSPageSize:true});
await b.close()})()
