import numpy


values = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
mean = numpy.mean(values)
print(mean)


# Mean
def mean(data_set):
    return sum(data_set) / len(data_set)


print(mean(values))
