import functools


data = [set(input().split(', ')) for _ in range(int(input()))]
languages = functools.reduce(set.intersection, data)
print(', '.join(sorted(languages)) if languages else 'Сериал снять не удастся', sep=', ')
