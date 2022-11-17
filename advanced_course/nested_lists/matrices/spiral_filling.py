n, m = [int(i) for i in input().split()]

i = 1
j = 0
c = 0
a = [[0] * (100) for _ in range(100)]

while c < m * n:
    while a[i][j+1] == 0 and j < m:
        a[i][j+1] = c+1
        j += 1
        c += 1

    while a[i+1][j] == 0 and i < n:
        a[i+1][j] = c+1
        i += 1
        c += 1

    while a[i][j-1] == 0 and j > 1:
        a[i][j-1] = c+1
        j -= 1
        c += 1

    while a[i-1][j] == 0 and i > 1:
        a[i-1][j] = c+1
        i -= 1
        c += 1

for i in range(1, n+1):
    for j in range(1, m+1):
        print(str(a[i][j]).ljust(3), end=' ')
    print()