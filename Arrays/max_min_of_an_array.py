#Input -> [0,10,20,11,45,26]
#Output -> Min: 0, Max: 45

def find_max(arr):
    max_value = arr[0]
   
    for x in arr:
        if x > max_value:
            max_value = x
    return max_value

def find_min(arr):
    min_value = arr[0]
    for x in arr:
        if x < min_value:
            min_value = x
    return min_value
li =[0,10,20,11,45,26]
print("Max: ",find_max(li))
print("Min: ",find_min(li))

