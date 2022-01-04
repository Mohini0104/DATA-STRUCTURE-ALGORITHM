def subSumArray(arr, n, sum):
    map = {}
    curr_sum = 0
    for i in range(0,n):
        curr_sum = curr_sum + arr[i]
        if curr_sum == sum:
            print("Sum found between indexes 0 to", i)
            return
        if(curr_sum - sum) in map:
            print("Sum found between indexes", map[curr_sum - sum] + 1, "to" ,i)
            return
        map[curr_sum]=i
    print("No subarray with given sum exists")
