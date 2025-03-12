x = 40  # global variable
result = x * 3
print("X value in Global before Function execution :", result)
# original_x = x
# Store global x in another variable to preserve its original value


def local_function():
    global x  # if we have not provided this condition we encounter error
    fun_result = x * 2  # result = local variable
    print("X value from Function :", fun_result)
    x = 15
    print("X value in Local :", x)


local_function()
print("X value in Global after Function execution :", x)

# op:
# X value in Global before Function execution : 120
# X value from Function : 80
# X value in Local : 15
# X value in Global after Function execution : 15
