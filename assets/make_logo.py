"""
Generates a simple, original circular Ganesha-silhouette badge (not a copy of
any existing artwork) to use as the center logo for the fallback QR code.
Kept intentionally minimal/geometric so it reads clearly as a generic,
original icon rather than a reproduction of any specific illustration.
"""
from PIL import Image, ImageDraw

SIZE = 400
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

maroon = (107, 29, 29, 255)
gold = (201, 147, 46, 255)
cream = (253, 246, 236, 255)

# Outer circle badge
d.ellipse([4, 4, SIZE - 4, SIZE - 4], fill=cream, outline=gold, width=10)

cx, cy = SIZE // 2, SIZE // 2 + 10

# Ears (two large ovals)
ear_w, ear_h = 150, 170
d.ellipse([cx - 175, cy - 100, cx - 175 + ear_w, cy - 100 + ear_h], fill=maroon)
d.ellipse([cx + 25, cy - 100, cx + 25 + ear_w, cy - 100 + ear_h], fill=maroon)
# Inner ear detail
d.ellipse([cx - 150, cy - 75, cx - 150 + 100, cy - 75 + 120], fill=cream)
d.ellipse([cx + 50, cy - 75, cx + 50 + 100, cy - 75 + 120], fill=cream)

# Head
d.ellipse([cx - 90, cy - 90, cx + 90, cy + 60], fill=maroon)

# Crown point
d.polygon([(cx, cy - 160), (cx - 35, cy - 90), (cx + 35, cy - 90)], fill=gold)
d.ellipse([cx - 14, cy - 175, cx + 14, cy - 150], fill=gold)

# Trunk (curved using arcs approximated by a thick line path)
trunk_pts = [
    (cx, cy + 40),
    (cx - 10, cy + 90),
    (cx + 15, cy + 130),
    (cx - 5, cy + 165),
]
d.line(trunk_pts, fill=maroon, width=34, joint="curve")
d.ellipse([trunk_pts[-1][0] - 17, trunk_pts[-1][1] - 17, trunk_pts[-1][0] + 17, trunk_pts[-1][1] + 17], fill=maroon)

# Eyes
d.ellipse([cx - 45, cy - 20, cx - 25, cy], fill=cream)
d.ellipse([cx + 25, cy - 20, cx + 45, cy], fill=cream)
d.ellipse([cx - 38, cy - 14, cx - 30, cy - 6], fill=(30, 20, 15, 255))
d.ellipse([cx + 30, cy - 14, cx + 38, cy - 6], fill=(30, 20, 15, 255))

img.save("assets/ganesha_badge.png")
print("saved assets/ganesha_badge.png")
