"""Painted-look backdrop generator v2 for Three Realms start flow.

Multi-layer digital-painting pipeline (numpy + PIL): graded skies, glow
bodies, aurora ribbons, noise clouds, atmospheric-perspective ridgelines,
fir silhouettes, keeps/spires, fog banks, particles, vignette, grain.
Outputs straight into the kit's RawArt so the runtime loader picks them up:
  T_Backdrop_login / great-north / mystic-lands / honorguard  (1920x1080)
  T_Realm_<id> realm-select cards (900x1200)
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUT = r"C:\dev\MMOKitEval\RawArt\backdrops"
W, H = 1920, 1080
rng = np.random.default_rng(1157)


# ---------- painting primitives ----------

def canvas(stops):
    """Vertical multi-stop gradient sky. stops: [(t, (r,g,b)), ...]"""
    ys = np.linspace(0, 1, H)
    col = np.zeros((H, 3), dtype=np.float32)
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        m = (ys >= t0) & (ys <= t1)
        f = np.clip((ys - t0) / max(t1 - t0, 1e-6), 0, 1)
        f = f * f * (3 - 2 * f)
        for ch in range(3):
            col[m, ch] = (1 - f[m]) * c0[ch] + f[m] * c1[ch]
    img = np.zeros((H, W, 3), dtype=np.float32)
    img[:] = col[:, None, :]
    return img


def value_noise_1d(n, cells, seed):
    r = np.random.default_rng(seed)
    g = r.uniform(-1, 1, cells + 1)
    x = np.linspace(0, cells, n)
    xi = np.minimum(x.astype(int), cells - 1)
    xf = x - xi
    s = xf * xf * (3 - 2 * xf)
    return g[xi] * (1 - s) + g[xi + 1] * s


def ridge_profile(n, seed, octaves=((4, 1.0), (11, 0.45), (29, 0.2), (67, 0.08))):
    y = np.zeros(n)
    for i, (cells, amp) in enumerate(octaves):
        y += value_noise_1d(n, cells, seed + i * 101) * amp
    y -= y.min()
    return y / max(y.max(), 1e-6)


def paint_ridge(img, base_y, amp, color, seed, haze=0.0, sky_ref=None):
    """Paint a mountain ridgeline; haze blends toward sky for depth."""
    prof = ridge_profile(W, seed)
    top = (base_y - prof * amp).astype(int)
    col = np.array(color, dtype=np.float32)
    ys = np.arange(H)[:, None]
    mask = ys >= top[None, :]
    layer = np.empty_like(img)
    layer[:] = col
    if haze > 0 and sky_ref is not None:
        layer = layer * (1 - haze) + sky_ref * haze
    img[mask] = layer[mask]
    return top


def glow(img, cx, cy, radius, color, intensity=1.0):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d2 = (xx - cx) ** 2 + (yy - cy) ** 2
    g = np.exp(-d2 / (2 * radius * radius)) * intensity
    for ch in range(3):
        img[:, :, ch] += g * color[ch]


def stars(img, count, max_bright=1.0, seed=7):
    r = np.random.default_rng(seed)
    for _ in range(count):
        x = int(r.uniform(0, W))
        y = int(r.uniform(0, H * 0.55))
        b = r.uniform(0.15, max_bright) * (1 - y / H)
        s = r.choice([1, 1, 1, 2])
        img[max(y - s + 1, 0):y + s, max(x - s + 1, 0):x + s] += b


def aurora(img, color_a, color_b, seed=3, strength=1.0):
    """Curtain aurora: sinuous base curve, vertical falloff streaks."""
    r = np.random.default_rng(seed)
    band = np.zeros((H, W), dtype=np.float32)
    xs = np.arange(W)
    base = H * 0.30 + value_noise_1d(W, 5, seed) * H * 0.10
    width = H * (0.10 + 0.06 * (value_noise_1d(W, 9, seed + 5) * 0.5 + 0.5))
    streak = value_noise_1d(W, 160, seed + 9) * 0.5 + 0.5
    ys = np.arange(H)[:, None]
    up = np.clip((base[None, :] - ys) / (width[None, :] * 2.2), 0, 1)
    dn = np.clip((ys - base[None, :]) / width[None, :], 0, 1)
    band = np.exp(-dn * 3.2) * (1 - np.exp(-up * 0.5)) * streak[None, :]
    band = np.clip(band, 0, 1) * strength
    t = np.clip((ys / H - 0.05) * 2.4, 0, 1)
    for ch in range(3):
        img[:, :, ch] += band * ((1 - t[:, 0])[:, None] * color_a[ch] + t[:, 0][:, None] * color_b[ch])


def firs(draw, ridge_top, count, seed, h_range=(30, 95), color=(4, 8, 12)):
    """Layered-triangle fir silhouettes planted on a ridge profile."""
    r = np.random.default_rng(seed)
    for _ in range(count):
        x = int(r.uniform(10, W - 10))
        gy = int(ridge_top[x])
        th = r.uniform(*h_range)
        tw = th * r.uniform(0.34, 0.45)
        tiers = 4
        for k in range(tiers):
            f0 = k / tiers
            f1 = (k + 1.35) / tiers
            yt = gy - th * (1 - f0) - th * 0.12
            yb = gy - th * (1 - f1)
            wk = tw * (0.25 + 0.75 * f1)
            draw.polygon([(x, yt), (x - wk, yb), (x + wk, yb)], fill=color)
        draw.rectangle([x - 1, gy - th * 0.15, x + 1, gy], fill=color)


def keep(draw, cx, base_y, scale, color):
    """Fortress silhouette: curtain wall + crenellated towers."""
    wall_h = 46 * scale
    draw.rectangle([cx - 150 * scale, base_y - wall_h, cx + 150 * scale, base_y], fill=color)
    for tx, tw, th in ((-150, 26, 105), (-60, 22, 80), (30, 30, 130), (130, 24, 92)):
        x0 = cx + tx * scale
        w = tw * scale
        h = th * scale
        draw.rectangle([x0 - w, base_y - h, x0 + w, base_y], fill=color)
        step = max(int(w * 0.6), 4)
        for mx in range(int(x0 - w), int(x0 + w), step * 2):
            draw.rectangle([mx, base_y - h - 7 * scale, mx + step, base_y - h], fill=color)
    for mx in range(int(cx - 150 * scale), int(cx + 150 * scale), 26):
        draw.rectangle([mx, base_y - wall_h - 6 * scale, mx + 10, base_y - wall_h], fill=color)


def spires(draw, cx, base_y, scale, color):
    """Arcane citadel: slender tapering towers."""
    for tx, tw, th in ((-110, 16, 210), (-40, 22, 300), (45, 14, 240), (115, 18, 170)):
        x0 = cx + tx * scale
        w = tw * scale
        h = th * scale
        draw.polygon([(x0, base_y - h), (x0 - w, base_y), (x0 + w, base_y)], fill=color)
        draw.polygon([(x0, base_y - h - 40 * scale), (x0 - w * 0.25, base_y - h + 10),
                      (x0 + w * 0.25, base_y - h + 10)], fill=color)


def particles(img_pil, count, seed, color=(255, 255, 255), r_range=(1, 2), alpha=110, blur=1.2):
    layer = Image.new("RGBA", img_pil.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = np.random.default_rng(seed)
    for _ in range(count):
        x = r.uniform(0, img_pil.width)
        y = r.uniform(0, img_pil.height)
        rad = r.uniform(*r_range)
        a = int(alpha * r.uniform(0.3, 1.0))
        d.ellipse([x - rad, y - rad, x + rad, y + rad], fill=color + (a,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img_pil.alpha_composite(layer)


def finish(arr, fname, size=None, ui_darken=True):
    """Vignette + grain + bottom grade, save."""
    arr = np.clip(arr, 0, 1)
    yy, xx = np.mgrid[0:arr.shape[0], 0:arr.shape[1]].astype(np.float32)
    cx, cy = arr.shape[1] / 2, arr.shape[0] / 2
    d = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2)
    vig = 1 - 0.34 * np.clip(d - 0.45, 0, 1) ** 1.6
    arr *= vig[:, :, None]
    if ui_darken:
        t = np.clip((yy / arr.shape[0] - 0.62) / 0.38, 0, 1)
        arr *= (1 - 0.42 * t)[:, :, None]
    arr += rng.normal(0, 0.008, arr.shape).astype(np.float32)
    img = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), "RGB")
    if size:
        img = img.resize(size, Image.LANCZOS)
    img.save(fname)
    print("painted", fname)
    return img


def to_pil(arr):
    return Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), "RGB").convert("RGBA")


def to_np(img_pil):
    return np.asarray(img_pil.convert("RGB")).astype(np.float32) / 255.0


# ---------- scenes ----------

def scene_great_north(aurora_strength=1.0):
    sky = canvas([(0.0, (0.010, 0.014, 0.045)), (0.42, (0.030, 0.055, 0.120)),
                  (0.75, (0.075, 0.115, 0.190)), (1.0, (0.045, 0.065, 0.105))])
    stars(sky, 420, 0.9, seed=11)
    aurora(sky, (0.05, 0.55, 0.35), (0.30, 0.20, 0.55), seed=4, strength=0.85 * aurora_strength)
    aurora(sky, (0.02, 0.38, 0.30), (0.18, 0.10, 0.42), seed=17, strength=0.5 * aurora_strength)
    glow(sky, W * 0.78, H * 0.16, 46, (0.9, 0.95, 1.0), 1.0)   # moon core
    glow(sky, W * 0.78, H * 0.16, 150, (0.25, 0.32, 0.5), 0.6)  # halo
    img = sky.copy()
    paint_ridge(img, int(H * 0.66), 200, (0.16, 0.21, 0.33), 31, haze=0.55, sky_ref=sky)
    paint_ridge(img, int(H * 0.74), 240, (0.10, 0.14, 0.24), 32, haze=0.30, sky_ref=sky)
    t3 = paint_ridge(img, int(H * 0.86), 210, (0.05, 0.075, 0.135), 33, haze=0.10, sky_ref=sky)
    pil = to_pil(img)
    d = ImageDraw.Draw(pil)
    keep(d, W * 0.24, int(t3[int(W * 0.24)]) + 8, 1.0, (10, 15, 26))
    firs(d, t3, 150, 41, (26, 88), (7, 11, 19))
    front = paint_ridge(to_np(pil), int(H * 1.02), 260, (0.018, 0.028, 0.052), 34)
    img2 = to_np(pil)
    front = paint_ridge(img2, int(H * 1.02), 260, (0.018, 0.028, 0.052), 34)
    pil = to_pil(img2)
    d = ImageDraw.Draw(pil)
    firs(d, front, 90, 42, (60, 150), (3, 6, 11))
    particles(pil, 260, 5, (235, 242, 255), (0.8, 2.2), 120, 1.0)  # snowfall
    return to_np(pil)


def scene_mystic_lands():
    sky = canvas([(0.0, (0.045, 0.012, 0.075)), (0.4, (0.14, 0.045, 0.22)),
                  (0.72, (0.30, 0.12, 0.30)), (1.0, (0.10, 0.05, 0.14))])
    stars(sky, 300, 0.8, seed=23)
    glow(sky, W * 0.5, H * 0.34, 210, (0.55, 0.25, 0.75), 0.55)   # arcane bloom
    glow(sky, W * 0.5, H * 0.34, 70, (0.95, 0.75, 1.0), 0.8)
    glow(sky, W * 0.16, H * 0.2, 90, (0.2, 0.4, 0.8), 0.5)
    img = sky.copy()
    paint_ridge(img, int(H * 0.68), 170, (0.22, 0.11, 0.30), 51, haze=0.5, sky_ref=sky)
    t2 = paint_ridge(img, int(H * 0.80), 200, (0.13, 0.06, 0.20), 52, haze=0.25, sky_ref=sky)
    pil = to_pil(img)
    d = ImageDraw.Draw(pil)
    spires(d, W * 0.5, int(t2[int(W * 0.5)]) + 6, 1.1, (16, 8, 26))
    # floating isles
    r = np.random.default_rng(9)
    for _ in range(7):
        x = r.uniform(W * 0.1, W * 0.9)
        y = r.uniform(H * 0.12, H * 0.42)
        w = r.uniform(40, 130)
        d.polygon([(x - w, y), (x + w, y), (x + w * 0.4, y + w * 0.55), (x - w * 0.3, y + w * 0.5)],
                  fill=(14, 7, 24))
        d.ellipse([x - w, y - w * 0.18, x + w, y + w * 0.22], fill=(18, 9, 30))
    img2 = to_np(pil)
    front = paint_ridge(img2, int(H * 1.03), 230, (0.04, 0.015, 0.07), 53)
    pil = to_pil(img2)
    particles(pil, 200, 8, (220, 160, 255), (1.0, 2.6), 130, 1.6)  # drifting motes
    return to_np(pil)


def scene_honorguard():
    sky = canvas([(0.0, (0.06, 0.045, 0.10)), (0.35, (0.28, 0.12, 0.14)),
                  (0.62, (0.75, 0.38, 0.16)), (0.78, (0.98, 0.66, 0.28)), (1.0, (0.35, 0.16, 0.10))])
    glow(sky, W * 0.5, H * 0.66, 190, (1.0, 0.72, 0.30), 1.0)   # setting sun
    glow(sky, W * 0.5, H * 0.66, 480, (0.7, 0.35, 0.12), 0.45)
    img = sky.copy()
    # cloud bands
    for i, yy in enumerate((0.18, 0.30, 0.44)):
        band = value_noise_1d(W, 7, 61 + i) * 0.5 + 0.5
        y0 = int(H * yy)
        th = int(H * 0.035 * (1 + band.mean()))
        seg = np.clip(band * 1.2, 0, 1)
        for ch, c in enumerate((0.16, 0.09, 0.12)):
            img[y0:y0 + th, :, ch] = img[y0:y0 + th, :, ch] * (1 - 0.7 * seg[None, :]) + c * 0.7 * seg[None, :]
    t1 = paint_ridge(img, int(H * 0.72), 150, (0.26, 0.14, 0.12), 71, haze=0.45, sky_ref=sky)
    t2 = paint_ridge(img, int(H * 0.84), 180, (0.14, 0.08, 0.08), 72, haze=0.2, sky_ref=sky)
    pil = to_pil(img)
    d = ImageDraw.Draw(pil)
    keep(d, W * 0.5, int(t2[int(W * 0.5)]) + 6, 1.6, (22, 12, 10))
    # banners: light shafts from the keep
    shaft = Image.new("RGBA", pil.size, (0, 0, 0, 0))
    ds = ImageDraw.Draw(shaft)
    for k in range(-2, 3):
        x0 = W * 0.5 + k * 60
        ds.polygon([(x0 - 14, int(t2[int(W * 0.5)]) - 160), (x0 + 14, int(t2[int(W * 0.5)]) - 160),
                    (x0 + 90, 0), (x0 - 90, 0)], fill=(255, 190, 90, 14))
    pil.alpha_composite(shaft.filter(ImageFilter.GaussianBlur(6)))
    img2 = to_np(pil)
    paint_ridge(img2, int(H * 1.04), 220, (0.05, 0.03, 0.03), 73)
    pil = to_pil(img2)
    particles(pil, 120, 12, (255, 200, 120), (0.8, 1.8), 90, 1.4)  # embers
    return to_np(pil)


def scene_login():
    """Hero shot: Great North night, stronger aurora, framing peaks."""
    img = scene_great_north(aurora_strength=1.35)
    return img


import os
os.makedirs(OUT, exist_ok=True)
finish(scene_login(), os.path.join(OUT, "T_Backdrop_login.png"))
gn = scene_great_north()
ml = scene_mystic_lands()
hg = scene_honorguard()
finish(gn, os.path.join(OUT, "T_Backdrop_great-north.png"))
finish(ml, os.path.join(OUT, "T_Backdrop_mystic-lands.png"))
finish(hg, os.path.join(OUT, "T_Backdrop_honorguard.png"))
# realm-select cards: center-crop to portrait
for name, arr in (("great-north", gn), ("mystic-lands", ml), ("honorguard", hg)):
    img = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), "RGB")
    cw = int(H * 0.75)
    x0 = (W - cw) // 2
    card = img.crop((x0, 0, x0 + cw, H)).resize((900, 1200), Image.LANCZOS)
    card.save(os.path.join(OUT, "T_Realm_%s.png" % name))
    print("card", name)
print("ALL BACKDROPS PAINTED")
