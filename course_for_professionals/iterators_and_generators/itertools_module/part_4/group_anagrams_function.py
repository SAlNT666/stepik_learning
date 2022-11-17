from itertools import groupby


group_anagrams = lambda words: (tuple(g[1]) for g in groupby(sorted(words, key=sorted), key=set))

groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)
