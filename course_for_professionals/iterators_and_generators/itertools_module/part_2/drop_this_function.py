from itertools import dropwhile


drop_this = lambda iterable, obj: dropwhile(lambda x: x == obj, iterable)


numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))
