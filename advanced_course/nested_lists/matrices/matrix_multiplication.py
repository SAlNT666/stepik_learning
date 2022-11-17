n1, m1 = [int(i) for i in input().split()]
matrix1 = [[int(e) for e in input().split()] for _ in range(n1)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(e) for e in input().split()] for _ in range(n2)]

matrix3 = [[0]*n1 for _ in range(m2)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            matrix3[i][j] = sum([matrix1[i][k] * matrix2[k][j] for k in range(m1)])

for row in matrix3:
    print(*row)
