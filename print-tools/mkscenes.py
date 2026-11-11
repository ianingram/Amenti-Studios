# Shared: turn a book's scene list into prompts, placeholders, sel entries and a paintings page.
import json, html, os, sys
from PIL import Image, ImageDraw, ImageFont
SREF = {'day': 'https://ianingram.github.io/Amenti-Readings/dracula/art/ch01-b5-2.jpg',
        'night': 'https://ianingram.github.io/Amenti-Readings/dracula/art/ch03-b1-1.jpg',
        'candle': 'https://ianingram.github.io/Amenti-Readings/dracula/art/ch03-b1-1.jpg'}
LIGHT = {'day': 'luminous daylight, plein air', 'night': 'dramatic chiaroscuro, moonlit night',
         'candle': 'warm lamplight and firelight, dramatic chiaroscuro', 'storm': 'dramatic chiaroscuro, stormy night, lightning'}
SREF['storm'] = SREF['night']

def build(slug, tagp, period, chars, scenes, refs, extra_no='', sref=None):
    O = f'/tmp/claude-0/books/{slug}/'
    D = json.load(open(O + 'data.json')); S = json.load(open(O + 'spreads.json'))
    C = {c['n']: c for c in D['chapters']}
    sr = dict(SREF); sr.update(sref or {})
    out = []; cnt = {}
    for (k, title, light, desc) in scenes:
        s = S[k - 1]; ch = int(s['ch']); cs = [int(x) for x in s['cues'].split(',') if x]
        cue = cs[len(cs) // 2] if cs else 1
        cnt[ch] = cnt.get(ch, 0) + 1
        tag = f"{tagp}{ch}-{chr(64 + cnt[ch])}"
        d = desc.format(**chars)
        no = '--no modern, text, letters' + (', ' + extra_no if extra_no else '')
        p = f"{tag} {d}, oil painting, {period}, rich academic realism, {LIGHT[light]} --ar 16:9 --sref {sr[light]} {no}"
        out.append({'n': k, 'tag': tag, 'ch': ch, 'chnum': C[ch]['num'], 'chsub': C[ch]['sub'], 'cue': cue, 'title': title, 'light': light, 'prompt': p, 'img': f'{slug[:2]}-{k:03d}.jpg'})
    rf = [{'name': n, 'prompt': f"{tagp}REF-{n} portrait of {d.format(**chars)}, half-length, plain dark background, oil painting, {period}, rich academic realism, soft studio light --ar 3:4"} for n, d in refs]
    json.dump({'scenes': out, 'refs': rf}, open(O + 'scenes.json', 'w'), indent=1, ensure_ascii=False)
    # placeholders + sel
    F = '/usr/share/fonts/truetype/dejavu/'
    big = ImageFont.truetype(F + 'DejaVuSerif.ttf', 58); sm = ImageFont.truetype(F + 'DejaVuSans.ttf', 30)
    for s in out:
        im = Image.new('RGB', (1600, 1100), (26, 32, 52)); d = ImageDraw.Draw(im)
        d.rectangle((40, 40, 1560, 1060), outline=(168, 130, 63), width=3)
        d.text((800, 420), f"Painting {s['n']}", fill=(224, 165, 60), font=sm, anchor='mm')
        d.text((800, 520), s['title'], fill=(239, 231, 216), font=big, anchor='mm')
        d.text((800, 620), s['tag'], fill=(150, 146, 170), font=sm, anchor='mm')
        im.save(O + 'art/' + s['img'], quality=80)
    for c in D['chapters']:
        c['sel'] = [[s['img'], s['cue']] for s in out if s['ch'] == c['n']]
    json.dump(D, open(O + 'data.json', 'w'), ensure_ascii=False)
    b = open('/tmp/claude-0/books/book.html').read()
    open(O + 'book-built.html', 'w').write(b.replace('__DATA__', json.dumps(D, ensure_ascii=False)))
    print(slug, len(out), 'scenes', len(rf), 'refs', 'missing spreads:', sorted(set(range(1, len(S) + 1)) - {s['n'] for s in out}))
