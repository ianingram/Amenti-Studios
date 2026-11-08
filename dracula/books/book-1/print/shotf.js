const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1068,height:840},deviceScaleFactor:3});
await p.goto('file:///tmp/claude-0/print/front.html');await p.waitForFunction(()=>document.title==='done');await p.waitForTimeout(800);
await p.screenshot({path:'/tmp/claude-0/print/front.png'});await b.close()})()
