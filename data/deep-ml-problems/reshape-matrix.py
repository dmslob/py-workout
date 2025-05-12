import numpy as np
# Function that reshapes a given matrix into a specified shape.
# if it cant be reshaped return back an empty list []


def reshape_matrix(matrix: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    """
    Write a Python function that reshapes a given matrix into a specified shape.
    if it cant be reshaped return back an empty list [ ]
    """
    try:
        np_matrix = np.array(matrix)
        reshaped = np_matrix.reshape(new_shape)
        return reshaped.tolist()
    except ValueError:
        return []


A = [
    [1, 2, 3],
    [4, 5, 6]]
v = (3, 2)
print(reshape_matrix(A, v))  # Output: [[1, 2], [3, 4], [5, 6]]

bad_shape = (4, 2)
print(reshape_matrix(A, bad_shape))  # Output: []
