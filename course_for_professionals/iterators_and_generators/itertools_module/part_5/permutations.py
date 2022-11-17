from itertools import permutations


[print(''.join(p)) for p in sorted(set(permutations(input())))]
