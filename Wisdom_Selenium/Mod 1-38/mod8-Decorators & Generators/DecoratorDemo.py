# Decorators
# Decorators are function, which can be access using '@' followed by function name
# these Decorators have some generic functions code..


def smart_div(func):
    def inner(self, a, b):
        print("Dividing two numbers ", a, " and ", b)
        if b == 0:
            print("Division not possible")
            quit()

        return func(self, a, b)

    return inner


class division:
    @smart_div
    def div(self, a, b):
        print("Text in div function")  # if b=0 this function will not run
        output = a / b
        return output


d = division()
print(d.div(56, 1))

# OP:
# Dividing two numbers  56  and  1
# Text in div function
# 56.0

# Dividing two numbers  56  and  0
# Division not possible
