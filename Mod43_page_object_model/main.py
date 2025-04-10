

from Durga_Package import a_pack
from Durga_Package.moudle1 import m1_first, var_m1_a

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



# print("---Sys path----",sys1)

# Now you can import the module


import allure
print(dir(allure))
"""
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__', 'attach', 'attachment_type', 
'description', 'description_html', 'dynamic', 'epic', 'feature', 'id', 'issue', 
'label', 'link', 'manual', 'parameter_mode', 'parent_suite', 'severity', 
'severity_level','step', 'story', 'sub_suite', 'suite', 'tag', 'testcase', 'title']



"""
























