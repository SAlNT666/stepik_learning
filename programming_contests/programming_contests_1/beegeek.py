def beegeek(a, b):
    return ' '.join(('Bee' * (i % 3 == 0) + 'Geek' * (i % 7 == 0) or str(i)) for i in range(a, b + 1))

print(beegeek(1, 2))