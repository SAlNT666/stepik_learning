def zip_longest(*lists, fill=None):
    length = max(len(i) for i in lists)
    return list(zip(*[i + [fill] * (length - len(i)) for i in lists]))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
