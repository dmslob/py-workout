# Sometimes, mean does not adequately represent the "typical" value for data.
# For example, when there are a few extreme values that are completely out of range,
# they can affect the mean.
# Another good indication is a median, a value such that half of data points
# are lower than it, and another half - higher

import numpy

def median(nums):
    n = len(nums)
    nums.sort()
    if n % 2 == 0:
        m1 = nums[n // 2 - 1]
        m2 = nums[n // 2]
        return (m1 + m2) / 2
    else:
        return nums[n // 2]


v1 = [-5, -5, -3, -4, 0, -1]
v2 = [49, 45, 89]
v3 = [44, 55, 22, 25, 13, 13, 23, 13, 56, 90, 39]

print(median(v1)) # -3.5
print(median(v2)) # 49
print(median(v3)) # 25

print(numpy.median(v1)) # 3.5
print(numpy.median(v2)) # 49.0
print(numpy.median(v3)) # 25.0
