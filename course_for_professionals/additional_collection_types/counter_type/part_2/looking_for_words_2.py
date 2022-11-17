from collections import Counter


words = Counter('арбуз малина клубника арбуз малина клубника'.lower().split())

print(*sorted(w for w in words if words[w] == words.most_common()[-1][1]), sep=', ')
