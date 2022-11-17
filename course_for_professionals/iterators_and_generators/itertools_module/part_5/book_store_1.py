from collections import Counter
from itertools import product


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

wallet = Counter(wallet)
coefficients = product(*[range(val+1) for val in wallet.values()])
combinations = sum(sum(n * v for n, v in zip(wallet.keys(), c)) == 100 for c in coefficients)
print(combinations)
