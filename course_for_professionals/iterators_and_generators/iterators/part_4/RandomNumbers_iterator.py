from random import randint


class RandomNumbers:
    def __new__(cls, left, right, n):
        return (randint(left, right) for _ in range(n))


iterator = RandomNumbers(1, 6, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
