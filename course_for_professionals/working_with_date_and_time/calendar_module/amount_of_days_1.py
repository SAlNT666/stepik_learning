from calendar import monthrange


year, month = [int(i) for i in input().split()]

print(monthrange(year, month)[1])
