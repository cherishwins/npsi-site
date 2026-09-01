#!/usr/bin/env bash
# Render the figure to PNG.
#
# The viewport is deliberately TALLER than the 1500px page and the result is
# cropped back down. Rendering headless Chromium at a viewport exactly equal to
# the page height silently drops the last band of the page: the NPSI wordmark
# and signature block paint zero pixels while still reporting as visible to
# getComputedStyle. Rendering at 1600 and cropping to 1500 paints correctly.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
OUT="${1:-$HERE/figure.png}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

"$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --run-all-compositor-stages-before-draw --virtual-time-budget=10000 \
  --window-size=1200,1600 --screenshot="$TMP/raw.png" \
  "file://$HERE/index.html" 2>/dev/null

python3 -c "
from PIL import Image
im = Image.open('$TMP/raw.png').convert('RGB')
assert im.size[0] == 1200, im.size
im.crop((0, 0, 1200, 1500)).save('$OUT')
print('wrote', '$OUT', Image.open('$OUT').size)
"
