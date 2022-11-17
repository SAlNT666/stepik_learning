from functools import cache


@cache
def ways(n):
    if n < 2:
        return (1, 0)[n < 1]
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)


print(ways(6))
