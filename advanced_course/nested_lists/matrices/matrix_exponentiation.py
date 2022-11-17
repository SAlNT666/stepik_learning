"""n = int(input())
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
k = int(input())
"""

n = 2
matrix = [[1, 2], [3, 2]]
k = 2

res_matrix = matrix.copy()
print(res_matrix)


def matrix_exponention():
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_matrix[i][j] = sum([res_matrix[i][k] * matrix[k][j] for k in range(n)])


for i in range(k-1):
    matrix_exponention()
    print(res_matrix)

for row in res_matrix:
    print(*row)
