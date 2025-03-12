
from Pages.Page2 import Page2

class Page1:
    def __init__(self, a):
        self.a = a

    def page1_method(self):
        print("This is from Page 1 Class")
        print("The value of a from page 1 :" + str(self.a))
        return Page2(self.a)


