import pytest

@pytest.mark.random
def test_demo():
    print("Demonstrating test cases")

@pytest.mark.alphabets
def test_a():
    print("a")

@pytest.mark.alphabets
def test_c():
    print("c")

@pytest.mark.alphabets
def test_d():
    print("d")

@pytest.mark.alphabets
def test_b():
    print("b")


# ============================= test session starts =============================
# collecting ... collected 5 items
#
# test_multiple.py::test_demo Demonstrating test cases
# test_multiple.py::test_a a
# PASSED
# test_multiple.py::test_c c
# PASSED
# test_multiple.py::test_d d
# PASSED
# test_multiple.py::test_b b
# PASSED
#
# ======================== 5 passed, 5 warnings in 0.03s ========================
