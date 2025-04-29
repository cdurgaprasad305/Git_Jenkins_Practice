"""
from Durga_Package import a_pack
from Durga_Package.module1 import m1_first, var_m1_a

# from Durga_Package.moduel2 import m2_first
#
m1_first()
# m2_first()
print(a_pack)
print(var_m1_a)
print("-----Main function block----------")

import sys
import os

# Add the path to the other project
other_project_path = os.path.abspath("C:\\Users\\Admin\\OneDrive\\Desktop\\Tonny")
sys.path.append(other_project_path)
"""
"""
import allure
print(dir(allure))
'description', 'description_html', 'dynamic', 'epic', 'feature', 'id', 'issue', 
'label', 'link', 'manual', 'parameter_mode', 'parent_suite', 'severity', 
'severity_level','step', 'story', 'sub_suite', 'suite', 'tag', 'testcase', 'title']
"""

"""
a = 0
p = []
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "cherry", "pineapple"]
for fruit in fruits:
    a = a + 1
    if fruit == "cherry":
        p.append(a)

print("The position of Cherry:", p)


filename = "document.final.version.txt"
name, extension = filename.rsplit(".", 1)

print("Actual file:", filename)
print("File Name:", name)  # "document.final.version"
print("File extension:", extension)  # "txt"

# OP:
# Actual file: document.final.version.txt
# File Name: document.final.version
# File extension: txt



tp = (0,4,'i','o',78)
# typle methods ['count', 'index']
print(tp.count(4))

# Example usage of index() in a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)

# Find the index of the first occurrence of the value 2
index_of_2 = my_tuple.index(2)
print("Index of 2:", index_of_2)  # Output: 1

"""

a=[1,2,3,4,5,6]
print(a)
print(type(a))
print(sum(a))

