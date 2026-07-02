"""Atmospheric placeholder backdrops (1920x1080) per realm + login:
vertical sky gradient in realm palette, layered ridge silhouettes,
scattered light motes, heavy vignette. Replaced by Daniel's key art
from art-drop whenever it lands.
"""
import random
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

OUT = Path(r"C:/dev/MMOKitEval/RawArt/backdrops")
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1920, 1080

PALETTES = {
    "login":        ((10, 12, 20), (36, 48, 72), (150, 170, 210)),
    "great-north":  ((8, 12, 22), (30, 48, 80), (140, 175, 220)),
    "mystic-lands": ((18, 12, 6), (80, 55, 22), (235, 185, 110)),
    "honorguard":   ((16, 8, 8), (70, 24, 20), (220, 120, 90)),
}

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

for name, (deep, mid, glow) in PALETTES.items():
    random.seed(hash(name) & 0xffff)
    img = Image.new("RGB", (W, H), deep)
    d = ImageDraw.Draw(img)
    # Sky gradient with a glow band above the horizon.
    for y in range(H):
        t = y / H
        if t < 0.55:
            c = lerp(deep, mid, t / 0.55)
        else:
            c = lerp(mid, deep, (t - 0.55) / 0.45)
        d.line((0, y, W, y), fill=c)
    # Glow halo behind where the UI panel sits.
    glow_img = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow_img)
    gd.ellipse((W*0.28, H*0.18, W*0.72, H*0.62), fill=tuple(int(x*0.35) for x in glow))
    glow_img = glow_img.filter(ImageFilter.GaussianBlur(160))
    img = Image.blend(img, Image.composite(glow_img, img, glow_img.convert("L")), 0.5)
    d = ImageDraw.Draw(img)
    # Ridge silhouettes (3 layers, darker as they near the viewer).
    for layer in range(3):
        base = H * (0.58 + 0.13 * layer)
        amp = 90 - 22 * layer
        shade = lerp(deep, (0, 0, 0), 0.35 + 0.2 * layer)
        pts = [(0, H)]
        x = 0
        y = base
        while x <= W:
            pts.append((x, y))
            x += random.randint(60, 160)
            y = base + random.randint(-amp, amp // 2)
        pts += [(W, H)]
        d.polygon(pts, fill=shade)
    # Light motes (stars / embers / fireflies by realm).
    for _ in range(140):
        x = random.randint(0, W); y = random.randint(0, int(H*0.5))
        r = random.choice((1, 1, 2))
        a = random.uniform(0.25, 0.9)
        d.ellipse((x-r, y-r, x+r, y+r), fill=lerp(deep, glow, a))
    # Vignette.
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse((-W*0.25, -H*0.35, W*1.25, H*1.35), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(220)).point(lambda p: 255 - int((255 - p) * 0.85))
    black = Image.new("RGB", (W, H), (0, 0, 0))
    img = Image.composite(img, black, vig)
    img.save(OUT / f"T_Backdrop_{name}.png")
    print("wrote", f"T_Backdrop_{name}.png")
