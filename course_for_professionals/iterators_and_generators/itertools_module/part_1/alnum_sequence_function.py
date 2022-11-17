from itertools import cycle
from string import ascii_uppercase


alnum_sequence = lambda: cycle(e for i in enumerate(ascii_uppercase, 1) for e in i)


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))
