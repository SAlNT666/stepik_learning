def primes(left, right):
    a = [0, 0] + list(range(2, right + 1))

    for i in range(2, right + 1):
        if a[i]:
            for j in range(i * i, right + 1, i):
                a[j] = 0
        print(i, a[i])
        if left <= i <= right and a[i] != 0:
            yield a[i]


generator = primes(1, 15)

print(*generator)
