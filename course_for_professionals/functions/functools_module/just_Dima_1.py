from functools import cache


@cache
def sort_letters(word):
    return ''.join(sorted(word.strip()))


[print(sort_letters(word)) for word in open(0)]
