#!/usr/bin/env bash
# Encode JPEGs and PNGs under images/ to sibling .webp. Requires Pillow venv.
# Medical Director placeholder (until a real photo): from repo root run
#   python3 scripts/generate_dr_yang_placeholder.py
#   python3 scripts/generate_dr_yang_placeholder.py --site transformativemedspa-website
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ ! -x .venv-img/bin/python ]]; then
  echo "Run: python3 -m venv .venv-img && .venv-img/bin/pip install Pillow" >&2
  exit 1
fi
.venv-img/bin/python << 'PY'
from pathlib import Path
from PIL import Image

root = Path("images")
n = 0
for p in sorted(root.rglob("*.jpg")):
    im = Image.open(p).convert("RGB")
    dst = p.with_suffix(".webp")
    im.save(dst, "WEBP", quality=82, method=6)
    n += 1
for p in sorted(root.rglob("*.png")):
    im = Image.open(p)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
    else:
        im = im.convert("RGB")
    dst = p.with_suffix(".webp")
    im.save(dst, "WEBP", quality=90, method=6)
    n += 1
print(n, "webp files written under images/")
PY
