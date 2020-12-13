def div(a, b):
    return a / b


def test_result1():
    assert div(1, 1) == 1


def test_result2():
    assert div(1, 0) == 1 / 0


def test_result3():
    assert div('a', 'b') == 'a' / 'b'
