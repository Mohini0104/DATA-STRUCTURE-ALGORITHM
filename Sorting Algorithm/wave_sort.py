'''
a1 >=a2 <=a3>= a4 <= a5 >=a6 ...
Input: [5,2,6,7,2,1,0,3]
Output: [5, 2, 7, 2, 6, 0, 3, 1]
'''
def wave_sort(arr):
    i = 0
    n = len(arr)
    while i <n:
        if i >0 and arr[i-1]>arr[i]:
            arr[i - 1],arr[i] = arr[i],arr[i-1]
        if i<n-1 and arr[i]<arr[i+1]:
            arr[i+1],arr[i]= arr[i],arr[i+1]

        i+=2

li = [5,2,6,7,2,1,0,3]
wave_sort(li)
print(li)
    
