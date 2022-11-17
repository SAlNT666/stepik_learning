def matrix_by_elem(matrix):
    yield from (i for j in matrix for i in j)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))
