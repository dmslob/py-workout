from typing import List


# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
def missing_number(nums: List[int]) -> int:
    n = len(nums)
    # Expected sum of [0, n]
    # Gauss' Formula: n * (n + 1) / 2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def missing_number_xor(nums: List[int]) -> int:
    res = len(nums) # Initialize with n
    for i, n in enumerate(nums):
        # XOR the index and the value
        res ^= i ^ n
    return res


numbers = [3, 0, 1]
print(missing_number(numbers))  # Output: 2
print(missing_number_xor(numbers))  # Output: 2
