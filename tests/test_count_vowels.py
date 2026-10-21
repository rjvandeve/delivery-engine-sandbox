from sandbox import count_vowels


def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("aeiou") == 5


def test_count_vowels_either_case():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("AeIoU aEiOu") == 10


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0
    assert count_vowels("xyz 123 !?") == 0


def test_count_vowels_only_aeiou_count():
    # y is not a vowel here; neither are accented letters.
    assert count_vowels("y Y") == 0
    assert count_vowels("éàü") == 0


def test_count_vowels_returns_int():
    assert isinstance(count_vowels("banana"), int)
    assert count_vowels("banana") == 3
