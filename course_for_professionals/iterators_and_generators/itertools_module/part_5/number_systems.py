from itertools import product
from string import ascii_uppercase, digits


n, m = int(input()), int(input())

print(*(''.join(d) for d in product((digits + ascii_uppercase)[:n], repeat=m)))
