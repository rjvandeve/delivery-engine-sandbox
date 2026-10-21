"""Toy package used to rehearse the Hermes project-delivery-engine end to end."""


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``."""
    return len(text.split())


def char_frequency(text: str, ignore_case: bool = True) -> dict[str, int]:
    """Counts of each non-whitespace character in ``text``.

    With ``ignore_case=True`` letters are counted case-insensitively and the
    keys are lower-case. Empty input returns ``{}``.
    """
    counts: dict[str, int] = {}
    for ch in text:
        if ch.isspace():
            continue
        if ignore_case:
            ch = ch.lower()
        counts[ch] = counts.get(ch, 0) + 1
    return counts
