li = [1, 2, 3, "mohini", 58.9, True]
print(li)
print(len(li))
# lenght of the list- len()
# indexing -> in python Indexing is done as 0-based from left right and -1 based from right to left
''' 
for i in range(0,len(li)):
     print(li[i], end='')

 print(li[-1])
 for i in range(-1,len(li)):
    print(li[i-1],i)
'''
li = [[1, 2, 3, 4], [5, 6], [1, 2, 3, 4], [5, 6, 7, 8]]
# print(li)
# print(li[0])
for i in range(0, len(li)):
    for j in range(0, len(li[i])):
        print(li[i][j], end=" ")
    print()

print("------------------------")

for row in li:
    for el in row:
        print(el, end="")
    print()

# list are mutable
li[0] = 99
print(li)

# slice of lists
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[0:4])  # [start,end]

print(li[1:])  # print from 1st to last index
print(li[:7])  # print first element to (7-1)th index
print(li[:])  # print begin to end
print(li[1:7:2])  # [start,end,jump]

''' Given a binary list of all 0's and 1's ,
 sort the list in non-decreasing order, 
 in single read of an array without taking extra
  space and no counting of the element is allowed
TC: 0(n)
  ex: [1,1,0,1,0] ->[0,0,1,1,1]
'''


