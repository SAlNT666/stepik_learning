from functools import reduce


odds = [int(i) for i in '2 4 3'.split()]
x = 10


def evaluate():
    expression = reduce(lambda x, y: x + y, map(lambda a, n: a * x ** n, odds, sorted(list(range(len(odds))), reverse=True)), 0)
    print(expression)

evaluate()