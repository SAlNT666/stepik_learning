words = input().lower().split()
print(max(words, key=lambda x: (words.count(x), x)))
