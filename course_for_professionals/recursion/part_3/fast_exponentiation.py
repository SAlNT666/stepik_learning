def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2:
        return a * get_fast_pow(a, n - 1)
    else:
        return get_fast_pow(a * a, n / 2)


print(get_fast_pow(5, 3))
