def recursive_sum(a, b):
    return a if b == 0 else recursive_sum(a + 1, b - 1)


print(recursive_sum(10, 0))
