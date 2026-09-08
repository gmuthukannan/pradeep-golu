"""
Generates a reliable, standard QR code (error-correction level H) with the
badge logo inset in the center. This is the guaranteed-scannable fallback,
not the full AI-art style from the reference image.

Usage: python3 assets/make_qr.py "<url>"
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

url = sys.argv[1] if len(sys.argv) > 1 else "https://gmuthukannan.github.io/pradeep-golu/"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="#6b1d1d", back_color="#fdf6ec").convert("RGBA")

logo = Image.open("assets/ganesha_badge.png").convert("RGBA")

# Logo should cover at most ~22% of the QR's width to stay within level-H
# error-correction budget (30% redundancy).
qr_w, qr_h = qr_img.size
logo_target = int(qr_w * 0.22)
logo = logo.resize((logo_target, logo_target), Image.LANCZOS)

# White padded backing so the logo doesn't blend into dark modules
pad = 14
backing = Image.new("RGBA", (logo_target + pad * 2, logo_target + pad * 2), "#fdf6ec")
backing.paste(logo, (pad, pad), logo)

pos = ((qr_w - backing.width) // 2, (qr_h - backing.height) // 2)
qr_img.paste(backing, pos, backing)

qr_img.save("assets/qr_code.png")
print(f"Encoded URL: {url}")
print("Saved assets/qr_code.png")
