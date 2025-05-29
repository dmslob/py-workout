import numpy as np


# https://www.deep-ml.com/problems/16
# Write a Python function that performs feature scaling on a dataset using both
# standardization and min-max normalization.
# The function should take a 2D NumPy array as input,
# where each row represents a data sample and each column represents a feature.
# It should return two 2D NumPy arrays: one scaled by standardization
# and one by min-max normalization.
# Make sure all results are rounded to the nearest 4th decimal.
def scale_features(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Ensure the input is a NumPy array
    data = np.asarray(data, dtype=float)
    # Standardization (Z-score normalization)
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    # Avoid division by zero if a feature has zero standard deviation
    # (i.e., all values in the column are the same)
    std_dev[std_dev == 0] = 1

    standardized_data = (data - mean) / std_dev
    standardized_data = np.round(standardized_data, 4)

    # Min-Max Normalization
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    # Avoid division by zero if a feature has the same min and max value
    # (i.e., all values in the column are the same)
    range_val = max_val - min_val
    range_val[range_val == 0] = 1

    min_max_normalized_data = (data - min_val) / range_val
    min_max_normalized_data = np.round(min_max_normalized_data, 4)

    return standardized_data, min_max_normalized_data


dataset = np.array([[1, 2], [3, 4], [5, 6]])
print("Original Dataset:\n", dataset)

standardized, min_max_normalized = scale_features(dataset)
print("\nStandardized Data (Z-score):\n", standardized)
print("\nMin-Max Normalized Data:\n", min_max_normalized)