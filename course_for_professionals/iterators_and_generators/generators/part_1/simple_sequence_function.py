def simple_sequence():
    c = 1
    while True:
        yield from (c for _ in range(c))
        c += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)
