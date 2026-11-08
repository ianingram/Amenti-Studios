const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1056,height:816},deviceScaleFactor:3});
await p.goto('file:///tmp/claude-0/print/credits.html');await p.waitForFunction(()=>document.title==='done');await p.waitForTimeout(800);
await (await p.$('.pg')).screenshot({path:'/tmp/claude-0/print/credits-flat.png'});await b.close()})()
