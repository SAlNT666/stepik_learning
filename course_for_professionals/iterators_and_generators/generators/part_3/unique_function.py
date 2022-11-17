def unique(iterable):
    old = set()
    for i in iterable:
        if i not in old:
            old.add(i)
            yield i


data = map(abs, range(-100, 100))

print(*unique(data))
