# module name should be prefixed : test_ , batch,
# function - def test_
# class name should start with Test
import pytest

@pytest.mark.skip("Skipping the test case")
def test_demo():
    print("\n-----Skipping Demonstrating test cases---")
    print("----This will not print----")


def test_a():
    print("\n----Testcase from a module is passed---")


def test_b():
    print("\n----Testcase from b model is passed----")


# ============================= test session starts =============================
# collecting ... collected 3 items
#
# test_demo.py::test_demo SKIPPED (Skipping the test case)
# Skipped: Skipping the test case
#
# test_demo.py::test_a
# ----Testcase from a module is passed---
# PASSED
# test_demo.py::test_b
# ----Testcase from b model is passed----
# PASSED
#
# ======================== 2 passed, 1 skipped in 0.02s =========================
