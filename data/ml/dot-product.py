def matrix_dot_vector(matrix: list[list[int | float]], vector: list[int | float]) -> list[int | float]:
    # Matrix-Vector Dot Product
    # Return a list where each element is the dot product of a row of 'matrix' with 'vector'.
    # If the number of columns in 'matrix' does not match the length of 'vector', return -1.
    # Check dimensions
    num_cols = len(matrix[0]) if matrix else 0
    if num_cols != len(vector):
        return -1  # Return -1 if dimensions are incompatible
    # Compute dot product
    result = []
    for row in matrix:
        product = sum(row[i] * vector[i] for i in range(num_cols))
        result.append(product)

    return result


# Example usage:
m1 = [[1, 2], [2, 4]]
v1 = [1, 2]
print(matrix_dot_vector(m1, v1))  # Output: [5, 10]

m2 = [[1, 2, 3], [2, 4, 5], [6, 8, 9]]
v2 = [1, 2, 3]
print(matrix_dot_vector(m2, v2))  # Output: [14, 25, 49]

m3 = [[1, 2], [2, 4], [6, 8], [12, 4]]
v3 = [1, 2, 3]
print(matrix_dot_vector(m3, v3))  # Output: -1


# dot product
X = [10, 20, 30]
Y = [7, 5, 3]
print(*zip(X, Y))
dot_product = sum(x * y for x, y in zip(X, Y))  # Output: 260
print(dot_product)

