from typing import List


# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers [index1] and numbers [index2]
# where 1 < index1 ‹ index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Explanation: The sum of 2 and 7 is 9.
# Therefore, index1 = 1, index2 = 2. We return [1, 2].
#
# Example 2:
# Input: numbers = [2, 3, 4] target = 6
# Output: [1, 3]
# Explanation: The sum of 2 and 4 is 6.
# Therefore, index1 = 1, index2 = 3. We return [1, 3]
# Time: O(n)
# Space: O(1)
def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return [left + 1, right + 1]
        elif summ < target:
            left += 1
        else:
            right -= 1


ns = [2, 7, 11, 15]
print(two_sum(ns, 9))
ns = [2, 3, 4]
print(two_sum(ns, 6))
