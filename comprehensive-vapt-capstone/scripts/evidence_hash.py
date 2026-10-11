#!/usr/bin/env python3
"""Print SHA-256 hashes for evidence files (integrity tracking, not proof of authenticity)."""
import argparse, hashlib
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", help="Evidence directory")
    args = parser.parse_args()
    root = Path(args.directory)
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")
    for path in sorted(root.rglob("*")):
        if path.is_file():
            print(f"{digest(path)}  {path}")
if __name__ == "__main__":
    main()
