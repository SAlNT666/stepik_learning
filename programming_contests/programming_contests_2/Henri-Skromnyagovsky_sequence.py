def get_sequence(n):
    n += 1
    c = 1
    n_max = 1
    res = []
    while n_max < n:
        n_max += c
        res += list(reversed(range(n_max - c, n_max)))
        c += 1

    n -= 1

    return res[:n]
    # n_list = list(range(1, n_max + 1))
    #
    # i = 0
    # for c_ in range(c):
    #     n_list = n_list[:i] + list(reversed(n_list[i:i + c_])) + n_list[i + c_:]
    #     i += c_
    #
    # return n_list[:n]


print(*get_sequence(100))



import time

start1 = time.time()

for _ in range(10000):
    get_sequence(1000)

print('my:', time.time() - start1)

