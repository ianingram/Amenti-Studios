import json,sys,re
slug=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3]);W=int(sys.argv[4]) if len(sys.argv)>4 else 110
D=json.load(open(f'{slug}/data.json'));S=json.load(open(f'{slug}/spreads.json'))
C={c['n']:c for c in D['chapters']}
for k,s in enumerate(S[a-1:b],start=a):
  c=C[int(s['ch'])];cs=[int(x) for x in s['cues'].split(',') if x]
  ps=[p for p in c['paras'] if cs and cs[0]<=p['cue']<=cs[-1]]
  if c.get('play'):
    who=[];sd=[]
    for p in ps:
      m=re.match(r'<p class="sp"><b>([^<]+)\.</b>',p.get('html',''))
      if m:
        w=m.group(1).replace('&nbsp;',' ')
        if w not in who: who.append(w)
      elif 'class="sd"' in p.get('html',''): sd.append(p['t'])
    print(f"#{k} ch{c['n']} {c['num']} {c['sub'][:38]} | {', '.join(who)[:90]} | SD: {' / '.join(sd)[:170]}")
  else:
    t=' '.join(p['t'] for p in ps)
    print(f"#{k} ch{c['n']} {c['sub'][:30]} | {t[:W]} … {t[len(t)//2:len(t)//2+W]} … {t[-W//2:]}")
