set1 = {1, 1, 50, 5.5, 99, 99, 99, "Apple", "Mango", "Apple"}
# We can duplicate, but in result it will not print duplicate

print(set1)
print(type(set1))
print(len(set1))

set1.add("yellow")
print(set1)
print(len(set1))

# OP:
# {1, 50, 99, 5.5, 'Apple', 'Mango'}
# <class 'set'>
# 6
# {1, 50, 99, 'yellow', 5.5, 'Apple', 'Mango'}
# 7
