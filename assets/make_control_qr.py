"""
Generates a plain black-on-white QR code (no logo) to use as the CONTROL
image for an AI-art QR pipeline (Illusion Diffusion / QR Code Monster).

Pure high-contrast modules, a wide quiet zone, and a large output size so
the ControlNet has clean structure to follow.

Usage: python assets/make_control_qr.py "<url>"
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else "https://tinyurl.com/4ftdfy5m"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=32,   # large modules -> big output
    border=6,      # generous quiet zone (default is 4)
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("assets/qr_control.png")

print(f"Encoded URL: {url}")
print(f"QR version: {qr.version}  ({img.size[0]}x{img.size[1]} px)")
print("Saved assets/qr_control.png")
