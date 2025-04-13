import numpy


def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None


def median_2(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if lstLen % 2:
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def median_3(n_num):
    n = len(n_num)
    n_num.sort()

    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
        return median
    else:
        median = n_num[n//2]
        return median


# 3.5
print(median([-5, -5, -3, -4, 0, -1]))
print(median_2([-5, -5, -3, -4, 0, -1]))
print(median_3([-5, -5, -3, -4, 0, -1]))
print(numpy.median([-5, -5, -3, -4, 0, -1]))
print(numpy.median([49, 45, 89]))
print(numpy.median([44, 55, 22, 25, 13, 13, 23, 13, 56, 90, 39]))



num1 = 12
num2 = 5
num3 = num1 // num2
# Output: division of 12 by 5 = 2.4
print("division of", num1, "by", num2, "=", num1 / num2)

# Output: floor division of 12 by 5 = 2
print("floor division of", num1, "by", num2, "=", num3)

print(7//2)