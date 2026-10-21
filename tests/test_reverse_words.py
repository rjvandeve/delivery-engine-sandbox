from sandbox import reverse_words


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"


def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"


def test_reverse_words_collapses_whitespace():
    assert reverse_words("  a   b\t\tc\n d  ") == "d c b a"


def test_reverse_words_empty_and_whitespace_only():
    assert reverse_words("") == ""
    assert reverse_words("   \t\n ") == ""


def test_reverse_words_keeps_words_intact():
    # Words themselves are not reversed; punctuation stays attached.
    assert reverse_words("Hello, world!") == "world! Hello,"
