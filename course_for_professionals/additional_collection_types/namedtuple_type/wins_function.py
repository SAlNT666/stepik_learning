from collections import defaultdict


def wins(pairs):
    competitors = defaultdict(set)
    [competitors[i].add(j) for i, j in pairs]
    return competitors


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))