class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap    = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i #store current number’s index for future checks
        return
    
       # Time Complexity: O(n) (loop through the list once)
       # Space complexity: O(n) dictionary can store up to n elements (all numbers).


"""
Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) #set n to size of array
        #iterate through the array 
        for i in range(n):
            for j in range(i+1, n):  #start iterating from second number
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [ ]

        Time Complexity: O(n^2) (2 Nested for loops)
        Space complexity: O(1) (constant space)

"""
        
