from sys import stdin


for i, m in enumerate(stdin):
    ...

print(('Дима', 'Анри')[i % 2 == int(m) % 2])
