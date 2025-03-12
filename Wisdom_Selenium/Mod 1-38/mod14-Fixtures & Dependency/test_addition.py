# When yield used in a function, `yield` transforms the function into a **generator**.
# A generator is an iterator that produces items (one at a time) rather than
# computing them all at once and storing them in memory.
# Key Features of `yield`:
# - When the function is called, execution starts from the top and runs until the `yield` statement.
# - Each time `next()` is called on the generator, the function resumes right after the
# last `yield` statement, retaining its state (e.g., local variable values).

# In pytest, the `yield` keyword is used within fixtures for **setup** and **teardown** purposes.
# The code before the `yield` runs during the fixture setup, while the code
# after `yield` is executed during the teardown phase (cleanup) after the test completes.


import pytest


@pytest.fixture()
def setup():
    global num1, num2
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    print("----Before Checking Yield function----")
    yield  # execution stops here...
    print("----After Checking Yield function----")
    print("Output : " + str(result))


def test_add(setup):
    global result
    result = int(num1) + int(num2)
    print("--test_add function--")


def test_difference(setup):
    global result
    result = int(num1) - int(num2)
    print("--test_difference function--")


def test_product(setup):
    global result
    result = int(num1) * int(num2)
    print("--test_product function--")


# OP:
# ============================= test session starts =============================
# collecting ... collected 3 items
#
# test_addition.py::test_add Enter num 1 : Enter num 2 : ----Before Checking Yield function----
# --test_add function--
# PASSED----After Checking Yield function----
# Output : 30
#
# test_addition.py::test_difference Enter num 1 : Enter num 2 : ----Before Checking Yield function----
# --test_difference function--
# PASSED----After Checking Yield function----
# Output : 10
#
# test_addition.py::test_product Enter num 1 : Enter num 2 : ----Before Checking Yield function----
# --test_product function--
# PASSED----After Checking Yield function----
# Output : 2475

# ============================== 2 passed in 7.38s ==============================
