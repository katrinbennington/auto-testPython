import pytest

from string_utils import StringUtils


def test_capitilize():
    # Arrange
    string_utils = StringUtils()
    input_string = "skypro"

    # Act
    result = string_utils.capitilize(input_string)

    # Assert
    assert result == "Skypro"

@pytest.mark.xfail
def test_capitilize_middle():
    # Arrange
    string_utils = StringUtils()
    input_string = "skYpro"

    # Act
    result = string_utils.capitilize(input_string)

    # Assert
    assert result == "Skypro"


def test_trim():
    # Arrange
    string_utils = StringUtils()
    input_string = " skypro"

    # Act
    result = string_utils.trim(input_string)

    # Assert
    assert result == "skypro"


def test_trim_two_spaces():
    # Arrange
    string_utils = StringUtils()
    input_string = "  skypro"

    # Act
    result = string_utils.trim(input_string)

    # Assert
    assert result == "skypro"


def test_trim_space_and_dot():
    # Arrange
    string_utils = StringUtils()
    input_string = " .skypro"

    # Act
    result = string_utils.trim(input_string)

    # Assert
    assert result == ".skypro"


def test_to_list_comas():
    # Arrange
    string_utils = StringUtils()
    input_string = "a,b,c,d"

    # Act
    result = string_utils.to_list(input_string)

    # Assert
    assert result == ["a", "b", "c", "d"]


def test_to_list_colon():
    # Arrange
    string_utils = StringUtils()
    input_string = "1:2:3"
    delimeter = ":"

    # Act
    result = string_utils.to_list(input_string, delimeter)

    # Assert
    assert result == ["1", "2", "3"]


def test_to_list_with_multiple_words():
    # Arrange
    string_utils = StringUtils()
    input_string = "Hello,World"

    # Act
    result = string_utils.to_list(input_string)

    # Assert
    assert result == ["Hello", "World"]


def test_delete_one_symbol():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "k"

    # Act
    result = string_utils.delete_symbol(input_string, symbol)

    # Assert
    assert result == "SyPro"


def test_delete_word_fragment():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "Pro"

    # Act
    result = string_utils.delete_symbol(input_string, symbol)

    # Assert
    assert result == "Sky"


def test_contains_true():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "S"

    # Act
    result = string_utils.contains(input_string, symbol)

    # Assert
    assert result == True


def test_contains_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "U"

    # Act
    result = string_utils.contains(input_string, symbol)

    # Assert
    assert result == False


def test_contains_true_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "s"

    # Act
    result = string_utils.contains(input_string, symbol)

    # Assert
    assert result == True


def test_delete_symbol():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "k"

    # Act
    result = string_utils.delete_symbol(input_string, symbol)

    # Assert
    assert result == "SyPro"


def test_delete_word_fragment():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "Pro"

    # Act
    result = string_utils.delete_symbol(input_string, symbol)

    # Assert
    assert result == "Sky"


def test_delete_double_symbol():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkkyProk"
    symbol = "k"

    # Act
    result = string_utils.delete_symbol(input_string, symbol)

    # Assert
    assert result == "SyPro"


def test_starts_with_true():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "S"

    # Act
    result = string_utils.starts_with(input_string, symbol)

    # Assert
    assert result == True


def test_starts_with_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "P"

    # Act
    result = string_utils.starts_with(input_string, symbol)

    # Assert
    assert result == False


def test_starts_with_true_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "s"

    # Act
    result = string_utils.starts_with(input_string, symbol)

    # Assert
    assert result == True


def test_end_with_true():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "o"

    # Act
    result = string_utils.end_with(input_string, symbol)

    # Assert
    assert result == True


def test_end_with_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "y"

    # Act
    result = string_utils.end_with(input_string, symbol)

    # Assert
    assert result == False


@pytest.mark.xfail
def test_end_with_true_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"
    symbol = "O"

    # Act
    result = string_utils.end_with(input_string, symbol)

    # Assert
    assert result == True

def test_is_empty_true():
    # Arrange
    string_utils = StringUtils()
    input_string = ""

    # Act
    result = string_utils.is_empty(input_string)

    # Assert
    assert result == True


def test_is_empty_two_spaces_true():
    # Arrange
    string_utils = StringUtils()
    input_string = " "

    # Act
    result = string_utils.is_empty(input_string)

    # Assert
    assert result == True


def test_is_empty_false():
    # Arrange
    string_utils = StringUtils()
    input_string = "SkyPro"

    # Act
    result = string_utils.is_empty(input_string)

    # Assert
    assert result == False

@pytest.mark.xfail
def test_list_to_string_numbers():
    # Arrange
    string_utils = StringUtils()
    input_string = "[1,2,3,4]"

    # Act
    result = string_utils.list_to_string(input_string)

    # Assert
    assert result == "1, 2, 3, 4"


def test_list_to_string_words():
    # Arrange
    string_utils = StringUtils()
    input_string = (["Sky", "Pro"])

    # Act
    result = string_utils.list_to_string(input_string)

    # Assert
    assert result == "Sky, Pro"


def test_list_to_string_dash():
    # Arrange
    string_utils = StringUtils()
    input_string = (["Sky", "Pro"])
    joiner = "-"

    # Act
    result = string_utils.list_to_string(input_string, joiner)

    # Assert
    assert result == "Sky-Pro"
