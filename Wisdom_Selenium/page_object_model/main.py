# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from testcases import test_login

"""
def print_hi(name):
    print(f"Hi, {name}")

if __name__ == "__main__":
    print_hi("PyCharm")
"""
# - This block ensures that the code below it will only execute if the script is
# run as the main program (not imported as a module in another script).
# - When the script is executed (using a Python interpreter or through the IDE),
# the block calls the `print_hi` function, passing `"PyCharm"` as the argument.
# -------------------

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


_i = 22
print("i value before for loop :", _i, "\n")
for __i in range(0, 3):
    pass  # pass keyword is used for empty for loop
    print("i value in side for loop ", __i)
print("\ni value after for loop: ", _i)

# OP:
# i value before for loop : 22
#
# i value in side for loop  0
# i value in side for loop  1
# i value in side for loop  2
#
# i value after for loop:  22
