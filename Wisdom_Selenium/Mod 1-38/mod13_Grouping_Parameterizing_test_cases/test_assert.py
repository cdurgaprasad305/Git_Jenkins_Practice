
# assert = actual result != expected result false + assertion error
import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,output", [(5, 6, 11), (96, 11, 107), (19, 2, 21)])
def test_calculate(a, b, output):
    result = add(a, b)
    print(f"The addition of {a} and {b} = {result}\n")
    assert output == result


def test_add():
    result = add(10,50)
    print("The sum of two numbers : ",result)
    assert 60==result

    result = add(20, 50)
    print("The sum of two numbers : ",result)
    assert 70 == result

    result = add(15, 50)
    print("The sum of two numbers : ",result)
    assert 65 == result

# OP:
# ============================= test session starts =============================
# collecting ... collected 4 items
#
# test_assert.py::test_calculate[5-6-11]
# test_assert.py::test_calculate[96-11-107]
# test_assert.py::test_calculate[19-2-21]
# test_assert.py::test_add The addition of 5 and 6 = 11
#
# PASSEDThe addition of 96 and 11 = 107
#
# PASSEDThe addition of 19 and 2 = 21
#
# PASSEDThe sum of two numbers :  60
# The sum of two numbers :  70
# The sum of two numbers :  65
# PASSED
#
# ============================== 4 passed in 0.03s ==============================