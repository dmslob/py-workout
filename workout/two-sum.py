from typing import List


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
