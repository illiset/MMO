"""Procedural placeholder icons for skill KINDS (64x64 PNG): dark plate,
gold rim, kind-glyph in kind color. Real icon art replaces these later.
Output: C:/dev/MMOKitEval/RawArt/icons/kind_<kind>.png
"""
from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path(r"C:/dev/MMOKitEval/RawArt/icons")
OUT.mkdir(parents=True, exist_ok=True)
GOLD = (200, 168, 96)
BG = (18, 17, 22)

KINDS = {
    "strike": ((216, 92, 76), "blades"),
    "dd": ((230, 140, 60), "burst"),
    "dot": ((160, 200, 90), "drops"),
    "heal": ((240, 214, 120), "cross"),
    "hot": ((240, 214, 120), "crossring"),
    "buff": ((120, 170, 230), "up"),
    "debuff": ((170, 110, 200), "down"),
    "cc": ((140, 140, 210), "chain"),
    "taunt": ((220, 120, 100), "bang"),
    "stance": ((150, 160, 180), "shield"),
    "shout": ((230, 180, 90), "arcs"),
    "passive": ((160, 160, 160), "ring"),
    "pet": ((150, 190, 140), "paw"),
    "cleanse": ((170, 220, 220), "spark"),
}

def draw_glyph(d, kind, c):
    if kind == "blades":
        d.line((18, 46, 46, 18), fill=c, width=5); d.line((18, 18, 46, 46), fill=c, width=5)
    elif kind == "burst":
        for a in range(8):
            import math
            x = 32 + 16 * math.cos(a * math.pi / 4); y = 32 + 16 * math.sin(a * math.pi / 4)
            d.line((32, 32, x, y), fill=c, width=4)
    elif kind == "drops":
        for cx, cy in ((24, 26), (40, 26), (32, 42)):
            d.ellipse((cx-5, cy-5, cx+5, cy+5), fill=c)
    elif kind == "cross":
        d.rectangle((28, 16, 36, 48), fill=c); d.rectangle((16, 28, 48, 36), fill=c)
    elif kind == "crossring":
        d.rectangle((28, 18, 36, 46), fill=c); d.rectangle((18, 28, 46, 36), fill=c)
        d.ellipse((12, 12, 52, 52), outline=c, width=3)
    elif kind == "up":
        d.polygon(((32, 16), (48, 40), (16, 40)), fill=c)
    elif kind == "down":
        d.polygon(((32, 48), (48, 24), (16, 24)), fill=c)
    elif kind == "chain":
        d.ellipse((14, 22, 34, 42), outline=c, width=4); d.ellipse((30, 22, 50, 42), outline=c, width=4)
    elif kind == "bang":
        d.rectangle((28, 14, 36, 38), fill=c); d.ellipse((28, 44, 36, 52), fill=c)
    elif kind == "shield":
        d.polygon(((32, 12), (50, 20), (46, 44), (32, 52), (18, 44), (14, 20)), outline=c, width=4)
    elif kind == "arcs":
        for r in (10, 17, 24):
            d.arc((32 - r, 32 - r, 32 + r, 32 + r), start=-60, end=60, fill=c, width=3)
    elif kind == "ring":
        d.ellipse((16, 16, 48, 48), outline=c, width=5)
    elif kind == "paw":
        d.ellipse((24, 30, 40, 46), fill=c)
        for cx, cy in ((20, 24), (32, 20), (44, 24)):
            d.ellipse((cx-4, cy-4, cx+4, cy+4), fill=c)
    elif kind == "spark":
        d.polygon(((32, 12), (37, 27), (52, 32), (37, 37), (32, 52), (27, 37), (12, 32), (27, 27)), fill=c)

for kind, (color, glyph) in KINDS.items():
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((2, 2, 62, 62), radius=8, fill=BG, outline=GOLD, width=2)
    draw_glyph(d, glyph, color)
    img.save(OUT / f"kind_{kind}.png")
print(f"wrote {len(KINDS)} kind icons -> {OUT}")
