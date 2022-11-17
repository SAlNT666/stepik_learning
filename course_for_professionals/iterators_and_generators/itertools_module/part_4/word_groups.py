from itertools import groupby


for n, w in groupby(sorted(input().split(), key=len), key=len):
    print(f"{n} -> {', '.join(sorted(w))}")
