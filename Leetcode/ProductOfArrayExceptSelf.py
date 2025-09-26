class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)            # get length of nums
        res = [1] * n            # result array, start with all 1s

        prefix = 1               # product of numbers on the LEFT
        for i in range(n):       # left → right
            res[i] = prefix      # store product so far (before nums[i])
            prefix *= nums[i]    # update prefix (include nums[i])

        suffix = 1               # product of numbers on the RIGHT
        for i in range(n-1, -1, -1):   # right → left
            res[i] *= suffix     # multiply with product from right side
            suffix *= nums[i]    # update suffix (include nums[i])
        
        return res               # final result



"""
#Brute Force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            res.append(product)
        return res

#Runtime: O(n^2)
#Space: O(1)
"""