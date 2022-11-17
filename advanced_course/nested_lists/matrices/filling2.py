n, m = [int(i) for i in input().split()]
matrix = [[] for _ in range(n)]
iterator = 1

for j in range(m):
    for i in range(n):
        matrix[i].append(iterator)
        iterator += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
