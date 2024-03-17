import pytest


def test_float_subtraction():
    a = 1.2
    b = 0.6
    assert a - b == 0.6


def test_float_negative_exponentiation():
    a = 0.2
    b = -1
    assert a ** b == 5.0


@pytest.mark.parametrize("a, b, expected", [
    (0.5, 2, 1.0),
    (1.5, -2, -3.0),
    (-3.0, 0, 0.0)
], ids=('1.0', '-3.0', '0.0'))
def test_float_multiplication(a, b, expected):
    assert a * b == expected
