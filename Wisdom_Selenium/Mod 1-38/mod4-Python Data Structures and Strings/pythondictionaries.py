d1 = {"fruit": "Apple"}
print(d1)  # {'fruit': 'Apple'}
print(len(d1))  # 1
print(type(d1))  # <class 'dict'

d1["vegetables"] = "Potato"
print(d1)
print(len(d1))

d1["fruit"] = "Mango"
print(d1)
print(len(d1))

if d1.get("fruits") == None:
    d1["fruits"] = "Grapes"
print(d1)
print(len(d1))

del d1["fruit"]
print(d1)
print(len(d1))

# OP:
# {'fruit': 'Apple'}
# 1
# <class 'dict'>
# {'fruit': 'Apple', 'vegetables': 'Potato'}
# 2
# {'fruit': 'Mango', 'vegetables': 'Potato'}
# 2
# {'fruit': 'Mango', 'vegetables': 'Potato', 'fruits': 'Grapes'}
# 3
# {'vegetables': 'Potato', 'fruits': 'Grapes'}
# 2
