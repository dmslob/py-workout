import numpy
import math

# Standard Deviation = how spread out the values are = Square root of Variance
# 1. Find mean
# 2. Find difference from mean for each values
# 3. Find the square for each difference
# 4. Find the average of squared differences (variance)
# 5. Find the square root of variance (standard deviation)
# Example: In the data set [1, 2, 3, 4, 5],
# the standard deviation is approximately 1.41,
# which indicates that the values are relatively close to the mean (3).
# In contrast, in the data set [1, 1, 1, 1, 5],
# the standard deviation is approximately 1.60,
# which indicates that the values are more spread out from the mean (1.8).
# σ^2 = ∑(xi - μ)2/n
def std_deviation(nums):
    n = len(nums)
    vals_mean = numpy.mean(nums)
    var = sum(pow(x - vals_mean, 2) for x in nums) / n  # variance
    std_dev = math.sqrt(var)  # standard deviation
    return std_dev


# Standard Deviation = how spread out the values are
values = [86, 87, 88, 86, 87, 85, 86, 89]
print(std_deviation(values))

std = numpy.std(values)
mean = numpy.mean(values)

print(std)
print(mean)

values = [32, 111, 138, 28, 59, 77, 97]

std = numpy.std(values)
mean = numpy.mean(values)

print(std)
print(mean)

vals = [42,45,50,38,50]
print(numpy.std(vals))
print(numpy.mean(vals))
