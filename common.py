from typing import AnyStr


def encode(s: AnyStr) -> bytes:
    if isinstance(s, bytes):
        return s
    return s.encode("utf8")


def decode(b: AnyStr) -> str:
    if isinstance(b, bytes):
        return b.decode("utf-8", "replace")
    return b