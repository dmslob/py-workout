# Sliding Window Algorithm
#
# MAXIMUM SUM SUBARRAY OF SIZE K
# Given an array of positive integers and a positive number k,
# find the maximum sum of any contiguous subarray of size k.
def find_max_sum(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i - start + 1) == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum


numbers = [3, 5, 2, 1, 7]
print(find_max_sum(numbers, 2))


# FIND MINIMUM SUM SUBARRAY OF SIZE K
# Input: arr = [10, 4, 2, 5, 6, 3, 8, 1]
# k = 3
# Output: 11
def get_min_sum(arr, k):
    curr_sum = 0
    min_sum = float("inf")
    start = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if i - start + 1 == k:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    return min_sum

print(get_min_sum([10, 4, 2, 5, 6, 3, 8, 1], 3))
