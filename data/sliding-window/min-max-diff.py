# Sliding Window Algorithm
#
# DIFFERENCE BETWEEN THE MAXIMUM AND MINIMUM AVERAGE
# OF ALL K-LENGTH CONTINUOUS SUB-ARRAYS
# Input: arr[] = {3, 8, 9, 15}, K = 2
# Output: 6.5
# All sub-arrays of length 2 are {3, 8}, {8, 9}, {9, 15}
# and their averages are (3+8)/2 = 5.5, (8+9)/2 = 8.5, and (9+15)/2 = 12.0 respectively.
#
# Therefore, the difference between the maximum(=12.0) and minimum(=5.5) is 12.0 - 5.5 = 6.5.
def min_max_diff(arr, k):
    n = len(arr)

    if k > n:
        return -1

    min_avg = float('inf')
    max_avg = float('-inf')

    window_sum = sum(arr[:k])

    for i in range(k, n):
        current_avg = window_sum / k
        min_avg = min(min_avg, current_avg)
        max_avg = max(max_avg, current_avg)
        window_sum -= arr[i - k]
        window_sum += arr[i]

    last_avg = window_sum / k
    min_avg = min(min_avg, last_avg)
    max_avg = max(max_avg, last_avg)

    difference = max_avg - min_avg

    return difference


# Test case
arr = [3, 8, 9, 15]
k = 2
result = min_max_diff(arr, k)
print(result)