import numpy

# Variance = how spread out the values are = Standard Deviation ^ 2
# 1. Find mean
# 2. Find difference from mean for each values
# 3. Find the square for each difference
# 4. Find the average of squared differences
# ∑(xi - μ)2/n
# Variance of weights show the extent to which weights are likely to differ from the mean.
weights = [86, 87, 88, 86, 87, 85, 86]

var = numpy.var(weights)
print(f'mean: {numpy.mean(weights)}, variance: {var}')
# mean: 86.14285714285714, variance: 0.8163265306122449

# or
def variance(nums):
    n = len(nums)
    nums_mean = numpy.mean(nums)
    return sum(pow(x - nums_mean, 2) for x in nums) / n

print(f'mean: {numpy.mean(weights)}, variance: {variance(weights)}')
# mean: 86.14285714285714, variance: 0.8163265306122449
