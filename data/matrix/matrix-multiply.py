def matrix_multiply(a, b):
    # Check if we can multiply matrix
    if len(a[0]) != len(b):
        raise ValueError("Number of 'a' columns must equal number of 'b' rows.")
    # init result matrix with 0
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
output = matrix_multiply(A, B)
for row in output:
    print(row)