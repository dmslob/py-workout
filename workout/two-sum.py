from typing import List


def find_two_sum_1(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    if n <= 2:
        return []
    h = {}
    for i in range(n):
        h[nums[i]] = i
    for i in range(n):
        y = target - nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]


def find_two_sum_2(nums: List[int], target: int) -> List[int]:
    if len(nums) <= 2:
        return []
    num_to_index = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_to_index:
            return [num_to_index[complement], i]
        else:
            num_to_index[nums[i]] = i
    return []


numbers = [3, 2, 2, 3]
print(find_two_sum_1(numbers, 6))
print(find_two_sum_2(numbers, 6))


#display_powers_of_2 = lambda n: [print(2 ** i) for i in range(n + 1)]
#display_powers_of_2(10)
