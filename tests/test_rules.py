from logsmith.rules import apply_rules, normalize_whitespace


def test_normalize_whitespace():
    assert normalize_whitespace("a\t b  c\n") == "a b c\n"


def test_apply_rules():
    s = "email a@b.com ip 127.0.0.1 token abcdef1234567890abcdef1234567890"
    out = apply_rules(s)
    assert "[redacted-email]" in out
    assert "[redacted-ip]" in out
    assert "[redacted-token]" in out
