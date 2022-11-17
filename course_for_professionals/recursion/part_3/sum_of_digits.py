def sum_d(d):
    return d if d < 10 else d % 10 + sum_d(d // 10)


print(sum_d(int(input())))
