n, X, Y, A, B = (int(i) for i in input().split())

sequence = list(range(1, n+1))

sequence[X-1:Y] = reversed(sequence[X-1:Y])
sequence[A-1:B] = reversed(sequence[A-1:B])
print(*sequence)
