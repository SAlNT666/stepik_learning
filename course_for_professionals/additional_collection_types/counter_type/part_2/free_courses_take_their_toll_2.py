from collections import Counter


books = Counter(input().split())
res = 0

for _ in range(int(input())):
    b, p = input().split()
    if books[b]:
        res += int(p)
        books[b] -= 1

print(res)
