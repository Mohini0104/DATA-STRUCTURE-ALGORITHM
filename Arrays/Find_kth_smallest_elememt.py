'''
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
---------
Output : 7
'''
def kth_element(arr,k):
    arr.sort()
    return arr[k-1]
li=[7,9,8,1,10,2]
kth=3
print(kth_element(li,kth))
# array=[9,0,8,10,11]
# array.sort()
# print(array)