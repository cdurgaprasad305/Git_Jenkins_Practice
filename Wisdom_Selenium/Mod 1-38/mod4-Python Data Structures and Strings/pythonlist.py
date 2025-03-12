list1 = [1,2,2, 525, 5.4, "apple"] # Duplicate can be added...
print(list1)
print(type(list1))
print(len(list1))

list1.append("mango")
print(list1)
print(len(list1))

list1.append([1, 525, 5.4, "apple"])
print(list1)
print(len(list1))

# length - 5 index = 0-5
print(list1[4])
print(list1[-4])

del list1[1]
print(list1)
print(len(list1))

list1[3] = "Mango"
print(list1)
print(len(list1))

del list1
print(list1) # NameError: name 'list1' is not defined. Did you mean: 'list'?

# OP:
# [1, 2, 2, 525, 5.4, 'apple']
# <class 'list'>
# 6
# [1, 2, 2, 525, 5.4, 'apple', 'mango']
# 7
# [1, 2, 2, 525, 5.4, 'apple', 'mango', [1, 525, 5.4, 'apple']]
# 8
# 5.4
# 5.4
# [1, 2, 525, 5.4, 'apple', 'mango', [1, 525, 5.4, 'apple']]
# 7
# [1, 2, 525, 'Mango', 'apple', 'mango', [1, 525, 5.4, 'apple']]
# 7
