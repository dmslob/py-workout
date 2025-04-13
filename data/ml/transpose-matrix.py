def transpose_matrix(mx: list[list[int | float]]) -> list[list[int | float]]:
    if not mx:
        return []
    # Check if all rows have the same number of columns
    row_length = len(mx[0])
    for row in mx:
        if len(row) != row_length:
            raise ValueError("All rows in the matrix must have the same length.")
    # Transpose the matrix
    transposed = [[row[i] for row in mx] for i in range(row_length)]
    return transposed


# Test:
try:
    m1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose_matrix(m1))  # Output: [[1, 4], [2, 5], [3, 6]]

    m2 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print(transpose_matrix(m2))  # Output: [[1, 3, 5], [2, 4, 6]]

    bad_matrix = [
        [1, 2],
        [3, 4, 5]
    ]
    print(transpose_matrix(bad_matrix))  # This will raise a ValueError
except ValueError as e:
    print("Error:", e)
