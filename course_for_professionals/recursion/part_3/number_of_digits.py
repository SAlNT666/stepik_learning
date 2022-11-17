def sum_d(d):
    return 1 if d < 10 else 1 + sum_d(d // 10)


print(sum_d(int(input())))
