from itertools import groupby
from bisect import bisect_left


# def ranges(numbers):
#     groups = [tuple(r) for _, r in groupby(numbers, key=lambda n: n - bisect_left(numbers, n))]
#     return [(r[0], r[-1]) for r in groups]


def ranges(numbers):
    groups = [tuple(n[1] for n in r) for _, r in groupby(enumerate(numbers), key=lambda x: x[1] - x[0])]
    return [(r[0], r[-1]) for r in groups]


numbers = [1, 2, 4, 7, 8, 10]
print(ranges(numbers))
