cubes_of_odds = lambda iterable: (x ** 3 for x in iterable if x % 2)


print(*cubes_of_odds([1, 2, 3, 4, 5]))
