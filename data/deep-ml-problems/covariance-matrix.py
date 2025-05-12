import numpy as np
# Function to calculate the covariance matrix for a given set of vectors.
# The function should take a list of lists, where each inner list
# represents a feature with its observations,
# and return a covariance matrix as a list of lists.


def covariance_matrix_numpy(data: list[list[float]]) -> list[list[float]]:
    """
    Calculates the covariance matrix.
    Parameters:
    data (list of lists): Each inner list is a feature containing multiple observations.
    Returns:
    list of lists: Covariance matrix as a list of lists.
    """
    data_array = np.array(data, dtype=float)
    # Compute covariance matrix; rows are variables (features), columns are observations
    cov_matrix = np.cov(data_array, bias=False)
    # Convert to a regular Python list of lists, rounded to 4 decimals
    return cov_matrix.round(4).tolist()


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    """
    Calculates the covariance matrix for the given data.
    Parameters:
    vectors (list of lists):
    Each inner list is a feature containing multiple observations.
    All features must have the same number of observations.
    Returns:
    list of lists: Covariance matrix.
    """
    if not vectors or not all(len(row) == len(vectors[0]) for row in vectors):
        raise ValueError("All features must have the same number of observations.")

    num_features = len(vectors)
    num_observations = len(vectors[0])
    # Compute the mean of each feature
    means = [sum(feature) / num_observations for feature in vectors]
    # Center the data by subtracting the mean
    centered_data = [[x - means[i] for x in vectors[i]] for i in range(num_features)]
    # Compute the covariance matrix
    covariance_matrix = []
    for i in range(num_features):
        row = []
        for j in range(num_features):
            cov = sum(centered_data[i][k] * centered_data[j][k] for k in range(num_observations)) / (num_observations - 1)
            row.append(cov)
        covariance_matrix.append(row)

    return covariance_matrix


def print_matrix(matrix):
    for row in matrix:
        print("  ", row)


# Test Case 1: Simple 2D case
data1 = [
    [2.1, 2.5, 4.0, 3.6],  # Feature 1
    [8.0, 12.0, 14.0, 10.0]  # Feature 2
]
print("Covariance Matrix for data1 by NumPy:")
print_matrix(covariance_matrix_numpy(data1))

print("Covariance Matrix for data1:")
print_matrix(calculate_covariance_matrix(data1))

# Test Case 2: 3 Features, 3 Observations
data2 = [
    [1, 2, 3],  # Feature 1
    [4, 5, 6],  # Feature 2
    [7, 8, 9]  # Feature 3
]
print("\nCovariance Matrix for data2 by NumPy:")
print_matrix(covariance_matrix_numpy(data2))

print("\nCovariance Matrix for data2:")
print_matrix(calculate_covariance_matrix(data2))

# Test Case 3: Features with no correlation
data3 = [
    [1, 2, 3, 4],  # Feature 1
    [4, 3, 2, 1]  # Feature 2 (negatively correlated)
]

print("\nCovariance Matrix for data3 by NumPy:")
print_matrix(covariance_matrix_numpy(data3))

print("\nCovariance Matrix for data3:")
print_matrix(calculate_covariance_matrix(data3))
