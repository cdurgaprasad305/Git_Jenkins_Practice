from collections import Counter

# Replace function

# ---------------------------------
usr_str = "Hi I am Gandhi, I stay in Gandhi Nagar and studied in Gandhi High School"
rl_str = usr_str.replace("Gandhi", "Ram", 2)
print(rl_str)

# OP:
# Hi I am Ram, I stay in Ram Nagar and studied in Gandhi High SchoolSchool
# ---------------------------------
my_st = "Hyderabad"
ch = my_st.replace("d", "p", 1)
print("Original String: ", my_st)
print("After replacing the characters in the String d with p for 1 occurrence :", ch)
print("Printing the set of Characters from the string: ", my_st[0:4])
# OP:
# Original String: Hyderabad
# After replacing the characters in the String d with p for 1 occurrence: Hyperabad
# Printing the set of Characters from the string:  Hyde

# ---------------------------------


# swapping two numbers with using third variable

a = 10
b = 20
print("---Before swapping---")
print("a:", a)
print("b:", b)

c = b
b = a
a = c
print("---After swapping---")
print("a: ", a)
print("b: ", b)

# OP:
# ---Before swapping---
# a: 10
# b: 20
# ---After swapping---
# a:  20
# b:  10
# ---------------------------------

# swapping two numbers without using third variable
a = 10
b = 20
print("---Before swapping---")
print("a:", a)
print("b:", b)
a = a + b  # a = 30
b = a - b  # b = 10
a = a - b  # a = 20
print("---After swapping---")
print("a: ", a)  # 20
print("b: ", b)  # 10

# OP:
# ---Before swapping---
# a: 10
# b: 20
# ---After swapping---
# a:  20
# b:  10
# ---------------------------------


# ***** 1. Basic Python Coding Questions

# How do you print "Hello, World!" in Python?
print("Hello, World!")

# How do you take user input in Python?
x = input("Enter a value: ")

nu = int(input("Enter a number: "))
if nu == 5:
    print("Number is equal to 5")
elif nu > 5:
    print("Number is greater than 5")
else:
    print("Number is less than 5")

# How do you check if a number is even or odd?
x = int(input("Enter a number:"))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# How do you find the largest of three numbers?

a = int(input("Enter value for a :"))
b = int(input("Enter value for b :"))
c = int(input("Enter value for c :"))

if a > b and a > c:
    print("a is greater: ", a)
elif b > c:
    print("b is greater: ", b)
else:
    print("c is greater: ", c)

# * ----How do you reverse a string in Python?

rstr = "Reverse the text string"
print("Original String: ", rstr)
# rstr = rstr[::-1]
# print("Reversed String: ", rstr)
# OP:
# Original String:  Reverse the text string
# Reversed String:  gnirts txet eht esreveR
# ----------OR------------
rstr = "Reverse the text string"
rs = ""
for i in rstr:
    rs = i + rs
print("String Reverse: ", rs)
# # OP:
# Original String:  Reverse the text string
# String Reverse:  gnirts txet eht esreveR

# ---------OR-------------

rswd = "String reverse based on words"
split_str = rswd.split()
print("Original String: ", rswd)
for i in split_str:
    print(i, ":", i[::-1])

# OP:
# Original String:  String reverse based on words
# String : gnirtS
# reverse : esrever
# based : desab
# on : no
# words : sdrow

# ----------------------


# ----How do you check if a string is a palindrome?

palstr = "madam"
print("Actual String: ", palstr)
if palstr == palstr[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

    # OP:
    # Actual String:  madam
    # String is Palindrome
    # ----------------------


# How do you check if a number is prime? TODO...
# How do you find the factorial of a number? TODO...
# How do you generate the Fibonacci sequence up to n terms? TODO...


# *****2. String Manipulation Questions

# ----How do you count the number of vowels in a string?
vol_str = "This is a sample text string contains some vowels for user"
vol_set = {"a", "e", "i", "o", "u"}
print("Actual String: ", vol_str)
for i in sorted(vol_set):
    a_occ = vol_str.count(i)
    print(i, ":", a_occ)

# OP:
# Actual String:  This is a sample text string contains some vowels for user
# a : 3
# e : 5
# i : 4
# o : 4
# u : 1


def vol_count(vol_str):
    vol_set = {"a", "e", "i", "o", "u"}
    print("Actual String: ", vol_str)
    for i in sorted(vol_set):
        a_occ = vol_str.count(i)
        print(i, ":", a_occ)


vol_str = "This is a sample user string aeiouaeiou"
spl_str = vol_str.split()
for i in spl_str:
    vol_count(i)

# OP:
# Actual String:  This
# a : 0
# e : 0
# i : 1
# o : 0
# u : 0
# Actual String:  is
# a : 0
# e : 0
# i : 1
# o : 0
# u : 0
# Actual String:  a
# a : 1
# e : 0
# i : 0
# o : 0
# u : 0
# Actual String:  sample
# a : 1
# e : 1
# i : 0
# o : 0
# u : 0
# Actual String:  user
# a : 0
# e : 1
# i : 0
# o : 0
# u : 1
# Actual String:  string
# a : 0
# e : 0
# i : 1
# o : 0
# u : 0
# Actual String:  aeiouaeiou
# a : 2
# e : 2
# i : 2
# o : 2
# u : 2

# How do you remove spaces from a string?

sp_str = "   the quick brown fox jumps over the lazy dog     "
print("Actual String:", sp_str)
print("Modified String:", sp_str.replace(" ", ""))
# .strip(" ") it will remove the space from both side of the string not in between the string

# OP:
# Actual String:    the quick brown fox jumps over the lazy dog
# Modified String: thequickbrownfoxjumpsoverthelazydog

# ---- How do you count the number of words in a string?

sp_str = "the quick brown fox jumps over the lazy dog"

print("Actual String:", sp_str)
print("Total no.of words in string:", len(sp_str.split()))
print("Total no.of characters in string:", len(sp_str.replace(" ", "")))

# OP:
# Actual String: the quick brown fox jumps over the lazy dog
# Total no.of words in string: 9
# Total no.of characters in string: 35

# Inserting space for each word *#
import re

text = "thequickbrownfox"
words = ["the", "quick", "brown", "fox"]

# Reconstruct the sentence
pattern = "|".join(words)
print("The Pattern:", pattern)
formatted_text = " ".join(re.findall(pattern, text))
print(formatted_text)

# OP:
# The Pattern: the|quick|brown|fox
# the quick brown fox

# ----How do you replace all occurrences of a substring in a string?

rs_str = "test for the replace string to test"
print("Original String: ", rs_str)
rs_str = rs_str.replace("test", "Check")
print("Replaced String: ", rs_str)

# OP:
# Original String:  test for the replace string to test
# Replaced String:  Check for the replace string to Check


#Rsplit --- The rsplit() method splits a string into a list, starting from the right.
filename = "document.final.version.txt"
name, extension = filename.rsplit(".", 1)

print("Actual file:", filename)
print("File Name:", name)  # "document.final.version"
print("File extension:", extension)  # "txt"

# OP:
# Actual file: document.final.version.txt
# File Name: document.final.version
# File extension: txt



# This code takes a string and splits it into words, then prints each word in reverse order.
str1 = "This is a sample test string with vowels"
arr_str = str1.split(" ")

for i in range (len(arr_str)-1,-1,-1):
    print(arr_str[i], end=" ")

# OP:
# vowels with string test sample a is This


# ----How do you check if two strings are Paidrams?


# ---- How do you convert a string to title case?

str_title = "this is a sample string"
print("Original String:", str_title)
print("Title case String:", str_title.title())

# OP:
# Original String: this is a sample string
# Title case String: This Is A Sample String

# ----How do you extract digits from a string?


str1 = "This is a sample string with digits 1234 and some 567 text."
print("Original String: ", str1)

digits = [int(i) for i in str1 if i.isdigit()]
print("Digits in the string: ", digits)
# or

digits1 = ""
for i in str1:
    if i.isdigit():
        digits1 = i + digits1

print("Digit in the string: ", digits1)

# OP:
# Original String:  This is a sample string with digits 1234 and some 567 text.
# Digits in the string:  [1, 2, 3, 4, 5, 6, 7]
# Digit in the string:  7654321


#---- Counts total occurrence of S and s in the string
str1 = "Testing stringssSSS"
Cs_count = str1.count("S")
ss_count = str1.count("s")
print("Total occurrence of S and s in the string:", Cs_count + ss_count)

# OP:
# Total occurrence of S and s in the string: 7



# -----How do you remove punctuation from a string?

import string

text = "Hello, world! How's it going?"
clean_text = text.translate(str.maketrans("", "", string.punctuation))
print(clean_text)

text1 = "Hello, world! How's it going?"

special_chars_count = sum(1 for char in text1 if char in string.punctuation)
print("Special characters count:", special_chars_count)


# How do you reverse each word in a given string?
# ----How do you find the first non-repeating character in a string? TODO...


# *****3. List and Tuple Coding Questions

# ----How do you find the sum of elements in a list?

usr_li = [1, 2, 3, 4, 5]
print("User list: ", usr_li)
sum1 = 0
for i in usr_li:
    sum1 = sum1 + i
print("Sum of elements in a list: ", sum1)

# OP:
# User list:  [1, 2, 3, 4, 5]
# Sum of elements in a list:  15

# ----How do you find the maximum and minimum element in a list?
usr_li = [1, 2, 3, 4, 5, -10, 10.5]
print("User list:", usr_li)
max1 = min1 = usr_li[0]

for i in usr_li:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i
print("Max of elements in a list:", max1)
print("Min of elements in a list:", min1)

# OP:
# User list: [1, 2, 3, 4, 5, -10, 10.5]
# Max of elements in a list: 10.5
# Min of elements in a list: -10


# ----How do you remove duplicates from a list?
usr_li = [1, 2, 3, 4, 5, 10, 10.5, 3, 4, 10.5, 7, 3, 9]
print("User list:", usr_li)
usr_st = set(usr_li)
print("Unique set:", usr_st)

# OP:
# User list: [1, 2, 3, 4, 5, 10, 10.5, 3, 4, 10.5, 7, 3, 9]
# Unique set: {1, 2, 3, 4, 5, 7, 9, 10, 10.5}

p = []
for i in usr_st:
    if usr_li.count(i) > 1:
        p = p + [i]
print("Duplicate elements in the list:", p)

# OP:
# Duplicate elements in the list: [3, 4, 10.5]

# ---- How do you find the second-largest number in a list?
usr_li = [1, 2, 3, 4, 5, 10, 10.5, 3, 4, 10.5, 7, 3, 9, 10]
print("User list:", usr_li)
ssl = sorted(set(usr_li))
print("Sorted list:", ssl)
max1 = len(ssl)
print("Second largest number:", ssl[max1 - 2])

# OP:
# User list: [1, 2, 3, 4, 5, 10, 10.5, 3, 4, 10.5, 7, 3, 9, 10]
# Sorted list: [1, 2, 3, 4, 5, 7, 9, 10, 10.5]
# Second-largest number: 10

# ---- How do you merge two lists into one sorted list?
usr_li1 = [1, 2, 3, 4, 5, 10, 10.5, 3, 4, 10.5, 7, 3, 9, 10]
usr_li2 = [10, 20, 30, 4, 5, 10, 10.5, 3, 4, 10.5, 70, 3, 9, 100]

new_lst = usr_li1 + usr_li2
print("User list:", sorted(set(new_lst)))

# OP:
# User list: [1, 2, 3, 4, 5, 7, 9, 10, 10.5, 20, 30, 70, 100]

# ----How do you rotate a list by k positions? TODO...

# ---- How do you find the most frequent element in a list?
usr_li1 = [    1,    2,    2,    3,    3,    4,    5,3,    10,    3,    10.5,    3,    4,    3,    10.5,3,    7,    3,    9,    10,    1,    1,
               1,    1,    1,    1,    11,    1,3,]
cl = Counter(usr_li1)
print("All occurrence in the list:", cl)
print("Count of each occurrence of the number:", cl.most_common())
print("Most repeated element and its occurrence:", cl.most_common()[0])
print("Occurrence:", cl.most_common()[0][1])

# OP:
# All occurrence in the list: Counter({1: 8, 3: 6, 2: 2, 4: 2, 10: 2, 10.5: 2, 5: 1, 7: 1, 9: 1, 11: 1})
# Count of each occurrence of the number: [(1, 8), (3, 6), (2, 2), (4, 2), (10, 2), (10.5, 2), (5, 1), (7, 1), (9, 1), (11, 1)]
# Most repeated element and its occurrence: (1, 8)
# Occurrence: 8


# ---- How do you convert a list of tuples into a dictionary?

# List of tuples
tuples_list = [("a", 1), ("b", 2), ("c", 3)]

# Convert to dictionary
dictionary = dict(tuples_list)

print(dictionary)
# OP:
# {'a': 1, 'b': 2, 'c': 3}


# ---- How do you find common elements in two lists?
usr_li1 = [1, 2, 2, 3, 3, 4, 5, 10, 3, 10.8, 3, 4, 3, 10.5, 7, 3, 9, 10]
usr_li2 = [1, 3, 3, 4, 5, 3, 10.5, 3, 4, 3, 10.5, 7]

counter1 = Counter(usr_li1)
counter2 = Counter(usr_li2)
print(counter1) #Counter({3: 6, 2: 2, 4: 2, 10: 2, 1: 1, 5: 1, 10.8: 1, 10.5: 1, 7: 1, 9: 1})
print(counter2) #Counter({3: 5, 4: 2, 10.5: 2, 1: 1, 5: 1, 7: 1})

common_elements = list((counter1 & counter2).elements())
print("Common elements in two list:", common_elements)
# Output: [1, 3, 3, 3, 3, 3, 4, 4, 5, 10.5, 7]

# or
p = []
for i in sorted(set(usr_li1)):
    for j in sorted(set(usr_li2)):
        if i == j:
            p.append(i)
print(p)

# [1, 3, 4, 5, 7, 10.5]


# ----How do you flatten a nested list?

def flatten_recursive(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_recursive(item))
        else:
            flat_list.append(item)
    return flat_list


nested = [1, [2, [3, 4], 5], 6]
print(flatten_recursive(nested))  # Output: [1, 2, 3, 4, 5, 6]


# *****4. Dictionary and Set Coding Questions

# ---- How do you merge two dictionaries?
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
# or
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}


# ---- How do you sort a dictionary by values?

my_dict = {"apple": 3, "banana": 1, "cherry": 2, "biscuit": 4}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3, 'biscuit': 4}


sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)  # Output:{'biscuit': 4, 'apple': 3, 'cherry': 2, 'banana': 1}


item_dict = dict(sorted(my_dict.items()))
print("New:", item_dict)

key_dict = sorted(my_dict.keys())
print("New Keys :", key_dict)
# OP:
# New: {'apple': 3, 'banana': 1, 'biscuit': 4, 'cherry': 2}
# New Keys : ['apple', 'banana', 'biscuit', 'cherry']

# ---- How do you find the key with the maximum value in a dictionary?

my_dict = {"a": 10, "b": 25, "c": 15}

max_key = max(my_dict, key=my_dict.get)
print(max_key)  # Output: 'b'

my_dict1 = {"a": 10, "b": 25, "c": 15, "d": 25}
max_value = max(my_dict1.values())

max_keys = [key for key, value in my_dict1.items() if value == max_value]
print(max_keys)  # Output: ['b', 'd']

my_dict2 = {"a": 10, "b": 25, "c": 15, "d": 25}
max1 = max(my_dict2)
print("The max value in dict-", max1, ":", my_dict2["d"])

# OP:
# The max value in dict- d : 25


# ---- How do you count the occurrences of each character in a string using a dictionary?

from collections import Counter

text = "hello world"
char_count = Counter(text)

print("Dict count collection ", char_count)
# OP:
# Dict count collection  Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# ---- How do you remove a key from a dictionary?

my_dict = {"a": 1, "b": 2, "c": 3}
print("Actual Dictionary", my_dict)
del my_dict["b"]
print("After deleting 'b' in dic", my_dict)  # Output: {'a': 1, 'c': 3}
# OP:
# Actual Dictionary {'a': 1, 'b': 2, 'c': 3}
# After deleting 'b' in dic {'a': 1, 'c': 3}


# ---- How do you check if a key exists in a dictionary?

my_dict = {"a": 10, "b": 20, "c": 30}

if "b" in my_dict:
    print("Key exists!")
else:
    print("Key does not exist.")

# ---- How do you find the union, intersection, and difference of two sets?

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}


intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}


difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
difference_set = set2 - set1
print(difference_set)  # Output: {4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}


symmetric_diff = set1 ^ set2
print(symmetric_diff)  # Output: {1, 2, 4, 5}
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Output: {1, 2, 4, 5}

# ---- How do you find duplicate elements in a list using sets?

my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]

duplicates = {x for x in my_list if my_list.count(x) > 1}
print(duplicates)  # Output: {1, 2, 3}
p = []
for i in my_list:
    if my_list.count(i) > 1:
        p = p + [i]
print("Duplicate elements in a list: ", set(p))
# OP:
# Duplicate elements in a list:  {1, 2, 3}

# ----How do you convert a list to a set to remove duplicates?

my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# ----How do you check if two sets are disjoint?

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # Output: True (No common elements)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.isdisjoint(set2))  # Output: False (Common element: 3)


set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(len(set1 & set2) == 0)  # Output: True
# set1 & set2 gives the intersection.


# *****5. Loop and Iteration Coding Questions

# How do you print numbers from 1 to 100 using a loop?

for i in range(1, 101):
    print(i)

i = 1
while i <= 100:
    print(i)
    i += 1


print(*range(1, 101))
# Uses * (unpacking) to print numbers in a single line.


# ----- How do you print all even numbers from 1 to 50?

for i in range(2, 51, 2):  # Start at 2, go up to 50, step by 2
    print(i)


for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#---- for loop with range values
for i in range(3):
    print(i)
# OP
# 0
# 1
# 2

for i in range(1, 3):
    print(i)
# OP:
# 1
# 2

# ----- How do you generate a list of square numbers using a loop?
squares = []
for i in range(1, 11):  # Generate squares from 1² to 10²
    squares.append(i**2)

print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ----- How do you find the sum of digits of a number using a loop?
num = 12345
sum_digits = 0

while num > 0:
    sum_digits += num % 10  # Get last digit
    num //= 10  # Remove last digit

print(sum_digits)  # Output: 15
# --------- OR ------------

n1 = 0
num_str = "78923"
x = len(num_str)

for i in range(x):
    p = num_str[i : i + 1]  # Mid-Function
    n1 = n1 + int(p)
print("Total sum value of numbers:", n1)
# OP:
# Total sum value of numbers: 29

# ---- How do you reverse a number using a loop?

r = []
num_str = 78923
print("Actual number:", num_str)

for i in range(len(str(num_str))):
    r.append(num_str % 10)
    num_str = num_str // 10

rs = "".join(map(str, r))
print("Reversed number:", rs)

# OP:
# Actual number: 78923
# Reversed number 32987


num = 12345
reversed_num = int("".join(reversed(str(num))))
print(reversed_num)  # Output: 54321


# ----- How do you print a pattern of stars (*)?

n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# OP:
#   *
#   ***
#  *****
# *******


# ----- How do you iterate over a dictionary using a loop?

my_dict = {"a": 1, "b": 2, "c": 3}

for i in my_dict:
    print(i, my_dict[i])
# OP:
# a 1
# b 2
# c 3

for key, value in my_dict.items():
    print(key, ":", value)
# OP:
# a : 1
# b : 2
# c : 3

# ----- How do you iterate over two lists simultaneously?
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

for i in range(len(list1)):  # Assumes lists are the same length
    print(list1[i], list2[i])
# OP:
# 1 a
# 2 b
# 3 c

list1 = [1, 2, 3, 4, 7]
list2 = ["a", "b", "c"]

for num, char in zip(list1, list2):
    print(num, char)
# OP:
# 1 a
# 2 b
# 3 c

# ✅ zip() pairs elements from both lists and stops at the shortest list.

from itertools import zip_longest

list1 = [1, 2, 3, 4]
list2 = ["a", "b"]

for num, char in zip_longest(list1, list2, fillvalue="-"):
    print(num, char)

# OP:
# 1 a
# 2 b
# 3 -
# 4 -


# ----- How do you find numbers divisible by both 3 and 5 in a range?

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# OP:
# 15
# 30
# 45
# 60
# 75
# 90


for i in range(15, 101, 15):  # Start at 15, step by 15
    print(i)
# OP:
# 15
# 30
# 45
# 60
# 75
# 90

# ----- How do you generate a multiplication table for a given number?
for i in range(1, 11):
    print(2, "*", i, "=", 2 * i)

    # 2 * 1 = 2
    # 2 * 2 = 4
    # 2 * 3 = 6
    # 2 * 4 = 8
    # 2 * 5 = 10
    # 2 * 6 = 12
    # 2 * 7 = 14
    # 2 * 8 = 16
    # 2 * 9 = 18
    # 2 * 10 = 20

# *****6. Function Coding Questions

# ----- How do you define and call a function in Python?
def greet():
    print("Hello, World!")  # Function definition

greet()  # Function call


def greet(name):
    print("Hello,", name)


greet("Alice")  # Output: Hello, Alice
greet("Bob")  # Output: Hello, Bob


def square(num):
    return num**2  # Returns the square of the number


result = square(5)
print(result)  # Output: 25


def add(a, b):
    return a + b


print(add(3, 5))  # Output: 8


def greet(name="Guest"):
    print("Hello,", name)


greet()  # Output: Hello, Guest
greet("Alice")  # Output: Hello, Alice
# ✅ If no argument is given, it uses the default value "Guest".


def person_info(name, age):
    print(f"Name: {name}, Age: {age}")


person_info(age=25, name="Alice")  # Order doesn't matter


def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4, 5))  # Output: 15
# ✅ *args allows passing multiple arguments as a tuple.


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


info(name="Alice", age=25, city="New York")

# ✅ **kwargs allows passing multiple named arguments as a dictionary.


def multiply(a, b):
    return a * b


def square(n):
    return multiply(n, n)  # Calls another function


print(square(4))  # Output: 16


# ----- How do you return multiple values from a function?
# 1. Using Tuples (Most Common)
def get_coordinates():
    x = 10
    y = 20
    return x, y  # Returns a tuple


cords = get_coordinates()
print(cords)  # Output: (10, 20)
print(cords[0])  # Output: 10
print(cords[1])  # Output: 20


x, y = get_coordinates()
print(x)  # Output: 10
print(y)  # Output: 20

# 2. Using Lists


def get_numbers():
    return [1, 2, 3]


numbers = get_numbers()
print(numbers)  # Output: [1, 2, 3]


# 3. Using Dictionaries (Named Values)


def get_student():
    return {"name": "Alice", "age": 25, "grade": "A"}


student = get_student()
print(student["name"])  # Output: Alice


# 4. Using Data Classes (Python 3.7+)

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grade: str


def get_student():
    return Student("Alice", 25, "A")


student = get_student()
print(student.name)  # Output: Alice


# 5. Using namedtuple (Immutable Alternative to Dict)

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])


def get_student():
    return Student("Alice", 25, "A")


student = get_student()
print(student.name)  # Output: Alice


# ----- How do you find the GCD (Greatest Common Divisor) of two numbers?

# 1. Using math.gcd() (Recommended)
# Python provides a built-in function in the math module:
import math

a, b = 48, 18
gcd = math.gcd(a, b)
print(gcd)  # Output: 6

# 2. Using Euclidean Algorithm (Recursive)


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


print(gcd_recursive(48, 18))  # Output: 6


# 3. Using Euclidean Algorithm (Iterative)


def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd_iterative(48, 18))  # Output: 6


# 4. Using functools.reduce() for Multiple Numbers
# If you need to find the GCD of more than two numbers:

from functools import reduce
import math

numbers = [48, 18, 30]
gcd_multiple = reduce(math.gcd, numbers)
print(gcd_multiple)  # Output: 6


# ----- How do you find the LCM (The Least Common Multiple) of two numbers?

# 1. Using math.lcm() (Python 3.9+) ✅ Recommended
import math

a, b = 12, 18
lcm = math.lcm(a, b)
print(lcm)  # Output: 36


# 2. Using the Formula: LCM(a, b) = (a * b) // GCD(a, b)

import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)


print(lcm(12, 18))  # Output: 36


# 3. Using functools.reduce() for Multiple Numbers
# To find the LCM of multiple numbers, use reduce():


from functools import reduce
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)


numbers = [12, 18, 24]
lcm_multiple = reduce(lcm, numbers)
print(lcm_multiple)  # Output: 72

# ----- How do you write a recursive function for factorial?


def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case


print(factorial(5))  # Output: 120
# OR

import math

print(math.factorial(5))  # Output: 120


# ----- How do you write a recursive function for Fibonacci?
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


print(fibonacci_iterative(6))  # Output: 5

# ----- How do you implement a function to check for a prime number?
def is_prime(n):
    if n < 2:
        return False  # 0 and 1 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True


print(is_prime(11))  # Output: True
print(is_prime(10))  # Output: False

# ----- How do you pass a list to a function and modify it?
def modify_list(lst):
    lst.append(4)  # Adding an element to the list
    lst[0] = 99  # Modifying an existing element


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [99, 2, 3, 4]

# ----- How do you write a lambda function to multiply two numbers?
multiply = lambda x, y: x * y
print(multiply(5, 3))  # Output: 15


# lambda x, y: x * y → A function that takes two arguments (x, y) and returns their product.
# Equivalent to:


def multiply(x, y):
    return x * y


# ----- How do you use the map(), filter(), and reduce() functions?

# 1. map() – Apply a Function to Each Element
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]


# 2. filter() – Select Elements That Meet a Condition
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]


# 3. reduce() – Apply a Function to Reduce an Iterable to a Single Value

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120 (1*2*3*4*5)


# *****7. File Handling Coding Questions

# ----- How do you read a file in Python?

# 1. Reading the Entire File (read())
with open("example.txt", "r") as file:
    content = file.read()

print(content)  # Outputs the entire file content


# 2. Reading Line by Line (readline())
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())  # `.strip()` removes newline characters
        line = file.readline()

# 3. Reading All Lines into a List (readlines())
with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)  # Output: ['First line\n', 'Second line\n', ...]


# 4. Iterating Over Lines (Most Efficient for Large Files)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process each line without loading everything into memory

# 5. Reading a File in Binary Mode (rb)
with open("example.jpg", "rb") as file:
    binary_data = file.read()


# 6. Handling File Not Found Errors
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# ----- How do you write data to a file?

# 1. Writing to a File ("w") – Overwrites Existing Content

with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")

print("Data written successfully!")


# 2. Appending to a File ("a") – Keeps Existing Contnt

with open("example.txt", "a") as file:
    file.write("Appending this line.\n")

print("Data appended successfully!")


# 3. Writing Multiple Lines (writelines())

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)

# 4. Writing Binary Data ("wb")
binary_data = b"Some binary content"

with open("example.bin", "wb") as file:
    file.write(binary_data)


# 5. Handling File Writing Errors

try:
    with open("example.txt", "w") as file:
        file.write("Safe writing example.\n")
except IOError:
    print("Error writing to file!")


# Example: Writing JSON Data

import json

data = {"name": "Alice", "age": 25}

with open("data.json", "w") as file:
    json.dump(data, file)

print("JSON data written successfully!")
# ✅ Best for: Writing structured data.


# ----- How do you append data to an existing file?


# 1. Using "a" Mode (Append)

with open("example.txt", "a") as file:
    file.write("This is a new line added.\n")

print("Data appended successfully!")


# 2. Appending Multiple Lines Using writelines()

lines = ["New line 1\n", "New line 2\n"]

with open("example.txt", "a") as file:
    file.writelines(lines)

print("Multiple lines appended successfully!")


# 3. Handling Errors Gracefully

try:
    with open("example.txt", "a") as file:
        file.write("Appending with error handling.\n")
except IOError:
    print("Error writing to file!")


# 4. Appending to a File in Binary Mode ("ab")

binary_data = b"\nNew binary data"

with open("example.bin", "ab") as file:
    file.write(binary_data)

print("Binary data appended successfully!")


# ----- How do you count the number of lines in a file? *#

# 1. Using a Loop (Efficient for Large Files)

with open("example.txt", "r") as file:
    line_count = sum(1 for line in file)

print(f"Total lines: {line_count}")

# 2. Using readlines() (Loads All Lines)

with open("example.txt", "r") as file:
    lines = file.readlines()

print(f"Total lines: {len(lines)}")


# 3. Using enumerate() (Readable & Efficient)
with open("example.txt", "r") as file:
    for line_count, _ in enumerate(file, start=1):
        pass

print(f"Total lines: {line_count}")


# 4. Handling File Not Found Errors
try:
    with open("example.txt", "r") as file:
        line_count = sum(1 for line in file)
    print(f"Total lines: {line_count}")
except FileNotFoundError:
    print("File not found!")


# ----- How do you check if a file exists? *#

# 1. Using os.path.exists() (Works for Files & Directories)

import os

if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File does not exist.")


# 2. Using os.path.isfile() (Files Only)

import os

if os.path.isfile("example.txt"):
    print("File exists!")
else:
    print("File does not exist.")

# 3. Using pathlib.Path.exists() (Modern Approach)

from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    print("File exists!")
else:
    print("File does not exist.")


# 4. Using try-except (Prevents Errors)

try:
    with open("example.txt", "r"):
        print("File exists!")
except FileNotFoundError:
    print("File does not exist.")


# ----- How do you delete a file using Python?


# 1. Using os.remove() (Traditional Approach)

import os

file_path = "example.txt"

if os.path.exists(file_path):  # Check if file exists
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print("File does not exist.")


# 2. Using pathlib.Path.unlink() (Modern Approach)

from pathlib import Path

file = Path("example.txt")

if file.exists():  # Check if file exists
    file.unlink()
    print("File deleted successfully!")
else:
    print("File does not exist.")


# 3. Handling Errors with try-except

import os

try:
    os.remove("example.txt")
    print("File deleted successfully!")
except FileNotFoundError:
    print("File does not exist.")
except PermissionError:
    print("Permission denied! Cannot delete file.")


# 4. Deleting Multiple Files Using glob

import glob
import os

for file in glob.glob("*.txt"):  # Delete all `.txt` files in the directory
    os.remove(file)
    print(f"Deleted: {file}")


# ----- How do you copy the contents of one file to another? *#

# 1. Using shutil.copyfile() (Recommended)

import shutil

shutil.copyfile("source.txt", "destination.txt")
print("File copied successfully!")


# 2. Using shutil.copy() (Copies Metadata Too)

import shutil

shutil.copy("source.txt", "destination.txt")
print("File copied successfully!")


# 3. Using shutil.copy2() (Copies Everything: Content + Metadata)

import shutil

shutil.copy2("source.txt", "destination.txt")
print("File copied successfully!")


# 4. Using Manual Read & Write (For Learning)

with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read())

print("File copied successfully!")


# 5. Copying Binary Files (Images, Videos, etc.)

with open("source.jpg", "rb") as src, open("destination.jpg", "wb") as dest:
    dest.write(src.read())

print("Binary file copied successfully!")

# ----- How do you find and replace text in a file?

# 1. Basic Find and Replace (read() + write())

file_path = "example.txt"

with open(file_path, "r") as file:
    content = file.read()  # Read entire file

content = content.replace("old_text", "new_text")  # Replace text

with open(file_path, "w") as file:
    file.write(content)  # Write modified content back

print("Text replaced successfully!")


# 2. Find and Replace Line by Line (Efficient for Large Files)

file_path = "example.txt"
temp_file = "temp.txt"

with open(file_path, "r") as file, open(temp_file, "w") as temp:
    for line in file:
        temp.write(line.replace("old_text", "new_text"))  # Replace in each line

import os

os.replace(temp_file, file_path)  # Replace original file with modified file

print("Text replaced successfully!")


# 3. Find and Replace Using fileinput (In-Place Editing)

import fileinput

file_path = "example.txt"

for line in fileinput.input(file_path, inplace=True):
    print(line.replace("old_text", "new_text"), end="")

print("Text replaced successfully!")


# 4. Using Regular Expressions (re.sub())

import re

file_path = "example.txt"

with open(file_path, "r") as file:
    content = file.read()

content = re.sub(r"\bold_text\b", "new_text", content)  # Replace exact word

with open(file_path, "w") as file:
    file.write(content)

print("Text replaced successfully!")

# ----- How do you read a file line by line? *#


# 1. Using a for Loop (Most Efficient)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # `.strip()` removes newline characters


# 2. Using readline() (Manual Line-by-Line Reading)

with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()


# 3. Using readlines() (Stores Lines in a List)

with open("example.txt", "r") as file:
    lines = file.readlines()  # Reads all lines into a list

for line in lines:
    print(line.strip())


# 4. Using fileinput for Large Files

import fileinput

for line in fileinput.input("example.txt"):
    print(line.strip())

# ----- How do you handle file errors using try-except?

# 1. Handling FileNotFoundError

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found!")


# 2. Handling PermissionError (File Cannot Be Accessed)

try:
    with open("/system/protected_file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Error: You don't have permission to access this file!")


# 3. Handling Multiple File Errors

try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist!")
except PermissionError:
    print("Error: Permission denied!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# 4. Handling Errors While Writing to a File

try:
    with open("readonly.txt", "w") as file:
        file.write("This is a test.")
except IOError:
    print("Error: Unable to write to file!")


# 5. Using finally to Ensure File Closure

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    if "file" in locals() and not file.closed:
        file.close()
        print("File closed successfully.")

