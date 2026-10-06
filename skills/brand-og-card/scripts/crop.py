#!/usr/bin/env python3
"""Center-crop + resize an image to an exact delivery size (needs Pillow: pip install pillow).
Usage: python3 scripts/crop.py in.png out.png 1200x630 [--anchor center|top|bottom|left|right]"""
import sys
try:
    from PIL import Image
except ImportError:
    sys.exit('error: pip install pillow')
src, dst, size = sys.argv[1], sys.argv[2], sys.argv[3]
anchor = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == '--anchor' else 'center'
W, H = (int(x) for x in size.lower().split('x'))
im = Image.open(src).convert('RGB')
r = max(W / im.width, H / im.height)
im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
dx, dy = im.width - W, im.height - H
x = {'left': 0, 'right': dx}.get(anchor, dx // 2)
y = {'top': 0, 'bottom': dy}.get(anchor, dy // 2)
im.crop((x, y, x + W, y + H)).save(dst, quality=92)
print(dst, W, H)
