n, res, i, counter = int(input()), list(), 1, 0
while counter < n:
    res += [i] * i
    counter += i
    i += 1
print(*res[:n])
