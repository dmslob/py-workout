def find_number(matrix, k):
    if not matrix or not matrix[0]:
        return False
    n = len(matrix)
    m = len(matrix[0])
    row, col = 0, m - 1
    while row < n and col >= 0:
        if matrix[row][col] == k:
            return True
        elif matrix[row][col] > k:
            col -= 1
        else:
            row += 1
    return False


A = [[1, 2, 3], [4, 5, 6]]
kk = 5
number_found = find_number(A, kk)
print(f'Number {kk} is found={number_found}')