from tools.calculator import calculate
from tools.file_reader import read_file


def test_calculator():
    assert calculate("2+3") == 5


def test_invalid_calculator():
    result = calculate("2+/3")
    assert "Error" in result


def test_file_reader():
    content = read_file("notes.txt")
    assert "AI" in content