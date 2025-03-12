
# Multiple Inheritance 
# Passing object of one or more class to another class (Sub Class)

class Employee_id:
    def emp_id(self, id):
        self.id = id


class Employee_DOB:
    def emp_dob(self, dob):
        self.dob = dob


class Employee_name(Employee_DOB, Employee_id):
    def emp_name(self, empName):
        self.empName = empName

    def show(self):
        print("{} : {} : {}".format(self.empName, self.id, self.dob))


d = Employee_name()
d.emp_name("Durga")
d.emp_id("0032")
d.emp_dob("25/02/1998")
d.show()

# OP
# Durga : 0032 : 25/02/1998