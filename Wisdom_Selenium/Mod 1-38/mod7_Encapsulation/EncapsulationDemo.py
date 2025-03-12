# Encapsulation
# Hiding Methods and Variable inside the class


class Laptop:
    def processor(self):
        print("I am in processor function")

    def graphicCard(self):
        print("I am in graphic card function")

    def camera(self):
        print("I am in camera function")


l = Laptop()
l.camera()
