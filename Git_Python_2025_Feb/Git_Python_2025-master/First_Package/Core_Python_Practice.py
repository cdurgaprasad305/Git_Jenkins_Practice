# Mobile Emulation
"""
options = Options()
options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")

input("Press Enter to Close")
driver.quit()
"""

import itertools
import logging
import math
import re
import time

# Constant Declarations
"""
PI = 3.14
URL = "https://www.google.com"
PATH = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"


def cons(pi_value=PI, app_url=URL, exe_path=PATH):
    print("The PI Value is: ", pi_value)
    print("The URL is: ", app_url)
    print("The Path is: ", exe_path)
    print("The updated PI Value is: ", pi_value + 2)  # We can update constant values


# OP:
# The PI Value is:  3.14
# The URL is:  https://www.google.com
# The Path is:  C:/Program Files (x86)/Google/Chrome/Application/chrome.exe
# The updated PI Value is:  5.140000000000001
cons()
"""

# Variable Declaration, Type check
"""
# Integer variable
age = 25

# Float Variable
price = 120.55

# String Variable
name = "Hari"

# Boolean Variable
is_employee = True

# Assign same value to multiple variable
p = y = z = 10

# Multiple variable with different values
a, b, c = 10, 20, 30

# Dynamic Variable value change
x = 10
print(x)
x = "Hello"
print(x)
x = 3.14
print(x)
print(type(x))

single_sting = "Hello"
print(type(single_sting))
double_string = "World"
print(type(double_string))
tripe_sting = Hello World contains many lines in
                  sample para info

print(type(tripe_sting))

# OP :
# 10
# Hello
# 3.14
# <class 'float'>
# <class 'str'>
# <class 'str'>
# <class 'str'>
"""

# List
"""
fruits = ["apple", "banana", "cherry"]  # Different data types allowed
numbers = [1, 2, 3, "Four", 2, 1]  # Duplicate allowed
print("The list elements : ", fruits)
print("The List values: ", numbers)
print("Type of the Variable: ", type(fruits))
print("Length of the list :", len(fruits))
print("Second order value in fruit :", fruits[1])
fruits.append("orange")
print("After appending the list :", fruits)
print("Second Element: ", fruits[1])

# OP :
# The list elements :  ['apple', 'banana', 'cherry']
# The List values:  [1, 2, 3, 'Four', 2, 1]
# Type of the Variable:  <class 'list'>
# Length of the list : 3
# Second order value in fruit : banana
# After appending the list : ['apple', 'banana', 'cherry', 'orange']
# Second Element:  banana
"""

# --The main difference between a list and tuple is that LIST is mutable and TUPLE is immutable.
# Tuple
"""
color = ("red", "yellow", "green", "red")  # Duplicate allowed
group_value = (10, 20, 30, "Fifty")  # Different data types allowed
# group_value.append(40) # OP: AttributeError: 'tuple' object has no attribute 'append'

print("The Tuple Values: ", group_value)
print("The type of the variable: ", type(color))
print("First Value :", color[0])
print("Length of the Tuple: ", len(color))

# OP:
# The Tuple Values:  (10, 20, 30, 'Fifty')
# The type of the variable:  <class 'tuple'>
# First Value : red
# Length of the Tuple:  4
"""

# Range
"""
r = range(1, 7)
print("Type of the variable: ", type(r))
print("The size of the Range: ", len(r))
print("The Second element of the range: ", r[1])
print("The last element of the range: ", r[-1])
print("The Second Last element of the range: ", r[-2])
try:
    print("The range values: ", r[8])  # IndexError: range object index out of range
except Exception as e:
    print("Exception Occurred: ", e)
print(list(r))

# OP:
# Type of the variable:  <class 'range'>
# The size of the Range:  6
# The Second element of the range:  2
# The last element of the range:  6
# The Second Last element of the range:  5
# Exception Occurred:  range object index out of range
# [1, 2, 3, 4, 5, 6]
"""

# ----Dictionary variable (key-value paris)
"""
user_info = {"name": "Ravi", "age": "28", "location": "Hyderabad", "2": "Two"}

print("Location : ", user_info["location"])
try:
    print("Other:",user_info["country"]) # KeyError: 'country'
except:
       print("Exception Occurred: ")

del user_info["age"]
print("After deleting the age: ", user_info)

if "name" in user_info:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")
user_info.clear() # Clear the dictionary

print("After clearing the dictionary: ", user_info)

# OP:
# Location :  Hyderabad
# Exception Occurred:  'country'
# After deleting the age:  {'name': 'Ravi', 'location': 'Hyderabad', '2': 'Two'}
# Name is present in the dictionary
# After clearing the dictionary:  {}
#----------------------------------------------

d = {"name": "John", "age": 25, "location": "USA"}

# Iterate over keys
for key in d.keys():
    print(key)  # "name", "age", "location"

# Iterate over values
for value in d.values():
    print(value)  # "John", 25, "USA"

# Iterate over key-value pairs
for key, value in d.items():
    print(key, value)  # ("name", "John","location"), etc.

print("----Items in Dictionary----",d.items())
# OP: ----Items in Dictionary---- dict_items([('name', 'John'), ('age', 25), ('location', 'USA')])

d1 = {"name": "John", "age": 25}
d2 = {"location": "USA", "age": 30}

# Update one dictionary with another
d1.update(d2)
print(d1)  # {'name': 'John', 'age': 30, 'location': 'USA'}

d = {"b": 2, "a": 1, "d": 3,"c":4}
print("Original Dictionary items: ",d.items())

# Sort by keys
sorted_keys = dict(sorted(d.items()))
print("Sorted Key: ",sorted_keys)

# Sort by values
sorted_values = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted Values: ",sorted_values)

# OP :
# Original Dictionary items:  dict_items([('b', 2), ('a', 1), ('d', 3), ('c', 4)])
# Sorted Key:  {'a': 1, 'b': 2, 'c': 4, 'd': 3}
# Sorted Values:  {'a': 1, 'b': 2, 'd': 3, 'c': 4}
"""

# ----Set
"""
# Creating a set
s = {1, 2, 3, 4, 5, 1, 2}
print(s)  # {1, 2, 3, 4, 5} # set will remove duplicate values

# Creating an empty set (use set(), not {})
s = set()
print(s)  # set()

# Sets with mixed data types
s = {1, 3.14, "hello", (1, 2)}  # Hashable items allowed
print(s)  # {1, 3.14, 'hello', (1, 2)}

# --Adding Elements
# Add a single element with `add()`
s.add(4)
print(s)

# Add multiple elements with `update()` (takes iterable inputs)
s.update([4, 5, 6])
print(s)

# Remove and clear elements
s.remove(3)
s.discard(5)  # No error even though 5 is not in the set
print(s)  # {1, 2, 3}

# Clear all elements from the set
s.clear()
print(s)  # set()
"""

# is and == operator
"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("Object value comparison : ", (x is y))
print("Object reference comparison : ", (x is z))
print("Variable Comparison with == :",x==y)

# OP:
# Object value comparison: False
# Object reference comparison: True
# Variable Comparison with ==: True

"""

# Typecasting - Convert one data type to another
"""
# From string to list
user_string = "John,Doe"
user_list = list(user_string)

print("User List: ", user_list)
print("The 4th element in the string", user_list[3])  # It will print the 4th element
# OP:
# User List:  ['J', 'o', 'h', 'n', ',', 'D', 'o', 'e']
# The 4th element in the string n

# From String to Set
my_str = "Sample text"
my_set = set(my_str)

print("Set from String: ", my_set)
# OP:
# Set from String:  {'e', 'S', 'm', 'p', 'x', 'a', 'l', 't'}
sorted_chars = "".join(sorted(set(my_set)))
print("Combined String: ", sorted_chars)  # Combined String:  Saelmptx

Unsorted_chars = "".join(set(my_set))
print("UnSorted Combined String: ", Unsorted_chars)  # UnSorted Combined String:  m aSlpetx

"""

# Finding only decimal value in the number
"""
a=105.7458
b=1
print(a/b) # 105.7458
print(a//b) # 105.0
print("The Decimal part in the number: ",round(a-(a//b),5))
# The Decimal part in the number:  0.7458
"""

# ----For Loop
"""
# for variable in sequence
# Code block to execute for each item

p = 1
fruits = ["apple", "mango", "banana"]
for i in fruits:
    print(p)
    print(fruits)
    print("India")
    print(i)
    p += 1

# OP:
# 1
# ['apple', 'mango', 'banana']
# India
# apple
# 2
# ['apple', 'mango', 'banana']
# India
# mango
# 3
# ['apple', 'mango', 'banana']
# India
# banana

# ----Nested For Loop
for i in range(4):
    print("----Outer loop value: ", i)
    for j in range(1, 4):
        print("Inner loop value: ", j)

# OP:
# ----Outer loop value:  0
# Inner loop value:  1
# Inner loop value:  2
# Inner loop value:  3
# ----Outer loop value:  1
# Inner loop value:  1
# Inner loop value:  2
# Inner loop value:  3
# ----Outer loop value:  2
# Inner loop value:  1
# Inner loop value:  2
# Inner loop value:  3
# ----Outer loop value:  3
# Inner loop value:  1
# Inner loop value:  2
# Inner loop value:  3

for i in itertools.count(1):  # Infinite Loop
    print(i)  # count(1) loop starts from 1
    if i == 5:
        break
# OP:
# 1
# 2
# 3
# 4
# 5

"""

# ----While Loop
"""
# while condition :
# Code block to execute

#--------------------
i = 0
while i < 10:
    print(i)
    i = i + 3
# OP:
# 0
# 3
# 6
# 9
#---------------------

i = 0
while i < 4:
    print("----Outer Loop: ", i)
    i = i + 1
    j = 1
    while j < 4:
        print("Inner Loop: ", j)
        j = j + 1
# OP:
# ----Outer Loop:  0
# Inner Loop:  1
# Inner Loop:  2
# Inner Loop:  3
# ----Outer Loop:  1
# Inner Loop:  1
# Inner Loop:  2
# Inner Loop:  3
# ----Outer Loop:  2
# Inner Loop:  1
# Inner Loop:  2
# Inner Loop:  3
# ----Outer Loop:  3
# Inner Loop:  1
# Inner Loop:  2
# Inner Loop:  3
"""

# Function to check if a number is prime and list range of prime numbers
"""

def is_prime(num):

    for i in range(2, int(num * 0.5) + 1):
        if num % i == 0:  # it will find the remainder
            return False
    return True


# Get all prime numbers up to n
def get_primes(n):
    primes = []
    for pnum in range(2, n + 1):
        if is_prime(pnum):
            primes.append(pnum)
    return primes


n = 50  # You can change this value
print("Prime numbers up to ", n, get_primes(n))
# OP:
# Prime numbers up to  50 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""

# Function Definition *args, **kwargs, @decorators
"""
x = 10

def loc_value():
    x = 20
    print("Local Variable value: ", x)  # 20


print("Global Variable value: ", x)  # 10
loc_value()

# ---------------------------
x = 10

def glob_value():
    global x
    x = 20
    print("Local Variable value: ", x)  # 20


glob_value()
print("Global Variable value: ", x)  # 20


# --------------------------
# Nested Function
def outer_func():
    print("----Outer Function")

    def inner_func():
        print("----Inner Function")

    inner_func()


outer_func()
# --------------------------


# Multiple Return Values
def multi_return_values(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val


my_sum, my_diff = multi_return_values(10, 20)
print("Sum: ", my_sum)
print("Difference: ", my_diff)


# OP:
# Sum:  30
# Difference:  -10

# --------------------------
# Function with Keyword arguments
def my_func(name, age=25):
    print("Name: ", name)
    print("Age: ", age)


my_func(name="John")
my_func(age=30, name="Hari")


# OP:
# Name:  John
# Age:  25
# Name:  Hari
# Age:  30
# --------------------------

# args functions
def arg_func(*args):
    print(args)

arg_func(1, 2, 3, "Durga", 4, "Prasad")
#  OP: (1, 2, 3, 'Durga', 4, 'Prasad')


# function with args and kwargs
def arg_func1(user, *args):
    print(user, args)


arg_func1("Ramesh", 1, 2, 3)

# OP:  Ramesh (1, 2, 3)

# -----------------------
# **kwargs functions

def user_info(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)

user_info(name="Alan",age=25,country="India")
# OP:
# name : Alan
# age : 25
# country : India

def user_info(**kwargs):
    print(kwargs)

user_info(name="Alan",age=25,country="India")
# OP: {'name': 'Alan', 'age': 25, 'country': 'India'}


def user_info(**kwargs):
    # Access a specific key directly
    name = kwargs.get('name')
    age = kwargs.get('age')

    return name, age


result = user_info(name='Alice', age=30, location='New York')
print(result)  # Output: ('Alice', 30)

# Function Decorators


def durga_info(func):
    def details():
        print("\n----Details from Durga Info")
        result = func()
        return result

    return details


@durga_info
def hari_info():
    print("----Hari Details")


hari_info()


@durga_info
def ram_info():
    print("----Ram Details")


ram_info()


@durga_info
def ravi_info():
    print("----Ravi Details")


ravi_info()

# OP:
# ----Details from Durga Info
# ----Hari Details
#
# ----Details from Durga Info
# ----Ram Details
#
# ----Details from Durga Info
# ----Ravi Details
"""

# Create a Class, Constructor, Instance Method, Class Method, Static Method
"""
class Car:
    var1 = 10  # Class variable

    def __init__(self, model):  # Constructor for initializing the attributes
        self.model = model
        self.int_var = 20  # we have to use self keyword

    def details(self):  # Instance Method
        print("Car Model: ", self.model)
        self.cost = 100000  # Class method variable or local variable

    def info1(self, c):
        print("Car Info", c)
        self.cost = 100125

    @staticmethod
    def add(a, b):  # Static method
        return a + b

    @staticmethod
    def multiply(a, b):  # Another static method
        return a * b


car1 = Car("BMW")  # Object creation for the Car class
car1.details()  # OP: Car Model:  BMW
car1.info1("Tata")  # OP: Car Info Tata

print("The Class variable value: ", car1.var1)  # OP: 10
print("Instant variable: ", car1.int_var)  # OP: 20
print("Variable value from class method: ", car1.cost)  # OP: 100000
# car1.cost variable is present in both method, but we got value from info1() method.

# Calling static methods without creating an object
print("Addition:", Car.add(5, 3))  # Output: 8
print("Multiplication:", Car.multiply(5, 3))  # Output: 15

# Static methods can also be called through objects (but not necessary)
print("Addition via object:", car1.add(10, 20))  # Output: 30
"""

# Inheritance, multilevel, multiple, Hierarchical,
"""
class Parent:
    def add1(self, x, y):
        print("--P--The sum of two numbers: ", x + y)


class Child(Parent):
    def sqr1(self, a):
        print("--C--The square of a numbers: ", a * a)


class GrandChild(Parent):
    def cube1(self, b):
        print("--GC--The cube of a numbers: ", b * b * b)
        super().add1(16, 23)  # Accessing Parent class method using super() or
        # Parent.add1(self, 16, 23) #Accessing Parent class method using Class Name


p1 = Parent()
p1.add1(10, 20)

c1 = Child()
c1.sqr1(10)
c1.add1(10, 20)

gc1 = GrandChild()
gc1.cube1(10)


# OP:
# --P--The sum of two numbers:  30
# --C--The square of a numbers:  100
# --P--The sum of two numbers:  30
# --GC--The cube of a numbers:  1000
# --P--The sum of two numbers:  39


# Multiple Inheritance
class Parent1:
    def add1(self, x, y):
        print("--P1--The sum of two numbers: ", x + y)
        return x + y


class Parent2:
    def add2(self, x, y):
        print("--P2--The Division of two numbers: ", x / y)
        return x + y


class Child(Parent1, Parent2):  # Multiple Inheritance
    def mul(self, x, y):
        print("--C--The multiplication of two numbers: ", x * y)
        return x * y


ch = Child()
ch.add1(10, 20)
ch.add2(10, 20)
ch.mul(10, 20)
# OP:
# --P1--The sum of two numbers:  30
# --P2--The Division of two numbers:  0.5
# --C--The multiplication of two numbers:  200


# Multilevel Inheritance
class Parent:
    def add1(self, x, y):
        print("--P--The sum of two numbers: ", x + y)
        return x + y


class Child(Parent):
    def sqr1(self, a):
        print("--C--The square of a numbers: ", a * a)
        return a * a


class GrandChild(Child): # Multilevel Inheritance
    def cube1(self, b):
        print("--GC--The cube of a numbers: ", b * b * b)
        return b * b * b


gc1 = GrandChild()
gc1.add1(10, 20)
gc1.sqr1(10)
gc1.cube1(10)
# OP:
# --P--The sum of two numbers:  30
# --C--The square of a numbers:  100
# --GC--The cube of a numbers:  1000

"""

# Method Overloading TODO ..
"""   
TODO...
"""

# Abstract Class
"""
from abc import ABC, abstractmethod


# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        #Calculate the area of the shape (must be overridden).
        pass

    @abstractmethod
    def perimeter(self):
        #Calculate the perimeter of the shape (must be overridden).
        pass


# Subclass implementing abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2  # π * r^2

    def perimeter(self):
        return 2 * 3.14 * self.radius  # 2πr


# Subclass implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Width * Height

    def perimeter(self):
        return 2 * (self.width + self.height)  # 2 * (Width + Height)


# Usage
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

#OP:
# Circle Area: 78.5
# Circle Perimeter: 31.400000000000002
# Rectangle Area: 24
# Rectangle Perimeter: 20
"""

# Static Method
"""
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

    def div1(self, a, b):
        return a / b


# Usage
result1 = MathUtils.add_numbers(5, 10)  # No instance needed
result2 = MathUtils.multiply_numbers(6, 7)

result3 = MathUtils().div1(10, 2)

# result3 = MathUtils().div(10, 2)

print("Sum:", result1)
print("Product:", result2)
print("Division:", result3)

# Instance Methods:** Non-static methods in Python are **instance methods** by default.
# These methods are designed to operate on the specific instance of a class
# (i.e., they have access to `self`, which holds the instance's data).


# OP:
# Sum: 15
# Product: 42
# Division: 5.0
"""

# Class Method TODO..
"""
TODO
"""

# With Statement
"""
# without using With statement
file = open("example.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()  # Ensures the resource is always released

# using with statement
with open("example.txt", "w") as file:
    file.write("Hello, World!")  # File is automatically closed after the block

"""

# Assertion, Logging
"""
# assert condition, optional_message
assert 5 == 5, "Simple check numbers"

# Configure logging to capture all levels and log to console and file (optional)
logging.basicConfig(level=logging.DEBUG,)  # Log messages starting from DEBUG level

# `level=logging.DEBUG`: This ensures that all messages
# (DEBUG, INFO, WARNING, ERROR, CRITICAL) are captured.

logging.info("Successfully logged in")
logging.error("Invalid username or password")
logging.critical("System is shutting down")
logging.warning("User is about to be logged out")
logging.debug("Logging out user")

# OP:
# INFO:root:Successfully logged in
# ERROR:root:Invalid username or password
# CRITICAL:root:System is shutting down
# WARNING:root:User is about to be logged out
# DEBUG:root:Logging out user
"""

# Regular expression, Date, Number, email_id
"""
# Sample text containing email addresses and dates 
text = """ """
Hello, you can reach us at support@example.com for support queries.or call 56897
Holiday on 2-3-2025 and reopens on 05-03-2025 For sales inquiries, call 8971568 
email sales@example.org or contact@example.co.in. your query will solve on 7-03-25
Thank you! reach on 9948612456
""" """

# ----Define a regular expression pattern to capture email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# ----Define a regular expression pattern to match numbers
number_pattern = r"\d+"

# Matches dd-mm-yyyy, dd/mm/yyyy, dd.mm.yyyy
# Regular expression for extracting dates in dd-mm-yyyy format
# date_pattern = r"\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b"
date_pattern = r"\b([0-9]|[0-2][0-9]|3[0-1])-(0?[1-9]|1[0-2])-(\d{2}|\d{4})\b"

# Use re.findall() to find all email addresses in the text
emails = re.findall(email_pattern, text)
phone_no = re.findall(number_pattern, text)
rg_date = re.findall(date_pattern, text)

# ----Display the extracted email addresses
print("Extracted Email Addresses:")
for email in emails:
    print(email)

# OP:
# Extracted Email Addresses:
# support@example.com
# sales@example.org
# contact@example.co.in

# ----Display the extracted Phone No.
print("Extracted Phone No: ")
for i in phone_no:
    print(i)
# OP:
# Extracted Phone No:
# 56897
# 8971568
# 9948612456

# ----Display the extracted Dates
print("Extracted Dates : ")
for dt in rg_date:
    print("-".join(dt))

# OP:
# Extracted Dates :
# 2-3-2025
# 05-03-2025
# 7-03-25


# Example text with mixed date formats
text = """ """
This is the sample text string contains different date formats 
2-11-25, 02-09-2025, 04-08-2025, 05-Feb-25, 08-Mar-2025, Mon-11-2025, 
""" """

# Regular expression to match all specified formats
date_pattern = (r"\b((\d{1,2}-(0?[1-9]|1[0-2])-(\d{2}|\d{4}))|(\d{2}-"
                r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-"
                r"(\d{2}|\d{4}))|((Mon|Tue|Wed|Thu|Fri|Sat|Sun)-\d{2}-"
                r"(\d{4})))\b")

# Extract all matching dates
dates = re.findall(date_pattern, text)

# Display the extracted dates
print("Extracted Dates:")
for match in dates:
    # Flatten match groups and remove empty entries
    extracted_date = next(filter(None, match))
    print(extracted_date)

#------------------------
# Given string
path = "/html/body/form/label/A/input"

# Regular expression to capture the last part (input) after the last '/'
match = re.search(r"[^/]+$", path)

# Print the output if there's a match
if match.group() in ("input",):
    print(match.group())  # Output: input

# ----------------------
"""

# try... except

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("file:///E:/Python%202024_7/First.html")

driver.find_element(By.XPATH , "//input[@type='radio' and @value = 'male' and @id='male']").click()

input("Press Enter to Close")
driver.quit()







