import pytest

# ---TODO---
@pytest.fixture
def smart():
    global a, b
    a = input("Enter variable 1 : ")
    b = input("Enter variable 2 : ")
    yield
    print("- - - - - -  - - -- - -  -- ")


@pytest.mark.run(order=1)
def test_case_add(smart):
    result = int(a) + int(b)
    print("the Output is : " + str(result))


@pytest.mark.run(order=4)
def test_case_difference(smart):
    result = int(a) - int(b)
    print("the Output is : " + str(result))


@pytest.mark.run(after="test_case_difference")
def test_case_product(smart):
    result = int(a) * int(b)
    print("the Output is : " + str(result))


@pytest.mark.run(order=2)
def test_case_div(smart):
    result = int(a) / int(b)
    print("the Output is : " + str(result))

# OP:
# ============================= test session starts =============================
# collecting ... collected 4 items
#
# test_allureDemo.py::test_case_add Enter variable 1 : Enter variable 2 : the Output is : 30
# PASSED- - - - - -  - - -- - -  --
#
# test_allureDemo.py::test_case_difference Enter variable 1 : Enter variable 2 : the Output is : 10
# PASSED- - - - - -  - - -- - -  --
#
# test_allureDemo.py::test_case_product Enter variable 1 : Enter variable 2 : the Output is : 2430
# PASSED- - - - - -  - - -- - -  --
#
# test_allureDemo.py::test_case_div Enter variable 1 : Enter variable 2 : the Output is : 0.8333333333333334
# PASSED- - - - - -  - - -- - -  --
# ======================= 4 passed, 4 warnings in 20.25s ========================

