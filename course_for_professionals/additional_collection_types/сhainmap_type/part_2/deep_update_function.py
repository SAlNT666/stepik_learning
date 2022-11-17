from collections import ChainMap


def deep_update(chainmap, key, value):
    [d.update({key: value}) for d in chainmap.maps if key in d]
    if key not in chainmap: chainmap[key] = value


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)
