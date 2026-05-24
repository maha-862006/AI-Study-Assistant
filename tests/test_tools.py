from tools.calculator import calculate
from tools.file_reader import read_file

def test_calculator_valid():
    assert calculate("2+3") == 5

def test_calculator_invalid():
    assert "Error" in str(calculate("2+/3"))

def test_calculator_divide_by_zero():
    assert "Division by zero" in str(calculate("5/0"))

def test_file_reader_existing():
    content = read_file("notes.txt")
    assert len(content) > 0

def test_file_reader_missing():
    result = read_file("missing.txt")
    assert "Error" in result