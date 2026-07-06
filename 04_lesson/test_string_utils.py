from string_utils import StringUtils

utils = StringUtils()


def test_capitilize_positive():
    assert utils.capitilize("skypro") == "Skypro"


def test_capitilize_empty():
    assert utils.capitilize("") == ""


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_without_spaces():
    assert utils.trim("skypro") == "skypro"


def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False


def test_delete_symbol_letter():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_word():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_contains_empty_string():
    assert utils.contains("", "S") is False


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "U") == "SkyPro"