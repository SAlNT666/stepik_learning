from collections import Counter


c = Counter()
with open('pythonzen.txt', encoding='utf-8') as f_in:
    for line in f_in:
        c.update(l for l in line.lower() if l.isalpha())

[print(f'{k}: {v}') for k, v in sorted(c.items())]
