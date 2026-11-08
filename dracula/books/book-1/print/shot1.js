const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1056,height:816},deviceScaleFactor:3});
await p.goto('file:///tmp/claude-0/print/book-built.html');await p.waitForFunction(()=>document.title==='done');await p.waitForTimeout(600);
await p.evaluate(()=>{document.body.style.background='#000';const f=document.querySelector('.pg');f.style.margin='0';[...document.querySelectorAll('.pg')].slice(1).forEach(x=>x.remove())});
const el=await p.$('.pg');await el.screenshot({path:'/tmp/claude-0/print/title-flat.png'});await b.close()})()
