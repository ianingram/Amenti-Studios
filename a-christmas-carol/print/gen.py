import json,re,qrcode
R='/home/claude/ar/a-christmas-carol/'
idx=json.load(open(R+'index.json'))
roman=['I','II','III','IV','V']
CH=[]
for i,c in enumerate(idx['chapters']):
  d=json.load(open(R+f'ep{i+1:02d}.json'));cs=d['cues']
  paras=[];cur=None
  for c2 in cs:
    t=re.sub(r'\s*\n\s*',' ',c2['text']).strip()
    if c2['para']<2: continue   # 'STAVE ONE.' / 'MARLEY'S GHOST.' headings
    if cur and cur['para']==c2['para']:
      cur['t']+=(' ' if not re.match(r'^[,.;:!?’]',t) else '')+t
    else:
      cur={'para':c2['para'],'cue':c2['n'],'t':t};paras.append(cur)
  for p in paras: p['t']=re.sub(r'\s+([,.;:!?])',r'\1',p['t'])
  name=c['document'].split('·',1)[1].strip().title().replace("’S","’s");name=re.sub(r'(?<=\w) (Of|The|To|A|An|And|In)\b',lambda m:' '+m.group(1).lower(),name)
  q=qrcode.QRCode(border=1,box_size=12);q.add_data(f'https://ianingram.github.io/Amenti-Studios/a-christmas-carol/?ch={i+1}');q.make_image(fill_color='#2a2018',back_color='white').save(f'qr{i+1}.png')
  CH.append({'num':roman[i],'card':f'stave{i+1}.jpg','qr':f'qr{i+1}.png','sub':name,'paras':paras,'pics':{},'picks':[],'sel':[]})
D={'chapters':CH,'cards':'cards/','rh':'A Christmas Carol · Stave ','title':'title-flat.jpg','foreword':[],'unit':'Stave','ornament':'orn-flat.jpg'}
json.dump(D,open('data.json','w'),ensure_ascii=False,indent=0)
for c in CH: print(c['num'],c['sub'],len(c['paras']),sum(len(p['t'].split()) for p in c['paras']))
