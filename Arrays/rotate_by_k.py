def reverse(li,s,e):
    while s<e:
        li[s],li[e]=li[e],li[s]
        s+=1
        e-=1
    
def rotate_by_k(li,k):
    n = len(li)
    k = k%n
    reverse(li,0,n-1)
    reverse(li,0,k-1)
    reverse(li,k,n-1)
arr=[1,2,3,4,5,6,7]
term=3
rotate_by_k(arr,term)
print("After Kth Rotation: ",arr)

 