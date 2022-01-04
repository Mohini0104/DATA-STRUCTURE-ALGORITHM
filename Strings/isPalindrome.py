# TC- O(N)
# SC- O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx +=1
        rightIdx -=1

    return True

print("Is this a palindrome: ",isPalindrome("abcbaaa"))

