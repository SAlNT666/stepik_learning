class DictItemsIterator:
    def __new__(cls, data):
        return iter(data.items())


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)
