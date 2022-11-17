from itertools import cycle


def roundrobin(*args):
    args_len = len(args)
    args = cycle(iter(a) for a in args)
    take = lambda args, n: (iter(next(args)) for _ in range(args_len))
    while args_len:
        try:
            for iterable in args:
                yield next(iterable)
        except StopIteration:
            args_len -= 1
            args = cycle(take(args, args_len))


numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))

print(list(roundrobin()))
