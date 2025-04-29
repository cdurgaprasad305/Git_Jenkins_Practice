import pytest
import tkinter as tk
from tkinter import messagebox
# Initialize the Tkinter application
root = tk.Tk()
root.withdraw()  # Hide the root window

# Use the messagebox
messagebox.showinfo("Title", "This is a message box!")

"""
def add1(a,b):
    return (a+b)

def test_verify():
    res1 = add1(10, 20)
    assert res1 == 30, "Test case failed"
    print("----------Assertion passed")

@pytest.mark.skip("Skipping this test case")
def test_skip():
    res2 = add1(20, 30)
    assert res2 == 50, "Test case failed"
"""


class TestDemo:

    @pytest.mark.parametrize("a, b, expected", [(10, 20, 30), (20, 30, 50), (30, 40, 70)])
    @pytest.mark.order(7)
    def test_add(self,a, b, expected):
        res = a + b
        assert res == expected, f"Test case failed for {a} + {b}"
        print(f"Test case passed for {a} + {b}")


    @pytest.mark.parametrize("a, b, expected", [(10, 20, -10), (20, 30, -10), (30, 40, -10)])
    @pytest.mark.order(5)
    def test_subtract(self,a, b, expected):
        res = a - b
        assert res == expected, f"Test case failed for {a} - {b}"
        print(f"Test case passed for {a} - {b}")


    @pytest.mark.parametrize("a, b, expected", [(10, 20, 200), (20, 30, 600), (30, 40, 1200)])
    @pytest.mark.order(3)
    def test_multiply(self,a, b, expected):
        res = a * b
        assert res == expected, f"Test case failed for {a} * {b}"
        print(f"Test case passed for {a} * {b}")


    @pytest.mark.parametrize("a, b, expected", [(10, 20, 0.5), (20, 10, 2), (30, 10, 3)])
    @pytest.mark.order(2)
    def test_divide(self,a, b, expected):
        res = a / b
        assert res == expected, f"Test case failed for {a} / {b}"
        print(f"Test case passed for {a} / {b}")


    @pytest.mark.parametrize("a,b,exp", [(10, 20, 30), (40, 50, 90)])
    @pytest.mark.order(1)
    def test_addition1(self,a, b, exp):
        p = add1(a, b)
        assert exp == p, "Fail in add"
        print("------------Test case passed for addition1")


def add1(c, d):
    res = c + d
    return res


    def test_first():
            print("This is the first test case")
            assert True



    def test_second():
        print("This is the 2 test case")
        assert True


    @pytest.mark.dependency(depends=["test_first"])
    def test_three():
        print("This is the 3 test case")
        assert True

