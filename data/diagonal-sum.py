# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal
# and all the elements on the secondary diagonal that are not part of the primary diagonal.
def diagonal_sum(mat: list[list[int]]) -> int:
    n = len(mat)
    sum = 0
    for i in range(n):
        sum += mat[i][i]
        sum += mat[i][n - 1 - i]
    if n % 2 == 1:
        sum -= mat[n // 2][n // 2]
    return sum


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(diagonal_sum(m1))  # 25

m2 = [[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]
print(diagonal_sum(m2))  # 8

m3 = [[5]]
print(diagonal_sum(m3))  # 5


