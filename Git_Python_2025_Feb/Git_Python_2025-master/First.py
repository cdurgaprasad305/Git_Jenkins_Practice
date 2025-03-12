"""
def add1():
    a=10
    b=20
    print("\nThe sum of two numbers: " +str(a+b))

def sub1():
        a = 10
        b = 20
        print("The Diff. of two numbers: " + str(a - b))

def mult1():
            a = 10
            b = 20
            print("The Product of two numbers: " + str(a * b))


# add1()
# sub1()
# mult1()
"""


def test_div():
    a = 10
    b = 2
    c = a / b
    print("------The Division of two numbers: " + str(c))


def test_first_add1():
    print("---> First Info <---")
    assert 10 == 10


def test_third_info():
    a = 10
    b = 4

    c = a / b
    d= a//b
    print("The Division of two numbers: " + str(c))
    print("The Floor Division of two numbers: " + str(d))
    print("---> third Info <---")
    assert c == 2.5


def test_second_info():
    print("---> Second Info <---")
    assert 10 == 10


# pytest "First.py" --maxfail=2

# The Execution of the program stops when it
# max fail reaches to 2
# Practice Push and pull in GIT
