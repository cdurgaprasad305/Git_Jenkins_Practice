# Multi Level InInheritance
# Passing object of one class to another class (Sub Class)


class Employee:
    def employee_name(self, emp_name):
        self.emp_name = emp_name


class Employee_id(Employee):
    def emp_id(self, id):
        self.id = id


class Employee_DOB(Employee_id):
    def emp_dob(self, dob):
        self.dob = dob

    def show(self):
        print("{} : {} : {}".format(self.emp_name, self.id, self.dob))


d = Employee_DOB()
d.employee_name("Suresh")
d.emp_id("0032")
d.emp_dob("25/02/1998")
d.show()

# OP:
# This is a demo function
# The value of a inside class : 50
# The value of b inside class and show function  : 100
# Ronny - Mathematics - 80
# Jerry - Mathematics - 90
# Jerry - Mathematics - 90
