s = 0
n = 0

for l in open(0):
    try:
        s += float(l)
    except ValueError:
        n += 1

print(int(s) if s % 1 == 0 else s)
print(n)
