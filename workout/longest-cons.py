from typing import List


# Longest consecutive sequence
# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in 0(n) time.
# Time: O(n)
# Space:
def lcs(nums: List[int]) -> int:
    s = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in s:
            next_num = num + 1
            length = 1
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]
output = lcs(nums)
print(output)  # 4
