# Over Riding
# Same Function Name with different parament argument


class Employee:
    def emp_name(self, empName):
        self.empName = empName

    def emp_name(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Employee_id(Employee):
    def emp_id(self, id):
        self.id = id

    # def emp_name(self, empName):
    #     self.empName = empName

    def emp_name(self, firstname, lastname=None):
        super().emp_name(firstname, lastname)

    def show(self):  # Refactor 'show' method for consistency
        print(f"{self.firstname} {self.lastname} : {self.emp_id}")


e = Employee_id()
e.emp_name("Durga")
e.emp_id("0032")
e.show()
print("= = = = = = = = = = = = =  = = = =")
e.emp_name("Pankaj", "Kumar")
e.show()
print("= = = = = = = = = = = = =  = = = =")
e.emp_name("Varhsa")
e.show()
e.emp_name("Durga", "Prasad")
e.show()
