"""Entrypoint: draw the v3 entry image to /output/entry.png.

Runs with no network, stdlib + PIL only. Deterministic: the drawing uses
fixed seeds, so repeated runs write byte-identical files.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw import draw_entry


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img = draw_entry()
    img.save(path, "PNG")
    print(f"wrote {path} ({os.path.getsize(path)} bytes)")


if __name__ == "__main__":
    main()
