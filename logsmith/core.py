from __future__ import annotations

import json
from typing import Iterable

from .rules import apply_rules, normalize_whitespace


def _clean_text(line: str) -> str:
    line = normalize_whitespace(line)
    line = apply_rules(line)
    return line


def clean_lines(lines: Iterable[str], *, jsonl: bool = False, keep_empty: bool = False) -> list[str]:
    out: list[str] = []
    for raw in lines:
        if jsonl:
            try:
                obj = json.loads(raw)
                msg = str(obj.get("message", ""))
                obj["message"] = _clean_text(msg)
                cleaned = json.dumps(obj, ensure_ascii=False) + "\n"
            except Exception:
                cleaned = _clean_text(raw)
        else:
            cleaned = _clean_text(raw)

        if keep_empty or cleaned.strip():
            if not cleaned.endswith("\n"):
                cleaned += "\n"
            out.append(cleaned)
    return out
