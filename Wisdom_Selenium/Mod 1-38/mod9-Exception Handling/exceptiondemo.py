# Exception
# If we are using try...block, then except or finally block any one is mandatory
# if we are not using except block and any exception raise code inside finally block
# will execute, and it will not execute the remaining lines in main function

x = input("Enter num 1 : ")
y = input("Enter num 2 : ")

try:
    result = int(x) / int(y)

except ZeroDivisionError as z:
    print("---0 denominator---", z)
    result = None

except ValueError as a:
    print("----denominator is not a number-----", a)
    result = None

except Exception as e:
    print("----Super Class Exception -----", e)  # this we have to keep as last.. as it is Super class exception
    result = None

finally:
    print(result)

# files : txt, excel, etc
# file not found, permission error

try:
    path = "D:\\Jaspreet\\demo.txt"
    filepath = open(path, "w")
    filepath.write("Exception handling for files......")
    filepath = open(path, "r")
    print(filepath.read())
except Exception as e:
    print("-----Exception Description---- ", e)
finally:
    try:
        filepath.close()
    except Exception as e:
        print("-----Finally block message----", e)
print("-----End of Program----")


# OP:
# Enter num 1 : 10
# Enter num 2 : 0
# ----Super Class Exception ----- division by zero
# None
# -----Exception Description----  [Errno 2] No such file or directory: 'D:\\Jaspreet\\demo.txt'
# -----Finally block message---- name 'filepath' is not defined
# -----End of Program----
