import pytest


def div(a, b):
    return a / b


@pytest.mark.parametrize('num1,num2,result', [
    (10, 2, 5),
    (6, 3, 2),
    (1, 1, 1),
])
def test_div_int(num1, num2, result):
    assert div(num1, num2) == result


@pytest.mark.parametrize('num1,num2,result', [
    (-10, 2, -5),
    (6, -3, -2),
    (-1, -1, 1),
])
def test_div_fuint(num1, num2, result):
    assert div(num1, num2) == result


@pytest.mark.parametrize('num1,num2,result', [
    (1.1, 2, 0.55),
    (4, 0.5, 8),
    (9.9, 4.5, 2.2),
])
def test_div_float(num1, num2, result):
    assert div(num1, num2) == result


@pytest.mark.exception
@pytest.mark.parametrize('num1,num2,result', [
    ('a', 2, ''),
    (4, 'b', ''),
    ('a', 'b', ''),
])
def test_div_string(num1, num2, result):
    assert div(num1, num2) == result


@pytest.mark.exception
@pytest.mark.parametrize('num1,num2,result', [
    (0, 2, 0),
    (4, 0, 0),
])
def test_div_zero(num1, num2, result):
    assert div(num1, num2) == result
