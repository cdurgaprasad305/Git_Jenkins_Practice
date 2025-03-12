import First_Package as fp
from First_Package.Four import four

print("Message from Third File")
result = four()

print(result)
print("The Variable value of b in __inti__.py file :" + str(fp.b))


# OP""
# --Welcome Durga-- from First_Package __init__.py File
# Message from Four.py -- Outside function
# Message from Third File
# Inside four (), Function Message from Four.py file from First_Package
# None
# The Variable value of b in __inti__.py file :20
