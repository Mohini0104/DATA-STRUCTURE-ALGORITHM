'''
Constructor: these are spcial function to initializ a brand new object from a class
Whenever we define def __init__ it's called a constructor

Self: keyword we can access the attributes and methods of the class in python.

A class without a constructor don't make much of sense,
'''
class ComplexNumber:
    real = 0
    img = 0

    def __init__(self, real, img) :
        self.real = real
        self.img = img

    def display(self):
        print(self.real,"i{img}")

c1 = ComplexNumber(5,3)
c1.display()