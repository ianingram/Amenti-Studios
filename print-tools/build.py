import json, re, sys, os, html, qrcode
slug = sys.argv[1]
CFG = json.load(open('/tmp/claude-0/books/books.json'))[slug]
SRC = CFG.get('src', slug)
R = f'/home/claude/ar/{SRC}/'
O = f'/tmp/claude-0/books/{slug}/'
os.makedirs(O + 'cards', exist_ok=True); os.makedirs(O + 'art', exist_ok=True)
if not os.path.exists(O + 'node_modules'): os.symlink('/tmp/claude-0/card/node_modules', O + 'node_modules')
idx = json.load(open(R + 'index.json'))

def roman(n):
    v = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]; s = ''
    for a, r in v:
        while n >= a: s += r; n -= a
    return s

def clean(t): return re.sub(r'\s+([,.;:!?])', r'\1', re.sub(r'\s*\n\s*', ' ', t)).strip()

def verse(t, isverse):
    t = t.replace('\n\n', '\n')
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    if not isverse: return [' '.join(lines)]
    return lines

CH = []
chs = idx['chapters']
for i, c in enumerate(chs):
    if CFG.get('only') and (c.get('book') not in CFG['only']): continue
    d = json.load(open(R + os.path.basename(c['file'])))
    cs = d['cues']; title = d.get('title', '')
    paras = []
    if CFG.get('play'):
        # Act/scene from document 'ACT I · SCENE II'; place from title 'Act I, Scene II — The same. A public place'
        m = re.match(r'ACT (\w+) · SCENE (\w+)', c['document']) or re.match(r'(PROLOGUE)', c['document'])
        act, scene = (m.group(1), m.group(2)) if m and m.lastindex == 2 else ('', '')
        place = title.split('—', 1)[1].strip() if '—' in title else title
        for c2 in cs:
            role = c2['role']; t = c2['text'].strip()
            if role == 'Stage directions':
                tt = clean(t).replace('*', '').strip('[] ')
                if re.match(r'^(ACT [IVX]+|SCENE [IVX]+\.|THE PROLOGUE)', tt): continue
                paras.append({'cue': c2['n'], 'html': f'<p class="sd">{html.escape(tt)}</p>', 'words': None, 't': tt})
                continue
            raw = [l for l in t.replace('\n\n', '\n').split('\n') if l.strip()]
            isv = len(raw) > 1 and sum(1 for l in raw[1:] if l.strip()[:1].isupper()) >= 0.7 * (len(raw) - 1)
            lines = verse(t, isv)
            name = html.escape(role.upper()).replace(' ', '&nbsp;')
            body = ' <br> '.join(html.escape(l) for l in lines)
            words = [f'<b>{name}.</b>'] + body.split(' ')
            paras.append({'cue': c2['n'], 'html': '<p class="sp">' + ' '.join(words) + '</p>', 'words': words, 't': ' '.join(lines)})
        num = roman(i + 1) if not act else act
        sub = (f'Scene {scene} · ' if scene else '') + place
        if c['document'].startswith('PROLOGUE') or not act: num, sub = '', title or 'Prologue'
    else:
        cur = None
        for c2 in cs:
            p = c2.get('para') or 0
            t = clean(c2['text'])
            if p < 4 and (t == t.upper() or re.match(r'^(PART|CHAPTER)\b', t)): continue
            if cur and cur['para'] == p:
                cur['t'] += ('' if re.match(r'^[,.;:!?’]', t) else ' ') + t
            else:
                cur = {'para': p, 'cue': c2['n'], 't': t}; paras.append(cur)
        num = roman(i + 1)
        sub = CFG.get('subfmt', '{title}').format(title=title, doc=c['document'], book=c.get('book', ''))
    url = f"https://ianingram.github.io/Amenti-Studios/{SRC}/?ch={i+1}"
    q = qrcode.QRCode(border=1, box_size=12); q.add_data(url); q.make_image(fill_color='#2a2018', back_color='white').save(O + f'qr{i+1}.png')
    CH.append({'n': i + 1, 'num': num, 'card': f'card{i+1}.jpg', 'qr': f'qr{i+1}.png', 'sub': sub, 'play': bool(CFG.get('play')), 'paras': paras, 'pics': {}, 'picks': [], 'sel': [], 'book': c.get('book')})
D = {'chapters': CH, 'cards': 'cards/', 'rh': CFG['rh'], 'title': 'title-flat.jpg', 'foreword': [], 'unit': CFG['unit'], 'ornament': 'orn-flat.jpg', 'every': CFG.get('every', 1)}
json.dump(D, open(O + 'data.json', 'w'), ensure_ascii=False)
print(slug, len(CH), 'chapters', sum(len(p.get('t', '').split()) for c in CH for p in c['paras']), 'words')
