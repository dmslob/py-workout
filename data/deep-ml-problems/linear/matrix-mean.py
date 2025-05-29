import numpy as np
# Function that calculates the mean of a matrix
# either by row or by column, based on a given mode.
# The function should take a matrix (list of lists)
# and a mode ('row' or 'column') as input and return a list of means
# according to the specified mode.


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculates the mean of a matrix either by row or by column, based on a given mode.
    It takes a matrix (list of lists) and a mode ('row' or 'column')
    as input and return a list of means according to the specified mode.
    """
    if not matrix or not matrix[0]:
        return []

    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]

    elif mode == 'column':
        num_rows = len(matrix)
        num_cols = max(len(row) for row in matrix)
        col_means = []
        for col in range(num_cols):
            col_values = [matrix[row][col] for row in range(num_rows) if col < len(matrix[row])]
            if col_values:
                col_means.append(sum(col_values) / len(col_values))
            else:
                col_means.append(0)  # Optional: define behavior for entirely missing columns
        return col_means

    else:
        raise ValueError("Mode must be 'row' or 'column'.")


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(calculate_matrix_mean(A, 'row'))  # Output: [2.0, 5.0, 8.0]
print(calculate_matrix_mean(A, 'column'))  # Output: [4.0, 5.0, 6.0]


def mean_by_mode(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculates the mean of a matrix either by row or by column, based on a given mode.
    numpy
    """
    try:
        np_matrix = np.array(matrix, dtype=float)
    except ValueError:
        return []

    if mode == 'row':
        return np.mean(np_matrix, axis=1).tolist()
    elif mode == 'column':
        return np.mean(np_matrix, axis=0).tolist()
    else:
        raise ValueError("Mode must be 'row' or 'column'.")


# Example usage:
B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(mean_by_mode(B, 'row'))  # Output: [2.0, 5.0, 8.0]
print(mean_by_mode(B, 'column'))  # Output: [4.0, 5.0, 6.0]
