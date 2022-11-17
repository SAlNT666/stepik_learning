from itertools import pairwise


max_pair = lambda iterable: max(sum(i) for i in pairwise(iterable))


print(max_pair([1, 8, 2, 4, 3]))
