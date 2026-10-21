from sandbox import is_anagram


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert is_anagram("evil", "vile")
    assert not is_anagram("abc", "abd")


def test_is_anagram_ignores_case():
    assert is_anagram("Listen", "Silent")
    assert is_anagram("DUSTY", "study")


def test_is_anagram_ignores_whitespace():
    assert is_anagram("dormitory", "dirty room")
    assert is_anagram("The eyes", "they see")
    assert is_anagram(" a\tb\nc ", "cba")


def test_is_anagram_requires_same_letter_counts():
    assert not is_anagram("aab", "abb")
    assert not is_anagram("abc", "abcc")


def test_is_anagram_empty_and_whitespace_only():
    assert is_anagram("", "")
    assert is_anagram("", "   ")
    assert not is_anagram("", "a")
    assert not is_anagram("a", "")


def test_is_anagram_keeps_punctuation_significant():
    # Only case and whitespace are ignored; punctuation still counts.
    assert not is_anagram("ab,", "ab")
    assert is_anagram("a,b", "b,a")
