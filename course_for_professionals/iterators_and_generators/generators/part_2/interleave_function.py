interleave = lambda *args: (e for i in zip(*args) for e in i)

print(*interleave('bee', '123'))
