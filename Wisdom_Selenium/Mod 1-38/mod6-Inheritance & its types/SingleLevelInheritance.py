# Single Level InInheritance
# Passing object of one class to another class (Sub Class)

class Employee:
    def emp_name(self, empName):
        self.empName = empName


class Employee_id(Employee):
    def emp_id(self, id):
        self.id = id

    def show(self):
        print("{} : {}".format(self.empName, self.id))


i = Employee_id()
i.emp_name("Durga")
i.emp_id("0032")
i.show()

# OP
# Durga : 0032