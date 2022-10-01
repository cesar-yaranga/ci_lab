from src import math_func


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(2) == 4


def test_product():
    assert math_func.product(4, 2) == 8
    assert math_func.product(4, 3) == 12


def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hello" in result
