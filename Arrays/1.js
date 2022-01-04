// 1. Two number sum
// Check if sum of two numbers in a array is equal to target sum

// let arr = [3, 5, -4, 8, 11, 1, -1, 6];
// let targetSum = 10;

function twoNumberSum(array, targetSum) {
    // Write your code here.
    const nums = {};
    for (const num of array){
        const potentialMatch = targetSum - num ;
        if (potentialMatch in nums){
            console.log ([potentialMatch , num]) ;
            // noinspection UnreachableCodeJS
            // console.log(potentialMatch);
        }else {
            nums[num] = true;
        }

    }
    return []
}

// Do not edit the line below.
twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10);

