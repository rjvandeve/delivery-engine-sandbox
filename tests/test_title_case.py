from sandbox import title_case


def test_title_case():
    assert title_case("hello world") == "Hello World"
    assert title_case("one two three") == "One Two Three"


def test_title_case_lowercases_rest_of_word():
    assert title_case("hELLO wORLD") == "Hello World"
    assert title_case("PYTHON") == "Python"


def test_title_case_preserves_whitespace():
    assert title_case("  a   b\t\tc\n d  ") == "  A   B\t\tC\n D  "


def test_title_case_empty_and_whitespace_only():
    assert title_case("") == ""
    assert title_case("   \t\n ") == "   \t\n "


def test_title_case_only_whitespace_delimits_words():
    # Unlike str.title, apostrophes/hyphens/digits do not start a new word.
    assert title_case("don't stop") == "Don't Stop"
    assert title_case("well-known 3rd") == "Well-known 3rd"
