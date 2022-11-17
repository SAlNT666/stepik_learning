def pairwise(iterable):
    it = iter(iterable)
    for i in it:
        for n in it:
            yield i, n
            i = n
        yield i, None


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))
