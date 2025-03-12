
from Pages.Page3 import Page3


class Page2:
    def __init__(self,a):
        self.a = a

    def page2_method(self):
        print("This is from Page 2 Class")
        print("The value of a from page 2 :" + str(self.a))
        return Page3(self.a)