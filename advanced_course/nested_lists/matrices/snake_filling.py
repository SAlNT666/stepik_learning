n, m = [int(i) for i in input().split()]
matrix = []

full_list = list(range(1, n*m+1))

for i in range(n):
    if i % 2:
        path_to_add = full_list[i * m:i * m + m]
        path_to_add.reverse()
        matrix.append(path_to_add)
    else:
        matrix.append(full_list[i * m:i * m + m])

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
