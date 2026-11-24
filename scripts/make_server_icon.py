#!/usr/bin/env python3
"""Generate the server-rack app icon (1024x1024) for the "Server" app.

Deep navy background + server rack cabinet (4 blades, green/amber LEDs,
vent slots). No phone imagery. Writes the icon into the three AppIcon
slots (default, dark, tinted) of the Scrcpy Remote asset catalog.

Run from the repository root:
    python3 scripts/make_server_icon.py
Requires Pillow (pip install pillow).
"""
import os
from PIL import Image, ImageDraw

SIZE = 1024
BG = (22, 35, 63)
RACK = (36, 52, 79)
RACK_EDGE = (61, 84, 120)
BLADE = (51, 70, 95)
BLADE_EDGE = (74, 99, 133)
VENT = (30, 43, 66)
LED_GREEN = (74, 222, 128)
LED_AMBER = (251, 191, 36)


def draw_icon(size=SIZE):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    s = size / 1024.0
    x0, y0, x1, y1 = 262 * s, 180 * s, 762 * s, 844 * s
    d.rounded_rectangle([x0, y0, x1, y1], radius=36 * s, fill=RACK,
                        outline=RACK_EDGE, width=max(2, int(4 * s)))
    blade_h = 120 * s
    gap = 24 * s
    bx0, bx1 = 292 * s, 732 * s
    by = 236 * s
    for _ in range(4):
        d.rounded_rectangle([bx0, by, bx1, by + blade_h], radius=16 * s,
                            fill=BLADE, outline=BLADE_EDGE,
                            width=max(1, int(2 * s)))
        cy = by + blade_h / 2
        r = 10 * s
        d.ellipse([322 * s - r, cy - r, 322 * s + r, cy + r], fill=LED_GREEN)
        d.ellipse([352 * s - r, cy - r, 352 * s + r, cy + r], fill=LED_AMBER)
        d.rounded_rectangle([392 * s, cy - 3 * s, 592 * s, cy + 3 * s],
                            radius=3 * s, fill=VENT)
        for i in range(3):
            vy = cy - 18 * s + i * 18 * s
            d.rounded_rectangle([622 * s, vy - 3 * s, 702 * s, vy + 3 * s],
                                radius=3 * s, fill=VENT)
        by += blade_h + gap
    return img


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_dir = os.path.join(
        repo_root, "scrcpy-app", "Scrcpy Remote",
        "Assets.xcassets", "AppIcon.appiconset")
    img = draw_icon()
    for name in ("AppIcon1024x1024.png",
                 "AppIcon1024x1024 1.png",
                 "AppIcon1024x1024 2.png"):
        out = os.path.join(icon_dir, name)
        img.save(out, "PNG")
        print("wrote", out)


if __name__ == "__main__":
    main()
