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


def is_palindrome(text: str) -> bool:
    """True when ``text`` reads the same backwards, ignoring case and whitespace."""
    normalized = "".join(ch for ch in text if not ch.isspace()).casefold()
    return normalized == normalized[::-1]


def is_anagram(a: str, b: str) -> bool:
    """True when ``a`` and ``b`` use the same letters, ignoring case and whitespace.

    Every non-whitespace character must appear the same number of times in
    both strings (punctuation still counts). Two empty or whitespace-only
    strings are anagrams of each other.
    """

    def normalize(text: str) -> list[str]:
        return sorted(ch for ch in text.casefold() if not ch.isspace())

    return normalize(a) == normalize(b)


def reverse_words(text: str) -> str:
    """Words of ``text`` in reverse order, joined by single spaces.

    Runs of whitespace (including leading/trailing) are collapsed, so empty or
    whitespace-only input returns ``""``.
    """
    return " ".join(reversed(text.split()))


def title_case(text: str) -> str:
    """``text`` with each whitespace-separated word capitalised.

    The first character of every word is upper-cased and the rest lower-cased.
    Only whitespace delimits words (so ``"don't"`` becomes ``"Don't"``, unlike
    ``str.title``), and the original whitespace between words is preserved.
    """
    out = []
    at_word_start = True
    for ch in text:
        if ch.isspace():
            out.append(ch)
            at_word_start = True
        elif at_word_start:
            out.append(ch.upper())
            at_word_start = False
        else:
            out.append(ch.lower())
    return "".join(out)
