def twoNumberSum(array, targetSum):
    nums={}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num]= True
       
    return[]
print(twoNumberSum([1,5,-1,8,11,9],10))

