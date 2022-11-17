from itertools import dropwhile


drop_while_negative = lambda iterable: dropwhile(lambda x: x < 0, iterable)


numbers = [-3, -2, -1, 0, 1, 2, 3]

print(*drop_while_negative(numbers))
