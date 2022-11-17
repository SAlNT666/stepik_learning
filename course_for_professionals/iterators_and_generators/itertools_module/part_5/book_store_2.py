from itertools import product


wallet = [100, 50, 20, 10, 5]
bounds = [100 // v + 1 for v in wallet]

coefficients = product(*[range(b) for b in bounds])
combinations = sum((sum(n * v for n, v in zip(wallet, c)) == 100 for c in coefficients))
print(combinations)
