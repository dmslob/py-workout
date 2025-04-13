from math import log, pi
from numpy import asarray
from numpy import random
import numpy

print(pi, log(32, 2))

print("numpy.random is a", type(numpy.random))
print("it contains names such as...", dir(numpy.random)[-15:])

rolls = random.randint(low=1, high=6, size=10)
print(rolls)

x = [8685.46, 3196.11]
y = [253.34, 844.34]
print(int(max(y)))

