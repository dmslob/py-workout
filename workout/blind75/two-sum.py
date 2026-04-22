from typing import List

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order
# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=oizxjoit
def find_two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) <= 2:
        return []
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []


numbers = [2, 7, 11, 15]
print(find_two_sum(numbers, 9))


def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None


ns = [2, 7, 11, 15]
print(two_sum(ns, 9))
ns = [2, 3, 4]
print(two_sum(ns, 6))
