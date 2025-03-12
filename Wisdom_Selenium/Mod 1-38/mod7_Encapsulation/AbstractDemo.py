from abc import ABC, abstractmethod

# `ABC` stands for **Abstract Base Class**. It is imported from the `abc` (Abstract Base Class) module in Python.
class HospitalA(ABC):
    @abstractmethod
    def OT(self):
        pass

    @abstractmethod
    def ortho(self):
        pass

    def ENT(self):
        print("I am in ENT function")

    def OPD(self):
        print("I am in OPD function")


class HospitalB(HospitalA): # Single level Inheritance
    def OT(self):
        print("I am in OT Function of Hospital B")

    def ortho(self):
        print("I am in ortho Function of Hospital B")

    def Cardio(self):
        print("I am in Cardio Function of Hospital B")


b = HospitalB()
b.ENT()  # Calling Abstract Method
b.OT()

# OP:
# I am in ENT function
# I am in OT Function of Hospital B
