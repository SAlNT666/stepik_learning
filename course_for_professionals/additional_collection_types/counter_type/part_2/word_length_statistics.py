from collections import Counter


words_length = Counter(len(i) for i in input().split())
print(*[f'Слов длины {k}: {v}' for k, v in sorted(words_length.items(), key=lambda x: x[1])], sep='\n')
