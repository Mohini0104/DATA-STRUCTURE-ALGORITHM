''' 
# - Difference in list and a array
Python has a library of it own which help us get the features of an array
import array  as arr ->this will import the array library

1. Arrays are homogenous contagius Data structure that will contain only one type of data
2. Whereas LIST is heterogenous collection or contagious collection of data
'''
import array as arr
v = arr.array('i',[1,2,3]) #i says the type of array
print(v)

for x in v:
    print(x)

v.append(23)
print(v)
