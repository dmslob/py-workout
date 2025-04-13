import math
import random
# calculates basic statistical properties (the mean, median, variance, etc.) of numeric data
import statistics

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print(random.choice(['apple', 'pear', 'banana']))

# sampling without replacement
print(random.sample(range(100), 10))
print(random.random())  # random float

# random integer chosen from range(6)
print(random.randrange(6))

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))


