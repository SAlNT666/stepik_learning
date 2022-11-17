first_largest = lambda iterable, n: next(filter(lambda x: x[1] > n, enumerate(iterable)), (-1,))[0]


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))
