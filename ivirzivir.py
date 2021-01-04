import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
def test_multiplication(a, b, expected):
    assert a * b == expected

    def test_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
            1 / 0


def test_set_comparison():
    set1 ="abcd"
    #set2 = set("8035")
    assert set1 == "abc"
