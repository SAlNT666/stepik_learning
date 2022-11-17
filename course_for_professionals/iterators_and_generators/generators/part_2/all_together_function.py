all_together = lambda *args: (e for i in args for e in i)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))
