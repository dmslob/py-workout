def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    """
    Multiplies a matrix by a scalar.
    Parameters:
    matrix (list of lists): The input matrix as a list of lists of numbers.
    scalar (int or float): The scalar value to multiply each element of the matrix.
    Returns:
    list of lists: The resulting matrix after multiplication.
    """
    res = []
    for row in matrix:
        result_row = [element * scalar for element in row]
        res.append(result_row)
    return res


M1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

M2 = [
    [1, 2],
    [3, 4]
]
scalar = 2

result = scalar_multiply(M1, scalar)
print(result)  # [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

result = scalar_multiply(M2, scalar)
print(result)  # [[2, 4], [6, 8]]

scalar = -1
print(scalar_multiply([[0, -1], [1, 0]], scalar))
