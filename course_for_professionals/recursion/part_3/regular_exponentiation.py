def get_pow(a, n):
    return 1 if n == 0 else a * get_pow(a, n - 1)


print(get_pow(5, 2))
