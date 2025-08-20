"""
🔹 Problem: Sum of Unique Elements

You are given a list of integers. Return the sum of elements that appear exactly once in the list.

Example 1:
Input: nums = [1, 2, 3, 2]
Output: 4
Explanation: The unique elements are 1 and 3, sum = 1 + 3 = 4.

Example 2:
Input: nums = [1, 1, 1, 1]
Output: 0
Explanation: No element appears exactly once.

Example 3:
Input: nums = [1, 2, 3, 4, 5]
Output: 15
Explanation: All elements are unique.

"""
# Function to implement
def sumOfUnique(nums):
    count = {}
    sum_total = 0
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    for n in count:
        if count[n] == 1:
            sum_total += n
    return sum_total
            
#RUNTIME O(n)
#Space O(m)
# Test cases
print(sumOfUnique([1, 2, 3, 2]))   # Expected 4
print(sumOfUnique([1, 1, 1, 1]))   # Expected 0
print(sumOfUnique([1, 2, 3, 4, 5])) # Expected 15


"""
Brute Force
def sumOfUnique(nums):
    sum_total = 0
    for n in nums:
        if nums.count(n) == 1
        summ_total += n
    return sum_total
"""

"""
Better Solution
def sumOfUnique(nums):
    count = {}
    
    # Count frequency of each number (O(n))
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    # Sum numbers that appear exactly once (O(n))
    total = 0
    for n, freq in count.items():
        if freq == 1:
            total += n
    
    return total

# Test cases
print(sumOfUnique([1,2,3,2]))   # 4
print(sumOfUnique([5,5,5]))     # 0
print(sumOfUnique([10,20,30]))  # 60
"""