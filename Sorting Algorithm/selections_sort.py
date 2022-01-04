def find_min_element_idx(arr,start):
    # arr is the list, 
    # start is the starting index of the unsorted region
    min_index = start;
    start+=1
    while(start< len(arr)):
        if arr[start]< arr[min_index]:
            min_index = start;
        start +=1
    return min_index;

def selection_sort(arr):
    i = 0;
    while i < len(arr):
        min_index = find_min_element_idx(arr, i)
        if(i != min_index):
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
        i += 1
    
    return 
li = [90,88,0,56,79,43];
selection_sort(li);
print(li);
        
    
