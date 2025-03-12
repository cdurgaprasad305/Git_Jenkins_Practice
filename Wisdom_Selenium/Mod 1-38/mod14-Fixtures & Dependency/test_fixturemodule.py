import pytest


@pytest.fixture(scope="module")
# if we provide scope, it wll display last method result only.
def setup():
    global num1, num2
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    yield
    print("Output : " + str(result))


def test_add(setup):
    global result
    result = int(num1) + int(num2)


def test_difference(setup):
    global result
    result = int(num1) - int(num2)


def test_product(setup):
    global result
    result = int(num1) * int(num2)


# OP:
# ============================= test session starts =============================
# collecting ... collected 3 items

# test_fixturemodule.py::test_add Enter num 1 : Enter num 2 : PASSED
# test_fixturemodule.py::test_difference PASSED
# test_fixturemodule.py::test_product PASSEDOutput : 200
#
# ============================== 2 passed in 4.17s ==============================
