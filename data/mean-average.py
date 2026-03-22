import numpy

values = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

def mean(data_set):
    return sum(data_set) / len(data_set)

mean_1 = numpy.mean(values)
print(mean_1)

mean_2 = mean(values)
print(mean_2)
