def around(iterable):
    it = iter(iterable)
    p = None
    for i in it:
        for n in it:
            yield p, i, n
            p = i
            i = n
        yield p, i, None


numbers = [1, 2, 3, 4, 5]

print(*around(numbers))
