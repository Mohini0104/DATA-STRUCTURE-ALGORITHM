if 2>3:
     print("hello")
elif (2<5):
    print("hi")

if(True):
    if(10>3):
        if(5>3):
            print("You Reached")
else:
    print("Very Far")


#Given a number check whether the numbr is a fibonacci or not?
# - The RATIO of sequential Fibonacci numbers(2/1, 3/2, 5/3) approach the golden ratio.
# - To Read: 1) What is golden ration?  2) What is benett formula and how is it used for calculating golden ratio? 3) How golden ratio is involved with fibonnaci?
from math import sqrt
n = 5
temp1 = 5*(n**2) + 4
temp2 = 5*(n**2) - 4
v1 = int(sqrt(temp1))
v2 = int(sqrt(temp2))
if(v1*v1 == temp1 or v2*v2 == temp2):
    print("yes")
else:
    print("No")

