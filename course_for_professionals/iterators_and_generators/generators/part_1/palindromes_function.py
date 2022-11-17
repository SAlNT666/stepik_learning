from itertools import count


def palindromes():
    yield from (n for n in count(1) if str(n) == str(n)[::-1])


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
