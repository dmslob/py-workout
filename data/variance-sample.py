import numpy

# Variance = how spread out the values are = Standard Deviation ^ 2
# 1. Find mean
# 2. Find difference from mean for each values
# 3. Find the square for each difference
# 4. Find the average of squared differences
values = [86, 87, 88, 86, 87, 85, 86]

var = numpy.var(values)

print(var)
