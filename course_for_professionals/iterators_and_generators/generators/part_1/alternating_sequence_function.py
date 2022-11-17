from itertools import count


def alternating_sequence(c=None):
    sign = True
    for i in range(1, c + 1) if c else count(1):
        yield i * (-1, 1)[sign]
        sign = not sign


generator = alternating_sequence()

print(next(generator))
print(next(generator))
