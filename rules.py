from __future__ import annotations

import re

_EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
_TOKENY = re.compile(r"\b[a-fA-F0-9]{24,}\b|\b[A-Za-z0-9_-]{32,}\b")


def normalize_whitespace(s: str) -> str:
    # preserve trailing newline if present
    nl = "\n" if s.endswith("\n") else ""
    s = s.rstrip("\n")
    s = s.replace("\t", " ")
    s = re.sub(r"[ ]{2,}", " ", s)
    return s.strip() + nl


def apply_rules(s: str) -> str:
    s = _EMAIL.sub("[redacted-email]", s)
    s = _IP.sub("[redacted-ip]", s)
    s = _TOKENY.sub("[redacted-token]", s)
    return s
