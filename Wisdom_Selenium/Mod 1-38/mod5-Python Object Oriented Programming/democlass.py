# create a function
def demo_function():
    print("This is a demo function")


demo_function()  # calling Demo_function


class DemoClass:
    a = 50

    def show(self):
        print("The value of a inside class :", self.a)
        # Calling Class Variable using self keyword
        b = 100
        print("The value of b inside class and show function  :", b)


DemoClass().show()  # calling show function with DemoClass


class Student:
    # to initialize common variable
    # name, roll no, class, sub, sub teacher, class incharge, theory, practical, assessment

    def __init__(self, subject):  # Parameterized Constructor
        self.subject = subject
        # default, parameterized
        # print("demo of default constructor)"

    def student_name(self, name):  # Function inside the class
        self.name = name

    def student_marks(self, marks):
        self.marks = marks

    def show(self):
        print(self.name + " - " + self.subject + " - " + str(self.marks))
        # calling function parameters in the same class


# Student().studentname("Ronn")
# Student().studentmarks(80)

s1 = Student("Mathematics")  # Creating object s1 for Student class with parameter
s1.student_name("Ronny")
s1.student_marks(80)
s1.show()

s2 = Student("Mathematics")
s2.student_name("Jerry")
s2.student_marks(90)
s2.show()

s1 = s2  # here s2 object is mapping to s1
s1.show()  # s2 object values are displayed

# OP:
# This is a demo function
# The value of a inside class : 50
# The value of b inside class and show function  : 100
# Ronny - Mathematics - 80
# Jerry - Mathematics - 90
# Jerry - Mathematics - 90
