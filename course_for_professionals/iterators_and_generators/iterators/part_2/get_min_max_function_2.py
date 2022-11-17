def get_min_max(iterable):
    try:
        min_n = max_n = next(iter(iterable))
        for n in iterable:
            if n < min_n:
                min_n = n
            if n > max_n:
                max_n = n
        return min_n, max_n
    except StopIteration:
        return


iterable = iter(range(10))

print(get_min_max(iterable))
