'''
Constructor: these are spcial function to initializ a brand new object from a class
Whenever we define def __init__ it's called a constructor

Self: keyword we can access the attributes and methods of the class in python.

A class without a constructor don't make much of sense,
'''
class ComplexNumber:
    real = 0   #class variable
    img = 0

    def __init__(self, real, img) :
        self.real = real #On the RHS it's the real we passed in the parameter and On LHS it's the real number of class
        self.img = img

    def display(self):
        print(self.real,f"+i{self.img}") #string intrepulation

    def sum(self,c):
        return ComplexNumber(self.real+c.real , self.img+c.img)
        
    def mul(self,m):
        return ComplexNumber(self.real*m.real, self.img*m.img)

c1 = ComplexNumber(5,3) #this calls class constructor
c2 = ComplexNumber(4,4)
c1.display()
c2.display()
c3 = c1.sum(c2)
c3.display()
c4 = c1.mul(c2)
c4.display()
# print(c1.real)

