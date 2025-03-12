

class Operation:
    def __init__(self): # Constructor
        self.a = 80  # Default public variables
        self.b = 59
        self._c = 10  # Protected Variable
        self._d = 20
        self.__e = 63  # Private Variable
        self.__f = 85

    def add(self): # Self will come automatically if the function inside the class
        total = self.a + self.b
        print("The total is : " + str(total) + " with public variables")

    def add_p(self):
        total = self._c + self._d
        print("The total is : " + str(total) + " with protected variables")

    def add_pp(self):
        total = self.__e + self.__f # Usage of Private variables
        return total


        # print("The total is : "+str(total)+" with private variables")


class output:
    o = Operation()

    def __sum_pp(self):
        return self.o.add_pp()

    def total(self):
        return self.__sum_pp()


o = output()
print(o.total())


o=Operation()
o.add()
o.add_p()
o.add_pp()

# OP:
# 148
# The total is : 139 with public variables
# The total is : 30 with protected variables


