import numpy
import math


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
