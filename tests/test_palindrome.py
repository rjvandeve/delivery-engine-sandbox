from sandbox import is_palindrome


def test_is_palindrome():
    assert is_palindrome("abba")
    assert is_palindrome("Never odd or even")
    assert not is_palindrome("abc")


def test_is_palindrome_ignores_case():
    assert is_palindrome("Abba")
    assert is_palindrome("RaceCar")


def test_is_palindrome_ignores_all_whitespace():
    assert is_palindrome("taco cat")
    assert is_palindrome(" a\tb\nb a ")


def test_is_palindrome_empty_and_whitespace_only():
    assert is_palindrome("")
    assert is_palindrome("   ")


def test_is_palindrome_keeps_punctuation_significant():
    # Only case and whitespace are ignored; punctuation still counts.
    assert not is_palindrome("ab,a")
