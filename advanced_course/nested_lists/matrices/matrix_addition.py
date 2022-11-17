n, m = [int(i) for i in input().split()]
matrix1 = [[int(e) for e in input().split()] for _ in range(n)]
input()
matrix2 = [[int(e) for e in input().split()] for _ in range(n)]

for i in range(n):
    print(*[matrix1[i][j] + matrix2[i][j] for j in range(m)])
