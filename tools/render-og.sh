#!/bin/sh
# Render an Open Graph card SVG to the PNG that og:image references.
#
#   tools/render-og.sh assets/img/wp12-og.svg            # writes assets/img/wp12-og.png
#   tools/render-og.sh assets/img/wp12-og.svg out.png    # explicit output path
#
# The cards carry a Google Fonts @import so they preview correctly in a browser.
# resvg cannot fetch it and silently drops the class rules that follow it, which
# renders every serif line in the fallback face. The import is stripped from a
# temporary copy and the card is rendered against the vendored brand faces in
# tools/fonts/ (SIL Open Font License, see tools/fonts/OFL.txt), so the PNG is
# the same on any machine, including a fresh cloud session with no fonts.
set -eu

src="$1"
out="${2:-${src%.svg}.png}"
fonts="$(cd "$(dirname "$0")" && pwd)/fonts"
tmp="$(mktemp --suffix=.svg)"
trap 'rm -f "$tmp"' EXIT

sed '/@import url(/d' "$src" > "$tmp"
npx --yes resvg-cli --font-dir "$fonts" "$tmp" "$out"
echo "rendered $out"
