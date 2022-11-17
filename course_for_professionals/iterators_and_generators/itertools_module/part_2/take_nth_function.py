from itertools import islice


take_nth = lambda iterable, n: next(islice(iterable, n - 1, None), None)


numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 30))
