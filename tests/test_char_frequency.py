from sandbox import char_frequency


def test_case_folding_by_default():
    assert char_frequency("AaBb!") == {"a": 2, "b": 2, "!": 1}


def test_ignore_case_false_keeps_case():
    assert char_frequency("AaBb", ignore_case=False) == {"A": 1, "a": 1, "B": 1, "b": 1}


def test_whitespace_excluded():
    assert char_frequency(" a\tb\n a \r\n") == {"a": 2, "b": 1}


def test_whitespace_only_returns_empty():
    assert char_frequency(" \t\n") == {}


def test_empty_input():
    assert char_frequency("") == {}
    assert char_frequency("", ignore_case=False) == {}
