n, m = [int(i) for i in input().split()]

for i in range(n * m):
    print(i+1 if i%m and i!=0 else '\n' + str(i+1), end=' ')
