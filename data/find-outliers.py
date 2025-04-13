import numpy as np


def find_outliers(data):
    sorted_data = sorted(data)

    q1 = np.percentile(sorted_data, 25)
    q3 = np.percentile(sorted_data, 75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = [x for x in sorted_data if x < lower_bound or x > upper_bound]

    return outliers


print(find_outliers([1, 3, 2, 14, 108, 2, 1, 8, 97, 1, 4, 3, 5]))