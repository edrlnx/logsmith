# logsmith

Small CLI utility to normalize and redact log lines.

Features:
- Trim and normalize whitespace
- Timestamp normalization (best-effort)
- Simple redaction rules (emails, tokens, IPs)
- JSONL support (optional)

## Install (dev)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

```