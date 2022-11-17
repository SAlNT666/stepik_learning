n, m = [int(i) for i in input().split()]
matrix = [[0]*m for _ in range(n)]

elems = iter(range(1, n*m+1))

for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = next(elems)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
