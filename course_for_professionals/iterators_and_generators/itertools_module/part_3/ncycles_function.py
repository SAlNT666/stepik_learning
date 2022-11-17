from itertools import tee, chain


ncycles = lambda iterable, times: chain.from_iterable(tee(iterable, times))


print(*ncycles([1, 2, 3, 4], 3))
