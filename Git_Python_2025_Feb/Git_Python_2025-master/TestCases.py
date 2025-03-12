# from selenium import webdriver
#
# driver = webdriver.Chrome("C://first//")
#
# driver.get("https://www.google.com/")`
# driver.back()


# x = 20  # Global variable
# def func1():
#     print("The Value of x in Global scope: "+str(x))  # Accessing global variable

# func1()
# OP:
# The Value of x in Global scope: 20


def outer_func():
    x = 10  # x is in the enclosing scope (non-local for inner_func)
    print("The value of x from Outer Function : " + str(x))

    def inner_func():
        # nonlocal x  # Refers to 'x' in the enclosing scope
        # x =10  # Modifies the non-local variable
        print("The Value of X from Inner Function  :", x)

    inner_func()
    print("Outer x:", x)


outer_func()
