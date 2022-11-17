from itertools import pairwise


is_rising = lambda iterable: all(a < b for a, b in pairwise(iterable))


print(is_rising([1, 2, 3, 5, 5]))
