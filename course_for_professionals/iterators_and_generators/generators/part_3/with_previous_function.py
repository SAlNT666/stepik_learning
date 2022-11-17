def with_previous(iterable):
    prev = None
    return ((i, prev, prev := i)[:2] for i in iterable)


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))
