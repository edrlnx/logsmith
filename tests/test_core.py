from logsmith.core import clean_lines


def test_clean_lines_basic():
    lines = ["hello   world\n", "user test@example.com\n"]
    out = clean_lines(lines)
    assert out[0] == "hello world\n"
    assert "[redacted-email]" in out[1]
