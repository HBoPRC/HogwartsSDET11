import allure
import pytest

# 测试对象
def div(a, b):
    return a / b


# 参数化，这里验证正整数
@allure.suite('正整数验证')
@pytest.mark.parametrize('num1,num2,result', [
    (10, 2, 5),
    (6, 3, 2),
    (1, 1, 1),
])
def test_div_int(num1, num2, result):
    assert div(num1, num2) == result


# 这里验证负整数
@allure.suite('负整数验证')
@pytest.mark.parametrize('num1,num2,result', [
    (-10, 2, -5),
    (6, -3, -2),
    (-1, -1, 1),
])
def test_div_fuint(num1, num2, result):
    assert div(num1, num2) == result


# 这里验证浮点数
@allure.suite('浮点数验证')
@pytest.mark.parametrize('num1,num2,result', [
    (1.1, 2, 0.55),
    (4, 0.5, 8),
    (9.9, 4.5, 2.2),
])
def test_div_float(num1, num2, result):
    assert div(num1, num2) == result


# 这里验证字符串
@allure.suite('字符串验证')
@pytest.mark.exception
@pytest.mark.parametrize('num1,num2,result', [
    ('a', 2, ''),
    (4, 'b', ''),
    ('a', 'b', ''),
])
def test_div_string(num1, num2, result):
    with pytest.raises(TypeError):
        div(num1, num2)


# 被除数为0
@allure.suite('被除数0值验证')
@pytest.mark.exception
@pytest.mark.parametrize('num1,num2,result', [
    (0, 2, 0),
])
def test_div_string(num1, num2, result):
    assert div(num1, num2) == result


# 除数为0
@allure.suite('除数0值验证')
@pytest.mark.exception
@pytest.mark.parametrize('num1,num2,result', [
    (4, 0, 0),
])
def test_div_zero(num1, num2, result):
    with pytest.raises(ZeroDivisionError):
        div(num1, num2)
