import pytest


@pytest.fixture()
def setup():
    global num1, num2
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    print("---Before Yield function---")
    yield
    print("----Output : " + str(result))
    print("\n---After Yield function---")


@pytest.mark.order(2)
def test_add(setup):
    global result
    print("Addition")
    result = int(num1) + int(num2)


@pytest.mark.order(1)
def test_difference(setup):
    global result
    print("Subtraction")
    result = int(num1) - int(num2)

# OP:
# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_ordering.py::test_difference Enter num 1 : Enter num 2 : ---Before Yield function---
# Subtraction
# PASSED----Output : -10
#
# ---After Yield function---
#
# test_ordering.py::test_add Enter num 1 : Enter num 2 : ---Before Yield function---
# Addition
# PASSED----Output : 50
# ---After Yield function---
# ======================== 2 passed, 2 warnings in 7.63s ========================