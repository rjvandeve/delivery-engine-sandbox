from sandbox import is_palindrome


def test_is_palindrome():
    assert is_palindrome("abba")
    assert is_palindrome("Never odd or even")
    assert not is_palindrome("abc")
