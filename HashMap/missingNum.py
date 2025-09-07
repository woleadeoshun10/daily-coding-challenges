"""
🧩 Problem: Find the Missing Number
You are given an array nums containing n distinct numbers in the range [0, n].
Return the one number that is missing from the array.

Example 1:
Input:
nums = [3, 0, 1]
Output:
2

Example 2:
Input:
nums = [0, 1]
Output:
2

Example 3:
Input:
nums = [9,6,4,2,3,5,7,0,1]
Output:
8

"""

def missingNumber(nums):
    hashNum = {}
    for i in nums:
         if i in hashNum:
            hashNum[i] += 1
         else:
            hashNum[i] = 1
    for i in range(len(nums) + 1):
        if i not in hashNum:
            return i
    return -1
"""
#BruteForce
def missingNumber(nums):
    n = len(nums)
    
    for i in range(n + 1):
        if i not in nums:
            return i
    return -1
"""
    
print(missingNumber([3,0,1]))             # 2
print(missingNumber([0,1]))               # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print(missingNumber([0]))                 # 1
