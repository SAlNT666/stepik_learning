from collections import Counter


def count_occurences(word, words):
    return words.lower().split().count(word.lower())


from time import monotonic


word = 'python'
words = 'Python Conferences python training python events'

start = monotonic()

for i in range(100_000):
    words.lower().split().count(word.lower())

print(monotonic() - start)

start = monotonic()

for i in range(100_000):
    Counter(words.lower().split())[word.lower()]

print(monotonic() - start)
