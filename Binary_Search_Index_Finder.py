"""
Given a sorted list of integers and a target value, write a function to perform binary search and return the index of the target value.
If the target does not exist in the list, return -1.

Your implementation should be efficient and should follow the binary search algorithm logic (divide and conquer).

"""


def binary_search(nums: list[int], target: int) -> int:
  first = 0
  last = len(nums) - 1

  while first <= last:
    mid = (last + first) // 2
    if nums[mid] == target:
      return mid
    elif target > nums[mid]:
     first = mid + 1
    else:
      last = mid -1

  return -1

nums = [1, 3, 5, 7, 9, 11, 15, 23, 35, 45, 90, 120, 126, 140]
target = 45
print("Target index:", binary_search(nums, target))  # Output: 3

