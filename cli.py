from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import clean_lines


def _read_lines(path: str) -> list[str]:
    if path == "-":
        return sys.stdin.read().splitlines(True)
    return Path(path).read_text(encoding="utf-8", errors="replace").splitlines(True)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="logsmith", description="Normalize + redact log lines.")
    sub = p.add_subparsers(dest="cmd", required=True)

    clean = sub.add_parser("clean", help="Clean a log file (or '-' for stdin).")
    clean.add_argument("path", help="Path to log file or '-' for stdin.")
    clean.add_argument("--jsonl", action="store_true", help="Treat input as JSON Lines.")
    clean.add_argument("--keep-empty", action="store_true", help="Keep empty lines after cleaning.")

    args = p.parse_args(argv)

    if args.cmd == "clean":
        lines = _read_lines(args.path)
        for out in clean_lines(lines, jsonl=args.jsonl, keep_empty=args.keep_empty):
            sys.stdout.write(out)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
