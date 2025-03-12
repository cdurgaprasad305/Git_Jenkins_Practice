tuple1 = (1, 525, 5.4,1, "apple")
# We can add duplicates, it will display duplicate

print(len(tuple1))
print(type(tuple1))

tuple1 = tuple1 + (4, "Black", 5.5)
print(tuple1)

# tuple1[3]="Apple"
# print(tuple1)

del tuple1
print(tuple1) # NameError: name 'tuple1' is not defined. Did you mean: 'tuple'?

# OP:
# 5
# <class 'tuple'>
# (1, 525, 5.4, 1, 'apple', 4, 'Black', 5.5)