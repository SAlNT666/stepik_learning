n, m = [int(i) for i in input().split()]
matrix = [[0]*m for _ in range(n)]

for i in range(n):
    border = i % m
    matrix[i] = list(range(1, m + 1))[border:] + list(range(1, m + 1))[:border]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
