def rev(arr,start, end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return

li="mohini"
rev(li,0,5)
print(li)


 