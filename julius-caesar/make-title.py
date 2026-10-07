#!/usr/bin/env python3
"""Julius Caesar — the front-page image: the words and the laurel, in gold leaf, on dark.
Everything is modelled as a height field (raised letters with a chiselled bevel; laurel leaves
domed with a midrib; stems; berries; a ribbon knot), lit as burnished gold leaf, with the leaf's
own texture — the seams between the squares of leaf, a fine grain, a little wear at the edges
where the red bole beneath shows through. Lettering: Cinzel (SIL OFL), Roman inscriptional capitals."""
import sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd

HERE = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'jc-hero.jpg'
W, H, SS = 2560, 1434, 2                   # final size; supersampled 2x
w, h = W * SS, H * SS
rng = np.random.default_rng(7)
cx, cy = w / 2, h / 2 + 10 * SS

height = np.zeros((h, w), np.float32)
alb = np.zeros((h, w), np.float32)         # 1 where gold

def stamp(hloc, x0, y0):
    """lay a local height patch over the field — later pieces lie on top of earlier ones"""
    hh, ww = hloc.shape
    xa, ya = max(0, x0), max(0, y0); xb, yb = min(w, x0 + ww), min(h, y0 + hh)
    if xa >= xb or ya >= yb: return
    sub = hloc[ya - y0: yb - y0, xa - x0: xb - x0]
    m = sub > 0
    base = height[ya:yb, xa:xb]
    top = np.where(m, np.maximum(base * 0.55 + sub, sub), base)
    height[ya:yb, xa:xb] = top
    alb[ya:yb, xa:xb] = np.maximum(alb[ya:yb, xa:xb], m.astype(np.float32))

# ── the words ──
def text_mask(s, size, wt=700, track=0.08):
    f = ImageFont.truetype(f'{HERE}/cinzel-{wt}.ttf', size)
    widths = [f.getlength(c) for c in s]; tw = sum(widths) + track * size * (len(s) - 1)
    asc, desc = f.getmetrics()
    im = Image.new('L', (int(tw + 40), asc + desc + 40), 0); d = ImageDraw.Draw(im); x = 20
    for c, cw in zip(s, widths): d.text((x, 20), c, font=f, fill=255); x += cw + track * size
    a = np.array(im) > 127
    ys, xs = np.where(a); return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
def raised(mask, bevel, top):
    d = nd.distance_transform_edt(mask).astype(np.float32)
    t = np.clip(d / bevel, 0, 1); return (top * (0.25 + 0.75 * t)) * mask       # a chamfer up to a flat face

big = text_mask('CAESAR', 300 * SS, 700, 0.06)
small = text_mask('JULIUS', 190 * SS, 700, 0.16)
sc = (740 * SS) / big.shape[1]
big = np.array(Image.fromarray(big.astype(np.uint8) * 255).resize((int(big.shape[1] * sc), int(big.shape[0] * sc)), Image.LANCZOS)) > 127
sc2 = (big.shape[1] * 0.74) / small.shape[1]
small = np.array(Image.fromarray(small.astype(np.uint8) * 255).resize((int(small.shape[1] * sc2), int(small.shape[0] * sc2)), Image.LANCZOS)) > 127
gap = 70 * SS
tot = small.shape[0] + gap + big.shape[0]
y_small = int(cy - tot / 2); y_big = y_small + small.shape[0] + gap
stamp(raised(small, 7 * SS, 11 * SS), int(cx - small.shape[1] / 2), y_small)
stamp(raised(big, 9 * SS, 14 * SS), int(cx - big.shape[1] / 2), y_big)
# a fine rule between the names, with a small lozenge at its centre
rule_y = y_small + small.shape[0] + gap // 2
rl = np.zeros((10 * SS, int(big.shape[1] * 0.56)), bool); rl[3 * SS: 6 * SS, :] = True
stamp(raised(rl, 1.5 * SS, 5 * SS), int(cx - rl.shape[1] / 2), rule_y - 5 * SS)
lz = 18 * SS; yy, xx = np.mgrid[-lz:lz + 1, -lz:lz + 1]; dm = (np.abs(xx) + np.abs(yy) * 1.6) <= lz
stamp(raised(dm, 6 * SS, 11 * SS), int(cx - lz), rule_y - lz)

# ── the laurel: two branches rising from a ribbon knot at the bottom, open at the crown ──
R = 540 * SS
TMAX = math.radians(152)
def pt(th, side, r=R): return cx + side * r * math.sin(th), cy + r * math.cos(th)
def leaf_patch(L, Wd, ang, curve):
    """one laurel leaf: lanceolate, pointed, domed, a groove down the midrib, a slight bend"""
    S = int(2 * L + 12); pad = S / 2
    yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
    # local frame: the leaf grows from the patch centre along +x, so any rotation stays inside the patch
    u = (xx - pad) / L; v = (yy - S / 2) / L
    v = v - curve * (u * (1 - u)) * 0.35                                  # the bend
    half = (Wd / L) * np.where((u > 0) & (u < 1), np.clip(np.sin(np.pi * np.clip(u, 0, 1) ** 0.75), 0, 1) ** 1.15, 0)
    inside = np.abs(v) < half
    r = np.where(inside, np.abs(v) / np.maximum(half, 1e-6), 1)
    dome = np.sqrt(np.clip(1 - r ** 2, 0, 1)) * (0.5 + 0.5 * np.clip(np.sin(np.pi * np.clip(u, 0, 1)), 0, 1) ** 0.5)
    rib = np.exp(-(np.abs(v) / (0.012 + 0.004 * (1 - u))) ** 2) * 0.32 * (1 - u * 0.7)
    vein = 0.05 * np.sin((u * 14 - np.abs(v) / max(Wd / L, 1e-3) * 4) * np.pi) * (r < 0.9)
    hl = np.where(inside, (dome - rib + vein) * (13 * SS) + 3 * SS, 0).astype(np.float32)
    im = Image.fromarray(hl)
    im = im.rotate(-math.degrees(ang), resample=Image.BICUBIC, center=(pad, S / 2), expand=False)
    return np.array(im), pad, S / 2
def stem(side):
    for th in np.linspace(0.02, TMAX * 0.97, 900):
        x, y = pt(th, side); rr = (9 - 4 * th / TMAX) * SS
        yy, xx = np.mgrid[-int(rr) - 1:int(rr) + 2, -int(rr) - 1:int(rr) + 2]
        d = np.sqrt(xx ** 2 + yy ** 2); m = d <= rr
        stamp((np.sqrt(np.clip(1 - (d / rr) ** 2, 0, 1)) * 6 * SS + 2 * SS) * m, int(x) - int(rr) - 1, int(y) - int(rr) - 1)
def berry(x, y, r):
    yy, xx = np.mgrid[-int(r) - 1:int(r) + 2, -int(r) - 1:int(r) + 2]
    d = np.sqrt(xx ** 2 + yy ** 2) / r; m = d <= 1
    stamp((np.sqrt(np.clip(1 - d ** 2, 0, 1)) * 12 * SS + 3 * SS) * m, int(x) - int(r) - 1, int(y) - int(r) - 1)
for side in (-1, 1):
    stem(side)
    n = 15
    ths = [0.13 + (TMAX - 0.13) * (k / (n - 1)) ** 0.93 for k in range(n)]
    for k, th in enumerate(ths):
        f = k / (n - 1)
        L = (175 - 70 * f) * SS * rng.uniform(0.93, 1.06); Wd = L * 0.2
        x, y = pt(th, side)
        tx, ty = side * math.cos(th), -math.sin(th)                       # direction of growth
        base = math.atan2(ty, tx)
        for j, out in enumerate((1, -1)):                                 # an outer and an inner leaf at each node
            spread = math.radians(rng.uniform(30, 40)) * out * (-side)
            ang = base + spread
            p, ox, oy = leaf_patch(L * (1.0 if out == 1 else 0.88), Wd, ang, curve=0.35 * out * (-side))
            stamp(p, int(x - ox), int(y - oy))
        if k % 3 == 1 and k < n - 2:                                      # a few berries, tucked in
            bx, by = pt(th + 0.035, side, R - 58 * SS); berry(bx, by, 13 * SS)
            bx, by = pt(th + 0.06, side, R - 40 * SS); berry(bx, by, 10 * SS)
    # the tip: one leaf pointing on along the curve
    x, y = pt(TMAX, side); base = math.atan2(-math.sin(TMAX), side * math.cos(TMAX))
    p, ox, oy = leaf_patch(100 * SS, 20 * SS, base, 0.0); stamp(p, int(x - ox), int(y - oy))
# the ribbon knot and its two tails
def tail(side):
    pts = []
    for t in np.linspace(0, 1, 400):
        x = cx + side * (20 + 95 * t + 14 * math.sin(t * 5)) * SS; y = cy + R + (14 + 105 * t) * SS
        wd = (26 - 10 * t) * SS
        pts.append((x, y, wd))
    for x, y, wd in pts:
        r = wd / 2; yy, xx = np.mgrid[-int(r) - 1:int(r) + 2, -int(r) - 1:int(r) + 2]
        d = np.sqrt(xx ** 2 + yy ** 2) / r; m = d <= 1
        stamp((np.sqrt(np.clip(1 - d ** 2, 0, 1)) * 5 * SS + 2 * SS) * m, int(x) - int(r) - 1, int(y) - int(r) - 1)
    # the swallowtail notch
    x, y, wd = pts[-1]
    yy, xx = np.mgrid[-int(wd):int(wd) + 1, -int(wd):int(wd) + 1]
    notch = (np.abs(xx) + np.abs(yy)) < wd * 0.45
    ys, xs = int(y + 6 * SS) - int(wd), int(x + side * 4 * SS) - int(wd)
    sub = height[ys: ys + notch.shape[0], xs: xs + notch.shape[1]]; a = alb[ys: ys + notch.shape[0], xs: xs + notch.shape[1]]
    sub[notch] = 0; a[notch] = 0
tail(-1); tail(1)
kn = np.zeros((int(70 * SS), int(90 * SS)), np.float32)
yy, xx = np.mgrid[0:kn.shape[0], 0:kn.shape[1]]
d = np.sqrt(((xx - kn.shape[1] / 2) / (kn.shape[1] / 2)) ** 2 + ((yy - kn.shape[0] / 2) / (kn.shape[0] / 2)) ** 2)
kn = np.where(d < 1, np.sqrt(np.clip(1 - d ** 2, 0, 1)) * 14 * SS + 3 * SS, 0).astype(np.float32)
stamp(kn, int(cx - kn.shape[1] / 2), int(cy + R - kn.shape[0] / 2))

def up(a): return np.array(Image.fromarray(a.astype(np.float32)).resize((w, h), Image.BILINEAR))
# ── light it as gold leaf ──
hs = nd.gaussian_filter(height, 1.2 * SS)
gy, gx = np.gradient(hs)
nx, ny, nz = -gx, -gy, np.ones_like(gx) * 1.6
nl = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2); nx, ny, nz = nx / nl, ny / nl, nz / nl
L1 = np.array([-0.55, -0.6, 0.58]); L1 /= np.linalg.norm(L1)            # key light, upper left
L2 = np.array([0.7, 0.35, 0.62]); L2 /= np.linalg.norm(L2)              # a warm fill from lower right
diff = np.clip(nx * L1[0] + ny * L1[1] + nz * L1[2], 0, 1)
diff2 = np.clip(nx * L2[0] + ny * L2[1] + nz * L2[2], 0, 1)
Hh = L1 + np.array([0, 0, 1.0]); Hh /= np.linalg.norm(Hh)
spec = np.clip(nx * Hh[0] + ny * Hh[1] + nz * Hh[2], 0, 1) ** 60
spec_w = np.clip(nx * Hh[0] + ny * Hh[1] + nz * Hh[2], 0, 1) ** 9
# the leaf texture: squares of gold leaf with faint seams, a fine grain, burnish variation
yy, xx = np.mgrid[0:h, 0:w]
cell = 88 * SS
jit = nd.gaussian_filter(rng.standard_normal((h // 64 + 2, w // 64 + 2)), 1.5)
seam = ((np.minimum(xx % cell, cell - xx % cell) < 1.2 * SS) | (np.minimum((yy + 31 * SS) % cell, cell - (yy + 31 * SS) % cell) < 1.2 * SS)).astype(np.float32)
seam = nd.gaussian_filter(seam, 0.8 * SS) * 0.22
grain = nd.gaussian_filter(rng.standard_normal((h, w)).astype(np.float32), 0.7 * SS) * 0.05
burn = up(nd.gaussian_filter(rng.standard_normal((h // 32, w // 32)).astype(np.float32), 3))
burn = burn / (np.abs(burn).max() + 1e-6) * 0.10
# wear: on the high edges, where the gold thins to the red bole
edge = np.clip(np.sqrt(gx ** 2 + gy ** 2) / (2.5), 0, 1)
wearn = up(nd.gaussian_filter(rng.standard_normal((h // 8, w // 8)).astype(np.float32), 1.2))
wear = np.clip((wearn - 1.15) * 2.2, 0, 1) * (0.35 + 0.65 * edge) * alb

GOLD_D = np.array([0.30, 0.17, 0.05]); GOLD = np.array([0.86, 0.63, 0.24]); GOLD_H = np.array([1.0, 0.93, 0.70])
BOLE = np.array([0.42, 0.13, 0.07])
light = 0.18 + 0.95 * diff + 0.22 * diff2
# a raking falloff across the picture, brighter toward the upper left, so the gold is never flat
rake = 0.85 + 0.25 * np.clip(1 - np.sqrt(((xx - w * 0.3) / w) ** 2 + ((yy - h * 0.2) / h) ** 2), 0, 1)
k = np.clip(light * rake * (1 + burn + grain - seam), 0, 1.6)[..., None]
col = np.where(k < 0.7, GOLD_D + (GOLD - GOLD_D) * (k / 0.7), GOLD + (GOLD_H - GOLD) * np.clip((k - 0.7) / 0.9, 0, 1))
col = col + (spec * 0.9 + spec_w * 0.18)[..., None] * GOLD_H
col = col * (1 - wear[..., None] * 0.75) + BOLE * wear[..., None] * 0.75 * (0.4 + 0.6 * k)

# ── the ground: near-black, warmed toward imperial red at the centre, a faint stone grain ──
r2 = np.sqrt(((xx - cx) / (w * 0.55)) ** 2 + ((yy - cy) / (h * 0.62)) ** 2)
bgk = np.clip(1 - r2, 0, 1) ** 1.6
stone = up(nd.gaussian_filter(rng.standard_normal((h // 4, w // 4)).astype(np.float32), 1.0)) * 0.012
bg = np.array([0.025, 0.018, 0.016]) + np.array([0.16, 0.03, 0.035]) * bgk[..., None] + stone[..., None]
# the gold casts a soft shadow down and to the right, and a close contact shadow
a = alb.astype(np.float32)
sh = nd.shift(nd.gaussian_filter(a, 14 * SS), (12 * SS, 10 * SS), order=1) * 0.75
sh2 = nd.shift(nd.gaussian_filter(a, 3 * SS), (3 * SS, 2.5 * SS), order=1) * 0.6
bg = bg * (1 - np.clip(sh + sh2, 0, 0.9))[..., None]
# a faint warm glow around the gold, as if lamplit
glow = nd.gaussian_filter(a, 40 * SS) * 0.08
bg = bg + glow[..., None] * np.array([0.9, 0.55, 0.2])
aa = nd.gaussian_filter(a, 0.6 * SS)[..., None]
img = bg * (1 - aa) + col * aa
img = np.clip(img, 0, 1) ** (1 / 1.05)
out = Image.fromarray((img * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
out.save(OUT, quality=90, optimize=True, progressive=True)
print('saved', OUT, out.size)
