from sandbox import count_consonants, count_vowels


def test_count_consonants():
    assert count_consonants("hello world") == 7
    assert count_consonants("bcdfg") == 5


def test_count_consonants_either_case():
    assert count_consonants("BCDFG") == 5
    assert count_consonants("HeLLo WoRLD") == 7


def test_count_consonants_empty():
    assert count_consonants("") == 0


def test_count_consonants_only_vowels():
    assert count_consonants("aeiou AEIOU") == 0


def test_count_consonants_ignores_non_letters():
    assert count_consonants("123 !? \t\n") == 0
    assert count_consonants("b2c3-d!") == 3


def test_count_consonants_y_is_consonant():
    assert count_consonants("y Y") == 2
    assert count_consonants("rhythm") == 6


def test_count_consonants_ascii_only():
    # Non-ASCII letters are neither vowels nor consonants here.
    assert count_consonants("éàüñß") == 0
    assert count_consonants("niño") == 1


def test_count_consonants_complements_count_vowels():
    text = "The Quick Brown Fox, 42 times!"
    letters = sum(1 for ch in text if ch.isascii() and ch.isalpha())
    assert count_consonants(text) + count_vowels(text) == letters


def test_count_consonants_returns_int():
    assert isinstance(count_consonants("banana"), int)
    assert count_consonants("banana") == 3
