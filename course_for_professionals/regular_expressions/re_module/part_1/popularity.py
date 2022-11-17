import sys


tg_word = 'beegeek'
total = 0

for row in [r.rstrip() for r in sys.stdin]:
    if row.startswith(tg_word):
        total += 2 + row.endswith(tg_word)
    elif row.endswith(tg_word):
        total += 2
    elif tg_word in row:
        total += 1

print(total)
