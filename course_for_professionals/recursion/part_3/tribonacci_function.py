from functools import cache


@cache
def tribonacci(n):
    if n in (1, 2, 3):
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(7))
